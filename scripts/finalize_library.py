"""Build the curated, dated research package from retained source evidence."""
import json, hashlib, collections, re
from pathlib import Path

R=Path(__file__).resolve().parents[1]
from snapshot_guard import refuse_audited_snapshot
refuse_audited_snapshot(R)
ASOF='2026-09-11'
C=json.loads((R/'catalogue.json').read_text()); B={d['id']:d for d in C}
def dump(p,data):
    p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def write(p,text):
    p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n')
def link(id,label=None):
    d=B[id];return f'[{label or d["title"]}](<{R/d["local_path"]}>)' if d.get('local_path') else f'[{label or d["title"]}]({d["url"]})'
def web(id,label='official source'):return f'[{label}]({B[id]["url"]})'
def file(name,label=None):return f'[{label or name}](<{R/name}>)'

# Preserve prior errors as history; successful retained originals are not failed acquisitions.
for d in C:
    if d.get('local_path') and (R/d['local_path']).exists() and d.get('error'):
        d['previous_error']=d.pop('error')
    d['automatic_metadata_warning']='Markets, topics, dates and priority were inferred from linked pages; use curated fields when present. Nearby table dates can belong to other rows.'
    d['default_retrieval']=False
    if d.get('content_type','').startswith('image/'):
        d['acquisition_disposition']='excluded-staff-photograph'
    elif d.get('error'):d['acquisition_disposition']='unresolved-or-redirected-link'
    elif d.get('local_path'):d['acquisition_disposition']='archived'
    else:d['acquisition_disposition']='catalogued-not-downloaded'

S=[]
def select(id,group,date,purpose,layer='current-local',review='Version/source listing inspected; no complete substantive review.',pages=None):
    d=B[id]
    s={'id':id,'group':group,'title':d['title'],'version_date_evidence':date,'why_read':purpose,'knowledge_layer':layer,'review_scope':review,'reviewed_pdf_pages':pages or [],'default_retrieval':False,'source_url':d['url'],'local_path':d.get('local_path'),'text_path':d.get('text_path'),'pages':d.get('pages'),'sha256':d.get('sha256')}
    d.update({k:v for k,v in s.items() if k not in ['title','source_url','group']});d['curated_group']=group
    S.append(s)

select('8719262f5e8b','Milan','Service Regulations: 26 January 2026. Posted February 2026.','Contractual starting point: services, admission, participant duties, suspension and liability.',review='Cover and selected scope/admission/conduct provisions read. Italian text prevails.',pages=[1,6,13,14,15,16])
select('ba7b6da1bec4','Milan','CSD Service Instructions: 7 October 2025, clean edition.','Detailed issuance, custody and asset-servicing procedures.')
select('dd1cf7cb930b','Milan','Settlement Service Instructions: 30 June 2025, clean edition.','Settlement participation, instructions and operating procedures.')
select('1bd67deaace2','Milan','T2S Gateway settlement links: valid from 1 May 2026.','Cross-border settlement routes and local market dependencies.')
select('a68f245f8337','Milan','Pricing policy: 11 December 2025; posted February 2026.','Understand the pricing structure before using individual tariffs.')
select('ac385b0f3106','Milan','Eligible ISIN list: daily snapshot 11 September 2026.','Instrument eligibility changes independently of rulebook versions. Workbook archived; rows not analysed.','reference')
select('de2d312169fc','Milan','Operational notice ON_36/2026: 11 September 2026; planned changes 30 November 2026, subject to testing.','Example of a current notice announcing future XTRM identifiers. Detailed specification is on MT-X.','future-release','One-page notice read in full.',[1])

