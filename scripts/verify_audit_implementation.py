"""Run scoped retrieval regressions and independent integrity checks; no LLM score."""
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

from retrieve_evidence import EvidenceLibrary

R = Path(__file__).resolve().parents[1]
OUT = R / json.loads((R / "retrieval/section-decisions.json").read_text()).get("verification_output_dir", "implementation/2026-09-13/verification")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    lib = EvidenceLibrary()
    cases = json.loads((R / "retrieval/evaluation-routing.json").read_text())
    # Later snapshots add their own fixture files; the original 34-case fixture stays unchanged.
    extra_files = sorted((R / "retrieval").glob("evaluation-routing-*.json"))
    for extra in extra_files:
        for case in json.loads(extra.read_text()):
            case["fixture"] = extra.name
            cases.append(case)
    results, failures = [], []
    for case in cases:
        actual = lib.retrieve(case["context"])
        ids = {e["id"] for e in actual["evidence"]}
        ok = actual["status"] == case["expected_status"] and set(case["required_section_ids"]).issubset(ids)
        results.append({**case, "actual_status": actual["status"], "retrieved_section_ids": sorted(ids),
                        "retrieved_citations": [c for s in actual["evidence"] for c in s["citations"]],
                        "outcome": "PASS" if ok else "FAIL", "reason": actual["reason"],
                        "llm_answer_evaluation": "NOT_RUN", "actual_model_answer": None})
        if not ok:
            failures.append(case["id"])
    checks = []

    def check(name, condition, detail=""):
        checks.append({"check": name, "outcome": "PASS" if condition else "FAIL", "detail": detail})
        if not condition:
            failures.append(name)

    base = {"as_of": lib.as_of, "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
    check("Missing scope requests context", lib.retrieve({})["status"] == "needs_context")
    check("Non-object context handled", lib.retrieve([])["status"] == "needs_context")
    check("Malformed question type handled", lib.retrieve(dict(base, question_type=["matching_concept"]))["status"] == "needs_context")
    check("Pre-effective business date blocked", lib.retrieve(dict(base, business_date="2025-01-01"))["status"] == "blocked")
    check("Future business date not silently current", lib.retrieve(dict(base, business_date="2027-01-01"))["status"] == "blocked")
    check("Cross-market leakage blocked", lib.retrieve(dict(base, entity="Athens"))["status"] == "blocked")
    check("Wrong actor role blocked", lib.retrieve(dict(base, role="issuer"))["status"] == "blocked")
    check("Wrong service blocked", lib.retrieve(dict(base, service="tax"))["status"] == "blocked")
    check("Calendar rollover does not certify currency", lib.retrieve(dict(base, as_of="2026-09-14"))["status"] == "needs_refresh")
    check("Historical as-of is not inferred", lib.retrieve(dict(base, as_of="2025-01-01"))["status"] == "needs_refresh")
    check("Invalid business date rejected", lib.retrieve(dict(base, business_date="2026-02-30"))["status"] == "needs_context")
    check("Wrong platform release blocked", lib.retrieve(dict(base, entity="T2S", question_type="native_message_overview", release="R2026.NOV"))["status"] == "blocked")
    check("Missing native release requests context", lib.retrieve(dict(base, entity="T2S", question_type="native_message_overview"))["status"] == "needs_context")
    check("Future law excluded from current mode", lib.retrieve(dict(base, entity="EU", service="regulatory", question_type="future_t1"))["status"] == "blocked")
    check("Unreviewed dated events block nominal answer", lib.retrieve(dict(base, entity="T2S", question_type="dated_t2s_schedule", business_date="2026-09-09", currency="EUR"))["status"] == "blocked")
    check("EUR event does not migrate to DKK", lib.retrieve(dict(base, entity="T2S", question_type="dated_t2s_schedule", business_date="2026-09-08", currency="DKK"))["status"] == "blocked")
    check("Local timetable cannot use platform label", lib.retrieve(dict(base, question_type="milan_participant_cutoff"))["status"] == "blocked")
    check("Unspecified cross-CSD chain requests context", lib.retrieve(dict(base, question_type="cross_csd_message_flow"))["status"] == "needs_context")
    oslo = lib.retrieve(dict(base, entity="Oslo", mode="reference", question_type="liquidity_duties"))
    check("Oslo approval dependency follows liquidity description", {"oslo-liquidity", "oslo-edition"}.issubset({s["id"] for s in oslo["evidence"]}))
    milan = " ".join(e["text"] for e in lib.by_id["milan-finality"]["evidence"])
    check("SF2 retains bilateral cancellation exception", "bilaterally" in milan and "without prejudice" in milan and "70 (2)" in milan)
    dora = lib.retrieve(dict(base, entity="EU", service="regulatory", role="csd_operator", question_type="dora_scope"))
    check("English DORA selects English OJ, not French capture", all(c["source_id"] == "dora-english-oj" and c["body_language"] == "en" for s in dora["evidence"] for c in s["citations"]) and bool(dora["evidence"]))
    matrix = json.loads((R / "implementation/2026-09-13/structured/t2s-matching-fields.json").read_text())
    currency = [x for x in matrix["rows"] if x["field"] == "Currency"]
    check("Functional matching preserves FOP cash-field distinction", any(x["FOP"] == "n/a" and x["DVP/DWP"] == "mandatory" for x in currency) and any(x["FOP"] == "additional" for x in currency))
    check("All three visually reviewed matching diagrams retained", Counter(x["diagram"] for x in matrix["rows"]) == Counter({55:13,56:5,57:5}) and all(term in " ".join(matrix["conditions"]) for term in ["ExCoupon", "CumCoupon", "Scheme Name", "case", "EUR 25"]))
    ev = json.loads((R / "implementation/2026-09-13/structured/t2s-events.json").read_text())["events"]
    announced = next(x for x in ev if x["published_time_as_displayed"] == "15:30:00")
    resolved = next(x for x in ev if x["published_time_as_displayed"] == "18:55:00")
    check("Announced IDVP and actual IFOP remain distinct", announced["announced_time"] == "17:00" and announced["actual_completion_time"] is None and resolved["actual_completion_time"] == "18:39" and resolved["supersedes_event_ids"] == ["t2s-20260908-181000"])
    catalogue = json.loads((R / "catalogue.json").read_text())
    curated = json.loads((R / "curated-manifest.json").read_text())
    check("No broad document defaults remain", all(d.get("default_retrieval") is False for d in catalogue + curated["documents"] + curated["legal_texts"]))
    current_export = [json.loads(x) for x in (R/"retrieval/exports/current.jsonl").read_text().splitlines()]
    check("Current export contains no future-only or reference-only sections", bool(current_export) and all("current" in s["modes"] for s in current_export))
    check("French capture correctly tagged", next(x for x in curated["legal_texts"] if x["id"] == "02022R2554-20221227")["actual_content_language"] == "fr")
    originals = json.loads((R / "audits/2026-09-13/evidence/original-hashes.json").read_text())
    byid = {d["id"]: d for d in catalogue}
    changed = [id for id, expected in originals.items() if sha(R/byid[id]["local_path"]) != expected]
    check("All 800 original documents preserved", len(originals) == 800 and not changed, str(changed))
    arcs = json.loads((R / "implementation/2026-09-13/structured/archive-members.json").read_text())
    check("All 14 containers staged without admission", len(arcs) == 14 and all(not m["admitted"] for a in arcs for m in a["members"]))
    check("Mislabelled XLSX identified by content", sum(a["detected_type"] == "xlsx" for a in arcs) == 1)
    check("Staged members match their content hashes", all(sha(R/m["staged_path"]) == m["sha256"] for a in arcs for m in a["members"] if m.get("staged_path")))
    for name in ["finalize_library.py", "write_research.py", "collect_sources.py", "build_library.py", "supplement_library.py", "list_sources_in_use.py"]:
        run = subprocess.run(["python3", str(R/"scripts"/name)], capture_output=True, text=True)
        check("Historical writer guarded: " + name, run.returncode != 0 and "Historical snapshot builder stopped" in run.stderr)
    # Mutate disposable copies only; the actual source archive is never edited.
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        (temp/"retrieval").mkdir()
        shutil.copyfile(R/"retrieval/build-manifest.json", temp/"retrieval/build-manifest.json")
        for name in json.loads((R/"retrieval/build-manifest.json").read_text())["files"]:
            dest = temp/name; dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R/name, dest)
        with (temp/"retrieval/admitted-sections.jsonl").open("a") as f:
            f.write("{}\n")
        caught = False
        try:
            EvidenceLibrary(temp)
        except ValueError:
            caught = True
        check("Changed export rejected", caught)
        # Point a fresh in-memory library to a deliberately altered disposable original.
        other = EvidenceLibrary()
        altered = temp/"altered.pdf"; altered.write_bytes(b"not the reviewed source")
        other.sources["8719262f5e8b"]["local_path"] = str(altered)
        check("Changed selected original blocks retrieval", other.retrieve(base)["status"] == "blocked")
    summary = {"evidence_as_of": lib.as_of, "build_manifest_sha256": sha(R/"retrieval/build-manifest.json"),
               "routing_cases": len(results), "routing_passed": sum(x["outcome"] == "PASS" for x in results),
               "routing_cases_original_fixture": sum(1 for x in results if not x.get("fixture")),
               "routing_cases_by_fixture": dict(Counter(x.get("fixture", "evaluation-routing.json") for x in results)),
               "routing_actual_statuses": dict(Counter(x["actual_status"] for x in results)),
               "integrity_checks": len(checks), "integrity_passed":sum(x["outcome"] == "PASS" for x in checks),
               "originals_verified_unchanged": len(originals)-len(changed), "failures": failures,
               "llm_answer_evaluation": "NOT_RUN — no language-model answer service is deployed",
               "scope": "Manual question routing, actual local evidence selection and controls. Not semantic answer accuracy or production readiness."}
    (OUT/"retrieval-results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2)+"\n")
    (OUT/"verification.json").write_text(json.dumps({"summary":summary,"checks":checks}, ensure_ascii=False, indent=2)+"\n")
    lines=["# Implementation verification", "", "These are actual local evidence-selection and integrity results. The audit's original expected-answer fixtures remain unchanged; no LLM answer-quality evaluation was run.", "", "```json", json.dumps(summary,indent=2), "```", "", "| Case | Routing result | Retrieved sections |", "|---|---|---|"]
    lines += [f"| {x['id']} | {x['outcome']}: {x['actual_status']} | {', '.join(x['retrieved_section_ids']) or 'None — blocked'} |" for x in results]
    (OUT/"VERIFICATION.md").write_text("\n".join(lines)+"\n")
    print(json.dumps(summary, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
