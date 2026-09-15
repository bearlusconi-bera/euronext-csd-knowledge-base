# Audit implementation results

This records the first implementation state. The subsequent adversarial findings are addressed in [the 14 September repair report](ADVERSARIAL-REPAIRS.md), including the separately dated November final-publication evidence and updated test results.

**Implemented 14 September 2026, using the reviewed 13 September evidence snapshot.** The library now admits specific evidence sections and enforces their scope through a local command. It remains a dated, bounded research system; complete production instructions across all five CSDs are not certified.

## What changed

- Preserved all 800 original documents and the independent audit. Disabled every whole-document default.
- Added 30 reviewed sections from 24 source identities, with separate current/reference/future exports, exact locators, source hashes and dependency checks.
- Repaired all three matching-field diagrams, the DORA language issue, workbook scope, dated ECB events and Interbolsa entity normalisation.
- Obtained Porto’s underlying calendar and timetable notices. Kept the timetable translation/time convention qualified.
- Corrected the currentness register, requirements map and cross-CSD explanation. Added project instructions for future AI use.
- Staged 162 members from 14 archive containers, identified one XLSX package and recorded XML/import dependencies without admitting unreviewed schema fields.
- Guarded historical builders so they cannot restore broad defaults or overwrite the corrected guides.

## Verification

**34/34 scoped retrieval cases and 39/39 integrity/control checks passed.** Of the 34 cases, 28 returned scoped evidence and six correctly blocked unsupported requests. All 800 originals matched their pre-audit hashes. Source-tampering, cross-market leakage, missing context, release mismatch, date rollover, event/currency mismatch and lost dependencies were tested.

These results test explicit question routing and evidence selection. No LLM answer service is deployed, so the original audit’s answer-quality tests remain **NOT RUN**. A correctly retrieved excerpt is not proof of a correct generated answer. See [actual test results](implementation/2026-09-13/verification/VERIFICATION.md).

The evidence package also passed archive CRC, member-hash, section-coverage and dependency checks. It contains 17 current, 11 reference and four future sections; two sections occur in both reference and future modes, giving 30 distinct sections. See [package verification](implementation/2026-09-13/verification/package-verification.json).

## Findings addressed

| Finding | Status | Applied change |
|---|---|---|
| F01 | Mitigated; authority gap remains | Quarantined the English/Italian Milan clock passages. Platform schedule is separately scoped; exact Milan participant cut-offs are blocked pending G01. |
| F02 | Implemented for the reviewed event date | Ingested all displayed 8 September events; separated announced IDVP, actual IFOP and superseding incident updates. Other dates/currencies require evidence. |
| F03 | Implemented | Disabled whole-workbook admission; preserved all extracted cells/merges and scoped Introduction evidence. Future place columns do not establish universal current eligibility. |
| F04 | Implemented | Disabled every whole-document default. Added 30 section decisions, hash-bound exports, scope/mode/date filters, dependencies and local retrieval. Historical builders cannot overwrite controls. |
| F05 | Critical repairs implemented; wider extraction remains scoped | Visually repaired Diagrams 55–57 (23 rows plus notes). Staged 162 members from 14 containers; XML/import inspection does not grant schema admission. Unreviewed diagrams/tables remain outside their permitted propositions. |
| F06 | English evidence repaired; reporting chain incomplete | Tagged original DORA body French and added the English OJ replacement. Only Articles 2/64 admitted; full reporting RTS/ITS/national chain remains G06. |
| F07 | Interpretation corrected; approval gap remains | Narrowed Athens warning to probable edition/amendment labelling, explicitly an inference. Kept history-only admission; independent HCMC/Gazette verification remains G08. |
| F08 | Mitigated; approval gap remains | Retained Oslo edition reservation and forced it to accompany reference-mode liquidity descriptions. Unconditional approval/current duties remain blocked. |
| F09 | Implemented | Kept November drafts, adopted T+1 law and Commission future-stage text separate. Publication/application/deployment are distinct; clock rollover does not promote a source. |
| F10 | Implemented metadata controls; some authority gaps remain | Preserved cover/footer/file/upload distinctions, unknown Porto effective date and tariff periods. Exact fee amounts require a reviewed row. Added Porto underlying timetable/calendar notices. |
| F11 | Implemented | Confirmed the full Interbolsa LEI with GLEIF and checksum. Preserved malformed ESMA C25; separately sourced normalisation and decision rows prevent identity/permission conflation. |
| F12 | Controls and dependency register implemented; broader coverage incomplete | Mapped all 17 dependencies, reviewed additional public provisions and blocked unsupported production questions. No client portal or firm entitlements were assumed. |

