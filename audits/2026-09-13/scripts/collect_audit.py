import concurrent.futures as cf
import datetime, hashlib, json, pathlib, re, sys
from urllib.parse import urljoin, urlsplit
import requests, fitz
from lxml import html

A=pathlib.Path(__file__).resolve().parents[1]
B=A.parents[1]
CAT=json.loads((B/'catalogue.json').read_text())
CUR=json.loads((B/'curated-manifest.json').read_text())

def save(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2))

def fetch(x):
    u=x['url']; ident=x.get('id') or hashlib.sha256(u.encode()).hexdigest()[:12]
    meta=A/'evidence'/f'live-{ident}.json'
    if meta.exists(): return json.loads(meta.read_text())
    d={**x,'audit_id':ident,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        r=requests.get(u,timeout=(12,45),headers={'User-Agent':'Mozilla/5.0 (independent public-document audit)'})
        d.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'),last_modified_http=r.headers.get('Last-Modified'),etag=r.headers.get('ETag'),sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content))
        suffix='.pdf' if r.content.startswith(b'%PDF-') else pathlib.Path(urlsplit(r.url).path).suffix.lower()
        if suffix not in ['.pdf','.xlsx','.xls','.docx','.zip']:suffix='.html'
        out=A/'sources'/f'{ident}{suffix}';out.write_bytes(r.content);d['saved_path']=str(out.relative_to(A))
        if x.get('original_sha256'):d['same_as_archived_bytes']=d['sha256']==x['original_sha256']
        if r.status_code==200 and suffix=='.pdf':
            pdf=fitz.open(out);d['pdf_pages']=len(pdf)
            t='\n'.join(f'\n## PDF page {n+1}\n'+p.get_text(sort=True) for n,p in enumerate(pdf))
            out=A/'extracted'/f'{ident}.md';out.write_text(t);d['text_path']=str(out.relative_to(A))
        elif r.status_code==200 and suffix=='.html':
            tree=html.fromstring(r.content);main=tree.xpath('//main');main=main[-1] if main else tree
            for e in main.xpath('.//script|.//style|.//nav|.//footer'):e.drop_tree()
            t='\n'.join(' '.join(s.split()) for s in main.text_content().splitlines() if s.strip())
            out=A/'extracted'/f'{ident}.txt';out.write_text(t);d['text_path']=str(out.relative_to(A))
            d['title']=' '.join(tree.xpath('//h1//text()') or tree.xpath('//title//text()'))
            d['links']=[{'title':' '.join(e.text_content().split()),'url':urljoin(r.url,e.get('href'))} for e in main.xpath('.//a[@href]')]
    except Exception as e:d['error']=str(e)
    save(meta,d);return d

def inventory():
    errors=[];hashes={};counts={};originals=[]
    for d in CAT:
        p=B/d['local_path'] if d.get('local_path') else None
        if p and p.exists():
            h=hashlib.sha256(p.read_bytes()).hexdigest();hashes[d['id']]=h; originals.append(p)
            if h!=d.get('sha256'):errors.append({'id':d['id'],'problem':'hash mismatch'})
        elif p:errors.append({'id':d['id'],'problem':'missing original'})
        if d.get('text_path') and not (B/d['text_path']).exists():errors.append({'id':d['id'],'problem':'missing extraction'})
    counts={'catalogue_entries':len(CAT),'retained_records':len(originals),'unique_contents':len(set(hashes.values())),'curated_documents':len(CUR['documents']),'legal_captures':len(CUR['legal_texts']),'pdf_pages':sum(d.get('pages') or 0 for d in CAT),'file_types':{t:sum(d.get('file_type')==t for d in CAT) for t in ['pdf','xlsx','xls','docx','zip']},'default_true_documents':sum(d.get('default_retrieval',False) for d in CUR['documents']),'default_true_without_text':[d['id'] for d in CUR['documents'] if d.get('default_retrieval') and not d.get('text_path')],'hash_errors':errors,'pdfs_with_low_text_pages':sum(bool(d.get('low_text_pages')) for d in CAT),'low_text_page_total':sum(len(d.get('low_text_pages',[])) for d in CAT)}
    save(A/'evidence/inventory-check.json',counts)
    save(A/'evidence/original-hashes.json',hashes)
    baseline={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.iterdir() if p.is_file()}
    save(A/'evidence/root-file-hashes-before.json',baseline)
    print(json.dumps(counts),flush=True)

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='inventory':inventory();sys.exit()
    if mode=='curated':
        rows=[{'id':d['id'],'url':d['source_url'],'title':d['title'],'original_sha256':d.get('sha256'),'kind':'curated-document'} for d in CUR['documents'] if d['default_retrieval'] or d['id'] in ['d89c56df8c5a','14dc34b8e54e','cdd34eb011e9','71233aed41e7','7244cf50f753','de2d312169fc','00a3e1aeba1c','f488a7016d8c']]
    else:rows=json.loads((A/sys.argv[1]).read_text())
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        results=list(pool.map(fetch,rows))
    save(A/'evidence'/f'fetch-{pathlib.Path(mode).stem}.json',results)
    for d in results:print(d['audit_id'],d.get('http_status'),d.get('same_as_archived_bytes'),d.get('title',d['url']),d.get('error',''),flush=True)