select('cbdf3c1f8b51','Copenhagen','Part 2 General Terms: 3 August 2026. Internal footers show inconsistent version numbers.','Eligibility, LEI, legal opinions, user permissions and issuer-agent responsibilities.',review='Cover and admission/participant provisions read. Use date plus hash, not an invented single footer version.',pages=[1,2,3,4,5])
select('16ded02d7a65','Copenhagen','Part 3 Book-entry Rules: 3 August 2026.','Account registration, rights and book-entry responsibilities.')
select('3d76a327339b','Copenhagen','Part 4 Settlement Rules: 1 May 2025.','VP versus T2S settlement, cash arrangements, instruction flows and fail penalties.',review='Cover and settlement/penalties provisions read. Interpret references to buy-ins against current higher-level law.',pages=[1,3,4,5,6])
select('30b6aea9c856','Copenhagen','Part 1 Definitions: 13 March 2025.','Definitions needed to interpret the other five rulebook parts.')
select('a7e4ccfb2933','Copenhagen','Part 5 DCP rules: published August 2023; still linked in current rulebook.','Direct T2S connectivity and the continuing relationship with the CSD.')
select('2b4a3465e7d6','Copenhagen','Part 6 FundHub: published March 2024; still linked in current rulebook.','Fund service scope and participation.')
select('14e2c64da9a0','Copenhagen','Fee table: January 2026.','Baseline tariff as of this research date.')
select('cdd34eb011e9','Copenhagen','Fee table: November 2026; published August 2026.','Future tariff; do not apply it to September costs.','future-release')

select('838261c7c0d4','Oslo','Registration Rules: effective 4 February 2025; adopted 10 January 2025.','Investor accounts, account operators, issuer registration and legal rights.',review='Cover/version and contents inspected. Norwegian text prevails.')
select('14dc34b8e54e','Oslo','VPO NOK Rules: 2 September 2024; current hub links a copy whose cover retains an approval qualification.','VPS securities leg, Norges Bank cash leg, membership and liquidity banks.',layer='needs-validation',review='Selected participation, settlement-bank and liquidity-bank rules read; approval qualification remains unresolved.',pages=[1,5,13,14,15,16,17,18,19])
for d in C:
    if d.get('local_path') and 'ES-OSL-Fee-Schedule-January-2026.pdf' in d['url']:
        select(d['id'],'Oslo','January 2026 fee schedule; file uploaded September 2026.','Current linked fee schedule, resolved from the media landing page.')

select('089b7aaef991','Porto','Operational Manual V43. Internal date 26 January 2026; filename 16 February 2026; posted April 2026.','Broadest local operating manual: onboarding, accounts, settlement and asset servicing.',review='Cover, contents and participant-admission section read; the several date signals are retained separately.',pages=[1,15,16,17])
select('67c9ce673c2a','Porto','STD message/file layouts V58: 8 April 2026.','Technical messages and file formats for implementation.')
select('04b490f176fe','Porto','ISO 15022 manual V9: 26 January 2026.','SWIFT message usage and local semantics.')
select('fcbc69b0fc35','Porto','Regulation 1/2016, consolidated through amendments listed on its cover, including 3/2022. Posted July 2023.','Participant eligibility and responsibilities; English translation is non-binding.',review='Cover and opening scope provisions inspected.',pages=[1])
select('4e7eec1c51e0','Porto','Regulation 2/2016, consolidated through amendment 1/2023 on cover. Posted January 2024.','General rules for the centralised securities and settlement systems; English translation is non-binding.',review='Cover and contents inspected.',pages=[1])
select('4ed2c4395487','Porto','Regulation 1/2018, current-hub consolidated copy posted July 2023.','Securities Lending Management System rules, including agent/participant roles.',review='Cover and opening scope inspected.',pages=[1])
select('32e563898f54','Porto','Circular 1/2026.','Corporate-events rules to read alongside the operational manual.')
select('269d50884667','Porto','Financial intermediary fee book: 1 January 2026.','Participant charges.')
select('7bb6fc64201a','Porto','Issuer fee book: 1 January 2026.','Issuer charges, distinct from participant tariffs.')
select('2a1af673b358','Porto','WFC 2025 disclosure, submitted 8 January 2026, posted May 2026.','Broad due-diligence questionnaire covering the CSD, controls and services.','reference')
select('840c5c3ee312','Porto','CSD links guide: March 2023, posted August 2024.','Background on links; revalidate live eligibility and route before use.','needs-validation')

