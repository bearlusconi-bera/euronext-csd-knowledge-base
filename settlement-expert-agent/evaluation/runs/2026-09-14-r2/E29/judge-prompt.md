You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Which data must an Athens (ATHEXCSD) participant include in a DSS settlement instruction, and how far in the past or future may the intended settlement date be?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Mandatory data i-xiv (counterparties, instruction type, settlement method, operation reason, cash value, trade date, ISD, ISIN, quantity, currency, counterparty CSD, place of settlement, securities account, hold/release).",
  "ISD not more than 60 calendar days before entry and not more than 365 after.",
  "Informational translation; Greek prevails; Resolution 5 codified 24 November 2025."
]
Fail conditions (must NOT appear):
[
  "Invent Annex II reasons or tolerance values."
]
Expected sections (if any): ['athens-instruction-content']
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
# Athens (ATHEXCSD) — mandatory and optional data of a DSS settlement instruction, and the intended settlement date window

## Direct answer

A settlement instruction entered in the DSS must carry, **at the time of entry**, the fourteen mandatory data items listed in Resolution 5 Part 4 §4.3(1)(A) — counterparty data, instruction type (delivery/receipt), settlement method (DVP/FOP/PFOD or another method), operation reason, cash value, transaction date, intended settlement date, ISIN, quantity, currency, the counterparty's CSD identifier in link cases, place of settlement, securities settlement account, and the Hold/Release condition — and may additionally carry seven optional items. The intended settlement date (ISD) **must not precede the date of entry by more than 60 calendar days and must not exceed the date of entry by more than 365 calendar days**, while no specific time limit applies between the ISD and the transaction date. **Documented requirement** — [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §§4.1–4.3(3) with footnotes 17–28; PDF 9–12; version "Resolution 5: effective 8 December 2025"; reviewed 2026-09-14; informational English translation with **Greek as the authoritative language** (the Greek text prevails); approval: source identity checked, no independent whole-edition supervisory approval certification; source reviewed 2026-09-13.

## Retrieval statuses and review dates

Two retrievals were made and **both returned `evidence_only`**, so nothing in this answer is suppressed by a `blocked`, `needs_context` or `needs_refresh` status:

| Retrieval | Context | Status | Section | Review date |
|---|---|---|---|---|
| 1 | Athens / settlement / participant / mode `reference` / `athens_instruction_content_matching`, as_of 2026-09-14 | `evidence_only` | [[athens-instruction-content]] | reviewed 2026-09-14 (underlying source reviewed 2026-09-13) |
| 2 | Athens / settlement / participant / mode `reference` / `athens_settlement_methods`, as_of 2026-09-14 | `evidence_only` | [[athens-settlement-methods]] | reviewed 2026-09-14 (underlying source reviewed 2026-09-13) |

The `evidence_only` reason line states that only the named propositions and their conditions are supported. Both sections carry the applicability basis `reference_description`: they describe the text of Resolution 5 as published in the reviewed edition, and the operative Rulebook provisions they implement (Part 5, Section V, articles 5.2–5.5) are **not** in the bundle. The evidence review date is 14 September 2026; that date is a fact about the review, not a statement that the text is unchanged on any later date.

## 1. Mandatory data at entry — Part 4 §4.3(1)(A)

