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
# T2S automatic cancellation of pending instructions: the two recycling periods

## Direct answer

**Documented requirement.** The reviewed T2S functional description prints two recycling periods — the number of working days a pending instruction may stay in T2S before the system cancels it: **20 working days for pending unmatched instructions** and **60 working days for pending matched instructions and settlement restrictions**. Both numbers are printed as the *current* values of a parameter **configured by the T2S Operator**, not as fixed rules of the specification [[t2s-recycling]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.7 with footnotes 199–200; PDF 296–299, version R2026.JUN; reviewed 2026-09-14; body language en, no authoritative language independently established, translation status "not independently established", approval qualification "Source identity checked; no independent whole-edition supervisory approval certification" (source reviewed 2026-09-13).

Term used here: *recycling* is the T2S process that carries a still-pending instruction forward into the next settlement day; the carry-forward triggers revalidation of that instruction at Start of Day, and when the configured period is exhausted the instruction is cancelled by the system rather than by a party [[t2s-recycling]] UDFS R2026.JUN, §1.6.1.7 (§1.6.1.7.1–1.6.1.7.2); PDF 296–299; reviewed 2026-09-14; same language and approval qualifications as above.

## Supported detail

**Documented requirement — the periods and what they cover** [[t2s-recycling]] UDFS R2026.JUN, §1.6.1.7 with footnotes 199–200; PDF 296–299; reviewed 2026-09-14; body language en, authoritative language not established, approval qualification as above:

| # | Population | Period printed | How the count runs |
|---|---|---|---|
| 1 | Unmatched settlement instructions (and cancellation instructions that need to be matched) | Footnote 199: "Current recycling period for unmatched instructions of 20 working days" — a period of working days configured by the T2S Operator | For unmatched **settlement** instructions: starts from the Intended Settlement Date (ISD) or the date of the last status change of the instruction, whichever is the later. **Any status value change restarts the count** — the UDFS example is a change of Party Hold from "Yes" to "No" |
| 2 | Unmatched cancellation instructions needing matching | Same unmatched period, configured by the T2S Operator | Starts from reception in T2S and runs until matching occurs |
| 3 | Pending **matched** instructions and settlement restrictions | Footnote 200: "Current recycling period for matched instructions of 60 working days" — a period of working days configured by the T2S Operator | Recycled until settlement or cancellation occurs |

**Documented requirement — when the cut falls and how it is calculated.** T2S recycles pending instructions at each end of settlement day, and cancels at the **End of Day (EoD) process** all instructions that have reached their recycling period. The period is reached when the difference between "D1" (the latest date between the ISD and the business day of the last status change of the instruction) and "D2" (the current business date) equals the number of business days defined for the applicable recycling period. Until EoD the instruction is still processed as normal throughout the whole business day, so reaching the limit does not stop same-day settlement attempts [[t2s-recycling]] UDFS R2026.JUN, §1.6.1.7; PDF 296–299 (calculation text at PDF 299); reviewed 2026-09-14; qualifications as above.

**Documented requirement — notification.** T2S sends **no** daily message about the result of the recycling process. Only when an instruction exceeds its recycling period does T2S cancel it automatically and send the T2S Actor a message with the corresponding reason code(s); interested parties may also be informed according to their message subscription preferences [[t2s-recycling]] UDFS R2026.JUN, §1.6.1.7; PDF 296–299; reviewed 2026-09-14; qualifications as above. The specific reason code values are not in the reviewed excerpt and are not reproduced here.

**Documented requirement — the exception that suspends automatic cancellation.** In an external-CSD scenario, instructions are **not** automatically cancelled but remain pending and are recycled for an indefinite period, until one of the conditions ceases to be fulfilled or the T2S Actors cancel them, where **all** of the following hold: (a) any of the relevant CSDs is external to T2S; (b) the external CSD is the issuer of the security; and (c) the external CSD is configured as not compliant with the T2S automatic cancellation of instruction [[t2s-recycling]] UDFS R2026.JUN, §1.6.1.7; PDF 298; reviewed 2026-09-14; qualifications as above. LIMITATION carried from the bundle: the external-CSD exception is stated, but individual CSD configurations are not certified — whether a given external CSD is configured as non-compliant is not in reviewed evidence.

**Documented requirement — automatic cancellation sits inside the cancellation process.** The cancellation section confirms that, additionally to actor-initiated cancellation, "T2S cancels instructions automatically (e.g. when an Unmatched Settlement Instruction has exceeded its recycling period in T2S)", and its "Cancellation by the system" list names exceeding the recycling period as one trigger, alongside: a realignment chain that cannot be built; instructions failing revalidation (triggered at Start of Day and by reference-data changes affecting the instruction); and certain partially settled instructions whose realignment chain becomes invalid at Start-of-Day revalidation [[t2s-cancellation]] UDFS R2026.JUN, §1.6.1.5 with Table 60 and footnote 195; PDF 280–284 (system cancellation at PDF 283–284); reviewed 2026-09-14; body language en, authoritative language not established, approval qualification "Source identity checked; no independent whole-edition supervisory approval certification" (source reviewed 2026-09-13). So the 60-working-day figure is a ceiling on *time*, not the only route to system cancellation: a matched instruction can be cancelled by the system earlier for the other reasons listed.

**Documented requirement — why the matched case cannot simply be undone by one party.** For a matched settlement instruction T2S requires **bilateral cancellation**: cancellation is only possible if both counterparties send their cancellation instructions for each leg separately, or if an authorised T2S Party sends a cancellation instruction carrying the information of both legs [[t2s-cancellation]] UDFS R2026.JUN, §1.6.1.5.3; PDF 282; reviewed 2026-09-14; qualifications as above. An unmatched instruction, by contrast, is cancelled or denied immediately after validation of the cancellation instruction [[t2s-cancellation]] UDFS R2026.JUN, §1.6.1.5.3; PDF 282; reviewed 2026-09-14; qualifications as above. Matching itself is only agreement on settlement terms between deliverer and receiver; it is not the transfer [[t2s-matching]] UDFS R2026.JUN, §1.6.1.2; PDF 267–271, Diagrams 55–57 and footnote 194; reviewed 2026-09-13; body language en, authoritative language not established, approval qualification as above — the transfer is the posting process, which updates cash balance, securities position and limit headroom and results in irrevocability of the settlement [[t2s-posting]] UDFS R2026.JUN, §1.6.1.8.1 and first overview paragraph; PDF 303–304; reviewed 2026-09-13; qualifications as above. That is why a "matched but unsettled" instruction keeps being recycled, and why the 60-working-day clock exists at all.

## Reasoned inference

- **Reasoned inference (from footnotes 199–200 read with the body text that the period is "configured by the T2S Operator").** 20 and 60 working days are the values the R2026.JUN UDFS states as current, so they describe the operator's configuration as documented in that edition and reviewed on 2026-09-14. They are not self-evidently the values in force on any later business date: an operator parameter change would not change the UDFS footnote. The authoritative statement of the live parameter is the T2S Operator's configuration, not this excerpt.
- **Reasoned inference (from the D1/D2 calculation and the restart rule).** Because any status value change resets D1 for an unmatched instruction, 20 working days is a maximum measured from the latest of ISD and last status change — not 20 working days from instruction entry. Repeated hold/release or other status changes extend the practical life of an unmatched instruction.
- **Reasoned inference (from the placement of the calculation text).** The D1/D2 formula is written for "a pending instruction" and "the applicable recycling period", so on its face it governs both populations; the excerpt's explicit start-date wording, however, is given only for unmatched settlement instructions and for unmatched cancellation instructions, while the matched sentence says only "until its settlement or cancellation occurs".

## Unresolved requirements (not in reviewed evidence)

- **Which calendar defines a "working day"/"business day" for the count.** The excerpt uses both terms and cross-references the Settlement Day section (page reference [155] in the UDFS); that section is not in this bundle, so the day-counting calendar and the settlement-day/civil-day boundary are not established here. No clock time is quoted, because the bundle prints none for recycling.
- **The reason code(s)** carried on the automatic-cancellation message, and the message identifier and version used to report it: not in reviewed evidence (the recycling excerpt refers to the "Send Settlement Instruction" and Status Management / Message subscription sections, which are not in the bundle).
- **Local CSD effects.** Whether and how Euronext Securities Milan, Copenhagen, Porto, Athens or Oslo restate, shorten or supplement these T2S periods in their own rulebooks or client documentation is not in reviewed evidence; the sections here are T2S-native. Bundle LIMITATIONS carried: "T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline" (both [[t2s-recycling]] and [[t2s-cancellation]]); local legal effects of cancellation (for example Milan Article 70) are separate sections at their own review date; and for [[t2s-matching]] "Functional matrix only; no production XML/XSD validation or local interface certification".

## Retrieval statuses

All three retrievals in this bundle returned **evidence_only** (contexts: T2S / settlement / participant / current, question types `matching_concept` as of 2026-09-13, `t2s_cancellation_process` as of 2026-09-14, `t2s_recycling_periods` as of 2026-09-14). No retrieval was `blocked`, `needs_context` or `needs_refresh`, so nothing is withheld on status grounds. Review dates available in the bundle are 2026-09-13 and 2026-09-14; the two sections that carry the answer ([[t2s-recycling]], [[t2s-cancellation]]) are reviewed 2026-09-14 and their underlying source was reviewed 2026-09-13. These are review dates, not a statement that the configuration is unchanged today (this answer is composed on a later date than the review).

## Open items

1. **T2S Operator's live recycling-period configuration** (to confirm that 20 and 60 working days are still the values in force after 2026-09-14): official route — the T2S professional-use documentation and operational communications published by the ECB/Eurosystem for the deployed release, via the T2S section of the ECB website used as this section's source.
2. **UDFS "Settlement Day" section** (page reference [155]) to establish the working-day calendar and the settlement-day boundary used by the D1/D2 count: official route — the same T2S UDFS R2026.JUN edition, section Settlement Day; not retrieved in this bundle.
3. **Cancellation reason code(s), status-advice message identity and version** for the automatic cancellation: official route — T2S UDFS sections Status Management and Message subscription, and the T2S message usage guidelines (MyStandards) for the deployed release; not retrieved in this bundle.
4. **External-CSD configuration** ("not compliant with the T2S automatic cancellation of instruction") for any specific issuer CSD and ISIN: not certified in reviewed evidence (bundle LIMITATION); official route — the relevant CSD's own documentation service and the T2S reference-data configuration held by the relevant CSD.
5. **Local restatements per CSD** (Milan, Copenhagen, Porto, Athens, Oslo) of pending-instruction lifetime and cancellation effects: official route — each CSD's public rulebook/documentation hub and its client platform (for example MT-X for Milan) — client-only material is outside this bundle. No gap id is named by this bundle for any of these items.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.567809+00:00). Review dates available: 2026-09-13, 2026-09-14.

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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_recycling_periods"}
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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
