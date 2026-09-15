"""Companion code change for snapshot revision v1.1 (apply together with scripts/patch_settlement_agent_snapshot_v1_1.py).

Adds a dedicated candidate path in scripts/retrieve_evidence.py for question_type `t2s_status_history`: dated ECB status
entries (event-scope sections) become retrievable on their own for a business date and currency, without pulling the
nominal baseline schedule. The nominal `dated_t2s_schedule` route is unchanged. Guarded: applies once.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "scripts/retrieve_evidence.py"
OLD = '''        matching_scope = [s for s in self.sections if topic in s["question_types"] and scope_without_date(s)]
        candidates = [s for s in matching_scope if scoped(s) and not s.get("event_scope")]
        if not candidates:
'''
NEW = '''        matching_scope = [s for s in self.sections if topic in s["question_types"] and scope_without_date(s)]
        if topic == "t2s_status_history":
            # Revision v1.1 (14 September 2026): dated status entries are retrievable on their own. They need the business
            # date and currency, match the event scope exactly (or a reviewed currency-neutral "ALL" scope) and do not
            # pull in the nominal baseline, which the dated_t2s_schedule route continues to govern.
            missing = [k for k in ["business_date", "currency"] if not context.get(k)]
            if missing:
                return result("needs_context", "Dated status history requires business date and currency.", missing_fields=missing)
            dated = [s for s in matching_scope if scoped(s) and s.get("event_scope")]
            candidates = [s for s in dated if self._overlay_matches(s["event_scope"], s["event_scope"].get("schedule_model"), context)]
            if dated and not candidates:
                return result("blocked", "No reviewed status entry for this business date and currency. Absence from the reviewed capture is not evidence of routine operations.", gap_ids=["G02"])
        else:
            candidates = [s for s in matching_scope if scoped(s) and not s.get("event_scope")]
        if not candidates:
'''


def main():
    text = PATH.read_text()
    if NEW in text:
        raise SystemExit("retriever v1.1 change already applied.")
    assert OLD in text, "expected candidate-filter block not found; inspect scripts/retrieve_evidence.py"
    PATH.write_text(text.replace(OLD, NEW, 1))
    print("applied retriever v1.1 change to", PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()
