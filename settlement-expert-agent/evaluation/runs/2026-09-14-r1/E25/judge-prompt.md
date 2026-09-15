You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
When does a T2S transfer order at Euronext Securities Copenhagen become irrevocable and final, and how does VP's pre-match affect the moment of entry?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Irrevocability when the transfer order has status Matched on T2S (§11.7.1); hold/release and bilateral cancellation remain possible.",
  "Finality at the credit entry on the receiving securities account on the T2S platform (§11.8.2.1).",
  "Moment of entry differs: pre-matched orders enter when VP declares them compliant; non-pre-matched when T2S does (§11.6.7).",
  "Part 4 version 13, 1 May 2025; review 14 September 2026."
]
Fail conditions (must NOT appear):
[
  "Confuse VP batch finality with T2S finality."
]
Expected sections (if any): ['copenhagen-t2s-settlement']
Expected retrieval statuses: ['evidence_only']

# Rubric
# Evaluation rubric — Settlement Expert Agent

Each end-to-end case is scored on the dimensions below. Three sources of judgement are kept apart and reported separately:

| Source | What it produces | Limits |
|---|---|---|
| Deterministic checks (`settlement_agent.py check`) | Citation ids exist in the retrieved bundle; non-`evidence_only` statuses disclosed; governing-language and publication-description qualifications present; review date stated; no clock times, message versions, EUR amounts or XML absent from the bundle | Pattern-based; cannot judge meaning |
| Independent judge (separate model instance, sees the question, the answer, the actual retrieved passages, the hidden expected points and fail conditions) | Scores 0–2 per dimension with a quoted reason | Same model family as the responder; not a human review |
| Maintainer inspection | For a sample of cases the maintainer reads the source passages against the answer and records agreement or disagreement with the judge | Same assistant that built the library; not independent |

## Dimensions (judge scores 0 = fail, 1 = partial, 2 = met)

1. **Routing / scope** — Did the answer address the entity, service, date and mode the question implies, split multiple intents, and resolve or explicitly assume ambiguous scope?
2. **Evidence selection** — Were the right sections used (compared with the expected sections), including dependency/qualification sections (for example Oslo edition reservation, Milan bilateral cancellation)?
3. **Citation entailment and locator accuracy** — Does each cited passage actually say what the answer attributes to it, with a correct locator (article/section/PDF page) and review date?
4. **Preserved qualifications** — Authoritative language, translation status, approval reservations, publication-description basis, release identity, currency/date scope, LIMITATION lines.
5. **Completeness** — Are the expected key points present, and are the unanswerable parts identified with the missing source named?
6. **No unsupported operational claims** — No invented fields, cardinalities, versions, times, fees, eligibility, deployment or legal effects. Illustrative content labelled.
7. **Justified abstention** — For negative cases: did it decline/limit correctly without refusing the supportable part? For positive cases: did it avoid blanket refusal when evidence was sufficient?
8. **Label discipline** — Documented requirement / reasoned inference / proposed design choice / unresolved requirement used where they matter.

A case **passes** when: no dimension scores 0; dimensions 3, 4 and 6 score 2; and every hidden `must_not` condition is absent. A case is **partial** when it has no 0 but at least one of dimensions 3, 4 or 6 scores 1. Otherwise it **fails**.

Judges must quote the passage that supports or contradicts each key point and must not rely on their own knowledge of CSD rules; if the bundle does not contain a fact, the correct behaviour of the answer is to say so.


# The answer under review
<<<ANSWER
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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.127304+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_baseline_schedule"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-schedule-r2]] — Baseline day phases and preceding-day/event dependencies (14 September re-verification) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.2 and exception conditions; PDF 156–158 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Table 37; PDF 160–163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.1; PDF 163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026.
LIMITATION: CET is the source convention; no UTC conversion.
LIMITATION: Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date.
EXCERPT (§1.4.2 and exception conditions; PDF 156–158):
1.4.2 T2S schedule

18   The T2S schedule is under the control of the T2S operator, for creation of any new timelines, changing
19    and/or deletion of existing time for a period or event. The T2S Operator has the necessary privileges by
20    default to perform temporary or permanent changes to the T2S schedule. T2S ensures that the T2S sched-
21    ule always conforms to the T2S operating day calendar by currency for any changes.

