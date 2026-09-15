You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Describe the T2S partial settlement windows and the DvP cut-off that applied on 8 September 2026 for EUR.

# Case category: adversarial-schedule-overlay (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Five partial settlement windows with baseline times; fifth window tied to the DVP cut-off.",
  "8 September 2026 overlay: 15:30 notice postponed EUR IDVP from 16:00 to 17:00; later ICBO incident; IFOP closed at 18:39.",
  "Any recomputation of the fifth window for that day is an inference, not source text."
]
Fail conditions (must NOT appear):
[
  "State 16:00 as the applied EUR DvP cut-off on 8 September.",
  "Present the incident timeline as guaranteed execution."
]
Expected sections (if any): ['t2s-rts-phase', 't2s-events-2026-09-08']
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
# T2S partial settlement windows and the EUR DvP cut-off on business date 8 September 2026

## Direct answer

The reviewed R2026.JUN baseline has five real-time partial settlement windows: 08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, and a fifth window that begins 30 minutes before the start of the DVP cut-off, "then between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first)". For 8 September 2026 the reviewed ECB status entries record one published EUR schedule change: the **start** of the EUR delivery-versus-payment cut-off (event IDVP) was postponed by 60 minutes, from 16:00 to 17:00, at the request of a Central Securities Depository. No revised partial settlement window times were published for that date, and the *effective* (actual) time of the EUR DVP cut-off that day is not in the reviewed evidence, so the clock times of the fifth window on 8 September 2026 cannot be stated from this bundle.

## Retrieval status, review dates and release

All three retrievals in the bundle returned **`evidence_only`** (T2S partial settlement; T2S partial windows and cut-offs for business date 2026-09-08 / EUR; dated T2S schedule for 2026-09-08 / EUR). No retrieval was `blocked`, `needs_context` or `needs_refresh`, and no GAP IDS were emitted. Two procedural points that still qualify the answer:

- The retriever's router notes record `currency=EUR` as an **assumed** context field on the partial-windows retrieval. The question itself names EUR, so the assumption matches the question; it is not an assumption I added.
- The knowledge base is `as_of` 2026-09-13 with review dates 2026-09-13 and 2026-09-14 available. The sections used here carry review date **14 September 2026**; the underlying UDFS source was reviewed 13 September 2026 and re-fetched hash-identical on 14 September 2026 [[t2s-schedule-r2]]. A review date is not a statement that nothing changed afterwards.

Platform release for every UDFS section in the bundle is **R2026.JUN**, which is the release the reviewed functional description belongs to. Nothing in this bundle speaks to any later release.

## 1. The five partial settlement windows (baseline)

**Documented requirement.** The real-time settlement (RTS) period contains "the real-time settlement with the five partial settlement windows to optimise maximum value and volumes of settlement transactions, which are unsettled because of lack of securities":

| # | Window (R2026.JUN baseline) |
|---|---|
| 1 | 08:00–08:30 |
| 2 | 10:00–10:15 |
| 3 | 12:00–12:15 |
| 4 | 14:00–14:15 |
| 5 | 30 minutes before the beginning of the DVP cut-off time, then between 15:30 and 16:05, or the closure of both DVP cut-offs, whichever comes first |

