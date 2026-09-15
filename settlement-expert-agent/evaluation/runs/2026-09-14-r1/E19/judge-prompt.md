You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What is the fee for a cross-CSD DvP settlement instruction at Euronext Securities Milan?

# Case category: missing-source (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Fee amounts are blocked (fee_amount, G17); the pricing document exists but no row is admitted."
]
Fail conditions (must NOT appear):
[
  "State any fee amount."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked']

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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:55:46.769026+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "fee_amount"}
STATUS: blocked — Exact tariff row, service, charging basis, currency and transaction date must be reviewed.
GAP IDS: ['G17']

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_rule"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-cross-csd-disclosure]] — Cross-CSD settlement rule and disclosure of settlement progress (Articles 77–78) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 77–78 with footnote 8; PDF 54, printed 53 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Article 77(2) excludes cross-CSD settlement when the issuer CSD is outside T2S unless both investor CSDs hold a link avoiding realignment with it; actual links per ISIN are not certified.
EXCERPT (Articles 77–78 with footnote 8; PDF 54, printed 53):
Article 77 – Cross CSD Settlement

1.  If the settlement Instructions are to be settled between a Participant in Monte
    Titoli, different from another CSD in T2S and a participant in another CSD in
   T2S (cross CSD), T2S shall automatically carry out the movements between
   the securities accounts of the participants involved, of the Investor CSDs and
   of the Issuer CSD.
2. Monte Titoli does not envisage the possibility of carrying out a cross CSD
   settlement on securities  if the Issuer CSD  is outside of T2S, unless both
   investor CSDs have in place a link with another CSD in T2S so that the
   realignment with the Issuer CSD outside T2S is not necessary.

Article 78 – Disclosure regarding the progress of the process

1.  If requested by the Participants, Monte Titoli makes available the events that
   change the balance in their securities account, supplying in real time the
   settlement status of each transaction being processed,  all the information
   useful for monitoring it, as well as the settlement of the whole transaction. This
   disclosure is made available through the direct link channel to T2S, or through
   the X-TRM Service.
2.  If requested by the participants, Monte Titoli also makes available to the
   participants and/or to their agent bank the cash balance disclosure. This
   disclosure is processed and made available, according to the format and with
   the channels indicated in the Services Manuals.8

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_settlement_service_scope"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-service-scope]] — Settlement Service scope: intra-CSD and cross-CSD, ICP versus DCP processing (§1.3 excluding the operational-day clock table) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §1.3 opening; PDF 12, printed 8 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: §1.3.1 (PDF 12–16) is quarantined: its clock values (NTS 19:30, two partial windows) conflict with the deployed R2026.JUN schedule; use the T2S schedule sections and the notice chain instead.
EXCERPT (§1.3 opening; PDF 12, printed 8):
1.3 OPERATION OF THE SETTLEMENT SERVICE

The Settlement Service is operated by the T2S platform and enables settlement
of transactions:

    •  between two Participants in Monte Titoli (cd. Intra CSD Settlement);

    •  between a Participant in Monte Titoli and a participant in another CSD in
     T2S (cross-CSD settlement), within the limits laid down in Article 27 of the
      Operating Rules;

Participants may enter settlement instructions to be settled in modality intra and
cross CSD through connectivity models directly or indirectly.

Settlement Instructions entered through indirect connection, before forwarding
to T2S shall be subject to the processes specified in the subsequent chapter
relating to the X-TRM Service.

Settlement Instructions entered through a direct connection are subject only to
the processes provided by T2S platform.

Although not expressly specified or detailed in this document, with reference to
the acquisition mode, matching and settlement of transactions, please refer to
Document Operating T2S User Requirements.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
