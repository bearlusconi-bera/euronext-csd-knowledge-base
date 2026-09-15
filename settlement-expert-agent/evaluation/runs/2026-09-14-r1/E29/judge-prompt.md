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
# ATHEXCSD (Athens): data content of a participant settlement instruction in the DSS, and the permitted intended settlement date window

## Direct answer

A settlement instruction entered in the DSS must, **at the time of entry**, carry fourteen mandatory data items (settlement counterparties, instruction type, settlement method, operation reason, cash value, transaction date, intended settlement date, ISIN, quantity, currency, counterparty CSD identifier for links, place of settlement, securities settlement account, and the Hold/Release condition), and may carry seven optional items. The intended settlement date (ISD) **must not precede the date of entry by more than 60 calendar days and must not exceed the date of entry by more than 365 calendar days**; there is no specific time limit between the ISD and the transaction date.

Note the anchor: the window is measured from the **date the instruction is entered**, in **calendar days**, not from the transaction date and not in business days.

One retrieval was **`blocked`**: the exact DSS interface specification (field formats, lengths, code values, message or file layout) is not in reviewed evidence. This answer therefore tells you *which data* the rules require, not *how to encode them* in the DSS.

*Terms explained on first use:* **DSS** — the Dematerialised Securities System operated by ATHEXCSD; **matching** — pairing the two sides of a settlement instruction so they can settle; **matching field** — a datum that must coincide on both sides for matching to occur; **tolerance level** — the permitted difference in cash value that still allows matching; **operation reason** — a code stating the type of transaction; **NCBO** — "No Change Beneficiary Owner".

## Retrieval statuses

The bundle was re-routed (see the note at the end of this section) and now contains four retrievals:

| Retrieval | Context | Status |
|---|---|---|
| 1 | Athens / settlement / participant / reference / `athens_instruction_content_matching`, as_of 2026-09-14 | `evidence_only` |
| 2 | Athens / settlement / participant / reference / `athens_settlement_methods`, as_of 2026-09-14 | `evidence_only` |
| 3 | Athens / settlement / participant / reference / `athens_production_interface`, as_of 2026-09-14 | **`blocked`** |
| 4 | Athens / settlement / participant / reference / `document_identity`, as_of 2026-09-13 | `evidence_only` |

**Disclosure of the blocked retrieval.** Retrieval 3 returned `blocked` with **GAP ID G12**, reason: "Current DSS technical notices and exact interface specifications required." Nothing in this answer describes the production DSS interface, and the gap is not filled from memory or from the T2S message set. Consistent with that, the settlement-methods section records that procedural and technical details "shall be determined in accordance with the technical procedures of ATHEXCSD which are announced by ATHEXCSD to Participants through the DSS or by any other appropriate means" [[athens-settlement-methods]] (cited in full below), and its own LIMITATION states that business hours, cycles and algorithm specifics are announced through the DSS and are **not in the library (gap G12)**.

**Routing note.** The bundle as first generated contained **no retrievals at all** (empty result set, no topic hits) and so supported no answer. Using the library's topic index, the retrieval was re-run against the listed Athens routes `athens_instruction_content_matching`, `athens_settlement_methods` and `document_identity`, plus the listed blocked topic `athens_production_interface` so that the interface gap is visible rather than silently absent. No question type, entity, date or release outside the index was used.

All three `evidence_only` retrievals are mode **`reference`** on basis **`reference_description`**: they describe what the cited editions say as at their review dates, not a certification of current in-force status.

## 1. Mandatory data (Resolution 5, Part 4, article 4.3(1)A)

**Documented requirement.** "In accordance with the terms of par. 1, article 5.2 of Section V of the Rulebook, in order for a settlement instruction that is entered in the DSS to be accepted for execution and settled through the DSS, it must at the time of its entry, to include the following mandatory data" [[athens-instruction-content]] ATHEXCSD Resolution 5, Part 4 §§4.1–4.3(3) with footnotes 17–28, PDF 9–12; version "Resolution 5: effective 8 December 2025"; reviewed 14 September 2026 (source reviewed 13 September 2026); body language English, **authoritative language Greek — informational English translation, the Greek text prevails**; Resolution 5 codified to 24 November 2025; source identity checked, no independent whole-edition supervisory approval certification.

