You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Which matching fields does EU law require CSDs to impose on participants, and what tolerance applies to settlement amounts?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "RTS 2018/1229 Article 5(3) list (a)-(l) and 5(4) transaction type taxonomy; Article 6 tolerance EUR 2 up to EUR 100 000, EUR 25 above; other currencies equivalent at ECB rate.",
  "Legal context, not local field lists."
]
Fail conditions (must NOT appear):
[
  "Confuse with T2S diagram fields without saying they are separate."
]
Expected sections (if any): ['sdr-matching-fields']
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
# Mandatory matching fields under EU law, and the matching tolerance for settlement amounts

## Direct answer

EU law (the Settlement Discipline RTS, Regulation 2018/1229) requires CSDs to make their participants populate eleven listed matching fields plus a twelfth open category chosen by the CSD, and, in addition, a transaction-type field drawn from a five-way taxonomy. For the settlement amount, CSDs must set a matching tolerance: for instructions in EUR it is EUR 2 per settlement instruction where the settlement amount is up to EUR 100 000 and EUR 25 where it is more than EUR 100 000; for other currencies, equivalent amounts based on the official ECB exchange rate, where available. All of this is documented in one reviewed section, reviewed 14 September 2026.

Retrieval status: the single retrieval in this bundle returned `evidence_only` (context: EU / regulatory / participant / current / `sdr_matching_fields`, as of 2026-09-14). No retrieval returned `blocked`, `needs_context` or `needs_refresh`, so nothing further had to be disclosed on that account. The knowledge base is as of 2026-09-13 and the review dates available are 2026-09-13 and 2026-09-14; the section used here carries the 2026-09-14 review date.

Terms used below, explained (explanation, not a documented requirement): *matching* is the process by which the two sides of a settlement instruction pair are confirmed to agree on the agreed values before settlement; a *tolerance level* is the maximum permitted difference in one of those values that still allows the two instructions to match; *FoP* (free of payment) means a securities transfer with no simultaneous cash leg.

## 1. The matching functionality and when matching is mandatory — Documented requirement

**Documented requirement.** CSDs must provide participants with a functionality supporting fully automated, continuous, real-time matching of settlement instructions throughout each business day, and must require participants to match their settlement instructions through that functionality prior to settlement. [[sdr-matching-fields]] Settlement Discipline RTS: consolidated 2 September 2024, Regulation 2018/1229 Article 5(1)–(2), version Consolidated 2 September 2024; reviewed 14 September 2026; body language English, authoritative language EU official languages, original or official-language text (not a translation); approval: source identity checked, no independent whole-edition supervisory approval certification.

**Documented requirement.** Three carve-outs are listed, where participants need not match through that functionality: (a) where the CSD has accepted that the instructions have already been matched by trading venues, CCPs or other entities; (b) where the CSD itself has matched the instructions; (c) for FoP instructions of the type referred to in Article 13(1)(g)(i) that consist of orders for transfers of financial instruments between different accounts opened in the name of the same participant or managed by the same account operator. The text adds that "account operators" for point (c) include entities that have a contractual relationship with a CSD and that operate securities accounts maintained by that CSD by recording book entries into those accounts. Same citation, Article 5(2).

## 2. The mandatory matching fields — Documented requirement

**Documented requirement.** CSDs must require participants to use the following matching fields in their settlement instructions. [[sdr-matching-fields]] Settlement Discipline RTS: consolidated 2 September 2024, Regulation 2018/1229 Article 5(3)(a)–(l), version Consolidated 2 September 2024; reviewed 14 September 2026; EU official languages authoritative, original or official-language text; approval: source identity checked, no independent whole-edition supervisory approval certification.

| # | Article 5(3) point | Matching field | Condition stated in the text | Label |
|---|---|---|---|---|
| 1 | (a) | Type of settlement instruction, as referred to in Article 13(1)(g) | — | Documented requirement |
| 2 | (b) | Intended settlement date of the settlement instruction | — | Documented requirement |
| 3 | (c) | Trade date | — | Documented requirement |
| 4 | (d) | Currency | Except in the case of FoP settlement instructions | Documented requirement |
| 5 | (e) | Settlement amount | Except in the case of FoP settlement instructions | Documented requirement |
| 6 | (f) | Nominal value for debt instruments, or quantity for other financial instruments | Instrument-dependent as drafted | Documented requirement |
| 7 | (g) | Delivery or receipt of the financial instruments or cash | — | Documented requirement |
| 8 | (h) | ISIN of the financial instrument | — | Documented requirement |
| 9 | (i) | Identifier of the participant that delivers the financial instruments or cash | — | Documented requirement |
| 10 | (j) | Identifier of the participant that receives the financial instruments or cash | — | Documented requirement |
| 11 | (k) | Identifier of the CSD of the participant's counterparty | Only for CSDs that use a common settlement infrastructure, including in the circumstances referred to in Article 30(5) of Regulation (EU) No 909/2014 | Documented requirement |
| 12 | (l) | Other matching fields required by the CSD for facilitating the settlement of transactions | Open category, at the CSD's requirement | Documented requirement |

