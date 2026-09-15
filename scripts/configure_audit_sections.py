"""One-time reviewed section decisions for the 13 September audit implementation.

The resulting JSON is the reviewable configuration. This script refuses to overwrite it.
Adding a source/section requires an editorial decision, never a layer-based default.
"""
import hashlib
import json
import subprocess
from pathlib import Path

R = Path(__file__).resolve().parents[1]
A = R / "audits/2026-09-13"
I = R / "implementation/2026-09-13"
C = {x["id"]: x for x in json.loads((R / "catalogue.json").read_text())}
L = {x["id"]: x for x in json.loads((R / "curated-manifest.json").read_text())["legal_texts"]}
SOURCES, SECTIONS = {}, []


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def register(id, language="en", authority=None, text_override=None):
    if id in SOURCES:
        return
    if id in C:
        d = C[id]; p = R / d["local_path"]; t = R / d["text_path"] if d.get("text_path") else None
    elif id in L:
        d = L[id]; p = t = R / d["text_path"]
    else:
        f, base = I / "evidence" / f"{id}.json", R
        if not f.exists():
            f, base = A / "evidence" / f"live-{id}.json", A
        d = json.loads(f.read_text()); p = base / d.get("local_path", d.get("saved_path"))
        t = base / d["text_path"] if d.get("text_path") else None
    if t is None and text_override:
        t = R / text_override
    if t is None:
        t = I / "extracted" / f"{id}.md"; t.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix == ".pdf":
            raw = subprocess.check_output(["pdftotext", "-layout", str(p), "-"], text=True)
            t.write_text("\n".join(f"## PDF page {i+1}\n\n{x}" for i, x in enumerate(raw.split("\f")) if x.strip()))
        else:
            t.write_text(p.read_text())
    assert sha(p) == d["sha256"], (id, "source changed")
    SOURCES[id] = {"id": id, "title": d.get("title", id), "url": d["url"],
                   "local_path": str(p.relative_to(R)), "sha256": d["sha256"],
                   "text_path": str(t.relative_to(R)), "text_sha256": sha(t),
                   "actual_content_language": language, "authoritative_language": authority,
                   "publication_date": None, "revision_date": None, "effective_from": None, "effective_to": None,
                   "verified_as_of": "2026-09-13", "document_version": d.get("version_date_evidence"),
                   "approval_status": "Source identity checked; no independent whole-edition supervisory approval certification",
                   "date_evidence": d.get("version_date_evidence", d.get("retrieved_at_utc", d.get("retrieved_at"))),
                   "provenance_note": "Only specified excerpts are admitted; original preserved."}


def part(id, pages=None, start=None, end=None, article=None, path=None, locator=None, lang="en", auth=None):
    register(id, lang, auth, path)
    x = {"source_id": id, "kind": "pdf_pages" if pages else "article" if article else "structured" if path and path.endswith(".json") else "text",
         "locator": locator or (f"PDF pages {pages}" if pages else f"Article {article}" if article else "Reviewed structured derivative")}
    for k, v in [("pages", pages), ("start", start), ("end", end), ("article", article), ("path", path)]:
        if v is not None:
            x[k] = v
    if path:
        x["derivative_sha256"] = sha(R / path)
    return x


def add(id, title, extracts, topics, entities, *, services=None, modes=None, roles=None, notes=None, deps=None, required=None, effective=None):
    SECTIONS.append({"id": id, "title": title, "decision": "admit", "verified_as_of": "2026-09-13",
                     "entities": entities, "services": services or ["settlement"], "roles": roles or ["participant", "csd_operator"],
                     "modes": modes or ["current"], "question_types": topics, "extracts": extracts,
                     "dependency_ids": deps or [], "required_context": required or [],
                     "effective_from": effective, "effective_to": None,
                     "applicability_rule": "Verified knowledge snapshot only; earlier/later applicability requires a separate reviewed decision. Event business dates are separately scoped.",
                     "review_depth": "Specified excerpts read; not whole-document certification",
                     "permitted_use": title, "limitations": notes or [],
                     "security_link_context": "No individual ISIN, entitlement, account or custody chain is certified",
                     "platform_release": "R2026.JUN" if any(p["source_id"] == "aa3d5a3b94c9" for p in extracts) else None})


