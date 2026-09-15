You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
how many working days before t2s auto-cancels an unmatched instruction? and a matched but unsettled one?

# Case category: paraphrase (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "20 working days for unmatched (from ISD or last status change), 60 for matched/settlement restrictions; external-CSD exception; footnotes give current values."
]
Fail conditions (must NOT appear):
[
  "Other numbers.",
  "Present as calendar days."
]
Expected sections (if any): ['t2s-recycling']
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
# T2S recycling periods before automatic cancellation

## Direct answer

**Documented requirement.** Two different periods, both configured by the T2S Operator:

| Pending instruction | Recycling period | Counted from |
|---|---|---|
| **Unmatched** Settlement Instruction | **20 working days** (the current value stated in footnote 199) | the **later** of the Intended Settlement Date and the date of the **last status change** of the instruction; any status value change restarts the count |
| **Matched but unsettled** Settlement Instruction (and Settlement Restrictions) | **60 working days** (the current value stated in footnote 200) | recycled "until its settlement or cancellation occurs"; the end-of-day calculation below uses the same D1 rule |

Both are described in the UDFS as "a period of working days **configured by the T2S Operator**", with 20 and 60 given as the *current* values in footnotes — they are a parameter, not a constant of the system. There is also an external-CSD exception under which an instruction is **never** automatically cancelled.

Source for the whole table: [[t2s-recycling]] T2S User Detailed Functional Specifications R2026.JUN, §1.6.1.7 with footnotes 199–200, PDF 296–299; version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026; English body text, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS carried with the claim: this is a **T2S-native functional description for R2026.JUN — not a local participant interface specification, production XSD or message usage guideline**; and the **external-CSD exception is stated but individual configurations are not certified**.

## Retrieval statuses (disclosure)

Three retrievals, all **evidence_only**: `t2s_recycling_periods` (as of 14 September 2026), `t2s_cancellation_process` (as of 14 September 2026) and `matching_concept` (as of 13 September 2026). No blocked, needs_context or needs_refresh status arose. Review dates are 14 September 2026 for the recycling and cancellation sections and 13 September 2026 for the matching and posting sections; all four describe platform release R2026.JUN.

## The supporting detail

**Documented requirement — what a recycling period is.** At each end of a Settlement Day, T2S recycles pending instructions for "a period of time known as recycling period, which is defined as the number of **working days** a pending instruction can remain in T2S, before being cancelled by the system". Recycling triggers the revalidation process at Start of Day, and the Instruction Recycling process manages the automatic cancellation of all pending instructions that have exceeded their recycling period — [[t2s-recycling]] §1.6.1.7.1–1.6.1.7.2, PDF 296; reviewed 14 September 2026.

**Documented requirement — the unmatched clock can be reset.** Unmatched Settlement Instructions are recycled starting from the Intended Settlement Date or the date of the last status change, whichever is later, and "**any status value change** is considered for restarting the count of the number of days for the recycling period"; the UDFS gives a change of Party Hold status from "Yes" to "No" as an example of a status change — [[t2s-recycling]] §1.6.1.7.3, PDF 297; reviewed 14 September 2026. Operationally this is the trap in "how many days do I have": touching an unmatched instruction can restart its 20-working-day window.

**Documented requirement — a third, separate period.** Unmatched **Cancellation Instructions** that need to be matched in T2S are recycled for a period of working days configured by the T2S Operator, starting from their reception in T2S until matching occurs — [[t2s-recycling]] §1.6.1.7.3, PDF 297; reviewed 14 September 2026. **Unresolved requirement:** the reviewed excerpt gives **no numeric value** for this third period (footnotes 199 and 200 cover unmatched settlement instructions and matched instructions only) — the number is **not in reviewed evidence**.