| # | Mandatory datum | Content as stated in the Resolution | Must coincide for matching? (§4.3(3)) |
|---|---|---|---|
| i | Data on the Settlement Counterparties | Data enabling identification of the Participants participating in the settlement of the transaction | Yes |
| ii | Instruction type | Whether the instruction relates to delivery or receipt of the Security | Yes |
| iii | The specific settlement method | "such as, in particular, delivery versus payment (DVP) or free of payment (FOP) or payment free of delivery (PFOD) or other method in accordance with Commission Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394" | Yes |
| iv | Operation reason | Type of transaction for settlement; "available operation reasons in the DSS are determined by the current Decision" (Annex II) | Yes |
| v | Cash value | "the monetary amount for settlement, which is expressed in euro. The cash value may be zero when the transaction is settled with the free of payment method" | Yes, subject to the tolerance level |
| vi | Transaction date | The day on which the transaction was concluded | Yes |
| vii | Intended settlement date | The day on which the transaction will be settled | Yes |
| viii | ISIN | Unique identification code of the Security to be settled | Yes |
| ix | Quantity | Number of Securities, "or, alternatively, by stating the nominal value of the Security as appropriate, as in the case of bonds" | Yes |
| x | Currency | (no further definition in the excerpt) | Yes |
| xi | Identifier of the CSD of the Participant's counterparty | "in the case of Direct and Indirect Links of ATHEXCSD, including also the cases referred to in paragraph 5, article 30 of Regulation (EU) 909/2014" | Yes |
| xii | Place of Settlement | "The system through which settlement is to take place" | Yes |
| xiii | Securities Settlement Account | "Data identifying the Securities Account, including Transitory Accounts and Provisional Settlement Accounts, through which the delivery or receipt of the Securities to be settled will take place" | **Not listed** among the matching data (matching covers i–xii only) |
| xiv | "Hold" or "Release" Condition | "Conditions as defined in article 5.4 of the Rulebook" | **Not listed** among the matching data |

All rows: [[athens-instruction-content]] Resolution 5 Part 4 §4.3(1)A, PDF 10–11; same version, review dates and qualifications as above.

**Reasoned inference.** Derived from the matching sentence in §4.3(3), which names "sub-cases of i) through xii)": items xiii (securities settlement account) and xiv (Hold/Release) are mandatory for **acceptance** but are not among the data that must coincide for **matching** — so the two sides may legitimately carry different accounts and different hold conditions and still match. The Resolution does not say this in terms; it is read off the enumeration.

## 2. Optional data (article 4.3(1)B)

**Documented requirement.** "In accordance with the terms of article 5.3, a settlement instruction entered in the DSS for execution may, in addition to the mandatory data ... include one or more of the following optional data": a) External matching code — "The code entered, following agreement, by the counterparty Participants for the purpose of distinguishing a pair of settlement instructions from others with similar content"; b) Place of trade; c) Participant's reference code — "Data entered by the Participant in order to facilitate communication within its systems"; d) Unit price; e) Participant End Client; f) Counterparty End Client; g) Comments. The list closes with: "Other data or conditions pertaining to the settlement instructions which are determined by ATHEXCSD" [[athens-instruction-content]] Resolution 5 Part 4 §4.3(1)B, PDF 11–12; same version, review dates and qualifications. Points (e) and (f) were added by decision 374/26.05.2025 with effect from the day following ATHEXCSD's announcement of the successful completion of the technical transition "and in any case until 29.9.2025" (footnote 25).

**Documented requirement — which optional data matter for matching.** Optional data a) and b) "must coincide in content, provided that the element provided for in the respective case has been entered". For e) and f): "matching is achieved provided that the data specified in those cases have been entered by both counterparties. Matching of settlement instructions can still be achieved even if the above data have been entered only by one counterparty or by neither of them." **Exception:** where the operation reason is 'NCBO – No Change Beneficiary Owner', 'Transfer of Securities between Fund Shares of the same Fund' or 'Transfer of Securities from an Issuer Share to the Securities Account of the same beneficiary', "the end client (full name or BIC – Business Identification Code) or the name or BIC of the Fund, must be declared in the relevant settlement instructions. In addition, the above end client details must be the same, in order to be matched" [[athens-instruction-content]] Resolution 5 Part 4 §4.3(3), PDF 12; same qualifications.

