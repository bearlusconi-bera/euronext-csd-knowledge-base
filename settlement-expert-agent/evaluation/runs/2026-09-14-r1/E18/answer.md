# Monte Titoli participant cut-off times for same-day DvP instructions

## Direct answer

**Unresolved requirement.** The reviewed evidence does **not** contain Monte Titoli's (Euronext Securities Milan's) participant cut-off times for sending DvP instructions for same-day settlement. The retrieval for that exact topic came back **blocked**, with gap **G01** and the reason "Applicable Milan timetable notice chain remains unresolved" — i.e. the Milan timetable/notice chain that would establish which published cut-offs are currently applicable has not been resolved in the library, so no Milan participant deadline can be quoted. I will not substitute a remembered or inferred time for it.

What *is* in reviewed evidence is (a) the T2S **baseline** day schedule, which is a platform-level nominal schedule and explicitly not a local participant cut-off, and (b) Milan's Service Regulations, which describe the processing phases but delegate the time frames to Monte Titoli's *Instructions* — the document layer that is unresolved.

## Retrieval statuses (disclosure)

| # | Context | Status | Consequence |
|---|---|---|---|
| 1 | Milan / settlement / current — participant cut-off | **blocked** — "Applicable Milan timetable notice chain remains unresolved", GAP IDS `['G01']` | No Milan participant cut-off time may be stated. The gap is not filled from any other source. |
| 2 | T2S / settlement / current — baseline schedule | evidence_only (SCHEDULE KIND: **baseline**) | Usable only as platform baseline, not as a Milan deadline. |
| 3 | Milan / settlement / current — instruction processing rules | evidence_only | Usable for phases and validation, contains no times. |

No business date was supplied with the question, so no dated T2S event overlay was retrieved; the baseline below therefore carries no statement about what actually happened on any specific business date.

## What the reviewed evidence does support