def add_followups():
    add("porto-dcp", "DCP technical access preserves the INTERBOLSA contractual relationship",
        [part("fcbc69b0fc35", [1,2], "Article 2", "Article 3", locator="Regulation 1/2016 Article 2, including 2(4); PDF 1–2", auth="pt")],
        ["dcp_relationship"], ["Porto"], notes=["Published rule; does not establish a particular participant's entitlements or replace local user specifications."])
    add("athens-cash", "Published DSS euro versus non-euro cash arrangements",
        [part("410859953fce", [2,3,4], "Purpose & Scope", "PART 2. Settlement Methods", locator="Resolution 5 purpose/scope and §§1.1–1.2; PDF 2–4", auth="el")],
        ["cash_arrangements"], ["Athens"], modes=["reference"], notes=["Informational English translation; Greek prevails. No account, currency-specific entitlement or complete current production procedure is certified."])
    add("athens-csa", "CSA staffing requirement with expressly stated exemptions",
        [part("513a8da7c0ad", [1,2], end="2. The CSA Certificate shall be granted", locator="Resolution 2 §§1 and 2.1(1), including exemptions and effect footnote; PDF 1–2", auth="el")],
        ["staff_certification"], ["Athens"], modes=["reference"], notes=["Informational English translation. Exemptions must accompany the staffing rule; candidate certification requirements are outside this excerpt."], effective="2026-07-20")
    add("oslo-liquidity", "Primary and substitute liquidity-bank declarations as published",
        [part("14dc34b8e54e", [17,18], locator="VPO NOK Rules §§9–10; PDF 17–18", auth="no")],
        ["liquidity_duties"], ["Oslo"], modes=["reference"], deps=["oslo-edition"], notes=["Unresolved edition approval must accompany any description. Section 20 conditions are not reviewed for a funding implementation."])
    add("esma-decision", "ESMA initial authorisation versus UK Stamp Duty extension",
        [part("535f6a23062a", path="implementation/2026-09-13/structured/esma-milan-decisions.json", locator="0- Info B12 and 1- CSD authorisations rows 23 and 36")],
        ["register_decision_type"], ["Milan"], services=["reference"], modes=["reference"], notes=["A service extension is not a new general settlement permission; do not collapse decision rows."])
    add("future-rts-dates", "Commission adopted text: differentiated future application stages",
        [part("591deafae0a9", article=2, end="Done at Brussels", locator="C(2026)4640 final, Article 2")],
        ["future_rts_dates"], ["EU"], services=["regulatory"], modes=["future"], notes=["Commission text dated 6 July 2026; OJ publication/entry into force not independently verified. Do not present the whole amendment as currently operative.", "Article 1 amendment points retain their distinct December 2026, July 2027 and October 2027 dates; operative details need those points and dependencies."])


