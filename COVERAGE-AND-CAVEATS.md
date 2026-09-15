# Coverage and limitations

**Audit implementation update:** whole-document retrieval is disabled. The original inventory remains intact; reviewed sections and additional sources are listed in [the implementation report](IMPLEMENTATION-REPORT.md) and [the section register](retrieval/README.md). Historical counts below describe the original collection; the English DORA replacement is an additional legal capture.

Research snapshot: **11 September 2026**.

## What is in the library

| Measure | Count |
|---|---:|
| Document URL records | 918 |
| Retained original document files | 800 |
| Unique retained document contents after checksum deduplication | 787 |
| PDF files | 694 |
| PDF pages, including duplicate files | 29,084 |
| PDF pages after content deduplication | 28,629 |
| Selected reading-guide documents | 84 |
| Selected complete official legal-text captures | 14 |
| Source-page records with extracted links | 357 |

Original documents total approximately **648 MB** (decimal), excluding web snapshots, extracted text and the starter ZIP. These are acquisition counts, not pages substantively reviewed. Formats include 694 PDFs, 51 XLSX, 3 XLS, 38 DOCX and 14 ZIP files.

## Search and selection scope

The research mapped Euronext Securities’ group site and the public documentation hubs for all five CSDs. It followed current rulebooks, admission rules, operating/technical manuals, corporate events, account structures, links, fees, selected notices, disclosures and strategic programmes. The bounded Euronext/Athens crawl completed its eligible queue; additional regulatory/infrastructure sources were collected separately. Athens’ two regulatory pages were checked to capture the master rulebook and all 22 resolutions.

Primary supporting sources include EUR-Lex, ESMA, ECB/T2S/AMI-SeCo, BIS/CPMI-IOSCO and ECSDA. The complete selected legal texts were recovered through the browser where direct requests did not return the actual text.

The sweep was English-led and also retained locally linked non-English documents. It was not an exhaustive crawl of every language, archive page, external regulator site or historical notice pagination. “Most recent found” is grounded in the reviewed canonical hubs, dates and original files, not a guarantee that no newer client-only or unlinked document exists.

## Review depth

Selected admission, settlement, cash-account, governance and programme-scope passages were substantively reviewed to produce the synthesis. Other documents were catalogued and, for PDFs, text-extracted. The selected documents’ review scope and PDF page references are recorded in the manifest. Six core cover/history pages were visually inspected in [the retained contact sheet](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/verification/core-document-covers.png>).

Large technical manuals were not read page by page. Graphics, complex tables and low-text pages have not received comprehensive visual/OCR review. Most workbooks, DOCX files and ZIP schemas were archived without structured extraction. The ESMA register was separately read and exported to cell-addressed JSON; original workbooks were not modified.

## Material gaps

| Gap | Consequence and specific next evidence |
|---|---|
| Client-only operational documentation | MT-X, MyVPS, MyEuronext, CLIMP and MyStandards may contain newer specifications, entitlements and notices. Milan notice ON_36/2026 explicitly directs users to MT-X for technical details. |
| Athens version conflict | Obtain the authoritative current master rulebook and reconciled effective date; preserve the captured resolutions meanwhile. |
| Oslo VPO approval qualification | Confirm the current approved rule text and applicability with the authoritative local source. |
| Current national law / EEA details | Check current Greek, Danish, Italian, Norwegian and Portuguese originals and applicable EEA incorporation before entity-specific legal conclusions. Linked translations alone do not resolve this. |
| Production-specific implementation | Exact cut-offs, service entitlements, connection details, test acceptance and negotiated arrangements depend on the participant/service. |
| Tax and pricing depth | Manuals and tariffs are retained, but a complete jurisdiction-by-jurisdiction tax procedure or cost model has not been produced. |
| Source availability | Several Athens service pages returned 522; two obsolete/malformed service links returned 404. Their absence is not evidence that the service does not exist. Core rules were obtained. |
| Future law and release status | Recheck T+1 detailed RTS publication/application, November T2S drafts and local go-live confirmations as their dates approach. |
| Extractions and metadata | Automatic classifications and nearby table dates need manual validation before broad production ingestion. |

## Acquisition exceptions and recovery

Three timed-out Euronext documents were recovered, including the daily 11 September ISIN workbook. Oslo law/fee media pages were resolved to actual documents. The old ESMA PDF link resolves to the current register workbook. BIS’s legacy PDF paths returned HTML; the relocated official PFMI PDFs were obtained.

Six headshot image links were excluded from document acquisition. The issuer-services media download at `/en/media/4177/download` returned HTML and remains unresolved; it is not a substitute for an operating manual. Low-priority historical/background links can remain catalogued without a local download. All underlying URLs, retained results and errors remain in the catalogue/metadata.

No source collection can establish that a firm satisfies admission, regulatory or operational requirements without its own facts and evidence. The concrete deliverable here is a curated research library, a sourced conceptual/requirements map and an ingestion design.
