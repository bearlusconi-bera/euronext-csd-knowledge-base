# sese.023.001.11 — what the reviewed evidence can and cannot give you

## Direct answer

**I cannot give you that list.** A full list of mandatory XML elements with their cardinalities for sese.023.001.11 is **not in reviewed evidence**, and one of the six retrievals behind this answer came back `blocked` precisely on that point. What the reviewed evidence does contain is one level coarser: the UDFS outline of the message's **building blocks**, each marked mandatory or optional and repetitive or non-repetitive. That is not the same thing as element-level cardinality (there are no `[1..1]` / `[0..n]` multiplicities, no element names below building-block level, no conditional rules and no data types in the admitted excerpt), so I will give you the building-block picture and name exactly what you must obtain to get the rest.

Two scope points must be settled before any field list is useful, and they change the answer:

- **sese.023.001.11 is the CSD/DCP-to-T2S message, not a bank-to-CSD interface** [[t2s-sese023-scope]]. So "as used by Monte Titoli participants" splits in two: a **directly connected party (DCP)** sends the T2S-native message; an **indirectly connected party (ICP)** instructs Milan over X-TRM, whose field set is a different, functionally-mapped list.
- **Release**: the retriever **assumed** `release=R2026.JUN` for four of the six retrievals, with the router note "release=R2026.JUN (deployed release assumed; the answer must disclose it)". I disclose that assumption here: everything below is the R2026.JUN UDFS text as reviewed on 2026-09-13 and 2026-09-14. I have no evidence in this bundle confirming which release was deployed on any particular business date, and a review date is not a statement about today.

## 1. Retrieval statuses — disclosed in full

| # | Context | Status |
|---|---|---|
| 1 | Milan, settlement, `native_message_overview`, current, R2026.JUN assumed, as of 2026-09-13 | `evidence_only` |
| 2 | T2S, settlement, `native_message_overview`, current, R2026.JUN assumed, as of 2026-09-13 | `evidence_only` |
| 3 | Milan, settlement, `t2s_message_sese023_scope`, current, R2026.JUN assumed, as of 2026-09-14 | `evidence_only` |
| 4 | T2S, settlement, `t2s_message_sese023_scope`, current, R2026.JUN assumed, as of 2026-09-14 | `evidence_only` |
| 5 | Milan, settlement, `milan_xtrm_field_mapping`, current, as of 2026-09-14 | `evidence_only` |
| 6 | Milan, settlement, `mystandards_usage_rules`, current, as of 2026-09-13 | **`blocked`** |

**Unresolved requirement — the blocked retrieval is the one that would have answered your question.** Retrieval 6 returned status `blocked` with the reason "MyStandards usage guidelines and XSDs require an account; T2S-native usage rules are not admitted field by field", and the retriever recorded **GAP ID G14**. Field-by-field usage rules are therefore not admitted evidence in this library, and I will not fill that gap from memory of ISO 20022 schemas — doing so is forbidden and would be indistinguishable from invention.

## 2. What is documented: the building blocks of sese.023.001.11

**Documented requirement.** The SecuritiesSettlementTransactionInstructionV11 message — a Settlement Instruction within T2S — is sent by a CSD or a directly connected T2S party to T2S, and allows the instructing party to request a transfer of securities relating to a securities transaction (for example an OTC trade, a corporate action, a repo), with or without a cash payment. In response T2S sends a sese.024.001.12 when validation, matching and settlement are carried out, and a sese.025.001.11 when settlement is successful. The message is composed of the following building blocks, with the status shown:

| Building block | Status in the UDFS outline | Repetitive? | Label |
|---|---|---|---|
| Transaction Identification | mandatory | not repetitive | Documented requirement |
| SettlementTypeAndAdditionalParameters | mandatory | non repetitive | Documented requirement |
| NumberCounts | optional | non repetitive | Documented requirement |
| Linkages | optional | **repetitive** | Documented requirement |
| TradeDetails | mandatory | non repetitive | Documented requirement |
| FinancialInstrumentIdentification | mandatory | non repetitive | Documented requirement |
| FinancialInstrumentAttributes | "not required in T2S" | not stated in the excerpt | Documented requirement |
| QuantityAndAccountDetails | mandatory | non repetitive | Documented requirement |
| SettlementParameters | mandatory | non repetitive | Documented requirement |
| DeliveringSettlementParties | optional | non repetitive | Documented requirement |
| ReceivingSettlementParties | optional | non repetitive | Documented requirement |
| CashParties | optional | non repetitive | Documented requirement |
| SettlementAmount | optional | non repetitive | Documented requirement |
| OtherAmounts | "not required in T2S" | not stated in the excerpt | Documented requirement |
| OtherBusinessParties | "not required in T2S" | not stated in the excerpt | Documented requirement |
| AdditionalPhysicalOrRegistrationDetails | "not required in T2S" | not stated in the excerpt | Documented requirement |