select('d89c56df8c5a','Athens','Hub says Amendment 8; filename and internal history indicate 7th amendment, with late-2025 dates.','Master rulebook. Preserve the conflict and obtain a reconciled edition before authoritative use.','needs-validation','Cover/history page and hub compared; inconsistent numbering/effective-date signals unresolved.',[1,2])
select('dab1b35a93c5','Athens','Resolution 1: hub in-force date 2 April 2025.','Participant admission stages, application documents and activation.',review='Opening admission/documentation provisions read.',pages=[1,2,3,4])
select('513a8da7c0ad','Athens','Resolution 2: effective 20 July 2026, confirmed by PDF footnote.','Certified personnel and continuing competence; preserve stated exemptions.',review='Opening certification provisions and effective-date footnote read.',pages=[1,2])
select('0afef141bd75','Athens','Resolution 4: effective 16 March 2026.','Central maintenance service.')
select('410859953fce','Athens','Resolution 5: effective 8 December 2025.','Settlement services and cash arrangements.',review='Selected euro/non-euro cash-settlement provisions read.',pages=[3,4])
select('b43be010e44f','Athens','Resolution 8: effective 14 July 2026.','Corporate actions and asset servicing.')
select('8b240d87dad0','Athens','Resolution 14: effective 1 April 2026.','IT and operational requirements.')
select('1d7c08130861','Athens','Resolution 18: effective 15 June 2026.','Detailed fee schedule.')
select('bbe3343b69ed','Athens','Resolution 19: effective 28 January 2026.','Rulebook amendment committee.')
select('3cfbaea6fa93','Athens','PFMI self-assessment: December 2023.','Structured background on risks and controls; predates acquisition and newer changes.','reference')

select('00a3e1aeba1c','European Offering','Account Structure V03: May 2026.','Milan onboarding, account types and market-specific registered-share arrangements.','future-programme','Scope and opening account/onboarding sections read.',[3,4,5])
select('05b157889a5e','European Offering','Connectivity V03.3: June 2026.','Connections and message flows for the Milan-based European Offering.','future-programme','Cover and service-scope section read.',[1,5])
select('afb2acf61501','European Offering','Place of Settlement Change Guidelines V3: March 2026.','Operational migration of settlement location.','future-programme')
select('7954e2be7dbe','European Offering','French Registered Shares V06.3: June 2026.','French ownership/registration workflows.','future-programme')
select('8a5f34ddaa95','European Offering','Belgian Registered Shares and Dematerialisation V4: February 2026.','Belgian registration and dematerialisation workflows.','future-programme')
select('4bd4c8173877','European Offering','IRI User Guide V02: July 2026.','Investor/registration service application workflow.','future-programme')
select('7d682b9f33d3','European Offering','Client Test Approach V2: March 2026.','Testing obligations and readiness activities.','future-programme')

select('71233aed41e7','Convergence','Settlement SDD V1.6: June 2026.','Future common-platform settlement model; first migration planned in 2028.','future-programme','Scope, future applicability, account/cash model and instruction routes read.',[1,6,8,9,10,11,12,13])
select('0fcc0c30007c','Convergence','Connectivity SDD V2: June 2026 cover; posted July 2026.','Future connectivity; different scope from European Offering Connectivity V03.3.','future-programme','Scope, network arrangements and interfaces read.',[1,4,5,8,9,10,11,12])
select('5be872c2e8e6','Convergence','Client Master Data and Account Management V1.3: June 2026.','Future participant/account model.','future-programme')
select('0b9a9fe38187','Convergence','National Numbering Agency SDD V5.0: 25 August 2026.','Future ISIN codification services.','future-programme')
select('0445be6be7bd','Convergence','Securities Management V2.4: May 2026 edition; posted June 2026.','Future issuance/security lifecycle.','future-programme')
select('fe5c44a4645e','Convergence','Name Registration V1.2: August 2026.','Future registration model. Clean edition preferred; a September redline also appears.','future-programme')
select('01a10dc8b37c','Convergence','Settlement Penalties V1.2: November 2025.','Future platform penalty processing.','future-programme')
select('9e67363e5982','Convergence','Extended Service Overview V3: July 2026.','Planned ancillary services and scope.','future-programme')
for id in ['f30e272ac07d','e4ec6d2a8cd3','9a9900fa74db']:
    select(id,'Convergence','Market newsletter: July 2026.','Market-specific progress, pending documentation and migration qualifications.','future-programme','Newsletter text inspected; Athens specifies indicative H2 2029 migration and late-2028 testing.',[1,2])

