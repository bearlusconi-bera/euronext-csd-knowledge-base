# Mandatory XML elements and cardinalities for sese.023.001.11 (Monte Titoli participants)

## Direct answer

**Unresolved requirement.** The reviewed evidence does not contain an element-level list of mandatory XML elements with cardinalities for `sese.023.001.11`, and I will not reconstruct one. The T2S-specific schema, the usage guideline and the message examples are published on MyStandards, which requires an account, and they are explicitly **not admitted** as reviewed evidence. One retrieval in this bundle returned **STATUS: blocked** for exactly this topic ("MyStandards usage guidelines and XSDs require an account; T2S-native usage rules are not admitted field by field", **GAP ID G14**), and the `[[t2s-sese023-scope]]` section carries the same LIMITATION: the business-rules table (PDF 1235 onwards) and the message examples are not admitted.

What the reviewed evidence *does* support, and what I set out below, is three different and weaker things:

1. the **message building-block outline** of `sese.023.001.11` with each block's mandatory/optional and repetitive/non-repetitive status (T2S UDFS, platform release **R2026.JUN**);
2. the **exhaustive functional matching-field list** (mandatory / additional / optional per transaction type);
3. Milan's published **X-TRM-to-T2S functional field correspondence table**, which is an ICP-level field correspondence, not a message layout.

A second qualification matters for "as used by Monte Titoli participants": `[[t2s-sese023-scope]]` carries the LIMITATION "This is the CSD/DCP-to-T2S message, not a bank-to-CSD interface", and the UDFS states the message "is sent by a CSD or a directly connected T2S party to T2S". **Reasoned inference** (derived from those two statements): a Monte Titoli participant that is *not* directly connected does not itself send `sese.023.001.11`; it instructs Milan over the local interface, and Milan's own published field table is the X-TRM correspondence in point 3. Whether a given participant is a DCP, and its actual entitlements, are **not in reviewed evidence**.

**Retrieval statuses in this bundle:** five retrievals returned `evidence_only`; retrieval 6 (`mystandards_usage_rules`, Milan, settlement, participant, current, as of 2026-09-14) returned **blocked** with GAP ID G14. No retrieval returned `needs_context` or `needs_refresh` after the release scope (`R2026.JUN`) was supplied.

---

## 1. Building blocks of `sese.023.001.11` — what the UDFS states

**Documented requirement.** `[[t2s-sese023-scope]]` T2S User Detailed Functional Specifications R2026.JUN (UDFS), §3.3.6.4.1–3.3.6.4.2 "Overview and scope of the message" / "The T2S-specific schema", PDF 1233–1234; version R2026.JUN; body language English, no authoritative language independently established; source reviewed 2026-09-13, section reviewed **14 September 2026**; platform release **R2026.JUN**; approval: source identity checked, no independent whole-edition supervisory approval certification.

The UDFS describes presence and repetition **per building block**, in words. It does not print ISO cardinality notation on these pages, and it does not descend to element level.

| # | Building block (UDFS spelling) | UDFS statement | Label |
|---|---|---|---|
| 1 | Transaction Identification | "mandatory and not repetitive" | Documented requirement |
| 2 | SettlementTypeAndAdditionalParameters | "mandatory and non repetitive" | Documented requirement |
| 3 | NumberCounts | "optional and non repetitive" | Documented requirement |
| 4 | Linkages | "optional and repetitive" | Documented requirement |
| 5 | TradeDetails | "mandatory and non repetitive" | Documented requirement |
| 6 | FinancialInstrumentIdentification | "mandatory and non repetitive" | Documented requirement |
| 7 | FinancialInstrumentAttributes | "not required in T2S" (no mandatory/repetition wording on the reviewed pages) | Documented requirement |
| 8 | QuantityAndAccountDetails | "mandatory and non repetitive" | Documented requirement |
| 9 | SettlementParameters | "mandatory and non repetitive" | Documented requirement |
| 10 | DeliveringSettlementParties | "optional and non repetitive" | Documented requirement |
| 11 | ReceivingSettlementParties | "optional and non repetitive" | Documented requirement |
| 12 | CashParties | "optional and non repetitive" | Documented requirement |
| 13 | SettlementAmount | "optional and non repetitive" | Documented requirement |
| 14 | OtherAmounts | "not required in T2S" | Documented requirement |
| 15 | OtherBusinessParties | "not required in T2S" | Documented requirement |
| 16 | AdditionalPhysicalOrRegistrationDetails | "not required in T2S" | Documented requirement |