All rows below are **Documented requirement** on [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §4.3(1)(A) items i–xiv; PDF 10–11; version "Resolution 5: effective 8 December 2025"; reviewed 2026-09-14; informational English translation, Greek authoritative; source identity checked, no independent whole-edition supervisory approval certification.

| # | Mandatory datum | What the excerpt says |
|---|---|---|
| i | Settlement counterparties | Data that enable identification of the Participants participating in the settlement of the transaction |
| ii | Instruction type | Whether the instruction relates to delivery or receipt of the Security |
| iii | Specific settlement method | "such as, in particular" delivery versus payment (DVP), free of payment (FOP), payment free of delivery (PFOD) "or other method" in accordance with Commission Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394 |
| iv | Operation reason | Data denoting the type of transaction for settlement; the available operation reasons in the DSS are determined by the Resolution (Annex II) |
| v | Cash value | The monetary amount for settlement, **expressed in euro**; may be zero when the transaction settles free of payment |
| vi | Transaction date | The day on which the transaction was concluded |
| vii | Intended settlement date | The day on which the transaction will be settled |
| viii | ISIN | The unique identification code of the Security to be settled |
| ix | Quantity | Number of Securities or, alternatively, the nominal value of the Security where appropriate (as for bonds) |
| x | Currency | (stated as a mandatory datum; no further specification in the excerpt) |
| xi | Counterparty's CSD identifier | Identifier of the CSD of the Participant's counterparty, in the case of Direct and Indirect Links of ATHEXCSD, including the cases in Article 30(5) of Regulation (EU) 909/2014 |
| xii | Place of settlement | The system through which settlement is to take place |
| xiii | Securities settlement account | Data identifying the Securities Account — including Transitory Accounts and Provisional Settlement Accounts — through which delivery or receipt takes place |
| xiv | "Hold" or "Release" condition | Conditions as defined in article 5.4 of the Rulebook |

Terminology, offered as **explanation** and not as a documented requirement: *DVP* is settlement of securities against a simultaneous cash leg; *FOP* is a securities movement with no cash leg; *PFOD* is a cash movement with no securities movement; a *hold/release* condition is a flag that keeps an otherwise valid instruction from settling until the instructing party releases it.

Scope qualifications that travel with the whole table: item v fixes the cash value in **euro**; item xi is conditional on ATHEXCSD Direct or Indirect Links; item xiv refers out to Rulebook article 5.4, which is **not in the bundle**.

## 2. Optional data — Part 4 §4.3(1)(B)

**Documented requirement** — an instruction may, in addition to the mandatory data, include one or more of: (a) external matching code (agreed by the counterparty Participants to distinguish a pair of instructions from others with similar content); (b) place of trade; (c) Participant's reference code; (d) unit price; (e) Participant End Client; (f) Counterparty End Client; (g) comments. The excerpt closes the list with "Other data or conditions pertaining to the settlement instructions which are determined by ATHEXCSD", i.e. the Resolution itself contemplates further ATHEXCSD-determined content that is **not enumerated in the reviewed excerpt**. Items (e) and (f) were added by Board decision 374/26.05.2025, effective the day after ATHEXCSD announced successful completion of the relevant technical transition "and in any case until 29.9.2025" (footnote 25). [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §4.3(1)(B) with footnote 25; PDF 11–12; reviewed 2026-09-14; informational English translation, Greek authoritative; source identity checked, no independent whole-edition supervisory approval certification.

## 3. Additional content conditioned on the operation reason — Part 4 §4.2

**Documented requirement** — where the operation reason is one of the following, the instruction must carry extra content or satisfy an extra acceptance condition [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §4.2 with footnotes 17–19; PDF 9–10; reviewed 2026-09-14; informational English translation, Greek authoritative; source identity checked, no independent whole-edition supervisory approval certification:

1. **NCBO ("No Change Beneficiary Owner")** — the beneficiary (full name or BIC) must be stated; for acceptance, one of the two matching instructions must relate to Securities kept in a **Clients Securities Account**.
2. **"Transfer between Securities Accounts of the same Share"** — both instructions must relate to Securities Accounts of the same Share; this does not apply where the instructions come from a System Operator, in which case the transfer is carried out only through the instruction of the System Operator or delegated Member/Participant settling the relevant arrears.
3. **"Transfer of Securities between Client Securities Accounts of different Shares of the same Client for consolidation in the DSS"** — the identity of that same Client must be established on the responsibility of the Participants involved, per ATHEXCSD procedures.
4. **"Transfer of Securities between Securities Accounts of the same beneficiary as Market Maker Participant at the commencement or cessation of Market Making"** — the identity of that same beneficiary as Market Maker must be established on the responsibility of the Participants involved.
5. **"Transfer of Securities between Fund Shares of the same Fund"** — the transfer must be between Shares of the same Fund per Rulebook Section III §4.9.2, and the instruction must contain the legal name or BIC of the Fund.

By stating the operation reason the Participant indicates the transaction type in compliance with Article 5(4) of Regulation (EU) 2018/1229, with the exception of the Market Claim reason "f" of the Annex, which ATHEXCSD uses exclusively when it creates settlement instructions under the Market Claims procedure (first paragraph as amended by Board decision 383/24.11.2025, effective 8 December 2025). **Unresolved requirement:** the Annex II catalogue of operation reasons is expressly outside the reviewed excerpt (bundle LIMITATION), so no operation-reason code list can be quoted from this evidence.

## 4. How far in the past or future the intended settlement date may sit — Part 4 §4.3(2)

**Documented requirement** — for an instruction to be accepted it must meet these specific terms, per Rulebook Section V article 5.2(1) [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §4.3(2)(a)–(c) with footnotes 26–27; PDF 12; version "Resolution 5: effective 8 December 2025"; reviewed 2026-09-14; informational English translation, Greek authoritative; source identity checked, no independent whole-edition supervisory approval certification:

| Boundary | Rule as written |
|---|---|
| Backdating | The ISD "must not precede the date of its entry by more than **60 calendar days**" |
| Forward dating | The ISD "must not exceed the date of its entry by more than **365 calendar days**" |
| ISD vs transaction date | "There is no specific time limit between the intended settlement date of the settlement instruction and the transaction date" |

Two points to keep attached to those figures. First, both windows are measured in **calendar days against the date of entry** of the instruction — not against the trade date and not in business days; the excerpt says nothing about how a boundary day falling on a non-business day is handled. Second, paragraph 2 was amended by Board decision 374/26.05.2025 with effect from 30 June 2025, and the edition reviewed here is Resolution 5 codified to 24 November 2025, effective 8 December 2025 (bundle LIMITATION). **Reasoned inference** (from the wording "In order for a settlement instruction to be accepted"): an instruction breaching either window fails acceptance rather than being accepted and then rejected later; the excerpt does not describe the rejection mechanics, error reporting or any repair path, so that consequence is **not established** in the reviewed evidence.

## 5. Matching and tolerance — Part 4 §4.3(3)

**Documented requirement** — matching requires that the mandatory data of sub-cases **i) through xii)** of item A, plus optional data **a)** (external matching code) and **b)** (place of trade), coincide in content, provided the element has been entered. For optional data **e)** and **f)** (Participant End Client and Counterparty End Client), matching is achieved provided both counterparties entered them; matching can still be achieved if only one counterparty or neither entered them. Exceptionally, where the operation reason is declared as **NCBO**, **"Transfer of Securities between Fund Shares of the same Fund"** or **"Transfer of Securities from an Issuer Share to the Securities Account of the same beneficiary"**, the end client (full name or BIC) or the name or BIC of the Fund must be declared for the instruction to be accepted, and those end-client details must be the same in order to match. On tolerance levels (Rulebook article 5.5(2)), matching is achieved even if the respective **cash value** fields do not match, provided the difference does not exceed the defined tolerance level. [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §4.3(3); PDF 12; reviewed 2026-09-14; informational English translation, Greek authoritative; source identity checked, no independent whole-edition supervisory approval certification.

**Reasoned inference** (derived from the mandatory list i–xiv read against the matching list i–xii): items **xiii) Securities Settlement Account** and **xiv) Hold/Release condition** are mandatory content but are *not* in the enumerated set of matching fields, so they are instruction-level data rather than fields that must agree between the two sides. The excerpt does not state this consequence expressly.