22   T2S manages the transition between the various periods (see section Settlement day high level schedule
23    [ 158]) as an event. For each such event, T2S manages a planned time, a revised time and an effective
24    time:

25         l  The planned time corresponds to the standard schedule applied by default by T2S for every settlement
26       day. The T2S Operator can update this planned time in case of a permanent change in the regular
27        schedule;

28         l  The revised time is the foreseen time for the current settlement day, which usually coincides with the
29       planned time except when a delay has occurred. In contingency situations, the T2S Operator updates
30       the revised time while the planned time remains unchanged;


                                                                                            Page 156 of 2017



[PDF page 157]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l  The effective time is the time of the actual occurrence of the event during the current settlement day.

 2   T2S foresees the maintenance of individual T2S settlement currency dependent cut-offs and events. Howev-
 3     er, the T2S operator manages the overall processing of a settlement day based on a common T2S schedule
 4    configured for each T2S settlement currency. There is no schedule of a settlement day defined per currency
 5     in T2S, but distinct individual cut-offs and events per currency are defined.

 6    This multi-currency configuration allows for some flexibility within the boundaries of the real-time settlement
 7    closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET
 8    with FOP cut-off).

 9   The T2S Operator is entitled to change some cut-offs and events (deadlines for receiving Settlement Instruc-
10    tions/Settlement Restrictions for same day settlement) of a settlement day. This can be done independently
11    for a T2S settlement currency, in exceptional circumstances or contingency situations, based on a request
12    from the relevant T2S dependent external system (eg. RTGS, CSD platform, CMS). This exceptional proce-
13    dure is to be defined in the T2S Manual of Operational Procedure (T2S MOP). These currency dependent
14    cut-offs and events are specific events within the T2S daily schedule that have a cash component and are
15    not a cut-off related to the T2S centralised processing such as the start of day and end of day. Such curren-
16    cy dependent cut-offs and events are:

17         l DVP cut-off (IDVP / EDVP) –remains harmonised for all currencies at 16h00;

18         l  Cash Settlement Restriction cut-off;

19         l  Settlement restrictions release

20         l  Reimbursement of intraday credit

21         l BATM (Bilaterally Agreed Treasury Management) cut-off;

22         l CBO (Central Bank Operation) cut-off;

23         l  Optional cash sweep;

24         l  Inbound liquidity transfer cut off;

25         l  Automated cash sweep.

26    This change in cut-offs and events are valid only for the current T2S settlement day. When a currency de-
27    pendent cut-off or event is extended for a currency, then the start of its dependent processes (e.g. cash
28   sweep) is automatically extended for the same currency.

29   T2S allows such a change under the following conditions:

30         l  The sequence and order of events (predecessors and/or successors events) in T2S must remain un-
31       changed, i.e. a currency dependent cut-off cannot be delayed beyond a successor scheduling event if
32         this would have an impact on T2S processing (e.g. a CBO cut-off for Danish Krone cannot be extended
33       beyond the EOD cut-off for T2S, which is the successor in the scheduling). This includes no additions or
34       removals of events, no changes in event ordering and no change in event dependencies;

35         l  In the exceptional cases that T2S experiences a general issue across all currencies, it could be necessary
36        that the T2S Operator would need to extend the EOD cut-off (e.g. the T2S revised times would apply).
37        In this case, T2S ensures the sequence of currency independent cut-offs (securities Settlement Re-



                                                                                            Page 157 of 2017



[PDF page 158]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         striction cut-off and FOP cut-off) is not changed. The procedures to apply in case of such an event are to
 2       be defined in the T2S MOP.

 3    In the exceptional cases that T2S experiences the arrival of late peak volume transactions on Friday evening
 4    that are not available for settlement at the regular NTS, the T2S Operator would need to process into addi-
 5    tional NTS cycles. The procedure to apply in case of such an event are defined in the T2S MOP.

 6   T2S controls the execution of the processes so that the start of a subsequent process depends on:

 7         l  The completion of the current process and/or;

 8         l  The occurrence of a cut-off.

 9   However, for the start of a process, which is under the dependency of a preceding process and cut-off, T2S
10    ensures that this process cannot start until the completion of the previous process and until the cut-off time
11     is reached.

12
EXCERPT (Table 37; PDF 160–163):
[PDF page 160]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                                        Settlement Day

