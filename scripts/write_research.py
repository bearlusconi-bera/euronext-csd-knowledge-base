"""Write the research synthesis with links to retained originals and primary sources."""
import json,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1]
from snapshot_guard import refuse_audited_snapshot
refuse_audited_snapshot(R)
C=json.loads((R/'catalogue.json').read_text()); B={d['id']:d for d in C}
M=json.loads((R/'curated-manifest.json').read_text());stats=json.loads((R/'verification/library-stats.json').read_text())
def f(p,label=None):return f'[{label or p}](<{R/p}>)'
def d(id,label=None):return f'[{label or B[id]["title"]}](<{R/B[id]["local_path"]}>)'
def u(id,label=None):return f'[{label or B[id]["title"]}]({B[id]["url"]})'
def w(p,s):(R/p).write_text(s.strip()+'\n')
csdr='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117'
reg=f'[CSDR, consolidated 17 January 2026]({csdr})'
group='https://www.euronext.com/en/csd'
conv='https://www.euronext.com/en/csd/strategic-projects/convergence-programme'
golive='https://www.euronext.com/en/news/confirmation-go-live-euronexts-new-settlement-model-september-2026'

w('HOW-CSD-WORKS.md',f'''
# How Euronext’s CSDs work

Research synthesis, **11 September 2026**. Read this with the linked local rules. It explains the architecture and the practical questions a knowledge base should answer; it is not a determination of a particular firm’s permissions.

## Five CSDs, with separate local operating rules

Euronext’s current CSD group includes Athens, Copenhagen, Milan, Oslo and Porto. A shared brand and planned common platform do not remove the need to identify the legal entity, market and service before answering an operational question. [Euronext Securities overview]({group}).

| Market | Legal entity named in local materials | Main current sources | Cash/settlement distinction established in the reviewed sources |
|---|---|---|---|
| Athens | Hellenic Central Securities Depository S.A. / ATHEXCSD | Master rulebook and 22 resolutions | DSS settlement and euro cash via TARGET-GR arrangements; specific non-euro routes |
| Copenhagen | VP Securities A/S | Six-part rulebook | Both VP and T2S arrangements; EUR and DKK T2S settlement |
| Milan | Monte Titoli S.p.A. | Service Regulations, CSD Instructions, Settlement Instructions | T2S settlement; gateway links add route-specific procedures |
| Oslo | Verdipapirsentralen ASA | Registration Rules and VPO NOK Rules | VPS securities records and NOK cash settlement at Norges Bank/NBO |
| Porto | Interbolsa – Sociedade Gestora de Sistemas de Liquidação e de Sistemas Centralizados de Valores Mobiliários, S.A. | Local regulations, Operational Manual and technical layouts | T2S arrangements and separately specified foreign-currency services |

Sources: {d('410859953fce','Athens Resolution 5, PDF pp. 3–4')}; {d('3d76a327339b','Copenhagen Part 4, PDF pp. 3–6')}; {d('8719262f5e8b','Milan Service Regulations')}; {d('14dc34b8e54e','Oslo VPO NOK, PDF pp. 13–19')}; {d('089b7aaef991','Porto Operational Manual, PDF pp. 15–17')}. Oslo’s linked English VPO copy retains an approval qualification; see the currentness register.

For authorisation questions, consult the **ESMA register dated 2 September 2026**, especially the authorisations, links and passports tabs. Some CSDs have several decision rows. Do not collapse those rows to a single initial authorisation. The workbook identifies recent Milan extensions, including a July 2026 decision. {d('535f6a23062a','Saved ESMA register')} and [official register landing page](https://www.esma.europa.eu/document/csd-register).

## The three core functions

**Initial recording** establishes an issue in book-entry form. **Central maintenance** maintains securities accounts at the top tier. **Settlement** completes transfers in a securities settlement system. Under CSDR, a CSD operates a settlement system and provides at least one of the other two core services. These functions are distinct from executing a trade, clearing it through a CCP, or providing a retail brokerage account. {reg}, Article 2 and Annex Section A.

An issuance workflow therefore needs the issuer, issue terms, identifiers, eligible security type, appointed agents and initial account postings. The ongoing ledger must remain consistent with the issued quantity. CSDR requires at least daily reconciliation and prohibits securities overdrafts or unauthorised securities creation within the settlement system. {reg}, Article 37; {d('4e7eec1c51e0','Porto general operating rules')}.

## A typical settlement workflow

This is an explanatory sequence. Its exact messages, cut-offs and finality points depend on the local system and instruction type.

1. The trading/clearing chain determines what securities and cash are due, by whom, and on which settlement date.
2. Parties or their agents submit instructions using the required instrument, account, counterparty, place-of-settlement and cash details.
3. The system validates instructions and matches the required fields. Acceptance or matching alone does not establish final settlement.
4. Securities and cash availability, instruction controls, priorities and system timing determine whether settlement can complete. Some services support partial settlement, hold/release or collateralisation, with local conditions.
5. Delivery-versus-payment links the securities and cash obligations. Finality depends on the system’s legal rules, including entry and irrevocability points.
6. Participants reconcile confirmations and balances. Unsettled instructions require investigation, funding/securities remediation and, where applicable, penalty processing.

Operational source trail: {d('dd1cf7cb930b','Milan Settlement Instructions')}, {d('3d76a327339b','Copenhagen Part 4')}, {d('089b7aaef991','Porto Operational Manual')}, {d('410859953fce','Athens Resolution 5')} and {d('14dc34b8e54e','Oslo VPO NOK rules')}. The legal foundations for finality and cash settlement are CSDR Articles 39–40 and the [Settlement Finality Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408).

## The cash leg matters as much as the securities leg

CSDR favours the relevant central-bank accounts where practical and available, while providing a framework for other cash arrangements. A technical connection does not itself provide cash, credit or a settlement-bank relationship. Treat currency, cash account, provider and funding responsibility as separate data fields. {reg}, Articles 40 and 54.

In Oslo, the reviewed rules describe settlement participants, liquidity banks and substitute arrangements. A substitute-liquidity-bank declaration is expressly not a funding guarantee. In Porto, affiliation procedures include appropriate cash-settlement account arrangements. These are concrete reasons to model liquidity dependencies in a participant knowledge base. {d('14dc34b8e54e','Oslo VPO NOK, PDF pp. 16–19')}; {d('089b7aaef991','Porto Manual, PDF pp. 15–17')}.

## Accounts, segregation and ownership

An account’s technical identifier, its segregation category and the legal identity of an owner are different facts. CSDR Article 38 addresses participant/client segregation and the choice between omnibus and individual client segregation, including disclosure of costs and protection. Local registration law and account-operator rules add further meaning. {reg}, Article 38; {d('838261c7c0d4','Oslo Registration Rules')}; {d('16ded02d7a65','Copenhagen Book-entry Rules')}.

The European Offering’s account guide shows how market conventions affect account structures, including French registered-share arrangements. Its rules are tied to the Milan-based offering. They cannot be applied automatically to every account elsewhere in the group. {d('00a3e1aeba1c','European Offering Account Structure V03, PDF pp. 3–5')}.

## Asset servicing continues after settlement

Corporate events include cash or securities distributions, reorganisations and elective events. Their workflows involve eligibility dates, entitlements, elections, payments and sometimes adjustments to pending transactions. The corporate-events handbook distinguishes issuer, issuer-agent, paying-agent and investor-CSD responsibilities. When a CSD holds through another CSD, upstream information and local market practice affect processing. {d('e1354fb2d76a','Corporate Events Processes Handbook V05, PDF pp. 16–17')}.

The July 2026 T+1 corporate-events guide is particularly useful for understanding how a shorter cycle changes key dates, market claims, transformations and buyer protection. Its purpose is future implementation. {d('a46c6c66a0e4','AMI-SeCo T+1 Corporate Events Guide, PDF pp. 1–5')}.

## T2S and cross-border links

T2S provides common settlement infrastructure. The local CSD relationship, account responsibilities and applicable rules still matter. Porto’s manual distinguishes directly connected participants (DCPs) from indirectly connected participants (ICPs). Direct technical access does not remove the CSD’s oversight. {d('089b7aaef991','Porto Manual, PDF pp. 15–17')}.

Keep three routes separate: settlement within one CSD, settlement across CSDs on T2S, and settlement through an external/non-T2S link. The Convergence settlement specification explains these distinctions, but describes a future platform. For a transaction today, use the local manual, current link/eligibility data and current T2S release. {d('71233aed41e7','Convergence Settlement SDD, PDF pp. 8–13')}; {d('1bd67deaace2','Milan T2S Gateway settlement links')}; {d('aa3d5a3b94c9','T2S UDFS R2026.JUN')}.

## Three changes that must remain separate

| Change | State at 11 September 2026 | Knowledge-base treatment |
|---|---|---|
| European Offering / new Euronext settlement model | Announced start 21 September 2026, using Milan for the expanded offering. The announcement covers Amsterdam, Brussels and Paris equity/ETP euro transactions and preserves choice of alternative CSDs. | Future rollout with specific markets, instruments and service scope |
| Convergence | Planned common platform over a longer horizon. Programme page gives Copenhagen first in August 2028, Porto in 2028, Milan/Athens in 2029; Oslo timing depends on a Norges Bank T2S decision. July Athens newsletter specifies indicative H2 2029. | Future architecture; keep local migration targets provisional |
| EU T+1 | Shorter cycle applies from 11 October 2027. ESMA’s July 2026 statement identifies an earlier 7 December 2026 allocation/confirmation milestone in the regulatory transition. | Separate the legislated cycle date from detailed RTS adoption/application status |

Sources: [new settlement model announcement]({golive}); [Convergence programme]({conv}); {d('9a9900fa74db','Athens July newsletter')}; [T+1 amendment](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2075); {d('f488a7016d8c','ESMA July statement')}. The programme webpage retains an old “dates to be confirmed” qualifier, so its schedule should not be represented as a binding commitment.
''')