## 3. Additional content conditions attached to particular operation reasons (article 4.2)

**Documented requirement.** The operation reason is itself mandatory data, drawn from **Annex II** to Resolution 5, and by stating it "Participants indicate the type of transaction in their settlement instructions, in compliance with the terms of paragraph 4, article 5, Regulation (EU) 2018/1229", with the exception of the Market Claim reason «f-» of Appendix II, "which is used by ATHEXCSD exclusively, when creating settlement instructions due to the application of Market Claims procedures". Specific reasons carry extra requirements [[athens-instruction-content]] Resolution 5 Part 4 §4.2, PDF 9–10; same version, review dates and qualifications:

| Operation reason | Additional requirement stated |
|---|---|
| NCBO ("No Change Beneficiary Owner") | The beneficiary (full name or BIC) must be stated in the relevant instructions; for acceptance, "one of the respective instructions must relate to Securities kept in a Clients Securities Account" |
| "Transfer between Securities Accounts of the same Share" | Both instructions must relate to Securities Accounts of the same Share. This does not apply where the instructions come from a System Operator; in that case the transfer "is carried out only through the settlement instruction of the System Operator or delegated Member or Participant that implements the transfer to settle the relevant arrears" |
| "Transfer of Securities between Client Securities Accounts of different Shares of the same Client for the purpose of consolidating those Shares in the DSS" | The identity of that same Client "must be established on the responsibility of the Participants involved in accordance with the procedures of ATHEXCSD" |
| "Transfer of Securities between Securities Accounts of the same beneficiary as Market Maker Participant at the commencement or cessation of Market Making" | The identity of that same beneficiary as Market Maker must be established on the responsibility of the Participants involved, per ATHEXCSD procedures |
| "Transfer of Securities between Fund Shares of the same Fund" | The transfer must be carried out between Shares of the same Fund "in compliance with the terms of par. 4.9.2, Section III of the Rulebook", and the instructions "must contain the legal name or Business Identifier Code (BIC) of the Fund" |

**Unresolved requirement.** The **Annex II list of operation reasons is outside the excerpt** (explicit LIMITATION on [[athens-instruction-content]]), so the permitted reason codes and their exact labels are **not in reviewed evidence**. "Share" is the English translation's term for a DSS account-structure element defined in the Rulebook; the Rulebook definition is not in the bundle and the Greek text prevails.

## 4. How far in the past or future the intended settlement date may be

**Documented requirement.** Article 4.3(2), "Terms of accepting a settlement instruction" — "In order for a settlement instruction to be accepted, it must fulfil the following specific terms, according to par.1, article 5.2 of Section V of the Rulebook":

- **a.** "The intended settlement date of the settlement instruction must not precede the date of its entry by more than **60 calendar days**."
- **b.** "The intended settlement date of the settlement instruction must not exceed the date of its entry by more than **365 calendar days**."
- **c.** "There is no specific time limit between the intended settlement date of the settlement instruction and the transaction date."

[[athens-instruction-content]] Resolution 5 Part 4 §4.3(2), PDF 12; version "Resolution 5: effective 8 December 2025"; reviewed 14 September 2026 (source reviewed 13 September 2026); informational English translation, Greek text prevails; footnotes 26–27 record that paragraph 2 and points b) and c) were worded as above by decision 374/26.05.2025 with effect as of 30.06.2025.

**Reasoned inference — the practical window.** Derived from a. and b. read together: for an instruction entered on day E, the acceptable ISD range is **E − 60 calendar days to E + 365 calendar days**, inclusive of the boundary in the sense that only dates *more than* 60 days before, or *more than* 365 days after, entry are excluded. Because of c., a very old transaction date does not by itself make the instruction unacceptable — only the ISD-to-entry distance is constrained.

**Unresolved requirement — acceptance is not settlement.** §4.3(2) states the conditions for **accepting** an instruction. What the DSS then does with a back-dated ISD (immediate settlement attempt, recycling, penalties, reporting) is **not in reviewed evidence**; the excerpt does not address it, and the operational cycle detail is exactly what gap G12 blocks.

