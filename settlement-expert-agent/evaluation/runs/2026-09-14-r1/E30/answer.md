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