So the **mandatory, non-repetitive** building blocks named by the UDFS are: Transaction Identification, SettlementTypeAndAdditionalParameters, TradeDetails, FinancialInstrumentIdentification, QuantityAndAccountDetails, SettlementParameters. That is a block-level list, not the element-level list the question asks for.

**Reasoned inference** (derived only from the wording above, not from a schema): a block described as "mandatory and non repetitive" behaves as a one-and-only-one occurrence and a block described as "optional and repetitive" (Linkages) as a zero-to-many occurrence. I deliberately do not write these as ISO cardinality expressions, because the reviewed pages do not print them and the admitted text does not establish the exact upper bounds. Any cardinality figure for a *child element* inside these blocks is **Unresolved requirement — not in reviewed evidence**.

**Documented requirement (same section):** the UDFS states that the T2S-specific schema, the HTML/PDF documentation and the message examples are provided outside the UDFS, under the MyStandards link printed at §3.3.6.4.2 for `sese.023.001.11_T2S`. **Documented requirement:** in response to the Settlement Instruction, T2S sends `sese.024.001.12` when validation, matching and settlement are carried out, and `sese.025.001.11` when settlement is successful `[[t2s-sese023-scope]]` (§3.3.6.4.1, PDF 1233; reviewed 2026-09-14).

**Documented requirement.** `[[t2s-messages]]` UDFS R2026.JUN §2.3.8, PDF 778 (section reviewed 2026-09-13; platform release R2026.JUN; LIMITATIONS: "T2S-native messages, not bank-to-local-CSD formats; subscriptions and privileges affect recipients" and "No production payload or full schema admitted") lists `sese.023.001.11` as the single inbound message of the Send Settlement Instruction dialogue, with outbound `sese.024.001.12` status advices (including "Accepted", "Matched", "Rejected", "CoSD Hold", "Partial Settlement (unsettled part)"), `sese.025.001.11` confirmations, `sese.028.001.10` allegement notification, `sese.029.001.06` allegement removal, `semt.020.001.07` message cancellation advice and `sese.032.001.11` "Realignment" generation notification. This confirms the message identity and version but adds no field content.

---

## 2. The closest documented substitute: the exhaustive matching-field list

This is functional field content, **not** XML element names or cardinalities.

**Documented requirement.** `[[t2s-matching]]` UDFS R2026.JUN, §1.6.1.2, PDF 267–271, Diagrams 55–57 and footnote 194 (version R2026.JUN; English; section reviewed 2026-09-13; platform release R2026.JUN; LIMITATIONS: "Functional matrix only; no production XML/XSD validation or local interface certification" and "Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD"). The reviewed transcription records `production_schema_validated: false`.

Mandatory matching fields (Diagram 55, PDF 269) — 13 rows; the diagram's own transaction-type headers read **DVP/DWP** and **FOP**, and I keep those labels rather than normalising them:

| Matching field (source wording) | DVP/DWP | FOP |
|---|---|---|
| Payment Type | mandatory | mandatory |
| Securities Movement Type | mandatory | mandatory |
| ISIN Code | mandatory | mandatory |
| Trade Date | mandatory | mandatory |
| Settlement Quantity | mandatory | mandatory |
| Intended Settlement Date | mandatory | mandatory |
| Delivering Party BIC | mandatory | mandatory |
| Receiving Party BIC | mandatory | mandatory |
| CSD of the Delivering Party | mandatory | mandatory |
| CSD of the Receiving Party | mandatory | mandatory |
| Currency | mandatory | n/a |
| Settlement Amount | mandatory | n/a |
| Credit/Debit | mandatory | n/a |

