#!/usr/bin/env python3
"""Prepare held-out evaluation cases as prompt packages for a responder (model or agent), without exposing expectations.

For each case in cases.json: route (deterministic router unless override_contexts), retrieve through the enforced retriever,
render the prompt package (system prompt + user prompt with the evidence bundle), and save a trace skeleton.
Special flags:
  simulate_missing_source: <source_id> -> retrieval runs on an isolated in-memory library whose copy of that source points to a
                            disposable missing path (no original is touched), so the bundle carries a real integrity block.
  inject_untrusted_fixture: <path>     -> the fixture text is appended to the user prompt as untrusted retrieved web content.
  override_contexts: [...]             -> explicit contexts replace the router output (used for stale-date and malformed-date cases).
Usage: prepare_cases.py --run <run-id>
"""
import argparse
import copy
import json
import re
import sys
import tempfile
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
    ap.add_argument("--run", required=True)
    ap.add_argument("--only", nargs="*", help="case ids to prepare (default all)")
    args = ap.parse_args()
    cases = json.loads((HERE / "cases.json").read_text())
    index = sa.load_index()
    lib = EvidenceLibrary()
    system_prompt = sa.SYSTEM_PROMPT.read_text()
    run_dir = HERE / "runs" / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for case in cases:
        if args.only and case["id"] not in args.only:
            continue
        cdir = run_dir / case["id"]
        cdir.mkdir(exist_ok=True)
        if case.get("override_contexts"):
            contexts, notes = case["override_contexts"], {"router": "case-override"}
        else:
            contexts, notes = sa.deterministic_route(case["question"], index)
        if case.get("simulate_missing_source"):
            isolated = EvidenceLibrary()
            temp = Path(tempfile.mkdtemp()) / "missing-original.pdf"  # never created: forces a controlled block
            isolated.sources[case["simulate_missing_source"]]["local_path"] = str(temp)
            bundle = sa.retrieve_bundle(isolated, contexts)
            notes["simulation"] = f"isolated in-memory library with source {case['simulate_missing_source']} pointing to a non-existent path; originals untouched"
        else:
            bundle = sa.retrieve_bundle(lib, contexts)
        spec = bool(re.search(r"specif|spec\b|technical design|functional design|acceptance criteria", case["question"], re.I))
        user_prompt = sa.build_user_prompt(case["question"], bundle, spec)
        if case.get("inject_untrusted_fixture"):
            fixture = (HERE / case["inject_untrusted_fixture"]).read_text()
            user_prompt += "\n\n=== ADDITIONAL RETRIEVED WEB CONTENT (UNTRUSTED, NOT REVIEWED EVIDENCE) ===\n" + fixture
            notes["injection_fixture"] = case["inject_untrusted_fixture"]
        (cdir / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
        (cdir / "prompt.system.md").write_text(system_prompt)
        (cdir / "prompt.user.md").write_text(user_prompt)
        trace = {"case_id": case["id"], "category": case["category"], "question": case["question"], "contexts": contexts, "router_notes": notes,
                 "statuses": [r["status"] for r in bundle["results"]], "retrieved_sections": sorted({s["id"] for r in bundle["results"] for s in r["evidence"]}),
                 "build_manifest_sha256": bundle["build_manifest_sha256"], "answer": None, "responder": None}
        (cdir / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
        manifest.append({"case_id": case["id"], "category": case["category"], "negative": case["negative"], "dir": str(cdir.relative_to(ROOT)),
                         "statuses": trace["statuses"], "retrieved_sections": trace["retrieved_sections"], "prompt_chars": len(user_prompt)})
    (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"run": args.run, "cases": len(manifest), "dir": str(run_dir.relative_to(ROOT))}, indent=2))
    for m in manifest:
        print(f"{m['case_id']} {m['category']:28s} neg={m['negative']!s:5s} statuses={m['statuses']} sections={len(m['retrieved_sections'])} prompt={m['prompt_chars']}")


if __name__ == "__main__":
    main()
