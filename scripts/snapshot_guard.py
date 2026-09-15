"""Prevent historical snapshot builders from overwriting reviewed audit controls."""
def refuse_audited_snapshot(root):
    if (root / "retrieval/section-decisions.json").exists():
        raise SystemExit("Historical snapshot builder stopped: this library has reviewed section controls. Refresh into a new snapshot; use build_retrieval.py to rebuild reviewed exports. No files changed.")
