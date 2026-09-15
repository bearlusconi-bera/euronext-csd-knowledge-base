# RNI G50 message layout for X-TRM instructions to Euronext Securities Milan (Monte Titoli)

## Direct answer

**I cannot give you the G50 layout.** The field-level layout of the RNI G50 message is not in reviewed evidence. The retrieval for the message-layout topic came back **blocked** (gap **G03**): *"Standard for X-TRM Users (A2A MT / RNI, VER.01.09) is client-only in MT-X; only the published field correspondence table is admitted."* No tag list, field order, lengths, cardinalities, formats or code values can be supplied from this bundle, and I will not reconstruct them from memory.

What the reviewed, public evidence does support is (1) that G50 exists as a printed message code and on which channel it is listed, (2) the functional field correspondence that an X-TRM instruction must carry (X-TRM field → T2S field, with type and default), and (3) the identity, version and location of the document that actually contains the layout.

## Retrieval statuses in this bundle

- Retrieval 1 (`milan_xtrm_message_layout`, Milan / settlement / participant / current): **blocked**, gap **G03** — the Standard for X-TRM Users is client-only in MT-X; only the published field correspondence table is admitted. This is the retrieval that would have carried your answer, and it is the reason the layout is withheld rather than approximated.
- Retrievals 2–5 (`milan_xtrm_field_mapping`, `milan_xtrm_service_access`, `milan_xtrm_standard_versions`, `milan_xtrm_lifecycle_maintenance`): **evidence_only**.

Routing note: this case was re-routed once by me to add the message-layout topic (which the index lists as blocked), the published field-mapping topic and the standard-versions topic, because the original contexts did not address the layout question at all.

## 1. Where G50 is printed — the access-method table

**Documented requirement.** Members may use interactive methods to access the X-TRM Service, and the "TECHNICAL TERMS OF USE" table lists, for the feature **"Acquisition/changing transactions"**, the codes **G50 and G51 in the "RNI F.T." column** and the same codes **G50 and G51 in the "SWIFT FileAct" column**; the "RNI M.S." column lists **G52 and G53**; "SWIFT FIN e/o InterAct" lists **MT540, MT541, MT542, MT543, MT548**; "MT-X/X-TRM On-line" is marked available ("X") with no code printed. For **"Results of operations transmission (ROM/ACB)"** the table prints **G56** under RNI F.T. and under SWIFT FileAct. For **"Alignment on-line system user"** it prints **G57 and G58** under RNI M.S. and **MT598, MT548** under SWIFT FIN e/o InterAct. An "X" marks availability of the feature on that channel as printed. [[milan-xtrm-service]] Instructions to Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025), §3.3 Access method, access-method table transcribed from rendered PDF 37 (printed 33); reviewed 14 September 2026 (2026-09-14); English body, **authoritative language Italian — the Italian text prevails (cover, PDF 1)**; source identity checked, no independent whole-edition supervisory approval certification.

Qualifications that travel with that row:

- LIMITATION: *"Message codes (G50–G58, MT540–MT548, MT598) are listed as printed; their layouts are in the client-only Standard for X-TRM Users."* This is the direct, source-level statement that your question cannot be answered from the Instructions.
- LIMITATION: the table's text extraction was column-garbled, so the **rendered page images are the reference** for the column-to-code assignment; the codes above follow that transcription.
- **Unresolved requirement:** the reviewed excerpts do **not** expand the abbreviations "RNI", "M.S." or "F.T.", and do not say which operation types (CVT, PCT/PCR, CTC) or which of "acquisition" versus "changing" each individual code carries. Any such mapping is not in reviewed evidence.

## 2. The closest published substitute — functional field correspondence (not a layout)

**Documented requirement.** Operations must contain all information indicated as mandatory in Table 2, "for convenience the related T2S field[s] are included". For matching purposes T2S distinguishes **mandatory** information (if not specified, can assume default values), **additional** optional information (if specified by one counterparty it is considered a mandatory feedback field and must also be specified by the other party) and **optional** information (feedback fields required only if specified by both counterparties). [[milan-xtrm-field-mapping]] Instructions to Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025), §3.4.1 Table 2 and additional-information list, PDF 39–41 (printed 35–37), transcribed from the rendered page images; reviewed 14 September 2026; English body, **authoritative language Italian, Italian text prevails**; source identity checked, no independent whole-edition supervisory approval certification.