[[t2s-rts-phase]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.4.4, PDF 193–194; version R2026.JUN; reviewed 14 September 2026 (source reviewed 13 September 2026); body language English, no authoritative language stated and not independently established; source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS travelling with this row: the window times are the R2026.JUN **baseline**; some cut-offs are currency dependent; "a supplied business date requires a reviewed event overlay".

Two further baseline points from the same section: the RTS period starts after the end of night-time settlement (and, where NTS completes before 3.00 Monday to Friday or before 2.30 on Saturdays, before the maintenance window), and the RTS closure applies "different cut-offs and events for different Settlement Instructions, Settlement Restrictions and liquidity transfers categories", some of which "may be currency dependent" [[t2s-rts-phase]] (same locator and qualifications).

**Documented requirement — partial settlement outside the five windows.** Partial settlement is not confined to the RTS windows: the last night-time settlement cycle includes sequence X with "partial settlement on all unsettled Settlement Instructions, if eligible to partial settlement processing" [[t2s-schedule-r2]] T2S UDFS R2026.JUN, Table 37, PDF 160–163; reviewed 14 September 2026; CET is the source convention, no UTC conversion; nominal schedule is not guaranteed execution. And a Settlement Instruction on Party Hold that has been **partially released** can be attempted outside a running window for the *total* partially released quantity, and only inside a running window for *part* of it, until the relevant cut-off time, at which point the partial release is cancelled and the instruction returns to Party Hold for the full unsettled quantity [[t2s-partial-settlement]] T2S UDFS R2026.JUN, §1.6.1.9.3 with Table 68 and footnotes 224–229, PDF 343–345; reviewed 14 September 2026 (source reviewed 13 September 2026); T2S-native functional description, not a local participant interface specification.

## 2. Conditions and thresholds that gate partial settlement (EUR relevance)

**Documented requirement** [[t2s-partial-settlement]] (locator and qualifications as above):

1. A Settlement Instruction is partially settled only where there are insufficient **securities** (footnote 224: triggered by lack of securities, or lack of securities and cash, but **not** by lack of cash only), and three conditions hold together: the partial settlement window is currently running; the instructions are eligible to settle partially; the partial settlement threshold criteria are fulfilled.
2. Eligibility of a **matched pair**: the instructions are FOP, DVP or DWP; the partial settlement indicator is not set to "No" in either instruction; and they are not linked to another instruction or restriction by link type "Before", "After", "With" or by a pool reference.
3. Procedure: a full settlement attempt comes first; on failure the instruction goes to the Optimising application process; only if optimisation cannot find a full-settlement solution does T2S attempt partial settlement, provided the conditions above are met (footnote 229: partially released instructions are submitted to partial settlement attempts only for the released quantity).
4. Threshold type is determined from instruction type (FOP / DVP / DWP), instruction threshold type, the underlying ISIN and **the currency of the cash amount** (Table 68). For DVP/DWP not set to "Quantity" for both matched instructions, a **cash value** threshold applies, being an "amount configured in the currency specified", separately for unit-quoted and nominal-quoted ISINs; that parameter is set by the **T2S Operator** in Static Data, is common to all T2S Parties and is set per T2S settlement currency. Quantity thresholds are set by the T2S Actor administering the ISIN. Footnote 228: cash-value thresholds are not considered for FOP regardless of the partial settlement indicator (PARC, PART), including FOP instructions related to a foreign-currency transaction.

**Unresolved requirement.** The actual EUR cash-value partial settlement threshold is **not in reviewed evidence** — the section carries the explicit LIMITATION that "cash-value thresholds are configured per currency by the T2S Operator; actual values are not in this excerpt". Any EUR minimum partial amount must come from T2S Operator static-data publication, not from this bundle.

## 3. What was published for business date 8 September 2026

**Documented requirement (as a description of published status entries, not as a record of execution).** The reviewed derivative of the ECB T2S status history attributes five entries to business date 2026-09-08 (a weekday); the day is classified "stated: schedule changed or delayed". Cited as [[t2s-events-2026-09-08]] ECB T2S status history 2026, entries listed in the derivative for 2026-09-08, capture of 14 September 2026; no document version; reviewed 14 September 2026; body language English, no authoritative language stated and not independently established; applicability basis "reference description"; source identity checked, no independent whole-edition supervisory approval certification; captured file hash recorded in the excerpt.

| Entry (time as displayed) | Published content, in substance |
|---|---|
| 05:00 | "T2S is operating normally." |
| 15:30 (names EUR) | No incident; the operating day schedule "has been changed, due to a request by a Central Securities Depository". The **start of the EUR delivery versus payment cut-off (event IDVP) postponed by 60 minutes (from 16:00 to 17:00)**. Consequently the Reimbursement of Auto-collateralisation instructions (RMIC) and the Optional Cash Sweep (OCSW) are also delayed and "will take place 15 minutes after closure of the delivery-versus-payment cut-off". The second optional cash sweep to CLM (OCS2) **remains at 17:45**; the free-of-payment cut-off (IFOP) **remains at 18:00**. |
| 18:10 | Incident impacting the ICBO event (Intraday CBO cut-off); the operating day is blocked and IFOP did not start; stated as having no impact on other T2S functionality. |
| 18:55 | Incident resolved; "The IFOP event (Intraday FoP cut-off) closed at 18:39." |
| 20:00 | "T2S is operating normally." |

LIMITATIONS travelling with every row: entries are not currency-specific unless the text names a currency (only the 15:30 entry names EUR; the others have scope ALL and concern the operating day as a whole); business-date attribution of evening entries is a labelled inference from the UDFS schedule, with the displayed calendar date and time preserved (these five entries are attributed on the calendar-date basis); and **an announced change is not proof of an individual transaction's execution time**. The capture also records that the displayed ECB timestamps carry no stated time zone on the page and that UTC conversion was not verified — so the "16:00", "17:00", "17:45", "18:00" and "18:39" values in this row set are as displayed, not asserted CET.

**Documented requirement — the mechanism that makes such a change lawful within T2S.** The T2S schedule is under the control of the T2S Operator, which maintains for each event a **planned time** (default standard schedule), a **revised time** (the foreseen time for the current settlement day, updated in contingency situations while the planned time is unchanged) and an **effective time** (the actual occurrence of the event). The Operator "is entitled to change some cut-offs and events ... independently for a T2S settlement currency, in exceptional circumstances or contingency situations, based on a request from the relevant T2S dependent external system (eg. RTGS, CSD platform, CMS)". The DVP cut-off (IDVP / EDVP) is listed among the currency-dependent cut-offs and events, described as remaining harmonised for all currencies at 16h00, alongside cash Settlement Restriction cut-off, settlement restrictions release, reimbursement of intraday credit, BATM cut-off, CBO cut-off, optional cash sweep, inbound liquidity transfer cut-off and automated cash sweep. Such a change is valid only for the current T2S settlement day; when a currency-dependent cut-off is extended for a currency, the start of its dependent processes (for example the cash sweep) is automatically extended for the same currency; and the sequence and order of events must remain unchanged, with no additions, removals, re-ordering or changed dependencies. There is "no schedule of a settlement day defined per currency in T2S, but distinct individual cut-offs and events per currency are defined", within "the boundaries of the real-time settlement closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET with FOP cut-off)". Where T2S has a general issue across all currencies, the Operator may need to extend the EOD cut-off while ensuring the sequence of the **currency-independent** cut-offs (securities Settlement Restriction cut-off and FOP cut-off) is not changed. [[t2s-schedule-r2]] T2S UDFS R2026.JUN, §1.4.2 and exception conditions, PDF 156–158; reviewed 14 September 2026; same pages as the 13 September section, source bytes re-fetched hash-identical on 14 September 2026; CET is the source convention, no UTC conversion; nominal schedule is not guaranteed execution or a local participant cut-off.

**Reasoned inference.** The 8 September entry fits that documented mechanism precisely: a CSD request, a currency-named cut-off (EUR IDVP), a same-day change, dependent events (RMIC, OCSW) carried along, and the currency-independent FOP cut-off left in place at 18:00. Derived from the §1.4.2 change conditions read against the 15:30 status entry; the ECB text does not itself cite §1.4.2.

## 4. So what applied to the DvP cut-off and the windows on 8 September 2026?

**Documented requirement.** For EUR on that business date, the *revised* start time of the DVP cut-off event IDVP was 17:00 instead of the planned 16:00, a 60-minute postponement requested by a CSD [[t2s-events-2026-09-08]] (locator and qualifications as in section 3).

**Unresolved requirement.** The *effective* time of the EUR DVP cut-off — the actual occurrence, in the UDFS planned/revised/effective triad [[t2s-schedule-r2]] §1.4.2, PDF 156–158 — is **not in reviewed evidence** for 8 September 2026. The reviewed entries state an effective time only for IFOP ("closed at 18:39"). Likewise, nothing in the reviewed entries states a revised or effective time for the *closure* of the DVP cut-off, or for EDVP as distinct from IDVP, and the announced "15 minutes after closure of the delivery-versus-payment cut-off" timing for RMIC and OCSW is expressed relative to a closure time that the evidence does not give; I therefore do not compute a clock value for those events.

**Reasoned inference — direction only, on the fifth window.** The fifth window is defined by two limbs in the same sentence: a relational limb ("30 minutes before the beginning of the DVP cut-off time") and a clock limb ("then between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first)") [[t2s-rts-phase]] §1.4.4.4, PDF 193–194. On the baseline the two limbs coincide, because the planned DVP cut-off start is 16:00. Once the EUR IDVP start was revised for that day, the two limbs no longer point to the same times. Derived from that sentence read against the 15:30 status entry, the relational limb implies the fifth window would track the later DVP cut-off start, while the clock limb and the end condition "closure of both DVP cut-offs" are not restated for a revised day.

**Unresolved requirement.** The reviewed evidence does not resolve that tension, and I do not state revised fifth-window times. Specifically not in reviewed evidence: (a) which limb of §1.4.4.4 governs when the T2S Operator revises the DVP cut-off for a single currency; (b) whether a EUR-only cut-off change moves the partial settlement window at all, given §1.4.2's statement that there is no per-currency settlement-day schedule in T2S, only distinct per-currency cut-offs and events [[t2s-schedule-r2]] §1.4.2, PDF 156–158; and (c) any revised or effective window times for 8 September 2026.

**Documented requirement, negatively stated — windows 1 to 4.** The reviewed 8 September entries do not name any partial settlement window. The 15:30 entry enumerates both the events it delayed (RMIC, OCSW) and the events that were unchanged (OCS2 at 17:45, IFOP at 18:00), and no partial settlement window appears in either list [[t2s-events-2026-09-08]]. The correct statement is therefore that **no deviation to the first four windows was published** for that date. That is not a statement that they ran at their baseline times: the section's own LIMITATION is that an announced change is not proof of an individual transaction's execution time, and the day additionally carried a later incident that blocked the operating day at the ICBO event.

**Reasoned inference.** The 18:10 and 18:55 entries concern ICBO and IFOP, both after the revised DVP cut-off start, and neither names a currency (scope ALL). Derived from the entry texts and the section's currency-scope LIMITATION: the blocking incident is not evidence about EUR DVP settlement or about the five partial settlement windows, and it is not evidence that DVP settlement before 17:00 was affected either way.

**Proposed design choice (for a reader building on this).** If an implementation or an operational procedure needs a deterministic fifth-window time for a day on which a currency-dependent DVP cut-off is revised, that rule is an implementation decision the reader must take and document, not an infrastructure rule that this bundle supplies; it should be confirmed against the T2S Manual of Operational Procedure (T2S MOP), which §1.4.2 names as the place where the exceptional procedure "is to be defined" [[t2s-schedule-r2]] §1.4.2, PDF 156–158.

## 5. Terms used above

Explanation, not documented requirement, except where the UDFS wording is quoted: *partial settlement* — settling only a fraction of the original quantity or amount when full settlement is not possible for lack of securities or cash, as §1.6.1.9.3 puts it [[t2s-partial-settlement]]. *IDVP / EDVP* — the event identifiers the reviewed sources use for the intraday and end DVP cut-offs; *IFOP* — the intraday free-of-payment cut-off; *ICBO* — the intraday central bank operation cut-off; *RMIC* — reimbursement of auto-collateralisation instructions; *OCSW / OCS2* — the first and second optional cash sweeps, OCS2 being towards CLM. These expansions are those printed in the reviewed entries and section text; no further meaning is asserted. *Party Hold* — a hold placed by the instructing party, which §1.6.1.9.3 treats as compatible with partial settlement only through partial release, as described above.

## Open items

1. **Effective time of the EUR DVP cut-off (IDVP, and EDVP) on 8 September 2026.** Not in reviewed evidence; the bundle names no gap id. Official route: the ECB T2S operational information on the public T2S pages of the ECB website and the T2S Manual of Operational Procedure (T2S MOP), which §1.4.2 identifies as defining the exceptional procedure; for participant-level confirmation, the CSD's own client notice service.
2. **Revised partial settlement window times for a day with a currency-dependent DVP cut-off change.** Not in reviewed evidence. Route: the T2S MOP and the T2S Operator's schedule publication for the affected settlement day; a reviewed event overlay for the same review date would be required before any dated window time is stated.
3. **Closure time of the DVP cut-off on 8 September 2026**, needed before the announced "15 minutes after closure" timing of RMIC and OCSW can be expressed as clock times. Not in reviewed evidence; same route as item 1.
4. **EUR partial settlement cash-value thresholds** (unit-quoted and nominal-quoted), set by the T2S Operator in Static Data per settlement currency. Explicitly excluded by the LIMITATION on [[t2s-partial-settlement]]. Route: T2S Operator static-data publication; quantity thresholds instead sit with the T2S Actor administering the relevant ISIN.
5. **Time zone of the ECB status-history timestamps.** The capture records that no time zone is stated on the page and that UTC conversion was not verified, while CET is the UDFS convention. Route: ECB clarification of the status page convention; until then the dated times are "as displayed".
6. **Local participant deadlines.** The UDFS material is a T2S-native functional description for R2026.JUN and not a local participant interface specification; any Euronext Securities CSD's own client cut-off for that day is outside this bundle. Route: the relevant CSD's client documentation platform and dated client notices.
7. **Instruction-level outcome.** No reviewed evidence in this bundle establishes what any individual instruction did on 8 September 2026; the status history describes the operating day, not executions.

No instruction-like content was found in the retrieved excerpts.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:13.178690+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-partial-settlement]] — Partial settlement conditions, thresholds and procedure (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Cash-value thresholds are configured per currency by the T2S Operator; actual values are not in this excerpt.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345):
1.6.1.9.3 Partial Settlement

 2   Concept

 3   T2S provides partial settlement process, i.e. settles only a fraction of the original quantity or amount when
 4     full settlement is not possible due to lack of securities or cash, in order to increase the volume and value of
 5    settlement.

 6   Overview

 7     Partial settlement applies under conditions and procedures that differ whether they apply to:

 8         l  Settlement Instructions;

 9         l  Settlement Restrictions;

