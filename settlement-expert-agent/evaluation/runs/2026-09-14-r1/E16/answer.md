# What the UDFS says about the sese.023 building blocks "under R2026.NOV"

## Direct answer

**Unresolved requirement.** No reviewed evidence exists for what the **R2026.NOV** UDFS says about the building blocks of the sese.023 settlement instruction. Both retrievals that asked for message content at release R2026.NOV returned **STATUS: blocked — "Requested release does not match the reviewed platform evidence" (GAP ID G15)**. The only R2026.NOV material admitted in this bundle is cover-page publication evidence, a maintainer-produced text comparison of sixteen *other* settlement sections, and Milan's deployment plan. None of them reaches the catalogue-of-messages chapter.

The building-block outline that exists in reviewed evidence is the **R2026.JUN** one. I set it out below labelled as June, because relabelling a June snapshot as the November text would be exactly the error the release scoping is there to prevent.

**Retrieval statuses in this bundle (7 retrievals):**

| # | Context | Status |
|---|---|---|
| 1 | T2S, settlement, participant, current, `t2s_message_sese023_scope`, release **R2026.NOV**, as of 2026-09-14 | **blocked** — requested release does not match the reviewed platform evidence; **GAP ID G15** |
| 2 | T2S, settlement, participant, current, `native_message_overview`, release **R2026.NOV**, as of 2026-09-13 | **blocked** — same reason; **GAP ID G15** |
| 3 | T2S, `t2s_message_sese023_scope`, release R2026.JUN | evidence_only |
| 4 | T2S, `native_message_overview`, release R2026.JUN | evidence_only |
| 5 | T2S, reference, `release_status`, release R2026.NOV | evidence_only |
| 6 | T2S, reference, `november_text_comparison` | evidence_only |
| 7 | Milan, future, `milan_t2s_release_plan_nov` | evidence_only |

---

## 1. What is documented about R2026.NOV itself

**Documented requirement.** `[[november-final-release]]` — Cover Note "Delivery of the T2S UDFS R2026.NOV and UHB R2026.NOV", PDF page 1, dated **14 September 2026**; and the T2S UDFS R2026.NOV cover page carrying the document date **11 September 2026**. Version: R2026.NOV final publication, no production-deployment certification. English original; applicability basis: reference description; section reviewed **14 September 2026**.

The cover note states that final versions of the UDFS R2026.NOV, UHB, GFS, DMT, URD, BFD and the BDM/BILL/CRDM/ESMIG UDFS and handbooks have been published; that "all changes in the documents were highlighted in revision marks" with CR references added; that draft intermediate versions were published on 31 July 2026 and reviewed from 3 to 21 August 2026; that the new versions incorporate the Change Requests in scope of Release 2026.NOV including editorial CRs approved by the CSD Steering Group until 23 July 2026; that the exhaustive list of Change Requests is **Annex A**; and that a list of all T2S messages with their MyStandards links is **Annex B**.

LIMITATIONS that travel with every one of those statements `[[november-final-release]]`: final publication is established but **November production deployment is not verified**; the 14 September cover/listing date, the 11 September UDFS document date and the earlier target are **separate facts**; and **only cover-page statements are admitted — no November operational provisions, payloads or changed message versions are admitted**.

Two consequences follow directly and both matter for this question:

- **Documented requirement / Unresolved requirement.** Annexes A and B — the exhaustive Change Request list and the message-to-MyStandards list — are named by the cover note but are **not in reviewed evidence**. They are precisely the artefacts that would show whether the sese.023 chapter changed and which message version R2026.NOV carries.
- **Unresolved requirement.** Whether R2026.NOV still uses the message version `sese.023.001.11` is **not established**; the section's own LIMITATION excludes changed message versions. I will not carry the June version number into a November statement.

**Documented requirement (dates are facts, not deployment).** Publication is not deployment. R2026.NOV is published in final form; it has not been shown to be running in production by any evidence in this bundle.

---

## 2. What the June-versus-November comparison covers — and why it does not answer this question

**Documented requirement.** `[[november-text-comparison]]` — "T2S User Detailed Functional Specifications R2026.NOV (UDFS) — full-text derivative", derived comparison of the June and November clean UDFS texts; version R2026.NOV final publication (11 September 2026), deployment not verified; English; applicability basis: reference description; section reviewed **14 September 2026**; approval: source identity checked, no independent whole-edition supervisory approval certification.

LIMITATIONS `[[november-text-comparison]]`: it is **a derivative produced by the library maintainer, not ECB text** — a textual comparison after normalisation, with diagrams and image tables not compared, and residual differences treated as formatting artefacts unless stated otherwise; **no sentence-level substantive change was detected in the compared ranges**; and **the comparison does not review the change requests actually delivered by R2026.NOV** (Milan lists 11 change requests and six defects in ON_28/2026).

The compared ranges are these sixteen settlement sections only: matching, allegement, instruction amendment, instruction cancellation, hold and release, instructions recycling, posting overview, partial settlement, realignment concept, linked instructions, conditional settlement (CoSD), status management, T2S schedule, real-time settlement (RTS) phase, business validation and night-time settlement (NTS) processing.

