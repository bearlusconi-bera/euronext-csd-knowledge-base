import pathlib,json,hashlib,collections,csv,fitz,zipfile
A=pathlib.Path(__file__).resolve().parents[1];B=A.parents[1]
def read(n):return json.loads((A/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,ok,detail):checks.append({'check':name,'status':'PASS' if ok else 'FAIL','detail':detail})
c=json.loads((B/'catalogue.json').read_text()); byid={x['id']:x for x in c}
old=read('evidence/original-hashes.json')
bad=[i for i,h in old.items() if not (B/byid[i]['local_path']).exists() or sha(B/byid[i]['local_path'])!=h]
check('All retained originals preserved',not bad,{'checked':len(old),'changed_or_missing':bad})
base=read('evidence/root-file-hashes-before.json'); changed=[p for p,h in base.items() if not (B/p).exists() or sha(B/p)!=h]
check('Root manifests and explanations preserved',not changed,{'checked':len(base),'changed_or_missing':changed})
r=read('SOURCE-DECISIONS.json');screened=[x for x in r if x['inventory_origin']=='catalogue']
check('One decision for every catalogue entry',len(screened)==918 and {x['source_id'] for x in screened}==set(byid),len(screened))
check('Unique decision IDs',len({x['source_id'] for x in r})==len(r),len(r))
check('No whole-document operational defaults',all(x['default_retrieval_proposed'] is False for x in r),'All decision rows false; section proposals separate.')
badpaths=[x['source_id'] for x in r if x.get('local_path') and not pathlib.Path(x['local_path']).exists()]
check('Source local paths resolve',not badpaths,badpaths)
e=read('EVALUATION-SET.json')
check('At least 20 unique evidence-backed fixtures',len(e)>=20 and len({x['id'] for x in e})==len(e) and all(x['required_citations'] and x['expected_answer'] and x['failure_conditions'] for x in e),len(e))
check('Retrieval results honestly NOT RUN',all(x['execution_status']=='NOT_RUN' and not x['retrieved_evidence'] and x['actual_answer'] is None for x in e),'No fabricated retrieval/model outcomes.')
m=read('COVERAGE-MATRIX.json')
check('All five markets represented',set(['Milan','Copenhagen','Porto','Oslo','Athens']) <= {x['entity_service'] for x in m},collections.Counter(x['entity_service'] for x in m))
check('Coverage rows complete',all(x['practical_question'] and x['required_and_supporting_evidence'] and x['gap_or_condition'] and x['status'] in ['covered','partial','missing','access-restricted','unresolved','not applicable'] for x in m),collections.Counter(x['status'] for x in m))
rv=read('REVIEWED-SOURCES.json');badpages=[]
for x in rv:
 if not x['pdf_pages_reviewed']:continue
 i=x['source_id'];p=B/byid[i]['local_path'] if i in byid else A/'sources'/f'{i}.pdf'
 if not p.exists():badpages.append([i,'missing original']);continue
 d=fitz.open(p)
 if any(n<1 or n>len(d) for n in x['pdf_pages_reviewed']):badpages.append([i,'out-of-range page'])
check('Recorded PDF sample indices resolve',not badpages,badpages)
ids={x['source_id'] for x in r}
relationships=read('SOURCE-RELATIONSHIPS.json');badids=[i for x in relationships for i in x['sources'] if i not in ids]
allow=read('RETRIEVAL-PROPOSAL.json')['allowlist'];badids += [i for x in allow for i in x['sources'] if i not in ids]
check('Relationship and allowlist sources resolve',not badids,badids)
live=[json.loads(p.read_text()) for p in (A/'evidence').glob('live-*.json')];badlive=[]
for x in live:
 if x.get('saved_path') and sha(A/x['saved_path'])!=x.get('sha256'):badlive.append(x['audit_id'])
check('Saved live evidence hashes match',not badlive,{'checked':sum(bool(x.get('saved_path')) for x in live),'mismatch':badlive})
attachment=pathlib.Path(json.loads((B/'metadata/discussion-sources.json').read_text())['user_attachment']['local_path'])
check('User attachment identity',attachment.exists() and sha(attachment)=='6a49ab91bce38b2687a9daf88cbc8279fff28ff65d6eeb4cb1aeaf2e0401bb90','Identity only; no full substantive audit of attachment.')
with (A/'SOURCE-DECISIONS.csv').open(newline='') as f: csvrows=list(csv.DictReader(f))
check('CSV/JSON source decision parity',len(csvrows)==len(r),len(csvrows))
(A/'evidence/audit-static-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
lines=['# Verification results — 13 September 2026','','These are static artifact/preservation checks, not retrieval tests or proof that the entire source library is correct.','','| Check | Result | Evidence |','| --- | --- | --- |']
for x in checks:lines.append('| '+x['check']+' | '+x['status']+' | '+str(x['detail']).replace('|','/')+' |')
lines += ['','## Existing library defects and blocked checks','','- **FAIL — content completeness:** UDFS PDF 269 field diagram absent from text extraction (F05).','- **FAIL — metadata/language integrity:** English-labelled DORA capture contains French operative text (F06).','- **FAIL — safe operational selection:** current Milan timing sources conflict; whole-document defaults cannot isolate the affected clauses (F01/F04).','- **BLOCKED — independent authority confirmation:** HCMC route refused connection; Oslo edition approval not found. This does not imply the underlying rules are invalid.','- **NOT RUN — 34 retrieval evaluations:** no retrieval runtime/index located; see EVALUATION-SET.json.','- **NOT RUN — full schema validation, authenticated client-interface testing, complete legal and whole-document review:** outside accessible/selected evidence.','','All recommended changes remain proposals. No tests were added to a production application because none was present.']
(A/'VERIFICATION.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'checks':len(checks),'passed':sum(x['status']=='PASS' for x in checks),'failed':[x for x in checks if x['status']=='FAIL']},indent=2))