## What still needs authoritative material

The highest-priority open dependency is the current Milan participant timetable/notice chain. Oslo edition approval and the independent Athens approval chain also remain unresolved. Exact production fields, instrument eligibility, client entitlements and complete tax/fee/reporting procedures remain blocked where their governing evidence is missing or unreviewed. All 17 dependencies have an explicit outcome in [the dependency register](implementation/2026-09-13/REMAINING-DEPENDENCIES.md).

The wider audit’s 83-question coverage matrix is retained as the backlog. Adding filters does not close those coverage gaps; each additional question must earn an admitted source section. Public layout review was selective, not a certification of every field in every manual.

## Use the result

Start with [the knowledge-base instructions](KNOWLEDGE-BASE-DESIGN.md) and [section index](retrieval/README.md). The [reviewed evidence pack](reviewed-evidence-pack.zip) separates current, reference and future material. Its metadata must be enforced by any receiving AI platform. The old starter pack remains a historical full-document reference collection.

The local retrieval command requires an explicit as-of date; a different date prompts source revalidation. No monitor or scheduled task was created.

## Added/repaired source provenance

The original 800-document inventory remains unchanged. Audit and implementation additions are registered below; identical URLs and translations are not counted as independent corroboration.

| Source ID | Original/source | Saved evidence |
|---|---|---|
| ecb-status-2026 | [ecb-status-2026](https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html) | [Saved original](implementation/2026-09-13/sources/ecb-status-2026.html) |
| dora-english-oj | [Regulation - 2022/2554 - EN - DORA - EUR-Lex Log in English](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) | [Saved original](audits/2026-09-13/sources/dora-english-oj.html) |
| ecb-sdd-hub | [ecb-sdd-hub](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/html/index.en.html) | [Saved original](implementation/2026-09-13/sources/ecb-sdd-hub.html) |
| athens-greek-master | [athens-greek-master](https://athens.euronext.com/sites/default/files/2026-06/%CE%9A%CE%91%CE%9D%CE%9F%CE%9D%CE%99%CE%A3%CE%9C%CE%9F%CE%A3_%CE%9B%CE%95%CE%99%CE%A4%CE%9F%CE%A5%CE%A1%CE%93%CE%99%CE%91%CE%A3_%CE%95%CE%9B%CE%9A%CE%91%CE%A4_7%CE%B7_%CE%A4%CF%81%CE%BF%CF%80%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_383_24.11.2025_%CE%99%CE%A3%CE%A7%CE%A5%CE%A3_8.12.2025.pdf) | [Saved original](audits/2026-09-13/sources/athens-greek-master.pdf) |
| porto-calendar-notice | [porto-calendar-notice](https://www.euronext.com/en/post-trade/es-porto/notices/251162) | [Saved original](implementation/2026-09-13/sources/porto-calendar-notice.html) |
| porto-timetable-notice | [porto-timetable-notice](https://www.euronext.com/en/media/11820/download) | [Saved original](implementation/2026-09-13/sources/porto-timetable-notice.pdf) |
| gleif-interbolsa | [gleif-interbolsa](https://api.gleif.org/api/v1/lei-records/529900LG70TCAGWCXT47) | [Saved original](implementation/2026-09-13/sources/gleif-interbolsa.json) |
| 591deafae0a9 | [EUR-Lex - C(2026)4640 - EN - EUR-Lex Log in English](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=PI_COM%3AC%282026%294640) | [Saved original](audits/2026-09-13/sources/591deafae0a9.html) |

All selected source identities, hashes and locators are in [the source register](retrieval/source-register.json). Review decisions and actual excerpt contents are separately inspectable. No entire manual was certified by this implementation.
