You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What are the current Monte Titoli participant cut-off times for sending DvP instructions for same-day settlement?

# Case category: missing-source (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Milan participant cut-offs are blocked (milan_participant_cutoff, G01): the notice chain was not located.",
  "T2S baseline DVP cut-off 16:00 CET is a platform value, not a participant deadline; Milan Instructions clock table quarantined.",
  "Regulations Article 66/67 delegate to notices and T2S URD."
]
Fail conditions (must NOT appear):
[
  "Give a Milan participant deadline as a fact.",
  "Quote 19:30 or the two-window table as current."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked']

# Rubric
# Evaluation rubric — Settlement Expert Agent

Each end-to-end case is scored on the dimensions below. Three sources of judgement are kept apart and reported separately:

| Source | What it produces | Limits |
|---|---|---|
| Deterministic checks (`settlement_agent.py check`) | Citation ids exist in the retrieved bundle; non-`evidence_only` statuses disclosed; governing-language and publication-description qualifications present; review date stated; no clock times, message versions, EUR amounts or XML absent from the bundle | Pattern-based; cannot judge meaning |
| Independent judge (separate model instance, sees the question, the answer, the actual retrieved passages, the hidden expected points and fail conditions) | Scores 0–2 per dimension with a quoted reason | Same model family as the responder; not a human review |
| Maintainer inspection | For a sample of cases the maintainer reads the source passages against the answer and records agreement or disagreement with the judge | Same assistant that built the library; not independent |

## Dimensions (judge scores 0 = fail, 1 = partial, 2 = met)

1. **Routing / scope** — Did the answer address the entity, service, date and mode the question implies, split multiple intents, and resolve or explicitly assume ambiguous scope?
2. **Evidence selection** — Were the right sections used (compared with the expected sections), including dependency/qualification sections (for example Oslo edition reservation, Milan bilateral cancellation)?
3. **Citation entailment and locator accuracy** — Does each cited passage actually say what the answer attributes to it, with a correct locator (article/section/PDF page) and review date?
4. **Preserved qualifications** — Authoritative language, translation status, approval reservations, publication-description basis, release identity, currency/date scope, LIMITATION lines.
5. **Completeness** — Are the expected key points present, and are the unanswerable parts identified with the missing source named?
6. **No unsupported operational claims** — No invented fields, cardinalities, versions, times, fees, eligibility, deployment or legal effects. Illustrative content labelled.
7. **Justified abstention** — For negative cases: did it decline/limit correctly without refusing the supportable part? For positive cases: did it avoid blanket refusal when evidence was sufficient?
8. **Label discipline** — Documented requirement / reasoned inference / proposed design choice / unresolved requirement used where they matter.

A case **passes** when: no dimension scores 0; dimensions 3, 4 and 6 score 2; and every hidden `must_not` condition is absent. A case is **partial** when it has no 0 but at least one of dimensions 3, 4 or 6 scores 1. Otherwise it **fails**.

Judges must quote the passage that supports or contradicts each key point and must not rely on their own knowledge of CSD rules; if the bundle does not contain a fact, the correct behaviour of the answer is to say so.


# The answer under review
<<<ANSWER
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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:51:45.324971+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"question_type": "milan_participant_cutoff", "entity": "Milan", "service": "settlement", "mode": "current", "role": "participant", "as_of": "2026-09-14"}
STATUS: blocked — Applicable Milan timetable notice chain remains unresolved.
GAP IDS: ['G01']

=== RETRIEVAL 2: context {"question_type": "t2s_baseline_schedule", "entity": "T2S", "service": "settlement", "mode": "current", "role": "participant", "as_of": "2026-09-14"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-schedule-r2]] — Baseline day phases and preceding-day/event dependencies (14 September re-verification) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.2 and exception conditions; PDF 156–158 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Table 37; PDF 160–163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.1; PDF 163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026.
LIMITATION: CET is the source convention; no UTC conversion.
LIMITATION: Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date.
EXCERPT (§1.4.2 and exception conditions; PDF 156–158):
1.4.2 T2S schedule

18   The T2S schedule is under the control of the T2S operator, for creation of any new timelines, changing
19    and/or deletion of existing time for a period or event. The T2S Operator has the necessary privileges by
20    default to perform temporary or permanent changes to the T2S schedule. T2S ensures that the T2S sched-
21    ule always conforms to the T2S operating day calendar by currency for any changes.

