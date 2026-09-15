# Currentness and source conflicts

Snapshot: **11 September 2026**. Publication date, upload date, effective date and programme go-live are separate facts. The library preserves originals and hashes so later changes to the same URL can be detected.

| Item | Evidence found | Treatment |
|---|---|---|
| ESMA CSD register | Workbook 0- Info!B12 and HTTP metadata both indicate 2 September 2026; URL contains 2025-10 | Use the workbook date, not the URL folder. Old PDF URL redirects to the same workbook. |
| ESMA register Porto identifier | 1- CSD authorisations!C25 contains `529900LG70TCA`, shorter than a valid full LEI | Preserve original; exclude that value from validated entity master data until confirmed elsewhere. |
| Athens master rulebook | Hub labels Amendment 8; linked filename and internal history indicate 7th amendment. History includes November/December 2025 signals; filename also carries an in-force date. | Latest linked copy retained, but no authoritative single version/effective date asserted. Excluded from default retrieval allowlist. |
| Athens individual resolutions | All 22 resolutions found across two regulatory pages, including 2026 updates | Prefer resolution-specific effective dates. Greek originals prevail over informational English translations. |
| Copenhagen Part 2 | Cover: 3 August 2026; footers show inconsistent version numbers | Identify by cover date and checksum, retaining the discrepancy. |
| Copenhagen fees | January 2026 and November 2026 tables both public | November table is future at the research date. |
| Oslo VPO NOK rules | Current legal hub links 2 September 2024 text whose cover retains an approval qualification | Retain as latest linked public copy; verify authoritative approval/version before treating as binding. |
| Porto Operational Manual | V43; internal date 26 January 2026; filename 16 February; upload April | Keep all three signals. Avoid a fabricated single publication date. |
| Porto Regulation 1/2017 | This is a revocation of a prior pricing regulation, not a book-entry rulebook | Not selected as the operating baseline. Rule numbers alone do not identify subject matter. |
| Porto Regulation 1/2018 | Securities Lending Management System | Classify as lending, not a generic tax regulation. |
| European Offering | Confirmed new settlement-model launch on 21 September 2026 | Future rollout as of 11 September; some underlying services may already be available. |
| Convergence | June/August 2026 specifications describe a future common platform; indicative migration schedule starts in 2028 | Future-programme collection. Never use these alone to describe today’s five local systems. |
| Convergence roadmap | Programme page retains a stale June-confirmation qualifier. July Athens newsletter specifies indicative H2 2029 and late-2028 testing. | Retain market-specific dated updates and label plans provisional. |
| T2S documentation | R2026.JUN final documentation dated 22 January; R2026.NOV documents released 3 August for market review | June baseline and November future drafts are separate. |
| EU T+1 | Regulation 2025/2075 specifies 11 October 2027 application. July 2026 ESMA statement describes detailed RTS under legislative scrutiny and a 7 December 2026 milestone. | Treat the cycle date and RTS legal process separately; check final OJ act and application provisions before asserting detailed duties are operative. |
| PFMI | Foundational 2012 documents still linked by BIS | An older year is not evidence of obsolescence. BIS has moved its publication download paths. |
| Porto WFC / Athens PFMI | Porto WFC 2025 submitted January 2026; Athens PFMI dated December 2023 | Preserve reporting period and publication date. Do not infer current operating effectiveness from an old disclosure. |
| Legacy ESMA Q&A PDF | Legacy PDF coexists with interactive Q&A/single-rulebook resources | Keep PDF as dated reference; check the current answer-by-answer resource for interpretive questions. |
| Milan notice ON_36/2026 | Published 11 September 2026; planned 30 November changes, conditional on testing. Detailed specification points to MT-X. | Evidence of both future applicability and a client-document coverage gap. |

All local originals and source URLs above are linked in [READING-GUIDE.md](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/READING-GUIDE.md>). Registry evidence is retained in [cell-addressed workbook extraction](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/extracted/535f6a23062a-rows.json>). Programme sources: [Convergence](https://www.euronext.com/en/csd/strategic-projects/convergence-programme), [European Offering launch](https://www.euronext.com/en/news/confirmation-go-live-euronexts-new-settlement-model-september-2026), [ESMA CSDR hub](https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/central-securities-depositories), [ECB T2S documentation](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/html/index.en.html).
