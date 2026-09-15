"""Collect official CSD web pages and document links, with resumable evidence."""
import concurrent.futures as cf
import hashlib, json, re, sys, time
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote
import requests
from lxml import html

ROOT = Path(__file__).resolve().parents[1]
from snapshot_guard import refuse_audited_snapshot
refuse_audited_snapshot(ROOT)
for folder in ['sources/pages','sources/documents','extracted','metadata']:
    (ROOT/folder).mkdir(parents=True,exist_ok=True)
ASOF='2026-09-11'
SEEDS = [
 'https://www.euronext.com/en/csd',
 'https://www.euronext.com/en/csd/copenhagen/legal-framework',
 'https://www.euronext.com/en/csd/milan/membership/rules-instructions',
 'https://www.euronext.com/en/csd/oslo/about-us',
 'https://www.euronext.com/en/csd/porto/legislation-and-regulation',
 'https://www.euronext.com/en/csd/porto/documentation',
 'https://www.euronext.com/en/csd/strategic-projects/european-offering',
 'https://www.euronext.com/en/csd/strategic-projects/convergence-programme',
 'https://athens.euronext.com/en/post-trade/csd',
 'https://athens.euronext.com/en/about/regulatory/athexcsd',
 'https://www.euronext.com/en/post-trade/euronext-securities/milan/membership/csd-expansion-documentation',
]

def clean(s): return ' '.join(s.split())
def norm(u):
    x=urlsplit(u)
    return urlunsplit((x.scheme,x.netloc,x.path.rstrip('/'),x.query,''))
def ident(u): return hashlib.sha256(u.encode()).hexdigest()[:12]
def allowed(u):
    p=urlsplit(u)
    return (p.netloc=='www.euronext.com' and p.path.startswith(('/en/csd','/en/post-trade/euronext-securities')) or p.netloc=='athens.euronext.com' and p.path.startswith(('/en/post-trade/csd','/en/about/regulatory/athexcsd','/en/about/regulatory/group/athexcsd'))) and not p.query and not re.search(r'/careers|/career|/contacts|/contact-us|/current-agms|/news-insights',p.path)
def fetch(u):
    meta_path=ROOT/'metadata'/f'{ident(u)}.json'
    if meta_path.exists(): return json.loads(meta_path.read_text())
    d={'url':u,'retrieved_at':ASOF,'id':ident(u)}
    try:
        r=requests.get(u,timeout=35,headers={'User-Agent':'Research document collection; public pages'})
        d.update(status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'),last_modified=r.headers.get('Last-Modified'))
        if r.status_code==200:
            tree=html.fromstring(r.content)
            mains=tree.xpath('//main[@id="content"]|//main')
            main=mains[-1] if mains else tree
            for el in main.xpath('.//script|.//style|.//nav|.//footer'):
                el.drop_tree()
            title=tree.xpath('//h1//text()') or tree.xpath('//title//text()')
            d['title']=clean(' '.join(title))
            d['text']='\n'.join(clean(t) for t in main.text_content().splitlines() if clean(t))
            links=[]
            for a in main.xpath('.//a[@href]'):
                dest=norm(urljoin(r.url,a.get('href')))
                if not dest.startswith('http'): continue
                context=a.getparent()
                for _ in range(3):
                    if context.getparent() is None or len(clean(context.text_content()))>800: break
                    context=context.getparent()
                links.append({'url':dest,'title':clean(a.text_content()),'context':clean(context.text_content())[:1400]})
            # Group navigation is useful only for the root page.
            if u=='https://www.euronext.com/en/csd':
                for a in tree.xpath('//a[@href]'):
                    dest=norm(urljoin(r.url,a.get('href')))
                    if allowed(dest): links.append({'url':dest,'title':clean(a.text_content()),'context':''})
            d['links']=list({(x['url'],x['title']):x for x in links}.values())
            d['local_html']=f'sources/pages/{ident(u)}.html'
            (ROOT/d['local_html']).write_bytes(r.content)
            d['sha256']=hashlib.sha256(r.content).hexdigest()
            (ROOT/'extracted'/f'{ident(u)}.md').write_text(f'# {d["title"]}\n\nSource: {u}\n\nRetrieved: {ASOF}\n\n'+d['text']+'\n')
    except Exception as e: d['error']=str(e)
    meta_path.write_text(json.dumps(d,ensure_ascii=False,indent=2))
    return d

def crawl():
    seen={}; queue=list(SEEDS)
    for depth in range(7):
        todo=[u for u in dict.fromkeys(queue) if u not in seen]
        todo=todo[:max(0,650-len(seen))]
        if not todo: break
        queue=[]
        with cf.ThreadPoolExecutor(max_workers=5) as ex:
            for d in ex.map(fetch,todo):
                seen[d['url']]=d
                for a in d.get('links',[]):
                    if allowed(a['url']): queue.append(a['url'])
        print('depth',depth,'pages',len(seen),'next',len(set(queue)),flush=True)
    docs={}
    for u,d in seen.items():
        for a in d.get('links',[]):
            if re.search(r'\.(pdf|docx?|xlsx?|pptx?|zip)(?:[/?]|$)|/media/\d+(?:/download)?$',a['url'],re.I):
                doc=docs.setdefault(a['url'],{'id':ident(a['url']),'url':a['url'],'occurrences':[]})
                doc['occurrences'].append({'hub':u,'title':a['title'],'context':a['context']})
    (ROOT/'metadata/pages.json').write_text(json.dumps(list(seen.values()),ensure_ascii=False,indent=2))
    (ROOT/'metadata/discovered-documents.json').write_text(json.dumps(list(docs.values()),ensure_ascii=False,indent=2))
    (ROOT/'metadata/unvisited-pages.json').write_text(json.dumps(sorted(set(queue)-set(seen)),indent=2))
    print('DOCUMENTS',len(docs),'FAILED',[(u,d.get('status'),d.get('error')) for u,d in seen.items() if d.get('status')!=200],flush=True)

if __name__=='__main__': crawl()
