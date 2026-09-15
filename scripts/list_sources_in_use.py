"""List all retained/discovered documents and identify recent discussion sources."""
import json,hashlib,re
from pathlib import Path
from collections import defaultdict

R=Path(__file__).resolve().parents[1]
from snapshot_guard import refuse_audited_snapshot
refuse_audited_snapshot(R)
C=json.loads((R/'catalogue.json').read_text())
M=json.loads((R/'curated-manifest.json').read_text())
B={x['id']:x for x in C}
def local(path,label):return f'[{label}](<{R/path}>)'
def esc(s):return str(s or '').replace('|','/').replace('\n',' ').strip()
def doclink(x):
    return local(x['local_path'],esc(x['title'])) if x.get('local_path') else f'[{esc(x["title"])}]({x["url"]})'

recent=[
 {'id':'71233aed41e7','role':'Main Euronext source for investor-CSD links, matching and message flows. Convergence document; used with the current T2S specification for platform mechanics.','review':'Selected passages substantively read; not a full-document review.','page_references':[12,20,28,29,33,36,37,40,41,42,44,50,83]},
 {'id':'aa3d5a3b94c9','role':'Main current-release T2S source for business-day timing, realignment, instruction processing and message types.','review':'Selected passages substantively read and table of contents checked; not a full-document review.','page_references':[87,157,160,162,163,165,168,171,373,374,375,376,385,386,387,753,778,1370]},
]
online=[
 {'title':'ECB Payments and Markets Glossary — investor CSD and issuer CSD','url':'https://www.ecb.europa.eu/services/glossary/html/act7i.en.html','role':'Definitions of investor CSD, issuer CSD and their relationship.'},
 {'title':'ECSDA Frequently Asked Questions','url':'https://ecsda.eu/faq','role':'The same CSD can act as issuer or investor CSD for different securities.'},
 {'title':'ECB — What is T2S?','url':'https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html','role':'Delivery versus payment, central-bank cash and participant access.'},
 {'title':'T2S Framework Agreement — October 2025 edition','url':'https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/shared/pdf/2025-10_T2S_Framework_Agreement_internet_published.pdf','role':'Matching requirements and permitted settlement-amount tolerances; consulted online, not saved as an original in the initial 800-file archive.'},
 {'title':'ESMA — Finalise preparations ahead of T+1 settlement deadlines','url':'https://www.esma.europa.eu/press-news/esma-news/esma-calls-firms-finalise-preparations-ahead-t1-settlement-deadlines','role':'EU T+1 transition date and earlier preparation milestones; underlying statement is also archived.'},
 {'title':'ECB — T2S Scope Defining Documents','url':'https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/html/index.en.html','role':'Version check distinguishing the R2026.JUN final set from R2026.NOV market-review drafts.'},
]
attachment=Path('/Users/mattiadalessandra/Downloads/service_description_document_-_settlement_services_v1.5 (2).pdf')
A={'title':'Euronext Securities Settlement Service Description Document v1.5 — November 2025','local_path':str(attachment),'pages':108,'review':'Attachment cover/version and SHA-256 compared with the library. It was not the primary basis for the settlement explanations.'}
if attachment.exists():A['sha256']=hashlib.sha256(attachment.read_bytes()).hexdigest()
source_use={'prepared_on':'2026-09-13','original_library_snapshot':'2026-09-11','scope':'Retrospective source list for this conversation, not a refreshed document sweep.','main_discussion_documents':recent,'additional_discussion_sources':online,'user_attachment':A}
(R/'metadata/discussion-sources.json').write_text(json.dumps(source_use,ensure_ascii=False,indent=2)+'\n')

out=['# Full document and source list','',
'Prepared 13 September 2026 from the 11 September research library and subsequent discussion. This inventory distinguishes files available for research from sources actually used in recent explanations. It is not a claim that every listed document has been fully read or remains applicable to every service.','',
'## Direct sources for our recent explanations','',
'These supported the investor-CSD definition, cross-CSD flow, T0/T+1/T+2 timeline and meaning of “matched”.','',
'| Source | Use and review scope |','|---|---|']
for s in recent:
    x=B[s['id']]
    out.append(f'| {doclink(x)} · [Official PDF]({x["url"]}) | {s["role"]} {s["review"]} Page references: {", ".join(map(str,s["page_references"]))}. |')
