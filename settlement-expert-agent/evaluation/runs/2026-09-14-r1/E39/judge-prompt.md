You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Milan's Settlement Service Instructions say night-time settlement starts at 19:30 but T2S says 20:00. Which applies to Monte Titoli participants today?

# Case category: conflicting-evidence (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "The 19:30/two-window passage is quarantined (conflict with deployed R2026.JUN: 20:00, five windows); T2S baseline 20:00 is the platform value; Milan's Regulations defer functioning to the T2S URD and hours to notices; participant-specific notice not located (G01).",
  "Do not choose 19:30; do not claim 20:00 is a Milan participant deadline either."
]
Fail conditions (must NOT appear):
[
  "Present 19:30 as current.",
  "Hide the conflict."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked', 'evidence_only']

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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:02:36.358797+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_nts_processing"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-nts-processing]] — Night-time settlement processing: cycles, sequences and reporting (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.2 NTS processing and reporting; PDF 167–169 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Cycle durations are volume dependent; the 22:20/00:00 targets are objectives, not commitments.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.4.4.2 NTS processing and reporting; PDF 167–169):
1.4.4.2 Night-time settlement (NTS)

2    This section presents the night-time settlement processes in the T2S settlement day.

3    For the ease of presentation, the night-time settlement period is shown in two parts of batch settlement,
4   each one referring to a settlement cycle.

5   The NTS period starts after the successful completion of the SOD period and is followed by the maintenance
6   window and the real-time settlement period.




                                                                                          Page 167 of 2017



[PDF page 168]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1    In the exceptional cases that T2S experience the late arrival of late peak volume transactions on Friday
 2    evening that are not available for settlement at the regular NTS, the peak volume transactions should be
 3    sent after the NTS. In that case, short NTS cycles are triggered by the T2S Operator during the injection of
 4    the late peak volume transactions put under Intraday Restriction. At the end of the injection, the T2S Opera-
 5    tor triggers an Additional NTS cycle. The exact procedure with the timing to apply in case of such an event
 6    are defined in the T2S MOP.

 7    Note: The exact timing needed to perform the sequences and the time available for the sequence reporting
 8     will be defined at a later stage, but the dependencies defined are ensured.

 9  NTSProcessing

10    During the night-time settlement period, T2S processes the Settlement Instructions, Settlement Restrictions
11   and liquidity transfers in sequences within two settlement cycles. T2S submits Settlement Instructions, Set-
12    tlement Restrictions and liquidity transfers for settlement according to an automatic pre-defined order, called
13    “sequence”.

14   A settlement cycle may consist of more than one sequence (for settlement of different types of Settlement
15    Instructions, Settlement Restrictions and liquidity transfers).

16    In each NTS sequence, T2S:

17         l  Processes those new Settlement Instructions, Settlement Restrictions and liquidity transfers received be-
18        fore the start of the sequence which are eligible for settlement at this sequence (and for the first Se-
19       quence all the ones received in T2S before 20:00 even though the cycle starts after 20:00);

20         l  Includes pending Settlement Instructions not settled during previous sequences.

21     If a Settlement Instruction/Settlement Restriction selected for a sequence is linked “with” or “after” a Set-
22    tlement Instruction/Settlement Restriction which does not correspond to the sequence criteria, these Settle-
23   ment Instruction(s)/Settlement Restriction(s) are excluded from this sequence.

24   T2S validates and accepts the static data maintenance instructions and maintenance instructions during the
25    night-time settlement period on a continuous basis. However, T2S processes these updates only during the
26    processing periods between the different sequences. T2S sends the information on the status of the static
27    data maintenance instructions and maintenance instructions to T2S Actors immediately after end of their
28    processing (i.e. acceptance/execution).

29    For all static data updates, i.e. immediate updates and updates with future date, T2S also performs a revali-
30    dation of all Settlement Instructions and Settlement Restrictions to ensure that they are valid for the consid-
31    ered static data update. Maintenance instructions (i.e. Amendment Instructions, Cancellation Instructions,
32    Hold/Release/Partial Release Instructions) are only revalidated at the SOD revalidation process. In case the
33    underlying Settlement Instruction or Settlement Restriction to be maintained is cancelled due to their revali-
34    dation, the maintenance instruction is denied when trying to be executed but not cancelled.

35     Similarly, T2S processes any instruction query received and validated during a settlement cycle run with a
36    query response back to the relevant T2S Actor.

37  NTSReporting





                                                                                            Page 168 of 2017



[PDF page 169]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1    At the end of each night-time sequence, T2S generates full or delta reports as per the report configuration
 2    setup of the relevant T2S Actors.

 3   T2S sends also to the T2S Actors messages such as settlement status advices, settlement confirmation,
 4    posting notification, etc that were queued due to an execution of a settlement sequence.

 5   The duration of the night-time settlement cycles are dependent on settlement volumes. The target objective
 6    for the first and last night-time cycles should finish by 22:20 and 00:00 respectively, as long as volumes do
 7    not exceed standard peak volumes.


 8

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_instruction_processing_rules"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_participant_cutoff"}
STATUS: blocked — Applicable Milan timetable notice chain remains unresolved.
GAP IDS: ['G01']

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
