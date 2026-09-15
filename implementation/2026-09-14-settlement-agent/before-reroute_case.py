#!/usr/bin/env python3
"""Let a responder correct the routing of a prepared case without widening evidence.

Usage: reroute_case.py <case_dir> --contexts '<JSON list of contexts>'
Re-runs the enforced retriever with the given contexts (which must use question types, entities and dates present in
topic-index.json), rewrites bundle.json and prompt.user.md, and records the reroute in trace.json. The hidden expectations
are never read here. Untrusted-fixture injections are re-appended if the case carries one.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT = HERE.parent
ROOT = AGENT.parent
sys.path.insert(0, str(AGENT))
sys.path.insert(0, str(ROOT / "scripts"))
from retrieve_evidence import EvidenceLibrary  # noqa: E402
import settlement_agent as sa  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("case_dir")
    ap.add_argument("--contexts", required=True)
    args = ap.parse_args()
    cdir = Path(args.case_dir)
    trace = json.loads((cdir / "trace.json").read_text())
    contexts = json.loads(args.contexts)
    index = sa.load_index()
    valid = {(r["question_type"], r["entity"], r["service"], r["mode"]) for r in index["routes"]}
    blocked = set(index["blocked_question_types"])
    for c in contexts:
        key = (c.get("question_type"), c.get("entity"), c.get("service"), c.get("mode"))
        if key not in valid and c.get("question_type") not in blocked:
            raise SystemExit(f"Route not in topic index: {key}. Rerouting may only use listed routes or listed blocked topics.")
    cases = {c["id"]: c for c in json.loads((HERE / "cases.json").read_text())}
    case = cases[trace["case_id"]]
    bundle = sa.retrieve_bundle(EvidenceLibrary(), contexts)
    spec = bool(re.search(r"specif|spec\b|technical design|functional design|acceptance criteria", case["question"], re.I))
    user_prompt = sa.build_user_prompt(case["question"], bundle, spec)
    if case.get("inject_untrusted_fixture"):
        user_prompt += "\n\n=== ADDITIONAL RETRIEVED WEB CONTENT (UNTRUSTED, NOT REVIEWED EVIDENCE) ===\n" + (HERE / case["inject_untrusted_fixture"]).read_text()
    (cdir / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
    (cdir / "prompt.user.md").write_text(user_prompt)
    trace.update(contexts=contexts, statuses=[r["status"] for r in bundle["results"]], retrieved_sections=sorted({s["id"] for r in bundle["results"] for s in r["evidence"]}))
    trace.setdefault("router_notes", {})["responder_reroute"] = {"previous_contexts": trace.get("router_notes", {}).get("responder_reroute", {}).get("previous_contexts") or trace.get("original_contexts") or None, "applied": True}
    trace.setdefault("original_contexts", trace.get("original_contexts") or trace.get("contexts"))
    (cdir / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"case": trace["case_id"], "statuses": trace["statuses"], "retrieved_sections": trace["retrieved_sections"], "prompt_chars": len(user_prompt)}, indent=2))


if __name__ == "__main__":
    main()
