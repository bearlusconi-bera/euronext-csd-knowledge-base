# Fee for a cross-CSD DvP settlement instruction at Euronext Securities Milan

## Direct answer

**Unresolved requirement — no fee can be quoted.** The reviewed evidence contains no tariff, price list or charging rule for Euronext Securities Milan (Monte Titoli), so no amount, currency or charging basis for a cross-CSD DvP (delivery versus payment — the simultaneous exchange of securities against cash) settlement instruction can be stated. The fee retrieval returned a **blocked** status, and I do not fill that gap from memory or from market practice.

## Retrieval statuses (disclosure)

| Retrieval | Context | Status | What it means here |
|---|---|---|---|
| 1 | Milan / settlement / current / `fee_amount` | **blocked** — gap **G17** | The retriever states: "Exact tariff row, service, charging basis, currency and transaction date must be reviewed." No pricing evidence is admitted, so the priced question is unanswerable from this bundle. |
| 2 | Milan / settlement / current / `milan_cross_csd_rule` | evidence_only | Supports what a cross-CSD settlement *is* and when Milan permits it — not its price. |
| 3 | Milan / settlement / current / `milan_settlement_service_scope` | evidence_only | Supports the scope of the Settlement Service and the two connectivity models — not its price. |

Because retrieval 1 is blocked, every statement below about cost is an **Unresolved requirement**; only the structural statements are documented.

## What the reviewed evidence does establish

**Documented requirement.** Cross-CSD settlement between a Monte Titoli participant and a participant in another CSD in T2S is carried out automatically by T2S, which performs the movements across the securities accounts of the participants, of the investor CSDs and of the issuer CSD. Monte Titoli does not envisage cross-CSD settlement on securities where the issuer CSD is outside T2S, unless both investor CSDs have a link with another CSD in T2S so that realignment with the issuer CSD outside T2S is not necessary — [[milan-cross-csd-disclosure]] Regulations as of 26 January 2026, Articles 77–78 with footnote 8, PDF 54 (printed 53), version 26 January 2026; section reviewed 14 September 2026, source reviewed 13 September 2026; English translation, the **Italian** text prevails (cover, PDF 1); source identity checked, no independent whole-edition supervisory approval certification. LIMITATION carried with the claim: actual links per ISIN are not certified, so whether a given cross-CSD instruction is even admissible is conditional on evidence this bundle does not contain.

**Documented requirement.** The Settlement Service is operated by the T2S platform and covers both intra-CSD settlement (two Monte Titoli participants) and cross-CSD settlement (a Monte Titoli participant and a participant in another CSD in T2S), within the limits of Article 27 of the Operating Rules. Participants may enter instructions through direct or indirect connectivity; instructions entered through an indirect connection are first subject to the X-TRM Service processes, while instructions entered through a direct connection are subject only to T2S processes — [[milan-service-scope]] Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025), §1.3 opening, PDF 12 (printed 8); section and source reviewed 14 September 2026; English translation with uneven wording, the **Italian** text prevails (cover, PDF 1); source identity checked, no independent whole-edition supervisory approval certification. LIMITATION carried with the claim: §1.3.1 (PDF 12–16) of that document is quarantined because its operational-clock values conflict with the deployed R2026.JUN schedule; nothing in this answer relies on it.

**Reasoned inference (from the two sections above, not from any tariff).** Because the same instruction can reach Milan through an indirect connection (ICP — indirectly connected participant, instructions pass through X-TRM) or a direct connection (DCP — directly connected participant, instructions go straight to T2S), and because cross-CSD settlement additionally drives realignment movements at investor and issuer CSD level, a fee enquiry has at least these unresolved dimensions: which legal entity charges (Milan, the counterparty CSD, T2S), the access model, the charging unit (per instruction, per settled movement, per realignment leg), the currency and the transaction date. None of these is settled by the bundle; this inference identifies the questions, it does not answer them.

**Proposed design choice (for the reader, not an infrastructure rule).** If this figure is needed for a cost model, decide explicitly whether you are pricing the *client-facing* Milan tariff only, or the all-in cost including the counterparty CSD's and T2S's own charges, before requesting evidence — the two produce different answers and the request to the CSD should say which.

## What is missing

- No fee amount, fee band, minimum/maximum, discount, rebate or billing-cycle rule is in reviewed evidence — **not in reviewed evidence**.
- No statement that cross-CSD DvP is priced differently from intra-CSD DvP, or from free-of-payment cross-CSD delivery — **not in reviewed evidence**.
- No effective date or version of any Milan tariff is in reviewed evidence, so even a figure obtained elsewhere could not be time-qualified against this knowledge base — **not in reviewed evidence**.

## Open items

1. **Gap G17 (blocked topic `fee_amount`)** — the exact tariff row, the service it is attached to, the charging basis, the currency and the transaction date must be reviewed before any amount can be given. Source needed: the published Euronext Securities Milan (Monte Titoli) price list / fee schedule applicable on the intended transaction date; its exact title, version and effective date are not in reviewed evidence.
2. **Counterparty and platform charges** — if the all-in cost is wanted, the other CSD's tariff and the T2S pricing schedule are separate documents, none of which is in this bundle.
3. **Instrument, link and account eligibility** — Article 77(2) makes cross-CSD settlement conditional on the issuer CSD being in T2S or on suitable links; per-ISIN link and account eligibility is not certified in reviewed evidence and would have to be confirmed before a fee is even applicable.
4. **Official route** — request the applicable tariff and its effective date through the Euronext Securities public documentation hub for Milan, or through the client platform (MT-X) for entitlement-restricted material; client-only documents cannot be substituted by reasoning. I do not draft or send that request.

Review dates of the evidence used: 14 September 2026 for both sections (underlying source review 13 September 2026 for the Regulations, 14 September 2026 for the Settlement Service Instructions). No claim here is asserted as "current today" beyond those review dates.