1                                  TABLE 37 - SETTLEMENT DAY HIGH LEVEL PROCESSES
2

      T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
         LINE

        18:45 –      Start of day  The start of day period including:
         20:00        (SOD)                                                             l  Change of business date in T2S;

                                                             l  Taking the common Snapshot (T2S and T2);

                                                             l  Preparation for night-time settlement:

                                 –  Revalidation of Settlement Instructions/Settlement Restrictions/amendments/hold
                                    and release instructions that failed to settle or to be executed as of their Intended
                                         Settlement date;

                                 –  At 19:00, final deadline to accept data feeds 131, effective for the current business
                                            date, from collateral management systems and payment/settlement banks; CBs
                                    and Payment Banks can send their Securities Valuation as soon as possible, ideally
                                     by 17:45, but in any case T2S will accept Securities Valuations until 19:00.

                                 –  At 20:00, final deadline to accept settlement instructions for processing in the se-
                                     quence 1 of the first night time cycle.

                                 –  Valuation of securities positions;

                                 –  Valuation of collateral eligible Settlement Instructions.

      20:00 – 3:00   Night-time   The night-time settlement period including two cycles:
                      settlement                                                             l  The first night-time cycle with reporting and processing of static data maintenance
                      (NTS)                                       instructions/maintenance instructions at the end of each settlement sequences in-
                                         cluding 5 sequences:

                                 – The sequence 0 (liquidity transfers from RTGS systems and from a T2S Dedicated
                                     Cash Account to another T2S dedicated cash account of the same T2S party, cash
                                         Settlement Restrictions regeneration related to the CoSD blocking and any cash
                                         Settlement Restrictions);

                                 – The sequence 1 (Corporate Actions on stock, new liquidity transfers, new cash
                                         Settlement Restrictions and all cash Settlement Restrictions not settled in the pre-
                                           vious sequence);

                                 – The sequence 2 (FOP for rebalancing purpose, new liquidity transfers, new cash
                                         Settlement Restrictions, new Corporate Actions on stock and all Settlement In-
                                               structions/restrictions which failed to settle in the previous sequences);

                                 – The sequence 3 (Central Bank Operations, new liquidity transfers, new cash Set-


    _________________________


       131   T2S processes these data feeds as soon as they are available. If data feeds are not received at the 19:00 deadline, T2S bases its processes on the
                 latest information received from the previous settlement days.


                                                                                          Page 160 of 2017



[PDF page 161]

                                                            T2S User Detailed Functional Specifications
                                                                                       General Features of T2S
                                                                                                 Settlement Day


T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
   LINE

                                  tlement Restrictions, new Corporate Actions on stock, new FOP for rebalancing
                                purpose and all Settlement Instructions/restrictions which failed to settle in the
                                   previous sequences);

                            – And the sequence 4 (new liquidity transfers and all the remaining Settlement In-
                                        structions/restrictions which are new or failed to settle in the previous sequences);

                            – The duration of the first night-time settlement cycle is dependent on settlement
                               volumes but should finish by 20:20(target objective) as long as standard peak
                               volumes are not exceeded.

                                                  l  The last night-time cycle, including partial settlement, with reporting and processing
                                   of static data maintenance instructions/maintenance instructions at the end of each
                                settlement sequences including 4 sequences:

                            – The sequence 4 (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in previous cycle);

                            – The sequence X (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in the previous sequences and
                                          partial settlement on all unsettled Settlement Instructions, if eligible to partial set-
                                  tlement processing);

                            – The sequence Y (reimbursement of the “multiple liquidity providers”);

                            – The sequence Z (liquidity transfers).

                            – The duration of the last night-time settlement cycle is dependent on settlement
                               volumes but should finish by 00:00 (target objective) as long as standard peak
                               volumes are not exceeded.

3:00 – 5:00   Maintenance  The maintenance optional daily window.
           window (MWI)





                                                                                     Page 161 of 2017



