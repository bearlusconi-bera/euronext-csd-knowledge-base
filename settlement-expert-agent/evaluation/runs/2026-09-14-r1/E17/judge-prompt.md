You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Does the T2S matching tolerance of EUR 2 / EUR 25 apply to settlement in Oslo's VPO NOK system?

# Case category: wrong-market (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "VPO NOK is a Norwegian netting system outside T2S; T2S tolerance values do not govern it.",
  "The EU RTS Article 6 tolerance applies to CSDs under CSDR; Norway/EEA incorporation is not established in the library.",
  "Oslo rules carry the edition-approval reservation and Norwegian text governs."
]
Fail conditions (must NOT appear):
[
  "Apply EUR 2/25 to VPO NOK as a fact.",
  "Assert Norwegian legal applicability of the RTS."
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
# Does the T2S matching tolerance (EUR 2 / EUR 25) apply to settlement in Oslo's VPO NOK system?

## Direct answer

**No — and the premise of the question should be rejected rather than answered conditionally.** The EUR 2 / EUR 25 bands are a **T2S** matching parameter, configured **per currency**, and the reviewed evidence explicitly warns against generalising the EUR bands to other currencies. **VPO NOK is a Norwegian netting system outside T2S**, settling in Norwegian kroner on VPO LOM accounts at Norges Bank through a preliminary calculation / clearing / settlement-cycle mechanism; T2S lifecycle rules do not apply to it. So the T2S tolerance does not reach VPO NOK settlement.

**Whether VPO NOK operates a matching tolerance of its own, and at what amount, is an Unresolved requirement.** The reviewed VPO NOK Rules sections mention Matching but state no tolerance figure, and the VPO NOK User Documentation — which the Rules themselves point to for formats, timings, assumptions and options — is not in the library. One retrieval in this bundle returned **STATUS: blocked** for exactly that material (**GAP ID G11**). Do not read "the T2S tolerance does not apply" as "no tolerance applies"; the second statement is not established either way.

**Retrieval statuses:** six retrievals returned `evidence_only`; retrieval 7 (Oslo, settlement, participant, current, `oslo_operational_calendar`, as of 2026-09-14) returned **blocked** — "Current VPO NOK operating calendar, cycle times and MyVPS specifications are not in reviewed evidence", **GAP ID G11**.

**Explanation of the term** (background, not a documented requirement): a *matching tolerance* is a permitted difference between the cash amounts stated by the two sides of a trade, within which a settlement system still treats the two instructions as matching rather than rejecting them as discrepant.

---

## 1. What the tolerance actually is, and the scope condition attached to it

**Documented requirement.** `[[t2s-matching]]` — T2S User Detailed Functional Specifications **R2026.JUN** (UDFS), §1.6.1.2, **PDF 267–271**, Diagrams 55–57 and footnote 194; version R2026.JUN; English, no authoritative language independently established; **platform release R2026.JUN**; section reviewed **13 September 2026**; approval: source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS: **functional matrix only — no production XML/XSD validation or local interface certification**; retain the diagram DVP/DWP labels, since the paragraph separately mentions DVP/PFOD. The reviewed transcription records `production_schema_validated: false`.

- If all matching fields on both instructions match **except** the Settlement Amount, T2S checks whether the difference between the two Settlement Amounts complies with the tolerance amount configured in T2S.
- **"This tolerance amount set up in T2S has two different bands per currency, depending on the cash countervalue. ECSDA proposal for Euro is the following"** — and the table that follows is headed **Tolerance amount for matching for euro**: tolerance EUR 2 where the cash countervalue is at or below EUR 100,000, and EUR 25 above EUR 100,000.
- The recorded condition on this row is explicit: *currency-specific configuration applies; do not generalise the EUR bands to other currencies.*
- The tolerance is a T2S-operator parameter: created and updated by the T2S Operator, marked mandatory, possible values "to be defined", with the EUR bands as the standard or default value (§1.6.1.2.4, Parameter Synthesis).
- Where instructions with different Settlement Amounts match, the amount submitted for settlement is the one indicated by the deliverer of the securities; among several candidates T2S takes the smallest amount difference, then the closest entry time.

**Two things follow directly from the wording, before any Oslo evidence is considered:** the figures are stated as the euro configuration, not as a system-wide constant; and they operate inside the **T2S** matching process, which compares the mandatory matching fields (including Currency and Settlement Amount for DVP/DWP) listed in Diagram 55.

**Section applicability.** `[[t2s-matching]]` carries entities **T2S, Milan, Copenhagen and Porto**. Oslo is not among the entities of this section, and no reviewed section in this bundle extends it to Oslo.

`[[t2s-posting]]` — UDFS R2026.JUN §1.6.1.8.1 and the first overview paragraph, PDF 303–304, reviewed 13 September 2026, platform release R2026.JUN — likewise describes T2S posting (eligibility and resource checks before the transfer) and carries the same four entities; it is a T2S process description and says nothing about VPO NOK.

---

## 2. What VPO NOK is, in reviewed evidence

All Oslo sections below come from the same source and carry the same qualifications: **ES-OSL VPO NOK Rules, edition of 2 September 2024**; body language English but this is a **translation from the original Norwegian, and the Norwegian text prevails in the event of any discrepancy**; applicability basis **reference description** (a description of a published document, not an establishment of its operative effect); approval: source identity checked, no independent whole-edition supervisory approval certification.

**Documented requirement — the edition approval reservation.** `[[oslo-edition-r2]]` (VPO NOK Rules cover, 2 September 2024; reviewed **14 September 2026**) and `[[oslo-edition]]` (same cover page; reviewed 13 September 2026) record the cover statement: **"ENTERED INTO FORCE ON 02.09.2024. SUBJECT TO APPROVAL BY FINANSTILSYNET."** LIMITATIONS: **system approval is not edition-specific approval, and independent edition approval remains unresolved (gap G07)**; the hub link and hash were unchanged on 14 September 2026, so the 14 September section is a re-verification of the same page rather than a new edition. This reservation travels with every Oslo statement in this answer.

**Documented requirement — VPO NOK is outside T2S.** `[[oslo-finality-moments]]` — VPO NOK Rules §§23.1–23.3, **PDF 36–37**, reviewed **14 September 2026** — carries the LIMITATION: **"VPO NOK is a Norwegian netting system outside T2S; T2S lifecycle rules do not apply."** Its own text describes irrevocability on Matching (the moment of irrevocability, CSDR Article 39(2)), bilateral cancellation requiring the counterparty's confirmation before the start of the settlement cycle in which the instruction was to be processed, a unilateral CCP cancellation on close-out under the Act on Financial Collateral of 26 March 2004 No. 17, hold/release provisions, and the moment of entry into the system (Matched, or Released where a hold was applied). English translation; Norwegian text governs; edition approval reservation applies.

**Documented requirement — the settlement mechanism.** `[[oslo-submission-settlement]]` — VPO NOK Rules §§21–22.1, **PDF 33–35**, reviewed **14 September 2026**: settlement involves the final transfer of ownership rights in the VPS Register together with **the final recording of accounting entries in Norwegian kroner in the VPO NOK accounts at Norges Bank that were involved in the Clearing**; cash settlement is effected on the participant's or its liquidity bank's **VPO LOM account with Norges Bank**; instructions are assigned to settlement groups FH, CH or FO by the participant's authorisation; accounting vouchers are sent to settlement banks after final transfer. LIMITATIONS: English translation, Norwegian text governs, edition approval reservation applies; and **the User Documentation referenced for formats and times is not in the library (gap G11)**.

**Documented requirement — cycle mechanics.** `[[oslo-priority-clearing]]` — VPO NOK Rules §§23.4–23.8, **PDF 37–39**, reviewed **14 September 2026**: before every clearing cycle VPS performs a **Preliminary Calculation** of participants' positions based on received settlement instructions, the financial instruments available on the specified VPS accounts and, for the first cycle of a settlement day, participants' **Cash Limits**; priority rules apply on insufficient securities or insufficient liquidity (deferred instructions first, then the instructions enabling the largest total settled value; penalty payments under Section 25 take priority until fully settled); linked buy/sell instructions may deviate from the priority rules; participants must make instruments and cash available; settlement banks and liquidity banks must fund their VPO LOM accounts to at least their overall net position; Norges Bank notifies VPS of Available Liquidity and clearing is then carried out. LIMITATIONS: English translation, Norwegian text governs, edition approval reservation applies; and **cycle times are in the User Documentation, not admitted**.

**Documented requirement — cash provision.** `[[oslo-liquidity]]` — VPO NOK Rules §§9–10, **PDF 17–18**, reviewed **13 September 2026**: the Liquidity Bank's declaration commits the bank to make available each day on its **VPO LOM account with Norges Bank** the cash needed for the named participant's instructions included in the Clearing, up to Base Liquidity plus any Additional Liquidity, cancellable on at least four banking days' notice; a Substitute Liquidity Bank's declaration confers an entitlement on the liquidity bank's insolvency but **no duty** to provide cash. LIMITATION: the unresolved edition approval must accompany any description, and the Section 20 conditions have not been reviewed for a funding implementation.

---

## 3. Why the T2S tolerance does not carry over

**Reasoned inference**, derived from the two documented sets above and from nothing else:

1. The tolerance is defined **inside the T2S matching process** and configured **per currency**, with the stated bands presented as the euro configuration (`[[t2s-matching]]`).
2. VPO NOK is a **Norwegian netting system outside T2S** to which **T2S lifecycle rules do not apply** (`[[oslo-finality-moments]]`), and its cash leg is recorded in **Norwegian kroner** at Norges Bank (`[[oslo-submission-settlement]]`).
3. Therefore a euro-denominated T2S matching parameter has no application to VPO NOK settlement. Applying it would require the very cross-system generalisation the evidence warns against.

**Unresolved requirement — what is *not* established:**

- Whether VPO NOK applies **any** amount tolerance in its own matching, and if so at what NOK values. The reviewed VPO NOK Rules sections use the defined term "Matched" and describe when an instruction is irrevocable and entered into the system, but **state no tolerance amount**. The Rules repeatedly defer to the **User Documentation** for assumptions, timings and options, and that document is **not in reviewed evidence (gap G11)**.
- Whether a T2S tolerance band is configured for NOK at all. No such band is in reviewed evidence; only the euro configuration is.
- Whether Euronext Securities Oslo operates any other settlement service, T2S-connected or otherwise, alongside VPO NOK. **Nothing in this bundle addresses that**, so this answer is confined to VPO NOK and must not be read as a statement about Euronext Securities Oslo as a whole.
- The **operative legal status** of the VPO NOK Rules edition relied on here: the cover reserves approval by Finanstilsynet, the sections are admitted on a reference-description basis, and the governing text is the Norwegian original (gap G07).

No validation, certification or production readiness is claimed for anything above.

---

## Open items

1. **VPO NOK User Documentation (and MyVPS specifications)** — the source that would establish whether VPO NOK applies a matching tolerance, its NOK amounts, the preliminary-calculation assumptions, the cycle timings and the linked-trade options. Blocked in this bundle: **GAP ID G11** ("Current VPO NOK operating calendar, cycle times and MyVPS specifications are not in reviewed evidence"), and named as missing in the LIMITATION lines of `[[oslo-submission-settlement]]` and `[[oslo-priority-clearing]]`. Official route: Euronext Securities Oslo's client documentation service for VPO NOK participants.
2. **The Norwegian original of the VPO NOK Rules and its approval status** — the English text used here is a translation and the Norwegian prevails; the cover reserves approval by Finanstilsynet and edition-specific approval remains unresolved (**gap G07**, `[[oslo-edition]]`, `[[oslo-edition-r2]]`). Official route: the Euronext Securities Oslo rules publication in Norwegian, together with the supervisory approval record.
3. **T2S currency configuration for NOK, if any** — would be needed before any statement that a T2S tolerance band exists or does not exist for Norwegian kroner. Official route: the T2S UDFS and the T2S reference-data configuration for settlement currencies, reviewed for the relevant release; the present `[[t2s-matching]]` evidence is R2026.JUN and euro-only.
4. **Confirmation of the scope of Euronext Securities Oslo's settlement services** — whether any service other than VPO NOK is operated and whether it settles in T2S; not addressed by any section in this bundle.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:57:45.356049+00:00). Review dates available: 2026-09-13, 2026-09-14.

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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "oslo_instruction_submission_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[oslo-edition-r2]] — VPO NOK Rules cover: edition approval reservation (14 September re-verification) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules cover, 2 September 2024 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: Same page as the 13 September section oslo-edition; hub link and hash unchanged on 14 September 2026.
LIMITATION: System approval is not edition-specific approval. Independent edition approval remains unresolved (gap G07).
EXCERPT (VPO NOK Rules cover, 2 September 2024):
[PDF page 1]

   EURONEXT SECURITIES OSLO





        VPO NOK RULES





THIS DOCUMENT IS A TRANSLATION FROM THE ORIGINAL NORWEGIAN VERSION. IN THE EVENT OF ANY

DISCREPANCIES, THE ORIGINAL NORWEGIAN DOCUMENT WILL PREVAIL.





ENTERED  INTO  FORCE ON  02.09.2024.  SUBJECT  TO  APPROVAL  BY

FINANSTILSYNET.





© 2024, Verdipapirsentralen ASA                                                                          1 of 58

--- SECTION [[oslo-submission-settlement]] — Submitting settlement instructions, settlement groups and settlement in VPO NOK (§§21–22.1) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules §§21–22.1; PDF 33–35 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: English translation; Norwegian text governs and the edition's approval reservation applies.
LIMITATION: User Documentation referenced for formats and times is not in the library (gap G11).
EXCERPT (VPO NOK Rules §§21–22.1; PDF 33–35):
21 SUBMITTING SETTLEMENT INSTRUCTIONS TO VPO NOK

A Participant must submit its Settlement Instructions as soon as possible once the trade has been
entered into to ensure early Matching and to facilitate timely Settlement.

When submitting a Settlement Instruction, the Participant shall register all the information required
pursuant to legislation, regulations, these VPO NOK Rules, and the User Documentation as in force
at any time. The Participant shall retain information about the Settlement Instruction for at least 48
hours following submission to VPO NOK to enable the Participant to resubmit a Settlement
Instruction in the event of operational difficulties.



21.1  DIFFERENT SETTLEMENT GROUPS AND ACCOUNTS WITH PARTICULAR
    SETTLEMENT FUNCTIONALITY

Settlement Instructions that are submitted using a VPS registration number associated with
authorisation as an Investment Firm shall be assigned to settlement group FH.

Settlement Instructions submitted using a VPS registration number associated with authorisation as
a Central Counterparty shall be assigned to settlement group CH.

Except where otherwise provided for by the last paragraph of this section, Settlement Instructions
submitted using a VPS registration number associated with authorisation as a Settlement Agent
shall be assigned to settlement group FO.

Securities accounts belonging to settlement group FH or CH are defined as Accounts with
Particular Settlement Functionality in Section 4 and are treated as such in accordance with the
provisions of Sections 23.5, 23.8 and 23.9.

Accounts with Particular Settlement Functionality may be assigned to customers of Participants that
are Settlement agents provided that the Customer is a Central Counterparty or Investment Firm as
defined in Section 5.1 c), d) and e) in these Rules. Settlement instructions submitted for such
accounts shall be assigned to settlement group CH or FH.




