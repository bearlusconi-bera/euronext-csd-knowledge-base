You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Was T2S operating normally on 9 September 2026 for EUR settlement?

# Case category: dated-routine (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "The captured status history contains only routine entries for 9 September 2026; this shows no deviation was published, not that every event ran on time.",
  "Currency scope ALL."
]
Fail conditions (must NOT appear):
[
  "Claim proof that all cut-offs ran on time."
]
Expected sections (if any): ['t2s-status-routine-2026', 't2s-schedule-r2']
Expected retrieval statuses: ['evidence_only']

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
# Was T2S operating normally on 9 September 2026 for EUR settlement?

## Direct answer

What the reviewed evidence supports is narrower than "operating normally": **no incident and no schedule-change entry was published for T2S business date 9 September 2026** on the ECB T2S status history page as captured on 14 September 2026, so **no deviation was announced** for that date. That is not the same as proof that every event of that settlement day occurred at its planned time, and the reviewed status list is not segmented by currency, so it is not an EUR-specific attestation. No effective (actual) event times for 9 September 2026 are in reviewed evidence.

**Retrieval status disclosure.** The bundle contains one retrieval, context `{"as_of":"2026-09-14","entity":"T2S","service":"settlement","role":"participant","mode":"current","question_type":"dated_t2s_schedule","currency":"EUR","business_date":"2026-09-09"}`, status **`evidence_only`**, schedule kind **actual**. No retrieval returned `blocked`, `needs_context` or `needs_refresh`. Knowledge base as of 2026-09-13; review dates available 2026-09-13 and 2026-09-14; both sections used here carry the review date **14 September 2026**.

## 1. What the dated status evidence establishes — Documented requirement (as a dated fact)

**Documented (dated) fact.** T2S business date 2026-09-09 appears in the derived list of 2026 weekday business dates for which the captured ECB status history contains **only routine entries** (operating normally / closed per schedule) and **no incident or schedule-change entry attributed to that date**. [[t2s-status-routine-2026]] ECB T2S status history 2026 (capture of 14 September 2026), locator: derived list of weekday business dates with routine-only entries, capture of 14 September 2026; section reviewed 14 September 2026; applicability basis `reference_description`; body language English, authoritative language not stated in the citation, translation status "not independently established"; approval: source identity checked, no independent whole-edition supervisory approval certification; source https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html, captured file hash recorded in the excerpt.

Qualifications that travel with that fact, taken from the section's own LIMITATION lines and the capture metadata:

- **It proves absence of a published deviation, not punctual execution.** LIMITATION: "Supports only the proposition that no incident or schedule change was published on the status page for that date; it does not prove every event ran exactly on time." The excerpt repeats this: absence of a published incident entry "does not prove that every event occurred exactly at its planned time".
- **Holiday caveat.** LIMITATION: "Weekday public holidays appear only if the page carried a routine entry for them; check the T2S calendar separately." The T2S operating day calendar was not retrieved in this bundle, so this answer does not establish whether 9 September 2026 was an opening day for EUR from the calendar side — only that the status page carried routine-only entries for it.
- **Currency scope.** The derived list carries `currency_scope: "ALL"`; it is not broken down per settlement currency. **Reasoned inference** (derived from that field plus the "no incident or schedule-change entry attributed to that date" wording): since the capture records no incident or schedule-change entry of any kind for that business date, no EUR-specific deviation was published either. What the evidence cannot do is confirm EUR-specific effective times, EUR cut-off extensions agreed bilaterally without a status publication, or anything about a participant's own CSD.
- **Time zone.** Capture note: "Displayed ECB timestamps preserved; time zone not stated on the page; UTC conversion not verified." The UDFS section separately states that CET is the source convention and that no UTC conversion is provided.
- **Business-date attribution is an inference, not source text.** Capture note: "Evening entries about night processes are attributed to the next T2S settlement day; this is a labelled inference from the UDFS schedule, not source text. Weekend calendar dates carry closure/maintenance statements and are not T2S business days." So the mapping between a page entry timestamped on a calendar evening and the T2S business date it belongs to is itself a labelled inference in the source capture.