**Documented requirement:** the **catalogue-of-messages chapter that contains the sese.023 building-block outline is not among the compared sections.** The comparison therefore says nothing about it, in either direction. Reading its "no substantive change detected" verdict as covering sese.023 would be a misuse of the derivative.

**Reasoned inference** (derived from the heading pairs recorded in the comparison, nothing else): the November edition renumbers the compared chapters — June §1.6.1.2 Matching appears as November §3.6.1.2, June §1.4.2 T2S schedule as November §3.4.2, and so on across all sixteen pairs, with page ranges shifted (for example Matching at June PDF 267–272 versus November PDF 279–284). It follows that **even the November locator of the sese.023 chapter is not established** — the June locator §3.3.6.4 must not be quoted as the November one. The comparison also records sentence-count and similarity differences that are attributed to formatting (figure/table caption restyling, dropped cross-reference page numbers, footnote repositioning), not to substance, within the compared ranges only.

---

## 3. The building-block outline that *is* in reviewed evidence — R2026.JUN

**Documented requirement.** `[[t2s-sese023-scope]]` — T2S User Detailed Functional Specifications **R2026.JUN** (UDFS), §3.3.6.4.1–3.3.6.4.2 "Overview and scope of the message" / "The T2S-specific schema", **PDF 1233–1234**; version R2026.JUN; English, no authoritative language independently established; **platform release R2026.JUN**; source reviewed 2026-09-13, section reviewed **14 September 2026**; approval: source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS: the business-rules table (PDF 1235 onwards) and the message examples are **not admitted**, and the T2S-specific schema is published on MyStandards which requires an account; and this is the **CSD/DCP-to-T2S message, not a bank-to-CSD interface**.

Scope statement (R2026.JUN): the SecuritiesSettlementTransactionInstructionV11, known as a Settlement Instruction within T2S, is sent by a CSD or a directly connected T2S party to T2S, and allows the instructing party to request a transfer of securities relating to a securities transaction (for example an OTC trade, a corporate action, a repo), with or without a cash payment. In response, T2S sends `sese.024.001.12` when validation, matching and settlement are carried out, and `sese.025.001.11` when settlement is successful.

Building blocks as the June UDFS describes them — **all of the following are R2026.JUN statements, none is a November statement**:

| Building block (UDFS spelling) | R2026.JUN wording | Content |
|---|---|---|
| Transaction Identification | mandatory, not repetitive | identification assigned by the instructing party to uniquely and unambiguously identify the transaction |
| SettlementTypeAndAdditionalParameters | mandatory, non repetitive | settlement type and identification information |
| NumberCounts | optional, non repetitive | number of transactions linked |
| Linkages | optional, repetitive | links instructions and specifies settlement sequences (after/before/with etc.) |
| TradeDetails | mandatory, non repetitive | detailed information related to the Settlement Instruction |
| FinancialInstrumentIdentification | mandatory, non repetitive | identifies the financial instrument being settled |
| FinancialInstrumentAttributes | "not required in T2S" | elements characterising the financial instrument |
| QuantityAndAccountDetails | mandatory, non repetitive | account and quantity details |
| SettlementParameters | mandatory, non repetitive | conditions that must be fulfilled before the transaction can settle, defined by the instructing party in compliance with the settlement rules of the market of settlement |
| DeliveringSettlementParties | optional, non repetitive | chain of delivering settlement parties |
| ReceivingSettlementParties | optional, non repetitive | chain of receiving settlement parties |
| CashParties | optional, non repetitive | cash parties, if different from the securities settlement parties |
| SettlementAmount | optional, non repetitive | total amount of money to be paid or received in exchange for the securities |
| OtherAmounts | "not required in T2S" | amounts other than the settlement amount |
| OtherBusinessParties | "not required in T2S" | other business parties relevant to the transaction |
| AdditionalPhysicalOrRegistrationDetails | "not required in T2S" | information for registration or physical settlement |

The June UDFS also states that the T2S-specific schema, the HTML/PDF documentation and the message examples are provided outside the UDFS under the MyStandards link printed at §3.3.6.4.2 for the T2S flavour of the message.

**Documented requirement.** `[[t2s-messages]]` — UDFS R2026.JUN §2.3.8, PDF 778 (section reviewed 2026-09-13; platform release R2026.JUN; LIMITATIONS: T2S-native messages, not bank-to-local-CSD formats, and subscriptions and privileges affect recipients; no production payload or full schema admitted) records `sese.023.001.11` as the single inbound message of the Send Settlement Instruction dialogue, with `sese.024.001.12` status advices, `sese.025.001.11` confirmations, `sese.028.001.10` allegement notification, `sese.029.001.06` allegement removal advice, `semt.020.001.07` message cancellation advice and `sese.032.001.11` realignment generation notification as outbound messages. Again: **R2026.JUN**.

