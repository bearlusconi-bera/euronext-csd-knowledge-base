# Proposed retrieval controls

No index or source manifest was changed. The JSON companion is a reviewable configuration design, not an implemented engine. Whole-document defaults are denied; only the named clauses can be considered after extraction and dependency checks. Most current-linked documents remain useful review candidates.

| ID | Scope | Permitted use | State |
| --- | --- | --- | --- |
| A01 | ECB T2S native platform; only CSDs/currencies/routes actually using T2S | conceptual matching versus settlement; baseline business-day phases; native message families and versions; conditional realignment mechanism | proposed-section-allowlist-after-extraction-validation |
| A02 | Monte Titoli S.p.A. / Milan settlement | published participant access requirements; matching/hold/cancellation distinctions; SF1/SF2/SF3 under published service rules | proposed-qualified-section-allowlist |
| A03 | EU CSDR covered entities/transactions; no automatic Norway national-law inference | current settlement-cycle ceiling and exceptions; CSD versus participant segregation/reconciliation/default responsibilities | proposed-bounded-legal-allowlist |
| A04 | EU financial entities as defined; no assumed Norway application | DORA includes CSDs; DORA general application date | proposed-bounded-legal-allowlist |
| A05 | Future or draft | explicit future-law/programme/release-status queries only | proposed-future-collection |
| A06 | Bounded legal/definition context | why an edition/date/approval ambiguity exists | proposed-audit-explanation-only |

## Metadata and dates

source_id, source_sha256, original_url, publisher/legal_issuer, legal_entity, market, service, role, security/link/currency scope, actual_content_language, authoritative_language, document_version, platform_release, publication_date, revision_date, approval_status/evidence, entry_into_force, provision_effective_from/to, retrieved_at, supersedes/amends/dependency_ids, PDF index and printed page, section/article/table/footnote, review_depth, extraction_status, retrieval_category, permitted_question_types, derived_from.

Unknown required applicability remains null; clarification or abstention, never inference disguised as verified metadata. Every inferred field includes inference label and evidence.

## Extraction and chunking

- Chunk by numbered provision plus required conditions/exceptions, never fixed size alone
- Article 72(2) retains Article 70(2); business-day timings retain previous-day/event dependencies
- Keep table headers, currency/payment-type branches, footnotes and legends with rows
- Keep realignment diagram, actor/account labels and narrative together
- Spreadsheet chunks carry workbook/sheet/cell ranges, full alternative columns and column-effective dates
- Archive members receive individual content hashes, MIME, source container and schema imports
- Cross-references outside reviewed scope trigger evidence expansion or abstention; no silent gap filling

## Exclusions and quarantine

- Milan timetable PDF 13/15 and corresponding Italian clauses
- Oslo unconditional edition approval
- ISIN workbook as universal current eligibility
- ESMA malformed C25 as identity key
- DORA French text as English quotation
- complete matching-field matrix from text-only UDFS PDF269
- unparsed archive member fields
- all unreviewed operative clauses
- AI-generated explanations as independent evidence
- duplicate clean/redline documents as separate corroboration
- marketing/landing pages as detailed operating rules
- broad regulatory acts without relevant articles
- historical WFC/PFMI disclosures as current procedures
- access forms and GFS-URD crosswalk as generic authority
- future migration designs or November drafts in current operational answers

## Refresh controls

- Re-fetch hashes at unchanged URLs and persist prior versions
- Poll/ingest notices only when an actual system is implemented; this audit creates no automation
- Manually approve effective/release state changes; dates alone do not promote drafts
- Apply business-date notice overlay after baseline retrieval
- Deduplicate by hash and canonical version/language without counting translations as independent evidence