**Documented requirement — additional field.** In addition to the Article 5(3) fields, CSDs must require participants to use a field indicating the transaction type, based on this taxonomy: (a) purchase or sale of securities; (b) collateral management operations; (c) securities lending/borrowing operations; (d) repurchase transactions; (e) other transactions (which can be identified by more granular ISO codes as provided by the CSD). Same section, Article 5(4). Note that the excerpt says "more granular ISO codes as provided by the CSD" without naming any code; no code values are in reviewed evidence.

**Reasoned inference** (derived from the "except in the case of FoP settlement instructions" wording in Article 5(3)(d) and (e)): for an FoP instruction the currency and settlement amount are not among the fields the CSD must impose, which is consistent with an FoP instruction having no cash leg. This is an inference from the drafting of the two exceptions; the RTS text in the bundle does not restate it as a separate rule.

**Reasoned inference**: point (l) means the list of twelve is a floor, not a ceiling — a CSD may impose further matching fields. The bundle's own LIMITATION line states this expressly: "Article 5(3)(l) allows CSDs to require other matching fields; T2S and local field lists are separate sections."

## 3. Tolerance for settlement amounts — Documented requirement

**Documented requirement.** For the purpose of matching, CSDs must set tolerance levels for settlement amounts. The tolerance level represents the maximum difference between the settlement amounts in two corresponding settlement instructions that would still allow matching. For settlement instructions in EUR, the tolerance level per settlement instruction is EUR 2 for settlement amounts of up to EUR 100 000, and EUR 25 for settlement amounts of more than EUR 100 000. For settlement instructions in other currencies, the tolerance level per settlement instruction is of equivalent amounts based on the official exchange rate of the ECB, where available. [[sdr-matching-fields]] Settlement Discipline RTS: consolidated 2 September 2024, Article 6, version Consolidated 2 September 2024; reviewed 14 September 2026; EU official languages authoritative, original or official-language text; approval: source identity checked, no independent whole-edition supervisory approval certification.

Two points on scope that the text itself fixes:

- The tolerance is expressed **per settlement instruction**, and it is a tolerance on the **settlement amount** only. No tolerance for any other matching field is stated in the reviewed evidence.
- The threshold is stated by reference to the settlement amount itself (up to EUR 100 000 versus more than EUR 100 000), not to the size of the difference.

**Unresolved requirement**: what a CSD applies when an official ECB exchange rate is not available for a given currency is not in reviewed evidence — Article 6 as excerpted says "where available" and stops there.

## 4. What this section does not establish

**Unresolved requirement — local field lists.** This is EU legal context only. The section's LIMITATION line states: "Legal context, not local procedures or Norway incorporation. Future amendments remain separate." So the reviewed evidence here does not establish (i) how Euronext Securities Milan (Monte Titoli), Copenhagen (VP), Porto (Interbolsa), Athens (ATHEXCSD) or Oslo (VPS) implement these fields in their own rulebooks or client interfaces, (ii) the T2S matching field list or T2S matching tolerance behaviour, (iii) any additional Article 5(3)(l) fields any of those CSDs actually require, or (iv) how the RTS is incorporated into Norwegian/EEA law for VPS. The bundle's second LIMITATION line confirms that "T2S and local field lists are separate sections" — none of those sections were retrieved here.

**Unresolved requirement — version currency.** The citation is to the consolidated text as at 2 September 2024, reviewed 14 September 2026. Amendments adopted or applying after that consolidation are, per the LIMITATION line, a separate matter and are not covered by this section; the review date is a statement about when the source was checked, not a guarantee that nothing has changed since. No later version was retrieved in this bundle.

**Unresolved requirement — message-level mapping.** Nothing in this bundle maps the Article 5(3) fields to ISO 20022 message elements, to T2S instruction fields or to any local interface specification. No message name, version, field tag or cardinality can be stated from this evidence.

**Not a proposed design choice here.** No implementation decision is being recommended in this answer; where a specification is needed, the field-to-message mapping rows would have to be marked "not in reviewed evidence" until the T2S and local sections are retrieved.

## Open items

