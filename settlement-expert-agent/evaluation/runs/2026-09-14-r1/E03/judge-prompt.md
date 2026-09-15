You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
For a Milan participant: (a) can I cancel a matched instruction unilaterally, and (b) how long does T2S keep an unmatched instruction before it is cancelled automatically?

# Case category: multi-intent (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Unilateral cancellation only before matching and only if not entered as non-changeable; matched instructions need bilateral cancellation or mandate route (Art 70).",
  "Unmatched instructions recycle for 20 working days from ISD or last status change, matched ones 60 working days (UDFS §1.6.1.7 footnotes 199-200; Milan Instructions §1.6 states the same 20/60).",
  "Two intents answered separately with their review dates (13 and 14 September)."
]
Fail conditions (must NOT appear):
[
  "State unconditional yes/no for cancellation.",
  "Give a recycling period other than 20/60 working days."
]
Expected sections (if any): ['milan-finality', 't2s-recycling']
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
# (a) Unilateral cancellation of a matched instruction; (b) how long an unmatched instruction survives in T2S

## Direct answer

**(a) No.** Once your instruction is matched you cannot cancel it unilaterally. Milan's rules allow unilateral cancellation only up to the moment of matching (and only if the instruction was not entered as non-changeable); a matched instruction requires **bilateral** cancellation, and T2S enforces the same thing technically — both counterparties must send cancellation instructions for their own leg, unless the instruction entered T2S as already matched and an authorised T2S party sends one cancellation carrying both legs. CoSD instructions are narrower still: in Milan they may only be cancelled by Monte Titoli.

**(b) 20 working days for an unmatched instruction**, as the current value: T2S recycles pending instructions for a "recycling period" — the number of working days a pending instruction may remain in T2S before the system cancels it — configured by the T2S Operator, and the UDFS footnote records the current unmatched period as 20 working days. The count runs from the intended settlement date **or the date of the last status change, whichever is later**, and any status change restarts it. Matched instructions have a separate, longer period (currently 60 working days). Note two qualifications: the value is operator-configured, not a fixed rule, and Milan's own automatic-cancellation article refers to "the time limits provided in the Instructions", a document not in this bundle.

**Routing note.** I corrected the routing for this case once: the prepared bundle covered matching and cancellation but carried no retrieval for recycling periods, which is the whole of part (b). I re-ran the retriever with `cancellation_rules` (Milan), `t2s_cancellation_process` (Milan), `t2s_recycling_periods` (Milan) and `matching_concept` (Milan). All four retrievals returned `evidence_only`; nothing was blocked, and no retrieval reported missing context or an unreviewed knowledge date.

---

## (a) Cancelling a matched instruction

### What Milan's Regulations say

**Documented requirement.** All from [[milan-finality]] Regulations as of 26 January 2026, Articles 69–71 and 72(1)–(3), PDF 50–51 (printed 49–50); version 26 January 2026; reviewed 13 September 2026; English translation and the **Italian text prevails**; source identity checked, no independent whole-edition supervisory approval certification:

1. **Unilateral cancellation, and its cut-off.** "Settlement Instructions may be unilaterally cancelled by the Participant which entered them **up to the time of the matching**, on condition that such Settlement Instructions were not entered as non-changeable" (Article 70(1)).
2. **After matching it is bilateral.** "Matched settlement Instructions may be cancelled bilaterally, with the consent of both Participants, or upon request of an entity acting on their behalf, subject to the prior submission to Monte Titoli of the relevant mandate" (Article 70(2)).
3. **The cancellation itself must match.** Cancellations are sent with the methods and time frames provided for in the Instructions, go through the acquisition phase and, if they refer to matched instructions, the matching phase; "When the cancellations are matched, the original settlement Instructions are cancelled" (Article 70(3)).
4. **CoSD.** "CoSD Settlement Instructions may only be cancelled by Monte Titoli" (Article 70(6)).
5. **Blocking by CCPs and market management companies.** Market management companies and central counterparties may ask Monte Titoli to block the cancellation functionality for their instructions (Article 70(4)); Monte Titoli may also enter cancellations at participants' request and in the other cases established by the Rules (Article 70(5)).
6. **Why matching is the boundary.** Instructions "cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70(2)" (Article 72(2)); the transfer becomes final only at the debiting of cash, or of securities where settlement by cash is not provided for (SF3, Article 72(3)).