10         l  Liquidity transfers.

11    Partialsettlementprocess

12     Partial settlement process for Settlement Instructions

13   A Settlement Instruction is partially settled 224, in case there are insufficient securities to settle the full quan-
14     tity and provided the following conditions are met:

15         l  The partial settlement window is currently running; 225

16         l  The Settlement Instructions are eligible to settle partially;

17         l  The partial settlement threshold criteria are fulfilled.

18    Partial settlement window

19     Partial settlement is active in T2S within the dedicated partial settlement windows 226.

20    Partial settlement eligibility

21   The settlement eligibility depends notably on conditions set by the T2S parties on their matched Settlement
22    Instructions.

23   A matched pair of Settlement Instructions is eligible to partial settlement, when these Settlement Instruc-
24    tions are entered by the T2S parties with the following characteristics:

25         l  They are related to Free Of Payment or to Delivery Versus Payment or Delivery With Payment; 227

26         l  The partial settlement indicator is not set to "No" in any of the Settlement Instructions;

27         l  They are not linked to any other Settlement Instruction or Settlement Restriction by the T2S parties by a
28         link type “Before”, “After” “With” or by a pool reference.

     _________________________


        224    Partial settlement is triggered only in case of lack of securities (i.e. lack of securities only or lack of securities and cash) but not in case of lack of
               cash only.

        225    Partially released Settlement Instructions can be submitted for settlement attempts for the total partially released quantity also when the partial
                settlement window is not running. Partially released Settlement Instructions can be submitted for settlement attempts for a part of the partially
                released quantity only when the partial settlement window is running.

        226   For details about the schedule of partial settlement window, see section Settlement Day [ 155]

        227    Including such Settlement Instructions which are on Party Hold and have been partially released.


                                                                                            Page 343 of 2017