| X-TRM field (as printed) | T2S field (as printed) | Type | Default |
|---|---|---|---|
| Issuer | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO |
| Counterparty | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO |
| Code of System Custody Issuer | CSD of Delivering / Receiving Party (based on Securities Movement Type) | Mandatory | NO |
| Code of System Custody Counterparty (footnote 1 marker) | CSD of Delivering / Receiving Party (based on Securities Movement Type) | Mandatory | NO |
| Settlement Date | Intended Settlement Date | Mandatory | (blank as printed) |
| Data Executed | Trade Date | Mandatory | Date of release of the contract in X-TRM |
| Object Code Negotiated | ISIN | Mandatory | NO |
| Quantity | Settlement Quantity | Mandatory | NO |
| Countervalue | Settlement Amount | Mandatory | NO |
| Settlement Currency | Currency | Mandatory | NO |
| Mark | Securities Movement Type | Mandatory | NO |
| Countervalue Verse | Credit / Debit Indicator | Mandatory | NO |
| n.a. | Payment Type ("this fields will be fill…" — cell truncated in the original layout) | Mandatory | NO |
| Settlement Transaction Condition (footnote 1 marker) | Settlement Transaction Condition (Opt Out) | Additional | NO |
| Trade Transaction Condition | Trade Transaction Condition ("CUM / Ex…" — cell truncated in the original layout) | Additional | NO |
| Beneficiary Issuer Code BIC | Client of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |
| Beneficiary Counterpart Code BIC | Client of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |
| Common Trade Reference | Common Trade Reference | Optional | NO |
| Counterpart Settlement Securities Account | Securities Account of Delivering / Receiving Party (based on Securities Movement Type) | Optional | NO |

Counts as transcribed: 13 mandatory, 2 additional, 4 optional. [[milan-xtrm-field-mapping]] §3.4.1 Table 2, PDF 39–41; reviewed 14 September 2026.

**Documented requirement.** In addition, X-TRM allows the following additional information to be specified: ISO code of the operation; partial settlement indicator; priority settlement indicator; indicator for the connection of settlement instructions; indicator of the changeability of settlement instructions; identification code of the "pool" of settlement ("Pool reference ID"); identification code of the associated settlement instructions ("Reference ID for Settlement Instructions"); identification code of settlement restrictions ("Reference ID for Settlement Restrictions"); identification code for the suspension, cancellation or modification of a settlement instruction. [[milan-xtrm-field-mapping]] §3.4.1 additional-information list, PDF 41 (printed 37); reviewed 14 September 2026.

Qualifications that travel with this table — they are the reason it is **not** an answer to your question:

- LIMITATION: *"Functional correspondence only: not the A2A/RNI message layouts, not a T2S XSD, and two source cells are truncated in the original layout (recorded)."* The section's own scope note repeats this: it is the correspondence "as published by Milan for ICP/X-TRM users. Not the client-only Standard for X-TRM Users message layouts; not a production XSD; not certification of T2S message paths."
- LIMITATION: footnote (1) is referenced on two rows but its text was not located on the reviewed pages — so whatever condition it attaches to "Code of System Custody Counterparty" and "Settlement Transaction Condition" is unknown.
- Two T2S-field cells are visibly truncated in the source and are preserved truncated, not completed.
- LIMITATION: Italian text prevails; English translation with uneven wording, quoted terms follow the source.

**Reasoned inference** (derived from the two limitations above plus the §3.3 limitation): the published material tells you *what information* an X-TRM instruction must convey and how each item maps to a T2S field, but not *how to encode it* in a G50 record. Nothing in the bundle states the relationship between a Table 2 row and a G50 field position, so do not treat the table row order as a layout.

## 3. The document that does contain the layout, and its version identity

**Documented requirement.** Notice **ON_11/2026 of 10 April 2026** informs all participants that the *"Standards for XTRM Users in A2A and RNI Mode"* documentation had to be updated for the Unfreeze ISO20022 and Clearing Bond and Repo Migration projects, with the technical documentation in Italian and English in track-changes mode available on **MT-X** in the folders *"Docs > Live Services > Technical Documentation > Under Review > Clearing Bond and Repo Migration"* and *"Docs > Live Services > Technical Documentation > Under Review > Unfreeze ISO 20022"*. The documents listed as updated are: *ES-MIL-A2A X-TRM Standard per utente X-TRM modalità MT A2A VER.01.09 ENG (TC)*; *ES-MIL-A2A … VER.01.09 ITA (TC)*; and — the one relevant to your question — ***ES-MIL-RNI X-TRM Standard per utente X-TRM modalità RNI VER.01.09 ITA (TC)***. The notice prints MT-T2S-TEST@euronext.com as the address for clarification requests. [[milan-xtrm-standard-versions]] ON_11/2026 "Update Standards for XTRM Users in A2A and RNI mode", 10 April 2026, PDF 1–2; reviewed 14 September 2026; English body, **authoritative language Italian, translation — authoritative language differs**; source identity checked, no independent whole-edition supervisory approval certification.

**Documented requirement.** Notice **ON_36/2026 of 11 September 2026** states that, starting **30 November 2026 and subject to successful testing**, new sources and market identifiers will be released for Vorvel, Certificates TLX and IPO markets, with the updates shown in track changes in the document *"Standard for Users X-TRM A2A and RNI mode"*, available on the MT-X platform in *"Documentation – Live Services – Technical Documentation – Under review – Market Request"*; the printed clarification address is MT-helpdesk.settlement@euronext.com. [[milan-xtrm-standard-versions]] ON_36/2026, 11 September 2026, PDF 1; reviewed 14 September 2026; English body, **authoritative language not independently established**; source identity checked, no independent whole-edition supervisory approval certification.

