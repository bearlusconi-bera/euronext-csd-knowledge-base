#!/usr/bin/env python3
"""Two commands for the evaluation run.

judge-prompts --run <id> : for each case with an answer.md, write judge-prompt.md (question, hidden expectations, rubric,
                           the answer, and the actual retrieved passages). A separate model instance answers it with a JSON
                           verdict saved as judge.json in the case folder.
aggregate --run <id>     : run the deterministic checks on every answer, read judge.json where present, compare retrieved
                           sections/statuses with expectations, and write results.json plus results.md.
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT = HERE.parent
ROOT = AGENT.parent
sys.path.insert(0, str(AGENT))
import settlement_agent as sa  # noqa: E402

# Judge prompts carry the complete bundle. The first judging pass of run 2026-09-14-r1 used 120000 characters, which truncated
# case E07; the limit was raised on 14 September 2026 and E07 was re-judged (the truncated first verdict is kept as
# judge.truncated-first-pass.json).
JUDGE_BUNDLE_MAX_CHARS = 600000
DIMENSIONS = ["routing_scope", "evidence_selection", "citation_entailment_locators", "preserved_qualifications", "completeness", "no_unsupported_claims", "justified_abstention", "label_discipline"]


def judge_prompt(case, expected, answer, bundle):
    rubric = (HERE / "RUBRIC.md").read_text()
    return f"""You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
{case['question']}

# Case category: {case['category']} ({'negative — the right behaviour is a limited or declined answer' if case['negative'] else 'positive — evidence should support a useful answer'})

# Hidden expectations (never shown to the responder)
Key points expected:
{json.dumps(expected.get('key_points', []), ensure_ascii=False, indent=2)}
Fail conditions (must NOT appear):
{json.dumps(expected.get('must_not', []), ensure_ascii=False, indent=2)}
Expected sections (if any): {expected.get('expected_sections', [])}
Expected retrieval statuses: {expected.get('expected_statuses', [])}

# Rubric
{rubric}

