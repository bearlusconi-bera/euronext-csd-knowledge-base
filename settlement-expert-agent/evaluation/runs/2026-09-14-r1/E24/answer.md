# "The settlement schedule for tomorrow"

## Direct answer

I cannot tell you tomorrow's settlement schedule from reviewed evidence, and I will not present a nominal schedule as if it were tomorrow's. Two things are missing: (1) **scope** — you have not said which system or CSD you mean, which business date "tomorrow" is, or which settlement currency; and (2) **a dated event overlay** — the only schedule evidence in the bundle is the T2S **baseline** (nominal) day structure, and the evidence itself states that dated queries require a reviewed event overlay for the same review date. What I can give you, clearly labelled, is that baseline as reviewed on **14 September 2026**.

## Retrieval statuses (disclosure)

| # | Context | Status |
|---|---|---|
| 1 | T2S / settlement / current — baseline schedule | evidence_only, **SCHEDULE KIND: baseline** |
| 2 | T2S / settlement / current — dated schedule | **needs_context** — "Actual schedules require business date and currency." MISSING CONTEXT FIELDS: `['business_date', 'currency']` |

So the dated route exists but could not run: it needs a business date and a currency from you. Below I answer conditionally on a stated assumption, as the second-best alternative to that clarification.

## What I need from you (short clarification)

1. **Which schedule?** The retrieved section covers **T2S** only (entities: T2S). If you mean a CSD's own local timetable — Euronext Securities Milan (Monte Titoli), Copenhagen (VP), Porto (Interbolsa), Athens (ATHEXCSD) or Oslo (VPS) — that is a different document and none was retrieved here.
2. **Which business date?** "Tomorrow" is relative. Relative to the 14 September 2026 review date it would be 15 September 2026, but the retriever needs a canonical business date from you, not an inferred one, and whether that date is a settlement day at all depends on the T2S operating day calendar by currency, which is not in this bundle.
3. **Which settlement currency?** This is not pedantry: T2S maintains individual currency-dependent cut-offs and events, so the answer genuinely differs by currency (see below).

**Assumption I adopt for the conditional answer that follows:** you mean the T2S platform day, and you want the nominal structure rather than a statement about actual operations on a specific date. Everything below is nominal on that basis.

## The T2S baseline day (nominal) — Documented requirement

All of the following is [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), Table 37 "Settlement day high level processes", PDF 160–163, and §1.4.4.1, PDF 163; reviewed **14 September 2026** (2026-09-14); platform release R2026.JUN; body language English, authoritative language not independently established; approval: source identity checked, no independent whole-edition supervisory approval certification; source reviewed 13 September 2026.

| T2S timeline | Period | Nominal content |
|---|---|---|
| 18:45 – 20:00 | Start of day (SOD) | Change of business date in T2S; common snapshot (T2S and T2); revalidation of instructions that failed to settle as of their intended settlement date; at 19:00 final deadline to accept data feeds effective for the current business date from collateral management systems and payment/settlement banks (securities valuations accepted until 19:00, ideally sent by 17:45); at 20:00 final deadline to accept settlement instructions for processing in sequence 1 of the first night-time cycle; valuation of securities positions and of collateral-eligible instructions |
| 20:00 – 3:00 | Night-time settlement (NTS) | First night-time cycle with sequences 0–4 (target objective to finish by 20:20 if standard peak volumes are not exceeded); last night-time cycle with sequences 4, X (including partial settlement of eligible unsettled instructions), Y and Z (target objective to finish by 00:00 on the same condition) |
| 3:00 – 5:00 | Maintenance window | Optional daily window |
| 2:30 Saturday – 2:30 Monday | Maintenance window | Mandatory weekend maintenance window |
| 5:00 (or after NTS if NTS ends before 3:00) – 18:00 | Real-time settlement (RTS) | Real-time settlement preparation; penalty mechanism processing; real-time settlement with five partial settlement windows; real-time settlement closure |
| 18:00 – 18:45 | End of day (EOD) | Stop of the settlement engine; internal T2S securities-account consistency check; recycling and purging; end-of-day reporting and statements |