LIMITATIONS carried with the above: SF2 retains the Article 70(2) bilateral cancellation, and SF3 is the relevant cash debit or the securities debit for free-of-payment instructions; no insolvency runbook, legal opinion, or the unreviewed remainder of Article 72 is admitted here.

*Explanation of the term (background wording, not a documented requirement):* "non-changeable" is the status under which an instruction is entered such that the participant may not later modify or unilaterally cancel it; "CoSD" is conditional settlement, where settlement depends on a condition administered by a designated party.

### How T2S enforces it

**Documented requirement.** All from [[t2s-cancellation]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.5 with Table 60 and footnote 195, PDF 280–284; version R2026.JUN; reviewed 14 September 2026 (underlying source reviewed 13 September 2026); body language English, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification:

| Situation | T2S behaviour |
|---|---|
| Referenced instruction **unmatched** | The cancellation instruction "is executed or denied immediately after its validation". |
| Referenced instruction **matched** | "T2S requires bilateral cancellation and the cancellation is only possible if both Counterparties send their Cancellation Instructions to cancel each leg separately **or** if the Cancellation Instruction is sent with the information of both legs by an authorised T2S Party." |
| Instruction that entered T2S **as already matched** | One cancellation instruction may address both legs or a single leg, depending on the reference used (Table 60: T2S Reference vs T2S Actor Reference). Where it addresses both legs, T2S splits it internally into two maintenance instructions, one per leg, creating two cancellation instructions. |
| **CoSD** instruction | Only Administering Parties or the relevant CSD may cancel; cancellation occurs on receipt of one valid cancellation instruction for each of the two matched instructions; T2S **rejects** cancellation requests from other T2S actors (i.e. CSD participants) for a CoSD instruction, and does not allow Administering Parties to request cancellation if at least one CoSD rule applies to an underlying realignment instruction. |
| **Denial conditions** | A cancellation instruction is denied if the referenced instruction's settlement status is "Settled" or "Cancelled"; if a cancellation instruction for it is already pending; if the referenced instruction is CoSD and the instructing party is not the relevant CSD or administering party; or if a realignment instruction related to it fulfils a CoSD rule and the instructing party is not the relevant CSD. T2S communicates the denial with the relevant reason code, subject to message subscription preferences. |
| **Timing of execution** | Cancellation instructions are immediately executed or denied during the Daytime Window, except those needing to be matched in T2S (bilateral cancellation); during night-time sequences, instructions received are not taken into account until the end of the sequence. |
| **What cannot be cancelled by actors** | T2S actors cannot cancel instruction types other than settlement instructions and settlement restrictions — for example they cannot cancel realignment instructions. They can cancel the unsettled remaining part of a partially settled instruction. |
| **Competing cancellations** | Footnote 195: where the CSD and the party each send a cancellation instruction for the same leg and both remain pending awaiting the counterparty, the T2S matching process prioritises the CSD cancellation instruction over the party cancellation instruction. |

LIMITATIONS carried with this table: the local legal effects of cancellation (for example Milan's Article 70) sit in separate sections at their own review dates; and this is a T2S-native functional description for R2026.JUN — **not** a local participant interface specification, a production XSD or a message usage guideline. I therefore state no field, message version or reason-code value.

**Reasoned inference** (derived from Article 70(2) read with §1.6.1.5.3): the only route that looks like a single-message cancellation of a matched instruction is not a unilateral right. It is either an authorised T2S party instructing both legs of an instruction that entered T2S as already matched, or, in Milan's wording, an entity acting on behalf of both participants under a mandate previously submitted to Monte Titoli. In both cases the other side's consent is presupposed; nothing in the reviewed evidence lets one counterparty cancel against the other's will.

**Documented requirement — the background reason this matters operationally.** Matching only establishes that both parties agree on the settlement terms [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2, PDF 267–271, Diagrams 55–57 and footnote 194; reviewed 13 September 2026 (LIMITATIONS: functional matrix only, no production XML/XSD validation or local interface certification; diagram DVP/DWP labels retained while the paragraph mentions DVP/PFOD). The securities move only when posting succeeds against eligibility and available resources, which is what produces irrevocability of the settlement [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1 and first overview paragraph, PDF 303–304; reviewed 13 September 2026.

---

## (b) How long T2S keeps an unmatched instruction

**Documented requirement.** All from [[t2s-recycling]] T2S UDFS R2026.JUN, §1.6.1.7 "Instructions Recycling" with footnotes 199–200, PDF 296–299; version R2026.JUN; reviewed 14 September 2026 (underlying source reviewed 13 September 2026); body language English, no authoritative language independently established:

1. **The concept.** "At each end of a Settlement Day, T2S recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in T2S, before being cancelled by the system." Recycling triggers the revalidation process at Start of Day, and the recycling process manages the automatic cancellation of all pending instructions that have exceeded their recycling period.
2. **Two periods.** T2S manages one recycling period for pending **unmatched** instructions and another for pending **matched** instructions and settlement restrictions.
3. **Unmatched — the number.** Unmatched settlement instructions are recycled "for a period of working days **configured by the T2S Operator**", and footnote 199 states: "Current recycling period for unmatched instructions of **20 working days**." The same unmatched period applies to cancellation instructions that need to be matched, counted from their reception in T2S until matching occurs.
4. **When the clock starts — and restarts.** The count starts "from the Intended Settlement Date or the date of the last status change of the instruction… depending on which date is the latest", and "any status value change is considered for restarting the count of the number of days for the recycling period". The UDFS gives a change of Party Hold status from "Yes" to "No" as an example of a status change.
5. **Matched — for contrast.** Pending matched instructions and settlement restrictions are recycled for a period of working days configured by the T2S Operator until settlement or cancellation occurs; footnote 200 states the current matched period as **60 working days**.
6. **The exception that removes the deadline.** In an external-CSD scenario, instructions are **not** automatically cancelled but remain pending and are recycled "for an indefinite period of time" while all three conditions hold: any of the relevant CSDs is external to T2S; the external CSD is the issuer of the security; and the external CSD is configured as not compliant with T2S automatic cancellation of instructions. This lasts until one of those conditions ceases to hold or the T2S actors cancel the instruction.

LIMITATIONS carried with these six points: the external-CSD exception is stated but **individual configurations are not certified** — whether a given external CSD is flagged non-compliant is not established here; and this is a T2S-native functional description for R2026.JUN, not a local participant interface specification, production XSD or message usage guideline.

**Documented requirement — the same outcome in Milan's own rules, without a number.** "Automatic cancellation of settlement instructions from the T2S platform is disposed when instructions: a) have not passed the daily validation phase; b) are not matched or are not settled **within the time limits provided in the Instructions**"; participants are informed of the progress and outcome of the cancellation process and of any automatic cancellation. [[milan-finality]] Articles 70(7)–(8), Regulations as of 26 January 2026, PDF 50 (printed 49); version 26 January 2026; reviewed 13 September 2026; English translation, Italian text prevails. **Documented requirement** also from the same source: T2S automatically cancels pending instructions once they exceed their recycling period, where the realignment chain cannot be built, where instructions fail revalidation (triggered at Start of Day and by reference-data changes affecting the instruction), and in the Start-of-Day realignment-chain scenario described for partially settled transactions [[t2s-cancellation]] §1.6.1.5.3 "Cancellation by the system process", PDF 283–284; reviewed 14 September 2026.

**Unresolved requirement — the two caveats you should carry into any operational rule.**
- The 20-working-day figure is a **footnoted current operator configuration**, not a fixed provision: the body text says the period is "configured by the T2S Operator". It is accurate as of the reviewed edition (R2026.JUN, reviewed 14 September 2026) and could be reconfigured without the body text changing. Nothing in the bundle establishes a notification route for such a change.
- Milan's Article 70(7)(b) points to "the time limits provided in the Instructions". **Monte Titoli's Instructions are not in this bundle**, so I cannot confirm that Milan applies no shorter or additional local limit, nor state what those limits are.

**Reasoned inference** (derived from points 3 and 4 above): because a status change restarts the count, an unmatched instruction that is repeatedly amended or put on and off hold can remain in T2S considerably longer than 20 working days from its original intended settlement date. The restart rule is documented; the practical consequence is my inference.

---

## Open items

- **Unresolved requirement — Monte Titoli's own time limits.** The Instructions referenced by Article 70(3) (methods and time frames for sending cancellations) and Article 70(7)(b) (time limits before automatic cancellation) are not in reviewed evidence. Establishing source: Monte Titoli's Instructions / Services Manuals, via the Euronext Securities Milan public documentation hub or the client documentation service.
- **Unresolved requirement — the current operator configuration.** Whether the recycling periods remain at the footnoted 20 and 60 working days after the review date of 14 September 2026 is not established by this bundle; only the R2026.JUN UDFS footnotes are. Establishing source: the T2S operational configuration as published by the Eurosystem / a later UDFS edition.
- **Unresolved requirement — external-CSD configuration.** Whether any CSD relevant to your instruction is external to T2S, is the issuer CSD, and is configured as not compliant with automatic cancellation is not certified by the evidence; this is what decides whether the deadline applies at all.
- **Unresolved requirement — the client interface.** No message name, version, field, reason code or status value for sending or receiving a cancellation is claimed above: the T2S sections are functional descriptions only, and the Milan local interface (X-TRM) specification was not retrieved for this question.
- **Not asserted:** no cut-off time, deadline hour, fee, ISIN or account eligibility appears above; none is in the reviewed evidence for this question.
- No gap id was named by the bundle, and after the routing correction every retrieval returned `evidence_only`.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:58:29.336791+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "cancellation_rules"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-finality]] — Matching, cancellation, hold and SF1/SF2/SF3 (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.
LIMITATION: No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted.
EXCERPT (Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50):
Article 69 – Matching of Settlement Instructions

1. The matching is carried out to check that the information corresponds to the
   settlement instructions entered.
2. The T2S system supplies the participants with complete disclosure regarding
   the  status  of  the  settlement  instructions  entered and  the  settlement
   instructions entered by the counterparty awaiting matching (alledgement).
3. The matching checks referred to in paragraph 1 cover mandatory matching
    fields, but may also regard the non-mandatory matching fields.
4. Unmatched settlement instructions may be changed by the Participants, but
   only as regards status indicators.

Article 70 - Cancellation of the settlement Instructions

1. Settlement Instructions may be unilaterally cancelled by the Participant which
   entered them up to the time of the matching, on condition that such Settlement
   Instructions were not entered as non-changeable.
2. Matched settlement Instructions may be cancelled bilaterally, with the consent
   of both Participants, or upon request of an entity acting on their behalf, subject
   to the prior submission to Monte Titoli of the relevant mandate.
3. Cancellations are sent by the Participants with the methods and the time
   frames provided for in the Instructions. They then go through the acquisition
   phase and,  if referring to matched settlement Instructions, the matching
   phase. When  the  cancellations  are  matched,  the  original  settlement
   Instructions are cancelled.
4. Market Management Companies and central counterparties may ask Monte
    Titoli to block these functionalities with regard to their settlement Instructions,
   according to the methods and conditions provided for in the operating rules for
   these systems and in accordance with the provisions for T2S.
5. Cancellations may also be entered by Monte  Titoli at the request of the
   Participants and in the other cases established by the Rules, in accordance with
   the provisions above.
6. CoSD Settlement Instructions may only be cancelled by Monte Titoli.
7. Automatic cancellation of settlement instructions from the T2S platform is
   disposed when instructions:
   a) have not passed the daily validation phase;
   b) are not matched or are not settled within the time limits provided in the
       Instructions;

8. Participants are informed of the progress and outcome of the cancellation
   process and of any automatic cancellation of settlement Instructions, pursuant
   to the previous paragraph.


49    In force as of 26 January 2026



[PDF page 51]

                                                            SERVICE REGULATIONS


Article 71 – Hold of the Settlement Instructions

1. The participant may hold the settlement of the settlement instructions entered
   by it so as not to subject them to settlement or hold the re-proposal of the
   Settlement Instructions not regulated, also partially, until there is a specific
   release, on condition that these Settlement Instructions have not been entered
   as non-changeable.
2. Market management companies and central counterparties may ask Monte
    Titoli to block the use of this functionality with regard to their settlement
   instructions, according to the methods and conditions provided for in the
   operating rules for these systems and in accordance with the provisions for
   T2S.
3. The settlement may also be put on hold by Monte Titoli, at the request of the
   participants and in the other cases established by the Rules, in accordance with
   the provisions above.

Article 72 – Input into the Settlement System and irrevocability of
settlement Instructions

1. Settlement Instructions are deemed “entered” into the Settlement System,
   pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the
   validation time in T2S ends (SF1).
2. Settlement Instructions cannot be revoked by a participant or a third party
   from the time of their matching in T2S (SF2), without prejudice to the bilateral
   cancellation of settlement Instructions provided for under Article 70 (2).
3. The transfer of securities and cash become final from the time of the debiting
   of the cash, or of the securities when settlement by cash is not provided for.
   (SF3)

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_cancellation_process"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_recycling_periods"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-finality]] — Matching, cancellation, hold and SF1/SF2/SF3 (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.
LIMITATION: No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted.
EXCERPT (Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50):
Article 69 – Matching of Settlement Instructions

1. The matching is carried out to check that the information corresponds to the
   settlement instructions entered.
2. The T2S system supplies the participants with complete disclosure regarding
   the  status  of  the  settlement  instructions  entered and  the  settlement
   instructions entered by the counterparty awaiting matching (alledgement).
3. The matching checks referred to in paragraph 1 cover mandatory matching
    fields, but may also regard the non-mandatory matching fields.
4. Unmatched settlement instructions may be changed by the Participants, but
   only as regards status indicators.

Article 70 - Cancellation of the settlement Instructions

1. Settlement Instructions may be unilaterally cancelled by the Participant which
   entered them up to the time of the matching, on condition that such Settlement
   Instructions were not entered as non-changeable.
2. Matched settlement Instructions may be cancelled bilaterally, with the consent
   of both Participants, or upon request of an entity acting on their behalf, subject
   to the prior submission to Monte Titoli of the relevant mandate.
3. Cancellations are sent by the Participants with the methods and the time
   frames provided for in the Instructions. They then go through the acquisition
   phase and,  if referring to matched settlement Instructions, the matching
   phase. When  the  cancellations  are  matched,  the  original  settlement
   Instructions are cancelled.
4. Market Management Companies and central counterparties may ask Monte
    Titoli to block these functionalities with regard to their settlement Instructions,
   according to the methods and conditions provided for in the operating rules for
   these systems and in accordance with the provisions for T2S.
5. Cancellations may also be entered by Monte  Titoli at the request of the
   Participants and in the other cases established by the Rules, in accordance with
   the provisions above.
6. CoSD Settlement Instructions may only be cancelled by Monte Titoli.
7. Automatic cancellation of settlement instructions from the T2S platform is
   disposed when instructions:
   a) have not passed the daily validation phase;
   b) are not matched or are not settled within the time limits provided in the
       Instructions;