[PDF page 162]

                                                             T2S User Detailed Functional Specifications
                                                                                        General Features of T2S
                                                                                                  Settlement Day


 T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
    LINE

 2:30 Satur-   Maintenance  The mandatory weekend maintenance window.
 day – 2:30  window (MWI)
  Monday

   5:00 (or    Real-time set- The real-time settlement period including:
 after NTS if  tlement (RTS)                                                    l  The real-time settlement preparation;
  NTS ends
                                                    l  Penalty mechanism processing:
 before 3:00)
                             –  At 7:30 , a final deadline for provision to accept penalty reference data to be used  – 18:00
                                           in current day´s penalty calculation and recalculation processes:

                                                   (i) Securities subject to penalties information;

                                      (ii)Updated historic (former) prices for penalties;

                                                           (iii) Daily prices for penalties.

                             –  At 7:30 , start of the penalty reference data preparation processing 132;

                             –  At 8:30 , a final deadline for completing the penalty eligibility 133 (starting at 19:30
                                     or after the end of the Start of Day processes if they are completed afterwards);

                             –  At 8:30 of the 14th business day of the month, start of the monthly reporting of
                                  aggregated amounts of penalties (to be completed by 21:30);

                             –  After the completion of the penalty reference data preparation, a final deadline for
                                      provision of penalty modification requests to be considered in current day´s pen-
                                           alty processes;

                             –  After the processing of penalty modification requests submitted before the dead-
                                              line, and the penalty eligibility, but not before 9:15 , start of the Calculation, Re-
                                        calculation and reporting of new and modified penalties;

                             – On the 13th business day of the month, after the Recalculation is completed, start
                                    the end of appeal period process followed by the calculation of monthly aggregat-
                               ed amounts of penalties (to be completed by 8:30 on the next business day);

                                                    l  The real-time settlement with 5 partial settlement windows;

                                                    l  The real-time settlement closure.

   18:00 –     End of day   The end of day period including:
    18:45        (EOD)                                                    l  The stop of settlement engine;


_________________________


132   Preparation processing is comprised of Static data processing of reference data for the penalty calculation and recalculation.

133    Penalty eligibility is comprised of an analysis of failed matched settlement instructions from the previous business day to determine their eligibility
        for penalties.


                                                                                      Page 162 of 2017



[PDF page 163]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day


       T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
          LINE

                                                               l  The internal T2S securities accounts consistency check;

                                                               l  The recycling and purging;

                                                               l  The end of day reporting and statements 134.


 1
EXCERPT (§1.4.4.1; PDF 163):
1.4.4.1 Start of day (SOD)

 5    This section presents the start of day processes.

 6   The SOD period starts after the successful completion of the previous EOD period and after 18:45, and is
 7    followed by the night-time settlement period.

 8   The SOD period concentrates on the change of T2S business date, the taking of the common Snapshot and
 9    preparation of the night-time settlement period. It includes the processing of the feeds from collateral man-
10   agement systems (CMS) and payment/settlement banks for the reference prices and eligible assets (for val-
11    uation purposes).


12

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_vp_settlement_finality"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-vp-matching-finality]] — VP settlement: entry, matching, moment of irrevocability, settlement and finality (Part 4 §§4–6.2) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §§4–6.2.1; PDF 7–9 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: Applies to the VP (non-T2S) settlement route; the T2S route is the section copenhagen-t2s-settlement.
EXCERPT (Part 4 §§4–6.2.1; PDF 7–9):
4.        VP Settlement - Entering of Transfer Orders
4.1        A Settlement Participant  is entitled to instruct Transfer Orders for VP
             Settlement.
4.2         The Settlement of a transaction requires that the parties in the Transfer
             Order specify a validity period that coincide, i.e. the period during which the
               securities transaction concerned may participate in the Settlement.  If a
              Transfer Order has been received by VP prior to the commencement of the
             Settlement period, cf. clause 5.2.3, the first Batch of that Settlement period
                  will be deemed to be the commencement of the validity period.  If the
              Transfer Order is received at a later time the following Batch will be deemed
              to be the commencement of the validity period. A specified validity period
           must as a minimum comprise one Batch and cannot include more than the
             remaining part of the Settlement period.
4.3        Upon receipt of the Transfer Order for VP Settlement, VP will make an
            acknowledgement  available  to  the  instructing  party  and  any  other
               Participants in the Settlement of the transaction in question. As from that
          moment the Transfer Order is deemed "entered" into the VP Clearing and
             Settlement system (the Moment of Entry).

5.        VP Settlement - Matching

