# 19:30 versus 20:00 for night-time settlement: what the reviewed evidence actually supports

## Direct answer

Neither figure is a participant deadline, and the premise of the question does not survive the evidence. The **T2S R2026.JUN functional specification does not say that night-time settlement starts at 20:00**: it says the NTS period starts after the successful completion of the start-of-day period, and 20:00 appears only as the reference point for what the **first sequence** includes — expressly "even though the cycle starts after 20:00" [[t2s-nts-processing]] T2S User Detailed Functional Specifications R2026.JUN, §1.4.4.2 NTS processing and reporting, PDF 167–169; reviewed 14 September 2026 (source reviewed 13 September 2026); platform release R2026.JUN; the retrieval is labelled **schedule kind: baseline**. **Milan's Service Regulations set no hour at all**: Article 74 establishes a night-time phase and a day-time phase, processed on a gross basis, without printing a time [[milan-instruction-processing]] Regulations as of 26 January 2026, Article 74, PDF 52–53 (printed 51–52); reviewed 14 September 2026 (source reviewed 13 September 2026); English translation, **Italian text prevails**. And the retrieval that would establish the **applicable Milan participant timetable came back blocked** (gap id **G01**, "Applicable Milan timetable notice chain remains unresolved"), so **no local Monte Titoli participant cut-off — 19:30 or otherwise — can be stated from reviewed evidence**. The honest answer to "which applies to me today" is therefore: the T2S baseline reference is documented at platform level; the Milan participant-facing deadline is **unresolved**, and the 19:30 figure named in your question is not supported by anything in this bundle.

## Retrieval statuses — all three disclosed

| # | Context | Status |
|---|---|---|
| 1 | T2S, settlement, participant, current, `t2s_nts_processing`, as of 2026-09-14 | **evidence_only**; schedule kind **baseline** |
| 2 | Milan, settlement, participant, current, `milan_instruction_processing_rules`, as of 2026-09-14 | **evidence_only** |
| 3 | Milan, settlement, participant, current, `milan_participant_cutoff`, as of 2026-09-13 | **blocked** — "Applicable Milan timetable notice chain remains unresolved"; gap ids **['G01']** |

Retrieval 3 is the one that matters most for your question, and it is blocked. I do not fill that gap. Note also that retrieval 3 was run against knowledge as of 13 September 2026 while retrievals 1 and 2 carry review date 14 September 2026; both sections were reviewed on 14 September 2026 with source review dates of 13 September 2026. Evidence reviewed on those dates is not "current today" merely because time has passed — no dated event overlay for any particular business date was retrieved, so nothing here describes how a specific day actually ran.

## What the T2S evidence says — Documented requirement

[[t2s-nts-processing]] T2S UDFS R2026.JUN, §1.4.4.2, PDF 167–169; reviewed 14 September 2026; platform release R2026.JUN; schedule kind baseline:

1. **Position of the NTS period.** "The NTS period starts after the successful completion of the SOD period and is followed by the maintenance window and the real-time settlement period." The start is expressed as a **dependency on completion of the preceding period**, not as a clock time.
2. **Where 20:00 actually appears.** In each NTS sequence T2S processes the new settlement instructions, settlement restrictions and liquidity transfers received before the start of the sequence that are eligible for that sequence — "and for the first Sequence all the ones received in T2S before 20:00 even though the cycle starts after 20:00". So 20:00 is an **inclusion reference for the first sequence**, and the text itself states the cycle starts **after** that point.
3. **Structure.** Night-time settlement is presented as two parts of batch settlement, each referring to a settlement cycle; a cycle may consist of more than one sequence; pending instructions not settled in previous sequences are included in later ones.
4. **Durations are objectives, not commitments.** "The duration of the night-time settlement cycles are dependent on settlement volumes. The target objective for the first and last night-time cycles should finish by 22:20 and 00:00 respectively, as long as volumes do not exceed standard peak volumes." The section's own LIMITATION repeats this: **cycle durations are volume dependent and the 22:20/00:00 targets are objectives, not commitments**.
5. **Exceptional Friday-evening handling.** Where late peak-volume transactions arrive on Friday evening and are not available at the regular NTS, short NTS cycles are triggered by the T2S Operator during injection under Intraday Restriction, and an Additional NTS cycle is triggered at the end of injection; "the exact procedure with the timing to apply in case of such an event are defined in the T2S MOP" — **the MOP is not in this bundle**.
6. **The specification flags its own open timing.** "Note: The exact timing needed to perform the sequences and the time available for the sequence reporting will be defined at a later stage, but the dependencies defined are ensured."

Qualification that travels with all of the above: this is a **T2S-native functional description for R2026.JUN — not a local participant interface specification, production XSD or message usage guideline**, and the source carries no independent whole-edition supervisory approval certification. This bundle contains no release-deployment section, so I state the release identity of the evidence (R2026.JUN UDFS) rather than asserting which release is in production.

## What the Milan evidence says — Documented requirement

[[milan-instruction-processing]] Regulations as of 26 January 2026, Articles 68 and 73–76, PDF 49–50 and 52–53 (printed 48–49 and 51–52); reviewed 14 September 2026 (source reviewed 13 September 2026); **English translation, Italian text prevails**; no independent whole-edition supervisory approval certification:

