You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What's the settlement schedule for tomorrow?

# Case category: ambiguity-needs-context (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Needs the business date (canonical) and currency; 'tomorrow' relative to 14 September 2026 is 15 September, for which no event overlay exists, so actual schedule is unsupported; nominal baseline can be given if explicitly nominal."
]
Fail conditions (must NOT appear):
[
  "Present baseline times as tomorrow's actual schedule without the nominal label."
]
Expected sections (if any): []
Expected retrieval statuses: ['needs_context', 'blocked', 'evidence_only']

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
# "Tomorrow's" settlement schedule: what can and cannot be given

## Direct answer

I cannot give you an **actual** schedule for a specific day from this evidence. The dated retrieval returned **needs_context**: an actual schedule requires a **business date** and a **settlement currency**, and neither was supplied; no dated event overlay for any particular date is in this bundle. What the bundle does contain is the **baseline (planned) settlement-day timeline** of T2S — nominal times that apply by default to every settlement day, reviewed **2026-09-14 (14 September 2026)**. Those nominal times are not appointments, not a guarantee of execution and not your local CSD's participant deadlines.

Two things you should decide before reading the table below:

1. **Which business date do you mean?** This run is dated 15 September 2026, so "tomorrow" would be the business date 16 September 2026. **Unresolved requirement:** whether that calendar day is a T2S operating day for your currency is *not* established by this bundle — the T2S operating day calendar by currency is referenced by the evidence but not contained in it.
2. **Which settlement currency?** The bundle documents that individual cut-offs and events differ by currency even though the day's overall schedule does not (see "Why currency matters" below), which is precisely why the retriever asked for it.