**Observation from the same excerpt — Unresolved requirement.** The calendar weekday **2026-09-08 is not in the routine-only list**, while 2026-09-07, 2026-09-09, 2026-09-10, 2026-09-11 and 2026-09-14 are. Twenty-five 2026 weekdays up to the capture date are absent from the list in the same way. The reviewed evidence does not say why any given weekday is absent: an absence is consistent with a published incident or schedule-change entry, with a weekday public holiday that carried no routine entry (per the LIMITATION above), or with no entry at all. This matters for the question because, under the UDFS day structure below, the settlement day for business date 9 September 2026 opened on the preceding calendar evening. No section in this bundle describes what, if anything, the status page says for 8 September 2026, so this is left as an open item rather than an assertion.

## 2. The baseline day against which "normal" would be judged — Documented requirement

**Documented requirement (nominal baseline, not an attendance record).** [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.2 and exception conditions, PDF 156–158; Table 37, PDF 160–163; §1.4.4.1, PDF 163; version R2026.JUN; section reviewed 14 September 2026 (source reviewed 13 September 2026, with the LIMITATION line recording that the source bytes were re-fetched and hash-identical on 14 September 2026); platform release R2026.JUN; body language English, authoritative language not stated, translation status "not independently established"; approval: source identity checked, no independent whole-edition supervisory approval certification.

| Period | Nominal timeline (CET, source convention) | Notes from the excerpt | Label |
|---|---|---|---|
| Start of day (SOD) | 18:45 – 20:00 | Change of T2S business date, common snapshot (T2S and T2), revalidation and preparation for night-time settlement; 19:00 final deadline for data feeds effective for the current business date; 20:00 final deadline to accept instructions for sequence 1 of the first night-time cycle. §1.4.4.1 adds that SOD starts after the successful completion of the previous EOD period **and** after 18:45. | Documented requirement |
| Night-time settlement (NTS) | 20:00 – 3:00 | Two cycles; first cycle sequences 0–4, "should finish by 20:20 (target objective) as long as standard peak volumes are not exceeded"; last cycle sequences 4, X (partial settlement), Y, Z, "should finish by 00:00 (target objective)". | Documented requirement |
| Maintenance window (MWI) | 3:00 – 5:00 daily (optional); 2:30 Saturday – 2:30 Monday (mandatory weekend) | As printed in Table 37. | Documented requirement |
| Real-time settlement (RTS) | From 5:00, or after NTS if NTS ends before 3:00 | RTS preparation, penalty mechanism processing, real-time settlement with 5 partial settlement windows, real-time settlement closure. | Documented requirement |
| End of day (EOD) | 18:00 – 18:45 | Stop of settlement engine, internal securities accounts consistency check, recycling and purging, EOD reporting and statements. | Documented requirement |

**Documented requirement — currency boundaries relevant to a EUR question.** The multi-currency configuration allows flexibility "within the boundaries of the real-time settlement closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET with FOP cut-off)", and the DVP cut-off (IDVP/EDVP) "remains harmonised for all currencies at 16h00". There is no schedule of a settlement day defined per currency in T2S; distinct individual cut-offs and events per currency are defined. Same section, §1.4.2, PDF 156–158.

**Documented requirement — why "normal" is a three-time concept.** For each event T2S manages a **planned time** (the standard schedule applied by default; changed only for a permanent schedule change), a **revised time** (the foreseen time for the current settlement day, usually coinciding with the planned time "except when a delay has occurred" — in contingency situations the operator updates the revised time while the planned time is unchanged) and an **effective time** (the time of the actual occurrence of the event during the current settlement day). Same section, §1.4.2, PDF 156.

**Reasoned inference** (derived from that three-time model plus the status-page LIMITATION): a statement that T2S "operated normally" on a given date would properly mean that the effective times for that settlement day matched the planned times. The reviewed evidence contains **no revised or effective times for 9 September 2026** — only the absence of a published deviation. So the supportable statement is "no deviation was published", not "every event ran on time".

**Documented requirement — what a published deviation could have looked like.** The T2S Operator is entitled to change some cut-offs and events (deadlines for receiving settlement instructions/restrictions for same-day settlement) of a settlement day, independently for a T2S settlement currency, in exceptional circumstances or contingency situations, based on a request from the relevant T2S dependent external system (RTGS, CSD platform, CMS), under a procedure to be defined in the T2S Manual of Operational Procedures (T2S MOP). The currency-dependent cut-offs and events listed are: DVP cut-off (IDVP/EDVP), cash settlement restriction cut-off, settlement restrictions release, reimbursement of intraday credit, BATM (Bilaterally Agreed Treasury Management) cut-off, CBO (Central Bank Operation) cut-off, optional cash sweep, inbound liquidity transfer cut-off, automated cash sweep. Such changes are valid only for the current T2S settlement day, and when a currency-dependent cut-off or event is extended for a currency the start of its dependent processes (for example the cash sweep) is automatically extended for the same currency. Conditions: the sequence and order of events must remain unchanged (a currency-dependent cut-off cannot be delayed beyond a successor scheduling event where that would affect T2S processing; no additions or removals of events, no change in ordering or dependencies); in exceptional cases of a general issue across all currencies the operator may need to extend the EOD cut-off (revised times would apply) while keeping the sequence of the currency-independent securities settlement restriction cut-off and FOP cut-off unchanged; and late Friday-evening peak volumes not available at the regular NTS may require processing into additional NTS cycles per the MOP. Same section, §1.4.2, PDF 157–158. **None of these exceptional measures is recorded for 9 September 2026 in the reviewed evidence** — and, by the status-page LIMITATION, the absence of a published entry is the only thing established.

**Reasoned inference — the day boundary.** Combining §1.4.4.1 ("The SOD period starts after the successful completion of the previous EOD period and after 18:45") with Table 37 (SOD 18:45–20:00 including the change of business date; NTS 20:00–3:00), the T2S settlement day carrying business date 9 September 2026 began on the preceding calendar evening and its night-time settlement ran across that night. This is an inference from those two excerpts, consistent with the capture's own attribution note; the excerpts do not state it as a sentence about 9 September 2026.

## 3. Qualifications that must stay attached

- **Nominal is not actual.** LIMITATION on [[t2s-schedule-r2]]: "Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date." The event overlay used here is the 14 September 2026 status capture in [[t2s-status-routine-2026]], and its evidential reach is limited to "no deviation published".
- **Not a participant deadline.** Nothing above is a Euronext Securities (Milan, Copenhagen, Porto, Athens, Oslo) client cut-off. Local CSD cut-offs, and any local notice for 9 September 2026, are not in this bundle.
- **CET only.** LIMITATION on [[t2s-schedule-r2]]: "CET is the source convention; no UTC conversion." All times above are as printed in the UDFS.
- **Release identity.** The schedule evidence is the R2026.JUN UDFS, the platform release recorded on the section. Any later release is a separate matter and is not addressed by this bundle.
- **Section overlap.** LIMITATION on [[t2s-schedule-r2]]: "Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026." This is a re-verification of the same pages, not new content.
- **No supervisory approval certification.** Both sections carry "Source identity checked; no independent whole-edition supervisory approval certification", and both citations record translation status "not independently established".

## 4. Bottom line by label

- **Documented (dated) fact:** no incident or schedule-change entry was published for T2S business date 9 September 2026 in the ECB status history as captured on 14 September 2026 [[t2s-status-routine-2026]].
- **Documented requirement:** the nominal R2026.JUN day structure and the currency-dependent cut-off regime, including the harmonised DVP cut-off at 16:00 and the 18:00 FOP cut-off boundary [[t2s-schedule-r2]].
- **Reasoned inference:** no EUR-specific deviation was published either, because the capture is currency-scope ALL and records no entry of that kind for the date.
- **Unresolved requirement:** whether every event of that settlement day occurred at its planned time (no effective times in evidence); whether 9 September 2026 was an opening day per the T2S operating day calendar for EUR (calendar not retrieved); why calendar weekday 8 September 2026 is absent from the routine-only list; and anything about local CSD operations on that date.

## Open items

1. **Effective (actual) event times for T2S business date 9 September 2026, EUR** — needed to say more than "no deviation published". Route: ECB T2S operational information/status history detail and, for participants, the T2S operational communications received via their CSD or directly connected party channel; not retrievable from the sections in this bundle.
2. **T2S operating day calendar for 2026** — needed to confirm 9 September 2026 was an opening day and to apply the holiday LIMITATION on [[t2s-status-routine-2026]]. Route: the public T2S calendar on the ECB TARGET documentation hub.
3. **Status-page content for calendar date 8 September 2026** (absent from the routine-only list, the calendar evening on which the 9 September settlement day opened) — not covered by any section in this bundle. Route: a reviewed capture of the same ECB status history filtered to that date, at the same review date.
4. **T2S Manual of Operational Procedures (T2S MOP)** — the UDFS defers the exceptional cut-off-extension and additional-NTS-cycle procedures to it; the MOP is not in this bundle. Route: the ECB T2S professional-use documentation set.
5. **Local Euronext Securities notices for 9 September 2026** and local participant cut-offs — not retrieved; these would be needed before telling a client anything about their own deadlines. Route: each CSD's public notices hub and client platform.
6. **Gap ids**: the retrieval records none (`gap_ids` is null); the constraints above are the sections' LIMITATION lines and the capture's own limitation text.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.450788+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule", "currency": "EUR", "business_date": "2026-09-09"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: actual

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

--- SECTION [[t2s-status-routine-2026]] — T2S business dates with only routine ECB status entries (14 September capture) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reference_description)
CITATION: ECB T2S status history 2026 (capture of 14 September 2026) | Derived list of weekday business dates with routine-only entries; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html
LIMITATION: Supports only the proposition that no incident or schedule change was published on the status page for that date; it does not prove every event ran exactly on time.
LIMITATION: Weekday public holidays appear only if the page carried a routine entry for them; check the T2S calendar separately.
EXCERPT (Derived list of weekday business dates with routine-only entries; capture of 14 September 2026):
{
  "source_id": "ecb-status-2026-20260914",
  "source_url": "https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html",
  "captured_on": "2026-09-14",
  "captured_file": "implementation/2026-09-14-settlement-agent/hubs/ecb-t2s-status-2026.html",
  "captured_sha256": "3377fac2c74fa893d9c8ebac5233cedd29ad73ab94fe911caa299c3ed7a24ec8",
  "timezone_note": "Displayed ECB timestamps preserved; time zone not stated on the page; UTC conversion not verified.",
  "attribution_note": "t2s_business_date follows the rule in attribution_basis. Evening entries about night processes are attributed to the next T2S settlement day; this is a labelled inference from the UDFS schedule, not source text. Weekend calendar dates carry closure/maintenance statements and are not T2S business days.",
  "kind": "routine_status_only_business_dates",
  "description": "T2S weekday business dates in 2026 up to the capture date for which the captured ECB status history contains only routine entries (operating normally / closed per schedule) and no incident or schedule-change entry attributed to that date.",
  "currency_scope": "ALL",
  "business_dates": [
    "2026-01-01",
    "2026-01-02",
    "2026-01-05",
    "2026-01-06",
    "2026-01-07",
    "2026-01-08",
    "2026-01-09",
    "2026-01-12",
    "2026-01-13",
    "2026-01-14",
    "2026-01-15",
    "2026-01-20",
    "2026-01-21",
    "2026-01-22",
    "2026-01-23",
    "2026-01-27",
    "2026-01-28",
    "2026-01-29",
    "2026-01-30",
    "2026-02-02",
    "2026-02-03",
    "2026-02-04",
    "2026-02-05",
    "2026-02-06",
    "2026-02-10",
    "2026-02-11",
    "2026-02-12",
    "2026-02-13",
    "2026-02-16",
    "2026-02-17",
    "2026-02-18",
    "2026-02-19",
    "2026-02-20",
    "2026-02-23",
    "2026-02-24",
    "2026-02-26",
    "2026-02-27",
    "2026-03-03",
    "2026-03-04",
    "2026-03-05",
    "2026-03-06",
    "2026-03-09",
    "2026-03-10",
    "2026-03-11",
    "2026-03-12",
    "2026-03-13",
    "2026-03-17",
    "2026-03-18",
    "2026-03-19",
    "2026-03-20",
    "2026-03-24",
    "2026-03-25",
    "2026-03-26",
    "2026-03-27",
    "2026-03-31",
    "2026-04-01",
    "2026-04-02",
    "2026-04-03",
    "2026-04-06",
    "2026-04-07",
    "2026-04-08",
    "2026-04-09",
    "2026-04-10",
    "2026-04-13",
    "2026-04-15",
    "2026-04-16",
    "2026-04-17",
    "2026-04-20",
    "2026-04-23",
    "2026-04-24",
    "2026-04-28",
    "2026-04-29",
    "2026-04-30",
    "2026-05-01",
    "2026-05-04",
    "2026-05-05",
    "2026-05-06",
    "2026-05-07",
    "2026-05-08",
    "2026-05-11",
    "2026-05-12",
    "2026-05-13",
    "2026-05-14",
    "2026-05-15",
    "2026-05-19",
    "2026-05-20",
    "2026-05-21",
    "2026-05-22",
    "2026-05-25",
    "2026-05-26",
    "2026-05-27",
    "2026-05-28",
    "2026-05-29",
    "2026-06-01",
    "2026-06-02",
    "2026-06-03",
    "2026-06-04",
    "2026-06-05",
    "2026-06-08",
    "2026-06-09",
    "2026-06-11",
    "2026-06-16",
    "2026-06-17",
    "2026-06-18",
    "2026-06-19",
    "2026-06-22",
    "2026-06-23",
    "2026-06-24",
    "2026-06-25",
    "2026-06-26",
    "2026-06-30",
    "2026-07-02",
    "2026-07-03",
    "2026-07-07",
    "2026-07-09",
    "2026-07-10",
    "2026-07-15",
    "2026-07-16",
    "2026-07-17",
    "2026-07-20",
    "2026-07-21",
    "2026-07-22",
    "2026-07-23",
    "2026-07-24",
    "2026-07-27",
    "2026-07-28",
    "2026-07-29",
    "2026-07-30",
    "2026-07-31",
    "2026-08-03",
    "2026-08-04",
    "2026-08-05",
    "2026-08-06",
    "2026-08-07",
    "2026-08-10",
    "2026-08-11",
    "2026-08-12",
    "2026-08-13",
    "2026-08-14",
    "2026-08-17",
    "2026-08-18",
    "2026-08-19",
    "2026-08-20",
    "2026-08-21",
    "2026-08-24",
    "2026-08-25",
    "2026-08-27",
    "2026-08-28",
    "2026-08-31",
    "2026-09-01",
    "2026-09-02",
    "2026-09-03",
    "2026-09-04",
    "2026-09-07",
    "2026-09-09",
    "2026-09-10",
    "2026-09-11",
    "2026-09-14"
  ],
  "limitation": "Absence of a published incident entry shows that no deviation was announced on the status page as captured; it does not prove that every event occurred exactly at its planned time, and weekday public holidays on which T2S was closed are included only if the page carried a routine entry."
}

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