**Unresolved requirement:** the **numeric tolerance values** are outside the reviewed excerpt (bundle LIMITATION: "Annex II operation reasons and the tolerance values are outside the excerpt"), so no cash-value tolerance amount may be quoted from this evidence. Note also that §4.3's title covers cancellation/transformation, informational balances and market-claim-generated instructions, but the reviewed excerpt runs only to §4.3(3), so those sub-paragraphs are not available here.

## 6. Settlement methods and the technical layer — Retrieval 2

**Documented requirement** — ATHEXCSD settles transactions on the basis of the settlement methods laid down in Rulebook Section V and in Commission Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394; for cash settlement it **blocks cash balances in the Cash Settlement Accounts**, and specifically where cash settlement is carried out in TARGET-GR with the participation of Settlement Banks, those balances are blocked through TARGET-GR in the respective Sub-accounts kept by Settlement Banks for Participants. Any procedural or technical detail — settlement methods, business hours and performance of settlement, the settlement algorithm's particular specifications, the number and duration of settlement cycles — is determined by ATHEXCSD's technical procedures and **announced to Participants through the DSS** or by other appropriate means. [[athens-settlement-methods]] ATHEXCSD Resolution 5, Part 2 §§2.1–2.2; PDF 4; version "Resolution 5: effective 8 December 2025"; reviewed 2026-09-14; informational English translation, Greek authoritative; approval: source identity checked, no independent whole-edition supervisory approval certification; source reviewed 2026-09-13.