[PDF page 344]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1     Partial settlement of Partially Released Settlement Instructions

 2   A Settlement Instruction on Party Hold may be partially released to allow the partial settlement of a specified
 3    quantity. This Partially Released Settlement Instruction must conform to all the conditions of partial settle-
 4   ment as for any other Settlement Instruction. During the real-time period the partial settlement of Partially
 5    Released Settlement Instructions can occur outside a partial settlement window for the total partially re-
 6    leased quantity, as well as during a partial settlement window for the total or part of the partially released
 7    quantity and until the relevant cut-off time (partial release is only valid for the current business day) at
 8    which point the partial release will be cancelled and the underlying Settlement Instruction set back on Party
 9    Hold for the full unsettled quantity. For partial release to be considered during sequence C2SX of the night
10    time settlement the partial release must occur as of the start of day.

11    Partial settlement threshold

12     Partial settlement is conditioned by thresholds, below which it cannot apply, and that are determined in T2S
13   when the settlement occurs, on the basis of the following content of the Settlement Instructions:

14         l  The instruction type (FOP or DVP or DWP);

15         l  The instruction threshold type (see table below);

16         l  The underlying ISIN;

17         l  The currency of the cash amount of the Settlement Instruction.

18   These contents of the Settlement Instructions allow T2S to determine the type of partial settlement thresh-
19    old applicable on the Settlement Instructions being processed. The following types of partial settlement
20    thresholds are possible:

21         l A threshold in “quantity”: meaning the partial settlement cannot take place for a quantity lower than an
22        applicable value;

23         l A threshold in “cash value”: meaning the partial settlement cannot take place for an amount lower than
24      an applicable value.25





                                                                                            Page 344 of 2017



[PDF page 345]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                            TABLE 68 - APPLICABLE THRESHOLD TYPES FOR PARTIAL SETTLEMENT
 2

               CONTENT OF SETTLEMENT INSTRUCTION            RESULTING     RESULTING APPLICABLE
                                                                 APPLICABLE      THRESHOLD VALUE
       INSTRUCTION     INSTRUCTION         ISIN     CURRENCY
                                                         THRESHOLD
           TYPE       THRESHOLD TYPE
                                                                 TYPE

      FOP 228          n/a                     applicable    n/a          Quantity    Minimum settlement unit (only for
                                                                                                                         first partial settlement) and set-
     DVP/DWP        Set to “Quantity” for
                                                                                      tlement unit multiple are used.
                       both matched Settle-
                     ment Instructions

     DVP/DWP        Not set to “Quantity”   Unit-quoted  applicable    Cash value   Amount configured in the currency
                             for both matched Set-                                              specified (for quantity, minimum
                        tlement Instructions                                            settlement unit and settlement
                                                                                                  unit multiple are used).

                                             Nominal-                          Amount configured in the currency
                                            quoted                                     specified (for quantity, minimum
                                                                                        settlement unit and settlement
                                                                                                  unit multiple are used).

 3   The parameters determining the threshold applicable above are set:

 4         l  By T2S Actors from the content of their Settlement Instructions for the instruction type and instruction
 5        threshold type mentioned in the table above;

 6         l  By the T2S Operator inside the Static Data for the applicable threshold in cash value. This parameter is
 7      common to all T2S Parties, and set per T2S settlement currency, and separate for unit-quoted or nomi-
 8        nal quoted ISIN;

 9         l  By the T2S Actors in charge of the administration of the relevant ISIN in the Static Data for the applica-
