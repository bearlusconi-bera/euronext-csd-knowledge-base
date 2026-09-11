"""Add selected infrastructure standards and resolve document landing pages."""
import json,re,concurrent.futures as cf
from collect_sources import ROOT,ASOF,ident
from build_library import download,canonical

D=json.loads((ROOT/'catalogue.json').read_text());byurl={d['url']:d for d in D}
extras=[]
def add(u,title,hub,scope='regulatory-and-infrastructure',status='latest-source-listed-version'):
    u=canonical(u)
    if u in byurl:extras.append(byurl[u]);return
    d={'id':ident(u),'url':u,'title':title,'retrieved_at':ASOF,'markets':[scope],
       'topics':['regulatory-and-infrastructure'] if scope=='regulatory-and-infrastructure' else ['operational-documentation'],
       'priority':'P1','applicability_status':status,'review_status':'catalogued-only','edition_type':'standard-or-clean',
       'date_evidence':[],'occurrences':[{'hub':hub,'title':title,'context':'Selected official supporting source','section':''}]}
    byurl[u]=d;extras.append(d)

add('https://www.bis.org/cpmi/publ/d101a.pdf','CPMI-IOSCO Principles for Financial Market Infrastructures (2012)','https://www.bis.org/committees/cpmi/pfmi/overview',status='foundational-standard')
add('https://www.bis.org/cpmi/publ/d106.pdf','PFMI Disclosure Framework and Assessment Methodology (2012)','https://www.bis.org/committees/cpmi/pfmi/overview',status='foundational-standard')
add('https://ecsda.eu/wp-content/uploads/2024/09/2024_09_11_ECSDA_Framework_update.pdf','ECSDA CSDR Settlement Fails Penalties Framework - 11 September 2024','https://ecsda.eu/archives/14977',status='latest-public-update-found-not-law')
for f in (ROOT/'metadata').glob('*.json'):
    p=json.loads(f.read_text())
    if not isinstance(p,dict) or not p.get('links'):continue
    for a in p['links']:
        u=canonical(a['url'])
        if p['url']=='https://www.ecb.europa.eu/press/intro/publications/html/index.en.html' and re.search(r'202603_(investorrights|t1corporateevents)|t2shaprrep202602|202512_(ISOmigration|scorecarulebook|corporateevents|scoreboard)|202509_barriersmarketintegration',u):
            if a['title']!='English':add(u,a['title'],p['url'])
        if p['url']=='https://www.euronext.com/en/media/14651' and '.pdf' in u:add(u,'Euronext Securities Oslo Fee Schedule - January 2026',p['url'],'oslo','effective-2026-01-per-title')
        if p['url']=='https://www.euronext.com/en/media/11004' and '.pdf' in u:add(u,a['title'],p['url'],'oslo','translated-national-law-2023-check-current-original')
        if 'sdd/html' in p['url'] and 'R2026.NOV' in u and a['title']!='English':add(u,a['title'],p['url'],status='future-draft-market-review-2026-11')
        if 'convergence-programme' in p['url'] and '/2026-07/es-' in u:add(u,a['title'],p['url'],'group','programme-update-2026-07')

with cf.ThreadPoolExecutor(max_workers=4) as ex:
    for r in ex.map(download,{x['id']:x for x in extras}.values()):
        print(r['id'],r.get('http_status'),r.get('pages'),r.get('error'),flush=True)
for d in byurl.values():
    f=ROOT/'metadata/downloads'/f'{d["id"]}.json'
    if f.exists():d.update(json.loads(f.read_text()))
(ROOT/'catalogue.json').write_text(json.dumps(list(byurl.values()),ensure_ascii=False,indent=2))
