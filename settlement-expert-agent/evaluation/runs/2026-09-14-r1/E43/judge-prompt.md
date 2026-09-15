You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What can I amend on a settlement instruction after it has matched in T2S, and what about a partially settled one?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Only partial settlement indicator/threshold type, priority and linkages block; one indicator per instruction; denied if settled/cancelled, CoSD (except linkage removal by CSD), or partially settled other than priority; already-matched leg references (Table 58-59)."
]
Fail conditions (must NOT appear):
[
  "Allow amending economic fields."
]
Expected sections (if any): ['t2s-amendment']
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
# Amending a settlement instruction in T2S after matching, and when it is partially settled

## Direct answer

**After matching you can amend only three process indicators — Partial Settlement Indicator (and its threshold type), Priority, and the Linkages Block — one per Amendment Instruction, and only on your own leg; any other field change requires cancelling the instruction and instructing it again.** **Once the instruction is partially settled, "Priority" is the only process indicator you may still amend**; an Amendment Instruction referring to anything else on a partially settled instruction is denied.

All three retrievals in this bundle returned `evidence_only`, so there is no blocked, needs_context or needs_refresh status to disclose. Everything below is T2S-native functional description for platform release **R2026.JUN** from the T2S UDFS; the sections were reviewed on **13 and 14 September 2026** (source document reviewed 13 September 2026) and each carries the limitation that this is **not a local participant interface specification, production XSD or message usage guideline**, and that no independent whole-edition supervisory approval certification exists for the source.

*Term explanations (background, not documented requirements): a "process indicator" is a control flag on an instruction that steers how T2S processes it, as opposed to the business content of the trade; an "Amendment Instruction" is a maintenance instruction referencing an existing instruction; "partially settled" means part of the quantity has already been transferred and a pending part remains.*

---

## 1. What may be amended after matching

**Documented requirement — the permitted process indicators.** T2S Actors can only amend the following process indicators of a **Settlement Instruction**: Partial Settlement Indicator and threshold type; Priority; Linkages Block. For a **Settlement Restriction** only Priority and the Linkages Block may be amended. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3, PDF page 279; reviewed 14 September 2026; English, no separate authoritative language established; T2S-native functional description only.

Table 59 states the same matrix by instruction state:

| Instruction state | "Partial Settlement Indicator" | "Linkages Block" | "Priority" |
|---|---|---|---|
| Settlement Instruction | YES | YES | YES |
| Settlement Restriction | NO | YES | YES |
| Partially Settled Instruction | NO | NO | YES |

[[t2s-amendment]] T2S UDFS R2026.JUN, Table 59 in §1.6.1.4, PDF page 280; reviewed 14 September 2026.

**Documented requirement — one indicator per instruction, and everything else means cancel and re-instruct.** "T2S Actors are only allowed to modify one process indicator per Amendment Instruction. If the T2S Actor wants to modify a second process indicator, a new Amendment Instruction is required. If the T2S Actor wants to modify other fields of the instruction, it has to cancel the referenced instruction and instruct it again." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 279; reviewed 14 September 2026.

**Documented requirement — who may amend.** T2S Actors send an Amendment Instruction to modify a process indicator "depending on its instruction type and its settlement status"; the T2S Party, the relevant CSD and the authorized parties can amend instructions of a given T2S Actor. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.1, PDF page 277; reviewed 14 September 2026.

**Documented requirement — when the amendment is denied.** T2S accepts and processes an Amendment Instruction that passes Business Validation **unless** any of the following is fulfilled, in which case it is denied:

1. the Settlement Status of the referenced Settlement Instruction or Settlement Restriction is "Settled" or "Cancelled";
2. the referenced Settlement Instruction is identified as CoSD and the Amendment Instruction does not aim to remove a linkage having the CSD as the Instructing Party;
3. the referenced Settlement Instruction or Settlement Restriction is partially settled and the Amendment Instruction refers to a process indicator other than "Priority".