21.2  OPTIONAL SETTLEMENT FUNCTIONALITY

A Participant authorised as a Settlement Agent may offer to label as an Optional Settlement
Account the ordinary securities account in the register of a customer that has an Account with
Particular Settlement Functionality pursuant to Section 21.1, fifth paragraph. VPS will label such
accounts in this way at the instruction of the Settlement Agent. A customer must request such
labelling in writing before the Settlement Agent can submit such an instruction to VPS.



© 2024, Verdipapirsentralen ASA                                                                         33 of 58



[PDF page 34]

Settlement Instructions submitted for an account labelled as an Optional Settlement Account are
treated in the same way as Settlement Instructions that are submitted for an Account with particular
settlement functionality in relation to the provisions of Sections 23.5, 23.8 and 23.9.





© 2024, Verdipapirsentralen ASA                                                                         34 of 58



[PDF page 35]

22 SETTLEMENT

Settlement involves the final transfer of ownership rights to financial instruments (securities
settlement) in the VPS Register as well as the final recording of accounting entries in Norwegian
kroner in the VPO NOK accounts at Norges Bank that were involved in the Clearing (cash
settlement).

Cash settlement (settlement of liquidity) for Participants that are Settlement Banks, is effected on
the Participant’s VPO LOM account with Norges Bank. Settlements for Participants that use
Liquidity Banks are effected on that bank’s VPO LOM account with Norges Bank.