## 5. Matching and tolerance (what is and is not available)

**Documented requirement.** Matching, implementing "case c), par. 1, article 5.5 of the Rulebook", requires that the mandatory data i)–xii) and the optional data a) and b) "coincide in content, provided that the element provided for in the respective case has been entered" [[athens-instruction-content]] §4.3(3), PDF 12; same qualifications.

**Documented requirement, with the value missing.** On tolerance: "Matching of settlement instructions is achieved even if their respective 'cash value' fields do not match, provided that the cash value difference does not exceed the tolerance level as defined in ..." — the excerpt ends there [[athens-instruction-content]] §4.3(3), PDF 12. **Unresolved requirement:** the LIMITATION on this section states expressly that "the tolerance values are outside the excerpt". The numeric tolerance bands are therefore **not in reviewed evidence** and must not be assumed from any other market's values.

## 6. Where the technical detail lives (and why it is not here)

**Documented requirement.** "Any procedural or technical details relating to settlement operations, as set forth in the Rulebook and this Resolution, for instance with respect to settlement methods, the business hours and performance of settlement, the particular specifications of the settlement algorithm, or the number and duration of settlement cycles, shall be determined in accordance with the technical procedures of ATHEXCSD which are announced by ATHEXCSD to Participants through the DSS or by any other appropriate means of notifying and communicating with them" [[athens-settlement-methods]] ATHEXCSD Resolution 5, Part 2 §§2.1–2.2, PDF 4; version "Resolution 5: effective 8 December 2025"; reviewed 14 September 2026 (source reviewed 13 September 2026); informational English translation, **Greek text prevails**; Resolution 5 codified to 24 November 2025; source identity checked, no independent whole-edition supervisory approval certification. LIMITATION: business hours, cycles and algorithm specifics are announced through the DSS and are not in the library (**gap G12**).

**Documented requirement (context for the cash leg).** ATHEXCSD settles on the basis of the settlement methods in Section V of the Rulebook and Commission Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394; "For the purposes of cash settlement, ATHEXCSD blocks cash balances in the Cash Settlement Accounts. Specifically in the case of cash settlement carried out in TARGET-GR with the participation of Settlement Banks, the aforesaid balances are blocked through TARGET-GR in the respective Sub-accounts kept by Settlement Banks for Participants" [[athens-settlement-methods]] §2.1, PDF 4; same qualifications.

**Reasoned inference.** Derived from §2.2 plus the blocked retrieval: the split is deliberate. Resolution 5 fixes the *normative* data content and acceptance window; the *interface* (formats, lengths, code lists, transport) is delegated to DSS announcements, which are client-facing and are the subject of gap G12. Any technical specification work must obtain those announcements; they cannot be inferred from Resolution 5, and a T2S message description is not a substitute for the DSS local interface.

## 7. Edition and approval qualifications for the underlying Rulebook

**Documented requirement.** The ATHEXCSD Rulebook rests on article 3 of Law 4569/2018 (Government Gazette Α/179/11.10.2018), decision 311/22.02.2021 of the ATHEXCSD Board and HCMC approval decision 6/904/26.2.2021 (Government Gazette Β/1007/16.03.2021), with seven amendments listed, the seventh being "Decision 383/24.11.2025 of the Board of Directors of ATHEXCSD (decision 1/1074/4.12.2025 of the Board of Directors of the Hellenic Capital Market Commission, Government Gazette Β/6784/16.12.2025)". The same history appears in the Greek master [[athens-edition]] ATHEXCSD Rulebook – Amendment 8, English master amendment history, PDF 2, and athens-greek-master, Greek master amendment history, PDF 2; version note: "Hub says Amendment 8; filename and internal history indicate 7th amendment, with late-2025 dates"; **reviewed 13 September 2026** (source reviewed 13 September 2026); the English master's body language is English with **no authoritative language designated and not independently established**, while the Greek master is the **original / official-language text**; source identity checked, no independent whole-edition supervisory approval certification. LIMITATION: the probable edition/amendment label mismatch is an **inference**, and the independent HCMC/Gazette chain remains **incomplete**.

