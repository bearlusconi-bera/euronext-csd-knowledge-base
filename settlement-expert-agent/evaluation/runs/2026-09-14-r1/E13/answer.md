# Atomic exchange of 1,000 shares (ISIN A) against 500 bonds (ISIN B) between two Monte Titoli participants

## Direct answer

**I cannot confirm that.** The reviewed evidence does not establish that T2S guarantees atomicity of a two-security exchange. The retrieval for that exact topic was returned **blocked**, and the one realignment section that does speak about "all-or-none" settlement carries an explicit LIMITATION saying it "[d]oes not establish atomicity of an arbitrary two-security swap". What *is* documented is a narrower, actor-specified construct — the **WITH** ("all-or-none") processing position code — and a T2S-internal all-or-none relationship between a business instruction and the realignment instructions T2S generates for it. Those are not the same thing as a guaranteed atomic two-security swap, and the validation rules that would tell you whether your specific link is accepted are not in reviewed evidence.

## Retrieval statuses that are not `evidence_only` (disclosure)

| Retrieval | Context | Status | What it means here |
|---|---|---|---|
| 1 | `question_type: securities_swap_atomicity`, entity T2S, mode current, `as_of` 2026-09-13 | **blocked** — "Two-security structure, actual eligible links and supported instruction linkage require separate evidence." **GAP ID G04** | The direct question you asked is not answerable from reviewed evidence. I must not fill this gap from memory or from market practice. |
| 2 | `question_type: realignment_mechanism`, entity T2S, mode current, `as_of` 2026-09-13 | evidence_only | Narrower supported mechanism retrieved alongside the blocked topic. |
| 3 | `question_type: t2s_linked_instructions`, entity T2S, mode current, `as_of` 2026-09-14 | evidence_only | Actor-specified WITH links are the closest supported construct. |

Review dates used: **13 September 2026** for `[[t2s-matching]]`, `[[t2s-posting]]` and `[[t2s-realignment]]`; **14 September 2026** for the section record `[[t2s-linked-instructions]]` (its underlying source was reviewed 13 September 2026). All four sections are T2S-native functional descriptions of platform release **R2026.JUN**.

## What the reviewed evidence does say

**1. A T2S Actor can link instructions with an all-or-none processing position code — including across different ISINs.**
*Documented requirement.* `[[t2s-linked-instructions]]` T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.11.1–1.6.1.11.3 with footnote 243, PDF 442–444, version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026; body language English, no authoritative language asserted; source identity checked but no independent whole-edition supervisory approval certification.

- The processing position code **[WITH]** means "a Settlement Instruction, or Settlement Restriction is to be settled at the same time as the linked Settlement Instruction or Settlement Restriction" (PDF 442). The UDFS itself glosses WITH as "All-or-none".
- Instructions "can be linked whatever the type (delivery/receipt), the ISIN code or the Intended Settlement Date, provided that the links do not contradict each other" (PDF 443). So the UDFS does not forbid linking a leg in one ISIN to a leg in another ISIN.
- A link is created by sending the instruction with a processing position code plus the reference of the linked instruction (T2S Instruction Reference or T2S Actor Instruction Reference); if the Actor reference is used, the Reference Owner BIC of the linked instruction is also required, and "[i]n case the instruction does not include this field, T2S does not create the link and the instruction is rejected" (PDF 443).
- A T2S Actor **cannot** link "[a] T2S internally generated Settlement Instruction", nor a Liquidity Transfer with a Settlement Instruction or Settlement Restriction (PDF 443).
- Changing a link (e.g. WITH → BEFO) requires first unlinking via an Amendment Instruction with linkage type UNLK, then a second Amendment Instruction with linkage type LINK (PDF 444).

**LIMITATIONS that travel with this claim:** "Table 71 validation rules for links (PDF 448) are not admitted." and "T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline." Consequently the *rules that determine whether your specific WITH link would pass validation* are outside reviewed evidence, and so is the way you would express the link on Monte Titoli's local interface.

