"""Revision v1.1 of the 2026-09-14 settlement-agent snapshot: make dated ECB status entries reachable on their own.

Finding (evaluation run 2026-09-14-r1, case E32): a dated question for a business date before 14 June 2026 is blocked on the
`dated_t2s_schedule` route because the only reviewed baseline schedule (R2026.JUN) was not yet effective, and the then-applicable
baseline (R2025.NOV) is not reviewed. That block is correct for the nominal schedule, but it also made the admitted ECB status
entries for those dates unreachable. This revision adds a dedicated route `t2s_status_history` on every 14 September overlay
(and the routine-only list) that returns only the dated entries, and removes the overlays' hard dependency on the baseline so the
baseline is pulled in through the schedule logic instead. It does not change any 13 September section or any evidence text.
Guarded: runs once. Rebuild, verify and package afterwards.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = "2026-09-14-settlement-agent-v1.1"


def main():
    path = ROOT / "retrieval/section-decisions.json"
    config = json.loads(path.read_text())
    if config.get("snapshot_revision") == REVISION:
        raise SystemExit("v1.1 already recorded.")
    assert config.get("snapshot_revision") == "2026-09-14-settlement-agent-v1", "v1.1 applies on top of v1 only"
    changed = []
    for s in config["sections"]:
        if s["verified_as_of"] == "2026-09-14" and s.get("event_scope") and s["event_scope"].get("schedule_model") == "T2S":
            if "t2s_status_history" not in s["question_types"]:
                s["question_types"].append("t2s_status_history")
            s["dependency_ids"] = [d for d in s["dependency_ids"] if d != "t2s-schedule-r2"]
            s["limitations"].append("Retrievable on its own through t2s_status_history (14 September revision v1.1); the nominal baseline is added only when the dated_t2s_schedule route applies and the reviewed baseline was effective on that date.")
            changed.append(s["id"])
    config["snapshot_revision"] = REVISION
    config.setdefault("snapshot_admissions", {})["2026-09-14"]["revisions"] = [{"revision": REVISION, "reason": "Make admitted dated ECB entries reachable for business dates before the reviewed baseline's effective date; no evidence text changed.", "sections": changed}]
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    admission_path = ROOT / "implementation/2026-09-14-settlement-agent/source-admission.json"
    admission = json.loads(admission_path.read_text())
    admission.setdefault("revisions", []).append({"revision": REVISION, "sections": changed, "evidence_changed": False})
    admission_path.write_text(json.dumps(admission, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"revision": REVISION, "sections_changed": len(changed)}))


if __name__ == "__main__":
    main()