**Reasoned inference:** because the November comparison never touched the catalogue of messages and the November cover-page evidence excludes payloads and changed message versions, nothing in this bundle supports carrying the June building-block list forward to R2026.NOV — neither as unchanged nor as changed. The honest statement is that the November text has not been reviewed for this chapter.

The two remaining R2026.JUN sections in the bundle, `[[t2s-posting]]` (UDFS §1.6.1.8.1 and overview paragraph, PDF 303–304, reviewed 2026-09-13) and `[[t2s-realignment]]` (UDFS §1.6.1.10, PDF 373–376, reviewed 2026-09-13; LIMITATIONS: actual links, accounts and ISIN eligibility require verification; does not establish atomicity of an arbitrary two-security swap), describe posting and realignment processing rather than the message's building blocks, so they do not bear on this question.

---

## 4. Milan's R2026.NOV plan — planned dates, not deployment

**Documented requirement.** `[[milan-r2026nov-plan]]` — ON_28/2026 "T2S Release R2026.NOV and Non-binding XSDs" (21 July 2026), PDF 1–2, and the operational notice "T2S Release R2026.NOV and binding XSDs" dated 10 August 2026 (hub date 07/08/2026), PDF 1–2. Body language English, **authoritative language Italian — these are translations and the Italian text governs**; applicability basis: reference description; subject release R2026.NOV; reviewed **14 September 2026**; approval: source identity checked, no independent whole-edition supervisory approval certification.

LIMITATIONS `[[milan-r2026nov-plan]]`: these are **operational/market notices — English communications by Euronext Securities Milan, not the Service Regulations or Instructions** — and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication; **planned dates are not deployment evidence**, and ON_28 page 2 contains an internal inconsistency ("from Tuesday 29 April" for the UTEST re-tests) preserved as printed; the MyStandards XSD documentation is **client-only**.

What the notices state: R2026.NOV will be available in the external test environment (UTEST) on 28 September 2026; external tests for participants using ES-MIL systems may run from 28 September to 28 October 2026; DCPs are invited to retest defects and change requests applicable to their operational model; the release **comprises 11 change requests (CR-0798, CR-0828, CR-0840, CR-0841, CR-0842, CR-0843, CR-0850, CR-0854, CR-0856, CR-0859, T2S-CHN-003) and the resolution of six defects**; and the release "will be deployed in production on 14 November, effective from 16 November 2026". Non-binding XSD documentation ("MyStandard Link_non_binding XSD_T2S-CoCo UDFS R2026.nov") and later binding XSD documentation ("MyStandard Link_binding XSD_T2S-CoCo UDFS R2026-nov") are placed in the MT-X documentation folder for the release.

**Reasoned inference / observed anomalies**, derived from the excerpts themselves: ON_28 page 2 dates the ES-MIL UTEST re-tests "from Tuesday 29 April" while the later 10 August notice dates the same re-tests "from Tuesday 28 September"; and the "Relevant documentation" paragraph of both notices names the declaration form with a **R2026.JUN** prefix while the body of the same notices names it with a R2026.NOV prefix. These are preserved as printed and not reconciled.

**Unresolved requirement.** Whether any of the eleven change requests or six defects touches the sese.023 message, its building blocks or its version is **not in reviewed evidence**; the change-request contents are not admitted anywhere in this bundle.

---

## 5. What I am not doing

- I am not presenting the R2026.JUN building-block list as the R2026.NOV list, and not asserting that it is unchanged.
- I am not quoting a November locator, page range or message version for the sese.023 chapter.
- I am not inferring sese.023 content from the "no substantive change detected" verdict, which applies only to sixteen other sections and is a maintainer-produced derivative, not ECB text.
- I am not treating the published November documentation as a deployed platform state.
- No validation, certification or production readiness is claimed for anything above.

---

## Open items

1. **The R2026.NOV UDFS catalogue-of-messages chapter for sese.023** — the only source that answers the question as asked. Blocked in this bundle: **GAP ID G15** ("Requested release does not match the reviewed platform evidence"; R2026.NOV operational provisions are unreviewed and the release is not deployed). Official route: the T2S UDFS R2026.NOV final publication on the ECB T2S documentation pages, read for the message chapter and its revision marks.
2. **Annex A to the R2026.NOV cover note** — the exhaustive Change Request list, named by `[[november-final-release]]` but not admitted; needed to establish whether any CR in R2026.NOV changes the sese.023 message.
3. **Annex B to the R2026.NOV cover note** — the list of all T2S messages with their MyStandards links; needed to establish the message version carried by R2026.NOV. Official route: the MyStandards entry for the T2S flavour of the message, which requires a MyStandards account.
4. **The R2026.NOV binding XSD documentation** — named in Milan's 10 August 2026 notice and placed in the MT-X documentation folder; **client-only**, so it is reachable only through Milan's client documentation service (MT-X).
5. **Confirmation of actual deployment** — production deployment on the planned dates is not verified by any evidence here; it would need the post-deployment operational notice or the T2S release confirmation, read after the event.