5.1         Introduction
5.1.1         For a Transfer Order to be included in a Batch, VP must have received both
              Transfer Orders concerning such transaction and Matching must be completed
              with a positive result before the time of legal effect of such Batch. If a Transfer
             Order designates a specific Batch in which the securities transaction is to be
               settled, Matching will be carried out until the time of legal effect of such Batch.
                   If no specific Batch has been designated, the Transfer Order will be included in
            matching until the time of legal effect of the last Batch, 20 settlement days
               thereafter.

5.2        Matching criteria etc.
5.2.1         After receipt in due time of the last of the two Transfer Orders VP will carry out
             Matching, i.e. a comparison of the information contained in such Transfer
             Orders, cf. the User Guidelines.
5.2.2            If the transaction amount instructed by the receiving Settlement Participant
                differs from that instructed by the delivering Settlement Participant, the



Settlement Rules - Version 13                                                                  | 7 of 17



[PDF page 8]

              transaction amount submitted  in the Transfer Order from the delivering
             Settlement Participant prevails, provided that the difference does not exceed
              VP’s tolerance thresholds for matching as described in the User Guidelines.
5.2.3            If the result of the matching is positive (Match), VP will make the output data
               available to the parties and any other Participants in the Settlement of the
               securities transaction in question.
5.2.4       Two Transfer Orders concerning net settlement which are Matched can provide
             the basis for Settlement of the securities transaction from a chosen intended
             settlement day and until Settlement takes place or the Transfer Orders are
                bilaterally cancelled by both Settlement Participants.

5.3       Moment of irrevocability
5.3.1      When Match of a Transfer Order has occurred the Transfer Order cannot be
              cancelled or revoked unilaterally by either of the Participant or a third party
              (the Moment of Irrevocability). The securities transaction is thus ready for
              settlement. However, if the parties to a transaction so agree, a binding Transfer
             Order can be cancelled by both parties submitting a cancellation transaction
             which must be received by VP prior to the time of legal effect of the Batch in
             which the cancellation is to have effect.

6.        VP Settlement - Settlement

6.1         Settlement terms
6.1.1       Net settlement

6.1.1.1      Settlement takes place when the net effect of all Transfer Orders in the relevant
             Batch is credited or debited to the affected Securities Accounts. In case of SEK
           DVP settlement, credit or debit of the affected Securities Accounts follow by
             Book-entry against the simultaneous recording  of trade amounts on the
              affected cash accounts. All updating will be carried out in the Batch in question
            and information thereon will be made available to the affected Participants.
6.1.2       Real time gross settlement
6.1.2.1       Real rime gross settlement will be carried out by crediting or debiting as the
             case may be the affected VP Accounts. The registration will be carried out
             immediately after the final verification of coverage, and information will be
          made available to the affected Participants.
6.1.3       Trade amounts
6.1.3.1     When the correct payment instructions in respect of the trade amounts have
            been provided by VP to Sveriges Riksbank for SEK Batches, or made available
              to the Cash Account Controller, VP is released of any and all liability as regards
             the further processing of the information and payments.
6.1.4       Settlement in the event of Insolvency Proceedings of a Participant
6.1.4.1      Settlement of Transfer Orders in accordance with clause 6.1 takes place until
           VP has received an  authoritative notice on Insolvency Proceedings  of a
               Participant from the Danish FSA or other public authority, and VP hereafter
              automatically has initiated its insolvency procedures. Though, VP may issue a
               default notice prior to any authoritative notice and request that the Participant
             provide VP with a statement on the Participants current status pursuant to its
              applicable corporate or company law.



Settlement Rules - Version 13                                                                  | 8 of 17



[PDF page 9]

6.1.4.2       Notwithstanding anything to the contrary in this clause,  if the insolvency
             procedure referred to in clause 6.1.4.1 is initiated during a Batch, the effects
              thereof will not occur until the current Batch has been concluded. Securities
              transactions concluded in a Batch are final, irrespective of the Insolvency
              Proceedings.
6.1.4.3       In case of Insolvency Proceedings of a Participant distinctions must be made
            between the Participant’s own transactions (″Participant Transactions″ - see
              clause 6.1.5.1) and transactions on behalf of a client of the Participant (″Client
              Transactions″ - see clause 6.1.5 ).
6.1.5         Client Transactions
6.1.5.1       Subject to clause 6.1.4.1 Client Transactions will not be settled as from the
              insolvency procedure referred to in clause 6.1.4.1 is initiated.
