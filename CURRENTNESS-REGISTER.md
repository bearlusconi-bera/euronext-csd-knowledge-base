# Currentness and source conflicts

Research snapshot: **11 September 2026**; base review **13 September 2026**; scoped November publication review **14 September 2026**. Other sources have not been globally refreshed to 14 September. Publication date, upload date, effective date and programme go-live are separate facts. The library preserves originals and hashes so later changes to the same URL can be detected.

| Item | Evidence found | Treatment |
|---|---|---|
| ESMA CSD register | Workbook 0- Info!B12 and HTTP metadata both indicate 2 September 2026; URL contains 2025-10 | Use the workbook date, not the URL folder. Old PDF URL redirects to the same workbook. |
| ESMA register Porto identifier | 1- CSD authorisations!C25 contains `529900LG70TCA`, shorter than a valid full LEI | Preserve raw C25 and exclude it from identity joins. Independently verified GLEIF value: `529900LG70TCAGWCXT47`; see the [normalised record](implementation/2026-09-13/structured/interbolsa-identity.json). Raw cell is not silently repaired. |
| Athens master rulebook | English hub says Amendment 8; Greek hub says Edition 8. Sampled Greek/English histories identify seven amendments and the seventh’s 8 December 2025 effect. | Probable edition-versus-amendment labelling (inference), not an established operative-text contradiction. Identity/history excerpts only; independent HCMC decision/Gazette chain remains incomplete. |
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
| T2S documentation | June final documentation supports the stored operational baseline. The 13 September capture listed November drafts; the 14 September final-delivery cover confirms publication, with the final UDFS dated 11 September. | Separate historical draft status, final publication and deployment. The new final-publication section is reference/future evidence dated 14 September; November deployment and changed technical provisions remain unverified. See [the admitted review](ADVERSARIAL-REPAIRS.md). |
| EU T+1 | Regulation 2025/2075 specifies 11 October 2027 application. July 2026 ESMA statement describes detailed RTS under legislative scrutiny and a 7 December 2026 milestone. | Treat the adopted cycle law separately from Commission text C(2026)4640. Its Article 2 distinguishes 7 December 2026, 1 July 2027 and 11 October 2027 stages; final OJ publication/entry into force remains independently unverified. Only a qualified future-text excerpt is admitted. |
| PFMI | Foundational 2012 documents still linked by BIS | An older year is not evidence of obsolescence. BIS has moved its publication download paths. |
| Porto WFC / Athens PFMI | Porto WFC 2025 submitted January 2026; Athens PFMI dated December 2023 | Preserve reporting period and publication date. Do not infer current operating effectiveness from an old disclosure. |
| Legacy ESMA Q&A PDF | Legacy PDF coexists with interactive Q&A/single-rulebook resources | Keep PDF as dated reference; check the current answer-by-answer resource for interpretive questions. |
| Milan notice ON_36/2026 | Published 11 September 2026; planned 30 November changes, conditional on testing. Detailed specification points to MT-X. | Evidence of both future applicability and a client-document coverage gap. |

