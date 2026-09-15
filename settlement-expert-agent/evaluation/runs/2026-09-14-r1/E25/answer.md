# Irrevocability, finality and the Moment of Entry for a T2S Transfer Order at Euronext Securities Copenhagen (VP)

## Direct answer

A Transfer Order instructed for T2S Settlement at VP becomes **irrevocable when T2S gives it the status "Matched"** — expressly irrespective of whether VP pre-matched it — and becomes **final (unconditional, irrevocable and enforceable) as from the credit account entry of the securities on the receiving Settlement Participant's securities account on the T2S platform**. VP's Pre-Match does not change either of those two moments; what it changes is the **Moment of Entry into the System**: a pre-matched order is deemed entered at the moment **VP** declared it compliant with the technical rules of T2S, while a non-pre-matched order is deemed entered only at the moment the **T2S platform** declared it compliant.

All five retrievals in the bundle returned **`evidence_only`**; no retrieval was `blocked`, `needs_context` or `needs_refresh`. Several LIMITATION lines do apply and are carried with the claims below.

---

## 1. The three moments, as documented

| # | Moment | Trigger in the reviewed text | Label |
|---|---|---|---|
| 1 | **Moment of Entry into the System** | Pre-matched order: when **VP** declared it compliant with the technical rules of T2S. Not pre-matched: when the **T2S platform** declared it compliant. | Documented requirement |
| 2 | **Moment of Irrevocability** | When the Transfer Order has been given the status **"Matched" on the T2S platform**, irrespective of whether it was pre-matched. | Documented requirement |
| 3 | **Moment of Settlement Finality** | As from the **account entry (credit)** of the securities on the receiving Settlement Participant's securities account **on the T2S platform**; the entry is thereafter mirrored in the VP Clearing and Settlement System. | Documented requirement |