6.1.6        Participant Transactions
6.1.6.1       Distinctions must be made between net settlement and  real time gross
              settlement:
               A.   Net settlement:

                       Until 18:00 hours on the date that VP is notified of the Insolvency
                    Proceedings, Transfer Orders submitted by the insolvent Participant that
                  have reach Moment of Entry and where also the relevant corresponding
                     Transfer Orders submitted by counterparties have reach Moment of
                    Entry prior to the notification, will be included in VP's Batches and will
                  be submitted for settlement in accordance with the normal terms for
                    Settlement in Batches.

                            If VP is not informed of the Insolvency Proceedings until after 18:00
                   hours on the date of the Insolvency Proceedings, VP will settle the
                       Participant’s Transfer Orders  until the time VP  is notified and has
                        initiated its insolvency procedure.

               B.   Real time gross settlement:

                       Until 18:00 hours on the date that VP is notified of the Insolvency
                    Proceedings, Transfer Orders submitted by the insolvent Participant that
                  have reach Moment of Entry and where also the relevant corresponding
                     Transfer Orders submitted by counterparties have reach Moment of
                    Entry  prior to the  notification  will be submitted  for settlement  in
                   accordance with the normal terms for Settlement in RTGS.

6.2         Settlement Finality
6.2.1       Net settlement
6.2.1.1     A Transfer Order for Settlement in a Batch is finally settled (unconditional,
              irrevocable and enforceable) as from the moment when the Batch in which the
              Transfer Order is settled is completed (the Moment of Settlement Finality). A
             Batch is completed as of the posting on a net basis of the trade amount, etc.
            and the crediting or debiting of the affected Securities Accounts by Book-entry,
                  cf. clause 6.1 above. The Transfer Order in question attain legal effect as at the
             time of legal effect specified for the Batch in question.
6.2.1.2       In the event of a provisional transfer of securities between VP and a Participant
           who is a CSD, retransfer of such securities prior to the first transfer becoming
                 final is prohibited.



Settlement Rules - Version 13                                                                  | 9 of 17

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_t2s_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-t2s-settlement]] — T2S settlement at VP: access (ICP/DCP), eligibility, accounts, auto-collateral, pre-match, moments of entry, irrevocability, finality and insolvency (Part 4 §11) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §11; PDF 14–17 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: The clause links an outdated T2S UHB URL (v2.1, 2015); use the current UDFS sections for platform mechanics.
LIMITATION: Pre-match by VP creates a consolidated already-matched instruction: moments of entry differ for pre-matched and non-pre-matched orders.
EXCERPT (Part 4 §11; PDF 14–17):
11.        T2S Settlement

11.1        General
11.1.1      The T2S Settlement services available to Settlement Participants are
              described in detail in the T2S User Detailed Functional Specification and in the
           T2S User Handbook (together the T2S User Guidelines) available on the
            European Central Bank webpage
             (https://www.ecb.europa.eu/paym/t2s/pdf/t2s_uhb_v2.1_clean_20151202.p
            df?c485053816eb8ca53b82c066cc118a8d). The T2S User Guidelines also
             apply to the Settlement Participant unless the VP Rule Book provides
              otherwise.

11.2       Access rules
11.2.1      A Settlement Participant may instruct a Transfer Order to T2S, either via VP if
                      it is an ICP of T2S or directly via the T2S platform if it is a DCP of T2S. In order
              to become a DCP the Settlement Participant must enter into a separate
            agreement with VP.

11.3       T2S Settlement - Transfer Orders
11.3.1      A Settlement  Participant  is  entitled  to  instruct Transfer Orders  for T2S
             Settlement,  if the Settlement Participant complies with the terms set out in
              clause 11.4. Also MTS Denmark may submit Transfer Orders in respect of bonds
             traded in MTS Denmark.
11.3.2        Transfer Orders may settle via T2S Settlement if the following conditions are
            met:
               A.   In case of a DvP, DwP and FoP transaction:

                                   i.    The securities concerned are eligible for Settlement via T2S
                           according to the User Guidelines and are made available on T2S
                         (“T2S Eligible Securities”),

                                   ii.    The securities concerned are book-entered with VP, and



Settlement Rules - Version 13                                                                 | 14 of 17



[PDF page 15]

               B.   In case of a DvP, DwP and PFoD transaction, the settlement currency is
                  a T2S Currency, and the transaction is to be settled in central bank
                 money, unless specifically agreed otherwise with VP.