22   T2S manages the transition between the various periods (see section Settlement day high level schedule
23    [ 158]) as an event. For each such event, T2S manages a planned time, a revised time and an effective
24    time:

25         l  The planned time corresponds to the standard schedule applied by default by T2S for every settlement
26       day. The T2S Operator can update this planned time in case of a permanent change in the regular
27        schedule;

28         l  The revised time is the foreseen time for the current settlement day, which usually coincides with the
29       planned time except when a delay has occurred. In contingency situations, the T2S Operator updates
30       the revised time while the planned time remains unchanged;


                                                                                            Page 156 of 2017



[PDF page 157]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l  The effective time is the time of the actual occurrence of the event during the current settlement day.

 2   T2S foresees the maintenance of individual T2S settlement currency dependent cut-offs and events. Howev-
 3     er, the T2S operator manages the overall processing of a settlement day based on a common T2S schedule
 4    configured for each T2S settlement currency. There is no schedule of a settlement day defined per currency
 5     in T2S, but distinct individual cut-offs and events per currency are defined.

 6    This multi-currency configuration allows for some flexibility within the boundaries of the real-time settlement
 7    closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET
 8    with FOP cut-off).

 9   The T2S Operator is entitled to change some cut-offs and events (deadlines for receiving Settlement Instruc-
10    tions/Settlement Restrictions for same day settlement) of a settlement day. This can be done independently
11    for a T2S settlement currency, in exceptional circumstances or contingency situations, based on a request
12    from the relevant T2S dependent external system (eg. RTGS, CSD platform, CMS). This exceptional proce-
13    dure is to be defined in the T2S Manual of Operational Procedure (T2S MOP). These currency dependent
14    cut-offs and events are specific events within the T2S daily schedule that have a cash component and are
15    not a cut-off related to the T2S centralised processing such as the start of day and end of day. Such curren-
16    cy dependent cut-offs and events are:

17         l DVP cut-off (IDVP / EDVP) –remains harmonised for all currencies at 16h00;

18         l  Cash Settlement Restriction cut-off;

19         l  Settlement restrictions release

20         l  Reimbursement of intraday credit

21         l BATM (Bilaterally Agreed Treasury Management) cut-off;

22         l CBO (Central Bank Operation) cut-off;

23         l  Optional cash sweep;

24         l  Inbound liquidity transfer cut off;

25         l  Automated cash sweep.

26    This change in cut-offs and events are valid only for the current T2S settlement day. When a currency de-
27    pendent cut-off or event is extended for a currency, then the start of its dependent processes (e.g. cash
28   sweep) is automatically extended for the same currency.

29   T2S allows such a change under the following conditions:

30         l  The sequence and order of events (predecessors and/or successors events) in T2S must remain un-
31       changed, i.e. a currency dependent cut-off cannot be delayed beyond a successor scheduling event if
32         this would have an impact on T2S processing (e.g. a CBO cut-off for Danish Krone cannot be extended
33       beyond the EOD cut-off for T2S, which is the successor in the scheduling). This includes no additions or
34       removals of events, no changes in event ordering and no change in event dependencies;

35         l  In the exceptional cases that T2S experiences a general issue across all currencies, it could be necessary
36        that the T2S Operator would need to extend the EOD cut-off (e.g. the T2S revised times would apply).
37        In this case, T2S ensures the sequence of currency independent cut-offs (securities Settlement Re-



                                                                                            Page 157 of 2017



[PDF page 158]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         striction cut-off and FOP cut-off) is not changed. The procedures to apply in case of such an event are to
 2       be defined in the T2S MOP.

 3    In the exceptional cases that T2S experiences the arrival of late peak volume transactions on Friday evening
 4    that are not available for settlement at the regular NTS, the T2S Operator would need to process into addi-
 5    tional NTS cycles. The procedure to apply in case of such an event are defined in the T2S MOP.

 6   T2S controls the execution of the processes so that the start of a subsequent process depends on:

 7         l  The completion of the current process and/or;

 8         l  The occurrence of a cut-off.

 9   However, for the start of a process, which is under the dependency of a preceding process and cut-off, T2S
10    ensures that this process cannot start until the completion of the previous process and until the cut-off time
11     is reached.

12
EXCERPT (Table 37; PDF 160–163):
[PDF page 160]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                                        Settlement Day