for x in online:out.append(f'| [{x["title"]}]({x["url"]}) | {x["role"]} |')
out += ['', '## Your attached document','',f'[{A["title"]}](<{attachment}>) — 108 pages. {A["review"]}','',
'## How to interpret the full inventory','',
'- **800 retained original files**, representing **787 unique contents** after checksum deduplication.',
'- **84 prioritised documents** from those files, plus **14 selected complete legal-text captures**. The curated reading list has 98 entries.',
'- **118 additional discovery records**: 107 not downloaded, 1 unresolved media link, 6 excluded staff photographs and 4 legacy links resolved to other records.',
'- The six online references above and your attachment are identified separately. They are not added to the original 800-file acquisition count.',
'- Other website discovery pages are recorded separately in '+local('metadata/all-pages.json','the source-page inventory')+'.',
'- Dates in the entries below are manually curated only where stated. Other documents need individual applicability/version validation.',
'', 'The documents listed in response to your Milan and T2S inventory questions were checked for availability/version. Listing a document is not the same as using all its contents to substantiate an answer. See '+local('READING-GUIDE.md','the 98-entry prioritised reading guide')+' for intended scope, and '+local('COVERAGE-AND-CAVEATS.md','coverage and limitations')+'.','']

groups=defaultdict(list)
for x in C:
    if x.get('local_path'):
        group=x.get('curated_group') or (x.get('markets') or ['Other'])[0]
        aliases={'milan':'Milan','copenhagen':'Copenhagen','porto':'Porto','oslo':'Oslo','athens':'Athens','group':'Group and programmes','regulatory-and-infrastructure':'Regulation and infrastructure'}
        groups[aliases.get(group,group)].append(x)
out += ['## All downloaded documents','',
'Each retained document URL is listed once below. Identical contents from different URLs are explicitly marked. Local document links and original source URLs are both provided.','',
'| Scope | Files |','|---|---:|']
for g,xs in sorted(groups.items()):out.append(f'| {g} | {len(xs)} |')
n=0
for g,xs in sorted(groups.items()):
    out += ['',f'### {g}','']
    for x in sorted(xs,key=lambda x:(not bool(x.get('curated_group')),x['title'].lower())):
        n+=1
        out += [f'{n}. **{doclink(x)}**',f'   - ID: `{x["id"]}`. [Official source]({x["url"]}). Format: {x.get("file_type","unknown").upper()}'+(f'; {x["pages"]:,} PDF pages.' if x.get('pages') else '.'),f'   - '+esc(x.get('version_date_evidence') or 'Version/effective date not individually validated in this inventory.')]
        if x.get('knowledge_layer'):out.append(f'   - Classification: {x["knowledge_layer"]}.')
        if x.get('review_scope'):out.append(f'   - Review scope: {esc(x["review_scope"])}')
        else:out.append('   - Archived/extracted for reference; no complete substantive review claimed.')
        if x.get('duplicate_of'):out.append(f'   - Identical file contents to document `{x["duplicate_of"]}`; preserve both source URLs.')
        out.append('')
assert n==800

out += ['## Selected legal texts','',
'These 14 EUR-Lex texts are complete browser captures, separate from the 800 original download files. Consolidation dates and provision-level application dates must be interpreted separately.','',
'| Legal text | Why it is included | Local capture |','|---|---|---|']
for x in M['legal_texts']:
    out.append(f'| [{esc(x["title"])}]({x["url"]}) | {esc(x["why_read"])} | {local(x["text_path"],"Saved text")} |')
out += ['', '## Discovery records without a retained original','',
'These are included for completeness and are not represented as documents used to support our answers. A resolved legacy link points to another retained record.','',
'| ID | Linked title | Acquisition result |','|---|---|---|']
for x in C:
    if x.get('local_path'):continue
    status=x.get('acquisition_disposition','unknown')
    if x.get('resolved_by'):status+=f' → `{x["resolved_by"]}`'
    out.append(f'| `{x["id"]}` | [{esc(x["title"])}]({x["url"]}) | {status} |')
out += ['', '## Machine-readable files','',
local('catalogue.json','Original document inventory')+' · '+local('curated-manifest.json','Prioritised sources')+' · '+local('metadata/discussion-sources.json','Sources used in this discussion'), '']
target=R/'FULL-DOCUMENT-LIST.md';target.write_text('\n'.join(out))

# Verify every local link and one-to-one coverage of the acquisition inventory.
missing=[]
for s in re.findall(r'\]\(<(/[^>]+)>\)',target.read_text()):
    if not Path(s).exists():missing.append(s)
check={'prepared_on':'2026-09-13','retained_files_listed':n,'discovery_records_without_original':sum(not bool(x.get('local_path')) for x in C),'legal_texts':len(M['legal_texts']),'additional_discussion_references':len(online),'main_discussion_documents':len(recent),'user_attachments':1,'missing_local_links':missing}
(R/'verification/full-list-check.json').write_text(json.dumps(check,indent=2)+'\n')
print(json.dumps(check,indent=2))
assert not missing
