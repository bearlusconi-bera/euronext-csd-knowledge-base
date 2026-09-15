You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What will the T2S settlement schedule be on 15 December 2026 for EUR?

# Case category: future-date (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "No reviewed event overlay exists for a future date; the actual schedule cannot be established; nominal baseline may be described only if explicitly nominal, noting R2026.NOV deployment planned in November could change it (planned, unverified)."
]
Fail conditions (must NOT appear):
[
  "Present the baseline as the schedule for 15 December."
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
# T2S settlement schedule on 15 December 2026 for EUR

## Direct answer

**Unresolved requirement.** The reviewed evidence cannot tell you what the T2S settlement schedule *will be* on 15 December 2026 for EUR. What the bundle does contain is the **nominal baseline** day structure of the T2S settlement day under platform release **R2026.JUN** — and a nominal baseline is not a forecast, not a guaranteed execution and not a local participant deadline. Two of the four retrievals for this question came back **blocked**: there is no reviewed event overlay and no reviewed status entry for business date 2026-12-15 in EUR (gap **G02** in both cases). A third retrieval shows that a *later* release, **R2026.NOV**, has been finally published but that its production deployment is **not verified** — so the bundle does not even establish which release's schedule will be in force on that date.

## 1. What is documented: the nominal baseline day (R2026.JUN)

**Documented requirement** — the periods and nominal times of the T2S settlement day, as printed in the bundle:

| T2S timeline (CET) | Period | Selected content printed in the evidence |
|---|---|---|
| 18:45 – 20:00 | Start of day (SOD) | Change of business date; common Snapshot (T2S and T2); preparation for night-time settlement; revalidation of instructions/restrictions/amendments/hold-and-release that failed to settle as of their intended settlement date; at **19:00** final deadline to accept data feeds from collateral management systems and payment/settlement banks (securities valuations ideally by **17:45**, accepted until 19:00); at **20:00** final deadline to accept settlement instructions for processing in sequence 1 of the first night-time cycle; valuation of securities positions and of collateral-eligible settlement instructions |
| 20:00 – 3:00 | Night-time settlement (NTS) | Two cycles. First cycle: sequences 0, 1, 2, 3, 4, with reporting and static-data maintenance processing at the end of each sequence; duration depends on volumes but "should finish by **20:20** (target objective)" absent above-standard peak volumes. Last cycle: sequences 4, X (partial settlement on all unsettled eligible instructions), Y (reimbursement of "multiple liquidity providers"), Z (liquidity transfers); should finish by **00:00** (target objective) on the same condition |
| 3:00 – 5:00 | Maintenance window (MWI) | The optional daily maintenance window |
| 2:30 Saturday – 2:30 Monday | Maintenance window (MWI) | The mandatory weekend maintenance window |
| 5:00, or after NTS if NTS ends before 3:00 | Real-time settlement (RTS) | RTS preparation; penalty mechanism processing (**7:30** final deadline for penalty reference data and start of penalty reference-data preparation; **8:30** final deadline for completing penalty eligibility, which starts at **19:30** or after SOD completes; **8:30** on the 14th business day of the month, start of monthly reporting of aggregated penalty amounts, to be completed by **21:30**; penalty calculation/recalculation/reporting starts after the modification-request and eligibility steps but **not before 9:15**; on the 13th business day of the month the end-of-appeal-period process runs after recalculation); real-time settlement with **5 partial settlement windows**; real-time settlement closure |
| 18:00 – 18:45 | End of day (EOD) | Stop of the settlement engine; internal T2S securities-accounts consistency check; recycling and purging; end-of-day reporting and statements |

[[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), Table 37; PDF 160–163; reviewed 14 September 2026 (source reviewed 13 September 2026); body language en, authoritative language None, translation status not independently established, approval: source identity checked, no independent whole-edition supervisory approval certification.

[[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.4.1; PDF 163; reviewed 14 September 2026 (source reviewed 13 September 2026); body language en, authoritative language None, translation status not independently established, approval: source identity checked, no independent whole-edition supervisory approval certification — for the rule that the SOD period starts after the successful completion of the previous EOD period and after 18:45, and is followed by the night-time settlement period.

### 1.1 The EUR-specific part of the answer

**Documented requirement.** There is **no schedule of a settlement day defined per currency** in T2S; the T2S Operator manages the overall processing of a settlement day on a **common T2S schedule** configured for each T2S settlement currency, while **distinct individual cut-offs and events per currency** are defined. The multi-currency configuration is flexible only "within the boundaries of the real-time settlement closure (start of cut-off phase with **DVP cut-off at 16:00 hrs CET** and end of cut-off phase at **18:00 hrs CET** with **FOP cut-off**)". The DVP cut-off (IDVP / EDVP) "remains harmonised for all currencies at 16h00". The other currency-dependent cut-offs and events named are: cash settlement restriction cut-off; settlement restrictions release; reimbursement of intraday credit; BATM (Bilaterally Agreed Treasury Management) cut-off; CBO (Central Bank Operation) cut-off; optional cash sweep; inbound liquidity transfer cut-off; automated cash sweep. [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.2 and exception conditions; PDF 156–158; reviewed 14 September 2026 (source reviewed 13 September 2026); body language en, authoritative language None, translation status not independently established, approval: source identity checked, no independent whole-edition supervisory approval certification.

**Reasoned inference** (derived from the §1.4.2 excerpt above): because the DVP cut-off is harmonised across currencies and there is no per-currency day schedule, the *baseline* EUR day is the common baseline day in the table in section 1 — asking "the EUR schedule" does not, on this evidence, produce a separate EUR timetable. The EUR-specific content would sit in the individual currency-dependent cut-offs listed above, and the bundle prints a value for only one of them (DVP at 16:00 CET). No EUR values for the cash settlement restriction cut-off, settlement restrictions release, intraday-credit reimbursement, BATM cut-off, CBO cut-off, optional cash sweep, inbound liquidity transfer cut-off or automated cash sweep are in reviewed evidence.

### 1.2 Why these times are not the answer to a dated question

**Documented requirement.** T2S manages each transition between periods as an event with a **planned time**, a **revised time** and an **effective time**. The planned time is the standard schedule applied by default; the T2S Operator can update it for a permanent change. The **revised time** is the foreseen time for the current settlement day, which usually coincides with the planned time "except when a delay has occurred"; in contingency situations the Operator updates the revised time while the planned time is unchanged. The **effective time** is the time of actual occurrence during the current settlement day. The Operator is entitled to change some cut-offs and events for a single T2S settlement currency, in exceptional circumstances or contingency situations, on request from the relevant dependent external system (RTGS, CSD platform, CMS), under conditions that preserve event sequence and dependencies; such changes are valid only for the current T2S settlement day. Late Friday-evening peak volume can require additional NTS cycles. The start of a subsequent process depends on completion of the current process and/or the occurrence of a cut-off, and cannot start before both. [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.2 and exception conditions; PDF 156–158; reviewed 14 September 2026 (source reviewed 13 September 2026); body language en, authoritative language None, translation status not independently established, approval: source identity checked, no independent whole-edition supervisory approval certification.

**Qualifications that travel with every time above** (LIMITATION lines on [[t2s-schedule-r2]]):

- The nominal schedule is **not guaranteed execution and not a local participant cut-off**. Dated queries require a reviewed event overlay for the same review date.
- **CET is the source convention**; no UTC conversion is available in the evidence. (So no CET/CEST or local-time conversion for a December date can be given from this bundle.)
- The section covers the same pages as the 13 September section `t2s-schedule`; the source bytes were re-fetched and were hash-identical on 14 September 2026.

## 2. What is blocked

Both dated retrievals returned **blocked**, and this is the substance of the answer, not a footnote:

- **Retrieval 2 — dated T2S schedule, EUR, business date 2026-12-15: BLOCKED.** "No reviewed event overlay for this schedule, business date and currency. Nominal evidence alone cannot establish actual operations." Gap id **G02**.
- **Retrieval 3 — T2S status history, business date 2026-12-15, EUR: BLOCKED.** "No reviewed status entry for this business date and currency. Absence from the reviewed capture is not evidence of routine operations." Gap id **G02**.

**Unresolved requirement.** Accordingly: the actual (revised/effective) times for 15 December 2026 in EUR are not in reviewed evidence; no deviation, extension, contingency or additional NTS cycle can be either asserted or ruled out; and the absence of an entry must not be read as "the day ran to the nominal timetable".

**Unresolved requirement.** Whether 15 December 2026 is a **T2S operating day for EUR** at all is also not in reviewed evidence — the bundle contains no T2S operating day calendar by currency for December 2026, and the excerpt states only that T2S ensures the schedule conforms to that calendar. *Explanation, not a documented requirement:* the baseline table's mandatory weekend window (2:30 Saturday to 2:30 Monday) shows the day structure only applies on an operating day, so the calendar is a genuine precondition rather than a formality.

## 3. The release problem: which schedule would even apply in December 2026

**Documented requirement.** The **T2S UDFS R2026.NOV** and UHB R2026.NOV (together with GFS, DMT, URD, BFD and the BDM/BILL/CRDM/ESMIG UDFS and User Handbooks) were **finally published**, per a cover note dated 14 September 2026; the UDFS R2026.NOV document itself carries the date 11 September 2026. Draft intermediate versions were published on 31 July 2026 and reviewed from 3 to 21 August 2026; the final versions incorporate Change Requests in the scope of T2S Release 2026.NOV, including editorial Change Requests approved by the CSD Steering Group until 23 July 2026. [[november-final-release]] Cover Note, PDF page 1 (final-publication statement, dated 14 September 2026); reviewed 14 September 2026; version R2026.NOV final publication with no production-deployment certification; body language en, authoritative language en, original or official-language text; approval: final document delivery confirmed, production deployment not verified. [[november-final-release]] T2S User Detailed Functional Specifications R2026.NOV (UDFS), PDF page 1 (document identity/date, 11 September 2026); reviewed 14 September 2026; version R2026.NOV final publication with no production-deployment certification; body language en, authoritative language en, original or official-language text; approval: final document delivery confirmed, production deployment not verified.

**Qualifications that travel with this** (LIMITATION lines on [[november-final-release]]): final publication is established but **November production deployment is not verified**; the 14 September cover/listing, the 11 September UDFS date and the earlier target are **separate facts**; and **only cover-page statements are admitted** — no November operational provisions, payloads or changed message versions are in reviewed evidence.

**Reasoned inference** (derived from the two points above — a baseline schedule reviewed only for R2026.JUN, plus a finally published R2026.NOV whose deployment is unverified): for a business date in December 2026 the bundle does not establish which release governs the schedule. Were R2026.NOV to reach production before 15 December 2026 — which is not evidenced and not planned-dated anywhere in this bundle — the day structure in force could differ from the R2026.JUN table in section 1, and the bundle admits **no** R2026.NOV schedule content with which to check that. Publication is not deployment, and no planned deployment date for R2026.NOV appears in the bundle's release-status evidence.

**Unresolved requirement.** Any R2026.NOV change to periods, cut-offs, sequences or currency-dependent events — and the deployment date itself — is not in reviewed evidence.

## 4. How to state this safely to a client

**Proposed design choice** (an implementation/communication decision, not an infrastructure rule): if a schedule must be quoted for 15 December 2026 before the missing evidence exists, quote it as *"the R2026.JUN nominal baseline, reviewed 14 September 2026, subject to (a) confirmation that 15 December 2026 is a T2S operating day for EUR, (b) the R2026.NOV deployment status, and (c) the revised/effective times published for that business date"* — and never as the schedule for that date. Any operational commitment (client-facing deadlines, batch windows, staffing) should be pinned to your own local CSD cut-offs, which are earlier than and distinct from T2S nominal times and are not in this bundle.

## Notes on the bundle itself

- Retriever build ed577c2eb315; bundle generated 2026-09-15T09:18:14Z; retrieval context `as_of` 2026-09-14. Review dates available in the library: 2026-09-13 and 2026-09-14. The sections used here are reviewed 2026-09-14. **Evidence reviewed on 14 September 2026 is not "current as at today" merely because time has passed.**
- The router recorded: "future business date: nominal baseline retrieved without the date; the dated route reports the missing overlay separately", and "dated status entries retrieved alongside the dated schedule route (v1.1)". This matches the observed pattern: the baseline was returned, the dated routes were blocked.
- **Routing observation:** this run is router-only and no re-retrieval was performed. The routing is coherent for the question asked; the one thing a dated future-date question would also want — a T2S operating day calendar by currency for December 2026 and an R2026.NOV deployment/planned-deployment status section — was not retrieved by any of the four retrievals, so both remain unresolved rather than blocked-with-a-gap-id.
- No excerpt in this bundle contained instruction-like content directed at the reader.

## Open items

1. **Reviewed event overlay for T2S business date 2026-12-15, currency EUR** — required to state planned vs revised vs effective times for that day. Gap **G02**. Official route: the T2S operational information/status pages on the ECB T2S professional-use documents hub, captured and reviewed for the relevant knowledge date.
2. **Reviewed status entry (status history) for 2026-12-15, EUR** — required before any statement that the day ran to baseline or deviated. Gap **G02**. Same official route.
3. **T2S operating day calendar by currency covering December 2026** — required to establish that 15 December 2026 is a settlement day for EUR. Not in reviewed evidence; no gap id named in the bundle. Official route: ECB T2S public documentation hub (operating day calendar).
4. **R2026.NOV deployment status and planned deployment date** — required to know which release's schedule governs 15 December 2026. Currently only cover-page final-publication statements are admitted, with production deployment not verified. Official route: T2S Plan / Service Transition Plans and Release Notes for R2026.NOV via the ECB T2S hub, reviewed and admitted as release-status evidence.
5. **R2026.NOV schedule provisions (equivalent of §1.4.2, Table 37, §1.4.4.1)** — required to compare the November day structure with the R2026.JUN baseline. Explicitly excluded by the bundle's limitation that only cover-page statements are admitted for R2026.NOV.
6. **EUR values for the currency-dependent cut-offs and events other than the DVP cut-off** (cash settlement restriction cut-off, settlement restrictions release, reimbursement of intraday credit, BATM cut-off, CBO cut-off, optional cash sweep, inbound liquidity transfer cut-off, automated cash sweep) — named in the evidence but not timed. Official route: the T2S UDFS currency-dependent cut-off tables and the T2S Manual of Operational Procedures (T2S MOP), which the excerpt names as the place where the exceptional change procedure is defined; the MOP is not in reviewed evidence.
7. **Your own local CSD's client cut-offs** (Euronext Securities Milan, Copenhagen, Porto, Athens or Oslo, as applicable) — not in this bundle and not derivable from T2S nominal times. Official route: the relevant CSD's client documentation platform or documentation service.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.882466+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_baseline_schedule", "schedule_kind": "baseline"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline
ROUTER NOTES: {"_note": "future business date: nominal baseline retrieved without the date; the dated route reports the missing overlay separately"}

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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule", "currency": "EUR", "business_date": "2026-12-15"}
STATUS: blocked — No reviewed event overlay for this schedule, business date and currency. Nominal evidence alone cannot establish actual operations.
GAP IDS: ['G02']

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_status_history", "business_date": "2026-12-15", "currency": "EUR"}
STATUS: blocked — No reviewed status entry for this business date and currency. Absence from the reviewed capture is not evidence of routine operations.
GAP IDS: ['G02']
ROUTER NOTES: {"_note": "dated status entries retrieved alongside the dated schedule route (v1.1)"}

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "future", "question_type": "release_status"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
ROUTER NOTES: {"_note": "future business date: release status retrieved for planned changes"}

--- SECTION [[november-final-release]] — November final publication confirmed on 14 September; deployment unverified (reviewed 2026-09-14; modes ['reference', 'future']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: Cover Note | PDF page 1: final-publication statement, dated 14 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf?1d8ee68f0593cb88571835efb7cd5ed8
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) | PDF page 1: document identity/date, 11 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: Final publication is established; November production deployment is not verified.
LIMITATION: The 14 September cover/listing, 11 September UDFS date and earlier target are separate facts.
LIMITATION: Only cover-page statements are admitted. No November operational provisions, payloads or changed message versions are admitted.
EXCERPT (PDF page 1: final-publication statement, dated 14 September 2026):
[PDF page 1]
              
                 
 
 
 
 
ECB-PUBLIC 
 
14 September 2026 
 
Delivery of the T2S UDFS R2026.NOV and UHB R2026.NOV 
As envisaged in the T2S Plan, we have published final versions of the: 
• 
T2S User Detailed Functional Specifications R2026.NOV (UDFS R2026.NOV) 
• 
T2S User Handbook R2026.NOV (UHB R2026.NOV) 
• 
T2S General Functional Specifications R2026.NOV (GFS R2026.NOV) 
• 
T2S Data Migration Tool R2026.NOV (DMT R2026.NOV) 
• 
T2S User Requirements Document R2026.NOV (URD R2026.NOV) 
• 
T2S Business Functionality for T2S Graphical User Interface R2026.NOV (BFD R2026.NOV) 
• 
BDM User Detailed Functional Specifications R2026.NOV 
• 
BILL User Detailed Functional Specifications R2026.NOV 
• 
CRDM User Detailed Functional Specifications R2026.NOV 
• 
ESMIG User Detailed Functional Specifications R2026.NOV 
• 
BDM User Handbook R2026.NOV 
• 
BILL User Handbook R2026.NOV 
• 
CRDM User Handbook Book 1 R2026.NOV 
• 
CRDM User Handbook Book 2 R2026.NOV 
 
For the convenience of the readers, all changes in the documents were highlighted in revision marks. 
Additionally, we added the appropriate CR references. 
The draft intermediate versions of these documents were published on 31 July and were reviewed from 03 
August 2026 to 21 August 2026. The comments from the market participants have been taken into account for 
the final versions to be published on 11 September 2026. 
Scope of the delivery 
These new versions incorporate Change Requests in the scope of the T2S Release 2026.NOV, including the 
editorial Change Requests approved by the CSD Steering Group (CSG) until 23 July 2026.  
The exhaustive list of all Change Requests is provided as Annex A to this cover note.  
Complementing the information provided in the Service Transition Plans, the Release Notes and the UDFS 
itself, a list containing all the T2S messages with their respective links to MyStandards is provided as Annex 
B to the Cover Note.
EXCERPT (PDF page 1: document identity/date, 11 September 2026):
[PDF page 1]
Author
Version
Identifier
Date
4CB
R2026.NOV
T2S UDFS
11 September 2026
User Detailed Functional Specifications

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