select('e1354fb2d76a','Corporate events','Processes Handbook V05: 7 May 2026.','Issuer, agent, paying-agent and investor-CSD flows. Handbook names four CSDs; do not extend its scope automatically to Athens.','reference','Cover, contents and selected scope/actor provisions read.',[1,16,17])
select('1f1f7d487837','Corporate events','CA4U Functional Guide, English: June 2026.','Application overview and operating functions.','reference')
select('70cf046f2af0','Corporate events','MyEuronext access material: August 2026.','Access/permissions workflow; service and market applicability must be checked.','reference')

select('535f6a23062a','Regulation and standards','ESMA register: 2 September 2026, confirmed in 0- Info!B12 and HTTP Last-Modified.','Authorisations, CSD links, passports and competent authorities. URL folder remains 2025-10.','regulatory-baseline','Workbook read without modifying it. Date and Euronext authorisation rows inspected. Porto C25 contains an incomplete LEI; do not use it as validated master data.')
B['535f6a23062a']['structured_extract_path']='extracted/535f6a23062a-rows.json'
select('1ae6d477d17b','Regulation and standards','CPMI-IOSCO PFMI: April 2012.','Foundational risk/operating framework. Still relevant despite its age.','foundational-standard')
select('cd6c6798015f','Regulation and standards','PFMI Disclosure Framework and Assessment Methodology: December 2012.','Template for comparing CSD controls and structuring due diligence.','foundational-standard')
select('bcfcff46ecf4','Regulation and standards','ECSDA penalties framework: 11 September 2024; latest public update found.','Industry implementation details, calendars and penalty flows. It is not legislation.','reference')
select('f488a7016d8c','Regulation and standards','ESMA T+1 statement: 20 July 2026.','Readiness deadlines and the regulatory transition; distinguish adopted drafts, scrutiny and application.','future-release')
select('a46c6c66a0e4','Regulation and standards','T+1 Corporate Events Harmonised Implementation Guide: July 2026 cover; hub updated 23 July.','T+1 changes to event dates, market claims, transformations and buyer protection.','future-release','Cover, contents and introductory purpose inspected.',[1,2,3,4,5])
for id,purpose in [('c164d86ada8e','Start here: release scope and status.'),('aa3d5a3b94c9','Detailed settlement system behaviour and messages.'),('06c4d87911f6','User-interface operations.'),('082eda43643a','General functional model.'),('3c811cac5943','User requirements and traceability.'),('0c80b5e41513','Data migration tooling/reference.'),('302a628be94a','Business functionality.'),('8c1289ebd427','Cross-reference from requirements to specifications.')]:
    select(id,'T2S','R2026.JUN final documentation; published 22 January 2026.',purpose,'current-infrastructure')
for d in C:
    if 'R2026.NOV' in d['url'] and d.get('local_path'):
        select(d['id'],'T2S future release','R2026.NOV documents published 3 August 2026 for market review.','Keep separate from the June production-release documentation.','future-release')