w('REQUIREMENTS-MAP.md',f'''
# Requirements map

As of **11 September 2026**. “CSD requirements” has three meanings: requirements for the infrastructure operator, requirements to participate, and requirements for an issuer/service user. Store these as separate roles. The tables below are research navigation and evidence checklists; they are not a complete application dossier for an unspecified business.

## 1. Operating a CSD

| Requirement area | Evidence to collect in the knowledge base | Primary legal anchor |
|---|---|---|
| Authorisation and permitted services | Legal entity, home jurisdiction, authority, decision, approved core/ancillary services, instruments and subsequent changes | CSDR Articles 16–19; ESMA register; RTS 2017/392 and ITS 2017/394 |
| Governance and compliance | Governance structure, conflicts management, controls, management suitability and public rules | CSDR Articles 26–29 |
| Record keeping and outsourcing | Record-retention controls, service providers, contractual responsibilities and oversight | CSDR Articles 29–30; relevant technical standards |
| Fair participation and transparent charges | Admission criteria, response/refusal procedures, user rights and service-level fees | CSDR Articles 33–35 |
| Integrity and safeguarding | Reconciliation processes, issue balances, participant/client segregation, disclosures and consent controls | CSDR Articles 37–38 |
| Settlement and finality | Entry/irrevocability/finality rules, DvP, cash provider and currency arrangements | CSDR Articles 39–40; Settlement Finality Directive and national implementation |
| Participant default | Default triggers, responsibilities, public procedures and periodic testing | CSDR Article 41 |
| Risk, resilience and capital | Legal/operational/business risk, recovery, accessible financial resources, risk-based capital and orderly wind-down | CSDR Articles 42–47; RTS 2017/390; DORA |
| Net settlement and links | Netting design, credit/liquidity risk, linked-CSD legal arrangements, reconciliations and additional intermediary risk | CSDR Articles 47a–48 |
| Cross-border service | Passport/recognition permissions and the securities’ applicable law | CSDR Articles 23, 25, 49; ESMA passports/links data |
| Banking-type ancillary services | Additional permissions, authorised designated provider, applicable prudential requirements | CSDR Title IV, including Article 54 |

Read the actual articles and referenced instruments in {reg}. Saved complete texts and links are in the {f('READING-GUIDE.md','reading guide')}. The selected CSDR provisions were reviewed, but the complete capital calculation, national transpositions and every implementing requirement were not assessed.

**DORA is part of the operating framework.** CSDR Article 45 now explicitly references it for ICT risk and recovery. A knowledge base focused only on connectivity specifications would omit incident handling, resilience testing and ICT third-party dependencies. [DORA consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02022R2554-20221227).

Use the PFMI as a cross-cutting control taxonomy, then map it to binding rules and local evidence. Porto’s WFC questionnaire and Athens’ PFMI self-assessment provide examples of disclosed controls; their dates matter, and disclosure is not independent proof that a control remains effective. {d('1ae6d477d17b','PFMI')}; {d('2a1af673b358','Porto WFC 2025')}; {d('3cfbaea6fa93','Athens December 2023 PFMI assessment')}.

## 2. Becoming and remaining a participant

| Workstream | Common evidence fields | Market differences established by the review |
|---|---|---|
| Eligible entity and permitted role | Regulatory status, jurisdiction, role, LEI, scope of requested services | Copenhagen distinguishes participant roles, including issuing agents and securities-account controllers. Oslo ties settlement access to specified institution categories and account-operator arrangements. |
| Legal admission | Application, constitutional documents, representatives, signatures, contracts and foreign-law opinions where required | Athens uses application approval, preparation and activation stages. Foreign documents may require specified authentication. |
| Financial/organisational capacity | Financial statements, staffing, operational capacity, controls and ongoing change notifications | Athens Resolution 1 asks for the last two years’ financial statements; Porto’s manual refers to annual reports for the last three years. Do not merge these into one group-wide requirement. |
| Personnel and permissions | Authorised users, role lists, qualified contacts and required certification | Athens Resolution 2 requires at least one CSA-certified employee/executive, with stated exemptions. Copenhagen requires competent and appropriately authorised users. |
| Accounts and cash | Securities accounts, account operators, currencies, settlement-bank contracts, central-bank accounts or service-provider arrangements | Oslo specifies liquidity-bank and substitute arrangements; Porto specifies relevant cash account arrangements. Technical connectivity is insufficient on its own. |
| Technical readiness | Production/test access, interfaces, identifiers, message validation, reconciliation, security and contingency channels | Milan requires successful configuration/operating tests before activation. DCP and ICP requirements differ. |
| Testing and continuity | End-to-end tests, emergency arrangements, recovery roles and ongoing exercises | Copenhagen’s CSD-link admission provisions include operational testing and emergency arrangements; current local obligations must be read separately from Convergence testing plans. |
| Ongoing operations | Funding/securities availability, cut-offs, matching, fail handling, fees and notifications | Use the current local calendar, notices and tariffs; these can change faster than the rulebook. |

Evidence: {d('8719262f5e8b','Milan Regulations, PDF pp. 13–16')}; {d('cbdf3c1f8b51','Copenhagen Part 2, PDF pp. 2–5')}; {d('14dc34b8e54e','Oslo VPO NOK, PDF pp. 13–19')}; {d('089b7aaef991','Porto Manual, PDF pp. 15–17')}; {d('dab1b35a93c5','Athens Resolution 1, PDF pp. 1–4')}; {d('513a8da7c0ad','Athens Resolution 2, PDF pp. 1–2')}.

Keep **response to an access request**, **approval**, **testing completion** and **activation** separate. A regulatory response deadline is not a promise of operational go-live. Where you need a specific onboarding schedule, resolve the entity, requested role, complete-documentation date and service dependencies first. CSDR Article 33 and the local admission provisions above provide the source trail.

## 3. Issuing securities and using issuer services

| Requirement area | Questions the knowledge base should resolve | Where to start |
|---|---|---|
| Eligible issuer and instrument | Which legal forms, instruments, jurisdictions and recording arrangements are accepted? | Local rulebook, service instructions, current instrument eligibility lists |
| Agents and contracts | Is an issuing agent, registrar or paying agent needed, and who contracts with whom? | Local issuer rules and agreements; Copenhagen Part 2; asset-servicing handbook |
| Identifiers and initial recording | Who assigns/validates identifiers, supplies terms and reconciles issued quantities? | Local issuance instructions and numbering-agency material |
| Account/registration model | Bearer or registered security, account type, ownership records, nominee structure and disclosures? | Local registration law and account rules; market-specific European Offering documents |
| Corporate events | Who announces the event, provides funds/securities, processes elections and reconciles entitlements? | Local rules, corporate-events handbook, service cut-offs and current notices |
| Fees and tax services | Which issuer tariff and optional service terms apply? What tax documents/deadlines apply to the specific event/jurisdiction? | Separate issuer fee books and jurisdiction-specific tax manuals |

The handbook’s general actor descriptions must be reconciled with local contracts. For example, a common description of an issuer’s relationship does not override Copenhagen’s specific tri-party arrangements. The handbook also names four CSDs, so its coverage should not be assumed to include Athens. {d('cbdf3c1f8b51','Copenhagen Part 2')}; {d('e1354fb2d76a','Corporate Events Handbook')}.

## Scope fields to attach to every requirement

Use: **obligated role → legal entity → jurisdiction → service → instrument/currency → account/connectivity model → effective period → source clause → exceptions → evidence needed**.

Example: Athens / participant / personnel certification / Resolution 2 / effective 20 July 2026 / CSA-qualified employee or executive / retain stated exemptions. This is a researched local requirement, not a universal condition for all five CSDs.

## Questions still requiring additional evidence

Exact production message schemas and entitlements; negotiated/member-only operating documents; current national-law originals and EEA incorporation details; complete tax procedures; service-specific cut-offs; actual client test acceptance; and the firm’s own eligibility. These are tracked in {f('COVERAGE-AND-CAVEATS.md')} rather than inferred from marketing pages.
''')

