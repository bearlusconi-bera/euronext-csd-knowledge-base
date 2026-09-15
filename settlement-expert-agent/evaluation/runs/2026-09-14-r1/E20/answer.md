# Copenhagen (VP) DCP go-live: which test cases must be passed

## Direct answer

**Unresolved requirement — the test cases cannot be listed.** The Copenhagen DCP User Guidelines are not in reviewed evidence, and the retrieval aimed at them returned **blocked**. What the reviewed rulebook does establish is the *obligation structure*: you must hold a valid Eurosystem T2S certification, whose test scenarios are defined solely by the Eurosystem (not by VP), and you must additionally perform all acts and tests reasonably requested by VP or the Eurosystem, successfully and to their satisfaction. The individual test cases sitting behind those obligations are named in documents this bundle does not contain. (DCP — directly connected participant: a participant that sends instructions straight to the T2S platform rather than through the CSD; ICP — indirectly connected participant, which instructs via the CSD.)

## Retrieval statuses (disclosure)

| Retrieval | Context | Status | Consequence |
|---|---|---|---|
| 1 | Copenhagen / settlement / current / `copenhagen_dcp_entitlements` | **blocked** — gap **G10** | Retriever reason: "Copenhagen DCP User Guidelines and accepted service tests are not public; Part 5 states requirements only." No test-case list, no acceptance criteria per test, no service-entitlement matrix is admitted. |
| 2 | Copenhagen / settlement / current / `dcp_admission` (as of 13 September 2026) | evidence_only | Supports the certification and testing *obligations* in Part 5. |
| 3 | Copenhagen / settlement / current / `copenhagen_t2s_settlement` (as of 14 September 2026) | evidence_only | Supports the access rule that DCP status requires a separate agreement with VP. |

Any count, name, identifier or pass/fail threshold of a specific test case would be fabrication and is therefore absent from this answer.

## Documented requirements (what you must satisfy, from the reviewed rulebook)

All rows below rest on [[copenhagen-dcp]] Euronext Securities Copenhagen VP Rule Book Part 5 — T2S DCP Service Rules, §§1–3, PDF 2–3, Version 01, published August 2023 and still linked in the current rulebook; section reviewed 13 September 2026, source reviewed 13 September 2026; applicability basis is **publication_description** — this is a qualified description of the **published** requirements at the review date, the operative **effective date** is **not established**, and it does not certify current legal applicability; body language English, no authoritative language independently established; source identity checked, with no independent whole-edition supervisory approval certification.

| # | Obligation | Label | Locator |
|---|---|---|---|
| 1 | The Participant must be in possession of a valid T2S certification received from the Eurosystem. | Documented requirement | Part 5 §2.3 |
| 2 | For that purpose the Participant must perform such Eurosystem certification tests and other acts as required by the Eurosystem from time to time (the clause cross-refers to clause 4, which is **not in the reviewed excerpt**). | Documented requirement | Part 5 §2.3 |
| 3 | The test scenarios are identical for all markets and are **solely defined by the Eurosystem**, but may vary depending on the connectivity channel used, on the Participant's plans to connect to multiple CSDs, and similar factors. | Documented requirement | Part 5 §2.3 |
| 4 | Obtaining and maintaining the T2S certificate is solely the Participant's responsibility. | Documented requirement | Part 5 §2.4 |
| 5 | The Participant must perform all such acts and tests as may be reasonably requested by VP or the Eurosystem from time to time; the tests must be performed successfully to a level satisfactory for VP or the Eurosystem, as the case may be. | Documented requirement | Part 5 §3.3 |
| 6 | The Participant must have signed a Participation Agreement with VP for access as Settlement Participant and is bound by the same terms as an ICP-only Participant unless the DCP Rules provide otherwise; where the DCP Rules and other parts of the Participation Agreement are inconsistent, the DCP Rules prevail. | Documented requirement | Part 5 §§1.2, 3.1 |
| 7 | The Participant must connect to T2S using the technical connection and communication interface set forth by the Eurosystem or VP from time to time. | Documented requirement | Part 5 §3.2 |
| 8 | VP's set-up to T2S has VP-specific technical characteristics with which the Participant must comply; these are **further described in the User Guidelines**. | Documented requirement (content of the characteristics: **not in reviewed evidence**) | Part 5 §3.5 |
| 9 | Authorisation covers the securities-related services, privileges and T2S functions described in the User Guidelines, and the message types and transaction types specified in the form "Request for DCP-access to T2S". | Documented requirement (the service list, the message types and the form itself: **not in reviewed evidence**) | Part 5 §2.1 |
| 10 | Being a DCP via VP may differ from other markets in available services and functions and in the **acts and tests to be conducted**. | Documented requirement | Part 5 §2.2 |
| 11 | The Participant may run its own tests; VP assists on a best-effort basis only. | Documented requirement | Part 5 §3.4 |
| 12 | VP may request such information, documents and assurances as it may reasonably require, to ensure the Participant's IT platform does not harm T2S. | Documented requirement | Part 5 §3.6 |

