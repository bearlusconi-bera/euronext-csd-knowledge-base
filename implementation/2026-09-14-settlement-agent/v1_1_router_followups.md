# Router revision v1.1 — follow-up edits after the patch script

`v1_1_router_patch.py` was applied on 14 September 2026 after evaluation run 2026-09-14-r1 was frozen. Three small follow-up edits were then made directly in `settlement-expert-agent/settlement_agent.py` (all router-only; no retriever, evidence or verification change):

| Step | Edit | 46-question regression (maintainer check against `cases-expected.json`, not held-out) | Fresh-paraphrase smoke (`evaluation/router-smoke-2026-09-14-v1_1.json`) |
|---|---|---|---|
| r1 router (v1) | — | 29/46 (four empty bundles: E18, E29, E41, E42) | — |
| patch script applied | patterns for blocked topics and CSD routes, T2S fallback, dated status route, future-date and relative-date handling, deployed-release default | 41/46 | 11/14 |
| follow-up 1 | wording additions: participant cut-off ("by what time", "hand over"), Porto/inter-CSD links ("connected to", "inter-CSD"), matching fields ("agree on", "amounts differ"); November comparison pattern tightened (no bare "differ") | 41/46 | 14/14 |
| follow-up 2 | special-purpose contexts (dated status entries, release status, Milan November plan, EU definitions, swap boundaries) keep their slots under the 8-context cap | 42/46 | 14/14 |
| follow-up 3 | a route whose sections are already covered by chosen contexts is skipped (frees slots for specification questions) | 44/46 | 14/14 |

Remaining two misses are not router defects: E11 simulates a missing source file (its expected block appears only in the prepared evaluation package), and E32 expects the nominal baseline for 14 April 2026, which is blocked by design because the baseline then in force (R2025.NOV) is not reviewed; the dated ECB entry for that day is now returned through `t2s_status_history`.

Regression run 2026-09-14-r2 (12 cases) was prepared with the router at the "patch script applied" state (41/46), before follow-ups 1–3. The pre-v1.1 router is preserved in `v1_1-before/settlement_agent.py`.

| follow-up 4 (after r2 responders reported off-topic retrievals in E41/E42) | `release_status` is added for a future business date only when a schedule route is in play; the T2S schedule/cycle routes are not substituted for a named CSD's missing timetable when a CSD-specific blocked topic fired (local schedules do not inherit T2S timing); blocked contexts carry the latest review date | see below | see below |

`SYSTEM-PROMPT.md` gained one sentence at the same time: a retrieved section that does not bear on the question need not be cited and is listed as "Retrieved but not used" (the r2 responders read the checker's informational `uncited_retrieved` list as an obligation to cite irrelevant material).