8. Participants are informed of the progress and outcome of the cancellation
   process and of any automatic cancellation of settlement Instructions, pursuant
   to the previous paragraph.


49    In force as of 26 January 2026



[PDF page 51]

                                                            SERVICE REGULATIONS


Article 71 – Hold of the Settlement Instructions

1. The participant may hold the settlement of the settlement instructions entered
   by it so as not to subject them to settlement or hold the re-proposal of the
   Settlement Instructions not regulated, also partially, until there is a specific
   release, on condition that these Settlement Instructions have not been entered
   as non-changeable.
2. Market management companies and central counterparties may ask Monte
    Titoli to block the use of this functionality with regard to their settlement
   instructions, according to the methods and conditions provided for in the
   operating rules for these systems and in accordance with the provisions for
   T2S.
3. The settlement may also be put on hold by Monte Titoli, at the request of the
   participants and in the other cases established by the Rules, in accordance with
   the provisions above.

Article 72 – Input into the Settlement System and irrevocability of
settlement Instructions

1. Settlement Instructions are deemed “entered” into the Settlement System,
   pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the
   validation time in T2S ends (SF1).
2. Settlement Instructions cannot be revoked by a participant or a third party
   from the time of their matching in T2S (SF2), without prejudice to the bilateral
   cancellation of settlement Instructions provided for under Article 70 (2).
3. The transfer of securities and cash become final from the time of the debiting
   of the cash, or of the securities when settlement by cash is not provided for.
   (SF3)

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