Citation for the whole table: [[t2s-sese023-scope]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §3.3.6.4.1–3.3.6.4.2 outline of the schema, PDF 1233–1234; version R2026.JUN; reviewed 2026-09-14 (source reviewed 2026-09-13); body language English, no authoritative language recorded, translation status "not independently established"; source identity checked, no independent whole-edition supervisory approval certification.

Content of each building block, as printed in the same excerpt: Transaction Identification contains an identification assigned by the instructing party to uniquely and unambiguously identify the transaction; SettlementTypeAndAdditionalParameters contains settlement type and identification information; NumberCounts contains the number of transactions linked; Linkages is used to link instructions and specify settlement sequences (for example after / before / with); TradeDetails contains detailed information related to the Settlement Instruction; FinancialInstrumentIdentification identifies the financial instrument being settled; QuantityAndAccountDetails contains the account and quantity details; SettlementParameters contains parameters stating the conditions that must be fulfilled before the transaction can settle, defined by the instructing party in compliance with the settlement rules of the market the transaction settles in; DeliveringSettlementParties and ReceivingSettlementParties contain the chain of delivering and receiving settlement parties; CashParties contains the cash parties where different from the securities settlement parties; SettlementAmount contains the total amount of money to be paid or received in exchange for the securities. Same citation [[t2s-sese023-scope]].

**Reasoned inference** (derived from the outline's wording, not printed as such): a building block marked mandatory and non-repetitive behaves like a once-only mandatory component of the message, and "not required in T2S" marks a block present in the ISO message but outside the T2S usage. Neither statement licenses you to translate a block status into an element cardinality: the outline says nothing about which elements *inside* a mandatory block are themselves mandatory, and a mandatory block can contain optional elements. Treating the table above as a cardinality list would be a mapping error, not a citation.

**Qualifications travelling with [[t2s-sese023-scope]]** (bundle LIMITATION lines, both material to your request): (i) "Business rules table (PDF 1235 onwards) and message examples are not admitted; the T2S-specific schema is published on MyStandards, which requires an account"; (ii) "This is the CSD/DCP-to-T2S message, not a bank-to-CSD interface." The excerpt itself states that the T2S-specific schema and documentation in HTML/PDF format, plus the message examples, are provided outside the UDFS on MyStandards.

## 3. The surrounding message dialogue (documented, for completeness)

**Documented requirement.** sese.023.001.11 is the inbound message of the Send Settlement Instruction dialogue. The outbound messages listed for that dialogue are SecuritiesSettlementTransactionStatusAdvice (sese.024.001.12) under the message usages "CoSD Hold", "Rejected", "Accepted", "Accepted with Hold", "Accepted with CSD Validation Hold", "Matched", "Cancelled", "No hold remain(s)", "Eligibility Failure", "Intraday Restriction", "Provision Check Failure", "Partial Settlement (unsettled part)", "CoSD awaiting from Administering Party" and "Counterparty's Settlement Instruction on Hold"; SecuritiesSettlementTransactionAllegementNotification (sese.028.001.10); SecuritiesSettlementAllegementRemovalAdvice (sese.029.001.06); SecuritiesMessageCancellationAdvice (semt.020.001.07); SecuritiesSettlementTransactionConfirmation (sese.025.001.11) under "Full Settlement", "Last Partial Settlement" and "Partial Settlement (settled part)"; and SecuritiesSettlementTransactionGenerationNotification (sese.032.001.11) under "Realignment" [[t2s-messages]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §2.3.8 inbound/outbound messages, PDF 778; version R2026.JUN; reviewed 2026-09-13; body language English, no authoritative language recorded, translation status "not independently established"; source identity checked, no independent whole-edition supervisory approval certification.

*Allegement — a notice to a counterparty that an instruction is waiting to be matched against it. This is an explanation of the term, not a documented requirement.*

**Documented requirement.** In a cross-CSD (including external-CSD) context, if T2S cannot create the necessary realignment because of erroneous links or account configuration, or because validation of potential T2S-generated realignment instructions fails, the inbound Settlement Instruction is **cancelled**; if realignment can be created, T2S creates the additional T2S-generated realignment Settlement Instructions and links them to the inbound instruction for settlement on an **all-or-none** basis, and for each one a "Realignment" SecuritiesSettlementTransactionGenerationNotification goes to the CSD involved in the realignment chain [[t2s-messages]] same document, §2.3 realignment dialogue, PDF 753; version R2026.JUN; reviewed 2026-09-13; English body text, translation status "not independently established". Qualifications carried by that section: "T2S-native messages, not bank-to-local-CSD formats; subscriptions and privileges affect recipients", and — directly on point for your request — **"No production payload or full schema admitted."**

**Documented requirement — an acceptance status is not a booking.** T2S ensures the generated realignment instructions and their business instructions settle on an all-or-none basis, and this relies on links set in reference data with no further action by T2S actors [[t2s-realignment]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.10 concepts and reference-data requirements, PDF 373–376; version R2026.JUN; reviewed 2026-09-13; English body text, translation status "not independently established" (qualifications: actual links, accounts and ISIN eligibility require verification; the section does not establish atomicity of an arbitrary two-security swap and does not describe every action outside T2S). The transfer itself happens at posting: the posting process checks eligibility and available resources and, when the check is satisfactory, updates the cash balance, securities position and limit headroom, "resulting in the irrevocability of the settlement" [[t2s-posting]] same document, §1.6.1.8.1 and first overview paragraph, PDF 303–304; version R2026.JUN; reviewed 2026-09-13; English body text, translation status "not independently established". Matching is not settlement; a "Matched" status advice is not a completed ledger movement.

## 4. If your participants are ICP (X-TRM), this is the list that exists

**Documented requirement — but read the four qualifications first.** Milan publishes a functional correspondence between X-TRM fields and T2S fields, with three information types defined in the source as: **Mandatory** — "mandatory information (if not specified can assume default values)"; **Additional** — "if specified by a counterparty, considered mandatory feedback fields and therefore must also be specified by the other party"; **Optional** — "considered feedback fields required only if specified by both counterparties". The reviewed table has **13 mandatory, 2 additional and 4 optional** rows:

| X-TRM field | T2S field | Type | Default |
|---|---|---|---|
| Issuer | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO |
| Counterparty | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO |
| Code of System Custody Issuer | CSD of Delivering / Receiving Party (based on Securities Movement Type) | Mandatory | NO |
| Code of System Custody Counterparty (footnote 1 marker) | CSD of Delivering / Receiving Party (based on Securities Movement Type) | Mandatory | NO |
| Settlement Date | Intended Settlement Date | Mandatory | blank as printed |
| Data Executed | Trade Date | Mandatory | Date of release of the contract in X-TRM |
| Object Code Negotiated | ISIN | Mandatory | NO |
| Quantity | Settlement Quantity | Mandatory | NO |
| Countervalue | Settlement Amount | Mandatory | NO |
| Settlement Currency | Currency | Mandatory | NO |
| Mark | Securities Movement Type | Mandatory | NO |
| Countervalue Verse | Credit / Debit Indicator | Mandatory | NO |
| n.a. | Payment Type ("this fields will be fill…" — cell text truncated in the original layout) | Mandatory | NO |
| Settlement Transaction Condition (footnote 1 marker) | Settlement Transaction Condition (Opt Out) | Additional | NO |
| Trade Transaction Condition | Trade Transaction Condition ("CUM / Ex…" — cell text truncated in the original layout) | Additional | NO |
| Beneficiary Issuer Code BIC | Client of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |
| Beneficiary Counterpart Code BIC | Client of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |
| Common Trade Reference | Common Trade Reference | Optional | NO |
| Counterpart Settlement Securities Account | Securities Account of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |

Beyond the table, the source states that X-TRM also allows the following additional information to be specified: ISO code of the operation; partial settlement indicator; priority settlement indicator; indicator for the connection of settlement instructions; indicator of the changeability of settlement instructions; identification code of the pool of settlement (Pool reference ID); identification code of the settlement instructions associates (Reference ID for Settlement Instructions); identification code of settlement restrictions (Reference ID for Settlement Restrictions); identification code for the suspension, cancellation, modification of settlement instruction.

Citation: [[milan-xtrm-field-mapping]] Instructions to Settlement Service and related instrumental activities — in force as of 30 June 2025, §3.4.1 Table 2 (X-TRM fields versus T2S fields) and additional information list, PDF 39–41 (printed 35–37); version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025); reviewed 2026-09-14; body language English but **the Italian text is the authoritative version and prevails** (cover, PDF 1) — English translation excerpt with uneven wording, authoritative language differs, quoted terms follow the source; source identity checked, no independent whole-edition supervisory approval certification. The table was transcribed from rendered page images at 110 dpi because text extraction of these tables was column-garbled; the images are the reference.

**Qualifications and recorded anomalies that travel with this table** — decisive for your question: (i) "Functional correspondence only: **not the A2A/RNI message layouts, not a T2S XSD**, and two source cells are truncated in the original layout (recorded)"; (ii) the footnote (1) referenced on two rows was **not located** on the reviewed pages; (iii) the truncated cells ("this fields will be fill…", "CUM / Ex…") are preserved as anomalies and **not completed**; (iv) the section's own scope line: "Functional field correspondence as published by Milan for ICP/X-TRM users. Not the client-only Standard for X-TRM Users message layouts; not a production XSD; not certification of T2S message paths." Note also that this is the edition in force as of 30 June 2025 — an older edition than the T2S UDFS R2026.JUN text above; the bundle contains no later edition of these Instructions, and I quote no schedule or cut-off from this document.

**Reasoned inference.** The X-TRM "Mandatory" semantics ("if not specified can assume default values") and the T2S-native mandatory/optional building-block statuses are **different concepts on different interfaces**, and the two lists cannot be merged into a single cardinality table. Mapping X-TRM rows onto sese.023.001.11 elements would require the local message layout plus the T2S usage guideline, neither of which is in reviewed evidence.

## 5. What a defensible field-level answer would require

| Needed artefact | Why | Label |
|---|---|---|
| T2S usage guideline / T2S-specific XSD for sese.023.001.11 on MyStandards | Only source of element-level mandatory status and cardinalities; the UDFS itself points outside the document for the schema, documentation and examples | Unresolved requirement — blocked, GAP G14 (account required) |
| UDFS business rules table for sese.023.001.11 (PDF 1235 onwards) | Conditional rules and rejection reasons; explicitly **not admitted** by the reviewed section | Unresolved requirement |
| Milan's client-only Standard for X-TRM Users message layouts | The actual ICP layout, as distinct from the published functional correspondence | Unresolved requirement |
| Confirmation of the deployed release on the intended business date | R2026.JUN was an **assumption inserted by the retriever**, not evidenced deployment | Unresolved requirement |
| Statement of whether your participants are DCP or ICP, and the ISIN / account / link configuration | Determines which interface and which field set applies at all | Needs your input — a scope element, not a documented fact |

**Proposed design choice** (yours to make, not an infrastructure rule): specify your interface layer against the building-block structure above and hold the element-level cardinalities as an explicit open dependency in your specification, rather than populating them from an uncertified source. I have produced no illustrative payload here on purpose: any XML I wrote would look like a production artefact and none is admitted.

I have not drafted or sent any request to Monte Titoli, Euronext Securities Milan, the ECB or SWIFT, and I have not consulted anything outside this bundle.

## Open items

1. **Element-level mandatory list and cardinalities for sese.023.001.11 — blocked, GAP G14.** Route: the T2S MyStandards usage guideline and T2S-specific schema (the reviewed excerpt names the MyStandards location for sese.023.001.11; access needs a SWIFT MyStandards account). Until that is reviewed, the list does not exist in this library.
2. **UDFS business rules table, PDF 1235 onwards, and the message examples** — not admitted by [[t2s-sese023-scope]] (reviewed 2026-09-14). Route: the same T2S UDFS R2026.JUN edition, sections beyond the reviewed page range, submitted for review.
3. **Milan's X-TRM client documentation** — the Standard for X-TRM Users layouts are client-only and absent. Route: the Euronext Securities Milan client documentation service / MT-X client platform.
4. **Footnote (1) of Milan Table 2** — referenced on two rows, text not located on PDF 39–41. Route: the full Italian authoritative edition of the Settlement Service Instructions (Italian text prevails), and any later edition superseding the 30 June 2025 one (MN_10/2025).
5. **Two truncated T2S-field cells** in Milan Table 2 ("this fields will be fill…", "CUM / Ex…") — recorded as anomalies, not reconstructed. Route: the Italian authoritative text of §3.4.1.
6. **Deployed-release confirmation.** R2026.JUN is a retriever assumption disclosed above; a release-status or notice section is needed to tie it to an actual business date.
7. **DCP versus ICP scope and per-ISIN eligibility** — client data, not a library gap. Needed from you before any specification row can be filled.