**Documented requirement.** To become a DCP, a Settlement Participant must enter into a **separate agreement with VP**; a Settlement Participant may instruct a Transfer Order to T2S either via VP as an ICP or directly via the T2S platform as a DCP — [[copenhagen-t2s-settlement]] VP Rule Book Part 4 — Settlement Rules, §11.2.1, PDF 14–17, Version 13, version date 1 May 2025; section reviewed 14 September 2026, source reviewed 13 September 2026; English rulebook text, **Danish law governs the VP system** and no authoritative-language statement was reviewed; source identity checked, no independent whole-edition supervisory approval certification.

## Two "User Guidelines" — a terminology trap in your question

**Reasoned inference (derived from comparing [[copenhagen-dcp]] Part 5 §§2.1, 2.5, 3.5 with [[copenhagen-t2s-settlement]] Part 4 §11.1.1).** The phrase "User Guidelines" carries two different referents in this rulebook:

1. In Part 4 §11.1.1, "the T2S User Guidelines" is defined as the **T2S User Detailed Functional Specification and the T2S User Handbook** published on the ECB webpage. LIMITATION attached: the clause links an outdated T2S User Handbook URL (v2.1, 2015); the current UDFS sections should be used for platform mechanics, and neither the UDFS nor the UHB is in this bundle.
2. In Part 5 (§§2.1, 2.5, 3.5), "the User Guidelines" is the document describing **VP's own** set-up process, VP-specific technical characteristics and the DCP service scope.

Your question presumes a VP-issued "DCP User Guidelines" containing an enumerated test-case catalogue. The reviewed text does not show that such a catalogue exists there: Part 5 §2.3 places the *certification* test scenarios with the **Eurosystem**, while Part 5 §3.3 leaves VP's additional tests open-ended ("as may be reasonably requested … from time to time"). Whether the VP User Guidelines nevertheless enumerate named VP tests is **not in reviewed evidence** — this is an inference about where the requirement lives, not a finding that no list exists.

## Proposed design choices (for your go-live plan; not infrastructure rules)

- Split your test plan into two tracks that have different owners: the **Eurosystem certification track** (scenarios defined solely by the Eurosystem, varying with connectivity channel and multi-CSD ambitions per Part 5 §2.3) and the **VP acceptance track** (open-ended, satisfaction-based per Part 5 §3.3). Do not assume a single combined checklist.
- Because Part 5 §3.3 sets a satisfaction standard rather than an objective pass mark, obtain VP's written statement of what "successfully … to a level satisfactory" means for your scope **before** you baseline a go-live date. The rulebook gives you no entitlement to a fixed criterion.
- Record your connectivity channel and whether you will connect to multiple CSDs early: Part 5 §2.3 makes both of these variables that change the test scenarios that apply to you.

## Unresolved requirements

- The enumerated **test cases**, their identifiers, sequencing, environments, data prerequisites and pass criteria — **not in reviewed evidence** (blocked, gap G10).
- Part 5 **clause 4**, cross-referenced by §2.3 as the certification clause, is outside the reviewed excerpt — **not in reviewed evidence**.
- The **"Request for DCP-access to T2S" form** and the message types and transaction types it specifies — **not in reviewed evidence**; do not infer a message set from T2S documentation.
- The **service entitlements and privileges** a VP DCP receives, and the VP-specific technical characteristics of §3.5 — **not in reviewed evidence**.
- Whether the published Part 5 text is the version legally in force at your intended go-live date — **not established**; the section's applicability basis is a description of the published document at the review date, with no operative effective date established.

## Open items

1. **Gap G10 (blocked topic `copenhagen_dcp_entitlements`)** — the Copenhagen DCP User Guidelines and the accepted service tests are not public; Part 5 states requirements only. Needed: the VP DCP User Guidelines edition applicable at your go-live date, with its version and effective date.
2. **Eurosystem certification test scenarios** — per Part 5 §2.3 these are defined by the Eurosystem, not by VP; the scenario catalogue applicable to your connectivity channel is not in reviewed evidence and must come from the Eurosystem/ECB certification material.
3. **Part 5 clause 4 and the "Request for DCP-access to T2S" form** — both are referenced by the reviewed text but not contained in it.
4. **Effective-date confirmation** for VP Rule Book Part 5 (Version 01, published August 2023) and Part 4 (Version 13, 1 May 2025), since Part 5's operative effective date is not established in reviewed evidence.
5. **Official route** — request items 1–4 through the Euronext Securities Copenhagen client documentation/relationship channel for the non-public DCP material, and through the Eurosystem's T2S certification process for the certification scenarios. I do not draft or send that request.

Review dates of the evidence used: 13 September 2026 for the Part 5 DCP section, 14 September 2026 for the Part 4 T2S settlement section (both sourced from reviews dated 13 September 2026). Nothing here is asserted as verified beyond those dates.