**Unresolved requirement:** business hours, settlement cycles and algorithm specifics are announced through the DSS and are **not in the library (gap G12)** per the bundle LIMITATION, so no cut-off time, cycle count or intraday deadline for entering or amending an instruction can be given, and nothing here converts the 60/365-day calendar windows into an intraday entry deadline.

## 7. What this evidence does not establish

- **Field-level interface mapping — Unresolved requirement.** The bundle contains the Resolution's data *categories*, not a DSS message layout, field names, cardinalities, formats, code values or ISO 20022 mappings. No local Athens interface specification or DSS announcement is in the bundle, and a T2S message description would not substitute for one.
- **Rulebook text — Unresolved requirement.** Part 5, Section V articles 5.2 (mandatory data), 5.3 (optional data), 5.4 (hold/release), 5.5 (matching and tolerance) and Section III §4.9.2 are referred to by the Resolution but are not in reviewed evidence; the same applies to Annex II.
- **Tolerance amounts, operation-reason codes, DSS timetable — Unresolved requirement** (see sections 3, 5 and 6).
- **Language and approval qualification.** Everything above is taken from an informational **English translation**; the **Greek** text prevails, and the bundle records only that source identity was checked, with no independent whole-edition supervisory approval certification.
- No instruction-like content was found inside the retrieved excerpts; the footnote and amendment text was treated as data.

## Open items

1. **ATHEXCSD Resolution 5, Annex II** (operation reasons catalogue, including Market Claim reason "f") — needed to state any operation-reason code. Official route: the ATHEXCSD/Euronext Athens public rules and regulations hub that publishes the Resolution 5 PDF cited above.
2. **Numeric matching tolerance levels for cash value** — named as outside the excerpt by the bundle LIMITATION on [[athens-instruction-content]]. Official route: the full Resolution 5 text and Rulebook article 5.5(2), via the same public hub.
3. **ATHEXCSD Rulebook, Part 5 Section V articles 5.2–5.5 and Section III §4.9.2** — needed to confirm the operative acceptance, hold/release and matching provisions that Resolution 5 implements. Official route: the ATHEXCSD Rulebook on the public hub.
4. **DSS technical announcements** — business hours, settlement cycles, algorithm specifics and any entry/amendment cut-offs; recorded as **gap G12** in the bundle LIMITATION on [[athens-settlement-methods]]. Official route: ATHEXCSD announcements to Participants through the DSS (client channel).
5. **Greek authoritative text of Resolution 5** — required before any wording above is relied on operationally, because the reviewed body language is an informational English translation while Greek prevails.
6. **A later review date** — the reviewed evidence carries review date 2026-09-14 (available review dates in this bundle: 2026-09-13 and 2026-09-14) for an edition codified to 24 November 2025 and effective 8 December 2025. Any reliance on a business date after that review requires a fresh review; no later amendment is evidenced here either way.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.739587+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "athens_instruction_content_matching"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[athens-instruction-content]] — Participant settlement instructions: operation reasons, mandatory and optional data, acceptance windows (60/365 days), matching and tolerance (Part 4 §§4.1–4.3) (reviewed 2026-09-14; modes ['reference']; entities ['Athens']; basis reference_description)
CITATION: ATHEXCSD Resolution 5 | Resolution 5 Part 4 §§4.1–4.3(3) with footnotes 17–28; PDF 9–12 | version Resolution 5: effective 8 December 2025. | body language en | authoritative language el | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://athens.euronext.com/sites/default/files/2025-12/RESOLUTION_Nr5-ATHEXCSD_383_24.11.2025_FORCE%208.12.2025.DOC.pdf
LIMITATION: Informational English translation; the Greek text prevails. Resolution 5 codified to 24 November 2025 (effective 8 December 2025).
LIMITATION: Annex II operation reasons and the tolerance values are outside the excerpt.
EXCERPT (Resolution 5 Part 4 §§4.1–4.3(3) with footnotes 17–28; PDF 9–12):
PART 4. Settlement of transactions on the instructions of Participants