**Why this matters here.** Every requirement above is stated by Resolution 5 "in accordance with" Rulebook Part 5, Section V, articles 5.2, 5.3, 5.4 and 5.5 — provisions that are **not in this bundle**. The Resolution is the implementing text; the Rulebook is the source of the obligations it implements, and its edition label is itself unresolved.

## Scope limits you should not skip

- **Governing language.** Both Resolution 5 sections are an **informational English translation; the Greek text prevails** [[athens-instruction-content]], [[athens-settlement-methods]]. Field names quoted here are translation artefacts, not normative labels.
- **Review dates are facts, not clocks.** Retrievals 1 and 2 were reviewed **14 September 2026**; retrieval 4 (edition evidence) was reviewed **13 September 2026**; the underlying sources were reviewed 13 September 2026. Nothing becomes "current today" through the passage of time, and no dated announcement overlay was retrieved.
- **Effective dates.** Resolution 5 is codified to 24 November 2025 and effective **8 December 2025**; individual provisions carry their own amendment footnotes (for example §4.3(2) as worded by decision 374/26.05.2025 with effect from 30.06.2025). Publication or codification of a text is not evidence of any later change.
- **No approval certification.** None of the three sections carries independent whole-edition supervisory approval certification; source identity only was checked.
- **Reference mode.** All three sections are `reference` / `reference_description`, not `current`.

## Open items

1. **Annex II to Resolution 5 (operation reasons)** — the permitted operation-reason codes and labels, including the Market Claim reason «f-» reserved to ATHEXCSD. Outside the retrieved excerpt (explicit LIMITATION). Route: ATHEXCSD public resolutions page (Resolution 5, Annex II), Greek governing version.
2. **Tolerance levels** for the cash-value matching field — the sentence is truncated in the reviewed excerpt and the LIMITATION states the values are outside it. Route: ATHEXCSD Resolution 5 §4.3(3) in full, Greek version.
3. **ATHEXCSD Rulebook, Part 5, Section V, articles 5.2, 5.3, 5.4 and 5.5** — the underlying obligations on mandatory/optional data, the Hold/Release definition and matching. Not in this bundle. Route: ATHEXCSD public Rulebook (Greek master preferred; note the unresolved 7th-amendment / "Amendment 8" label question).
4. **DSS technical announcements — gap G12 (blocked retrieval).** Exact interface specification: field formats, lengths, code values, message/file layouts, business hours, number and duration of settlement cycles, settlement-algorithm specifics. Delegated by Resolution 5 §2.2 to ATHEXCSD technical procedures announced through the DSS. Route: ATHEXCSD client channel (DSS announcements to Participants); these are client-only and cannot be replaced by T2S documentation.
5. **Processing of a back-dated ISD** (within the 60-calendar-day allowance) — settlement attempt, recycling, and any penalty or reporting consequence. Not addressed in the retrieved excerpt; likely in the Rulebook Section V and the DSS announcements (gap G12).
6. **Independent HCMC / Government Gazette approval chain** for the current Rulebook edition, and resolution of the "Amendment 8" versus "7th amendment" label. Incomplete in reviewed evidence [[athens-edition]]. Route: HCMC decisions and the Government Gazette references listed in the amendment history.