**1. T2S platform cut-offs (baseline, not a Milan participant deadline) — Documented requirement.**
Within T2S, the real-time settlement closure runs between the DVP cut-off at **16:00 CET** and the end of the cut-off phase at **18:00 CET** with the FOP cut-off; the DVP cut-off (IDVP/EDVP) "remains harmonised for all currencies at 16:00". The UDFS describes such cut-offs as "deadlines for receiving Settlement Instructions/Settlement Restrictions for same day settlement", and records that the T2S Operator may change some currency-dependent cut-offs for the current settlement day only, in exceptional or contingency situations and on request from the relevant dependent external system, without changing event sequence or dependencies. [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.2 and exception conditions, PDF 156–158; reviewed 14 September 2026 (2026-09-14); platform release R2026.JUN; body language English, authoritative language not independently established; source identity checked, no independent whole-edition supervisory approval certification; source reviewed 13 September 2026.

**2. The T2S settlement day opens the previous evening — Documented requirement.**
Start of day (SOD) runs **18:45–20:00** and begins after the successful completion of the previous end-of-day period and after 18:45; night-time settlement runs **20:00–3:00**; the maintenance window is **3:00–5:00**; real-time settlement starts at **5:00** (or after NTS if NTS ends before 3:00); end of day is **18:00–18:45**. At **20:00** there is the "final deadline to accept settlement instructions for processing in the sequence 1 of the first night time cycle". [[t2s-schedule-r2]] T2S UDFS R2026.JUN, Table 37 "Settlement day high level processes", PDF 160–163, and §1.4.4.1, PDF 163; reviewed 14 September 2026; same qualifications as above.

**LIMITATION lines that travel with both points above** [[t2s-schedule-r2]]: "Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date."; "CET is the source convention; no UTC conversion."; "Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026."

**3. Milan's Regulations set phases, not times, and point to the Instructions — Documented requirement.**
The Monte Titoli settlement process "includes a night-time phase and a day-time phase", with instructions processed on a gross basis in each phase; in each phase Monte Titoli settles the new settlement instructions "entered before each phase during the night-time settlement phase and in real-time during the daytime phase", together with instructions unsettled from the previous phase. Instructions not settled for want of securities or cash are re-proposed in the subsequent phase of the same settlement day or for settlement on the subsequent day. Settlement instructions are acquired for individual transactions (DVP or FOP), bilateral netting, and CCP-netted balances, and are validated on completeness, formal correctness and consistency with T2S common static data; non-validated instructions are rejected. Where a time frame is required — for example for the automatic collateral-posting mechanisms — the Regulations refer to "the methods and time frames provided for in the Instructions", and the operating procedures for non-settled instructions in corporate-action contexts are likewise "set out in the Instructions". [[milan-instruction-processing]] Monte Titoli Regulations as of 26 January 2026, Article 68, PDF 49–50 (printed 48–49) and Articles 73–76, PDF 52–53 (printed 51–52); reviewed 14 September 2026; **English translation, the Italian text prevails** (cover, PDF 1); source identity checked, no independent whole-edition supervisory approval certification; source reviewed 13 September 2026. A further LIMITATION on this section: Articles 69–72 (matching, cancellation, hold, finality) sit in a different section (`milan-finality`) reviewed 13 September 2026 and were not retrieved here.

## Reasoned inference (clearly not a documented Milan cut-off)

- **Reasoned inference**, derived from point 3: because the Regulations allocate time frames to Monte Titoli's Instructions rather than fixing them in the Regulations themselves, the participant-facing cut-offs you are asking for would live in the Instructions and in Monte Titoli's timetable notices — precisely the chain that gap G01 records as unresolved. This explains *why* the answer is unavailable; it does not supply a time.
- **Reasoned inference**, derived from points 1 and 2: since the T2S settlement day opens at SOD 18:45 the previous evening and the DVP cut-off is 16:00 CET, the *platform* window for same-day DvP settlement on a T2S business date is materially wider than any local deadline a CSD imposes on its participants. A Monte Titoli participant deadline is normally at or before the platform cut-off, never after it — but the actual Milan value is not in reviewed evidence, so no number can be given, and 16:00 must not be used as if it were the Monte Titoli participant cut-off.
- **Explanation, not evidence** (background, for terminology only): "DvP" = delivery versus payment, the securities leg and the cash leg settling conditionally on each other; "same-day settlement" here means an instruction sent for settlement on the current settlement day rather than a future intended settlement date.

## What you must not read into this answer

- The T2S baseline times above are **not appointments and not local participant deadlines**; they are nominal values for the platform, and the evidence itself says so.
- The review date of all retrieved sections is **14 September 2026**. Nothing here is asserted to be "current today" by the passage of time, and no statement is made about any particular business date, delay or deviation.
- No Milan cut-off, no Milan timetable notice, no X-TRM submission deadline and no agent-bank deadline is stated anywhere above, because none is in the bundle.

## Open items

1. **Monte Titoli participant cut-off times for DvP same-day settlement — blocked, gap G01** ("Applicable Milan timetable notice chain remains unresolved"). Required source: the applicable Monte Titoli *Instructions* accompanying the Service Regulations as of 26 January 2026, plus the currently applicable Monte Titoli timetable notice chain that supersedes earlier timetable passages. Official route: the Euronext Securities Milan public documentation hub (Regulations, Instructions and notices) and, for client-only material, the Monte Titoli client platform (MT-X) documentation service. No message to the CSD is drafted here.
2. **Business date scope.** If you need a specific business date (for example to know whether a deviation was published), supply the date and the currency; a dated answer additionally requires a reviewed T2S event overlay for the same review date, which was not retrieved for this question.
3. **Access model.** Whether you submit ICP (through Monte Titoli's own interface) or DCP (directly to T2S) changes which deadline binds you. The bundle contains no Milan ICP/DCP submission deadlines, so this distinction cannot be resolved from reviewed evidence either.
4. **Related Milan articles not retrieved here.** Articles 69–72 (matching, cancellation, hold, finality) are in section `milan-finality`, reviewed 13 September 2026, and were not part of this retrieval; if the question extends to the last moment for cancelling or holding an instruction, that section must be retrieved.
