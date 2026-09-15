# Settlement Expert Agent — specification

Version 2026-09-14, revision v1.1 (snapshot `2026-09-14-settlement-agent-v1.1`; evidence unchanged since v1). Research date and intended operational date: 14 September 2026. Base operational evidence review: 13 September 2026; additional evidence reviewed 14 September 2026. Evaluation run 2026-09-14-r1 was executed on v1 (build manifest `f9493d10…`); revision v1.1 (build manifest `ed577c2e…`) followed its findings and was regression-checked in run 2026-09-14-r2 (see §9).

## 1. Purpose and scope

A research and specification assistant for securities settlement at Euronext Securities Milan (priority), Copenhagen, Porto, Athens and Oslo, and for TARGET2-Securities (T2S), with the EU legal frame (CSDR, Settlement Finality Directive, settlement-discipline RTS, RTS 2017/392 definitions). It answers explanatory questions and drafts functional/technical specifications, always from reviewed excerpts, with citations, qualifications and explicit gaps.

It is **not** a production-specification authority: the library holds bounded excerpts of public documents. Client-only specifications (Milan X-TRM standards, Copenhagen User Guidelines, Porto STD appendices, Athens DSS announcements, MyStandards schemas), per-ISIN eligibility, fees and participant-specific cut-offs are outside reviewed evidence and are blocked by design.

## 2. Architecture

```
question ──► router ──► explicit contexts ──► scripts/retrieve_evidence.py ──► evidence bundle ──► composer (model) ──► answer
                │                                    (all controls enforced here)          │                    │
        topic-index.json                                                           SYSTEM-PROMPT.md      check_answer()
```

| Layer | Implementation | Trust level |
|---|---|---|
| Evidence library | `retrieval/section-decisions.json`, `source-register.json`, `admitted-sections.jsonl`, hash-bound build manifest; 124 sections from 51 source identities after this snapshot | Reviewed, hash-verified |
| Retriever | `scripts/retrieve_evidence.py` (unchanged contract; extensions: currency-neutral `ALL` overlays and reviewed lists of routine business dates; nine additional blocked topics mapped to audit gaps; v1.1: question type `t2s_status_history` returns the reviewed dated ECB status entries on their own for a business date and currency, without the nominal baseline) | Deterministic enforcement |
| Topic index | `settlement_agent.py topics` derives `topic-index.json` from the current build: 172 routes (question type × entity × service × mode), 18 blocked topics, context vocabulary | Derived; not evidence |
| Router | Deterministic keyword router in `settlement_agent.py route` (revision v1.1: keyword triggers for blocked topics, CSD-specific patterns for Athens/Oslo/Copenhagen/Porto/EU routes, T2S platform fallback when a question names only a CSD, dated status entries alongside dated schedule questions, baseline-plus-release-status for future dates, deployed-release default for message routes, relative-date handling; assumptions recorded under `_assumed`/`_note`); a model router may replace it but must pick listed routes | Advisory; cannot create evidence |
| Composer | Model runtime with `SYSTEM-PROMPT.md`: `cli` (Claude Code CLI headless), `api` (Anthropic Messages API), or `manual`/agent (prompt package) | Untrusted output, checked |
| Checker | `settlement_agent.py check`: citations ⊆ bundle, status disclosure, governing-language and publication-description qualifications, review date, unsupported clock times/message versions/EUR amounts/XML, label discipline | Deterministic; pattern-based |
| Trace | `traces/<stamp>/` with bundle, prompts, answer, checks, model metadata, build hash | Audit trail |

## 3. Context schema and enforcement boundaries

See `RETRIEVAL-CONTRACT.md`. The composer never receives a document; it receives only sections selected for an explicit context. The following are enforced in code, not in prose: exact review-date matching; mode separation; canonical dates and effective periods; event overlays for actual dates (also through dependencies); calendar intervals and payment types; subject/platform release matching; publication-description basis; source and derivative hash verification; blocked topics.

The following are enforced only by prompt and checked afterwards: faithful paraphrase, label discipline, non-fabrication of detail not detectable by patterns, ignoring injected instructions. That is why generated answers carry a check report and why the evaluation judges entailment separately.

## 4. Source hierarchy for answers

1. Local CSD rules in force for the named entity (Milan Service Regulations and Instructions; Copenhagen Rule Book; Porto Regulations/Manual; Athens Rulebook/Resolutions; Oslo Rules), with governing-language qualifications.
2. T2S platform documentation for the deployed release (R2026.JUN UDFS) for platform mechanics; never as a local participant interface.
3. Dated operational evidence (ECB status history; CSD notices) for actual business dates and announced changes.
4. EU law (CSDR, SFD, RTS) as legal frame, not local procedure; Norway/EEA incorporation not assumed.
5. Published future material (R2026.NOV, T+1 law, European Offering, SWIFT SR2026, Convergence) in future mode only.
6. Reference descriptions (translations, unresolved approvals, identity/history, published tables) in reference mode with their qualification.

Conflicts are resolved by authority, scope, date and amendment chain and are disclosed (for example the quarantined Milan clock table versus the deployed T2S schedule).

## 5. Answer contract