No section in the bundle contained instruction-like content directed at the answering system.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:58:12.924955+00:00). Review dates available: 2026-09-13, 2026-09-14.

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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "athens_production_interface"}
STATUS: blocked — Current DSS technical notices and exact interface specifications required.
GAP IDS: ['G12']

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "document_identity"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[athens-edition]] — Athens edition versus amendment evidence (reviewed 2026-09-13; modes ['reference']; entities ['Athens']; basis reference_description)
CITATION: ATHEXCSD Rulebook - Amendment 8 | English master amendment history; PDF 2 | version Hub says Amendment 8; filename and internal history indicate 7th amendment, with late-2025 dates. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://athens.euronext.com/sites/default/files/2026-06/ATHEXCSD_RULEBOOK_7th_Ammendment_383_24.11.2025_FORCE_8.12.2025.pdf
CITATION: athens-greek-master | Greek master amendment history; PDF 2 | version None | body language el | authoritative language el | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://athens.euronext.com/sites/default/files/2026-06/%CE%9A%CE%91%CE%9D%CE%9F%CE%9D%CE%99%CE%A3%CE%9C%CE%9F%CE%A3_%CE%9B%CE%95%CE%99%CE%A4%CE%9F%CE%A5%CE%A1%CE%93%CE%99%CE%91%CE%A3_%CE%95%CE%9B%CE%9A%CE%91%CE%A4_7%CE%B7_%CE%A4%CF%81%CE%BF%CF%80%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_383_24.11.2025_%CE%99%CE%A3%CE%A7%CE%A5%CE%A3_8.12.2025.pdf
LIMITATION: Probable edition/amendment label mismatch is an inference. Independent HCMC/Gazette chain remains incomplete.
EXCERPT (English master amendment history; PDF 2):
[PDF page 2]

  In accordance with article 3 of Law 4569/2018 (Government Gazette Α/179/11.10.2018),

             decision 311/22.02.2021 of the Board of Directors of ATHEXCSD

                     and approval decision 6/904/26.2.2021

                    of the Hellenic Capital Market Commission (HCMC)

                    (Government Gazette Β/1007/16.03.2021)





                       AMENDMENTS:

1.  Decision  324/28.01.2022  of  the  Board  of  Directors  of ATHEXCSD  (decision
   944/31.01.2022 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette B/1064/10.03.2022).
2.  Decision  352/25.09.2023  of  the  Board  of  Directors  of ATHEXCSD  (decision
   3/1000/31.10.2023 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette B/6249/31.10.2023)
3.  Decision  362/29.07.2024  of  the  Board  of  Directors  of ATHEXCSD  (decision
   1030/22.8.2024 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette B/5036/04.09.2024)
4.  Decision  365/04.09.2024  of  the  Board  of  Directors  of ATHEXCSD  (decision
   1032/4.9.2024 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette B/5225/17.09.2024)
5.  Decision  367/21.10.2024  of  the  Board  of  Directors  of ATHEXCSD  (decision
   7/1040/28.11.2024 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette Β/1398/21.03.2025)
6.  Decision  374/26.05.2025  of  the  Board  of  Directors  of ATHEXCSD  (decision
   1057/26.6.2025 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette Β/4140/30.07.2025)
7.  Decision  383/24.11.2025  of  the  Board  of  Directors  of ATHEXCSD  (decision
   1/1074/4.12.2025 of the Board of Directors of the Hellenic Capital Market Commission,
   Government Gazette Β/6784/16.12.2025)





                                                                        2



                                      PRIVATE
EXCERPT (Greek master amendment history; PDF 2):
[PDF page 2]
     σύμφωνα με το άρθρο 3 του ν.4569/2018 (ΦΕΚ Α/179/11.10.2018)

    την από 22.02.2021 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ.

                      και την υπ’αριθμ. 6/904/26.2.2021

               εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                    ΦΕΚ Β/1007/16.03.2021





                           ΤΡΟΠΟΠΟΙΗΣΕΙΣ:



1.  324/28.01.2022 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.

     1a/944/31.01.2022 εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                    ΦΕΚ Β/1064/10.03.2022

2.  352/25.09.2023 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
           3/1000/31.10.2023 εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                        ΦΕΚ Β/6249/31.10.2023

3.  362/29.07.2024 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
            1030/22.8.2024 εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                        ΦΕΚ Β/5036/04.09.2024

4.  365/04.09.2024 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
             1032/4.9.2024 εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                        ΦΕΚ Β/5225/17.09.2024

5.  367/21.10.2024 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
          7/1040/28.11.2024  εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                        ΦΕΚ Β/ 1398/21.03.2025

6.  374/26.05.2025 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
            1057/26.6.2025  εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς

                        ΦΕΚ Β/4140/30.07.2025

7.  383/24.11.2025 απόφαση του Διοικητικού Συμβουλίου της ΕΛ.Κ.Α.Τ. και την υπ’ αριθμ.
         1/1074/4.12.2025 εγκριτική απόφαση της Επιτροπής Κεφαλαιαγοράς ΦΕΚ
                                 Β6784/16.12.2025





                                PRIVATE
                                                                  2 από 206

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