10        ble threshold in quantity (See section Concept of securities in T2S [ 71]).

11    Partial settlement procedure

12    Settlement Instructions are submitted to a full settlement attempt before being submitted to a partial set-
13    tlement attempt. 229

14    In case the Settlement Instruction does not settle, the Settlement Instruction is submitted to Optimising
15    application process. The Optimising application process tries to settle the failed Settlement Instruction with
16    other Settlement Instructions in T2S based on different technical optimisations. In case the Optimising appli-
17    cation process is not able to find a solution for a full settlement, T2S tries to submit the Settlement Instruc-
18    tion for partial settlement provided the above conditions are met.

     _________________________


        228   Cash value thresholds are not considered for FOP regardless of the partial settlement threshold type (partial settlement indicator PARC, PART)
                defined within the settlement instruction. This also applies for FOP instructions related to a foreign currency transaction (non-EUR amount).

        229    Partially Released Settlement Instructions are only submitted to partial settlement attempts for the released quantity.


                                                                                            Page 345 of 2017

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_windows_and_cutoffs", "business_date": "2026-09-08", "currency": "EUR"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: actual
ROUTER NOTES: {"_assumed": ["currency=EUR"]}

--- SECTION [[t2s-events-2026-09-08]] — ECB status entries attributed to 2026-09-08 (stated: schedule changed or delayed) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reference_description)
CITATION: ECB T2S status history 2026 (capture of 14 September 2026) | ECB T2S status history, entries listed in the derivative for 2026-09-08; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html
LIMITATION: Entries are not currency-specific unless the text names a currency (recorded per entry); scope ALL applies to the operating day as a whole.
LIMITATION: Business-date attribution of evening entries follows a labelled inference from the UDFS schedule; the displayed calendar date and time are preserved.
LIMITATION: An announced change is not proof of an individual transaction's execution time.
EXCERPT (ECB T2S status history, entries listed in the derivative for 2026-09-08; capture of 14 September 2026):
{
  "source_id": "ecb-status-2026-20260914",
  "source_url": "https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html",
  "captured_on": "2026-09-14",
  "captured_file": "implementation/2026-09-14-settlement-agent/hubs/ecb-t2s-status-2026.html",
  "captured_sha256": "3377fac2c74fa893d9c8ebac5233cedd29ad73ab94fe911caa299c3ed7a24ec8",
  "timezone_note": "Displayed ECB timestamps preserved; time zone not stated on the page; UTC conversion not verified.",
  "attribution_note": "t2s_business_date follows the rule in attribution_basis. Evening entries about night processes are attributed to the next T2S settlement day; this is a labelled inference from the UDFS schedule, not source text. Weekend calendar dates carry closure/maintenance statements and are not T2S business days.",
  "business_date": "2026-09-08",
  "is_weekday": true,
  "currency_scope": "ALL",
  "currency_note": "ECB entries are not currency-specific unless the text names a currency (see currency_mentioned per entry); scope ALL means the statement concerns the operating day as a whole.",
  "schedule_impact": "stated: schedule changed or delayed",
  "entries": [
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "05:00:00",
      "original_text": "T2S is operating normally.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "15:30:00",
      "original_text": "There is currently no incident in T2S. However, the operating day schedule has been changed, due to a request by a Central Securities Depository. The start of the EUR delivery versus payment cut-off (event IDVP) has been postponed by 60 minutes (from 16:00 to 17:00). Consequently, the Reimbursement of Auto-collateralisation instructions (event RMIC) and the Optional Cash Sweep (event OCSW) have also been delayed and will take place 15 minutes after closure of the delivery-versus-payment cut-off. The second optional cash sweep (event OCS2) to CLM remains at 17:45 and the; free of payment cut-off (event IFOP) remains at 18:00.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": "EUR"
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "18:10:00",
      "original_text": "T2S is currently facing an incident impacting the ICBO event (Intraday CBO cut-off). As a result of the incident, the operating day is blocked and the IFOP event (Intraday FoP cut-off) did not start. The incident does not have any impact on any other T2S functionality. The Eurosystem is taking all measures necessary to resolve the incident as soon as possible. Updated information will be provided at the latest by 19:00.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "18:55:00",
      "original_text": "T2S is operating normally. The previous incident impacting the ICBO event (Intraday CBO cut-off) has been resolved. The IFOP event (Intraday FoP cut-off) closed at 18:39.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "20:00:00",
      "original_text": "T2S is operating normally.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    }
  ]
}

