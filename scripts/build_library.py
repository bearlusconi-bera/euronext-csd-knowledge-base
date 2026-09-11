"""Build a provenance catalogue and archive prioritised official documents."""
import concurrent.futures as cf
import hashlib,json,re,unicodedata,sys
from pathlib import Path
from urllib.parse import urljoin,urlsplit,urlunsplit,unquote
import requests,fitz
from lxml import html
from collect_sources import ROOT,ASOF,ident,clean,norm

DOC_RE=re.compile(r'\.(pdf|docx?|xlsx?|pptx?|zip)(?:[/?]|$)|/media/\d+(?:/download)?$',re.I)
CORE_HUBS=['rules-instructions','euronext-securities-copenhagen-rule-book','vp-rule-book','oslo/about-us/legal-framework','porto/legislation-and-regulation/our-rules','porto/documentation/operational-documentation','about/regulatory/athexcsd','programme-documentation','csd-expansion-documentation','corporate-events-service']
TOPICS={
 'rules-and-authorisation':r'rule|regulat|csdr|legal|authoris|resolution|circular',
 'participation-and-accounts':r'particip|admission|application|account|segregat|onboard|membership|client.master',
 'settlement':r'settlement|t2s|vpo|vps|penalt|t\+1|t_1|timetable|operational.day',
 'issuance-and-registration':r'issu|registr|securities.management|codific|nna|isin',
 'asset-servicing-and-tax':r'corporate|ca4u|asset.servic|dividend|tax|fiscal|vot|shareholder|meeting',
 'connectivity-and-testing':r'connect|swift|iso.?(15022|20022)|message|interface|gateway|test|dictionary|layout',
 'risk-and-resilience':r'risk|insolven|default|continuity|disclosure|iosco|cpmi|agc|dora|resilien|due.diligence',
 'pricing':r'fee|pricing|price|tariff',
}

def canonical(u):
    p=urlsplit(u)
    if p.netloc=='www.ecb.europa.eu':return urlunsplit((p.scheme,p.netloc,p.path,'',''))
    return norm(u)

