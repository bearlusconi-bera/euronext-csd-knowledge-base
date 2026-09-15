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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:58:13.830989+00:00). Review dates available: 2026-09-13, 2026-09-14.

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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