4.1 General provisions
For the settlement of transactions on the instructions of Participants, the terms of Part 5, Section V of the
Rulebook shall apply.


4.2 Operation Reason
The available Operation Reasons as mandatory data of settlement instructions in accordance with point iv,
par. 1, article 5.2, Part 5, Section V of the Rulebook are those set out in Annex II hereof, which is attached
hereto and forms an integral part hereof (hereinafter “Annex  II”). By stating the Operation Reason,
Participants indicate the type of transaction in their settlement instructions, in compliance with the terms
of paragraph 4, article 5, Regulation (EU) 2018/122917, with the exception of reason Market Claim «f- of
Appendix II, which is used by ATHEXCSD exclusively, when creating settlement instructions due to the
application of Market Claims procedures. 18

If the operation reason given is “No Change Beneficiary Owner” (NCBO) of Annex II of this Resolution, the
beneficiary (full name or BIC – Business Identification Code) must be stated in the relevant settlement
instructions. For such instructions to be accepted for settlement, one of the respective instructions must
relate to Securities kept in a Clients Securities Account.

If the operation reason is “Transfer between Securities Accounts of the same Share” of Annex II of this
Resolution, for such settlement instructions to be accepted, both instructions must relate to Securities
Accounts of the same Share. The previous sentence does not apply when the settlement instructions come
from a System Operator. In this case, the transfer of Securities is carried out only through the settlement
instruction of the System Operator or delegated Member or Participant that implements the transfer to
settle the relevant arrears.

If the operation reason is “Transfer of Securities between Client Securities Accounts of different Shares of
the same Client for the purpose of consolidating those Shares in the DSS” of Annex II of this Resolution, for





17 The first paragraph of article 4.2 was replaced as above by virtue of decision 325/31.01.2022 of the Board of
Directors with effect as of 01.02.2022.
18 The paragraph 1 of article 4.2 was amended as above by virtue of decision 383/24.11.2025 of the Board of
Directors of ATHEXCSD with effect as of 8.12.2025.


Resolution 5 (24/11/2025)                 9                        www.athexgroup.gr



[PDF page 10]

such settlement instructions to be accepted, the identity of that same Client must be established on the
responsibility of the Participants involved in accordance with the procedures of ATHEXCSD.

If the operation reason is “Transfer of Securities between Securities Accounts of the same beneficiary as
Market Maker Participant at the commencement or cessation of Market Making”, for such settlement
instructions to be accepted, the identity of that same beneficiary as Market Maker must be established on
the responsibility of the Participants involved in accordance with the procedures of ATHEXCSD.

If the operation reason is “Transfer of Securities between Fund Shares of the same Fund”, the aforesaid
transfer of Securities must be carried out between Shares of the same Fund in compliance with the terms
of par. 4.9.2, Section III of the Rulebook, and the relevant settlement instructions must contain the legal
name or Business Identifier Code (BIC) of the Fund19.

4.3 Requirements for accepting a settlement instruction - Date of settlement of the
   settlement instruction – Matching20 - Tolerance levels – Cancellation or
    Transformation21 of the settlement instruction – Informational balancesi22 -
   Creation of settlement instructions due to application of Market Claims
   procedure23
 1.  24Mandatory and optional matching fields of a settlement instruction
   Α.  In accordance with the terms of par. 1, article 5.2 of Section V of the Rulebook, in order for a
      settlement instruction that is entered in the DSS to be accepted for execution and settled through
      the DSS, it must at the time of its entry, to include the following mandatory data:

             i. Data on the Settlement Counterparties: These are data that enable identification of the
       Participants participating in the settlement of the transaction.

              ii. Instruction type: Data that determine whether the settlement instruction relates to delivery or
       receipt of the Security.

              iii. The specific settlement method, such as, in particular, delivery versus payment (DVP) or free of
     payment (FOP) or payment free of delivery (PFOD) or other method in accordance with Commission
      Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394.