# Explicit legal allowlist avoids earlier, truncated captures and superseded originals.
L=json.loads((R/'metadata/legal-browser-sources.json').read_text()); LB={d['id']:d for d in L}
legal_specs=[
 ('02014R0909-20260117','CSDR: consolidated 17 January 2026','Core services, authorisation, governance, access, safeguarding, settlement and prudential requirements.'),
 ('02017R0392-20170310','RTS 2017/392: consolidated 10 March 2017','Authorisation and operational/organisational requirements.'),
 ('02017R0394-20170310','ITS 2017/394: consolidated 10 March 2017','Standard forms, templates and procedures for authorisation and reporting.'),
 ('02017R0390-20170310','RTS 2017/390: consolidated 10 March 2017','Capital and prudential requirements; banking-type services where applicable.'),
 ('02017R0389-20170310','Delegated Regulation 2017/389: consolidated 10 March 2017','Penalty parameters and substantial importance.'),
 ('02018R1229-20240902','Settlement Discipline RTS: consolidated 2 September 2024','Settlement-fail prevention, penalties and related procedures; read with later changes and their application dates.'),
 ('32017R0391','Delegated Regulation 2017/391','Internalised-settlement reporting.'),
 ('32017R0393','Implementing Regulation 2017/393','Internalised-settlement reporting templates.'),
 ('02022R2554-20221227','DORA: consolidated 27 December 2022','ICT risk, incident reporting, testing and third-party risk.'),
 ('01998L0026-20240408','Settlement Finality Directive: consolidated 8 April 2024','Transfer-order finality and insolvency protection; national implementation matters.'),
 ('32018R1212','Implementing Regulation 2018/1212','Shareholder identification and transmission of shareholder-rights information.'),
 ('32023R2845','CSDR Refit 2023/2845','Amending act; use alongside the consolidated CSDR, not as a substitute.'),
 ('32025R2075','T+1 amendment 2025/2075','11 October 2027 application date for the shorter settlement cycle.'),
 ('02022R0858-20220602','DLT Pilot Regime: consolidated 2 June 2022','Separate pilot permissions/exemptions for DLT infrastructures; optional specialised research track.')]
LEGAL=[]
for id,title,purpose in legal_specs:
    d=LB[id].copy(); assert d.get('complete_text_capture'),id
    d['title']=title;d['why_read']=purpose;d['default_retrieval']=False;d['knowledge_layer']='regulatory-baseline';d['review_scope']='Complete displayed text captured and version navigation inspected; not a full legal review.'
    if id=='02014R0909-20260117':d['review_scope']='Selected Articles 2, 5, 16, 26, 33, 37–48, 54 and Annex reviewed; not all provisions or cross-references reviewed.'
    if id=='32025R2075':d['knowledge_layer']='future-release';d['default_retrieval']=False
    if id=='02022R0858-20220602':d['knowledge_layer']='specialised-reference';d['default_retrieval']=False
    d['sha256']=hashlib.sha256((R/d['text_path']).read_bytes()).hexdigest();LEGAL.append(d)

# Match identical downloads while retaining every provenance URL.
hashes=collections.defaultdict(list)
for d in C:
    if d.get('sha256'):hashes[d['sha256']].append(d['id'])
for ids in hashes.values():
    preferred=next((i for i in ids if any(s['id']==i for s in S)),ids[0])
    for id in ids:
        B[id]['canonical_content_id']=preferred
        if id!=preferred:B[id]['duplicate_of']=preferred;B[id]['default_retrieval']=False

overrides_path=R/'metadata/curation-overrides.json'
if overrides_path.exists():
    overrides=json.loads(overrides_path.read_text())
    for old,new in overrides.get('resolved_links',{}).items():
        B[old]['resolved_by']=new;B[old]['acquisition_disposition']='resolved-to-another-record'
    for s in S:
        if s['id']=='535f6a23062a':
            s['structured_extract_path']=overrides['registry_structured_extract']
        if s['id']=='f488a7016d8c':
            s['review_scope']='Two-page statement read in full, including scrutiny status and both milestone dates.'
            s['reviewed_pdf_pages']=overrides['esma_statement_reviewed_pages']
            B[s['id']]['review_scope']=s['review_scope'];B[s['id']]['reviewed_pdf_pages']=s['reviewed_pdf_pages']
dump('catalogue.json',C);dump('curated-manifest.json',{'as_of':ASOF,'documents':S,'legal_texts':LEGAL})
P=[]
for p in (R/'metadata').glob('*.json'):
    x=json.loads(p.read_text())
    if isinstance(x,dict) and x.get('url') and 'links' in x:P.append(x)