All local originals and source URLs above are linked in [READING-GUIDE.md](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/READING-GUIDE.md>). Registry evidence is retained in [cell-addressed workbook extraction](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/extracted/535f6a23062a-rows.json>). Programme sources: [Convergence](https://www.euronext.com/en/csd/strategic-projects/convergence-programme), [European Offering launch](https://www.euronext.com/en/news/confirmation-go-live-euronexts-new-settlement-model-september-2026), [ESMA CSDR hub](https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/central-securities-depositories), [ECB T2S documentation](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/html/index.en.html).

## Applied source controls

| Source issue | Implemented treatment |
|---|---|
| Milan timetable versus current T2S | June 2025 English PDF 13/15 and corresponding Italian passages retain 19:30/two-window values; current T2S baseline is 20:00/five windows. Quarantine those local clock claims. The notice chain for actual Milan participant deadlines remains unresolved. |
| Dated T2S exceptions | 8 September 2026 events are stored individually. The 15:30 notice announced EUR IDVP at 17:00; the 18:55 update reports IFOP closed at 18:39. Announcement, occurrence and event-update relationships remain separate. Other business dates are not inferred. |
| Matching diagrams omitted from text | PDF 269–270 Diagrams 55–57 were visually transcribed, including all 23 rows, cash-field branches, case sensitivity and client-code conditions. This repairs functional matching evidence, not production XSD certification. |
| DORA language | Original English-labelled consolidated capture has French operative text. Preserved and tagged `fr`; reviewed English Articles 2 and 64 use the English OJ replacement. |
| Offering ISIN workbook | Original retained; all nonempty cached cells and merged ranges extracted. Introduction and column/date scope can answer reference questions. No row is admitted as universal current Milan eligibility. |
| Porto calendar | Notice 25/1162 dated 17 November 2025 was obtained and reviewed. It expressly retains May 1, 2026 FoP settlement. No inference that all services/currencies are open. |
| Porto timetable | Notice 394/2024 obtained: paragraph 15 gives 17 April 2024 effect and paragraph 14 revokes 611/2021. Its English translation is expressly nonbinding. Original clock values and the website’s CET table are not silently merged; Portuguese original/time convention and day-specific exceptions remain dependencies. |
| Porto report identifier | Manual PDF 66 prints `semt.07`. Preserve as a source anomaly; do not fabricate its full production identifier. Exact local schemas remain separately scoped. |
| Archive contents | 14 containers inspected/staged as 162 members; one container is an XLSX package by content. No member or schema receives automatic admission. |
| Whole-document defaults | All disabled. Only the named evidence sections are eligible under their scope, mode and verified snapshot. |

Use [the section register](retrieval/README.md) and [latest repair results](ADVERSARIAL-REPAIRS.md). Historical statements in the original audits are retained as audit evidence, not overwritten by these corrections.

## 14 September 2026 recheck (settlement-agent snapshot)

Research date **14 September 2026**. All 19 directly fetchable registered documents are byte-identical to the register (see `implementation/2026-09-14-settlement-agent/recheck/recheck-report.json`). Direct HTTP to EUR-Lex returns 202 challenge pages; the in-app browser reached EUR-Lex.

| Item | Evidence found on 14 September | Treatment |
|---|---|---|
| T2S R2026.JUN deployment | Milan ON_20/2026 (11 June): production release 12 June, effective 15 June 2026; ECB status entries 12–14 June record closure and completion | Deployed baseline confirmed from two sources; section effective dates keep the ECB completion date |
| T2S R2026.NOV | ECB SDD hub lists the final documents dated 14 September; Milan ON_28/2026 and the 10 August notice plan production deployment on 14 November, effective 16 November 2026; sentence-level comparison of the admitted June sections with the November text found no substantive change (formatting differences only) | Published future release; deployment not verified; November sections admitted in future/reference mode only |
| ECB T2S status history | Routine entries for 12 and 14 September added since the 13 September capture; no new incidents after 8 September | Dated overlays admitted for 17 non-routine business dates and a routine-only list (weekdays to 14 September) with currency scope ALL; business-date attribution of evening entries is a labelled inference |
| Milan operational notices | 20 notices from December 2025 to 11 September 2026 reviewed by title; 14 admitted | No notice restates participant cut-offs after R2026.JUN; §1.3.1 of the Settlement Instructions stays quarantined (G01) |
| Milan X-TRM standards | ON_11/2026 and ON_20/2026 identify Standard for X-TRM Users A2A/RNI VER.01.09 (final version June 2026) in MT-X; ON_36/2026 plans a 30 November update | Version identity admitted; content client-only (G03) |
| RTS 2017/392 capture | The library's consolidated EN capture contains German text; EUR-Lex served German for the EN consolidated URL on 14 September | Capture relabelled `de`; English Article 1 definitions captured from the original act through the browser and admitted as a reference section |
| GLEIF Interbolsa record | Only the golden-copy publish date changed | Identity unchanged |
| Porto notices hub | Registry notices only (11–14 September) | No timetable change found |
| Copenhagen, Athens, Oslo hubs | Linked rulebooks and resolutions unchanged | Edition/approval gaps unchanged (G07, G08, G10) |
| Milan European Offering | MN_07/2026 (8 September) confirms go-live 21 September 2026, first ISD 23 September | Future mode; not live on 14 September |
