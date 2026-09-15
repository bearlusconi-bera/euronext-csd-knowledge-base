# Settlement Expert Agent

An evidence-bound assistant for questions and specifications about settlement at Euronext Securities Milan (priority), Copenhagen, Porto, Athens, Oslo and T2S. It answers only from reviewed excerpts of official documents, cites each claim with a locator and review date, keeps every source qualification attached, and says precisely what is missing. It is a **research and specification assistant**, not a production-specification authority: client-only specifications, per-ISIN eligibility, fees and participant-specific cut-offs are blocked by design.

Built 14 September 2026 on library snapshot `2026-09-14-settlement-agent-v1` (124 reviewed sections from 51 source identities; base operational review 13 September 2026, additional review 14 September 2026).

## Files

| File | Purpose |
|---|---|
| `settlement_agent.py` | Runnable pipeline: `topics`, `route`, `retrieve`, `ask`, `check` |
| `SYSTEM-PROMPT.md` | Copyable agent instructions (the answer contract) |
| `AGENT-SPEC.md` | Architecture, enforcement boundaries, runtimes, limitations |
| `RETRIEVAL-CONTRACT.md` | Context schema, statuses, invariants, refresh |
| `SPECIFICATION-TEMPLATE.md` | Headings and labels for functional/technical specifications |
| `topic-index.json` | What can be asked, with which context (derived from the current build; rebuild with `topics`) |
| `COVERAGE-REGISTER.md` | Question-to-source matrix, gap status, prioritised missing sources |
| `examples/` | Representative sourced answers (issuer/investor CSD; cross-CSD DvP flow; technical specification exposing missing production fields) |
| `evaluation/` | 46 held-out cases, prompt packages, answers, deterministic checks, judge verdicts, `EVALUATION-REPORT.md` |
| `traces/` | Every `ask` run: bundle, prompts, answer, checks, model metadata |

## How to use it

From the library root (`euronext-csd-knowledge-base/`):

```sh
# 1. (once per rebuild) derive the topic index from the reviewed build
python3 settlement-expert-agent/settlement_agent.py topics

# 2. see how a question would be routed (no model needed)
python3 settlement-expert-agent/settlement_agent.py route "Once T2S says matched, is my Milan client's DvP settled?"

# 3. fetch evidence for explicit contexts (all controls enforced by the library retriever)
python3 settlement-expert-agent/settlement_agent.py retrieve --contexts '[{"as_of":"2026-09-13","entity":"Milan","service":"settlement","role":"participant","mode":"current","question_type":"matching_concept"}]' --prompt

# 4. ask end to end with a model runtime
python3 settlement-expert-agent/settlement_agent.py ask "…" --runtime cli          # Claude Code CLI (run `claude auth login` first)
ANTHROPIC_API_KEY=… python3 settlement-expert-agent/settlement_agent.py ask "…" --runtime api [--model claude-fable-5-1]
python3 settlement-expert-agent/settlement_agent.py ask "…" --runtime manual       # writes a prompt package for you or another agent

# 5. check any answer against the bundle it was written from
python3 settlement-expert-agent/settlement_agent.py check --answer answer.md --bundle bundle.json --question "…"
```

In Claude Code, the fastest path is: run `ask … --runtime manual`, open the trace folder, paste `prompt.system.md` as the system prompt and `prompt.user.md` as the message, save the reply as `answer.md`, then run `check`. The evaluation in `evaluation/` was run exactly this way with subagents.

### Runtime status on 14 September 2026

The CLI runtime is implemented but could not run here: the CLI's stored login had expired (`claude auth login` fixes it). The API runtime is implemented but untested (no key). See `implementation/2026-09-14-settlement-agent/runtime-check.json`.

## Example questions that work well