def configure():
    T, M, EU = "aa3d5a3b94c9", "8719262f5e8b", "02014R0909-20260117"
    tcsds = ["T2S", "Milan", "Copenhagen", "Porto"]
    add("t2s-matching", "Matching rules and repaired functional field diagrams", [
        part(T, [267,268,269,270,271], "1.6.1.2 Matching", "1.6.1.3 Allegement", locator="§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194"),
        part(T, path="implementation/2026-09-13/structured/t2s-matching-fields.json", locator="Visually checked Diagrams 55–57; original PDF 269–271")],
        ["matching_concept", "matching_fields", "realignment_mechanism"], tcsds,
        notes=["Functional matrix only; no production XML/XSD validation or local interface certification.", "Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD."], effective="2026-06-14")
    add("t2s-posting", "Posting checks eligibility and resources before transfer", [part(T, [303,304], "1.6.1.8 Posting", "They can be submitted", locator="§1.6.1.8.1 and first overview paragraph; PDF 303–304")],
        ["matching_concept", "realignment_mechanism", "cross_csd_message_flow"], tcsds, effective="2026-06-14")
    add("t2s-realignment", "Realignment generation, CSD roles and all-or-none relationship", [part(T, [373,374,375,376], "1.6.1.10 Realignment", "The following example illustrates", locator="§1.6.1.10; concepts and reference-data requirements; PDF 373–376")],
        ["realignment_mechanism", "cross_csd_message_flow", "investor_csd_definition"], tcsds,
        deps=["t2s-posting"], notes=["Actual links/accounts and ISIN eligibility require verification.", "Does not establish atomicity of an arbitrary two-security swap or describe every action outside T2S."], effective="2026-06-14")
    add("t2s-messages", "Native message families and realignment notification", [part(T,[753],"This analysis may result",locator="§2.3 realignment dialogue; PDF 753"),part(T,[778],locator="§2.3.8 inbound/outbound messages; PDF 778")],
        ["native_message_overview", "cross_csd_message_flow"], tcsds, required=["release"], deps=["t2s-realignment"],
        notes=["T2S-native messages, not bank-to-local-CSD formats; subscriptions and privileges affect recipients.", "No production payload or full schema admitted."], effective="2026-06-14")
    add("t2s-schedule", "Baseline day phases and preceding-day/event dependencies", [part(T,[156,157,158],"1.4.2 T2S schedule","1.4.3 Overview",locator="§1.4.2 and exception conditions; PDF 156–158"),part(T,[160,161,162,163],end="1.4.4 Detailed description",locator="Table 37; PDF 160–163"),part(T,[163],"1.4.4.1 Start of day","1.4.4.1.1",locator="§1.4.4.1; PDF 163")],
        ["t2s_baseline_schedule", "business_day_timeline", "dated_t2s_schedule"], ["T2S"],
        notes=["CET is the source convention; no UTC conversion.", "Nominal schedule is not guaranteed execution or a local participant cut-off.", "Dated queries require an event overlay."], effective="2026-06-14")
    add("t2s-events-sep08", "8 September announced schedule and actual incident updates", [part("ecb-status-2026",path="implementation/2026-09-13/structured/t2s-events.json",locator="8 September 2026 updates: 15:30,18:10,18:55 and same-day status notices")],
        ["dated_t2s_schedule"], ["T2S"], required=["business_date","currency"], deps=["t2s-schedule"],
        notes=["Reviewed business date 2026-09-08 only. IDVP 17:00 was announced; actual IDVP completion is not established.", "18:55 resolves the ICBO incident and reports IFOP closure at 18:39; it does not erase the earlier IDVP exception."])
    add("milan-access", "Published securities-account, cash-agent and DCP access requirements", [part(M,[44,45],"Article 60","Article 62",locator="Articles 60–61; PDF 44–45, printed 43–44",auth="it")],
        ["settlement_access","dcp_admission"],["Milan"], notes=["Italian text prevails. Complete CLIMP onboarding, entitlements and accepted tests remain unverified."], effective="2026-01-26")
    add("milan-finality", "Matching, cancellation, hold and SF1/SF2/SF3", [part(M,[50,51],"Article 69","4. In the event of an obvious technical error",locator="Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50",auth="it")],
        ["matching_concept","cancellation_rules","finality"],["Milan"],notes=["SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.","No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted."],effective="2026-01-26")
    for n,topic,title in [(5,"settlement_cycle","Settlement-cycle ceiling and exceptions"),(37,"reconciliation_duties","Issue-integrity and daily reconciliation duties"),(38,"segregation_duties","CSD/participant segregation duties and national-law qualification"),(41,"default_governance","Default-rule and testing duties")]:
        add(f"csdr-{n}",title,[part(EU,article=n,locator=f"CSDR Article {n}; consolidation 17 January 2026",auth="EU official languages")],[topic],["EU"],services=["regulatory"],notes=["Legal context, not local procedures or Norway incorporation. Future amendments remain separate."],effective="2026-01-17")
    add("dora-scope","DORA CSD scope and application date in English",[part("dora-english-oj",article=2,locator="Regulation 2022/2554 Article 2, including exclusions",auth="EU official languages"),part("dora-english-oj",article=64,end="Done at Strasbourg",locator="Article 64",auth="EU official languages")],
        ["dora_scope"],["EU"],services=["regulatory"],roles=["csd_operator"],notes=["English OJ replacement for reviewed provisions only; no complete incident-reporting chain."],effective="2025-01-17")
    add("t1-law","Adopted T+1 amendment with future application",[part("32025R2075",article=1,locator="Regulation 2025/2075 Article 1"),part("32025R2075",article=2,end="Done at Strasbourg",locator="Article 2")],
        ["future_t1"],["EU"],services=["regulatory"],modes=["future"],notes=["Adopted law; future application on 11 October 2027. Never auto-promote by date."])
    add("november-release","November draft status and publication target",[part("7244cf50f753",[1,2],locator="R2026.NOV market-review cover note; PDF 1–2"),part("ecb-sdd-hub",start="3 August 2026T2S Draft",end="22 January 2026T2S Data Migration",locator="Live SDD hub release listings, 13 September 2026")],
        ["release_status"],["T2S"],modes=["reference","future"],notes=["Publication target is not proof of final publication or deployment. Current hub lists market-review drafts."])
    add("copenhagen-dcp","DCP certification and continuing participation agreement",[part("a7e4ccfb2933",[2,3],"1. Scope","4. Instructions from the Eurosystem",locator="Part 5 §§1–3; PDF 2–3")],
        ["dcp_admission"],["Copenhagen"],notes=["Published requirements; exact User Guidelines and accepted service tests are unverified."])
    add("copenhagen-day","VP versus T2S business-day boundaries",[part("3d76a327339b",[3],locator="Part 4 §§1–2.2.6; PDF 3")],["business_day_timeline"],["Copenhagen"],notes=["Retain currency and technical-delay qualifications; not the full operational timetable."],effective="2025-05-01")
    add("oslo-edition","VPO edition approval qualification",[part("14dc34b8e54e",[1],locator="VPO NOK Rules cover, 2 September 2024")],["approval_status"],["Oslo"],modes=["reference"],notes=["System approval is not edition-specific approval. Independent edition approval remains unresolved."])
    add("athens-edition","Athens edition versus amendment evidence",[part("d89c56df8c5a",[2],locator="English master amendment history; PDF 2"),part("athens-greek-master",[2],locator="Greek master amendment history; PDF 2",lang="el",auth="el")],["document_identity"],["Athens"],modes=["reference"],notes=["Probable edition/amendment label mismatch is an inference. Independent HCMC/Gazette chain remains incomplete."])
    add("porto-calendar","2026 calendar and May 1 FoP exception",[part("porto-calendar-notice",start="NOTICE N.º 1162/25",end="Euronext Securities Porto, 17th November, 2025",locator="Notice 25/1162, dated 17 November 2025; 2026 calendar")],["porto_calendar"],["Porto"],required=["business_date","payment_type"],notes=["English public notice. Portuguese legal text governs contested wording. No universal May 1 opening for every service/currency."],effective="2026-01-01")
    add("porto-timetable","Porto timetable notice and source clock convention",[part("porto-timetable-notice",[1,2,3],locator="Notice 394/2024 §§1–15; effective 17 April 2024",auth="pt")],["timetable_document_scope"],["Porto"],modes=["reference"],notes=["English translation expressly not legally binding. Preserve source clock values; conversion and dated exceptions are not certified."])
    add("interbolsa-identity","GLEIF LEI and preserved malformed ESMA cell",[part("gleif-interbolsa",path="implementation/2026-09-13/structured/interbolsa-identity.json",locator="GLEIF lei/legalName/registration JSON fields; ESMA C25 separately")],["entity_identity"],["Porto"],services=["reference"],modes=["reference"])
    add("offering-workbook-scope","European Offering workbook scope and future columns",[part("ac385b0f3106",path="implementation/2026-09-13/structured/european-offering-scope.json",locator="Introduction B5:B8 and full Introduction; 11 September workbook")],["isin_scope"],["Milan"],services=["reference"],modes=["reference","future"],notes=["Not universal Milan eligibility; no row grants per-ISIN operational permission."])
    add("porto-report-families","Published Porto daily reconciliation report families",[part("089b7aaef991",[66],locator="Operational Manual §7.1; PDF 66, printed 65",auth="pt"),part("04b490f176fe",[3],locator="ISO15022 v9 reconciliation-message overview; PDF 3")],["reconciliation_reports"],["Porto"],modes=["reference"],notes=["Manual effective date unresolved. Exact fields and subscriptions need their current specifications.","Manual prints semt.07; preserve anomaly rather than silently expanding it into a production identifier."])
    add_followups()
    SOURCES[T].update(document_version="R2026.JUN",platform_release="R2026.JUN",publication_date="2026-01-22",deployment_date="2026-06-14")
    SOURCES[M].update(document_version="26 January 2026",effective_from="2026-01-26",authoritative_language="it")
    SOURCES["dora-english-oj"].update(document_version="OJ Regulation (EU) 2022/2554",effective_from="2025-01-17")
    quarantines = json.loads((A/"RETRIEVAL-PROPOSAL.json").read_text())["quarantined_claims"]
    quarantines = [q for q in quarantines if q != "complete matching-field matrix from text-only UDFS PDF269"]
    quarantines.append("Production XML/XSD claims unsupported by repaired functional matching diagrams")
    config = {"schema_version":1,"as_of":"2026-09-13","whole_document_admission":False,"default_policy":"deny","sections":SECTIONS,"quarantines":quarantines,
              "excluded_categories":["whole documents","unreviewed clauses","marketing as operating authority","generated explanations as primary evidence","unparsed schema fields","historical disclosures as current procedures"]}
    for name, data in [("section-decisions.json",config),("source-register.json",SOURCES)]:
        target=R/"retrieval"/name
        if target.exists():
            raise RuntimeError(f"Refusing to replace reviewed configuration: {target}")
        target.parent.mkdir(exist_ok=True)
        target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print(f"{len(SECTIONS)} sections; {len(SOURCES)} pinned source identities")


if __name__ == "__main__":
    configure()