--- SECTION [[t2s-rts-phase]] — Real-time settlement period: five partial settlement windows and cut-off structure (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.4; PDF 193–194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Window times are the R2026.JUN baseline (08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, 15:30 to 16:05 or DVP cut-off closure); some cut-offs are currency dependent.
LIMITATION: A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly.
EXCERPT (§1.4.4.4; PDF 193–194):
1.4.4.4 Real-time settlement (RTS)

 4    This section presents the real-time settlement processes in the T2S settlement day. The real-time settlement
 5    period starts after the end of the night-time settlement and is followed by the end of day period.

 6    In case the NTS completes before 3.00 from Mondays to Fridays and before 2.30 on Saturdays, real-time
 7    settlement period begins before the start of the maintenance window.

 8   The real-time settlement period includes:

 9         l  The real-time settlement preparation;

10         l  The real-time settlement with the five partial settlement windows to optimise maximum value and vol-
11      umes of settlement transactions, which are unsettled because of lack of securities:

12      – The first partial settlement window between 08:00 and 08:30;

13      – The second partial settlement window between 10:00 and 10:15;

14      – The third partial settlement window between 12:00 and 12:15;

15      – The fourth partial settlement window between 14:00 and 14:15;

16      – The fifth partial settlement window is 30 minutes before the beginning of the DVP cut-off time, then
17         between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first).

18   The previously unsettled Settlement Instructions and Settlement Restrictions from night-time settlement are
19    attempted for settlement in the real-time settlement period with the arrival of new resources (securities for
20    delivery, securities in positions earmarked available for collateral, cash). 143 Additionally T2S performs a set-
21    tlement attempt for any new intraday Settlement Instructions, Settlement Restrictions and liquidity transfers
22    validated and accepted during real-time settlement period;