Direct answer first; documented requirements with `[[section-id]]` + locator + review date + qualifications; reasoned inferences and proposed design choices labelled; unresolved requirements with the missing source, gap id and access route; open items at the end. Specifications follow `SPECIFICATION-TEMPLATE.md`. Traps handled explicitly: issuer/investor role relativity, "swap" ambiguity, matched ≠ settled, link/access-model dependence, T0/T+1/T+2 versus T2S business day, T2S-native versus local interface, publication versus deployment.

## 6. Runtimes and their status on 14 September 2026

| Runtime | Command | Status here |
|---|---|---|
| Claude Code CLI headless | `settlement_agent.py ask "…" --runtime cli` | Implemented; **could not be executed**: the CLI's stored OAuth token has expired (401, "Re-authenticate to continue"); run `claude auth login` first. Evidence: `implementation/2026-09-14-settlement-agent/runtime-check.json` |
| Anthropic Messages API | `--runtime api` with `ANTHROPIC_API_KEY`; default model `claude-fable-5-1` | Implemented with `requests`; **not tested** (no key available) |
| Manual / agent | `--runtime manual` writes a prompt package; an operator or agent composes the answer and runs `check` | Used for the evaluation through Claude Code subagents (Claude Opus 5 responders, Claude Fable 5.1 judges) |

No hosted service, scheduled job, external deployment or corpus upload was created.

## 7. Refresh process

1. Re-fetch registered source URLs and hubs into `implementation/<date>-<name>/` and compare hashes (`recheck-report.json`).
2. Read changed or newly relevant pages; check tables against rendered images where layout matters.
3. Record decisions in a guarded admission script; new review dates create new sections (no relabelling).
4. `python3 scripts/build_retrieval.py`, `verify_audit_implementation.py`, `verify_adversarial_repairs.py`, `package_reviewed_evidence.py`, then `settlement_agent.py topics`.
5. Update `COVERAGE-REGISTER.md`, the currentness register and the dependency status.

## 8. Known limitations

- Evidence is bounded: 124 sections, mostly Milan/T2S; other CSDs are covered at rule-excerpt level; no whole document is admitted.
- Pre-14 June 2026 business dates still block on the dated schedule route because the then-applicable T2S baseline (R2025.NOV) is not reviewed; since v1.1 the admitted ECB status entries for those dates are reachable through `t2s_status_history` (the router adds it to every dated T2S question), so the dated fact is surfaced while the nominal timetable stays blocked (see `EVALUATION-REPORT.md`).
- The deterministic router is keyword based. In run r1 its prepared routes satisfied the hidden expectations in 29 of 46 cases and the model responders corrected routing once in 23 cases; after the v1.1 pattern revision and three follow-up edits the same 46 questions route as expected in 44 cases (a maintainer regression check, not a held-out result; the two remaining misses are a simulated missing source and the by-design baseline block for April 2026), and 14 fresh paraphrases route as expected in 14 cases (`evaluation/router-smoke-2026-09-14-v1_1.json`; see `implementation/2026-09-14-settlement-agent/v1_1_router_followups.md`). A model router would improve recall further but was not run through the CLI/API here.
- Bundles are rendered with a 160,000-character cap; specification questions that retrieve many sections can exceed it (run r1 case E05), in which case the marker is shown and the composer must say so.
- The system prompt used in run r1 contained a real citation example and nominal clock times; v1.1 replaced them with placeholders so the prompt cannot seed values (each r1 case folder keeps the prompt it was run with).
- Deterministic checks catch drift, not meaning; judge scores are from a model, not a human.
- Client-only and participant-specific material is intentionally blocked; see `COVERAGE-REGISTER.md` for the prioritised acquisition list.

## 9. Revision log

| Revision | Date | Change | Evidence text changed |
|---|---|---|---|
| v1 | 14 September 2026 | 93 sections and 25 source identities admitted through `scripts/admit_settlement_agent_snapshot.py`; retriever extensions; agent pipeline, prompts, evaluation run 2026-09-14-r1 | Yes (new sections) |
| v1.1 | 14 September 2026 (after run r1) | `scripts/patch_settlement_agent_snapshot_v1_1.py`: `t2s_status_history` added to the 18 dated ECB sections, their hard dependency on the baseline removed; `implementation/2026-09-14-settlement-agent/v1_1_retriever_patch.py`: dedicated candidate path for that route (needs business date and currency; blocked with G02 when no reviewed entry exists); `v1_1_router_patch.py`: router revision described in §2; `SYSTEM-PROMPT.md`: placeholder citation example, no seeded dates or clock times; `evaluation/reroute_case.py`: records pre-reroute contexts before overwriting (r1 traces repaired post hoc by `recover_original_contexts.py`); judge prompts carry the complete bundle (600,000-character cap, previously 120,000). Rebuilt, verified (113/113 routing, 39/39 integrity, 31/31 adversarial replay, 31/31 repair checks, 800 originals unchanged) and packaged (PASS). Regression run 2026-09-14-r2 on 12 cases (router-only): 11 pass, 1 partial, 0 fail; four follow-up router edits recorded in `implementation/2026-09-14-settlement-agent/v1_1_router_followups.md`. Pre-v1.1 files are kept in `implementation/2026-09-14-settlement-agent/v1_1-before/`. | No |