22.1 ACCOUNTING VOUCHERS

When VPS carries out a final transfer of ownership rights to financial instruments in VPS, it sends
accounting vouchers to the Settlement Banks so that transactions can be posted on the bank
accounts that the Participants have specified to VPS for this purpose.





© 2024, Verdipapirsentralen ASA                                                                         35 of 58

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "oslo_finality_moments"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[oslo-edition-r2]] — VPO NOK Rules cover: edition approval reservation (14 September re-verification) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules cover, 2 September 2024 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: Same page as the 13 September section oslo-edition; hub link and hash unchanged on 14 September 2026.
LIMITATION: System approval is not edition-specific approval. Independent edition approval remains unresolved (gap G07).
EXCERPT (VPO NOK Rules cover, 2 September 2024):
[PDF page 1]

   EURONEXT SECURITIES OSLO





        VPO NOK RULES





THIS DOCUMENT IS A TRANSLATION FROM THE ORIGINAL NORWEGIAN VERSION. IN THE EVENT OF ANY

DISCREPANCIES, THE ORIGINAL NORWEGIAN DOCUMENT WILL PREVAIL.





ENTERED  INTO  FORCE ON  02.09.2024.  SUBJECT  TO  APPROVAL  BY

FINANSTILSYNET.





© 2024, Verdipapirsentralen ASA                                                                          1 of 58

