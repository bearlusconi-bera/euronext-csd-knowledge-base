# Settlement Expert Agent snapshot — 14 September 2026

Authorised by the user's build prompt (`CLAUDE-SETTLEMENT-EXPERT-BUILD-PROMPT.md`). Research date and intended operational date: 14 September 2026.

1. **Inspect** the existing library, retriever, audits, repairs and dependencies before changing anything (done first; all four verification scripts passed on the 14 September repair build).
2. **Discover and refresh**: re-fetch the 26 registered sources and the official hubs into `recheck/` and `hubs/`; chase the Milan notice chain, dated ECB events, November publication/deployment and the known gaps; record every route, version, selection, exclusion and unresolved dependency in `DISCOVERY-LOG.md`.
3. **Curate**: read the candidate pages, check layout-sensitive tables against rendered images, build structured derivatives (X-TRM tables, dated ECB entries with labelled business-date attribution, June-vs-November comparison), and record 93 bounded sections and 25 source identities through the guarded `scripts/admit_settlement_agent_snapshot.py`. Preserve every original and the historical audit outputs; the 13 September sections are untouched.
4. **Retriever extensions** (minimal): currency-neutral `ALL` overlays and reviewed lists of routine business dates; nine additional blocked topics mapped to audit gaps; verifiers read the configured output directory and a dated successor replaces the repair-state check "14 September current export is empty"; new routing fixture with 79 cases alongside the unchanged 34.
5. **Agent**: `settlement-expert-agent/` with the runnable pipeline (topics, route, retrieve, ask, check), system prompt, specification template, retrieval contract, agent spec, coverage register and README.
6. **Verify**: rebuild, run both verifiers and package; then a 46-case held-out end-to-end evaluation with separate responder and judge model instances, deterministic checks and maintainer inspection; report retrieval and generated-answer performance separately (`settlement-expert-agent/evaluation/EVALUATION-REPORT.md`).
7. **Handover**: what exists, how to use it, supported topics and dates, actual results, and the prioritised blockers.

Runtime note: the Claude Code CLI headless runtime could not be exercised because its stored login had expired (`runtime-check.json`); the evaluation used Claude Code subagents as the model runtime. No hosted service, monitor or external deployment was created and no party was contacted.

Revision log: v1 (admissions, 14 September); v1.1 (applied after evaluation run 2026-09-14-r1 was frozen: dated ECB entries reachable through `t2s_status_history` via `scripts/patch_settlement_agent_snapshot_v1_1.py` and `v1_1_retriever_patch.py`; router revision `v1_1_router_patch.py` after run r1 showed 29/46 prepared routes; system prompt without seeded values; reroute-trace fix; rebuilt, verified and packaged again — build manifest `ed577c2e…`; pre-v1.1 files in `v1_1-before/`; regression run 2026-09-14-r2).