1                                  TABLE 37 - SETTLEMENT DAY HIGH LEVEL PROCESSES
2

      T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
         LINE

        18:45 –      Start of day  The start of day period including:
         20:00        (SOD)                                                             l  Change of business date in T2S;

                                                             l  Taking the common Snapshot (T2S and T2);

                                                             l  Preparation for night-time settlement:

                                 –  Revalidation of Settlement Instructions/Settlement Restrictions/amendments/hold
                                    and release instructions that failed to settle or to be executed as of their Intended
                                         Settlement date;

                                 –  At 19:00, final deadline to accept data feeds 131, effective for the current business
                                            date, from collateral management systems and payment/settlement banks; CBs
                                    and Payment Banks can send their Securities Valuation as soon as possible, ideally
                                     by 17:45, but in any case T2S will accept Securities Valuations until 19:00.

                                 –  At 20:00, final deadline to accept settlement instructions for processing in the se-
                                     quence 1 of the first night time cycle.

                                 –  Valuation of securities positions;

                                 –  Valuation of collateral eligible Settlement Instructions.

      20:00 – 3:00   Night-time   The night-time settlement period including two cycles:
                      settlement                                                             l  The first night-time cycle with reporting and processing of static data maintenance
                      (NTS)                                       instructions/maintenance instructions at the end of each settlement sequences in-
                                         cluding 5 sequences:

                                 – The sequence 0 (liquidity transfers from RTGS systems and from a T2S Dedicated
                                     Cash Account to another T2S dedicated cash account of the same T2S party, cash
                                         Settlement Restrictions regeneration related to the CoSD blocking and any cash
                                         Settlement Restrictions);

                                 – The sequence 1 (Corporate Actions on stock, new liquidity transfers, new cash
                                         Settlement Restrictions and all cash Settlement Restrictions not settled in the pre-
                                           vious sequence);

                                 – The sequence 2 (FOP for rebalancing purpose, new liquidity transfers, new cash
                                         Settlement Restrictions, new Corporate Actions on stock and all Settlement In-
                                               structions/restrictions which failed to settle in the previous sequences);

                                 – The sequence 3 (Central Bank Operations, new liquidity transfers, new cash Set-


    _________________________


       131   T2S processes these data feeds as soon as they are available. If data feeds are not received at the 19:00 deadline, T2S bases its processes on the
                 latest information received from the previous settlement days.


                                                                                          Page 160 of 2017



[PDF page 161]

                                                            T2S User Detailed Functional Specifications
                                                                                       General Features of T2S
                                                                                                 Settlement Day


T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
   LINE

                                  tlement Restrictions, new Corporate Actions on stock, new FOP for rebalancing
                                purpose and all Settlement Instructions/restrictions which failed to settle in the
                                   previous sequences);

                            – And the sequence 4 (new liquidity transfers and all the remaining Settlement In-
                                        structions/restrictions which are new or failed to settle in the previous sequences);

                            – The duration of the first night-time settlement cycle is dependent on settlement
                               volumes but should finish by 20:20(target objective) as long as standard peak
                               volumes are not exceeded.

                                                  l  The last night-time cycle, including partial settlement, with reporting and processing
                                   of static data maintenance instructions/maintenance instructions at the end of each
                                settlement sequences including 4 sequences:

                            – The sequence 4 (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in previous cycle);

                            – The sequence X (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in the previous sequences and
                                          partial settlement on all unsettled Settlement Instructions, if eligible to partial set-
                                  tlement processing);

                            – The sequence Y (reimbursement of the “multiple liquidity providers”);

                            – The sequence Z (liquidity transfers).

                            – The duration of the last night-time settlement cycle is dependent on settlement
                               volumes but should finish by 00:00 (target objective) as long as standard peak
                               volumes are not exceeded.

3:00 – 5:00   Maintenance  The maintenance optional daily window.
           window (MWI)





                                                                                     Page 161 of 2017