w('CURRENTNESS-REGISTER.md',f'''
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

All local originals and source URLs above are linked in {f('READING-GUIDE.md')}. Registry evidence is retained in {f('extracted/535f6a23062a-rows.json','cell-addressed workbook extraction')}. Programme sources: [Convergence]({conv}), [European Offering launch]({golive}), [ESMA CSDR hub](https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/central-securities-depositories), [ECB T2S documentation](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/html/index.en.html).
''')

w('KNOWLEDGE-BASE-DESIGN.md',f'''
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

{f('curated-manifest.json')} contains **84 selected documents and 14 complete selected legal texts**. The comprehensive {f('catalogue.json')} contains the wider discovery/acquisition inventory. Neither automatically validates every clause of every document.

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

{f('starter-pack.zip')} contains a smaller selection of foundational/legal and local operating sources, plus an index. It omits future programmes and the two unresolved master-rule copies. Use the full reading guide to add specialist tax, corporate-events, connectivity, message-schema and programme material as needed. Keep this research library private unless source permissions allow redistribution.
''')

failed=[]
for p in (R/'metadata').glob('*.json'):
    v=json.loads(p.read_text())
    if isinstance(v,dict) and v.get('url') and v.get('http_status',200)>=400:failed.append(v)
dump_path=R/'verification/page-failures.json';dump_path.write_text(json.dumps(failed,indent=2))
w('COVERAGE-AND-CAVEATS.md',f'''
# Coverage and limitations

Research snapshot: **11 September 2026**.

## What is in the library

| Measure | Count |
|---|---:|
| Document URL records | {stats['catalogued_document_urls']:,} |
| Retained original document files | {stats['retained_document_files']:,} |
| Unique retained document contents after checksum deduplication | {stats['unique_retained_contents']:,} |
| PDF files | {stats['pdf_files']:,} |
| PDF pages, including duplicate files | {stats['pdf_pages_including_duplicate_files']:,} |
| PDF pages after content deduplication | {stats['unique_pdf_pages']:,} |
| Selected reading-guide documents | {stats['curated_documents']} |
| Selected complete official legal-text captures | {stats['complete_selected_legal_texts']} |
| Source-page records with extracted links | {stats['page_records_with_link_extraction']} |

Original documents total approximately **648 MB** (decimal), excluding web snapshots, extracted text and the starter ZIP. These are acquisition counts, not pages substantively reviewed. Formats include 694 PDFs, 51 XLSX, 3 XLS, 38 DOCX and 14 ZIP files.

## Search and selection scope

The research mapped Euronext Securities’ group site and the public documentation hubs for all five CSDs. It followed current rulebooks, admission rules, operating/technical manuals, corporate events, account structures, links, fees, selected notices, disclosures and strategic programmes. The bounded Euronext/Athens crawl completed its eligible queue; additional regulatory/infrastructure sources were collected separately. Athens’ two regulatory pages were checked to capture the master rulebook and all 22 resolutions.

Primary supporting sources include EUR-Lex, ESMA, ECB/T2S/AMI-SeCo, BIS/CPMI-IOSCO and ECSDA. The complete selected legal texts were recovered through the browser where direct requests did not return the actual text.

The sweep was English-led and also retained locally linked non-English documents. It was not an exhaustive crawl of every language, archive page, external regulator site or historical notice pagination. “Most recent found” is grounded in the reviewed canonical hubs, dates and original files, not a guarantee that no newer client-only or unlinked document exists.

## Review depth

Selected admission, settlement, cash-account, governance and programme-scope passages were substantively reviewed to produce the synthesis. Other documents were catalogued and, for PDFs, text-extracted. The selected documents’ review scope and PDF page references are recorded in the manifest. Six core cover/history pages were visually inspected in {f('verification/core-document-covers.png','the retained contact sheet')}.

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
''')

