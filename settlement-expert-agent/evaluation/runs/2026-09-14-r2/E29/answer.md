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