11.4       T2S Accounts
11.4.1      A Settlement Participant must have access to at least one T2S Account with VP,
              unless the Settlement Participant does not need to settle T2S Settlement
             Required Transactions.
11.4.2      A Settlement Participant may in respect of the securities registered on a T2S
             Account use the functionalities blocking, reservation and earmarking as further
              described in the User Guidelines.

11.5       T2S Auto-Collateral
11.5.1        Securities on a T2S Account can be used for T2S Auto-Collateral as agreed with
             VP. This requires that  (i) the Cash Settlement Agent has entered into an
            agreement according to which the securities registered on one or more defined
           T2S Account(s) may be used as collateral for credits granted by the relevant
               central bank in connection with T2S Settlement (referred to as the T2S Auto-
               Collateral agreement), (ii) the Cash Settlement Agent has delivered to VP a
            form stipulating that it wants to use T2S Auto-Collateral, and (iii) that the T2S
             Account has been earmarked for T2S Auto-Collateral by registration of a
                restrictive right in the VP Clearing and Settlement system. The types of
                restrictive rights that may be registered in this respect are described in the
             User Guidelines.
11.5.2      The VP Clearing and Settlement System supports the different T2S Auto-
               Collateral processes which are offered by the T2S System and described in the
           T2S User Guidelines. The T2S Auto-Collateral process depends on the T2S
              Auto-Collateral agreement entered into between the Settlement Participant and
             the relevant central bank. When a Settlement Participant enters into a T2S
              Auto-Collateral agreement the Settlement Participant must initiate the set-up
               of the right account structure with VP, and the central bank must instruct the
           T2S system. Hereafter the T2S Auto-Collateral is handled automatically by the
           T2S system in accordance with the T2S User Guidelines.

11.6        Entering of Transfer Orders, Validation and Pre-Match
11.6.1          All securities registered on a T2S Account may be used for T2S Settlement, and
             cannot be used for VP Settlement, unless the securities are transferred to a VP
             Account. The User Guidelines contain a detailed description of how and when
               securities may be transferred between VP Accounts and T2S Accounts.
11.6.2      A Transfer Order instructed for T2S Settlement is validated by VP upon receipt
                in order to declare it compliant with the technical rules of T2S as set out in the
           T2S User Guidelines. First, VP verifies that the sending party is authorised to
               instruct the Transfer Order via VP. Subsequently, VP applies the validation
                 criteria, and validates  if the mandatory data fields are correctly filled in. A
               detailed description of the information to be reported for validation is contained
                in the User Guidelines.
11.6.3      An unsuccessful validation of a Transfer Order causes a rejection of the Transfer
             Order, and information of the reason for the rejection are generated and sent
              to the submitting party.



Settlement Rules - Version 13                                                                 | 15 of 17



[PDF page 16]

11.6.4      Upon a successful validation of a Transfer Order concerning a T2S Transfer, but
               prior to upload of the Transfer Order for entry in the match module on the T2S
              platform, VP will attempt to perform Match outside the T2S platform (a Pre-
             Match), as further described in the User Guidelines. In case of no pre-match,
             the Transfer Order is immediately passed on by VP to the T2S platform for
            Match in the T2S matching module. If the result of the Pre-Match is successful,
           VP will create a new consolidated Transfer Order to T2S for entry in the T2S
            match module as described in the User Guidelines.
11.6.5      The right for VP to conduct Pre-Matches follows from an agreement (the
               Collective Agreement) with the ECB.
11.6.6          If the transaction amount instructed by the receiving Settlement Participant
                differs from that instructed by the delivering Settlement Participant, the
              transaction amount submitted  in the Transfer Order from the delivering
             Settlement Participant prevails, provided that the difference does not exceed
             the T2S tolerance match rules as set out in the T2S User Guidelines.
11.6.7      A Transfer Order, which has been successfully validated and Pre-Matched, is
           deemed "entered" into the VP Clearing and Settlement system at the moment
               at which  it was declared compliant with the technical rules of T2S by VP
              (the Moment of Entry into the System for pre-matched Transfer Orders).
            Whereas a Transfer Order for T2S Settlement, that has not been Pre-Matched,
             but passed on to the T2S System, is deemed “entered” into at the moment at
             which it has been declared compliant with the technical rules of T2S by the T2S
              platform (the Moment of Entry into the System for not pre-matched Transfer
              Orders).