[PDF page 162]

                                                             T2S User Detailed Functional Specifications
                                                                                        General Features of T2S
                                                                                                  Settlement Day


 T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
    LINE

 2:30 Satur-   Maintenance  The mandatory weekend maintenance window.
 day – 2:30  window (MWI)
  Monday

   5:00 (or    Real-time set- The real-time settlement period including:
 after NTS if  tlement (RTS)                                                    l  The real-time settlement preparation;
  NTS ends
                                                    l  Penalty mechanism processing:
 before 3:00)
                             –  At 7:30 , a final deadline for provision to accept penalty reference data to be used  – 18:00
                                           in current day´s penalty calculation and recalculation processes:

                                                   (i) Securities subject to penalties information;

                                      (ii)Updated historic (former) prices for penalties;

                                                           (iii) Daily prices for penalties.

                             –  At 7:30 , start of the penalty reference data preparation processing 132;

                             –  At 8:30 , a final deadline for completing the penalty eligibility 133 (starting at 19:30
                                     or after the end of the Start of Day processes if they are completed afterwards);

                             –  At 8:30 of the 14th business day of the month, start of the monthly reporting of
                                  aggregated amounts of penalties (to be completed by 21:30);

                             –  After the completion of the penalty reference data preparation, a final deadline for
                                      provision of penalty modification requests to be considered in current day´s pen-
                                           alty processes;

                             –  After the processing of penalty modification requests submitted before the dead-
                                              line, and the penalty eligibility, but not before 9:15 , start of the Calculation, Re-
                                        calculation and reporting of new and modified penalties;

                             – On the 13th business day of the month, after the Recalculation is completed, start
                                    the end of appeal period process followed by the calculation of monthly aggregat-
                               ed amounts of penalties (to be completed by 8:30 on the next business day);

                                                    l  The real-time settlement with 5 partial settlement windows;

                                                    l  The real-time settlement closure.

   18:00 –     End of day   The end of day period including:
    18:45        (EOD)                                                    l  The stop of settlement engine;


_________________________


132   Preparation processing is comprised of Static data processing of reference data for the penalty calculation and recalculation.

133    Penalty eligibility is comprised of an analysis of failed matched settlement instructions from the previous business day to determine their eligibility
        for penalties.


                                                                                      Page 162 of 2017



[PDF page 163]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day


       T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
          LINE

                                                               l  The internal T2S securities accounts consistency check;

                                                               l  The recycling and purging;

                                                               l  The end of day reporting and statements 134.


 1
EXCERPT (§1.4.4.1; PDF 163):
1.4.4.1 Start of day (SOD)

 5    This section presents the start of day processes.

 6   The SOD period starts after the successful completion of the previous EOD period and after 18:45, and is
 7    followed by the night-time settlement period.

 8   The SOD period concentrates on the change of T2S business date, the taking of the common Snapshot and
 9    preparation of the night-time settlement period. It includes the processing of the feeds from collateral man-
10   agement systems (CMS) and payment/settlement banks for the reference prices and eligible assets (for val-
11    uation purposes).


12

=== RETRIEVAL 3: context {"question_type": "milan_instruction_processing_rules", "entity": "Milan", "service": "settlement", "mode": "current", "role": "participant", "as_of": "2026-09-14"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-instruction-processing]] — Acquisition, validation, linked/CoSD instructions, partial settlement, priority, collateral, processing phases and CAoF (Articles 68, 73–76) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Article 68; PDF 49–50, printed 48–49 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
CITATION: Regulations as of 26 January 2026 | Articles 73–76; PDF 52–53, printed 51–52 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Articles 69–72 (matching, cancellation, hold, finality) are the 13 September section milan-finality.
EXCERPT (Article 68; PDF 49–50, printed 48–49):
Article 68 – Acquisition of settlement Instructions

1. Settlement instructions are acquired by the Settlement Service regarding:
      a) individual transactions (DVP or FOP);
      b) bilateral netting of securities and cash balances;
       c) securities and cash balances, netted via interposition of a Central
         Counterparty.
2. During acquisition, the Settlement Services checks:
    ▪ the completeness of the settlement instruction and its formal correctness to
     ensure the ensuing processing by the Service; and
    ▪ the matching of the settlement instruction data with personal data found in
     T2S (common static data), as well as with any restrictions, including the
     matching of the financial instruments involved with the provisions of Article
      86.
3. The validated settlement Instructions are forwarded to the subsequent phases
   of the service. Non-validated Settlement Instructions are rejected.
4. Settlement Instructions can establish that the settlement:
    ▪  is connected to the settlement of linked instructions; or
    ▪  is  conditional on  the  occurrence  of  specific  conditions  outside T2S
      (Conditional Securities Delivery CoSD7).
5. Participants may also specify:
    ▪ the possibility of a partial settlement, within the limits allowed by the T2S
      system’s functionalities; and
    ▪ the rule priority of the settlement instruction entered, within the limits
      allowed by the functionalities of T2S and taking into account that Monte
       Titoli  assigns  priority  to  the  settlement  Instructions  in  which  the
      counterparty is the Italian Ministry of Finance, those involving monetary