--- SECTION [[oslo-finality-moments]] — VPO NOK: irrevocability on matching, CCP close-out exception, hold provisions and the moment of entry (§§23.1–23.3) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules §§23.1–23.3; PDF 36–37 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: English translation; Norwegian text governs and the edition's approval reservation applies.
LIMITATION: VPO NOK is a Norwegian netting system outside T2S; T2S lifecycle rules do not apply.
EXCERPT (VPO NOK Rules §§23.1–23.3; PDF 36–37):
23 PROCESSING OF SETTLEMENT INSTRUCTIONS


23.1 WHEN SETTLEMENT INSTRUCTIONS CAN NO LONGER REVOKED

Once a Settlement Instruction has been Matched, it cannot be revoked unless both the Participants
involved in the trade in question send instructions to cancel their respective Settlement Instructions
(the moment of irrevocability, cf. Article 39, item 2, of the CSDR). This takes place by means of
one Participant submitting a cancellation instruction that is then confirmed by the other Participant
involved. The other Participant’s confirmation of the cancellation must be received prior to the Start
of the Settlement cycle in which the Settlement Instruction in question was to be processed.

A Settlement Instruction for a transfer between a Participant and a Participant approved as a Central
Counterparty, and between two participants approved as Central Counterparties may be cancelled
unilaterally by the Central Counterparty, even after the transaction has been submitted. The first
sentence only applies if this is connected with the Central Counterparty carrying out a close-out of
the Participant in question on the basis of an agreement on the pledging of financial collateral
between the Participant and the Central Counterparty, cf. the Act on Financial Collateral of 26
March 2004 No. 17. Close-out has the effect that the Participant's duties to deliver financial
instruments and cash (liquidity) pursuant to Settlement Instructions that have been submitted are
cancelled with immediate effect, and are replaced by the calculation and netting of the monetary
amounts denominated in Norwegian kroner that the Participant is due to pay to/receive from the
Central Counterparty.