11.6.8      A Transfer Order may be submitted for same day settlement, for settlement up
              to 13 months in advance of the settlement day, and for a settlement day in the
             past if all relevant static data were valid at the past settlement day.
11.6.9      VP supports various T2S  functionalities such as  linking,  partial  delivery,
                prioritization, etc. The functionalities supported by VP are described in the User
              Guidelines.

11.7       Matching on the T2S platform
11.7.1      When a Transfer Order has been given the status “Matched” on the T2S
              platform, irrespectively of whether it has been Pre-Matched or not, the Transfer
             Order  cannot  unilaterally  be  cancelled  or  revoked  (the  Moment  of
                Irrevocability). From the Moment of Irrevocability and until settlement has
             taken place, the functionality “Hold & Release” may, however, be applied by
            each party and the parties may bilaterally agree to cancel their Transfer Orders
                until settlement. This is further described in the User Guidelines.
11.7.2      A Transfer Order that has not been matched will be handled in accordance with
             the Recycling terms set out in the T2S User Guidelines.

11.8        Settlement
11.8.1      General
11.8.1.1     T2S Settlement  is  carried out by  crediting/debiting the T2S Account as
               applicable, and debiting/crediting a linked DCA as applicable. VP is not involved
                in the process of providing cash liquidity on the DCA as lines are handled in the
           payment system by the Cash Settlement Agent and the relevant central bank.
              For FoP Settlement, the DCA is not impacted.



Settlement Rules - Version 13                                                                 | 16 of 17



[PDF page 17]

11.8.1.2    A Transfer Order that has been matched but not settled because of lack of
             coverage will be handled in accordance with the recycling terms set out in the
             User Guidelines.
11.8.1.3     Information on Securities Account entries on the T2S platform will be made
               available to the affected Settlement Participants and other relevant parties as
              described in the User Guidelines.
11.8.2      Settlement Finality
11.8.2.1    A Transfer Order is finally settled (unconditional, irrevocable and enforceable)
             as from the account entry (credit) of the securities on the receiving Settlement
               Participant’s Securities Account on the T2S platform (the Moment of Settlement
                Finality). The corresponding account entry will hereafter be mirrored in the VP
              Clearing and Settlement System.
11.8.3      T2S Settlement in the event of Insolvency Proceedings of a Participant
11.8.3.1     Settlement of Transfer Orders in accordance with clause 11.8.1 takes place
                until VP has received an authoritative notice on Insolvency Proceedings of a
             Settlement Participant from the Danish FSA or other public authority, and VP
              hereafter has initiated its T2S insolvency procedures as described below. VP
          may also issue a default notice prior to any authoritative notice and request
              that the Settlement Participant provide VP with a statement on the Settlement
               Participant’s current status pursuant to its applicable corporate or company
              law.
11.8.3.2      Transfer Orders submitted by the insolvent Settlement Participant that have
             reached Moment of Entry and where also the relevant corresponding Transfer
             Orders submitted by counterparties have reached Moment of Entry prior to the
          moment of opening of the Insolvency Proceedings will be attempted settled in
             the T2S system.
11.8.3.3      Transfer Orders that have reached Moment of Entry after the moment of
             opening of the Insolvency Proceedings, but have been matched on the T2S
              platform prior to VP became aware, nor should have been aware of the opening
               of such proceedings, and are for settlement on the same T2S Business Day will
            be attempted settled in the T2S system, but will, however be cancelled  if
              unsettled at the end of the day.
11.8.3.4      Transfer  Orders  not  covered  in  clauses  11.8.3.2 and  11.8.3.3  will be
             immediately cancelled after VP becomes aware of the opening of the Insolvency
              Proceedings.
11.8.3.5      In case  of insolvency  of a Settlement Participant VP  will make relevant
              insolvency information available to relevant parties on the T2S settlement
              platform in accordance with the T2S User Guidelines and European Securities
            and Markets Authority’s “Guidelines on CSD participants default rules and
              procedures”.
11.8.3.6     Any actions taken by VP in the event of the opening of Insolvency Proceedings
              against a Settlement Participant will be executed in accordance with the T2S
             User Guidelines on a case-by-case basis.





Settlement Rules - Version 13                                                                 | 17 of 17

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