**Documented requirement — how the cut is computed.** At the End of Day process T2S cancels all instructions that have reached their recycling period. The period "is considered as reached when: The difference between 'D1' (latest date between the ISD and the business day of the last status change of the instruction) and 'D2' (current business date) equals the number of business days defined for the applicable recycling period." Once reached, T2S stops recycling and cancels automatically; "nevertheless, until the EoD the instruction is still processed as normal throughout the whole business day" — [[t2s-recycling]] §1.6.1.7.3, PDF 299; reviewed 14 September 2026. So an instruction on its final day can still settle normally that day.

**Documented requirement — you are told only at the end.** T2S does **not** send a daily message about the result of the recycling process; only when an instruction exceeds its recycling period does T2S cancel it and send a message with the corresponding reason code(s); interested parties may also be informed according to their message subscription preferences — [[t2s-recycling]] §1.6.1.7.3, PDF 299; reviewed 14 September 2026. **Unresolved requirement:** the reason codes themselves are **not in reviewed evidence** and must not be guessed.

**Documented requirement — the exception where nothing is cancelled.** In an external-CSD scenario, instructions meeting **all** of the following remain pending and are recycled for an **indefinite** period until one of the conditions ceases to hold or a T2S Actor cancels them: (i) any of the relevant CSDs is external to T2S; (ii) the external CSD is the issuer of the security; and (iii) the external CSD is configured as **not compliant** with the T2S automatic cancellation of instructions — [[t2s-recycling]] §1.6.1.7.3, PDF 298; reviewed 14 September 2026. LIMITATION carried: the exception is stated, but **individual CSD configurations are not certified** in reviewed evidence, so whether a specific external CSD is flagged non-compliant cannot be answered from this bundle.

**Documented requirement — automatic cancellation is not only about recycling.** T2S automatically cancels pending instructions when they exceed their recycling period, and also: when the realignment chain cannot be built; when instructions do not pass the revalidation process (triggered at Start of Day and by a reference-data change affecting the instruction); and, where Start-of-Day revalidation finds the realignment chain invalid for the current settlement day, a new valid chain can be built but the transaction is already partially settled — [[t2s-cancellation]] T2S UDFS R2026.JUN, §1.6.1.5.3 "Cancellation by the system", PDF 284; version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026. LIMITATIONS carried: **T2S-native functional description for R2026.JUN, not a local participant interface specification, production XSD or message usage guideline**; and **local legal effects of cancellation (for example Milan Article 70) are separate sections at their own review date** — none of those local sections is in this bundle. Practical consequence: a matched instruction can disappear well before day 60.

**Documented requirement — the two periods sit either side of a different rule.** Once an instruction is matched, T2S requires **bilateral cancellation**: cancellation is only possible if both counterparties send their cancellation instructions for each leg separately, or if an authorised T2S Party sends one cancellation instruction carrying the information of both legs; an unmatched instruction's cancellation is executed or denied immediately after validation — [[t2s-cancellation]] §1.6.1.5.3, PDF 282 with Table 60 (PDF 283) and footnote 195; reviewed 14 September 2026. And the matching section states plainly that T2S automatically cancels instructions that remain unmatched after a certain period, after first sending a Settlement Allegement to the counterparty — [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3, PDF 271; reviewed 13 September 2026 (LIMITATION: functional matrix only; no production XML/XSD validation or local interface certification).