19 The last paragraph of article 4.2 was repealed as above by virtue of decision 374/26.05.2025 of the Board of
Directors of ATHEXCSD with effect as of 30.06.2025.
20 The title of article 4.3 was amended as above by virtue of decision 374/26.05.2025 of the Board of Directors
with effect as of 30.06.2025.
21 The title of article 4.3 was amended as above by virtue of decision 367/21.10.2024 of the Board of Directors
with effect as of 02.12.2024.
22 The title of article 4.3 was amended as above by virtue of decision 378/29.09.2025 of the Board of Directors
with effect as of 30.09.2025.
23 The title of article 4.3 was amended as above by virtue of decision 383/24.11.2025 of the Board of Directors
with effect as of 8.12.2025.
24 A new paragraph 1 has been added to Article 4.3 and the article was worded as above by virtue of decision
374/26.05.2025 of the Board of Directors with effect as of 30.06.2025.



Resolution 5 (24/11/2025)                    10                        www.athexgroup.gr



[PDF page 11]

          iv. Operation reason: Data that denote the type of transaction for settlement. The available
      operation reasons in the DSS are determined by the current Decision.

        v. Cash value: The value that determines the monetary amount for settlement, which is expressed
        in euro. The cash value may be zero when the transaction is settled with the free of payment method.

          vi. Transaction date: Data that indicate the day on which the transaction was concluded.

           vii. Intended settlement date: Data that indicate the day on which the transaction will be settled.

           viii. ISIN: The unique identification code of the Security to be settled (ISIN: International Securities
       Identification Number).

          ix. Quantity: The quantity of Securities to be settled. Such quantity is expressed in number of
       Securities or, alternatively, by stating the nominal value of the Security as appropriate, as in the case
       of bonds.

        x. Currency

          xi. Identifier of the CSD of the Participant’s counterparty, in the case of Direct and Indirect Links of
     ATHEXCSD, including also the cases referred to in paragraph 5, article 30 of Regulation (EU)
      909/2014.

          xii. Place of Settlement: The system through which settlement is to take place.

           xiii. Securities Settlement Account: Data identifying the Securities Account, including Transitory
      Accounts and Provisional Settlement Accounts, through which the delivery or receipt of the
       Securities to be settled will take place.

        xiv. “Hold” or “Release” Condition: Conditions as defined in article 5.4 of the Rulebook.

   Β.  In accordance with the terms of article 5.3, a settlement instruction entered in the DSS for execution
      may, in addition to the mandatory data of instance a), par. 1 of article 5.2, include one or more of the
       following optional data:

       a) External matching code: The code entered, following agreement, by the counterparty
       Participants for the purpose of distinguishing a pair of settlement instructions from others with
        similar content.

      b) Place of trade: Data identifying where the transaction to be settled was concluded.

       c) Participant's reference code: Data entered by the Participant in order to facilitate communication
       within its systems.

      d) Unit price: The price at which the transaction to be settled was concluded.

      e) Participant End Client: These are the details identifying the entitled Client of the Participant.

        f) Counterparty End Client: These are the details identifying the entitled Client of the Counterparty
       Participant.25

25 Points (e) and (f) of B) of paragraph 1 of Article 4.3 "Participant's Entity Customer" and "Counterparty's Entity
Customer" respectively were added as above by the decision of the Board of Directors 374/26.05.2025 with


Resolution 5 (24/11/2025)                          11                        www.athexgroup.gr



[PDF page 12]

      g) Comments: Data that further specify the settlement instructions.

Other data or conditions pertaining to the settlement instructions which are determined by ATHEXCSD.


 2.  26Terms of accepting a settlement instruction
     In order for a settlement instruction to be accepted, it must fulfil the following specific terms,
    according to par.1, article 5.2 of Section V of the Rulebook:

a. The intended settlement date of the settlement instruction must not precede the date of its entry by
more than 60 calendar days.

b. The intended settlement date of the settlement instruction must not exceed the date of its entry by more
than 365 calendar days.