**Documented requirement.** "A Transfer Order, which has been successfully validated and Pre-Matched, is deemed 'entered' into the VP Clearing and Settlement system at the moment at which it was declared compliant with the technical rules of T2S by VP (the Moment of Entry into the System for pre-matched Transfer Orders). Whereas a Transfer Order for T2S Settlement, that has not been Pre-Matched, but passed on to the T2S System, is deemed 'entered' into at the moment at which it has been declared compliant with the technical rules of T2S by the T2S platform" — [[copenhagen-t2s-settlement]] Euronext Securities Copenhagen, Part 4 – Settlement Rules (VP Rule Book Part 4), clause 11.6.7, PDF 16; version "Part 4 Settlement Rules: 1 May 2025" (page footer: Settlement Rules – Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; English rulebook text — Danish law governs the VP system and no authoritative-language statement was reviewed.

**Documented requirement.** Irrevocability: "When a Transfer Order has been given the status 'Matched' on the T2S platform, irrespectively of whether it has been Pre-Matched or not, the Transfer Order cannot unilaterally be cancelled or revoked (the Moment of Irrevocability)." From that moment and until settlement, **Hold & Release may still be applied by each party**, and **the parties may bilaterally agree to cancel** their Transfer Orders until settlement — [[copenhagen-t2s-settlement]] Part 4 – Settlement Rules, clause 11.7.1, PDF 16; version 1 May 2025 (Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; English text, Danish law governs, authoritative language not established.

**Documented requirement.** Finality: "A Transfer Order is finally settled (unconditional, irrevocable and enforceable) as from the account entry (credit) of the securities on the receiving Settlement Participant's Securities Account on the T2S platform (the Moment of Settlement Finality). The corresponding account entry will hereafter be mirrored in the VP Clearing and Settlement System." — [[copenhagen-t2s-settlement]] Part 4 – Settlement Rules, clause 11.8.2.1, PDF 17; version 1 May 2025 (Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; same language qualification.

**Documented requirement — matched is not settled.** A Transfer Order that has been matched but not settled for lack of coverage is handled under the recycling terms of the User Guidelines (clause 11.8.1.2, PDF 17), and an unmatched Transfer Order is handled under the T2S recycling terms (clause 11.7.1–11.7.2, PDF 16) — [[copenhagen-t2s-settlement]], version 1 May 2025 (Version 13); section reviewed 14 September 2026. Irrevocability at matching therefore does not by itself transfer the securities; only the account entry in step 3 does.

---

## 2. How the Pre-Match works and why it moves the Moment of Entry

**Documented requirement — sequence.** For a Transfer Order instructed for T2S Settlement:

1. **Validation by VP on receipt.** VP validates the order "in order to declare it compliant with the technical rules of T2S": first it verifies that the sending party is authorised to instruct via VP, then it applies the validation criteria and validates that the mandatory data fields are correctly filled in (clause 11.6.2, PDF 15).
2. **Rejection on failure.** An unsuccessful validation causes rejection, and information on the reason is generated and sent to the submitting party (clause 11.6.3, PDF 15).
3. **Pre-Match attempt.** "Upon a successful validation of a Transfer Order concerning a T2S Transfer, but prior to upload of the Transfer Order for entry in the match module on the T2S platform, VP will attempt to perform Match outside the T2S platform (a Pre-Match)" (clause 11.6.4, PDF 16).
4. **No pre-match → straight to T2S.** "In case of no pre-match, the Transfer Order is immediately passed on by VP to the T2S platform for Match in the T2S matching module" (clause 11.6.4).
5. **Successful pre-match → consolidated order.** "If the result of the Pre-Match is successful, VP will create a new consolidated Transfer Order to T2S for entry in the T2S match module as described in the User Guidelines" (clause 11.6.4).
6. **Legal basis for pre-matching.** "The right for VP to conduct Pre-Matches follows from an agreement (the Collective Agreement) with the ECB" (clause 11.6.5, PDF 16).

All of the above: [[copenhagen-t2s-settlement]] Part 4 – Settlement Rules, clauses 11.6.2–11.6.5, PDF 15–16; version 1 May 2025 (Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; English rulebook text, Danish law governs the VP system, no authoritative-language statement reviewed. LIMITATION carried: *pre-match by VP creates a consolidated already-matched instruction, and the moments of entry differ for pre-matched and non-pre-matched orders*.

**Reasoned inference (from clauses 11.6.2, 11.6.4 and 11.6.7 read in sequence).** Because VP's declaration of compliance (step 1) happens *before* the pre-match attempt (step 3) and before upload to T2S, a successful Pre-Match fixes the Moment of Entry **retrospectively at the earlier VP validation moment**, i.e. earlier in the chain than for an order that travels unmatched to T2S. The rulebook states the two moments; the ordering conclusion is my inference from the drafting sequence, not a separate sentence in the text.

**Reasoned inference (from clause 11.6.4 and T2S UDFS §1.6.1.2.2).** The consolidated Transfer Order that VP creates after a successful Pre-Match is the kind of instruction the platform treats as already matched: "T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. Instructions that enter into T2S as already matched are created with the matching fields as if they were matched in T2S (i.e. follow the same matching rules as in T2S)", and instructions with Match status "Matched" do not go through the T2S matching process — [[t2s-matching]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.2.2, PDF 268; version R2026.JUN; reviewed 13 September 2026; body language English, authoritative language not independently established; approval: source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS carried: functional matrix only — no production XML/XSD validation or local interface certification. The rulebook does not itself say that the consolidated order carries the ISO "already matched" indicator, so the mapping is inference, not a documented interface requirement.

**Documented requirement — why the Moment of Entry matters.** Entry is the hinge for insolvency treatment, not for transfer of title:
- Orders of an insolvent Settlement Participant that reached Moment of Entry **and** whose corresponding counterparty orders reached Moment of Entry **before** the opening of Insolvency Proceedings "will be attempted settled in the T2S system" (clause 11.8.3.2, PDF 17).
- Orders that reached Moment of Entry **after** the opening but were matched on the T2S platform before VP became aware, or should have been aware, of the opening, and are for settlement on the same T2S Business Day, "will be attempted settled in the T2S system, but will, however be cancelled if unsettled at the end of the day" (clause 11.8.3.3, PDF 17).
- All other Transfer Orders "will be immediately cancelled after VP becomes aware of the opening of the Insolvency Proceedings" (clause 11.8.3.4, PDF 17).

[[copenhagen-t2s-settlement]] Part 4 – Settlement Rules, clauses 11.8.3.1–11.8.3.6, PDF 17; version 1 May 2025 (Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; English text, Danish law governs.

**Reasoned inference.** Since VP's pre-match moves the Moment of Entry earlier (to VP's own compliance declaration), a pre-matched order of a participant heading into insolvency can satisfy the clause 11.8.3.2 test at a point in time at which a non-pre-matched order would not yet have entered. This follows from combining clauses 11.6.7 and 11.8.3.2; the rulebook does not draw the consequence itself.

---

## 3. Matching detail and the amount tolerance

**Documented requirement.** If the transaction amount instructed by the receiving Settlement Participant differs from that instructed by the delivering Settlement Participant, **the delivering participant's amount prevails**, provided the difference does not exceed the T2S tolerance match rules set out in the T2S User Guidelines — [[copenhagen-t2s-settlement]] Part 4 – Settlement Rules, clause 11.6.6, PDF 16; version 1 May 2025 (Version 13); section reviewed 14 September 2026; English text, Danish law governs.

**Documented requirement (platform side).** T2S checks the Settlement Amount difference against a configured tolerance amount with two bands per currency depending on the cash countervalue; the ECSDA proposal for **Euro** is EUR 2 for a countervalue ≤ EUR 100,000 and EUR 25 above EUR 100,000, and the same values appear as the standard/default parameter maintained by the T2S Operator. Where instructions with different Settlement Amounts match, the Matched Settlement Amount submitted for settlement is the amount indicated by the **deliverer** of the securities — [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3, Table 57 and §1.6.1.2.4, PDF 270–271; version R2026.JUN; reviewed 13 September 2026; English body text, authoritative language not independently established; no independent whole-edition supervisory approval certification. LIMITATIONS carried: functional matrix only, no production XML/XSD validation or local interface certification; the matching diagrams retain DVP/DWP labels while the paragraph separately mentions DVP/PFOD.

**Unresolved requirement.** The reviewed tolerance table is for **Euro only**. The bundle contains **no tolerance band for Danish krone or for any other T2S settlement currency** used at VP, and no VP User Guidelines text. The DKK tolerance is *not in reviewed evidence*; it would be established by VP's User Guidelines and by the currency-specific T2S tolerance configuration.

**Documented requirement — date range for entry.** A Transfer Order may be submitted for same-day settlement, for settlement up to **13 months** in advance of the settlement day, and for a settlement day **in the past** if all relevant static data were valid at that past settlement day — [[copenhagen-t2s-settlement]] clause 11.6.8, PDF 16; version 1 May 2025 (Version 13); section reviewed 14 September 2026.

---

## 4. What happens on the platform between matching and finality

**Documented requirement.** The T2S posting application process "checks if the settlement of Settlement Instructions, Settlement Restrictions and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources"; instructions are submitted to posting at the Intended Settlement Date, and "when the check is satisfactory, the posting application process updates the cash balance, securities position and limit headroom, resulting in the irrevocability of the settlement" — [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1–1.6.1.8.2, PDF 303–304; version R2026.JUN; reviewed 13 September 2026; English body text, authoritative language not independently established; no independent whole-edition supervisory approval certification.

**Reasoned inference.** The UDFS "irrevocability of the settlement" at posting and VP's "Moment of Settlement Finality" at the credit entry describe the same booking event from two perspectives — the platform's balance update and the rulebook's account entry on the receiving participant's securities account. The bundle contains no sentence equating the two, so treat the equivalence as inference; the authoritative statement for a VP participant is clause 11.8.2.1.

**Documented requirement — settlement mechanics at VP.** T2S Settlement is carried out by crediting/debiting the T2S Account and debiting/crediting a linked DCA as applicable; VP is not involved in providing cash liquidity on the DCA, which is handled in the payment system by the Cash Settlement Agent and the relevant central bank; for FoP settlement the DCA is not impacted — [[copenhagen-t2s-settlement]] clause 11.8.1.1, PDF 16; version 1 May 2025 (Version 13); section reviewed 14 September 2026.

**Documented requirement — day boundary, as context only.** The T2S settlement day is not a civil day: the start of day (SOD) period runs 18:45–20:00 and starts after the successful completion of the previous EOD period and after 18:45; night-time settlement (NTS) runs 20:00–3:00; real-time settlement (RTS) runs from 5:00 (or after NTS if NTS ends later) with the DVP cut-off harmonised for all currencies at 16:00 CET and the FOP cut-off ending the cut-off phase at 18:00 CET; end of day (EOD) runs 18:00–18:45 — [[t2s-schedule-r2]] T2S UDFS R2026.JUN, §1.4.2 (PDF 156–158), Table 37 (PDF 160–163) and §1.4.4.1 (PDF 163); version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026; English body text, authoritative language not independently established. LIMITATIONS carried: **CET is the source convention with no UTC conversion; the nominal schedule is not guaranteed execution and is not a local participant cut-off; a dated query requires a reviewed event overlay for the same review date**; the same pages as the 13 September section were re-fetched and were hash-identical on 14 September 2026. These are baseline values only — they do not tell you when a specific instruction on a specific business date actually matched or settled, and the bundle contains no dated event overlay.

---

## 5. Do not confuse the two Copenhagen routes

The bundle also contains VP's **non-T2S (VP Settlement) route**, whose moments are different and must not be quoted for a T2S Transfer Order (the section carries the LIMITATION that it applies to the VP, non-T2S settlement route):

| VP Settlement (non-T2S) | Trigger |
|---|---|
| Moment of Entry | When VP makes the **acknowledgement of receipt** available to the instructing party and other participants in that settlement (clause 4.3) |
| Moment of Irrevocability | When **Match** has occurred at VP; bilateral cancellation is still possible if received before the time of legal effect of the relevant Batch (clause 5.3.1) |
| Moment of Settlement Finality (net) | When the **Batch is completed** — posting on a net basis of the trade amount and the crediting/debiting of the affected securities accounts by book-entry; the order attains legal effect at the time of legal effect specified for that Batch (clause 6.2.1.1) |
| RTGS settlement | Crediting/debiting of the affected VP Accounts, registered immediately after the final verification of coverage (clause 6.1.2.1) |

**Documented requirement** — [[copenhagen-vp-matching-finality]] Euronext Securities Copenhagen, Part 4 – Settlement Rules, clauses 4–6.2.1, PDF 7–9; version "Part 4 Settlement Rules: 1 May 2025" (Version 13); section reviewed 14 September 2026, source reviewed 13 September 2026; English rulebook text, Danish law governs the VP system and no authoritative-language statement was reviewed. LIMITATION carried: this section covers the VP (non-T2S) route only.

**Documented requirement.** Securities registered on a T2S Account may be used for T2S Settlement and **cannot** be used for VP Settlement unless transferred to a VP Account; the User Guidelines describe how and when securities may be transferred between VP Accounts and T2S Accounts — [[copenhagen-t2s-settlement]] clause 11.6.1, PDF 15; version 1 May 2025 (Version 13); section reviewed 14 September 2026.

---

## 6. Scope qualifications you must keep attached

- **Access model.** A Settlement Participant may instruct a Transfer Order to T2S **either via VP as an ICP** (indirectly connected participant) **or directly on the T2S platform as a DCP** (directly connected participant), and becoming a DCP requires a separate agreement with VP — [[copenhagen-t2s-settlement]] clause 11.2.1, PDF 14; version 1 May 2025 (Version 13); section reviewed 14 September 2026. **Reasoned inference:** VP's Pre-Match is described as something VP performs on orders it receives before upload to T2S (clause 11.6.4), so the pre-matched Moment of Entry in clause 11.6.7 is relevant to the ICP flow; the bundle does not state how a DCP-submitted order interacts with VP's Pre-Match. That interaction is **not in reviewed evidence**.
- **Eligibility.** T2S settlement of DvP, DwP and FoP transactions requires the securities to be T2S-eligible according to the User Guidelines and made available on T2S, and to be book-entered with VP; for DvP, DwP and PFoD the settlement currency must be a T2S currency settled in central bank money unless specifically agreed otherwise with VP — clauses 11.3.2 A–B, PDF 14–15; same citation and qualifications.
- **Outdated cross-reference in the rulebook.** Clause 11.1.1 points participants to the "T2S User Guidelines" via a **2015 T2S User Handbook URL (v2.1)**; that link is stale and platform mechanics should be taken from the current UDFS sections cited above (LIMITATION carried from [[copenhagen-t2s-settlement]]).
- **Dates are review facts.** The Copenhagen sections were reviewed **14 September 2026** against a source reviewed **13 September 2026**; the T2S UDFS matching and posting sections were reviewed **13 September 2026**; the T2S schedule section was re-verified **14 September 2026** (hash-identical bytes). Nothing here is warranted as the position on any later date.
- **No instruction-like content** was found in the retrieved excerpts; nothing in the evidence purported to direct this answer.

---

## Open items

1. **VP User Guidelines** (the VP-specific description referenced throughout Part 4 §11). They are the named source for: the detailed Pre-Match procedure and the construction of the consolidated Transfer Order (clause 11.6.4); the validation criteria and mandatory data fields (clause 11.6.2); tolerance thresholds actually applied, including **any DKK band** (clause 11.6.6); recycling terms (clauses 11.7.2, 11.8.1.2); Hold & Release detail (clause 11.7.1); blocking/reservation/earmarking and supported T2S functionalities (clauses 11.4.2, 11.6.9); and account transfers between VP and T2S accounts (clause 11.6.1). **Not in the bundle.** Official route: Euronext Securities Copenhagen client documentation / VP Rule Book documentation service.
2. **Local interface specification** — which ISO 20022 message, version and field carries the pre-matched/already-matched indicator, the match status advice and the hold/release instruction on VP's own interface. **Not in reviewed evidence**; the UDFS is a functional matrix only, with no production XML/XSD validation or local interface certification.
3. **DKK (and non-EUR) matching tolerance bands** in the T2S configuration. The reviewed Table 57 is for Euro only. Official route: T2S UDFS currency-specific configuration plus VP User Guidelines.
4. **DCP flow and Pre-Match.** Whether and how a DCP-submitted Transfer Order is pre-matched by VP, and which Moment of Entry then applies. Not stated in Part 4 §11.
5. **Dated event overlay.** Any statement about what actually happened on a specific business date (delays, revised times, extended cut-offs under the T2S MOP) needs a reviewed event overlay for that date; the bundle contains baseline schedule values only.
6. **Governing-language confirmation.** The Copenhagen rulebook excerpts are English text; Danish law governs the VP system and no authoritative-language statement was reviewed. A Danish authoritative version, if one exists, would need to be reviewed before relying on the wording of "entered", "irrevocability" and "finally settled" in a legal opinion.

No retrieval in this bundle returned `blocked`, `needs_context` or `needs_refresh`.
