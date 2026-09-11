# Turning this library into a knowledge base

The sources are collected and organised; a retrieval application has not been deployed. Start with the curated manifest instead of importing the entire extraction directory without filters.

## Suggested collections

| Collection | Include | Retrieval rule |
|---|---|---|
| Regulatory baseline | Selected current consolidated legislation, technical standards, ESMA register, PFMI | Resolve jurisdiction, service and provision-level effective dates |
| Current local operations | Current-hub rulebooks, instructions, manuals and current fee tables for each CSD | Require an explicit market/entity filter |
| European Offering | Milan-based expansion documentation and test/readiness material | Mark rollout date and distinguish service availability from future migration |
| Convergence | Future SDDs, market newsletters and migration/test material | Use only for future-state/design questions unless later go-live is verified |
| Future regulations/releases | T+1 implementation and future T2S/local releases | Distinguish consultation, adoption, publication and application |
| Reference and history | WFC/PFMI disclosures, old notices, superseded editions, redlines | Retrieve only when date/history is requested or necessary |
| Unresolved sources | Conflicting versions and questionable approval status | Surface the ambiguity; exclude from unqualified current-operating answers |

## Import files and metadata

[curated-manifest.json](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/curated-manifest.json>) contains **84 selected documents and 14 complete selected legal texts**. The comprehensive [catalogue.json](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/catalogue.json>) contains the wider discovery/acquisition inventory. Neither automatically validates every clause of every document.

Keep these fields for each document: source URL, source-page URL, legal entity, market, topic, service, document type, language, version, publication date, effective-from/to, retrieval date, SHA-256, knowledge layer, edition type, review scope and conflict note. Keep dates unknown where the evidence is missing. A future application date inside consolidated law still needs clause-level handling.

The manifest includes `default_retrieval` as a conservative suggested selection. It excludes the conflicting Athens master edition, the qualified Oslo VPO copy and future releases/programmes from ordinary current-state retrieval. It is a starting filter, not certification that all included passages are current.

The catalogue’s original `markets`, `topics`, `date_evidence` and priority fields were inferred during discovery. In particular, nearby table text can contain dates belonging to other rows. Prefer the manually selected `version_date_evidence`, `knowledge_layer` and `review_scope` fields. Entries without these fields are unvalidated candidates.

## Text preparation

1. Keep the original as the citation authority. The `extracted/` files are derivative text.
2. Deduplicate by content hash while preserving all source URLs and redirects. The catalogue records a canonical content ID for duplicates.
3. For PDFs, use chapter/article boundaries and preserve the one-based PDF page index. Do not split a requirement from its exceptions, footnotes or table headings. Text extraction has not validated diagram interpretation or complex table order.
4. Review `low_text_pages` before relying on a PDF. OCR and visual inspection remain necessary for any relevant scanned pages, diagrams or lost tables.
5. Legal browser captures include site navigation. Remove that for retrieval while preserving CELEX, consolidation date, article boundaries, amendment markers and source notices. Use only the 14 complete captures listed in the manifest; earlier attempts remain as research evidence and may be truncated.
6. Most XLSX/XLS/DOCX/ZIP files are archived only. Extract tables with headers and addresses, documents with their structure, and message-schema archives before indexing. The ESMA register is the exception: a cell-addressed JSON extraction is included.
7. For registers, interpret merged/continuation rows and multiple decisions carefully. Store authorisations, links and passports separately. Preserve malformed identifiers as source anomalies rather than silently repairing them.

## Answer format

Every operational answer should state **market/entity, service, as-of date and current/future status**, followed by the source document and exact article/section/page. If the question omits a material scope choice, provide the common framework and explain what differs locally.

For requirements, return: obligated role, action, condition/exception, deadline, evidence and citation. For procedures, return: inputs, actor, step, output, error/fail path, cut-off and source. For fees, state effective tariff, charging unit, currency and assumptions.

When source texts disagree, show the conflict. Normative law, local-language authoritative rules, contracts, operating instructions and programme descriptions have different roles; a generic publication-date sort cannot resolve their hierarchy. A programme presentation cannot override a local rule.

## Starter evaluation set

Use these questions to check retrieval quality before trusting an assistant built on the library:

| Question | Required behaviour |
|---|---|
| What are a CSD’s three core services? | Cite CSDR Annex A and distinguish the legal definition from ancillary services |
| Are all five Euronext CSDs operating on one platform today? | Separate current systems from Convergence and its indicative timetable |
| What changed in Copenhagen participant requirements in August 2026? | Retrieve the dated Part 2/3 editions; compare prior versions before claiming a specific change |
| Does an Oslo backup liquidity bank guarantee funding? | Retrieve the specific VPO clause, answer its meaning and disclose the linked copy’s approval qualification |
| How many years of financial statements are required for admission? | Ask/resolve Athens versus Porto; do not merge their requirements |
| Is Athens’ newest master rulebook Amendment 8? | Surface the hub/file/history conflict |
| Which Copenhagen fees apply in September 2026? | Select January schedule; exclude November future tariff |
| Is the June 2026 Settlement SDD today’s operating manual? | Identify Convergence future scope |
| What is the latest ESMA register date? | Use 0- Info!B12: 2 September 2026, not the URL folder |
| What is Porto’s LEI in the register? | Flag incomplete C25 and seek corroboration; do not invent missing characters |
| Is T+1 already operating? | State 11 October 2027 cycle application and separate earlier implementation milestones |
| Can a DCP dispense with CSD membership? | Explain technical access versus the continuing legal/service relationship using the local rules |
| Which exact message field should production use? | Use market/release-specific schema; disclose if the authoritative schema is client-only |

These are proposed checks, not a passed evaluation of a deployed system.

## Refresh procedure

Revisit canonical rulebook/manual hubs and current notices, then compare link targets and content hashes. Record changes as new versions, preserving old files and their effective periods. Recheck the ESMA register and EUR-Lex consolidation history; for T2S, verify the release’s status, not merely the upload date. Reconcile English translations with authoritative originals when a legal conclusion depends on wording.

The collection scripts cache this dated snapshot. They are acquisition provenance, not an installed update monitor. Use a new snapshot directory for a refresh and carry forward manual curation explicitly. No scheduled automation or external publication has been created.

## Portable starter pack

[starter-pack.zip](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/starter-pack.zip>) contains a smaller selection of foundational/legal and local operating sources, plus an index. It omits future programmes and the two unresolved master-rule copies. Use the full reading guide to add specialist tax, corporate-events, connectivity, message-schema and programme material as needed. Keep this research library private unless source permissions allow redistribution.