# The answer under review
<<<ANSWER
{answer}
ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
{sa.bundle_for_prompt(bundle, max_chars=JUDGE_BUNDLE_MAX_CHARS)}

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{{"scores": {{"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n}},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{{"citation": "...", "problem": "...", "passage_quote": "..."}}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}}
"""


def cmd_judge_prompts(args):
    run_dir = HERE / "runs" / args.run
    cases = {c["id"]: c for c in json.loads((HERE / "cases.json").read_text())}
    expected = json.loads((HERE / "cases-expected.json").read_text())
    n = 0
    for cdir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        ans = cdir / "answer.md"
        if not ans.exists():
            continue
        case = cases[cdir.name]
        bundle = json.loads((cdir / "bundle.json").read_text())
        (cdir / "judge-prompt.md").write_text(judge_prompt(case, expected.get(cdir.name, {}), ans.read_text(), bundle))
        n += 1
    print(json.dumps({"run": args.run, "judge_prompts_written": n}))


def verdict_from(scores, violations):
    if not scores:
        return "NOT_RUN"
    if violations or any(v == 0 for v in scores.values()):
        return "fail"
    if all(scores.get(d) == 2 for d in ["citation_entailment_locators", "preserved_qualifications", "no_unsupported_claims"]):
        return "pass"
    return "partial"


def cmd_aggregate(args):
    run_dir = HERE / "runs" / args.run
    cases = {c["id"]: c for c in json.loads((HERE / "cases.json").read_text())}
    expected = json.loads((HERE / "cases-expected.json").read_text())
    rows = []
    for cdir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        case = cases[cdir.name]
        exp = expected.get(cdir.name, {})
        trace = json.loads((cdir / "trace.json").read_text())
        bundle = json.loads((cdir / "bundle.json").read_text())
        retrieved = set(trace["retrieved_sections"])
        statuses = set(trace["statuses"])
        routing = {"expected_sections_present": sorted(set(exp.get("expected_sections", [])) & retrieved), "expected_sections_missing": sorted(set(exp.get("expected_sections", [])) - retrieved),
                   "expected_statuses_seen": sorted(set(exp.get("expected_statuses", [])) & statuses), "unexpected_statuses": sorted(statuses - set(exp.get("expected_statuses", [])))}
        routing["routing_ok"] = not routing["expected_sections_missing"] and bool(routing["expected_statuses_seen"] or not exp.get("expected_statuses"))
        responder = json.loads((cdir / "responder.json").read_text()) if (cdir / "responder.json").exists() else trace.get("responder")
        row = {"case_id": cdir.name, "category": case["category"], "negative": case["negative"], "statuses": trace["statuses"], "retrieved_sections": trace["retrieved_sections"], "routing": routing,
               "rerouted_by_responder": bool(trace.get("router_notes", {}).get("responder_reroute")), "responder": responder, "deterministic": None, "judge": None, "final": "NOT_RUN"}
        ans = cdir / "answer.md"
        if ans.exists():
            answer = ans.read_text()
            det = sa.check_answer(answer, bundle, case["question"])
            (cdir / "checks.json").write_text(json.dumps(det, ensure_ascii=False, indent=2) + "\n")
            row["deterministic"] = det["summary"]
            jp = cdir / "judge.json"
            if jp.exists():
                j = json.loads(jp.read_text())
                row["judge"] = {"scores": j.get("scores"), "verdict": j.get("verdict"), "recomputed_verdict": verdict_from(j.get("scores", {}), j.get("must_not_violations")),
                                "must_not_violations": j.get("must_not_violations", []), "key_points_missing": j.get("key_points_missing", []), "citation_problems": j.get("citation_problems", []),
                                "unsupported_claims": j.get("unsupported_claims", []), "reason": j.get("reason")}
                final = row["judge"]["recomputed_verdict"]
                if det["summary"]["failed"]:
                    final = "fail" if final == "fail" else "partial"
                row["final"] = final
            else:
                row["final"] = "JUDGE_NOT_RUN"
        rows.append(row)
    total = len(rows)
    judged = [r for r in rows if r["final"] in ("pass", "partial", "fail")]
    summary = {"run": args.run, "cases": total, "answered": sum(1 for r in rows if r["deterministic"]), "judged": len(judged),
               "pass": sum(1 for r in judged if r["final"] == "pass"), "partial": sum(1 for r in judged if r["final"] == "partial"), "fail": sum(1 for r in judged if r["final"] == "fail"),
               "negative_cases": sum(1 for r in rows if r["negative"]), "routing_ok": sum(1 for r in rows if r["routing"]["routing_ok"]),
               "deterministic_all_pass": sum(1 for r in rows if r["deterministic"] and not r["deterministic"]["failed"]),
               "responders": sorted({json.dumps(r["responder"], sort_keys=True) for r in rows if r["responder"]})}
    out = {"summary": summary, "rows": rows}
    (run_dir / "results.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    lines = [f"# Evaluation run {args.run}", "", "```json", json.dumps(summary, indent=2), "```", "",
             "| Case | Category | Neg | Statuses | Routing | Deterministic failed | Judge scores (r,e,c,q,cp,u,a,l) | Final |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        js = r["judge"]["scores"] if r["judge"] and r["judge"].get("scores") else {}
        sc = ",".join(str(js.get(d, "-")) for d in DIMENSIONS) if js else "-"
        det = ",".join(r["deterministic"]["failed"]) if r["deterministic"] else "-"
        lines.append(f"| {r['case_id']} | {r['category']} | {'Y' if r['negative'] else ''} | {','.join(r['statuses'])} | {'ok' if r['routing']['routing_ok'] else 'missing ' + ','.join(r['routing']['expected_sections_missing']) or 'check'} | {det or 'none'} | {sc} | {r['final']} |")
    (run_dir / "results.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(summary, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("judge-prompts"); p.add_argument("--run", required=True); p.set_defaults(fn=cmd_judge_prompts)
    p = sub.add_parser("aggregate"); p.add_argument("--run", required=True); p.set_defaults(fn=cmd_aggregate)
    a = ap.parse_args(); a.fn(a)


if __name__ == "__main__":
    main()