def inventory():
    docs={};pages=[]
    for f in sorted((ROOT/'metadata').glob('*.json')):
        d=json.loads(f.read_text())
        if not isinstance(d,dict) or 'url' not in d or 'links' not in d:continue
        pages.append(d)
        # Re-parse stored page to retain accurate table-row and section metadata.
        tree=html.fromstring((ROOT/d['local_html']).read_bytes()) if d.get('local_html') else None
        for a in d['links']:
            u=canonical(a['url'])
            if not DOC_RE.search(u):continue
            title=a['title'];context=a['context'];section=''
            if tree is not None:
                matches=[x for x in tree.xpath('//a[@href]') if canonical(urljoin(d.get('final_url',d['url']),x.get('href')))==u]
                if matches:
                    el=matches[0];rows=el.xpath('ancestor::tr')
                    if rows:
                        context=clean(rows[-1].text_content())
                        cells=rows[-1].xpath('./td')
                        if cells and (not title or title.lower() in ['downloadpdf','download','english']):title=clean(cells[0].text_content())
                    heads=el.xpath('preceding::h2|preceding::h3|preceding::h4|preceding::h5')
                    if heads:section=clean(heads[-1].text_content())
            if not title or title.lower() in ['download','english','downloadpdf','click here','link','pdf']:
                title=unquote(urlsplit(u).path.rsplit('/',1)[-1])
                if title=='download':title=(context[:170] or d.get('title','Untitled'))
            doc=docs.setdefault(u,{'id':ident(u),'url':u,'title':title,'occurrences':[],'retrieved_at':ASOF})
            occurrence={'hub':d['url'],'title':title,'context':context,'section':section}
            if occurrence not in doc['occurrences']:doc['occurrences'].append(occurrence)
            if len(doc['title'])>220 and len(title)<220:doc['title']=title
    for d in docs.values():
        context=' '.join(x['hub']+' '+x['title']+' '+x['section'] for x in d['occurrences'])
        d['markets']=[m for m in ['milan','copenhagen','oslo','porto','athens'] if m in context.lower()]
        if not d['markets']:d['markets']=['group' if 'euronext' in d['url'] else 'regulatory-and-infrastructure']
        d['topics']=[k for k,v in TOPICS.items() if re.search(v,d['title']+' '+unquote(d['url']),re.I)]
        d['priority']='P1' if any(h in context for h in CORE_HUBS) else 'P2' if d['topics'] else 'P3'
        d['applicability_status']='unverified-public-source'
        d['review_status']='catalogued-only'
        d['date_evidence']=list(dict.fromkeys(re.findall(r'\b\d{2}/\d{2}/20\d{2}\b|\b20\d{2}-\d{2}-\d{2}\b', ' '.join(x['context'] for x in d['occurrences']))))
        if any(re.search(r'revoked|abrogat|archiv|previous version',x['section'],re.I) for x in d['occurrences']):
            d['applicability_status']='historical-section';d['priority']='P3'
        if re.search(r'track.?change|with.?evidence|with.?ev_|revised|revision.mark',d['title']+' '+d['url'],re.I) and not re.search('without',d['title']+' '+d['url'],re.I):
            d['edition_type']='redline-or-revision-marks'
        else:d['edition_type']='standard-or-clean'
        # Latest posted is not necessarily effective. Preserve that distinction.
        if re.search(r'Nov(?:ember)?[ _%]*2026|R2026.NOV',d['title']+' '+unquote(d['url']),re.I):d['applicability_status']='future-version'
        if any('programme-documentation' in x['hub'] or 'csd-expansion-documentation' in x['hub'] for x in d['occurrences']):
            d['applicability_status']='programme-document-service-applicability-varies'
        if any('ecb.europa' in x['hub'] for x in d['occurrences']):
            d['priority']='P1' if re.search(r'R2026.JUN.*clean|CoverNote_Final',d['url'],re.I) else 'P3'
        if re.search(r'annual.report|financial.statement|audited|financial.report|annual.account|statistics|statistical|share.capital|board.*director',d['title'],re.I):d['priority']='P3'
        if re.search(r'webinar|newsletter|global.reference.group',d['title'],re.I):d['priority']='P3'
    (ROOT/'metadata/all-pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
    (ROOT/'catalogue.json').write_text(json.dumps(list(docs.values()),ensure_ascii=False,indent=2))
    return list(docs.values())

def download(d):
    out=ROOT/'metadata/downloads'/f'{d["id"]}.json';out.parent.mkdir(exist_ok=True)
    if out.exists():return json.loads(out.read_text())
    result={'id':d['id'],'url':d['url'],'retrieved_at':ASOF}
    try:
        r=requests.get(d['url'],timeout=50)
        result.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'),last_modified=r.headers.get('Last-Modified'))
        if r.status_code==200:
            b=r.content
            if b[:5]==b'%PDF-':ext='.pdf'
            elif b[:2]==b'PK':
                ext=Path(unquote(urlsplit(r.url).path)).suffix.lower()
                if ext not in ['.xlsx','.docx','.pptx','.zip']:ext='.zip'
            elif b[:4]==bytes([208,207,17,224]):ext=Path(unquote(urlsplit(r.url).path)).suffix.lower() or '.bin'
            else:
                result['error']='Response was not a recognised document (possibly a media landing page)';out.write_text(json.dumps(result,indent=2));return result
            slug=re.sub(r'[^a-zA-Z0-9]+','-',unicodedata.normalize('NFKD',d['title']).encode('ascii','ignore').decode()).strip('-')[:90]
            result['local_path']=f'sources/documents/{d["id"]}-{slug}{ext}'
            (ROOT/result['local_path']).write_bytes(b)
            result.update(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),file_type=ext[1:],review_status='archived-not-substantively-reviewed')
            if ext=='.pdf':
                pdf=fitz.open(stream=b,filetype='pdf');result['pages']=len(pdf)
                contents=[];empty=[]
                for n,page in enumerate(pdf,1):
                    t=page.get_text(sort=True)
                    if len(t.strip())<30:empty.append(n)
                    contents.append(f'\n\n## PDF page {n}\n\n'+t)
                result['text_path']=f'extracted/{d["id"]}.md'
                (ROOT/result['text_path']).write_text(f'# {d["title"]}\n\nSource: {d["url"]}\n\nRetrieved: {ASOF}\n\nExtraction: text only; reading order and graphics not verified.\n'+''.join(contents))
                result.update(text_characters=sum(map(len,contents)),low_text_pages=empty,review_status='text-extracted-not-substantively-reviewed',pdf_metadata=pdf.metadata)
                pdf.close()
    except Exception as e:result['error']=str(e)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2));return result

def main():
    docs=inventory()
    selected=[d for d in docs if d['priority'] in ['P1','P2']]
    print('discovered',len(docs),'selected',len(selected),flush=True)
    if '--inventory-only' in sys.argv:return
    results={}
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for i,r in enumerate(ex.map(download,selected),1):
            results[r['id']]=r
            if i%25==0:print('processed',i,'/',len(selected),flush=True)
    for d in docs:
        if d['id'] in results:d.update(results[d['id']])
    (ROOT/'catalogue.json').write_text(json.dumps(docs,ensure_ascii=False,indent=2))
    print('saved',sum('local_path' in d for d in docs),'pages',sum(d.get('pages',0) for d in docs),'failures',sum('error' in d or d.get('http_status',200)!=200 for d in docs),flush=True)

if __name__=='__main__':main()