Settlement Instructions that do not require Matching, i.e. Settlement Instructions for transactions
with parties other than Participants in VPO NOK, cannot be revoked after the Start of Settlement in
which the Settlement Instruction in question is to be processed.




23.2 SPECIAL PREVISIONS ON TRANSACTIONS THAT ARE OR HAVE BEEN PUT
   ON HOLD

A Settlement Instruction can be put on Hold by the participant who submitted the Settlement
Instruction. This can be done also after the Settlement Instruction has been Matched.

A Settlement Instruction that has been put on Hold will not be settled until the Participant that
submitted it marks it as Released.

The rules in Section 23.1 regarding when a Settlement Instruction can no longer be revoked also
apply to Settlement Instructions that have been put on Hold by one or both Participants involved.





© 2024, Verdipapirsentralen ASA                                                                         36 of 58



[PDF page 37]

23.3  THE POINT IN TIME WHEN A SETTLEMENT INSTRUCTION IS DEEMED TO
    HAVE BEEN ENTERED INTO VPO NOK (THE MOMENT OF ENTRY INTO THE
     SYSTEM, CF. THE CSDR, ARTICLE 39, ITEM 2).

A Settlement Instruction has the status of being entered into the system once it has been Matched.
This does not, however, apply to Settlement Instructions that have been put on Hold by one or both
of the Participants involved either before or after Matching. A Settlement Instruction that is put on
Hold by one or both Participants is first considered to be entered into the system once both
Participants have marked it as Released.

