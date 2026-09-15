import json, pathlib, hashlib, csv, collections, re, datetime

A=pathlib.Path(__file__).resolve().parents[1]
B=A.parents[1]
CAT=json.loads((B/'catalogue.json').read_text())
CUR=json.loads((B/'curated-manifest.json').read_text())
CM={x['id']:x for x in CAT}
CU={x['id']:x for x in CUR['documents']}
LEG={x['id']:x for x in CUR['legal_texts']}
LIVE={x['audit_id']:x for p in sorted((A/'evidence').glob('live-*.json')) for x in [json.loads(p.read_text())]}
REV={}

def write(name,s): (A/name).write_text(s.strip()+'\n')
def js(name,obj): write(name,json.dumps(obj,ensure_ascii=False,indent=2))
def table(headers,rows):
    def esc(x):return str(x if x is not None else 'unknown').replace('|',' / ').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(esc,r))+' |' for r in rows])
def csvout(name,rows):
    with (A/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader()
        for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
def src(i):
    d=CM.get(i) or LEG.get(i) or LIVE.get(i) or {}
    live=LIVE.get(i) or LIVE.get('legal-'+i) or {}
    path=d.get('local_path') or (d.get('saved_path') if i in LIVE and i not in CM and i not in LEG else None) or d.get('text_path')
    if path:path=str(B/path) if i in CM or i in LEG else str(A/path)
    elif live.get('saved_path'):path=str(A/live['saved_path'])
    return {'id':i,'title':d.get('title') or live.get('title') or i,'url':d.get('url') or d.get('source_url') or live.get('url'), 'local_path':path,'live_evidence':str(A/f"evidence/live-{live.get('audit_id')}.json") if live else None}
def cite(i,locator):
    s=src(i);return f"[{s['title']}]({s['url'] or s['local_path']}) — {locator}"
def reviewed(i,scope,pages=None,depth='selected-operative-passages',note='',category=None):
    REV[i]={'source_id':i,'depth':depth,'substantive':depth in ['selected-operative-passages','complete-short-document','selected-workbook-cells','selected-legal-provisions'], 'scope':scope,'pdf_pages_reviewed':pages or [],'remaining_review_gap':note or 'All other passages, annexes, cross-references and operational dependencies remain unreviewed.', 'category_override':category}

reviewed('8719262f5e8b','Articles 60–61, 65–72: admission, connectivity, eligibility, notices, matching, cancellation, hold and SF1/SF2/SF3.',[44,45,48,49,50,51])
reviewed('milan-it-regulations','Italian authoritative language: cover, Articles 60–61 and 69–72; independently compared with sampled English clauses.',[1,44,45,50,51])
reviewed('dd1cf7cb930b','Settlement instructions: general hierarchy; §1.1 access/CLIMP, timetable and partial settlement, selected market-claims rules.',[5,7,8,13,15,17,18,19,20,21,22,23],category='Current operational authority',note='Timetable clauses on PDF 13 and 15 conflict with current ECB baseline and are quarantined; other sections only candidates pending dependency review.')
reviewed('milan-it-settlement','Italian timetable and partial-settlement clauses; confirms the discrepancy is also present in the governing language.',[12,15],category='Quarantine')
reviewed('de2d312169fc','ON_36/2026, 11 September 2026: planned 30 November X-TRM identifiers, conditional on tests, and exact MT-X folder.',[1],'complete-short-document',category='Future or draft')
reviewed('cbdf3c1f8b51','Part 2: cover/version anomaly and §§2.1–2.3, 3.1.1, selected admission, CSD-link testing and staff obligations.',[1,2,3,4])
reviewed('3d76a327339b','Part 4 §§2.2–2.4: VP/T2S business days, currency/route conditions, penalties and applicable buy-in-law reference.',[3,4,5,6])
reviewed('a7e4ccfb2933','Part 5 §§2–3: DCP certificate, agreement, service entitlements, user guidelines and local technical conditions.',[2,3])
reviewed('14e2c64da9a0','January 2026 fee book: cover/revision and contents only. No fee line validated.',[1,2],'identity-and-version-only',category='Specialist material')
reviewed('cdd34eb011e9','November 2026 fee book: cover/revision and contents only. Not yet applicable on audit date.',[1,2],'identity-and-version-only',category='Future or draft')
reviewed('838261c7c0d4','Registration rules: account operator responsibilities and §2.1.4.2 back-up account operator response.',[14,19])
reviewed('14dc34b8e54e','VPO NOK cover approval reservation; §§8–11 liquidity-bank and substitute-bank obligations.',[1,16,17,18,19],category='Quarantine',note='Norwegian governing text carries same approval reservation; system approval on regulator hub does not establish approval of this particular edition.')
reviewed('822d46bb9149','Norwegian VPO NOK cover: in force 2 September 2024, subject to Finanstilsynet approval.',[1],'identity-and-version-only',category='Quarantine')
reviewed('089b7aaef991','V43: Chapter 1 affiliation/DCP forms; Chapter 4 calendar/notices; §7.1 reconciliation and position/activity reports.',[1,16,17,18,33,66])
reviewed('fcbc69b0fc35','Regulation 1/2016: scope; Articles 2–3 contract remains with INTERBOLSA for DCP and financial information.',[1,2])
reviewed('4e7eec1c51e0','Regulation 2/2016 cover amendment list and contents only.',[1,2],'identity-and-version-only')
reviewed('32e563898f54','Circular 1/2026: translation qualification, corporate-events scope and definitions; not full event procedures.',[1,2],category='Specialist material')
reviewed('d89c56df8c5a','Athens English master: amendment history and Section XIII Part 9 / footnote 94 on seventh amendment effect.',[2,217],category='Current operational authority',note='Edition label largely reconciled; approval/Gazette independently inaccessible and remaining operational rules not reviewed.')
reviewed('athens-greek-master','Greek master: amendment history and final Section XIII Part 9 / footnote 94.',[2,206],category='Current operational authority')
reviewed('dab1b35a93c5','Resolution 1 §1.1.1.2(5): two years of financial information with new-entity exception; foreign participant legal support.',[4])
reviewed('513a8da7c0ad','Resolution 2 §§1–2.1: certification exemptions and minimum certified CSA staff/ongoing competence.',[2])
reviewed('410859953fce','Resolution 5 cover and §§1.1–1.2, 2.2: EUR TARGET-GR versus non-EUR cash arrangements and DSS technical announcements.',[1,3,4,5])
reviewed('207ccb1774e7','Resolution 21 Articles 1–2: settlement-instruction types, HCMC notification and amendment footnotes.',[2])
reviewed('e1354fb2d76a','Corporate Events user guide §§2.2–2.3: standards and roles; Milan/Porto/Copenhagen/Oslo scope, investor-CSD dependency.',[16,17],category='Specialist material')
reviewed('aa3d5a3b94c9','R2026.JUN UDFS: §1.4 / Table 37 and business-date dependencies; §§1.6.1.2, 1.6.1.8, 1.6.1.10; Table 57 tolerance; realignment notification example and message overview.',[157,160,162,163,165,168,267,268,269,270,271,303,304,373,374,375,376,385,386,387,753,778],note='Selected sections of 2,017 pages. Diagram 55 visually reviewed on PDF 269; other field diagrams, full message usage definitions, business rules, annexes and configurations not reviewed.')
reviewed('c164d86ada8e','R2026.JUN final cover note, 22 January 2026; Annex A scope and Annex B MyStandards dependencies.',[1,2,3])
reviewed('7244cf50f753','R2026.NOV draft cover note: market-review window and planned 11 September final publication.',[1,2],category='Future or draft')
reviewed('71233aed41e7','v1.6 Convergence settlement design: investor-CSD/realignment and illustrative message-flow passages used by existing explanation.',[12,20,28,29,33,36,37,40,41,42,44,50,83],depth='identity-and-version-only',category='Future or draft',note='This audit checked its programme status and existing discussion provenance; listed pages are PRIOR library discussion references, not independently re-reviewed in this audit.')
REV['71233aed41e7']['pdf_pages_reviewed']=[]
reviewed('ac385b0f3106','Introduction B5:B8; Equities/ETPs/International ETPs I1:L1 and sample data including Equities A2/I2/K2/L2. Multiple alternative-depositary columns sampled.',depth='selected-workbook-cells',category='Future or draft',note='All rows not substantively validated. Current-place columns describe bounded listing data through 10 September; future designated/alternative places apply from 21 September. Not a universal eligibility register.')
reviewed('535f6a23062a','Info B12 (2 September 2026); authorised-CSD rows 25/34/36, including C25 malformed LEI and Milan UK stamp-duty extension. Sheet structure/merged-cell inspection.',depth='selected-workbook-cells',category='Bounded legal/definition context',note='Not all authorisation decisions independently obtained. Workbook row values must not be silently repaired; existing separate row extraction was found.')
reviewed('02014R0909-20260117','CSDR consolidated text: Articles 5, 37, 38 and 41; sampled Article 45 opening.',depth='selected-legal-provisions',category='Bounded legal/definition context')
reviewed('02022R2554-20221227','Articles 2 and 64 sampled; operative capture is French despite English URL/navigation.',depth='selected-legal-provisions',category='Quarantine')
reviewed('dora-english-oj','English OJ replacement: Articles 2(1)(g) and 64 only.',depth='selected-legal-provisions',category='Bounded legal/definition context')
reviewed('32025R2075','Articles 1–2: T+1 amendment; adoption/publication, entry into force versus application on 11 October 2027.',depth='selected-legal-provisions',category='Future or draft')
reviewed('591deafae0a9','Commission C(2026)4640 final, 6 July 2026: Article 2 staggered application dates; official record still unnumbered (EU) …/….',depth='selected-legal-provisions',category='Future or draft',note='OJ publication number and completion of scrutiny/entry into force not independently verified. Not current settlement law on audit date.')
reviewed('cd837a71029f','CMVM Regulation 4/2025 official Gazette: Articles 1–2 (amendments to 5/2018), Article 7 publication of CSD rules.',depth='selected-legal-provisions',category='Bounded legal/definition context',note='Direct HTTP capture is a JavaScript shell; operative passages read through web tool. Source must be recaptured before machine retrieval; no full Portuguese regulatory audit.')
reviewed('t2s-2026-status-events','Official 2026 events: 14 June deployment confirmation; 8 September 15:30/18:10/18:55 cutoff/incident updates; latest 12 September closure.',depth='selected-operative-passages',category='Current operational authority',note='Only named events reviewed. A daily event is an exception for its dated scope, not a permanent amendment.')
reviewed('porto-working-hours','2026 calendar, May 1 FoP exception, operating-hour table and references to notices 25/1162 and 0394/2024.',depth='selected-operative-passages',category='Current operational authority',note='Referenced binding notices not yet read; webpage permits bounded calendar illustration only pending notice verification.')

def inventory_category(d):
    i=d['id']; old=CU.get(i,d); layer=old.get('knowledge_layer','');t=d.get('title','').lower()
    if REV.get(i,{}).get('category_override'):return REV[i]['category_override']
    if d.get('canonical_content_id') and d['canonical_content_id']!=i:return 'Exclude from retrieval'
    if any(s in layer for s in ['future','draft']):return 'Future or draft'
    if layer=='needs-validation':return 'Quarantine'
    if 'histor' in layer or any(s in t for s in ['previous version','annual report','self-assessment','disclosure report']):return 'Historical'
    if i in ['70cf046f2af0','8c1289ebd427']:return 'Exclude from retrieval'
    if any(s in t for s in ['pricing','fee','tax','layout','corporate','penalties framework','data migration','fundhub']):return 'Specialist material'
    if layer in ['current-local','current-infrastructure']:return 'Current operational authority'
    if layer in ['foundational-standard','regulatory-baseline']:return 'Bounded legal/definition context'
    if any(s in t for s in ['presentation','brochure','newsletter','press release','webinar']):return 'Exclude from retrieval'
    return 'Quarantine'

def publisher(url):
    u=(url or '').lower()
    for key,name in [('euronext.com','Euronext / local CSD (legal issuer requires document check)'),('ecb.europa.eu','European Central Bank'),('esma.europa.eu','ESMA'),('eur-lex.europa.eu','European Union / EUR-Lex'),('ecsda.eu','ECSDA'),('bis.org','CPMI-IOSCO / BIS'),('finanstilsynet.no','Finanstilsynet Norway'),('finanstilsynet.dk','Finanstilsynet Denmark'),('bancaditalia.it','Banca d’Italia'),('diariodarepublica.pt','Portuguese official Gazette / CMVM'),('athens','ATHEXCSD / Athens Euronext')]:
        if key in u:return name
    return None

def register_row(i,d,origin):
    r=REV.get(i,{});l=LIVE.get(i) or LIVE.get('legal-'+i) or {};c=CU.get(i,d)
    cat=inventory_category(d) if origin=='catalogue' else r.get('category_override') or ('Bounded legal/definition context' if origin=='legal-capture' else 'Exclude from retrieval')
    s=src(i)
    if origin=='archived-webpage':s={'url':d.get('url'),'local_path':str(B/'metadata/all-pages.json'),'title':d.get('title')}
    reason='Provisional metadata screening only; no operational admission. Inspect specific clauses, effective period, language, dependencies and supersession before enabling.'
    if r:reason=r.get('scope','')+' '+r.get('remaining_review_gap','')
    if cat=='Exclude from retrieval' and not r:reason='Discovery, derivative, duplicate or narrowly administrative material; no independently reviewed operational proposition. Preserve archive; use only for locating primary evidence.'
    return {'source_id':i,'inventory_origin':origin,'title':s.get('title') or d.get('title'), 'original_url':s.get('url') or d.get('url'),'local_path':s.get('local_path'), 'publisher':publisher(s.get('url') or d.get('url')), 'entity_service':{'archived_market_hints':d.get('markets'), 'curated_group_claim':c.get('group'), 'verified_scope':r.get('scope') if r else None, 'warning':'Market/group hints are inherited claims, not verified legal-entity or service identifiers.'},'version_claim':c.get('version_date_evidence') or d.get('version_date_evidence'), 'dates':{'publication_date':None,'upload_date':None,'revision_date':None,'effective_from':None,'effective_to':None,'archived_date_evidence':d.get('date_evidence'), 'document_date_evidence':c.get('version_date_evidence'), 'http_last_modified':l.get('last_modified_http') or d.get('last_modified'), 'retrieved_at':l.get('retrieved_at_utc') or d.get('retrieved_at'), 'note':'Null is unknown. Exact, evidence-backed overrides are in SOURCE-RELATIONSHIPS.json and section allowlist; URL folders and HTTP dates are not legal dates.'}, 'review_depth':r.get('depth','metadata-screening-only'),'substantive_review':r.get('substantive',False),'reviewed_locator':r.get('scope'), 'pdf_pages_reviewed':r.get('pdf_pages_reviewed',[]),'applicability':'Only explicit permitted propositions in RETRIEVAL-PROPOSAL.json; otherwise pending. No whole-document admission.', 'approval_status':'Not independently certified for whole document; see bounded section decision and findings.', 'supersession':'Unknown unless relationship recorded in SOURCE-RELATIONSHIPS.json; no inference from newer upload.', 'retrieval_category':cat,'category_is_provisional':True,'default_retrieval_proposed':False,'reason':reason,'sha256':d.get('sha256') or l.get('sha256'),'live_status':l.get('http_status'),'live_hash_matches_archive':l.get('same_as_archived_bytes'),'live_evidence':s.get('live_evidence'),'adds_evidence_beyond_existing':'Named sampled propositions only; marginal value otherwise unassessed.'}

REG=[register_row(d['id'],d,'catalogue') for d in CAT]
REG += [register_row(d['id'],d,'legal-capture') for d in CUR['legal_texts']]
pages=json.loads((B/'metadata/all-pages.json').read_text())
REG += [register_row('page:'+str(n)+':'+d.get('id',''),d,'archived-webpage') for n,d in enumerate(pages,1)]
discussion=json.loads((B/'metadata/discussion-sources.json').read_text())
for n,d in enumerate(discussion['additional_discussion_sources'],1):
    r=register_row('discussion:'+str(n),d,'discussion-web-source');r.update(title=d['title'],original_url=d['url'],local_path=str(B/'metadata/discussion-sources.json'));REG.append(r)
attachment=discussion['user_attachment'];r=register_row('user-attachment-v1.5',attachment,'user-attachment');r.update(title=attachment['title'],local_path=attachment['local_path'],sha256=attachment['sha256'],retrieval_category='Future or draft',reason='Older v1.5 programme design; preserve as historical programme comparison, not current CSD authority. Only file identity checked.');REG.append(r)
known=set(CM)|set(LEG)
for i,d in LIVE.items():
    if i not in known and not (i.startswith('legal-') and i[6:] in LEG):REG.append(register_row(i,d,'audit-addition'))
js('SOURCE-DECISIONS.json',REG);csvout('SOURCE-DECISIONS.csv',REG)
js('REVIEWED-SOURCES.json',list(REV.values()))
write('REVIEWED-SOURCES.md','# Review depth and evidence ledger\n\nAudit date: 13 September 2026. Counts below mean selected substantive review, not complete review. All PDF numbers are one-based file pages; Porto printed numbers are generally one lower, Milan Service Regulations one lower, and the settlement instructions differ by section (operational timetable is four lower). UDFS page numbers coincide in the reviewed passages.\n\n'+table(['Source','Depth','Pages / precise scope','Remaining gap'],[[cite(i,'audit sample'),r['depth'],str(r['pdf_pages_reviewed'])+' '+r['scope'],r['remaining_review_gap']] for i,r in REV.items()])+'\n\nVisual inspection: original UDFS PDF 269 and Milan settlement instructions PDF 15 were viewed; the existing generated cross-CSD figure was also viewed. Other saved PNGs were rendered, not all visually reviewed. Workbook checks used cell-level reads. All 14 archive member lists were inspected; member contents were not parsed. Source instructions were treated as untrusted content throughout.\n')

REL=[
 {'id':'milan-clock-conflict','sources':['dd1cf7cb930b','milan-it-settlement','aa3d5a3b94c9'],'relationship':'unresolved-conflicting-timetable','scope':'Milan PDF 13/15; Italian PDF 12/15 vs UDFS PDF 160/162','action':'Quarantine local timetable claims. Use ECB current platform baseline only for platform questions, plus dated notices; obtain Milan service-specific confirmation.'},
 {'id':'milan-regulations-language','sources':['8719262f5e8b','milan-it-regulations'],'relationship':'translation-governing-original','effective_from':'2026-01-26','scope':'Sampled Articles 60–61,69–72','action':'Italian text governs; preserve English/Italian page citations and their paired hashes.'},
 {'id':'athens-edition','sources':['d89c56df8c5a','athens-greek-master'],'relationship':'probable-edition-versus-amendment-label','board_revision_date':'2025-11-24','approval_date_claim_in_document':'2025-12-04','gazette_date_claim_in_document':'2025-12-16','effective_from_claim':'2025-12-08','scope':'Seventh amendment only, Section XIII Part 9, footnote 94','action':'Greek hub Edition 8 plus seven amendments explains English hub Amendment 8 label (inference). No conflicting operative texts established; independent HCMC/Gazette decision remains unverified.'},
 {'id':'oslo-approval','sources':['14dc34b8e54e','822d46bb9149','1ee1619da83d'],'relationship':'approval-reservation-unresolved','effective_from_claim':'2024-09-02','scope':'VPO NOK 2 September 2024 edition','action':'System approval on regulator hub is insufficient to remove edition-specific subject-to-approval qualification.'},
 {'id':'cph-fee-periods','sources':['14e2c64da9a0','cdd34eb011e9'],'relationship':'announced-successor','current_fee_from_claim':'2026-01-01','future_fee_from_claim':'2026-11-01','current_revision_claim':'2025-12','future_revision_claim':'2026-07','action':'Select by charging date and service/volume, not publication month; no exact fee lines validated.'},
 {'id':'cph-version-label','sources':['cbdf3c1f8b51'],'relationship':'inconsistent-footer-version','effective_from_claim':'2026-08-03','scope':'Cover and footers 12/13','action':'Pin current linked PDF by hash and cover date; retain footer inconsistency, do not infer two different rulebooks.'},
 {'id':'porto-manual-dates','sources':['089b7aaef991'],'relationship':'separate-date-evidence','revision_date_claim':'2026-01-26','filename_date':'2026-02-16','url_upload_month':'2026-04','effective_from':None,'action':'V43 latest linked, not proven effective 16 February or April. Chapter 4 delegates hours/calendar to notices.'},
 {'id':'isin-columns','sources':['ac385b0f3106'],'relationship':'mixed-temporal-columns','data_through':'2026-09-10','file_date_claim':'2026-09-11','future_columns_effective_from':'2026-09-21','scope':'Introduction B5:B8 and I/K/L onward in instrument sheets','action':'Split historical current-place from future designated/alternative places; never infer general Milan/T2S eligibility.'},
 {'id':'jun-release','sources':['c164d86ada8e','aa3d5a3b94c9','t2s-2026-status-events'],'relationship':'release-with-deployment-evidence','publication_claim':'2026-01-22','deployment_confirmed':'2026-06-14','action':'Allow reviewed R2026.JUN technical passages subject to subsequent dated notices; June final documents found on current ECB hub.'},
 {'id':'nov-release','sources':['7244cf50f753'],'relationship':'future-draft-latest-located','revision_date_claim':'2026-07-31','upload_date_claim':'2026-08-03','planned_final_publication':'2026-09-11','effective_from':None,'action':'Live hub still exposed draft at audit. Planned publication date has passed; final November publication not verified. Do not promote draft or assume release deployed.'},
 {'id':'tplus1','sources':['32025R2075'],'relationship':'adopted-law-future-application','adoption_date':'2025-10-08','publication_date':'2025-10-14','entry_into_force':'2025-11-03','application_from':'2027-10-11','action':'Not a draft; future application collection. Current CSDR Art 5(2) remains T+2 ceiling for covered transactions.'},
 {'id':'settlement-discipline-2026','sources':['591deafae0a9'],'relationship':'adopted-commission-text-oj-status-unverified','adoption_date':'2026-07-06','publication_date':None,'entry_into_force':None,'application_schedule':[{'date':'2026-12-07','scope':'Default in Article 2'},{'date':'2027-07-01','scope':'Article 1(3)(a) only insofar as amending Article 5(4)(b) of 2018/1229; separately Article 1 points (8)(a)(i), (8)(b), (8)(c), (9), (11), (12), (13)'},{'date':'2027-10-11','scope':'Article 1(3)(b), (4), (5), (6), (7), (10)'}],'action':'Recheck exact amendment numbering/OJ before implementation. Article-level application windows required.'},
 {'id':'dora-language','sources':['02022R2554-20221227','dora-english-oj'],'relationship':'replacement-language-capture','observed_original_body_language':'fr','url_language':'en','replacement_body_language':'en','action':'Quarantine original as English-labelled evidence; retain French legal text with corrected language, admit only checked replacement provisions.'},
 {'id':'esma-lei','sources':['535f6a23062a','950e61a0ad04'],'relationship':'source-data-anomaly','scope':'Authorised CSDs C25','action':'Preserve truncated 529900LG70TCA in raw record. Corroborated full INTERBOLSA LEI 529900LG70TCAGWCXT47 belongs in separately sourced corrected field; GLEIF not checked.'}
]
# Resolve the captured MyInterbolsa evidence identifier rather than assume a URL hash.
for d in LIVE.values():
    if 'interbolsa.pt/Cliente/Core/MyPublic/DisciplinaDaLiquidacao' in d.get('url',''):REL[-1]['sources'][-1]=d['audit_id']
js('SOURCE-RELATIONSHIPS.json',REL)

stats={'as_of':'2026-09-13','catalogue_records_screened':len(CAT),'archived_webpage_records_screened':len(pages),'legal_capture_records_screened':len(LEG),'additional_discussion_web_records':len(discussion['additional_discussion_sources']),'user_attachment_records':1,'register_records_including_overlapping_origins':len(REG),'retained_archive_documents':800,'unique_archive_content_hashes':787,'substantively_reviewed_source_records':sum(r['substantive'] for r in REV.values()),'substantively_reviewed_archived_documents':sum(r['substantive'] and i in CM for i,r in REV.items()),'live_requests':len(LIVE),'live_http_200':sum(d.get('http_status')==200 for d in LIVE.values()),'existing_document_urls_hash_compared':sum('same_as_archived_bytes' in d for d in LIVE.values()),'unchanged_document_hashes':sum(d.get('same_as_archived_bytes') is True for d in LIVE.values()),'live_identity_checks_on_existing_current_operational_layer':sum(i in CU and CU[i]['knowledge_layer'] in ['current-local','current-infrastructure'] and d.get('same_as_archived_bytes') is True for i,d in LIVE.items()),'whole_operational_manuals_certified_current_in_every_provision':0,'rag_runtime_found':False,'retrieval_tests_run':0}
js('AUDIT-COUNTS.json',stats)
print(json.dumps(stats,indent=2))
