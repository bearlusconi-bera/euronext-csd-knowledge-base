#!/usr/bin/env python3
"""Post-hoc trace repair for evaluation run 2026-09-14-r1 (maintainer, 14 September 2026).

reroute_case.py (as used during run r1) overwrote trace["contexts"] before recording trace["original_contexts"], so for
every case a responder rerouted, original_contexts mirrors the corrected contexts and previous_contexts is null. The prepared
contexts are recomputable: prepare_cases.py derived them deterministically from the question with the same topic index
(build manifest unchanged during the run), or took them from the case's override_contexts. This script records them under
"original_contexts_recovered" with a note and leaves every other field untouched. It never touches answers or judgements.
Usage: recover_original_contexts.py --run 2026-09-14-r1
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT = HERE.parent
sys.path.insert(0, str(AGENT))
import settlement_agent as sa  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    cases = {c["id"]: c for c in json.loads((HERE / "cases.json").read_text())}
    index = sa.load_index()
    run_dir = HERE / "runs" / args.run
    repaired = []
    for cdir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        tpath = cdir / "trace.json"
        trace = json.loads(tpath.read_text())
        rr = trace.get("router_notes", {}).get("responder_reroute")
        if not rr or not rr.get("applied") or "original_contexts_recovered" in trace:
            continue
        case = cases[trace["case_id"]]
        if case.get("override_contexts"):
            original = case["override_contexts"]
            how = "case override_contexts"
        else:
            original, _notes = sa.deterministic_route(case["question"], index)
            how = "deterministic_route(question) with the unchanged topic index (build manifest " + trace.get("build_manifest_sha256", "")[:12] + ")"
        trace["original_contexts_recovered"] = original
        trace["original_contexts_note"] = ("Recovered post hoc by the maintainer on 2026-09-14: reroute_case.py recorded original_contexts after overwriting "
                                           "contexts, so the stored original_contexts equals the rerouted contexts. Recovered via " + how + ".")
        tpath.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
        repaired.append({"case": trace["case_id"], "original_contexts": len(original), "rerouted_contexts": len(trace["contexts"])})
    print(json.dumps({"run": args.run, "repaired": repaired}, indent=2))


if __name__ == "__main__":
    main()