[[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 278; reviewed 14 September 2026.

**Documented requirement — amendment does not reach other instruction types.** "T2S Actors are not able to amend other instruction types than Settlement Instructions or Settlement Restrictions … (i.e. Realignment instructions cannot be amended by T2S Actors)." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 278; reviewed 14 September 2026.

**Reasoned inference — matching itself is not what limits you.** None of the three denial conditions is keyed to match status; they are keyed to settlement status, CoSD identification and partial settlement. Derived from the denial list in [[t2s-amendment]] §1.6.1.4.2. What matching changes is *whose* leg an Amendment Instruction can reach and which reference identifies it, per Table 58 below. The set of amendable indicators is the same before and after matching; the reviewed excerpt does not state a separate pre-matching regime, so do not read one into it.

### Whose leg you can amend (Table 58)

**Documented requirement.** An Amendment Instruction can amend a process indicator of both legs at the same time, or only one leg, of a Settlement Instruction **that entered T2S as already matched**, depending on the reference used:

| Amendment Instruction of … | Instruction sent to T2S **already matched** | Instruction **matched in T2S** |
|---|---|---|
| one leg of the Settlement Instruction | T2S Reference | T2S Actor Reference **or** T2S Reference |
| both legs of the Settlement Instruction | T2S Actor Reference | X (not available) |

[[t2s-amendment]] T2S UDFS R2026.JUN, Table 58 in §1.6.1.4.2, PDF pages 278–279; reviewed 14 September 2026.

For a both-legs Amendment Instruction on an already-matched Settlement Instruction, T2S splits the amendment into two separate maintenance instructions, one per leg, so two different Amendment Instructions are created in T2S; status reporting derived from each lifecycle is handled separately, and the T2S Actor may subscribe to notifications of only one of the two legs. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2 and §1.6.1.4.3, PDF pages 279–280; reviewed 14 September 2026.

**Reasoned inference — for an instruction matched *in* T2S you reach only your own leg.** Table 58 marks the both-legs cell "X" for instructions matched in T2S, so a party that matched in T2S amends one leg only. Derived from Table 58 in [[t2s-amendment]]. This matters for the Partial Settlement Indicator: partial settlement eligibility requires that the indicator "is not set to 'No' in any of the Settlement Instructions" [[t2s-partial-settlement]] T2S UDFS R2026.JUN, §1.6.1.9.3, PDF page 343; reviewed 14 September 2026 — that is, on both sides. Amending your own leg alone therefore does not by itself make a matched pair partially settleable if the counterparty's instruction says "No". The reviewed evidence does not say whether the counterparty is notified of your amendment beyond the general subscription mechanism.

**Documented requirement — how you learn the outcome.** T2S informs the T2S Actor of the result of the amendment process through a Status Advice message; interested parties can also be informed depending on their message subscription preferences. No specific T2S Reference Data configuration by the T2S Actor is needed for amendment. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3–§1.6.1.4.4, PDF page 280; reviewed 14 September 2026.

### What you cannot amend, and therefore must cancel and re-instruct

**Reasoned inference — derived from §1.6.1.4.3 read with the matching-field tables.** Because only the three process indicators are amendable, the business content that T2S matches on cannot be changed by amendment. The reviewed matching evidence lists these as **mandatory** matching fields for both DVP/DWP and FOP: Payment Type, Securities Movement Type, ISIN Code, Trade Date, Settlement Quantity, Intended Settlement Date, Delivering Party BIC, Receiving Party BIC, CSD of the Delivering Party and CSD of the Receiving Party — plus Currency, Settlement Amount and Credit/Debit for DVP/DWP; **additional** fields include the Opt-out ISO transaction condition indicator and the CUM/EX Indicator (and Currency, Settlement Amount and Credit/Debit for FOP); **optional** fields include Common Trade Reference, the client of the delivering and of the receiving CSD participant, and the securities accounts of the delivering and receiving parties. [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2, PDF pages 267–271, Diagrams 55–57 and footnote 194; reviewed 13 September 2026. Two limitations travel with this list: it is a **functional matrix only, with no production XML/XSD validation or local interface certification**, and the diagram headers read **DVP/DWP** while the surrounding paragraph mentions DVP/PFOD — these labels must not be silently normalised into a certified schema mapping. Changing any such field means a cancel-and-reinstruct, not an amendment.

**Unresolved requirement — the cancellation half of that route.** The UDFS section "Instruction Cancellation" is referenced from the excerpts but is **not in this bundle**, so the conditions for cancelling an instruction that has already matched — in particular whether both counterparties must instruct the cancellation, and the effect on the pending part of a partially settled instruction — are **not in reviewed evidence**. Do not assume the cancellation is unilateral. The reviewed matching excerpt establishes only that T2S automatically cancels Settlement Instructions that **remain unmatched** after a certain period of time. [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3, PDF page 271; reviewed 13 September 2026.

---

## 2. The partially settled instruction

**Documented requirement — Priority only.** "Additionally, for partially settled instructions, T2S Actors are only allowed to amend the 'Priority' of the unsettled part of the partially settled Settlement Instruction or Settlement Restriction." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3, PDF page 279; reviewed 14 September 2026. Table 59 confirms it: for a Partially Settled Instruction, Partial Settlement Indicator = NO, Linkages Block = NO, Priority = YES [[t2s-amendment]] Table 59, PDF page 280. And the third denial condition makes the consequence explicit: an Amendment Instruction against a partially settled instruction referring to any process indicator other than "Priority" is **denied** [[t2s-amendment]] §1.6.1.4.2, PDF page 278.

**Reasoned inference on a textual tension in the source, so you can read it correctly.** The overview sentence on PDF 278 says T2S Actors "are not able to amend other instruction types than Settlement Instructions or Settlement Restrictions, including the pending part of a partially settled Settlement Instruction or Settlement Restriction (i.e. Realignment instructions cannot be amended by T2S Actors)". Read in isolation that sentence sounds like a total bar on the pending part; read with §1.6.1.4.3, Table 59 and the third denial condition — all three of which expressly permit "Priority" on the unsettled part — the operative rule is the narrow one: Priority yes, everything else no. I state this as my reading of the excerpt, not as a separate documented rule, and a production specification should have it confirmed against the full §1.6.1.4 text.

**Practical consequence — Reasoned inference.** The Partial Settlement Indicator and threshold type must therefore be right **before** the instruction partially settles; once a partial settlement has occurred you can no longer switch partial settlement on or off, change the threshold type, or change linkages for the remaining quantity. Only re-prioritising the unsettled part remains. Derived from §1.6.1.4.3 and Table 59 in [[t2s-amendment]].

### When partial settlement happens at all (so you know what you are amending into)

**Documented requirement.** A Settlement Instruction is partially settled where there are insufficient securities to settle the full quantity, provided that the partial settlement window is currently running, the instructions are eligible to settle partially, and the partial settlement threshold criteria are fulfilled. Footnote 224: partial settlement is triggered **only in case of lack of securities** (lack of securities alone, or lack of securities and cash) — **not in case of lack of cash only**. [[t2s-partial-settlement]] T2S UDFS R2026.JUN, §1.6.1.9.3, PDF page 343 with footnote 224; reviewed 14 September 2026.

**Documented requirement — eligibility.** A matched pair is eligible when the instructions are related to Free Of Payment, Delivery Versus Payment or Delivery With Payment; the partial settlement indicator is not set to "No" in any of the Settlement Instructions; and they are **not linked** to any other Settlement Instruction or Settlement Restriction by the T2S parties by a link type "Before", "After", "With" or by a pool reference. Footnote 227 includes instructions on Party Hold that have been partially released. [[t2s-partial-settlement]] §1.6.1.9.3, PDF page 343; reviewed 14 September 2026.

**Documented requirement — thresholds.** Partial settlement is conditioned by thresholds determined in T2S when the settlement occurs, on the basis of the instruction type (FOP, DVP or DWP), the instruction threshold type, the underlying ISIN and the currency of the cash amount. Thresholds are either in "quantity" or in "cash value". Per Table 68: for FOP the applicable threshold type is quantity (minimum settlement unit is used only for the first partial settlement, together with the settlement unit multiple); for DVP/DWP with threshold type set to "Quantity" on both matched instructions the resulting type is quantity; for DVP/DWP not set to "Quantity" on both, the resulting type is cash value, for unit-quoted and for nominal-quoted ISINs alike. Footnote 228: cash-value thresholds are not considered for FOP regardless of the partial settlement threshold type defined in the instruction, including FOP instructions related to a foreign-currency transaction. [[t2s-partial-settlement]] §1.6.1.9.3 with Table 68 and footnote 228, PDF pages 344–345; reviewed 14 September 2026. **LIMITATION carried with this claim: the cash-value thresholds are configured per currency by the T2S Operator and the actual values are not in this excerpt** — I do not state any threshold value.

**Documented requirement — order of attempts.** Settlement Instructions are submitted to a full settlement attempt before a partial settlement attempt; if the instruction does not settle it goes to the Optimising application process, and only if optimisation finds no full-settlement solution does T2S try partial settlement, provided the conditions are met. Footnote 229: Partially Released Settlement Instructions are only submitted to partial settlement attempts for the released quantity. [[t2s-partial-settlement]] §1.6.1.9.3, PDF page 345 with footnote 229; reviewed 14 September 2026.

**Documented requirement — partial release, a different lever from amendment.** A Settlement Instruction on Party Hold may be **partially released** to allow partial settlement of a specified quantity, and must meet all the ordinary partial settlement conditions. During the real-time period, partial settlement of a Partially Released Settlement Instruction can occur outside a partial settlement window for the **total** partially released quantity, and during a window for the total or part of it, until the relevant cut-off time — partial release is valid only for the current business day, at which point the partial release is cancelled and the underlying Settlement Instruction is set back on Party Hold for the full unsettled quantity. For partial release to be considered during sequence C2SX of night-time settlement, the partial release must occur as of the start of day. [[t2s-partial-settlement]] §1.6.1.9.3, PDF pages 343–344 with footnotes 225–227; reviewed 14 September 2026.

**Unresolved requirement — the partial settlement window schedule.** Footnote 226 of the same section refers the schedule of the partial settlement window to the UDFS "Settlement Day" section, which is **not in this bundle**. The window times and the relevant cut-off time referred to above are therefore **not in reviewed evidence** and I state none. Nominal T2S times would in any case be baseline values, not a participant deadline, and a specific business date would need its own dated overlay.

---

## 3. Why "Settled" is an absolute bar

**Documented requirement.** The posting application process checks whether settlement can be achieved considering eligibility and available resources, and "when the check is satisfactory, the posting application process updates the cash balance, securities position and limit headroom, **resulting in the irrevocability of the settlement**". [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1, PDF pages 303–304; reviewed 13 September 2026. **Reasoned inference:** this is the substance behind the first denial condition — there is nothing left to amend on the settled quantity, only on a pending part, and only its Priority. Matching is not that moment: matching is agreement on the settlement terms between deliverer and receiver [[t2s-matching]] §1.6.1.2.1, PDF page 267; reviewed 13 September 2026, whereas posting is the transfer.

---

## 4. Summary table

| Question | Answer | Label |
|---|---|---|
| Amendable after matching | Partial Settlement Indicator + threshold type; Priority; Linkages Block | Documented requirement [[t2s-amendment]] §1.6.1.4.3, PDF 279 |
| Amendable on a Settlement Restriction | Priority; Linkages Block | Documented requirement [[t2s-amendment]] Table 59, PDF 280 |
| Amendable once partially settled | Priority of the unsettled part only | Documented requirement [[t2s-amendment]] §1.6.1.4.3 and Table 59, PDF 279–280 |
| Number of indicators per Amendment Instruction | One; a second needs a new Amendment Instruction | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 279 |
| Any other field | Cancel the referenced instruction and instruct it again | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 279 |
| Both legs at once | Only for instructions that entered T2S already matched, using the T2S Actor Reference; marked X for instructions matched in T2S | Documented requirement [[t2s-amendment]] Table 58, PDF 278–279 |
| Amending a Realignment instruction | Not possible for T2S Actors | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 278 |
| Conditions to cancel a matched instruction | Not in reviewed evidence (UDFS "Instruction Cancellation" not retrieved) | Unresolved requirement |
| Partial settlement window times and cut-off | Not in reviewed evidence (UDFS "Settlement Day" not retrieved) | Unresolved requirement |
| Threshold values | Not in reviewed evidence; configured per currency by the T2S Operator | Unresolved requirement |
| Local interface message, field and version to carry the amendment | Not in reviewed evidence | Unresolved requirement |

No claim above is a validated, certified or production-ready mapping; all of it is the T2S-native functional layer for R2026.JUN.

---

## Open items

1. **UDFS "Instruction Cancellation" section** — needed to state the conditions for cancelling a matched instruction (including whether both parties must instruct it) and the treatment of the pending part of a partially settled instruction. Route: retrieve the cancellation topic from the library; the underlying document is the public T2S UDFS R2026.JUN on the ECB's T2S professional-use documents pages.
2. **UDFS "Settlement Day" section** — needed for the partial settlement window schedule and the relevant cut-off referred to in footnote 226, and for anything time-related. Any dated answer would additionally need a reviewed overlay for the specific business date and currency.
3. **Partial settlement threshold values** — configured per T2S settlement currency by the T2S Operator in Static Data (and per ISIN for the quantity threshold by the actor administering that ISIN). Route: T2S Static Data for the currency and ISIN concerned; not derivable from this excerpt.
4. **Your local CSD interface specification** — this answer is T2S-native. The message, version and field by which your CSD accepts an Amendment Instruction, the references it expects, and any local entitlement are not in reviewed evidence; route is your CSD's client documentation service (for example the client platform of Euronext Securities Milan, Copenhagen or Porto) and, for T2S-native usage rules, an account-based MyStandards access, which the library does not admit field by field.
5. **Business Validation rules** — the amendment acceptance path depends on the UDFS Business Validation section, which is referenced in the excerpt but not retrieved here.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.724444+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_instruction_amendment"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-amendment]] — Instruction amendment: permitted process indicators and denial conditions (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.4 with Tables 58–59; PDF 277–280 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.4 with Tables 58–59; PDF 277–280):
1.6.1.4 Instruction Amendment


13    1.6.1.4.1 Concepts

14   T2S Actors are able to send an Amendment Instruction to modify a process indicator of an instruction in the
15    system, depending on its instruction type and its settlement status. The T2S Party, the relevant CSD and the
16    authorized parties can amend instructions of a given T2S Actor.





                                                                                            Page 277 of 2017



[PDF page 278]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                          DIAGRAM 66 - INSTRUCTION AMENDMENT APPLICATION PROCESS





 2

 3    1.6.1.4.2 Overview

 4   T2S accepts and processes an Amendment Instruction sent by a T2S Actor when it successfully passes the
 5    Business Validation process (see section Business Validation [ 218]), unless any of the following conditions
 6     is fulfilled:

 7         l  The Settlement Status of the Referenced Settlement Instruction or Settlement Restriction is “Settled” or
 8        “Cancelled”;

 9         l  The Referenced Settlement Instruction is identified as CoSD and the Amendment Instruction does not
10       aim to remove a linkage having the CSD as the Instructing Party (See section Conditional Settlement
11        [ 452]);

12         l  The referenced Settlement Instruction or Settlement Restriction is partially settled and the Amendment
13        Instruction refers to a process indicator other than “Priority”.

14     If the referenced instruction fulfils any of these conditions, the Amendment Instruction is denied. T2S Actors
15    are not able to amend other instruction types than Settlement Instructions or Settlement Restrictions, includ-
16    ing the pending part of a partially settled Settlement Instruction or Settlement Restriction (i.e. Realignment
17    instructions cannot be amended by T2S Actors).


                                                                                            Page 278 of 2017



[PDF page 279]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   An Amendment Instruction can be used to amend a process indicator of both legs at the same time or only
 2   one leg of a Settlement Instruction that entered T2S as already matched depending if the reference used in
 3    the Amendment Instruction refers to the information of one leg or both legs of the Settlement Instruction as
 4   shown in the table below (see section Instruction Types [ 86]).

 5                                 TABLE 58 - REFERENCES FOR AMENDMENT INSTRUCTION
 6

                                      ALREADY MATCHED SETTLEMENT      SETTLEMENT INSTRUCTIONS
                                              INSTRUCTION                 MATCHED IN T2S

      Amendment Instruction of one leg of             T2S Reference                  T2S Actor Reference
       the Settlement Instruction                                                                                         Or

                                                                               T2S Reference

      Amendment Instruction of both legs of         T2S Actor Reference                      X
       the Settlement Instruction

 7    For Amendment Instructions referring to both legs of the Settlement Instruction (i.e. if the T2S Actor In-
 8    struction Reference refers to a Settlement Instruction sent as already matched to T2S), T2S splits the infor-
 9    mation of the Amendment instruction into two separate maintenance instructions, one per each leg of the
10    referenced Settlement Instruction. As the inbound message related to the already matched maintenance
11    instruction is split internally, two different Amendment Instructions are created in T2S.

12   T2S Actors are only allowed to modify one process indicator per Amendment Instruction. If the T2S Actor
13   wants to modify a second process indicator, a new Amendment Instruction is required. If the T2S Actor
14   wants to modify other fields of the instruction, it has to cancel the referenced instruction and instruct it
15    again.


16    1.6.1.4.3 Amendment process

17   T2S Actors can only amend the following process indicators of a Settlement Instruction:

18         l  Partial Settlement Indicator and threshold type;

19         l  Priority;

20         l  Linkages Block (See Section Linked Instructions [ 442]).

21   T2S Actors can only amend the following process indicators of a Settlement Restriction:

22         l  Priority;

23         l  Linkages Block (See Section Linked Instructions [ 442]).

24    Additionally, for partially settled instructions, T2S Actors are only allowed to amend the “Priority” of the un-
25    settled part of the partially settled Settlement Instruction or Settlement Restriction.





                                                                                            Page 279 of 2017



[PDF page 280]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                               TABLE 59 - PROCESS INDICATORS ALLOWED FOR AMENDMENT
 2

                                  “PARTIAL SETTLEMENT       “LINKAGES BLOCK”            “PRIORITY”
                                     INDICATOR”

       Settlement Instruction              YES                  YES                  YES

       Settlement Restriction            NO                  YES                  YES

         Partially Settled Instruction         NO               NO                  YES

 3   T2S informs the T2S Actor on the result of the amendment process through a Status Advice message, as
 4    described in sections Send Amendment Instruction of a Settlement Instruction or of a Settlement Restriction
 5   on Securities Position and Send Amendment Instruction of a Settlement Restriction on Cash Balance. Inter-
 6    ested parties can also be informed depending on their message subscription preferences (see Section Status
 7   Management [ 653] and Section Message subscription [ 135]).

 8    In case of already matched Amendment Instructions, the status reporting derived from the lifecycle of each
 9   Amendment Instruction created in T2S is handled separately. Nevertheless, the T2S Actor may subscribe to
10    the notifications of one of the two legs of the already matched Amendment Instruction only.


11    1.6.1.4.4 Parameters Synthesis

12   No specific configuration from T2S Actor is needed in T2S Reference Data.


13

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_settlement"}
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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