- "T2S reports my instruction as matched. Has my client at Monte Titoli received the shares?" (matching vs posting, SF2/SF3, Italian prevails)
- "Which fields must match in T2S and what tolerance applies in EUR?" (UDFS diagrams 55–57; RTS 2018/1229 Articles 5–6)
- "What was the EUR DvP cut-off on 8 September 2026?" (dated ECB overlay: postponed to 17:00)
- "How does an ICP send an OTC DvP through X-TRM and which fields map to T2S?" (Milan Instructions §3.4.1 Table 2, transcribed)
- "When does a Copenhagen T2S transfer order become irrevocable and final?" (Part 4 §11)
- "Is R2026.NOV deployed?" (published 14 September; Milan plans 14/16 November; not deployed)
- "Specify the flow and messages for a cross-CSD DvP, ICP, EUR, direct link, R2026.JUN" (assumption-bound specification)

Questions that return a controlled block with the missing source named: Milan participant cut-offs (G01), X-TRM message layouts (G03), per-ISIN eligibility (G04), fee amounts (G17), Copenhagen DCP test cases (G10), Athens DSS cycles (G12), Oslo calendar (G11), production XSD fields (G14), two-security swap atomicity (G04).

## What is supported

See `COVERAGE-REGISTER.md` for the full matrix. In short: Milan and T2S are covered at rule and process level (participants, accounts, static data, X-TRM channels and field correspondence, lifecycle, matching, hold/release, cancellation, recycling, partial settlement, links, CoSD, statuses, realignment, external settlement, default procedure, corporate actions on flow, penalties procedure and calendar, dated schedule overlays, release status and plans). Copenhagen, Porto, Athens and Oslo are covered at excerpt level with their governing-language and approval qualifications. EU law covers definitions, participation, finality, cash settlement, SFD entry/irrevocability and settlement-discipline facilities.

Review dates: most Milan/T2S/other-CSD sections were reviewed on 14 September 2026; the original 31 sections keep 13 September 2026. A question spanning both is answered with both dates stated; the agent never relabels evidence as current because time passed.

## How to request a specification

Ask for a "specification" and state: CSD, service and route (intra-CSD, cross-CSD in T2S, external), roles, instrument/link/account assumptions, release, currency, access model (ICP/DCP), and the intended business date or "nominal". The agent uses `SPECIFICATION-TEMPLATE.md`, labels each row (documented requirement, reasoned inference, proposed design choice, unresolved requirement) and lists the production documents that are missing (typically the X-TRM standard, MyStandards usage guidelines/XSDs and MT23 static data).

## How evidence is refreshed

Follow `RETRIEVAL-CONTRACT.md` § Refresh: new dated snapshot folder, hash recheck, page reading, guarded admission script, rebuild, both verifiers, packaging, `topics`. Never advance a section's review date without a new verification record; re-verified pages become new sections with the new date.

## When client-specific documents are required

Whenever the question concerns a particular firm: its account structure and SAC/DCA mapping, Party 1/Party 2 configuration, entitlements and message subscriptions, test acceptance, SSIs and counterparties, cash-agent arrangements, fee schedule, or a specific ISIN's link. The agent names the document and the route (MT-X, CLIMP, MyVPS, MyStandards, the CSD's documentation service) instead of inferring.

## Evaluation

Run `2026-09-14-r1` (held-out, 46 natural-language cases, 19 negative; Claude Code subagents as the model runtime — Claude Opus 5 responders, Claude Fable 5.1 judges): 40 pass, 5 partial, 1 fail; all 46 answers pass the deterministic checks; 19/19 negative cases pass; no hidden fail condition triggered; the instruction-injection case was disclosed and rebutted. The one fail (E32) was a retrieval-design gap fixed in revision v1.1; the deterministic router alone met expectations in 29/46 prepared bundles and responders corrected routing once in 23 cases, which drove the v1.1 router revision (44/46 on the same questions afterwards, 14/14 fresh paraphrases). The CLI and API runtimes were NOT_RUN. Regression run `2026-09-14-r2` (12 cases, revision v1.1, responders forbidden to correct routing): 11 pass, 1 partial, 0 fail; prepared routes met the hidden expectations in 11/12 (4/12 under the r1 router); the r1 fail (E32) passes. See `evaluation/EVALUATION-REPORT.md` for the per-case tables, the non-pass analysis, the maintainer inspection and the limits of this evaluation.