Qualifications:

- LIMITATION: *"Identifies document titles, versions and MT-X folders only; the standards' content is client-only (gap G03)."* Knowing that VER.01.09 exists does not put any of its fields into reviewed evidence.
- LIMITATION: operational/market notices are English communications by Euronext Securities Milan; they are **not** the Service Regulations or the Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite being published. This section's applicability basis is a *reference description* of documents (modes: reference / future), not a statement of current operative content.
- LIMITATION: the ON_36/2026 changes **take effect 30 November 2026 subject to testing** — that is a planned change, not a deployed one, and as at the 14 September 2026 review date nothing in the bundle says it has been released.
- **Unresolved requirement:** the bundle does not establish whether VER.01.09 is the version currently in force for RNI mode, whether the April 2026 "Under Review" drafts were finalised, or whether a later version now supersedes them. ON_11/2026 lists the RNI-mode standard only in an **ITA** variant (the A2A standard is listed in both ENG and ITA); whether an English RNI edition exists is not in reviewed evidence.

## 4. Process context for a G50-carried instruction (what the published rules do say)

**Documented requirement**, useful when you eventually read the layout: an operation entered into X-TRM undergoes **validation** (formal, logical and congruency checks; a rejection message is sent to the entering party if it fails) and then **valorisation/"enrichment"**, which adds database data (party relationships, securities account, other defaults) and calculated values; valorisation is performed only if validation found no errors. Once valorised, X-TRM forwards the instruction to the Settlement Service either in **batch** before the start of the night-time settlement phase or in **real time** during X-TRM opening hours; OTC transactions are sent in real time because they must be matched. T2S then applies its own validation, and only if the instruction also passes T2S validation does X-TRM assign a unique **reference code (reference ID)** and send an acceptance message. For modifications, in addition to all the data of the operation the operator must also provide the reference code given by X-TRM at entry, and participants may modify only the partialisation indicator, settlement priority and linkage blocks; anything else requires deletion and re-entry. [[milan-xtrm-lifecycle]] Instructions to Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025), §§3.4.2–3.4.7, PDF 41–47 (printed 37–43); reviewed 14 September 2026; English body, **authoritative language Italian, Italian text prevails**; source identity checked, no independent whole-edition supervisory approval certification. LIMITATION: market/CCP-specific maintenance permissions are published in Service Notices, which are not admitted to this library.

**Proposed design choice** (yours to make, not an infrastructure rule): if you are scoping an integration now, build the functional payload from the Table 2 correspondence and the additional-information list, and treat the physical encoding — record structure, field positions, lengths, formats and code values — as an open dependency to be closed against the RNI standard before any development, since no substitute for it exists in public documentation.

## 5. What is explicitly *not* available (all Unresolved requirement)

- The G50 record layout: field names, order, offsets/lengths, data types, cardinalities, mandatory/optional flags at message level, code lists and reason codes.
- Which G-code applies to entry versus amendment versus cancellation, and the header/trailer or file envelope conventions of RNI F.T.
- Any example message. I will not produce an illustrative G50 record: an invented example of a fixed-format client interface would be indistinguishable from a production artefact.
- The expansion and technical meaning of "RNI", "M.S." and "F.T." as used in §3.3.

## Open items

1. **Gap G03 — Standard for X-TRM Users, RNI mode.** Required document: *ES-MIL-RNI X-TRM Standard per utente X-TRM modalità RNI* (VER.01.09 per ON_11/2026, plus any later version), which is client-only. Official route: the **MT-X platform**, folders *"Docs > Live Services > Technical Documentation"* — "Under Review > Unfreeze ISO 20022" and "Under Review > Clearing Bond and Repo Migration" per ON_11/2026, and "Under review > Market Request" per ON_36/2026 — accessed under your firm's X-TRM participant entitlements; the notices print MT-T2S-TEST@euronext.com and MT-helpdesk.settlement@euronext.com as the clarification addresses. I have not contacted anyone and am not drafting any request.
2. **Version currency.** Confirm, from MT-X, which RNI-mode version is in force at your intended business date and whether an English edition exists; ON_11/2026 lists the RNI standard in ITA only, and the Italian text prevails for the Milan Instructions in any case.
3. **Footnote (1) of Table 2**, referenced on the "Code of System Custody Counterparty" and "Settlement Transaction Condition" rows, was not located on PDF 39–41; the qualifying condition is unknown.
4. **Two truncated Table 2 cells** ("Payment Type — this fields will be fill…", "Trade Transaction Condition — CUM / Ex…") need the Italian authoritative edition of the Instructions to complete.
5. **Service Notices** carrying market/CCP-specific permissions (maintenance functionality by market/CCP) are not admitted to this library; obtain them from Euronext Securities Milan's notice publication if they bear on your flows.
6. **Review date.** All statements above rest on evidence reviewed **14 September 2026 (2026-09-14)**; available review dates in this library are 2026-09-13 and 2026-09-14. Nothing here is asserted as verified after that date.