Settlement Instructions that do not require Matching, i.e. Settlement Instructions for transactions
with parties other than Participants in VPO NOK, are considered to have been entered into the
system from the Start of Settlement in which the Settlement Instruction in question is to be
processed, provided it has not been put on Hold.

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "oslo_preliminary_calculation_priority"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[oslo-edition-r2]] — VPO NOK Rules cover: edition approval reservation (14 September re-verification) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules cover, 2 September 2024 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: Same page as the 13 September section oslo-edition; hub link and hash unchanged on 14 September 2026.
LIMITATION: System approval is not edition-specific approval. Independent edition approval remains unresolved (gap G07).
EXCERPT (VPO NOK Rules cover, 2 September 2024):
[PDF page 1]

   EURONEXT SECURITIES OSLO





        VPO NOK RULES





THIS DOCUMENT IS A TRANSLATION FROM THE ORIGINAL NORWEGIAN VERSION. IN THE EVENT OF ANY

DISCREPANCIES, THE ORIGINAL NORWEGIAN DOCUMENT WILL PREVAIL.





ENTERED  INTO  FORCE ON  02.09.2024.  SUBJECT  TO  APPROVAL  BY

FINANSTILSYNET.





© 2024, Verdipapirsentralen ASA                                                                          1 of 58

--- SECTION [[oslo-priority-clearing]] — VPO NOK: preliminary calculation, priority rules, linked instructions, liquidity duties and clearing (§§23.4–23.8) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules §§23.4–23.8; PDF 37–39 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: English translation; Norwegian text governs and the edition's approval reservation applies.
LIMITATION: Cycle times are in the User Documentation, not admitted.
EXCERPT (VPO NOK Rules §§23.4–23.8; PDF 37–39):
23.4  PRELIMINARY CALCULATION

Prior to every Clearing cycle, VPS shall carry out a Preliminary Calculation of the Participants’
positions in VPO NOK.

The Preliminary Calculation for the first Settlement cycle on a settlement day is based on the
received Settlement Instructions, the financial instruments that are available on the VPS accounts
that the Participants have specified for the Settlement cycle in question, and the Participants’ Cash
Limits (liquidity limits) where applicable. The Preliminary Calculation for subsequent Settlement
cycles on a settlement day shall be based on the same factors, with the exception of any Cash
Limits. The assumptions applied in the Preliminary Calculation, and the timing thereof, are detailed
in the User Documentation.

The Cash Limit for a Participant that uses a Liquidity Bank, is the sum of Base Liquidity and
Additional Liquidity, less any amount used in a previous Settlement cycle on the same day. No
Cash Limit is applied in the Preliminary Calculation for other Participants.

The Preliminary Calculation also shows the overall net position per Settlement Bank. For the
purpose of this calculation, each bank’s own Settlement Instructions (if the bank is a Participant
itself) and those of Participants for which the bank is the Liquidity Bank are netted.





© 2024, Verdipapirsentralen ASA                                                                         37 of 58



[PDF page 38]

23.5 PRIORITY RULES USED FOR THE PRELIMINARY CALCULATION


23.5.1 Priority rules in the event of insufficient financial instruments

If it is not possible to settle all the Settlement Instructions included in the Preliminary Calculation
due to an insufficient number of financial instruments to cover the Participants’ Settlement
Instructions, the following sequencing shall apply: In respect of Transfers from accounts in the
settlement groups FH and CH and from accounts labelled as Optional Settlement Accounts:
     -   Priority will be given to Settlement Instructions that were deferred on earlier Settlement
       Days, including Settlement Instructions that were deferred as a result of a Partial Delivery,
         cf. Section 23.9.
     -   Thereafter, priority will be given to Settlement Instructions that will enable the largest
       possible total value to be settled in the Settlement in question.

