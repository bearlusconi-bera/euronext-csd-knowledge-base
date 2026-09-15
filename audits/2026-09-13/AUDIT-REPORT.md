# Independent audit — Euronext CSD / T2S knowledge library

**As of 13 September 2026. Verdict: useful evidence library, not ready for unrestricted operational answering.** It can support cited explanations of selected settlement concepts, local participant requirements and regulatory responsibilities. It cannot yet reliably give complete production instructions, current local cut-offs, instrument eligibility, fees/tax answers or full onboarding/default procedures across all five CSDs.

The archive is intact and many source distinctions are already sensible. The main risk is admitting an entire current-labelled document despite unresolved dates, scope, missing diagram content or unreviewed clauses. No deployed retrieval application/index was located. This audit changes no original archive, manifest or generated explanation; every recommendation is a proposal.

## Highest-priority corrections

1. **Resolve the Milan timetable conflict.** Both English and Italian current-linked settlement instructions retain 19:30 NTS / two partial windows; current T2S R2026.JUN gives 20:00 / five. Quarantine those local passages and obtain the applicable notice chain. Add dated ECB exceptions: on 8 September the announced EUR DvP cut-off moved to 17:00. See F01–F02.
2. **Remove the ISIN workbook’s broad current admission.** Its scope is European Offering listing data, with designated/alternative places from 21 September. It is not universal current Milan eligibility. See F03.
3. **Use section-level admission and repair extraction.** The matching-field diagram is missing from text despite a text-rich page; DORA’s English-labelled original has French operative text. Keep roles, service, language, release, dates, footnotes and exceptions with every claim. See F04–F06.
4. **Close specific authority and procedure gaps.** Athens is principally an edition/amendment label issue in the reviewed history, while Oslo’s edition-specific approval reservation remains unresolved. Public Porto layouts should be reviewed before seeking client-only specifications. See F07–F12 and the missing-source queue.

## What was actually checked

| Measure | Audit result |
|---|---:|
| Catalogue URL entries given a provisional metadata decision | 918 |
| Retained originals / unique content hashes | 800 / 787 |
| Archived webpage records / selected legal captures screened | 357 / 14 |
| Additional discussion URLs / user attachment records screened | 6 / 1 |
| All decision records, including audit additions and overlapping origins | 1335 |
| Sources with substantive sampled review | 33 |
| Of these, archived document records | 22 |
| Live requests / HTTP 200 responses | 115 / 113 |
| Existing document URLs compared by SHA-256 / unchanged | 62 / 62 |
| Live identity checks on existing current-local/current-infrastructure candidates | 39 |
| Whole operational manuals certified in every provision | 0 |
| Practical coverage rows / evaluation cases | 83 / 34 |
| Retrieval tests actually run | 0 |

The 33 substantive source records comprise 22 archived documents, three additional local-language PDFs, six legal-text records and two operational web sources. Sampling a long manual is not a full-document review. The 39 operational live checks verify availability/identity and current source trails, **not** all service applicability or supervisory approvals. The 62 unchanged hashes cover a selected subset, not all 800 remote sources. All 800 retained originals matched their archived hashes locally. Metadata-only categories remain provisional and never grant admission. Overlapping inventory origins are not additional independent authorities.

Official live checks covered all five CSDs’ documentation hubs, ECB SDD/releases/status, ESMA, EUR-Lex and national-authority routes. Banca d’Italia, Danish and Norwegian Finanstilsynet and the Portuguese official Gazette were accessible; the HCMC CSD route refused the connection. One guessed Italian rules URL returned 404; the working Italian source route and originals were then used. Full independent national authorisation/approval decisions were not obtained. Browser/web reading recovered selected legal material where direct HTTP was incomplete; no authenticated client service was inspected.

## Deliverables

- [Prioritised findings](FINDINGS.md): 12 findings with source, exact locator, likely answer error and correction.
- [Source decisions, CSV](SOURCE-DECISIONS.csv) and [JSON](SOURCE-DECISIONS.json): one provisional decision for every inventory record, plus additions; no whole-document admission.
- [Reviewed source ledger](REVIEWED-SOURCES.md) and [date/amendment relationships](SOURCE-RELATIONSHIPS.json): precise sampling, approval limits and separate temporal states.
- [Coverage matrix](COVERAGE-MATRIX.md), [CSV](COVERAGE-MATRIX.csv) and [JSON](COVERAGE-MATRIX.json): 83 practical questions with roles, evidence and gaps.
- [Missing/replacement material](MISSING-SOURCES.md): 17 prioritised document dependencies with official routes and access status.
- [Retrieval proposal](RETRIEVAL-PROPOSAL.md) and [machine-readable proposal](RETRIEVAL-PROPOSAL.json): bounded allowlists, exclusions, metadata and extraction/chunking controls.
- [Explanation/claim review](CLAIM-REVIEW.md): assessment of existing summaries and a qualified cross-CSD explanation.
- [Evaluation set](EVALUATION-SET.md) and [JSON](EVALUATION-SET.json): 34 evidence-backed expected answers; **all NOT RUN**.
- [Verification results](VERIFICATION.md): archive preservation, artifact consistency and known static defects.

New downloads, extracts, HTTP timestamps, redirects and hashes are in `sources/`, `extracted/` and `evidence/`. The scripts reproduce the reports from the retained evidence and explicit review annotations; they do not independently perform semantic review.

## Scope limits

This was risk-based sampling, prioritising Milan/T2S and the existing date/authority flags. It did not read 29,084 PDF pages, verify all instrument links, inspect all fee rows, certify all message schemas or assess every legal provision. It did not authenticate to MT-X, CLIMP, MyVPS, MyEuronext or MyStandards. The 14 archive member lists were inspected, but their contents were not fully parsed. Only two original PDF pages and the existing generated cross-CSD image were visually reviewed; other saved PNGs are rendered evidence, not additional visual-review claims. No successful RAG retrieval or answer-quality score is claimed.

The first implementation step is the narrow section allowlist and conflict quarantine, followed by extraction repair and the current Milan notice/interface dependencies. Broader coverage should be earned by closing specific matrix questions and then running the supplied evaluation set.