starter_ids=['1ae6d477d17b','535f6a23062a','2a1af673b358','8719262f5e8b','ba7b6da1bec4','dd1cf7cb930b','cbdf3c1f8b51','16ded02d7a65','3d76a327339b','838261c7c0d4','089b7aaef991','fcbc69b0fc35','4e7eec1c51e0','67c9ce673c2a','dab1b35a93c5','513a8da7c0ad','410859953fce','8b240d87dad0']
starter_legal=[x for x in M['legal_texts'] if x['id'] in ['02014R0909-20260117','02017R0392-20170310','02022R2554-20221227']]
with zipfile.ZipFile(R/'starter-pack.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    rows=['# CSD starter pack','Snapshot: 11 September 2026. 21 source documents. Curated introduction; not the complete library. Future programme documents and the unresolved Athens master/Oslo VPO editions are omitted. Dates and original-language precedence still matter.','']
    for id in starter_ids:
        x=B[id];name=Path(x['local_path']).name;z.write(R/x['local_path'],'sources/'+name);rows.append(f'- {x["title"]}: {x["url"]} | {x.get("version_date_evidence","")}')
    for x in starter_legal:
        z.write(R/x['text_path'],'sources/'+Path(x['text_path']).name);rows.append(f'- {x["title"]}: {x["url"]}')
    z.writestr('START-HERE.md','\n'.join(rows))

w('README.md',f'''
# Euronext CSD knowledge library

**Research date: 11 September 2026.** Public-source research covering **Athens, Copenhagen, Milan, Oslo and Porto**, plus CSDR, ESMA, T2S, PFMI, DORA and the T+1 transition.

The library contains **800 original document files**, with **84 prioritised documents and 14 selected legal texts** in the reading guide. Sources were downloaded, indexed and, where practical, extracted. Selected core passages were studied to write the synthesis; the full 29,084 PDF pages were not substantively reviewed.

## Start here

| Need | Open |
|---|---|
| Understand how the CSDs function | {f('HOW-CSD-WORKS.md','How the CSDs work')} |
| Find the requirements for operators, participants and issuers | {f('REQUIREMENTS-MAP.md','Requirements map')} |
| Read the most useful, latest-found documents | {f('READING-GUIDE.md','Prioritised reading guide')} |
| Search the complete collected inventory | {f('SOURCE-CATALOGUE.md','Full source catalogue')} |
| See every document in one list, including sources used in this conversation | {f('FULL-DOCUMENT-LIST.md','Full document list')} |
| Check versions, future dates and conflicting sources | {f('CURRENTNESS-REGISTER.md','Currentness register')} |
| Build a retrieval knowledge base | {f('KNOWLEDGE-BASE-DESIGN.md','Ingestion and evaluation guide')} |
| Understand coverage and remaining gaps | {f('COVERAGE-AND-CAVEATS.md','Coverage and caveats')} |
| Upload a smaller starting selection | {f('starter-pack.zip','21-source starter pack')} |

## What the research established

Current local operations, the **September 2026 European Offering**, and the **longer-term Convergence programme** need separate collections. The European Offering launch is announced for **21 September 2026**. Convergence’s June/August 2026 specifications describe a future common platform, with an indicative migration sequence beginning in 2028. [Launch announcement]({golive}); [Convergence programme]({conv}).

Recent sources include the **2 September 2026 ESMA register**, **3 August 2026 Copenhagen rulebook updates**, **2026 Porto operating/technical manuals**, **July 2026 Athens resolution updates**, and **2026 Milan expansion documents**. The reading guide records older editions that remain the latest linked public baseline instead of discarding them by year.

The Athens master rulebook has conflicting version labels, and the linked Oslo VPO copy retains an approval qualification. These are flagged and excluded from default current-state retrieval. Client-only manuals and exact implementation entitlements remain outside the public collection.

## Files and provenance

Originals live in `sources/documents/`; website snapshots in `sources/pages/`; extracted PDF and legal text in `extracted/`. The source catalogue links each retained document directly. SHA-256 hashes and acquisition results are retained in metadata.

Use {f('curated-manifest.json')} for the prioritised selection and {f('catalogue.json')} for all discovered document records. The latter includes historical, future, duplicate and unreviewed material. Do not import every file as equally authoritative. The collection is a dated local snapshot, with no automatic update schedule or deployed chatbot.
''')
print('Wrote research guides and 21-source starter pack.')