**Documented requirement — why "matched but unsettled" exists at all.** The posting application process checks whether settlement can be achieved "considering their eligibility to settlement and the available resources", and instructions are submitted to posting at the Intended Settlement Date — [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1–1.6.1.8.2, PDF 303–304; reviewed 13 September 2026. A matched instruction that lacks securities or cash simply keeps being recycled until it settles, is cancelled, or hits the matched-instruction period.

## Reasoned inference and what it does not cover

**Reasoned inference (derived from §1.6.1.7.3 and footnotes 199–200).** Because both periods are T2S Operator parameters and the footnotes describe the *current* values, 20 and 60 working days should be treated as the values documented in the R2026.JUN UDFS at the 14 September 2026 review date, not as permanent constants. If a number matters contractually, confirm the operator configuration for the business date in question.

**Reasoned inference (derived from the definition of the period in working/business days).** "Working days" is counted on the applicable settlement-day calendar, which the UDFS cross-references to its Settlement Day section — that section was **not retrieved**, so the exact calendar and any market-specific closing days behind the count are **not in reviewed evidence**.

**Unresolved requirement.** Whether your CSD applies any earlier local cancellation, hold or housekeeping rule ahead of the T2S period is **not in reviewed evidence**: no CSD rulebook section was retrieved for this question, and a T2S-native description is not a local interface or local legal statement.

**Proposed design choice (yours, not a platform rule).** If you build ageing alerts, key them on D1 (the later of ISD and the last status change) rather than on instruction creation, and raise the alert several working days before the applicable period expires, since T2S sends no daily recycling message. Choose your own lead time; the evidence supports the D1 basis, not any particular alert threshold.

## Open items

1. **Numeric value of the recycling period for unmatched Cancellation Instructions** — referenced in §1.6.1.7.3 but not quantified in the reviewed excerpt.
2. **Reason codes** accompanying the automatic-cancellation message — not in reviewed evidence; the excerpt points to Status Management (page marker [653]) and Message subscription (page marker [135]), neither retrieved.
3. **Settlement Day / calendar section** (page marker [155]) — needed to convert "working days" into concrete dates for a given market.
4. **Business Validation (page marker [218]) and Realignment (page marker [373])** — needed to assess the non-recycling automatic-cancellation triggers listed in [[t2s-cancellation]].
5. **External-CSD configuration** — whether a given external issuer CSD is configured as not compliant with automatic cancellation is a per-CSD configuration that reviewed evidence does not certify.
6. **Local CSD overlay** — for Milan, Copenhagen, Porto, Athens or Oslo specifics, the relevant rulebook and instructions sections at their own review dates are needed; official route is the CSD's public documentation hub or its client platform for entitlement-restricted material. I do not contact them on your behalf.

All values above are stated as reviewed on **14 September 2026** (recycling and cancellation) and **13 September 2026** (matching and posting), for platform release **R2026.JUN**.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:01:07.653411+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_recycling_periods"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-recycling]] — Instruction recycling periods (20 and 60 working days) and automatic cancellation (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.7 with footnotes 199–200; PDF 296–299 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: External-CSD exception to automatic cancellation is stated; individual configurations are not certified.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.7 with footnotes 199–200; PDF 296–299):
1.6.1.7 Instructions Recycling


 2    1.6.1.7.1 Concept

 3    At each end of a Settlement Day (See section Settlement Day [ 155]), T2S recycles pending instructions for
 4   a period of time known as recycling period, which is defined as the number of working days a pending in-
 5    struction can remain in T2S, before being cancelled by the system.

 6                           DIAGRAM 73 - INSTRUCTION RECYCLING APPLICATION PROCESS





 7

 8    1.6.1.7.2 Overview

 9   The recycling of an instruction in T2S triggers the revalidation process at the Start of Day, as described in
10    section Business Validation [ 218]. The Instruction Recycling process manages the automatic cancellation of
11     all the pending instructions that have exceed their recycling period in T2S.


12    1.6.1.7.3 Recycling Process

13   T2S manages two different recycling periods for pending instructions in the system, i.e. the recycling period
14    for pending Unmatched Instructions and the recycling period for pending Matched Instructions and Settle-
15   ment Restrictions.



                                                                                            Page 296 of 2017



[PDF page 297]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   The Recycling period for Unmatched Instructions 199 (i.e. the number of days during which an unmatched
 2    instruction can be matched in T2S) applies to Unmatched Settlement Instructions and Cancellations Instruc-
 3    tions that need to be matched.

 4   Unmatched Settlement Instructions are recycled in T2S for a period of working days configured by the T2S
 5    Operator, starting from the Intended Settlement Date or the date of the last status change of the instruction
 6    (e.g. T2S considers a change of Party Hold status from “Yes” to “No” as a status change) depending on
 7    which date is the latest. Any status value change is considered for restarting the count of the number of
 8    days for the recycling period. For more information on status changes see section Status Management
 9    [ 653].

10                     DIAGRAM 74 - RECYCLING PERIOD FOR UNMATCHED SETTLEMENT INSTRUCTIONS





11

12   Unmatched Cancellation Instructions that need to be matched in T2S are recycled for a period of working
13    days configured by the T2S Operator, starting from its reception in T2S until its matching occurs.





     _________________________


        199   Current recycling period for unmatched instructions of 20 working days.


                                                                                            Page 297 of 2017



[PDF page 298]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                    DIAGRAM 75 - RECYCLING PERIOD FOR UNMATCHED CANCELLATION INSTRUCTIONS





 2

 3    Pending Matched Instructions and Settlement Restrictions are recycled in T2S for a period of working days
 4     200 configured by the T2S Operator until its settlement or cancellation occurs (See section Instruction Cancel-
 5    lation [ 280]).

 6   As an exception, in an external CSD scenario, instructions fulfilling the following conditions will not be auto-
 7    matically cancelled, but will remain pending in the system and recycled for an indefinite period of time until
 8   any of the conditions listed below becomes unfulfilled or they are cancelled by the T2S Actors:

 9         l  Any of the relevant CSDs is external to T2S;

10         l  The external CSD is the issuer of the security; and

11         l  The external CSD is configured as not compliant with the T2S automatic cancellation of instruction.

12

13

14





     _________________________


        200   Current recycling period for matched instructions of 60 working days.


                                                                                            Page 298 of 2017



[PDF page 299]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                          DIAGRAM 76 - RECYCLING PERIOD FOR MATCHED INSTRUCTIONS





 2

 3   T2S does not send a daily message to the T2S Actors informing about the result of the recycling process.
 4    Only when an instruction exceeds its recycling period, T2S cancels it automatically and sends a message to
 5    the T2S Actor informing on the cancellation of its instruction with the corresponding reason code(s). The
 6    dialogue is reflected in section Send Settlement Instruction. Interested parties can also be informed depend-
 7    ing on their message subscription preferences (see section Status Management [ 653] and section Message
 8    subscription [ 135]).

 9   T2S calculates the recycling period applicable to a pending instruction as follows:

10    At EoD process, T2S cancels all instructions that have reached their recycling period. The recycling period is
11    considered as reached when: The difference between “D1” (latest date between the ISD and the business
12   day of the last status change of the instruction) and “D2” (current business date) equals the number of
13    business days defined for the applicable recycling period.
14   Once the recycling period is reached, T2S stops recycling the instruction, leading to the automatic cancella-
15    tion of the instruction in the system and sending of the corresponding status notification to the T2S Actors.
16    Nevertheless, until the EoD the instruction is still processed as normal throughout the whole business day.
17

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_cancellation_process"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-cancellation]] — Instruction cancellation: bilateral cancellation, CoSD cancellation and system cancellation (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.5 with Table 60 and footnote 195; PDF 280–284 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Local legal effects of cancellation (e.g. Milan Article 70) are separate sections at their own review date.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.5 with Table 60 and footnote 195; PDF 280–284):
1.6.1.5 Instruction Cancellation


14    1.6.1.5.1 Concept

15   T2S Actors are able to cancel their Unsettled Settlement Instructions or Settlement Restrictions through a
16    Cancellation Instruction. The T2S Party, the relevant CSD and the authorized parties can cancel instructions
17    of a given T2S Actor.

18    Additionally, under specific conditions, T2S cancels instructions automatically (e.g. when an Unmatched Set-
19    tlement Instruction has exceeded its recycling period in T2S).





                                                                                            Page 280 of 2017



[PDF page 281]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                          DIAGRAM 67 - INSTRUCTION CANCELLATION APPLICATION PROCESS





 2

 3    1.6.1.5.2 Overview

 4    After its validation, T2S processes Cancellation Instructions sent by a T2S Actor to cancel previously sent
 5    Settlement Instructions or Settlement Restrictions, unless it fulfils any of the following conditions:

 6         l  The Settlement Status of the Referenced Settlement Instruction or Settlement Restriction is “Settled” or
 7        “Cancelled”;

 8         l  There is a pending Cancellation Instruction for the same Settlement Instruction;

 9         l  The Referenced Settlement Instruction is identified as CoSD, and the Instructing Party is not the relevant
10      CSD or the relevant Administering Party (See section Conditional Settlement [ 452]);

11         l  There is a Realignment Instruction related with the Referenced Settlement Instruction that fulfils a CoSD
12        Rule, and the Instructing Party is not the relevant CSD.

13     If the Cancellation Instruction fulfils any of these conditions, the Cancellation Instruction is denied and T2S
14   communicates its denial together with the relevant reason code to the T2S Actor or any interested party,
15    depending on their message subscription preferences (see Section Status Management [ 653]).





                                                                                            Page 281 of 2017



[PDF page 282]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   T2S Actors are not able to cancel other instruction types rather than Settlement Instructions or Settlement
 2    Restrictions (e.g. T2S Actors cannot cancel Realignment instructions). Additionally, T2S Actors can cancel the
 3    unsettled remaining part of a partially settled Settlement Instruction or Settlement Restriction.

 4    Cancellation Instructions are immediately executed or denied during the Daytime Window, with the excep-
 5    tion of Cancellation Instructions that need to be matched in T2S to cancel two matched Settlement Instruc-
 6    tions (“bilateral cancellation”). During the Night time sequences, the instructions received are not taken into
 7    account until the end of the sequence.


 8    1.6.1.5.3 Cancellation process

 9    InstructionCancellationprocess

10   T2S Actors can send Cancellation Instructions to cancel previously sent Settlement Instructions or Settle-
11   ment Restrictions. The dialogue between T2S and T2S Actors referring to the cancellation of the referenced
12    Settlement Instructions or Settlement Restrictions is described as part of the overall process for each type of
13    instructions in section Send Cancellation Instruction of a Settlement Instruction or a Settlement Restriction
14   on Securities Position and section Send Cancellation Instruction of a Settlement Restriction on cash balance
15    while the precise description of the cancellation Processing of a Settlement Instruction or Settlement Re-
16     striction (either because a T2S Actor has send a Cancellation Instruction or because any other reason) is
17    reflected in section Settlement Instruction Cancellation Processing, section Securities Settlement Restriction
18    Cancellation Processing and section Cash Settlement Restriction Cancellation Processing.

19     If the referenced instruction is an Unmatched Settlement Instruction or a Settlement Restriction, the Cancel-
20    lation Instruction is executed or denied immediately after its validation.

21     If the referenced Settlement Instruction is matched, T2S requires bilateral cancellation and the cancellation
22     is only possible if both Counterparties send their Cancellation Instructions to cancel each leg separately or if
23    the Cancellation Instruction is sent with the information of both legs by an authorised T2S Party 195.

24   A Cancellation Instruction can be used to cancel both legs at the same time or only one leg of a Settlement
25    Instruction that entered T2S as already matched depending if the reference used in the Cancellation Request
26    refers to the information of one leg or both legs of the Settlement Instruction as shown in the table below
27    (see section Instruction Types [ 86]).





     _________________________


        195   In case the CSD and the Party send their respective cancellation instructions for the same leg, and both remain pending in the system awaiting for
                   their counterparty in order to match and be executed, T2S matching process prioritises for the matching the CSD cancellation instruction over the
                 party cancellation instruction.


                                                                                            Page 282 of 2017



[PDF page 283]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                               TABLE 60 - REFERENCES USED IN CANCELLATION SCENARIOS
 2

                                      ALREADY MATCHED SETTLEMENT      SETTLEMENT INSTRUCTIONS
                                              INSTRUCTION                 MATCHED IN T2S

        Cancellation Instruction of one leg of             T2S Reference                  T2S Actor Reference
       the Settlement Instruction (two Cancel-                                                                                                         or
        lations needed)
                                                                               T2S Reference

        Cancellation Instruction of both legs of         T2S Actor Reference                      X
       the Settlement Instruction

 3    For Cancellation Instructions referring to both legs of the Settlement Instruction (i.e. if the T2S Actor In-
 4    struction Reference refers to a Settlement Instruction sent as already matched to T2S), T2S splits the infor-
 5    mation of the Cancellation instruction into two separate maintenance instructions, one per each leg of the
 6    referenced Settlement Instruction. As the inbound message related to the already matched maintenance
 7    instruction is split internally, two different Cancellation Instructions are created in T2S.

 8   T2S informs the T2S Actor on the result of the cancellation process, via a Status Advice message. Interested
 9    parties can also be informed depending on their message subscription preferences (see section Status Man-
10   agement [ 653] and section Message subscription [ 135]).

11    In case of already matched Cancelation Instructions, the status reporting derived from the lifecycle of each
12    Cancellation Instruction created in T2S is handled separately. Nevertheless, the T2S Actor may subscribe to
13    the notifications of one of the two legs of the already matched maintenance instruction only.

14    CancellationofCoSDprocess

15   When a Settlement Instruction is identified as CoSD, only Administering Parties or the relevant CSD can can-
16    cel it under certain circumstances:

17         l  In case there is more than one Administering Party for a Settlement Instruction, each Administering Par-
18        ty should send its CoSD Cancellation Instruction for the relevant Settlement Instruction without a need
19        to specify any CoSD rule in the message (i.e. The Administering Parties only have to send one Cancella-
20        tion Instruction regardless if more than one CoSD rule applies) (See section Conditional Settlement
21        [ 452]), or;

22         l  The Instructing Party’s CSD involved in the Settlement Instruction (i.e. the CSD that owns the securities
23       account) should send a Cancellation Instruction for the relevant Settlement Instruction.

24    In both cases, cancellation is only possible if either all Administering Parties or the CSD of each Settlement
25    Instruction send their Cancellation Instruction. Cancellation takes place upon the reception by T2S of one
26    valid Cancellation Instruction for each of the two matched Settlement Instructions.

27   T2S does not allow Administering Parties to request the cancellation of a Settlement Instruction, if at least
28   one CoSD rule applied/applies to at least one underlying Realignment Instruction.

29   T2S rejects cancellation requests submitted by other T2S Actors (i.e. CSD Participants), when the referenced
30    Settlement Instruction is identified as CoSD.

31    Cancellationbythesystemprocess

                                                                                            Page 283 of 2017



[PDF page 284]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   T2S automatically cancels pending instructions in the system under the following conditions:

 2         l  Settlement Instructions, Settlement Restrictions and Cancellation Instructions once they exceed their re-
 3        cycling period in T2S (See section Instructions Recycling [ 296]).

 4         l  Settlement Instructions when the realignment chain cannot be built (See section Realignment [ 373]).

 5         l  Instructions that do not successfully pass the revalidation process. The revalidation process is triggered
 6        at the Start of Day in T2S and by a change in the Reference Data that affects the instruction (See sec-
 7        tion Business Validation [ 218]).

 8         l  Settlement instructions that during the Start of Day revalidation process it is detected that the realign-
 9      ment chain used for settlement has become invalid for the current settlement day and while a new valid
10       realignment chain can be built, the transaction is already partially settled (See section Realignment
11        [ 373]) Pending Cancellation Instruction in the system when one of the conditions for the denial of a
12        Cancellation Instruction is fulfilled. (See section Send Cancellation Instruction of a Settlement Instruction
13        or a Settlement Restriction on Securities Position and section Send Cancellation Instruction of a Settle-
14      ment Restriction on cash balance.)


15    1.6.1.5.4 Parameters Synthesis

16   No specific configuration from T2S Actor is needed in T2S Reference Data.


17

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
