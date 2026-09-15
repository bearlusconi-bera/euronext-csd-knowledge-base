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