Additional matching fields (Diagram 56, PDF 270): Opt-out ISO transaction condition indicator and CUM/EX Indicator for both transaction types; Currency, Settlement Amount and Credit/Debit as additional fields for FOP. Optional matching fields (Diagram 57, PDF 270): Common Trade Reference, Client of delivering CSD participant, Client of receiving CSD participant, Securities account of the delivering party, Securities account of the receiving party.

Conditions that travel with these rows **Documented requirement** `[[t2s-matching]]`: mandatory fields "must be present in the instruction" and must carry the same value on both sides, except Settlement Amount for DVP/PFOD where a tolerance may apply and except Credit/Debit (CRDT/DBIT) and Securities Movement Type (DELI/RECE), which match opposite; an additional field filled by one counterparty must be filled and match on the other side, while blank/blank matches; an optional field may match a blank field, but two filled values must match; footnote 194 — upper- and lower-case letters are treated as different, so values must not be case-normalised before comparison; Diagram 56 note — CUM/EX matching considers only ExCoupon and CumCoupon, other values are treated as blank; Diagram 57 note — client fields match BICs or proprietary codes (Identification, Issuer, Scheme Name), and a BIC does not match a proprietary code.

**Reasoned inference:** "mandatory matching field" is a matching-process obligation, derived from §1.6.1.2.3; it is not the same statement as an XSD element being declared with a minimum occurrence of one, and the two lists must not be equated. **Explanation (background, not a documented requirement):** a matching field is a settlement detail that T2S compares between the two sides of a trade before the instructions can be considered matched.

---

## 3. Milan-specific: the published X-TRM-to-T2S field correspondence

**Documented requirement.** `[[milan-xtrm-field-mapping]]` Instructions to Settlement Service and related instrumental activities — in force as of 30 June 2025, §3.4.1 Table 2 and the additional-information list, PDF 39–41 (printed 35–37); version "Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025)"; body language English but the **authoritative language is Italian and the Italian text prevails** (cover, PDF 1) — the English wording is an uneven translation and quoted terms follow the source; reviewed **14 September 2026**; approval: source identity checked, no independent whole-edition supervisory approval certification.

LIMITATIONS that travel with every use of this table: it is **functional correspondence only — not the A2A/RNI message layouts, not a T2S XSD**; two source cells are truncated in the original layout ("this fields will be fill…", "CUM / Ex…") and the truncated wording is preserved, not completed; the footnote marker (1) appears on two rows but the footnote text was not located on the reviewed pages.

The table's own type semantics: **Mandatory** = "mandatory information (if not specified can assume default values)"; **Additional** = if specified by one counterparty it becomes a mandatory feedback field for the other; **Optional** = a feedback field required only if specified by both counterparties.

Rows typed **Mandatory** (13): Issuer → Delivering / Receiving Party BIC (based on Securities Movement Type); Counterparty → Delivering / Receiving Party BIC (based on Securities Movement Type); Code of System Custody Issuer → CSD of Delivering / Receiving Party; Code of System Custody Counterparty (footnote 1 marker) → CSD of Delivering / Receiving Party; Settlement Date → Intended Settlement Date (default cell blank as printed); Data Executed → Trade Date (default "Date of release of the contract in X-TRM"); Object Code Negotiated → ISIN; Quantity → Settlement Quantity; Countervalue → Settlement Amount; Settlement Currency → Currency; Mark → Securities Movement Type; Countervalue Verse → Credit / Debit Indicator; and one row with X-TRM field "n.a." mapping to "Payment Type" whose cell text is truncated in the original layout. All other defaults in these rows print "NO".