**2. T2S does guarantee all-or-none settlement in the cases where T2S itself generates the linked instruction.**
*Documented requirement.* `[[t2s-linked-instructions]]` (same locator as above): "T2S ensures in those cases the settlement on an all-or-none basis of the initial Settlement Instruction together with the T2S generated Settlement Instruction for realignment, for auto-collateralisation or the T2S generated liquidity transfer for corporate rebalancing liquidity etc." (PDF 442).
Confirmed for realignment by `[[t2s-realignment]]` UDFS R2026.JUN §1.6.1.10, concepts and reference-data requirements, PDF 373–376, version R2026.JUN; reviewed 13 September 2026; English, no authoritative language asserted; source identity checked, no independent whole-edition approval certification: "T2S ensures that the T2S generated realignment Settlement Instructions and their business Settlement Instructions settle on an all-or-none basis" (PDF 375).

**This is a vertical guarantee, not a horizontal one.** It binds *one* business instruction to *its own* generated realignment chain. `[[t2s-realignment]]` carries the LIMITATION: "Does not establish atomicity of an arbitrary two-security swap or describe every action outside T2S", and "Actual links/accounts and ISIN eligibility require verification."

**3. A single settlement instruction cannot carry two ISINs, so your exchange is at minimum two matched instruction pairs.**
*Reasoned inference*, derived from the matching field matrix in `[[t2s-matching]]` UDFS R2026.JUN §1.6.1.2, PDF 267–271, Diagrams 55–57 and footnote 194, version R2026.JUN; reviewed 13 September 2026; English, no authoritative language asserted; source identity checked, no independent whole-edition approval certification. "ISIN Code", "Settlement Quantity", "Securities Movement Type" and the delivering/receiving party BICs are each a **single mandatory matching field** per instruction (Diagram 55, PDF 269), and matching "compares the settlement details of Settlement Instructions provided by the deliverer and the receiver" (PDF 267). One instruction therefore describes one ISIN moving in one direction. The 1,000 shares of ISIN A and the 500 bonds of ISIN B are two separate securities movements, each needing its own matched pair. **LIMITATIONS:** "Functional matrix only; no production XML/XSD validation or local interface certification." and "Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD" — the diagram headers read DVP/DWP and FOP, and I have not normalised them.

**4. Settlement becomes irrevocable at posting, not at matching.**
*Documented requirement.* `[[t2s-posting]]` UDFS R2026.JUN §1.6.1.8.1 and first overview paragraph, PDF 303–304, version R2026.JUN; reviewed 13 September 2026; English, no authoritative language asserted; source identity checked, no independent whole-edition approval certification: the posting process "checks if the settlement ... can be achieved considering their eligibility to settlement and the available resources", and "[w]hen the check is satisfactory, the posting application process updates the cash balance, securities position and limit headroom, resulting in the irrevocability of the settlement" (PDF 303). Instructions are submitted to posting "at the Intended Settlement Date" (PDF 303).
Note also that posting may *group* instructions on the same resource "without any business links between one another" (PDF 303) — grouping for optimisation is explicitly not a business link, so it must not be read as an atomicity guarantee.

**5. Your instructions must still match before any of this applies.**
*Documented requirement.* `[[t2s-matching]]` (locator as above): all Settlement Instructions except those entering already "Matched" go through matching (PDF 268); unmatched instructions generate a Settlement Allegement to the counterparty after a waiting period, and "T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time" (PDF 271). *Explanation of terms, not a documented requirement:* an **allegement** is a notice telling a counterparty that an instruction is sitting in the system waiting to be matched against it. Footnote 194: upper- and lower-case letters are treated as different when comparing matching-field values, so references must not be case-normalised (PDF 269).

## Why this does not amount to "T2S guarantees atomicity of this swap"