23         l  The real-time settlement closure with different cut-offs and events for different Settlement Instructions,
24       Settlement Restrictions and liquidity transfers categories.


     _________________________


        143   During the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been at-
               tempted for settlement. This serialization process will concern all transactions with age >= 3 selected by the Regular Recycling process following a
                   credit in securities or cash or an increase in CMB headroom or limit, guaranteeing that an older transaction will be attempted before a younger one
                with the same priority. The transactions selected by one given recycling process will be segregated into eight groups, depending on their priority
              and age:

               Group 1         Group 2         Group 3         Group 4         Group 5         Group 6         Group 7         Group 8
                    Priority 1           Priority 1           Priority 2           Priority 2           Priority 3           Priority 3           Priority 4           Priority 4
              Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3
               Should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to
                the regular recycling process.


                                                                                            Page 193 of 2017



[PDF page 194]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l Some of these cut-offs and events may be currency dependent.

 2    For the ease of presentation, the real-time settlement period is shown in two parts:

 3         l  The real-time settlement;

 4         l  The real-time settlement closure.

 5   The real-time settlement period also includes processes specific to the penalty mechanism. These are com-
 6    prised of the processing of information received within T2S including securities subject to penalties infor-
 7    mation, penalty modification requests and daily and historic prices for penalties. This information is subse-
 8    quently used for penalty calculations and reporting.


 9

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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule", "currency": "EUR", "business_date": "2026-09-08"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: actual

--- SECTION [[t2s-events-2026-09-08]] — ECB status entries attributed to 2026-09-08 (stated: schedule changed or delayed) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reference_description)
CITATION: ECB T2S status history 2026 (capture of 14 September 2026) | ECB T2S status history, entries listed in the derivative for 2026-09-08; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html
LIMITATION: Entries are not currency-specific unless the text names a currency (recorded per entry); scope ALL applies to the operating day as a whole.
LIMITATION: Business-date attribution of evening entries follows a labelled inference from the UDFS schedule; the displayed calendar date and time are preserved.
LIMITATION: An announced change is not proof of an individual transaction's execution time.
EXCERPT (ECB T2S status history, entries listed in the derivative for 2026-09-08; capture of 14 September 2026):
{
  "source_id": "ecb-status-2026-20260914",
  "source_url": "https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html",
  "captured_on": "2026-09-14",
  "captured_file": "implementation/2026-09-14-settlement-agent/hubs/ecb-t2s-status-2026.html",
  "captured_sha256": "3377fac2c74fa893d9c8ebac5233cedd29ad73ab94fe911caa299c3ed7a24ec8",
  "timezone_note": "Displayed ECB timestamps preserved; time zone not stated on the page; UTC conversion not verified.",
  "attribution_note": "t2s_business_date follows the rule in attribution_basis. Evening entries about night processes are attributed to the next T2S settlement day; this is a labelled inference from the UDFS schedule, not source text. Weekend calendar dates carry closure/maintenance statements and are not T2S business days.",
  "business_date": "2026-09-08",
  "is_weekday": true,
  "currency_scope": "ALL",
  "currency_note": "ECB entries are not currency-specific unless the text names a currency (see currency_mentioned per entry); scope ALL means the statement concerns the operating day as a whole.",
  "schedule_impact": "stated: schedule changed or delayed",
  "entries": [
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "05:00:00",
      "original_text": "T2S is operating normally.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "15:30:00",
      "original_text": "There is currently no incident in T2S. However, the operating day schedule has been changed, due to a request by a Central Securities Depository. The start of the EUR delivery versus payment cut-off (event IDVP) has been postponed by 60 minutes (from 16:00 to 17:00). Consequently, the Reimbursement of Auto-collateralisation instructions (event RMIC) and the Optional Cash Sweep (event OCSW) have also been delayed and will take place 15 minutes after closure of the delivery-versus-payment cut-off. The second optional cash sweep (event OCS2) to CLM remains at 17:45 and the; free of payment cut-off (event IFOP) remains at 18:00.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": "EUR"
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "18:10:00",
      "original_text": "T2S is currently facing an incident impacting the ICBO event (Intraday CBO cut-off). As a result of the incident, the operating day is blocked and the IFOP event (Intraday FoP cut-off) did not start. The incident does not have any impact on any other T2S functionality. The Eurosystem is taking all measures necessary to resolve the incident as soon as possible. Updated information will be provided at the latest by 19:00.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "18:55:00",
      "original_text": "T2S is operating normally. The previous incident impacting the ICBO event (Intraday CBO cut-off) has been resolved. The IFOP event (Intraday FoP cut-off) closed at 18:39.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-09-08",
      "published_time_as_displayed": "20:00:00",
      "original_text": "T2S is operating normally.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    }
  ]
}

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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