Rows typed **Additional** (2): Settlement Transaction Condition (footnote 1 marker) → Settlement Transaction Condition (Opt Out); Trade Transaction Condition → Trade Transaction Condition (CUM / Ex — truncated cell).

Rows typed **Optional** (4): Beneficiary Issuer Code BIC and Beneficiary Counterpart Code BIC → Client of Delivering / Receiving Party; Common Trade Reference → Common Trade Reference; Counterpart Settlement Securities Account → Securities Account of Delivering / Receiving Party.

The same section also lists further information that *may* be specified in X-TRM: ISO code of the operation, partial settlement indicator, priority settlement indicator, indicator for the connection of settlement Instructions, indicator of the changeability of settlement instructions, Pool reference ID, Reference ID for Settlement Instructions, Reference ID for Settlement Restrictions, and the identification code for suspension, cancellation or modification of a settlement instruction.

**Reasoned inference:** Milan's "Mandatory" typing here is a business-content obligation on the X-TRM instruction, with defaults available, which is again not an XML cardinality. Note also that the Milan wording "mandatory information (if not specified can assume default values)" is weaker than the UDFS matching wording "must be present in the instruction"; the bundle does not reconcile the two, so I do not merge them.

---

## 4. What I am explicitly not doing

- **No element-level list.** No XML element names, paths, minimum/maximum occurrence figures, data types, formats, code lists, conditional rules or business-rule identifiers for `sese.023.001.11` are in the bundle. Writing any would be fabrication.
- **No schema-to-field mapping.** Neither the matching-field list nor the Milan table is mapped to XML elements in reviewed evidence; combining them into an element list would be an invented mapping.
- **No claim about a participant's actual interface.** ICP versus DCP status, service entitlements, account and ISIN eligibility are not in reviewed evidence.
- No production readiness, validation or certification is claimed for anything above.

Other sections returned by the bundle — `[[t2s-posting]]` (UDFS §1.6.1.8.1, PDF 303–304, reviewed 2026-09-13) and `[[t2s-realignment]]` (UDFS §1.6.1.10, PDF 373–376, reviewed 2026-09-13; LIMITATIONS: actual links/accounts and ISIN eligibility require verification; does not establish atomicity of an arbitrary two-security swap) — concern posting and realignment processing, not message field content, so they do not bear on this question.

---

## Open items

1. **T2S-specific schema and usage guideline for `sese.023.001.11`** — the only source that would establish mandatory elements and cardinalities. Blocked in this bundle: **GAP ID G14** ("MyStandards usage guidelines and XSDs require an account; T2S-native usage rules are not admitted field by field"). Official route: the MyStandards link printed by the UDFS at §3.3.6.4.2 for `sese.023.001.11_T2S`, which requires a MyStandards account.
2. **UDFS business-rules table (PDF 1235 onwards) and message examples** — not admitted per the LIMITATION on `[[t2s-sese023-scope]]`; would supply conditional rules and reason codes. Official route: the T2S UDFS R2026.JUN publication on the ECB T2S documentation pages.
3. **Milan's A2A / RNI message layouts ("Standard for X-TRM Users")** — expressly outside `[[milan-xtrm-field-mapping]]` per its LIMITATION; needed before any statement about what a Monte Titoli participant actually sends field by field. Official route: Milan's client documentation service (MT-X), which is client-only.
4. **The missing footnote (1) text** behind two Milan mandatory rows, and the two truncated Table 2 cells ("Payment Type — this fields will be fill…", "Trade Transaction Condition (CUM / Ex…") — not located on the reviewed pages; the Italian authoritative edition of the Instructions in force as of 30 June 2025 would resolve them.
5. **Client/participant data** — whether the participant in question is a DCP or an ICP, and its service entitlements; not in reviewed evidence and only obtainable from the participant's own contractual documentation with Euronext Securities Milan.
