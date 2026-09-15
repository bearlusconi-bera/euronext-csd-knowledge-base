"""Replay the preserved audit, then test repair-specific temporal and provenance rules."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from retrieve_evidence import EvidenceLibrary

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "implementation/2026-09-14/verification"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    audit_path = ROOT / "audits/2026-09-14-adversarial"
    spec = importlib.util.spec_from_file_location("preserved_adversarial_audit", audit_path / "scripts/run_adversarial.py")
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    # Redirect output only. The original case generator and assertions are unchanged.
    audit.AUDIT = OUT / "adversarial"
    (audit.AUDIT / "evidence").mkdir(parents=True, exist_ok=True)
    with contextlib.redirect_stdout(io.StringIO()):
        audit.main()
    replay = json.loads((audit.AUDIT / "summary.json").read_text())
    same_cases = json.loads((audit.AUDIT / "cases.json").read_text()) == json.loads((audit_path / "cases.json").read_text())
    lib = EvidenceLibrary()
    base = dict(as_of="2026-09-13", entity="T2S", service="settlement", role="participant", mode="current")
    checks = []

    def check(name, condition):
        checks.append({"name": name, "outcome": "PASS" if condition else "FAIL"})

    def get(**kw):
        return lib.retrieve(dict(base, **kw))

    def ids(result):
        return {s["id"] for s in result["evidence"]}

    check("Original 31 case definitions unchanged", same_cases)
    actual = get(question_type="t2s_baseline_schedule", business_date="2026-09-08", currency="EUR")
    check("Date supplied on baseline route defaults to actual and includes overlay", actual["schedule_kind"] == "actual" and "t2s-events-sep08" in ids(actual))
    nominal = get(question_type="business_day_timeline", business_date="2026-09-09", schedule_kind="baseline")
    check("Explicit nominal baseline stays usable and labelled", nominal["status"] == "evidence_only" and nominal["schedule_kind"] == "baseline" and ids(nominal) == {"t2s-schedule"})
    check("Actual question cannot silently change into baseline", get(question_type="dated_t2s_schedule", business_date="2026-09-08", currency="EUR", schedule_kind="baseline")["status"] == "needs_context")
    check("Actual scope requires a business date", get(question_type="business_day_timeline", schedule_kind="actual", currency="EUR")["status"] == "needs_context")
    check("Actual scope requires currency", get(question_type="business_day_timeline", business_date="2026-09-08")["status"] == "needs_context")
    check("Unknown schedule scope rejected", get(question_type="business_day_timeline", schedule_kind="assume-normal")["status"] == "needs_context")
    check("Local actual schedule cannot inherit T2S overlay", get(entity="Copenhagen", question_type="business_day_timeline", business_date="2026-09-08", currency="EUR")["status"] == "blocked")
    inherited = EvidenceLibrary()
    synthetic = copy.deepcopy(inherited.by_id["t2s-posting"])
    synthetic.update(id="test-timeline-wrapper", question_types=["nested_timeline"], dependency_ids=["t2s-schedule"])
    inherited.sections.append(synthetic)
    inherited.by_id[synthetic["id"]] = synthetic
    wrapped = inherited.retrieve(dict(base, question_type="nested_timeline", business_date="2026-09-09", currency="EUR"))
    check("Schedule reached through a dependency also requires an event overlay", wrapped["status"] == "blocked")
    check("Empty business date rejected", get(question_type="business_day_timeline", business_date="")["status"] == "needs_context")
    check("Compact ISO date rejected", get(question_type="business_day_timeline", business_date="20260908")["status"] == "needs_context")
    final = get(as_of="2026-09-14", question_type="release_status", mode="reference", release="R2026.NOV")
    check("14 September query selects only final-publication evidence", final["status"] == "evidence_only" and ids(final) == {"november-final-release"})
    check("Reported evidence date matches scoped review", final["knowledge_as_of"] == "2026-09-14" and all(s["verified_as_of"] == "2026-09-14" for s in final["evidence"]))
    check("Final-publication source provenance is dated 14 September", all(c["source_verified_as_of"] == "2026-09-14" for s in final["evidence"] for c in s["citations"]))
    check("Final publication is not production deployment", final["evidence"][0]["publication_status"] == "final_published" and any("deployment is not verified" in x for x in final["evidence"][0]["limitations"]))
    old = get(question_type="release_status", mode="reference", release="R2026.NOV")
    check("13 September query retains its historical draft evidence", ids(old) == {"november-release"} and old["evidence"][0]["publication_status"] == "market_review_draft_at_review_date")
    check("Later publication source cannot leak into older query", not any(c["source_verified_as_of"] > "2026-09-13" for s in old["evidence"] for c in s["citations"]))
    check("Unknown release blocked in new review date", get(as_of="2026-09-14", question_type="release_status", mode="reference", release="R2099.NOV")["status"] == "blocked")
    check("New publication review does not refresh operational evidence", get(as_of="2026-09-14", entity="Milan", question_type="matching_concept")["status"] == "needs_refresh")
    check("Final November text cannot enter current operational mode", get(as_of="2026-09-14", question_type="release_status", mode="current", release="R2026.NOV")["status"] == "blocked")
    for entity, topic in [("Copenhagen", "dcp_admission"), ("Porto", "dcp_relationship")]:
        answer = get(entity=entity, question_type=topic)
        check(entity + " current evidence is explicitly a publication description", answer["evidence"][0]["applicability_basis"] == "publication_description" and any("operative effective date is not established" in x for x in answer["evidence"][0]["limitations"]))
        check(entity + " publication description does not establish historical duties", get(entity=entity, question_type=topic, business_date="2026-09-12")["status"] == "blocked")
    ctx = dict(base, entity="Milan", question_type="finality")
    command = subprocess.run([sys.executable, str(ROOT / "scripts/retrieve_evidence.py"), "--context", json.dumps(ctx), "--summary"], capture_output=True, text=True, check=True)
    answer = json.loads(command.stdout)
    check("Summary CLI preserves authoritative language and translation", all(c["authoritative_language"] == "it" and "translation" in c["translation_status"] for s in answer["evidence"] for c in s["citations"]))
    with tempfile.TemporaryDirectory() as temp:
        other = EvidenceLibrary()
        derivative = next(e for e in other.by_id["t2s-matching"]["extracts"] if e.get("path"))
        derivative["path"] = str(Path(temp) / "missing.json")
        check("Missing structured derivative blocks without an exception", other.retrieve(dict(base, question_type="matching_fields"))["status"] == "blocked")
    manifest = json.loads((ROOT / "retrieval/build-manifest.json").read_text())
    check("Tested build binds retrieval implementation bytes", "scripts/retrieve_evidence.py" in manifest["files"])
    partitions = [p for d in lib.review_dates for p in (ROOT / "retrieval/exports" / d).glob("*.jsonl")]
    check("Date-partitioned exports contain only their exact review date", len(partitions) == 6 and all(
        json.loads(line)["verified_as_of"] == p.parent.name for p in partitions for line in p.read_text().splitlines()))
    check("14 September current-operational export is deliberately empty", (ROOT / "retrieval/exports/2026-09-14/current.jsonl").read_text() == "")
    preserved = json.loads((ROOT / "implementation/2026-09-14/historical-evidence-hashes.json").read_text())
    changed = [name for name, expected in preserved.items() if sha(ROOT / name) != expected]
    check("All historical audit/evaluation files preserved", not changed)
    summary = {"adversarial_cases": replay["new_adversarial_total"], "adversarial_passed": replay["new_adversarial_passed"],
               "repair_checks": len(checks), "repair_checks_passed": sum(c["outcome"] == "PASS" for c in checks),
               "changed_historical_files": changed, "build_manifest_sha256": sha(ROOT / "retrieval/build-manifest.json"),
               "failures": [c["name"] for c in checks if c["outcome"] != "PASS"],
               "llm_answer_evaluation": "NOT_RUN"}
    if summary["adversarial_passed"] != summary["adversarial_cases"]:
        summary["failures"].append("Adversarial replay has failing cases")
    (OUT / "repair-verification.json").write_text(json.dumps({"summary": summary, "checks": checks}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    if summary["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