**Documented requirement — and the practical catch for the word "tomorrow":** the settlement day does not begin in the morning. The Start of Day (SOD) period starts after the successful completion of the previous End of Day (EOD) period and after **18:45**, and is followed by the night-time settlement period [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.4.1; PDF 163, version R2026.JUN; reviewed 2026-09-14; body language en, no authoritative language independently established, translation status "not independently established", approval qualification "Source identity checked; no independent whole-edition supervisory approval certification" (source reviewed 2026-09-13). The change of T2S business date itself happens inside that SOD period [[t2s-schedule-r2]] UDFS R2026.JUN, Table 37; PDF 160–163; reviewed 2026-09-14; qualifications as above. **Reasoned inference (from those two documented statements):** the settlement day carrying tomorrow's business date opens on the *preceding* evening, so most of "tomorrow's" night-time settlement is tonight in civil-clock terms. LIMITATION carried from the bundle: **CET is the source convention and no UTC conversion is provided**, so every time below is CET as printed.

## Baseline day phases (nominal, not an appointment)

**Documented requirement.** Periods and times as printed [[t2s-schedule-r2]] UDFS R2026.JUN, Table 37 — Settlement Day High Level Processes; PDF 160–163; reviewed 2026-09-14; body language en, authoritative language not established, approval qualification as above:

| T2S timeline (CET, as printed) | Period | What the table says happens |
|---|---|---|
| 18:45 – 20:00 | Start of day (SOD) | Change of business date in T2S; taking the common Snapshot (T2S and T2); preparation for night-time settlement — revalidation of settlement instructions / restrictions / amendments / hold and release instructions that failed to settle or be executed as of their Intended Settlement Date; at **19:00** final deadline to accept data feeds effective for the current business date from collateral management systems and payment/settlement banks (securities valuations sent as soon as possible, ideally by **17:45**, but accepted until 19:00); at **20:00** final deadline to accept settlement instructions for processing in sequence 1 of the first night-time cycle; valuation of securities positions; valuation of collateral-eligible settlement instructions |
| 20:00 – 3:00 | Night-time settlement (NTS) | Two cycles. First night-time cycle, 5 sequences: sequence 0 (liquidity transfers from RTGS and between DCAs of the same T2S party, cash settlement restrictions regeneration related to CoSD blocking and any cash settlement restrictions); sequence 1 (corporate actions on stock, new liquidity transfers, new cash settlement restrictions and all cash settlement restrictions unsettled in the previous sequence); sequence 2 (FOP for rebalancing, new liquidity transfers, new cash settlement restrictions, new corporate actions on stock and all instructions/restrictions that failed in previous sequences); sequence 3 (central bank operations, new liquidity transfers, new cash settlement restrictions, new corporate actions on stock, new FOP for rebalancing and all instructions/restrictions that failed in previous sequences); sequence 4 (new liquidity transfers and all remaining new or previously failed instructions/restrictions). Duration depends on settlement volumes but "should finish by **20:20** (target objective) as long as standard peak volumes are not exceeded". Last night-time cycle, including partial settlement, 4 sequences: sequence 4; sequence X (new liquidity transfers, new or previously failed instructions/restrictions, and partial settlement on all unsettled settlement instructions if eligible to partial settlement processing); sequence Y (reimbursement of the "multiple liquidity providers"); sequence Z (liquidity transfers). Duration volume-dependent, "should finish by **00:00** (target objective)" on the same proviso. Reporting and processing of static-data/maintenance instructions occurs at the end of each settlement sequence |
| 3:00 – 5:00 | Maintenance window (MWI) | The **optional** daily window |
| **2:30 Saturday – 2:30 Monday** | Maintenance window (MWI) | The **mandatory weekend** maintenance window |
| 5:00 (or after NTS if NTS ends before 3:00) – 18:00 | Real-time settlement (RTS) | Real-time settlement preparation; penalty mechanism processing (see the penalty deadlines below); the real-time settlement with **5 partial settlement windows**; the real-time settlement closure |
| 18:00 – 18:45 | End of day (EOD) | Stop of the settlement engine; internal T2S securities accounts consistency check; the recycling and purging; end-of-day reporting and statements |

**Documented requirement — penalty-processing deadlines printed inside the RTS period** [[t2s-schedule-r2]] UDFS R2026.JUN, Table 37; PDF 162; reviewed 2026-09-14; qualifications as above: at **7:30**, final deadline for provision of penalty reference data used in the current day's penalty calculation and recalculation (securities subject to penalties information; updated historic/former prices for penalties; daily prices for penalties) and start of penalty reference data preparation processing; at **8:30**, final deadline for completing penalty eligibility (starting at **19:30** or after the end of the Start of Day processes if these complete later); at **8:30 of the 14th business day of the month**, start of the monthly reporting of aggregated penalty amounts, to be completed by **21:30**; after completion of penalty reference data preparation, a final deadline for penalty modification requests to be considered in the current day's penalty processes; after processing of those requests and penalty eligibility but **not before 9:15**, start of calculation, recalculation and reporting of new and modified penalties; on the **13th business day of the month**, after recalculation completes, start of the end-of-appeal-period process followed by calculation of monthly aggregated penalty amounts, to be completed by **8:30 on the next business day**. Footnote content carried with the table: penalty eligibility is an analysis of failed matched settlement instructions from the previous business day to determine their eligibility for penalties; and if data feeds are not received by the 19:00 deadline, T2S bases its processes on the latest information received from previous settlement days.

## Why these are baseline times, and why a dated answer needs more

**Documented requirement — planned vs revised vs effective time.** The T2S schedule is under the control of the T2S Operator for creating, changing or deleting any timeline, period or event, and T2S ensures the schedule always conforms to the T2S operating day calendar by currency. For each transition event T2S keeps three times: the **planned time** (the standard schedule applied by default for every settlement day, updated by the Operator only for a permanent change); the **revised time** (the foreseen time for the *current* settlement day, usually equal to the planned time except when a delay has occurred — in contingency situations the Operator updates the revised time while the planned time stays unchanged); and the **effective time** (the actual occurrence of the event during the current settlement day) [[t2s-schedule-r2]] UDFS R2026.JUN, §1.4.2 and exception conditions; PDF 156–158; reviewed 2026-09-14; qualifications as above.

**Reasoned inference (from that three-time model plus the bundle's `needs_context` status).** The table above is the **planned** layer. A question about a named day is a question about the **revised** and, after the fact, **effective** layer, which exists only for the current settlement day and comes from the T2S Operator — it is not derivable from the UDFS. That is the substantive reason the dated retrieval could not be answered, on top of the missing business date and currency.

**Documented requirement — why currency matters.** T2S provides for maintenance of individual settlement-currency-dependent cut-offs and events, but the Operator manages the settlement day on a **common schedule configured per settlement currency**: there is **no settlement-day schedule defined per currency**, only distinct individual cut-offs and events per currency. The multi-currency configuration allows flexibility within the boundaries of real-time settlement closure — start of the cut-off phase with **DVP cut-off at 16:00 hrs CET**, end of the cut-off phase at **18:00 hrs CET** with the FOP cut-off. The Operator is entitled to change some cut-offs and events (deadlines for receiving settlement instructions/restrictions for same-day settlement) independently for a settlement currency, in exceptional circumstances or contingency situations, on request from the relevant T2S-dependent external system (for example RTGS, CSD platform, CMS), under a procedure to be defined in the T2S Manual of Operational Procedures (MOP). The currency-dependent cut-offs and events named are: **DVP cut-off (IDVP / EDVP) — "remains harmonised for all currencies at 16h00"**; cash settlement restriction cut-off; settlement restrictions release; reimbursement of intraday credit; BATM (bilaterally agreed treasury management) cut-off; CBO (central bank operation) cut-off; optional cash sweep; inbound liquidity transfer cut-off; automated cash sweep. Such a change is valid **only for the current T2S settlement day**, and when a currency-dependent cut-off or event is extended for a currency, the start of its dependent processes (for example the cash sweep) is automatically extended for the same currency [[t2s-schedule-r2]] UDFS R2026.JUN, §1.4.2 and exception conditions; PDF 156–158; reviewed 2026-09-14; qualifications as above.

**Documented requirement — the conditions on any such change** [[t2s-schedule-r2]] UDFS R2026.JUN, §1.4.2; PDF 157–158; reviewed 2026-09-14; qualifications as above:

1. The sequence and order of events (predecessor and/or successor events) must remain unchanged — a currency-dependent cut-off cannot be delayed beyond a successor scheduling event where this would affect T2S processing (the UDFS example: a CBO cut-off for Danish krone cannot be extended beyond the T2S EOD cut-off, its successor in the scheduling). This includes no additions or removals of events, no change in event ordering and no change in event dependencies.
2. If T2S experiences a general issue across all currencies, the Operator may need to extend the EOD cut-off (T2S revised times would apply); in that case T2S ensures the sequence of the currency-independent cut-offs (securities settlement restriction cut-off and FOP cut-off) is not changed. Procedures for such an event are to be defined in the T2S MOP.
3. If late peak volume transactions arrive on a Friday evening and are not available for settlement at the regular NTS, the Operator would need to process additional NTS cycles; the procedure is defined in the T2S MOP.

**Documented requirement — process dependencies, which is why a delay propagates.** T2S controls execution so that the start of a subsequent process depends on completion of the current process and/or the occurrence of a cut-off; where a process depends on both a preceding process and a cut-off, it cannot start until the previous process has completed **and** the cut-off time has been reached [[t2s-schedule-r2]] UDFS R2026.JUN, §1.4.2; PDF 158; reviewed 2026-09-14; qualifications as above.

## Retrieval statuses (disclosed in full)

| Retrieval | Context | Status | Effect on this answer |
|---|---|---|---|
| 1 | T2S / settlement / participant / current, `t2s_baseline_schedule`, as of 2026-09-14 | **evidence_only** (schedule kind: **baseline**) | Supplies [[t2s-schedule-r2]]; all documented content above rests on it |
| 2 | T2S / settlement / participant / current, `dated_t2s_schedule`, as of 2026-09-14 | **needs_context** — "Actual schedules require business date and currency"; missing context fields: **business_date**, **currency** | Returned **no sections**. Nothing in this answer states an actual schedule for any dated day, and no deviation, delay or extension is asserted or denied for any date |

**Assumption I adopt, stated rather than hidden:** you are asking about the standing schedule of a normal T2S settlement day, in CET, for the release documented in the bundle (platform release R2026.JUN), and you are not asking me to confirm anything about one named calendar day. If you do want a named day, give me the business date and the settlement currency and the question must be re-run against a reviewed **event overlay** for that date — which this bundle does not contain.

**Bundle LIMITATION lines carried with every claim above** [[t2s-schedule-r2]]: (i) the section covers the same pages as the 13 September section `t2s-schedule`, with source bytes re-fetched and hash-identical on 14 September 2026; (ii) CET is the source convention, no UTC conversion; (iii) **the nominal schedule is not guaranteed execution and not a local participant cut-off, and dated queries require a reviewed event overlay for the same review date**. Review dates available in this bundle are 2026-09-13 and 2026-09-14; the section relied on is reviewed 2026-09-14 and its source was reviewed 2026-09-13. Stating those dates is not a statement that the schedule is unchanged on any later date.

## Unresolved requirements

- **The actual schedule for any named business date** (including 16 September 2026): not in reviewed evidence. No revised or effective times, no published deviation and no confirmation of a routine day are present. I therefore cannot say either that tomorrow will run to the nominal times or that it will not.
- **Whether a given calendar day is a T2S operating day for your currency**: the T2S operating day calendar by currency is referenced by §1.4.2 but is not in the bundle. Note the mandatory weekend maintenance window from 2:30 Saturday to 2:30 Monday as printed in Table 37, which bears on weekend dates.
- **Your own local participant deadlines.** No Euronext Securities (Milan, Copenhagen, Porto, Athens, Oslo) schedule or client cut-off table was retrieved. T2S nominal times are platform times; a CSD participant's send deadlines are typically earlier and are set by the CSD's own documentation — nothing in this bundle establishes them, and none should be inferred from the table above.
- **T2S MOP content** governing contingency extensions, additional Friday NTS cycles and the exceptional currency-cut-off procedure: named by the evidence, not contained in it.

## Open items

1. **Business date and settlement currency from you** (for example: business date 16 September 2026; currency EUR or DKK) — required context fields named by the `needs_context` retrieval; without them no dated schedule can be composed.
2. **Reviewed dated event overlay for the requested business date** at the same review date as the schedule section: official route — the T2S Operator's operational communications and the T2S operating day calendar by currency published on the ECB/Eurosystem T2S professional-use documentation pages (the source family of this section). Not in this bundle; the bundle names no gap id.
3. **T2S Manual of Operational Procedures (MOP)** for the contingency and exceptional cut-off-change procedures referenced in §1.4.2: official route — the Eurosystem T2S operational documentation.
4. **Local CSD settlement-day timetable and client cut-offs** for the CSD you actually instruct through: official route — that CSD's public documentation hub and its client platform (for example MT-X for Euronext Securities Milan). Client-only material is outside this bundle, and no local timetable is cited here.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.695392+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_baseline_schedule"}
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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule"}
STATUS: needs_context — Actual schedules require business date and currency.
MISSING CONTEXT FIELDS: ['business_date', 'currency']
ROUTER NOTES: {"_note": "relative date in the question; business date and currency deliberately left for the retriever to request"}

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