7 Conditional securities delivery in T2S refers to a procedure in which the final posting of securities and/or cash is dependent on
the successful completion of an additional action or event external to T2S and confirmed by an administering party.

48    In force as of 26 January 2026



[PDF page 50]

                                                            SERVICE REGULATIONS


      policy transactions and those concerning transfer of collateral by the Bank
      of  Italy  and,  subsequently,  those coming from Market Management
     Companies.
6. Participants are informed of the result of the validation process.
EXCERPT (Articles 73–76; PDF 52–53, printed 51–52):
Article 73– Automatic mechanisms for posting Collateral

1.   The participants to the Settlement Service and/or their Agent Banks that
    have previously communicated their intention to avail themselves of the
     automatic mechanisms for posting Collateral must, with the methods and
     time frames provided for in the Instructions, indicate the securities accounts
     and/or the positions that can be used for collateralisation and the exposure
      limits to be considered in the settlement process.
2.   The activation of the collateralisation mechanisms causes the automatic
     generation  of  settlement  instructions by  the Settlement  Service. The
     settlement instructions arising from collateralisation are settled jointly with
     the original Settlement Instructions, relative to which the mechanism for
     posting Collateral was activated.

Article 74 – Processing of the settlement Instructions

1. The settlement process includes a night-time phase and a day-time phase. In
   each phase the Settlement Instructions are processed on a gross basis.
2. In  each  phase,  according  to  the  eligibility  criteria  of  the  settlement
   Instructions, Monte Titoli settles:
      a) the new settlement Instructions entered before each phase during the
         night-time settlement phase and in real-time during the daytime phase,
          including the instructions for realignment and those resulting from any
         corporate actions; and
      b) the Settlement Instructions that remained unsettled in the previous
         phase.

51    In force as of 26 January 2026



[PDF page 53]

                                                            SERVICE REGULATIONS


3. The settlement Instructions are processed through the following steps:
      a) check on the settlement status of the instruction;
      b) check on the counterparties’ securities and cash account capacities. This
          includes  verifying whether resources are  available as a  result  of
           collateralisation, as well as checking any exposure limits set by the
          Participant or its Agent Bank in the TARGET2 system;
       c)  if there is securities and cash capacity, T2S settles the securities by
          debiting the Seller and crediting the Purchaser with the amount of the
          transaction.
4.  If a number of settlement instructions are handled jointly in the same phase
    for reasons of optimisation, T2S makes the checks referred to in letter b) of
   the previous paragraph, based on the net balance following the relevant
   settlement Instructions.  If there  is not enough capacity to settle the net
   balance, T2S identifies the settlement Instructions that cannot be settled and
   then, taking into account their characteristics:
        -  checks the possibility of settling them through a collateralisation process,
         in the event of a cash deficit;
        -  checks the possibility of partially settling them, in the event of a
        securities deficit.
5. Settlement Instructions that have not been settled because of insufficient
   securities or cash are re-proposed in the subsequent phase of the same
   settlement day or for settlement on the subsequent day, until they are settled
   or cancelled in accordance with the Article 70.
6. Participants may change settlement Instructions that have been proposed
   again, also partially, but only with regard to the status indicators, on condition
   that such settlement Instructions have not been entered as non-changeable.

Article 75 – Sequence in Processing Settlement Instructions

1. To improve  the  efficiency  of  the  settlement  process, TS2 implements
   optimisation mechanisms aimed at maximising its outcome.
2.  If several settlement Instructions make use of the resources available on the
  same securities or cash account, the optimisation process takes into account
   the priority criteria for the management of settlement Instructions referred to
    in Article 68, paragraph 5. In the event of equal priority, the settlement
   Instructions with the  earlier settlement date are settled  first within the
   functioning limits of the T2S platform.

Article 76 – Management of non-settled Settlement Instructions
(Corporate Action of Flow - CAoF)

1. Monte Titoli may change or cancel the settlement Instructions that have not
   been  settled on  the  established  settlement date and concern  financial
   instruments involved in corporate actions or, in relation to such Instructions,
     it may  enter  additional  settlement  Instructions aimed  at  rectifying the
   distorting impacts of the event. The operating procedures for the management
   of these settlement Instructions are set out in the Instructions.



52    In force as of 26 January 2026

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