1. **T2S matching field list and T2S matching tolerance behaviour** — needed to say how these RTS fields are actually matched in T2S. Not retrieved in this bundle; the LIMITATION line names "T2S and local field lists" as separate sections. Route: retrieve the T2S matching sections from the library; underlying official route is the ECB's T2S documentation service (UDFS/UHB) via the public T2S documentation hub.
2. **Local matching field lists and any Article 5(3)(l) additional fields per CSD** (Milan, Copenhagen, Porto, Athens, Oslo) — not in reviewed evidence. Route: the relevant CSD sections in the library; official route is each CSD's public rules/notices hub and its client platform documentation (for example Milan's X-TRM standards on the client platform, Copenhagen's User Guidelines, Porto's STD Manual appendices, Athens' DSS announcements), which are client-only material.
3. **Norway/EEA incorporation of Regulation 2018/1229** for VPS — expressly excluded by the section's LIMITATION line. Route: the Norwegian implementing/incorporating instrument, not retrieved here.
4. **Any amendment to the Settlement Discipline RTS after the 2 September 2024 consolidation** — "future amendments remain separate" per the LIMITATION line. Route: EUR-Lex CELEX 02018R1229 consolidated series, re-reviewed for a later date.
5. **Treatment where no official ECB exchange rate is available** for a non-EUR settlement currency — not in reviewed evidence.
6. **Gap ids**: the bundle records no gap ids for this retrieval (`gap_ids` is null); the two LIMITATION lines above are the named constraints.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.321865+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "sdr_matching_fields"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[sdr-matching-fields]] — Settlement discipline RTS: matching functionality, mandatory matching fields, transaction-type field and tolerance levels (Articles 5–6) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: Settlement Discipline RTS: consolidated 2 September 2024 | Regulation 2018/1229 Article 5; consolidation 2 September 2024 | version Consolidated 2 September 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02018R1229-20240902
CITATION: Settlement Discipline RTS: consolidated 2 September 2024 | Article 6 | version Consolidated 2 September 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02018R1229-20240902
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
LIMITATION: Article 5(3)(l) allows CSDs to require other matching fields; T2S and local field lists are separate sections.
EXCERPT (Regulation 2018/1229 Article 5; consolidation 2 September 2024):
Article 5

Matching and population of settlement instructions

1.   CSDs shall provide to participants a functionality that supports fully automated, continuous real-time matching of settlement instructions throughout each business day.
2.   

CSDs shall require participants to match their settlement instructions through the functionality referred to in paragraph 1 prior to their settlement, except in the following circumstances:

(a) 

where the CSD has accepted that the settlement instructions have already been matched by trading venues, CCPs or other entities;

(b) 

where the CSD itself has matched the settlement instructions;

(c) 

in the case of free of payment (‘FoP’) settlement instructions, referred to in point (g)(i) of Article 13(1), which consist of orders for transfers of financial instruments between different accounts opened in the name of the same participant or managed by the same account operator.

Account operators referred to in point (c) shall include entities that have a contractual relationship with a CSD and that operate securities accounts maintained by that CSD by means of recording book entries into those securities accounts.

3.   

CSDs shall require participants to use the following matching fields in their settlement instructions for the matching of settlement instructions:

(a) 

the type of settlement instruction, as referred to in point (g) of Article 13(1);

(b) 

the intended settlement date of the settlement instruction;

(c) 

the trade date;

(d) 

the currency, except in the case of FoP settlement instructions;

(e) 

the settlement amount, except in the case of FoP settlement instructions;

(f) 

the nominal value for debt instruments, or the quantity for other financial instruments;

(g) 

the delivery or receipt of the financial instruments or cash;

(h) 

the ISIN of the financial instrument;

(i) 

the identifier of the participant that delivers the financial instruments or cash;

(j) 

the identifier of the participant that receives the financial instruments or cash;

(k) 

the identifier of the CSD of the participant's counterparty, in the case of CSDs that use a common settlement infrastructure, including in the circumstances referred to in Article 30(5) of Regulation (EU) No 909/2014;

(l) 

other matching fields required by the CSD for facilitating the settlement of transactions.

4.   

In addition to the fields referred to in paragraph 3, CSDs shall require their participants to use a field indicating the transaction type in their settlement instructions based on the following taxonomy:

(a) 

purchase or sale of securities;

(b) 

collateral management operations;

(c) 

securities lending/borrowing operations;

(d) 

repurchase transactions;

(e) 

other transactions (which can be identified by more granular ISO codes as provided by the CSD).
EXCERPT (Article 6):
Article 6

Tolerance levels

For the purpose of matching, CSDs shall set tolerance levels for settlement amounts.

The tolerance level shall represent the maximum difference between the settlement amounts in two corresponding settlement instructions that would still allow matching.

For settlement instructions in EUR, the tolerance level per settlement instruction shall be EUR 2 for settlement amounts of up to EUR 100 000 and EUR 25 for settlement amounts of more than EUR 100 000 . For settlement instructions in other currencies, the tolerance level per settlement instruction shall be of equivalent amounts based on the official exchange rate of the ECB, where available.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