| Question you need answered | Status | Basis |
|---|---|---|
| Does T2S guarantee atomicity of an arbitrary two-security exchange? | **Unresolved requirement** | Retrieval 1 **blocked**, GAP **G04**: "Two-security structure, actual eligible links and supported instruction linkage require separate evidence." `[[t2s-realignment]]` LIMITATION says it "[d]oes not establish atomicity of an arbitrary two-security swap". |
| Does the WITH code mean "settled at the same time"? | **Documented requirement** | `[[t2s-linked-instructions]]`, PDF 442. |
| Would a WITH link between your ISIN A legs and your ISIN B legs pass T2S validation? | **Unresolved requirement** | Table 71 "Rules applying to linked Settlement Instructions/Settlement Restrictions" (PDF 448) is referenced by the excerpt but is **not admitted** as reviewed evidence. Table 79 (PDF 534), referenced for contradicting links, is likewise not in the bundle. |
| Are ISIN A and ISIN B eligible in Monte Titoli, and on which accounts? | **Unresolved requirement** | `[[t2s-realignment]]` LIMITATION: "Actual links/accounts and ISIN eligibility require verification." GAP **G04**. "ISIN A" and "ISIN B" are placeholders in your question, not identifiers I can check. |
| Is this intra-CSD or cross-CSD? | **Reasoned inference, conditional** | You describe both parties as Monte Titoli participants, which points to an intra-CSD settlement. But `[[t2s-realignment]]` defines issuer CSD / investor CSD **per securities issue** (PDF 375), so whether realignment instructions are generated at all depends on whether Monte Titoli is issuer CSD or investor CSD *for each of ISIN A and ISIN B*. That is not in reviewed evidence for your two instruments. |
| How would you express the link on Monte Titoli's local interface? | **Unresolved requirement** | `[[t2s-linked-instructions]]` LIMITATION: the excerpt is "not a local participant interface specification, production XSD or message usage guideline". Monte Titoli's own X-TRM standards are not in this bundle. |

**Proposed design choice (yours to make, not an infrastructure rule):** if you proceed, the candidate design is four settlement instructions — a matched delivering/receiving pair for ISIN A and a matched delivering/receiving pair for ISIN B — carrying a **WITH** processing position code and the reference of the linked instruction, with the Reference Owner BIC supplied whenever you link by T2S Actor Instruction Reference. I label this a design choice, not a documented guarantee, because the admitted evidence does not validate this construct for a two-security exchange and the applicable link-validation table is not admitted. Do not present it internally as an atomicity guarantee until the open items below are closed.

*One further caution, from the excerpt itself and not an instruction to you:* the UDFS notes that for external-CSD settlement "[a]ll actions required by the realignment but without interaction with T2S are not described" (`[[t2s-realignment]]`, PDF 374). Any part of a swap that steps outside T2S is therefore outside the scope of anything I can cite.

## Open items

1. **Atomicity of a two-security exchange — GAP G04.** Needed: T2S UDFS material establishing the two-security structure, the supported instruction linkage for it, and actual eligible links. Route: ECB T2S professional-use documentation hub (T2S UDFS for the deployed release) and, if Monte Titoli-specific, Euronext Securities Milan's documentation service.
2. **Table 71 — "Rules applying to linked Settlement Instructions/Settlement Restrictions", UDFS R2026.JUN PDF 448.** Not admitted in reviewed evidence; it governs whether your WITH link is accepted. Route: same ECB T2S documentation hub, then admission through a dated review.
3. **Table 79 — "Set-up or increase of blocking, reservation or earmarking on securities", UDFS R2026.JUN PDF 534**, referenced by the excerpt for non-contradicting links. Not in reviewed evidence.
4. **Instrument and link eligibility for the two real ISINs — GAP G04.** Needed: current ISIN eligibility, CSD-link, securities-account and currency static data for both instruments at Euronext Securities Milan. Route: Monte Titoli client platform / MT-X and the CSD's documentation service; you must supply the actual ISINs.
5. **Monte Titoli local interface expression of the link.** Needed: the current X-TRM standard for A2A users, which is client-only. Route: MT-X.
6. **Nothing here is validated against production XML/XSD or certified for a local interface**, per the LIMITATION lines on `[[t2s-matching]]` and `[[t2s-linked-instructions]]`. No claim of production readiness is made.