In respect of transfers from other accounts, priority will be given in the order the Settlement
Instructions were submitted by the Participants.



23.5.2 Priority rules in the event of insufficient Liquidity (cash)

If there is insufficient cash (liquidity) within any Cash limits that apply to Participants, the
following sequencing shall apply:
     -   Priority will be given to Settlement Instructions that were deferred on earlier Settlement
       Days, including Settlement Instructions that were deferred as a result of a Partial Delivery,
         cf. Section 23.9.
     -   Thereafter, priority will be given to the Settlement Instructions that will enable the
       largest possible total value to be settled in the Settlement in question.

Settlement Instruction for payment of penalty pursuant to Section 25 will be given priority until the
penalties have been fully settled.



23.5.3 General provisions on priority rules

It is specified in Section 21.1 above and in the User Documentation which accounts belong to
settlement group FH and which accounts belong to settlement group CH. Optional Settlement
Accounts are regulated in Section 21.2. When applying the priority rules, VPS shall apply the
current optimisation model.



23.5.4 Linked Settlement Instructions

VPS may deviate from the priority rules set out in the first and second paragraphs when processing
linked Settlement Instructions. This applies when a Participant links buy and sell instructions on the

© 2024, Verdipapirsentralen ASA                                                                         38 of 58



[PDF page 39]

same account, with the effect that the sale is conditional on the related purchase taking place. The
financial instruments purchased in a linked trade will be used to fill the sale instruction in the same
Settlement, even if a different outcome would have resulted from applying the ordinary priority
rules. The User Documentation details the current options for linked trades.


23.6 THE PARTICIPANT’S DUTY TO MAKE FINANCIAL INSTRUMENTS AND
LIQUIDITY (CASH) AVAILABLE

The Participant has a duty to make available for each Settlement the number of financial
instruments and the cash (liquidity) necessary to carry out all the Settlement Instructions that are
submitted to VPO NOK under the Participant’s Settlement Agreement and included in the
Settlement in question.


23.7  TRANSFER OF CASH (LIQUIDITY) TO VPO LOM ACCOUNTS

Participants that are Settlement Banks, and those that serve as Liquidity Banks that provide cash
(liquidity) for Participants in VPO NOK, are required to transfer to their VPO LOM accounts, at the
time stated in the User Documentation, an amount that is at least equal to the bank’s overall net
position in the Preliminary Calculation, cf. Section 23.4, final paragraph.


23.8 CLEARING

At the time specified in the User Documentation, Norges Bank notifies VPS of the Available
Liquidity on each Settlement Bank’s VPO LOM account (account balance).

At the time specified in the User Documentation, Clearing is carried out based on Settlement
Instructions, the Available Liquidity, and the financial instruments available on the VPS accounts
that Participants have specified for use in the Settlement in question.

If a Settlement Bank fails to transfer sufficient cash (liquidity) to the bank’s VPO LOM account to
cover its overall net position according to the Preliminary Calculation, cf. Section 23.4, final
paragraph, the Available Liquidity will not be sufficient to cover both the bank’s own Settlement
Instructions and those submitted by Participants for which the bank is the Liquidity Bank. In such
events, Clearing will be calculated in the following way:

   A) If there is only one Participant linked to the Settlement Bank’s VPO LOM account, the
      amount of Available Liquidity will be entered as a new Cash Limit (liquidity limit).
   B) If there is more than one Participant linked to the Settlement Bank’s VPO LOM account, the
       Available Liquidity is allocated so that:
              - Priority will be given to Settlement Instructions that were deferred on earlier
           Settlement Days, including Settlement Instructions that were deferred as a result of a
            Partial Delivery, cf. Section 23.9.



© 2024, Verdipapirsentralen ASA                                                                         39 of 58