**The closure boundaries.** The multi-currency configuration allows flexibility "within the boundaries of the real-time settlement closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET with FOP cut-off)", and the DVP cut-off (IDVP/EDVP) "remains harmonised for all currencies at 16:00". [[t2s-schedule-r2]] UDFS R2026.JUN §1.4.2, PDF 156–158; reviewed 14 September 2026; same qualifications as above.

**The settlement day opens the previous evening.** The SOD period starts after the successful completion of the previous EOD period and after 18:45, and the change of the T2S business date happens inside it. [[t2s-schedule-r2]] UDFS R2026.JUN §1.4.4.1, PDF 163, and Table 37, PDF 160; reviewed 14 September 2026. **Reasoned inference**, derived from this: whatever date you eventually name as "tomorrow", its T2S settlement day nominally opens during the preceding evening — so a question about "tomorrow" may in practice already concern this evening's SOD. This inference concerns the structure only; it says nothing about what will actually happen on any date.

## Why this is not "tomorrow's schedule" — Documented requirement

- **Planned, revised and effective times are three different things.** T2S manages each transition as an event with a planned time (the standard schedule applied by default every settlement day), a revised time (the foreseen time for the current settlement day, which usually coincides with the planned time except when a delay has occurred — in contingency the operator updates the revised time while the planned time stays unchanged) and an effective time (the actual occurrence during the current settlement day). The table above is **planned** time only. [[t2s-schedule-r2]] UDFS R2026.JUN §1.4.2, PDF 156–158; reviewed 14 September 2026.
- **Cut-offs can move on the day.** The T2S Operator is entitled to change some currency-dependent cut-offs and events — the deadlines for receiving settlement instructions and restrictions for same-day settlement — independently per settlement currency, in exceptional circumstances or contingency situations, at the request of the relevant dependent external system; such a change is valid only for the current settlement day, may not break the sequence and dependencies of events, and follows a procedure defined in the T2S Manual of Operational Procedures. The operator may also extend the end-of-day cut-off if a general cross-currency issue occurs, and may run additional night-time settlement cycles when late Friday-evening peak volume arrives. [[t2s-schedule-r2]] UDFS R2026.JUN §1.4.2, PDF 156–158; reviewed 14 September 2026.
- **Currency matters.** There is no settlement-day schedule defined per currency in T2S, but distinct individual cut-offs and events per currency are defined — among them the DVP cut-off, the cash settlement restriction cut-off, settlement restrictions release, reimbursement of intraday credit, the BATM and CBO cut-offs, optional cash sweep, inbound liquidity transfer cut-off and automated cash sweep. [[t2s-schedule-r2]] UDFS R2026.JUN §1.4.2, PDF 156–158; reviewed 14 September 2026. This is exactly why retrieval 2 asks you for a currency.
- **LIMITATION lines that travel with every line above** [[t2s-schedule-r2]]: "Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date."; "CET is the source convention; no UTC conversion."; "Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026."
- **Unresolved requirement.** Whether any deviation, delay or extension is published for the date you mean is not established: no dated event overlay was retrieved, because the dated retrieval stopped for want of a business date and currency. The absence of an overlay in this bundle is **not** evidence that the day will be routine — it is simply unreviewed here. Equally, the times above are **not** appointments and **not** your local participant deadline: the deadline your instructions must actually meet is set by your CSD, and no CSD timetable is in this bundle.

## Open items

1. **Business date and currency** for the dated retrieval (needs_context, missing fields `business_date` and `currency`). Give me the canonical date you mean by "tomorrow" and the settlement currency, and the dated route can be run against a reviewed event overlay for the same review date.
2. **Which entity.** If you meant a CSD's own settlement timetable rather than the T2S platform day, say which CSD; the retrieved section is scoped to T2S only and no local timetable, local cut-off or participant deadline is in this bundle.
3. **Operating day calendar.** Whether the date you name is a settlement day for the currency you name depends on the T2S operating day calendar by currency, which is not in reviewed evidence here. Official route for the platform side: the ECB's T2S documentation pages for the deployed release (UDFS and the T2S operational documentation); for a local timetable, the relevant CSD's public documentation hub and its client platform documentation service.
4. **Same-day deadlines.** If your real question is "by when must I instruct for settlement on that date", that is a cut-off question: the platform boundary is the 16:00 CET DVP cut-off cited above, but your binding deadline is the local one, which is not in this bundle.