c. There is no specific time limit between the intended settlement date of the settlement instruction and
the transaction date.27



 3.  Matching – Tolerance levels28
In implementation of the provisions mentioned in case c), par. 1, article 5.5 of the Rulebook on matching of
settlement instructions, the mandatory data of sub-cases of i) through xii) of item A), par. 1, of the current
article, as well as the data of a) and b), par. 1 of the current article, must coincide in content, provided that
the element provided for in the respective case has been entered.
Specifically for data of cases e) and f) of item B of the current article, matching is achieved provided that
the data specified in those cases have been entered by both counterparties. Matching of settlement
instructions can still be achieved even if the above data have been entered only by one counterparty or by
neither of them. Exceptionally, in cases where the reason for the movement is declared as 'NCBO – No
Change Beneficiary Owner’, 'Transfer of Securities between Fund Shares of the same Fund' and 'Transfer of
Securities from an Issuer Share to the Securities Account of the same beneficiary’, as described in Annex II
of the current Resolution, in order for the instruction to be accepted, the end client (full name or BIC –
Business Identification Code) or the name or BIC of the Fund, must be declared in the relevant settlement
instructions. In addition, the above end client details must be the same, in order to be matched.


In implementation of paragraph 2, article 5.5 of the Rulebook on tolerance levels, the following shall apply:

       a) Matching of settlement instructions is achieved even if their respective ‘cash value’ fields do not
       match, provided that the cash value difference does not exceed the tolerance level as defined in


effect as of the day following the announcement of ATHEXCSD on the successful completion of the relevant
technical transition and in any case until 29.9.2025.
26 Paragraph 2 of article 4.3 was amended as above by virtue of decision 374/26.05.2025 of the Board of
Directors with effect as of 30.06.2025.
27 Points b) and c) of paragraph 1 of article 4.3 were amended as above by virtue of decision 374/26.05.2025 of
the Board of Directors with effect as of 30.06.2025
28 A new paragraph 3 was added to Article 4.3 and the article was worded as above by virtue of decision
374/26.05.2025 of the Board of Directors with effect as of 30.06.2025.



Resolution 5 (24/11/2025)                     12                        www.athexgroup.gr

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "athens_settlement_methods"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[athens-settlement-methods]] — Settlement methods, cash blocking and delegation of technical details to DSS announcements (Part 2) (reviewed 2026-09-14; modes ['reference']; entities ['Athens']; basis reference_description)
CITATION: ATHEXCSD Resolution 5 | Resolution 5 Part 2 §§2.1–2.2; PDF 4 | version Resolution 5: effective 8 December 2025. | body language en | authoritative language el | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://athens.euronext.com/sites/default/files/2025-12/RESOLUTION_Nr5-ATHEXCSD_383_24.11.2025_FORCE%208.12.2025.DOC.pdf
LIMITATION: Informational English translation; the Greek text prevails. Resolution 5 codified to 24 November 2025 (effective 8 December 2025).
LIMITATION: Business hours, cycles and algorithm specifics are announced through the DSS and are not in the library (gap G12).
EXCERPT (Resolution 5 Part 2 §§2.1–2.2; PDF 4):
PART 2. Settlement Methods

2.1 Settlement methods
ATHEXCSD settles transactions on the basis of the settlement methods laid down in Section V of the
Rulebook and the provisions of Commission Delegated Regulation (EU) 2017/392 and Commission
Implementing Regulation (EU) 2017/394.

For the purposes of cash settlement, ATHEXCSD blocks cash balances in the Cash Settlement Accounts.
Specifically in the case of cash settlement carried out in TARGET-GR with the participation of Settlement
Banks, the aforesaid balances are blocked through TARGET-GR in the respective Sub-accounts kept by
Settlement Banks for Participants.


2.2 Technical details
Any procedural or technical details relating to settlement operations, as set forth in the Rulebook and this
Resolution, for instance with respect to settlement methods, the business hours and performance of
settlement, the particular specifications of the settlement algorithm, or the number and duration of
settlement cycles, shall be determined in accordance with the technical procedures of ATHEXCSD which
are announced by ATHEXCSD to Participants through the DSS or by any other appropriate means of
notifying and communicating with them.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