=== RETRIEVAL 5: context {"as_of": "2026-09-13", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "liquidity_duties"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[oslo-edition]] — VPO edition approval qualification (reviewed 2026-09-13; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules cover, 2 September 2024 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: System approval is not edition-specific approval. Independent edition approval remains unresolved.
EXCERPT (VPO NOK Rules cover, 2 September 2024):
[PDF page 1]

   EURONEXT SECURITIES OSLO





        VPO NOK RULES





THIS DOCUMENT IS A TRANSLATION FROM THE ORIGINAL NORWEGIAN VERSION. IN THE EVENT OF ANY

DISCREPANCIES, THE ORIGINAL NORWEGIAN DOCUMENT WILL PREVAIL.





ENTERED  INTO  FORCE ON  02.09.2024.  SUBJECT  TO  APPROVAL  BY

FINANSTILSYNET.





© 2024, Verdipapirsentralen ASA                                                                          1 of 58

--- SECTION [[oslo-liquidity]] — Primary and substitute liquidity-bank declarations as published (reviewed 2026-09-13; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules §§9–10; PDF 17–18 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: Unresolved edition approval must accompany any description. Section 20 conditions are not reviewed for a funding implementation.
EXCERPT (VPO NOK Rules §§9–10; PDF 17–18):
[PDF page 17]

9  DECLARATIONS FROM LIQUIDITY BANKS


The Liquidity Bank’s Liquidity Declaration shall state that:

A named participant in VPO NOK is entitled to have its Settlement Instructions in VPO NOK
settled via the Liquidity Bank’s VPO LOM account with Norges Bank, and in addition the bank
will make available on this account each day the cash (liquidity) necessary to carry out all the
Participant's Settlement Instructions that are included in the Clearing, subject to the limit of the
value of Base Liquidity with the addition of any Additional Liquidity.

The bank’s Liquidity Declaration can only be cancelled by giving at least four banking days’ notice.





© 2024, Verdipapirsentralen ASA                                                                         17 of 58



[PDF page 18]

10 DECLARATIONS FROM SUBSTITUTE LIQUIDITY BANKS


The Substitute Liquidity Bank’s Declaration to a Participant shall state that:

In the event the Participant’s Liquidity Bank enters into insolvency proceedings, the Participant is
entitled to have its Settlement Instructions in VPO settled via its Substitute Liquidity Bank’s VPO
LOM account with Norges Bank. This account will in such case be considered as the Participant’s
Settlement Account for cash (liquidity) settlement.

The Declaration of a Substitute Liquidity Bank does not imply a duty to make cash (liquidity)
available on its account in order to settle the Participant’s Settlement Instructions.

However, if the Substitute Liquidity Bank chooses to make cash (liquidity) available to the
Participant, it may do so. In such case, this shall be done in accordance with the rules set out in
Section 20.





© 2024, Verdipapirsentralen ASA                                                                         18 of 58

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "approval_status"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[oslo-edition-r2]] — VPO NOK Rules cover: edition approval reservation (14 September re-verification) (reviewed 2026-09-14; modes ['reference']; entities ['Oslo']; basis reference_description)
CITATION: ES-OSL VPS NOK Rules.pdf | VPO NOK Rules cover, 2 September 2024 | version VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification. | body language en | authoritative language no | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf
LIMITATION: Same page as the 13 September section oslo-edition; hub link and hash unchanged on 14 September 2026.
LIMITATION: System approval is not edition-specific approval. Independent edition approval remains unresolved (gap G07).
EXCERPT (VPO NOK Rules cover, 2 September 2024):
[PDF page 1]

   EURONEXT SECURITIES OSLO





        VPO NOK RULES





THIS DOCUMENT IS A TRANSLATION FROM THE ORIGINAL NORWEGIAN VERSION. IN THE EVENT OF ANY

DISCREPANCIES, THE ORIGINAL NORWEGIAN DOCUMENT WILL PREVAIL.





ENTERED  INTO  FORCE ON  02.09.2024.  SUBJECT  TO  APPROVAL  BY

FINANSTILSYNET.





© 2024, Verdipapirsentralen ASA                                                                          1 of 58

=== RETRIEVAL 7: context {"as_of": "2026-09-14", "entity": "Oslo", "service": "settlement", "role": "participant", "mode": "current", "question_type": "oslo_operational_calendar"}
STATUS: blocked — Current VPO NOK operating calendar, cycle times and MyVPS specifications are not in reviewed evidence.
GAP IDS: ['G11']

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