dump('metadata/all-pages.json',P)
stats={'as_of':ASOF,'catalogued_document_urls':len(C),'retained_document_files':sum(bool(d.get('local_path')) for d in C),'unique_retained_contents':len(hashes),'pdf_files':sum(d.get('file_type')=='pdf' for d in C),'pdf_pages_including_duplicate_files':sum((d.get('pages') or 0) for d in C),'unique_pdf_pages':sum((B[ids[0]].get('pages') or 0) for ids in hashes.values()),'retained_bytes':sum(d.get('bytes',0) for d in C),'curated_documents':len(S),'complete_selected_legal_texts':len(LEGAL),'page_records_with_link_extraction':len(P),'types':dict(collections.Counter(d['file_type'] for d in C if d.get('file_type')))}
dump('verification/library-stats.json',stats)

# Human-readable source index, split by scope for manageable navigation.
groups=collections.defaultdict(list)
for d in C:
    for m in d.get('markets',[]) or ['other']:groups[m].append(d)
index=['# Full source catalogue',f'\nSnapshot: 11 September 2026. {len(C)} discovered document URLs; not all were downloaded or reviewed. Start with the curated reading guide. Automatic topic/date labels in the JSON are discovery aids, not verified applicability.\n',file('READING-GUIDE.md','Curated reading guide'),'', '| Scope | Document URL records | Index |','|---|---:|---|']
for group,docs in sorted(groups.items()):
    name=f'catalogues/{group}.md';index.append(f'| {group} | {len(docs)} | {file(name, "Open")} |')
    out=[f'# {group}: source catalogue','\nDated public-source snapshot. Documents can appear under multiple scopes. “Archived” means a local original exists; it does not mean current or fully reviewed.\n']
    for d in sorted(docs,key=lambda d:(not d.get('curated_group'),d['title'].lower())):
        title=d['title'].replace('\n',' ')
        out += [f'## {title}',f'\nID: `{d["id"]}`. Acquisition: {d["acquisition_disposition"]}.\n',f'[Official source]({d["url"]})'+(f' · {link(d["id"],"Local original")}' if d.get('local_path') else '')+(f' · {file(d["text_path"],"Extracted text")}' if d.get('text_path') else ''),'']
        if d.get('curated_group'):out += [d['version_date_evidence'],f'Layer: {d["knowledge_layer"]}. {d["review_scope"]}','']
        else:out += ['Applicability and substantive contents not individually validated.','']
    write(name,'\n'.join(out))
write('SOURCE-CATALOGUE.md','\n'.join(index)+f'\n\nMachine-readable records: {file("catalogue.json")} and {file("curated-manifest.json")}.\n')

guide=['# Prioritised reading guide','\nResearch date: **11 September 2026**. “Latest” below means the most recent edition found on the reviewed official hubs. Source-page listing does not by itself prove every provision is currently applicable.\n',
'Start with CSDR, PFMI, the ESMA register and Porto’s WFC disclosure. Then read the rulebook and operating instructions for the market you need. Keep future programme documents in a separate reading track.\n',
'## Regulatory foundation\n','| Document and official text | Why read it |','|---|---|']
for d in LEGAL:
    guide.append(f'| [{d["title"]}]({d["url"]}) · {file(d["text_path"],"Saved text")} | {d["why_read"]} |')
for group in dict.fromkeys(s['group'] for s in S):
    guide += [f'\n## {group}\n','| Document | Version/date evidence | Purpose and applicability |','|---|---|---|']
    for s in S:
        if s['group']!=group:continue
        guide.append(f'| {link(s["id"])} · {web(s["id"])} | {s["version_date_evidence"]} | **{s["knowledge_layer"]}**. {s["why_read"]} |')
guide += ['\n## How deeply were these reviewed?\n','Selected rulebook, admission, settlement and programme-scope passages were read to produce the synthesis. Most supporting technical manuals received version/contents checks and text extraction, not a page-by-page substantive review. Exact selected page scopes are recorded in '+file('curated-manifest.json')+'. PDF page numbers use the viewer’s one-based page index, which can differ from printed numbering.']
write('READING-GUIDE.md','\n'.join(guide))

print(json.dumps(stats,indent=2))