1. **Article 74(1):** "The settlement process includes a night-time phase and a day-time phase. In each phase the Settlement Instructions are processed on a gross basis." **No clock time is printed in the article.**
2. **Article 74(2):** in each phase, according to the eligibility criteria, Monte Titoli settles (a) the new settlement instructions **entered before each phase** during the night-time phase and in real time during the day-time phase — including realignment instructions and those resulting from corporate actions — and (b) instructions that remained unsettled in the previous phase. The trigger is again **"entered before the phase"**, not an hour.
3. **Article 74(5)–(6):** instructions unsettled for want of securities or cash are re-proposed in the subsequent phase of the same settlement day or on the subsequent day until settled or cancelled under Article 70; participants may change re-proposed instructions only as to status indicators, and only if the instruction was not entered as non-changeable.
4. **Article 75:** optimisation takes account of the Article 68(5) priority criteria; on equal priority, instructions with the earlier settlement date settle first, within the functioning limits of the T2S platform.
5. **Article 68(2)–(3), (5)–(6):** acquisition checks completeness, formal correctness and consistency with T2S common static data and restrictions; validated instructions move to the next phases and non-validated ones are rejected; participants may request partial settlement and priority within T2S functionality, with Monte Titoli assigning priority to instructions with the Italian Ministry of Finance as counterparty, monetary-policy transactions and Bank of Italy collateral transfers, then those from Market Management Companies; participants are informed of the validation result.

Section LIMITATION: Articles 69–72 (matching, cancellation, hold, finality) sit in a different section (`milan-finality`, 13 September) that was **not retrieved** for this question.

## Reconciling the two figures — Reasoned inference

Derived from the two documented sets above plus the blocked retrieval; none of this is a quotation.

1. **There is no conflict at the level of the reviewed evidence.** The Milan Regulations define the *phases*; the T2S UDFS defines *how and when the platform runs the cycles*. Milan's Regulations contain no hour that could contradict 20:00. Derived from Article 74(1)–(2) against §1.4.4.2.
2. **The 20:00 in the T2S text is not a start time and not your deadline.** It is the reference for first-sequence inclusion, and the retrieval is explicitly labelled **baseline** — a nominal platform value, not an appointment and not a local participant deadline. Whether your instruction actually reaches T2S in time for the first sequence depends on your CSD's own input timetable, which is precisely what is blocked here. Derived from §1.4.4.2 line 19 and the retrieval's schedule-kind label.
3. **A local figure such as 19:30 would, if it exists, live in Milan's participant timetable, not in the Regulations.** That is exactly the chain reported unresolved under gap G01, so the figure can be neither confirmed nor denied from reviewed evidence — and it must not be presented as current on the strength of an older printing. Derived from the blocked retrieval 3 and from Article 74 containing no time.
4. **"Today" cannot be turned into an operational time.** Even the documented 22:20/00:00 figures are volume-dependent objectives, and an actual business date would need a dated event overlay that was not retrieved. Derived from §1.4.4.2 line 5–7 and the section LIMITATION.

## Unresolved requirement — what I cannot state

- **The applicable Monte Titoli participant cut-off / input timetable for the night-time phase**, on any date. Blocked, gap **G01**: the applicable Milan timetable notice chain remains unresolved. No time of day may be relied on for Milan participants from this bundle, in either direction.
- **The status of the 19:30 figure** in your question: it is not present in any retrieved section. This library does not treat an older printing of that passage as current evidence, and I will not quote it as such. Resolving it requires the timetable notice chain under G01.
- **The exact start clock time of the NTS period** in T2S: the specification gives a dependency ("after successful completion of SOD"), and states that exact sequence timing "will be defined at a later stage". The T2S MOP, which holds the timing for the exceptional Friday procedure, is not in the bundle.
- **Matching, cancellation, hold and finality boundaries** around the night-time phase: Articles 69–72 were not retrieved here (`milan-finality`, reviewed 13 September 2026).
- **Which T2S release is in production** on any given date: no release-deployment section was retrieved; only the release identity of the specification (R2026.JUN) is established.
- **Any local interface consequence** (message, screen, entitlement, file cut-off) of the above: the T2S UDFS is not a local participant interface specification, and Milan's X-TRM standards were not retrieved.

## Open items

1. **Milan participant timetable notice chain (gap G01)** — the authoritative, currently applicable Euronext Securities Milan notice or timetable establishing participant input deadlines for the night-time phase, and the notice that supersedes the older 19:30 printing; route: Euronext Securities Milan public notices page, plus the client documentation service for client-only timetables.
2. **Italian authoritative text of the Service Regulations (26 January 2026), Article 74** — the English excerpt used here is a translation and the Italian prevails; route: the same public documentation hub.
3. **T2S Manual of Operational Procedures (MOP)** — for the timing of the short/Additional NTS cycles in the exceptional Friday late-peak procedure; route: the ECB T2S professional-use documents page.
4. **T2S release-deployment evidence** — to state which release is actually in production on a given date rather than only the release identity of the specification; not retrieved for this question.
5. **Dated event overlay for the specific business date you care about** — nominal values above are baseline; a date-specific answer needs the dated notice or T2S operational communication for that day, plus the business date itself, which you have not specified.
6. **`milan-finality` (Articles 69–72)** if the question extends to matching, cancellation, hold or finality around the night-time phase.
