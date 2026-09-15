#!/usr/bin/env python3
"""Settlement Expert Agent — enforced-retrieval pipeline over the reviewed CSD/T2S evidence library.

Layers
  1. topics    : build topic-index.json from the reviewed sections (what can be asked, with which context).
  2. route     : natural-language question -> explicit retrieval contexts (deterministic router, or a model router).
  3. retrieve  : run every context through scripts/retrieve_evidence.py (all controls enforced there), return a bundle.
  4. compose   : produce the answer with a model runtime (cli = Claude Code CLI headless, api = Anthropic Messages API)
                 or a prompt package for a manual/agent runtime.
  5. check     : deterministic checks of an answer against its bundle (citations, qualifications, blocks, unsupported detail).
  6. ask       : route -> retrieve -> compose -> check, saving a full trace.

Nothing here widens the evidence: the model only ever sees excerpts returned by the retriever, and every answer is checked
against that bundle. See RETRIEVAL-CONTRACT.md and SYSTEM-PROMPT.md.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "scripts"))
from retrieve_evidence import BLOCKED, EvidenceLibrary  # noqa: E402

SYSTEM_PROMPT = HERE / "SYSTEM-PROMPT.md"
TOPIC_INDEX = HERE / "topic-index.json"
TRACES = HERE / "traces"
DEFAULT_API_MODEL = "claude-fable-5-1"
CITATION = re.compile(r"\[\[([a-z0-9][a-z0-9\-]*)\]\]")


# --------------------------------------------------------------------------- topic index
def build_topic_index(lib):
    entries = []
    for s in lib.sections:
        entries.append({
            "section_id": s["id"], "title": s["title"], "question_types": s["question_types"], "entities": s["entities"],
            "services": s["services"], "roles": s["roles"], "modes": s["modes"], "verified_as_of": s["verified_as_of"],
            "required_context": s["required_context"], "dependency_ids": s["dependency_ids"],
            "effective_from": s.get("effective_from"), "effective_to": s.get("effective_to"),
            "platform_release": s.get("platform_release"), "subject_release": s.get("subject_release"),
            "schedule_model": s.get("schedule_model"), "event_scope": s.get("event_scope"), "calendar_scope": s.get("calendar_scope"),
            "applicability_basis": s.get("applicability_basis"), "limitations": s.get("limitations", []),
            "sources": sorted({c["title"] for c in s["citations"]}),
            "authoritative_languages": sorted({str(c.get("authoritative_language")) for c in s["citations"]}),
        })
    routes = {}
    for e in entries:
        for qt in e["question_types"]:
            for ent in e["entities"]:
                for mode in e["modes"]:
                    for svc in e["services"]:
                        key = f"{qt}|{ent}|{svc}|{mode}"
                        r = routes.setdefault(key, {"question_type": qt, "entity": ent, "service": svc, "mode": mode, "roles": set(), "review_dates": set(), "sections": set(), "required_context": set()})
                        r["roles"].update(e["roles"]); r["review_dates"].add(e["verified_as_of"]); r["sections"].add(e["section_id"]); r["required_context"].update(e["required_context"])
    for r in routes.values():
        for k in ["roles", "review_dates", "sections", "required_context"]:
            r[k] = sorted(r[k])
        r["latest_review_date"] = max(r["review_dates"])
    index = {"built_from_build_manifest_sha256": hashlib.sha256((ROOT / "retrieval/build-manifest.json").read_bytes()).hexdigest(),
             "knowledge_base_as_of": lib.as_of, "available_review_dates": lib.review_dates,
             "blocked_question_types": {k: {"gap_id": v[0], "reason": v[1]} for k, v in BLOCKED.items()},
             "context_vocabulary": {"entity": sorted({e for s in lib.sections for e in s["entities"]}), "service": sorted({e for s in lib.sections for e in s["services"]}),
                                    "role": sorted({e for s in lib.sections for e in s["roles"]}), "mode": ["current", "reference", "future"],
                                    "optional_fields": ["business_date", "currency", "release", "access_model", "link_model", "payment_type", "schedule_kind"],
                                    "cross_csd_message_flow_supported_only_for": {"release": "R2026.JUN", "access_model": "ICP", "currency": "EUR", "link_model": "direct-both-in-T2S"}},
             "routes": sorted(routes.values(), key=lambda r: (r["question_type"], r["entity"], r["mode"], r["service"])),
             "sections": entries}
    return index


# --------------------------------------------------------------------------- deterministic router
ENTITY_PATTERNS = [
    ("Milan", r"\bmilan\b|monte titoli|\bes-?mil\b|x-?trm|\bmt-?x\b|\bclimp\b|\brni\b|montetitoli|italian|italy"),
    ("Copenhagen", r"copenhagen|\bvp\b|vp securities|danish|denmark|\bdkk\b|fundhub"),
    ("Porto", r"\bporto\b|interbolsa|portug|lisbon|\bstd\b|\bslme\b|\bspme\b"),
    ("Athens", r"athens|athexcsd|\bdss\b|greek|greece|hellenic|athexclear|target-gr"),
    ("Oslo", r"\boslo\b|\bvps\b|\bvpo\b|norweg|norway|\bnok\b|verdipapirsentralen|finanstilsynet"),
    ("EU", r"\bcsdr\b|regulation \(eu\)|\beu law\b|directive 98/26|settlement finality directive|\bsfd\b|\bdora\b|2018/1229|2017/392|\barticle \d+ csdr|\brts\b|european law|legally"),
    ("T2S", r"\bt2s\b|target2-securities|udfs|eurosystem|\becb\b|sese\.\d{3}|realign|night-time|\bnts\b|\brts\b"),
]
TOPIC_PATTERNS = [
    # (question_type, entity restriction or None, regex)
    ("matching_concept", None, r"\bmatch(ed|ing)?\b(?!.*field)"),
    ("matching_fields", None, r"matching field|mandatory field|additional field|optional field|which fields (must|do|should) (we|i)? ?(match|populate)|fields? (must|should|need to|have to) (be )?match|tolerance"),
    ("sdr_matching_fields", "EU", r"matching field|tolerance|fields? (must|should|need to) match"),
    ("t2s_allegement_rules", None, r"allegement|alleged"),
    ("t2s_instruction_amendment", None, r"\bamend"),
    ("t2s_cancellation_process", None, r"\bcancel"),
    ("cancellation_rules", "Milan", r"\bcancel|revok"),
    ("finality", "Milan", r"final(ity)?|irrevocab|sf1|sf2|sf3|moment of entry"),
    ("t2s_hold_release_process", None, r"\bhold\b|release"),
    ("t2s_recycling_periods", None, r"recycl|automatically cancel|20 (working|business) days|60 (working|business) days"),
    ("t2s_partial_settlement", None, r"partial(ly)? settle|partial settlement|threshold"),
    ("t2s_partial_windows_and_cutoffs", None, r"partial settlement window|cut-?off|dvp cut|fop cut"),
    ("t2s_linked_instructions", None, r"\blink(ed|age|s)?\b(?!.*csd link)|\bwith\b link|pool reference|all-or-none|before/after"),
    ("t2s_conditional_settlement", None, r"\bcosd\b|conditional (securities )?(delivery|settlement)|administering part"),
    ("t2s_status_model", None, r"status(es)?|reason code|status advice"),
    ("t2s_validation_concept", None, r"validat"),
    ("realignment_mechanism", None, r"realign|omnibus|mirror account|technical issuer"),
    ("investor_csd_definition", None, r"investor csd|issuer csd"),
    ("issuer_investor_csd_definitions", "EU", r"investor csd|issuer csd"),
    ("cross_csd_message_flow", None, r"cross-?csd.*(message|flow|sese)|message flow|which messages|dvp flow"),
    ("native_message_overview", None, r"sese\.0\d\d|native message|iso 20022 message|message families"),
    ("t2s_message_sese023_scope", None, r"sese\.023|settlement instruction message|building block"),
    ("t2s_message_sese024_usages", None, r"sese\.024|status advice"),
    ("t2s_baseline_schedule", None, r"schedule|timetable|business day|settlement day|start of day|end of day|\bsod\b|\beod\b|what time|when does"),
    ("business_day_timeline", None, r"business day|settlement day|t\+2|t\+1|monday|tuesday|wednesday|opens? (on|at)|calendar day"),
    ("t2s_nts_processing", None, r"night-?time|\bnts\b|sequence|cycle"),
    ("dated_t2s_schedule", None, r"\bon \d{1,2} (january|february|march|april|may|june|july|august|september|october|november|december) 2026|\b2026-\d\d-\d\d|that day|incident|delayed|postponed"),
    ("settlement_access", "Milan", r"access|join|become a participant|prerequisite|admission|requirements? (for|to) participat"),
    ("dcp_admission", None, r"\bdcp\b|directly connected|certificate"),
    ("milan_settlement_scope_and_participants", "Milan", r"categor(y|ies) of participant|indirect participant|power of attorney|\bpoa\b|who can (be|become) a participant"),
    ("milan_agent_bank_and_penalties", "Milan", r"agent bank|penalt|systematically failing|suspension"),
    ("milan_instruments_notices_urd", "Milan", r"admitted (to|for) settlement|financial instruments admitted|service (information )?notice|user requirements document|\burd\b|conduct"),
    ("milan_instruction_processing_rules", "Milan", r"acquisition|priority|collateral|processing of (the )?settlement|night-time|re-?proposed|linked instruction"),
    ("milan_cross_csd_rule", "Milan", r"cross-?csd|issuer csd is outside|investor csd"),
    ("milan_connectivity_and_static_data", "Milan", r"static data|\blei\b|climp|indirect participant|\bdca\b|connectivity model|icp|dcp|operating conditions|urgent request"),
    ("milan_settlement_service_scope", "Milan", r"intra-?csd|cross-?csd|scope of the settlement service"),
    ("milan_market_claims_transformations", "Milan", r"market claim|transformation|corporate action on flow|\bcaof\b|record date|opt-?out|buyer protection|\bclai\b|\btran\b"),
    ("milan_penalty_procedure_auto_cancellation", "Milan", r"penalt|automatic(ally)? cancel|appeal"),
    ("milan_external_settlement", "Milan", r"external settlement|foreign settlement|outside t2s|pre-?positioning|pre-?funding"),
    ("milan_xtrm_service_access", "Milan", r"x-?trm|access method|\brni\b|swift|fileact|mt-?x"),
    ("milan_xtrm_field_mapping", "Milan", r"x-?trm field|which fields|field mapping|t2s field|mandatory|additional|optional"),
    ("milan_xtrm_lifecycle_maintenance", "Milan", r"x-?trm|enrichment|valoris|doubling|routing|hold|release|maintenance|modif"),
    ("milan_default_procedure", "Milan", r"default|insolven|\btoi\b|\btoa\b"),
    ("milan_cross_csd_link_guide", "Milan", r"gateway|mt23|\bssi\b|link(s)? (with|to) (other|foreign)|which csds|issuer csd chapter|external csd"),
    ("milan_party2_configuration_rule", "Milan", r"party ?2|party ?1|trading member|negoziatore|client configuration|sac t2s"),
    ("milan_t2s_release_deployment", "Milan", r"r2026\.jun|june release|deployed|production release|go-?live"),
    ("milan_t2s_release_plan_nov", "Milan", r"r2026\.nov|november release|xsd|utest"),
    ("milan_mtx_connectivity_change", "Milan", r"tls|port 8443|mt-?x access"),
    ("milan_settlement_message_field_change", "Milan", r"common reference|comm//|cmonid|repo"),
    ("milan_swift_release_2026", "Milan", r"swift (annual )?release|sr ?2026|standards release"),
    ("milan_calendar_exception", "Milan", r"1 may|may 1|1st may|labour day|holiday"),
    ("milan_participation_requirement_notification", "Milan", r"confirm(ation)? of (the )?requirements|notify (any )?changes|ongoing (participation )?requirements"),
    ("milan_mtx_payment_fields", "Milan", r"\bcab\b|account number field|t2s payer"),
    ("milan_xtrm_standard_versions", "Milan", r"standard for x-?trm users|\bspu\b|ver\.? ?01\.09|standards? for xtrm"),
    ("milan_penalties_calendar", "Milan", r"penalt(y|ies) calendar|appeal period|pfod payment date|monthly report"),
    ("milan_securities_migration_event", "Milan", r"migration|migrat"),
    ("european_offering_go_live", "Milan", r"european offering|designated (place|csd)|new settlement model|21 september"),
    ("copenhagen_settlement_routing", "Copenhagen", r"vp settlement|t2s settlement|route|which system|fundhub|dkk|sek|batch"),
    ("copenhagen_penalty_procedure", "Copenhagen", r"penalt|buy-?in|appeal|\bpbd\b"),
    ("copenhagen_vp_settlement_finality", "Copenhagen", r"batch|net settlement|moment of entry|irrevocab|final"),
    ("copenhagen_t2s_settlement", "Copenhagen", r"t2s|pre-?match|icp|dcp|auto-?collateral|final|moment of entry|insolven"),
    ("copenhagen_access_and_links", "Copenhagen", r"access|legal opinion|\blei\b|csd link|participation agreement|emergency plan"),
    ("business_day_timeline", "Copenhagen", r"business day|18:00|18:45|settlement day"),
    ("porto_instruction_registration", "Porto", r"register|registration|instruction type|\bdvp\b|\bfop\b|\bdwp\b|\bpfod\b|sf1|sf2|channel|swift|iso 15022"),
    ("porto_instruction_fields", "Porto", r"field|slrt|format|mandatory|matching|note"),
    ("porto_hold_release_amendment", "Porto", r"hold|release|amend|mt530|sese\.030"),
    ("porto_cancellation_allegement", "Porto", r"cancel|allegement|mt578|sese\.028"),
    ("porto_settlement_processing_partial", "Porto", r"partial|fail|\bpenf\b|settle(ment)? processing|priority"),
    ("porto_cross_csd_links", "Porto", r"link|cross-?csd|interlinking|registration and control account"),
    ("porto_foreign_currency_settlement", "Porto", r"foreign currency|non-?euro|\bslme\b|\bspme\b|\bcgd\b|cosd"),
    ("porto_operating_hours_published", "Porto", r"operating hours|timetable|schedule|cut-?off|\bwet\b|\bcet\b"),
    ("porto_calendar", "Porto", r"calendar|closing day|holiday|1 may|may 1"),
    ("reconciliation_reports", "Porto", r"reconcil|report|semt|mt535|mt536"),
    ("dcp_relationship", "Porto", r"\bdcp\b|direct(ly)? connected"),
    ("oslo_instruction_submission_settlement", "Oslo", r"submit|settlement group|liquidity bank|vpo lom|accounting voucher"),
    ("oslo_finality_moments", "Oslo", r"irrevocab|revoke|moment of entry|final|hold|matched|ccp"),
    ("oslo_preliminary_calculation_priority", "Oslo", r"preliminary calculation|priority|clearing|cash limit|linked"),
    ("liquidity_duties", "Oslo", r"liquidity bank|substitute"),
    ("approval_status", "Oslo", r"approv|edition|binding"),
    ("athens_settlement_methods", "Athens", r"settlement method|technical detail|dss announcement|cash blocking"),
    ("athens_market_infrastructure_settlement", "Athens", r"athexclear|settlement file|multilateral|bilateral|market infrastructure"),
    ("athens_instruction_content_matching", "Athens", r"mandatory data|operation reason|matching|tolerance|60 calendar|365"),
    ("cash_arrangements", "Athens", r"cash|target-gr|alpha bank|non-?euro"),
    ("staff_certification", "Athens", r"certif|csa"),
    ("csdr_definitions", "EU", r"defin|what is (a )?(settlement fail|dvp|delivery versus payment|csd link|participant|intended settlement date)"),
    ("participation_and_communication_law", "EU", r"participation|access|one month|iso 20022|communication standard|article 33|article 35"),
    ("finality_and_cash_settlement_law", "EU", r"finality|cash settlement|central bank money|article 39|article 40|dvp"),
    ("sfd_entry_irrevocability", "EU", r"moment of entry|irrevocab|insolvency|transfer order|directive 98/26"),
    ("sdr_settlement_facilities_information", "EU", r"hold and release|partial settlement|bilateral cancellation|allegement|status information|batches|article 7|article 8|article 10|article 11"),
    ("settlement_cycle", "EU", r"t\+2|settlement cycle|article 5"),
    ("future_t1", "EU", r"t\+1"),
    ("segregation_duties", "EU", r"segregat|omnibus"),
    ("reconciliation_duties", "EU", r"reconcil|integrity of the issue"),
    ("default_governance", "EU", r"default rule|participant default"),
    ("dora_scope", "EU", r"dora|ict|operational resilience|incident report"),
    ("release_status", "T2S", r"r2026\.nov|november release|published|final publication|draft"),
    ("november_matching_text", "T2S", r"r2026\.nov.*match|november.*match"),
    ("november_text_comparison", "T2S", r"chang(e|es|ed) (in|between) (june|november)|differ|compar|what changed"),
    ("isin_scope", "Milan", r"eligible isin|isin list|workbook"),
    ("register_decision_type", "Milan", r"esma register|authoris|stamp duty"),
    ("entity_identity", "Porto", r"\blei\b|legal name|identity"),
]
FIELD_HINTS = {
    "currency": r"\b(EUR|DKK|SEK|NOK|USD|GBP|CHF|JPY)\b",
    "release": r"\b(R20\d\d\.(?:JUN|NOV))\b",
    "business_date": r"\b(20\d\d-\d\d-\d\d)\b",
    "payment_type": r"\b(FOP|DVP|DWP|PFOD)\b",
    "access_model": r"\b(ICP|DCP)\b",
}
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"], 1)}


def detect_dates(q):
    out = set(re.findall(r"\b(20\d\d-\d\d-\d\d)\b", q))
    for d, m, y in re.findall(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(20\d\d)\b", q):
        out.add(f"{y}-{MONTHS[m.lower()]:02d}-{int(d):02d}")
    return sorted(out)


def detect_entities(q):
    ql = q.lower()
    found = [e for e, pat in ENTITY_PATTERNS if re.search(pat, ql)]
    return found or ["T2S"]


def deterministic_route(question, index, max_contexts=6):
    """Keyword router: produces candidate explicit contexts from the topic index. It never invents values that the index lacks."""
    ql = question.lower()
    entities = detect_entities(question)
    route_keys = {(r["question_type"], r["entity"], r["service"], r["mode"]): r for r in index["routes"]}
    hits = []
    for qt, ent_restr, pat in TOPIC_PATTERNS:
        if not re.search(pat, ql):
            continue
        for ent in entities:
            if ent_restr and ent != ent_restr:
                continue
            for mode in ["current", "reference", "future"]:
                for svc in ["settlement", "regulatory", "reference"]:
                    r = route_keys.get((qt, ent, svc, mode))
                    if r:
                        hits.append((qt, ent, svc, mode, r))
    blocked_hits = [qt for qt in BLOCKED if re.search(qt.replace("_", "[ _-]?"), ql)]
    wants_future = bool(re.search(r"\bfuture\b|planned|will |upcoming|november|t\+1|2027|go-?live|when will", ql))
    wants_current = not re.search(r"\bhistor|draft|reference only", ql)
    contexts, seen = [], set()
    for qt, ent, svc, mode, r in hits:
        if mode == "future" and not wants_future:
            continue
        if mode == "reference" and any(h[0] == qt and h[1] == ent and h[3] == "current" for h in hits) and wants_current:
            continue  # prefer the current-mode route when one exists
        key = (qt, ent, svc, mode)
        if key in seen:
            continue
        seen.add(key)
        ctx = {"as_of": r["latest_review_date"], "entity": ent, "service": svc, "role": "participant" if "participant" in r["roles"] else r["roles"][0], "mode": mode, "question_type": qt}
        for field, pat in FIELD_HINTS.items():
            m = re.search(pat, question)
            if m and (field in r["required_context"] or (field == "release" and qt.startswith(("t2s_message", "november", "release", "milan_t2s_release"))) or (qt == "cross_csd_message_flow" and field in ["currency", "access_model", "release"])):
                ctx[field] = m.group(1)
        if qt == "cross_csd_message_flow" and re.search(r"direct link|both (csds )?in t2s|two t2s csds|another t2s csd", ql):
            ctx["link_model"] = "direct-both-in-T2S"
            ctx.setdefault("_assumed", []).append("link_model=direct-both-in-T2S (from wording; verify the actual link)")
        dates = detect_dates(question)
        if dates and (qt in ["dated_t2s_schedule", "t2s_partial_windows_and_cutoffs", "t2s_baseline_schedule", "business_day_timeline", "t2s_nts_processing", "milan_calendar_exception", "porto_calendar"] or "business_date" in r["required_context"]):
            ctx["business_date"] = dates[0]
            if "currency" not in ctx and qt.startswith(("dated_t2s", "t2s_")):
                ctx["currency"] = "EUR"  # stated assumption; the answer layer must disclose it
                ctx["_assumed"] = ["currency=EUR"]
        if re.search(r"nominal|baseline|normal(ly)? scheduled|standard schedule", ql) and "business_date" in ctx:
            ctx["schedule_kind"] = "baseline"
        contexts.append(ctx)
    for qt in blocked_hits:
        contexts.append({"as_of": index["knowledge_base_as_of"], "entity": entities[0], "service": "settlement", "role": "participant", "mode": "current", "question_type": qt, "_note": "explicitly blocked topic"})
    if re.search(r"swap|exchange (of )?(two|2) securities|security-for-security|securities-for-securities|atomic", ql):
        contexts.append({"as_of": index["knowledge_base_as_of"], "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "securities_swap_atomicity"})
        if not any(c["question_type"] == "realignment_mechanism" for c in contexts):
            contexts.append({"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "realignment_mechanism", "_note": "narrower supported mechanism (all-or-none realignment chain) retrieved alongside the blocked swap topic"})
        if not any(c["question_type"] == "t2s_linked_instructions" for c in contexts):
            contexts.append({"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_linked_instructions", "_note": "actor-specified WITH links are the closest supported construct"})
    return contexts[:max_contexts], {"entities": entities, "topic_hits": sorted({h[0] for h in hits}), "blocked_hits": blocked_hits, "dates": detect_dates(question)}


# --------------------------------------------------------------------------- retrieval bundle
def retrieve_bundle(lib, contexts):
    results = []
    for ctx in contexts:
        clean = {k: v for k, v in ctx.items() if not k.startswith("_")}
        r = lib.retrieve(clean)
        results.append({"context": clean, "router_notes": {k: v for k, v in ctx.items() if k.startswith("_")}, "status": r["status"], "reason": r["reason"],
                        "knowledge_as_of": r.get("knowledge_as_of"), "schedule_kind": r.get("schedule_kind"), "missing_fields": r.get("missing_fields"),
                        "gap_ids": r.get("gap_ids"), "topic_review_dates": r.get("topic_review_dates"),
                        "evidence": [{"id": s["id"], "title": s["title"], "verified_as_of": s["verified_as_of"], "modes": s["modes"], "entities": s["entities"],
                                      "applicability_basis": s.get("applicability_basis"), "publication_status": s.get("publication_status"),
                                      "subject_release": s.get("subject_release"), "platform_release": s.get("platform_release"),
                                      "limitations": s["limitations"], "citations": s["citations"],
                                      "evidence": s["evidence"]} for s in r["evidence"]]})
    return {"generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "build_manifest_sha256": hashlib.sha256((ROOT / "retrieval/build-manifest.json").read_bytes()).hexdigest(),
            "knowledge_base_as_of": lib.as_of, "available_review_dates": lib.review_dates, "results": results}


def bundle_for_prompt(bundle, max_chars=160000):
    """Render the bundle as the only evidence the model may use. Excerpts are quoted verbatim with their metadata."""
    out = [f"EVIDENCE BUNDLE (retriever build {bundle['build_manifest_sha256'][:12]}, generated {bundle['generated_at_utc']}). Review dates available: {', '.join(bundle['available_review_dates'])}."]
    for i, r in enumerate(bundle["results"], 1):
        out.append(f"\n=== RETRIEVAL {i}: context {json.dumps(r['context'])}\nSTATUS: {r['status']} — {r['reason']}")
        if r.get("missing_fields"):
            out.append(f"MISSING CONTEXT FIELDS: {r['missing_fields']}")
        if r.get("gap_ids"):
            out.append(f"GAP IDS: {r['gap_ids']}")
        if r.get("topic_review_dates"):
            out.append(f"TOPIC REVIEW DATES AVAILABLE: {r['topic_review_dates']}")
        if r.get("schedule_kind"):
            out.append(f"SCHEDULE KIND: {r['schedule_kind']}")
        if r.get("router_notes"):
            out.append(f"ROUTER NOTES: {json.dumps(r['router_notes'])}")
        for s in r["evidence"]:
            out.append(f"\n--- SECTION [[{s['id']}]] — {s['title']} (reviewed {s['verified_as_of']}; modes {s['modes']}; entities {s['entities']}; basis {s['applicability_basis']}"
                       + (f"; subject release {s['subject_release']}" if s.get('subject_release') else "") + (f"; platform release {s['platform_release']}" if s.get('platform_release') else "") + ")")
            for c in s["citations"]:
                out.append(f"CITATION: {c['title']} | {c['locator']} | version {c.get('document_version')} | body language {c['body_language']} | authoritative language {c.get('authoritative_language')} | {c.get('translation_status')} | approval: {c.get('approval_status')} | source reviewed {c['source_verified_as_of']} | url {c['source_url']}")
            for lim in s["limitations"]:
                out.append(f"LIMITATION: {lim}")
            for e in s["evidence"]:
                out.append(f"EXCERPT ({e['locator']}):\n{e['text']}")
    text = "\n".join(out)
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n[BUNDLE TRUNCATED AT {max_chars} CHARACTERS — say so in the answer and do not infer omitted content]"
    return text


# --------------------------------------------------------------------------- model runtimes
def run_cli(system_prompt, user_prompt, model=None, timeout=600):
    cmd = ["claude", "-p", user_prompt, "--system-prompt", system_prompt, "--output-format", "json", "--tools", "", "--no-session-persistence"]
    if model:
        cmd += ["--model", model]
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDECODE") and k not in ("CLAUDE_CODE_ENTRYPOINT",)}
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"claude CLI failed (rc={proc.returncode}): {proc.stderr[:800]}")
    data = json.loads(proc.stdout)
    return data.get("result") or data.get("content") or proc.stdout, {"runtime": "cli", "model": model or "cli-default", "raw": {k: data.get(k) for k in ["model", "usage", "total_cost_usd", "session_id", "is_error"]}}


def run_api(system_prompt, user_prompt, model=None, timeout=600):
    import requests  # local dependency already present in this environment
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")
    body = {"model": model or DEFAULT_API_MODEL, "max_tokens": 8000, "system": system_prompt, "messages": [{"role": "user", "content": user_prompt}]}
    resp = requests.post("https://api.anthropic.com/v1/messages", headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}, json=body, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    text = "".join(block.get("text", "") for block in data.get("content", []))
    return text, {"runtime": "api", "model": data.get("model"), "raw": {"usage": data.get("usage"), "stop_reason": data.get("stop_reason"), "id": data.get("id")}}


# --------------------------------------------------------------------------- deterministic answer checks
def check_answer(answer, bundle, question=""):
    """Checks that do not need a model. They catch citation drift, dropped qualifications, hidden blocks and unsupported detail.
    They cannot judge semantic faithfulness; that is the judge's job (see evaluation/RUBRIC.md)."""
    retrieved = {s["id"]: s for r in bundle["results"] for s in r["evidence"]}
    evidence_text = "\n".join(e["text"] for s in retrieved.values() for e in s["evidence"])
    meta_text = json.dumps(bundle, ensure_ascii=False)
    cited = CITATION.findall(answer)
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "outcome": "PASS" if ok else "FAIL", "detail": detail})

    unknown = sorted({c for c in cited if c not in retrieved})
    add("all_citations_in_bundle", not unknown, f"unknown citations: {unknown}")
    add("has_citation_when_evidence_present", (not retrieved) or bool(cited), "evidence retrieved but no [[section-id]] citation")
    non_ok = [r for r in bundle["results"] if r["status"] != "evidence_only"]
    if non_ok:
        statuses = {r["status"] for r in non_ok}
        words = {"blocked": r"\bblock|not (in|within) (the )?reviewed|cannot (be )?(support|answer|establish)|no reviewed|unsupported|not admitted|gap\b", "needs_context": r"clarif|need(s|ed)? (more|the|to know)|please specify|which|depends on|assum", "needs_refresh": r"refresh|revalidat|not (been )?reviewed for|review date|snapshot|as of"}
        for st in statuses:
            add(f"discloses_{st}", bool(re.search(words[st], answer, re.I)), f"a retrieval returned {st} but the answer does not disclose it")
    # qualifications that must survive
    auth_langs = {c.get("authoritative_language") for s in retrieved.values() for c in s["citations"] if c.get("authoritative_language") and c.get("authoritative_language") != c.get("body_language") and c.get("authoritative_language") != "EU official languages"}
    lang_names = {"it": r"italian", "el": r"greek", "no": r"norwegian", "pt": r"portuguese", "de": r"german", "fr": r"french"}
    for lang in auth_langs:
        add(f"authoritative_language_{lang}_disclosed", bool(re.search(lang_names.get(lang, lang), answer, re.I)), "translation used but governing language not mentioned")
    if any(s.get("applicability_basis") == "publication_description" for s in retrieved.values()):
        add("publication_description_qualified", bool(re.search(r"publish|published|publication|operative|effective date|not (been )?establish", answer, re.I)))
    if any(s.get("subject_release") == "R2026.NOV" or s.get("publication_status") for s in retrieved.values()):
        add("november_not_treated_as_deployed", not re.search(r"(R2026\.NOV|November release)[^.]{0,80}\b(is|was|has been) (deployed|live|in production)\b(?![^.]{0,40}\b(not|plan))", answer, re.I))
    review_dates = {s["verified_as_of"] for s in retrieved.values()}
    add("review_date_stated", (not retrieved) or any(d in answer or dt.date.fromisoformat(d).strftime("%-d %B %Y") in answer for d in review_dates), f"none of {sorted(review_dates)} stated")
    # unsupported detail heuristics: clock times, message versions, XML, amounts not present in evidence/question/metadata
    allowed = (evidence_text + "\n" + meta_text + "\n" + question)
    times = sorted({t for t in re.findall(r"\b(\d{1,2}:\d{2})\b", answer) if t not in allowed})
    add("no_unsupported_clock_times", not times, f"times absent from evidence: {times}")
    versions = sorted({v for v in re.findall(r"\b((?:sese|semt|camt|seev|reda|admi|head)\.\d{3}\.\d{3}\.\d{2})\b", answer) if v not in allowed})
    add("no_unsupported_message_versions", not versions, f"versions absent from evidence: {versions}")
    add("no_fabricated_xml", not re.search(r"<(Document|SctiesSttlmTxInstr|TxId|SttlmTpAndAddtlParams|TradDtls|FinInstrmId|QtyAndAcctDtls|SttlmParams|Rcvg|Dlvrg|Amt|DlvrgSttlmPties|RcvgSttlmPties)\b", answer))
    amounts = sorted({a for a in re.findall(r"\bEUR\s?[\d.,]+\b", answer) if a.replace("EUR ", "EUR").replace(" ", "") not in allowed.replace(" ", "") and a not in allowed})
    add("no_unsupported_eur_amounts", not amounts, f"amounts absent from evidence: {amounts}")
    add("labels_distinguished", (not retrieved) or bool(re.search(r"documented requirement|reasoned inference|proposed design|unresolved requirement|inference|not established|assumption", answer, re.I)), "no explicit distinction between documented, inferred, proposed and unresolved content")
    summary = {"checks": len(checks), "passed": sum(c["outcome"] == "PASS" for c in checks), "failed": [c["check"] for c in checks if c["outcome"] != "PASS"],
               "cited_sections": sorted(set(cited)), "retrieved_sections": sorted(retrieved), "uncited_retrieved": sorted(set(retrieved) - set(cited))}
    return {"summary": summary, "checks": checks}


# --------------------------------------------------------------------------- commands
def build_user_prompt(question, bundle, spec_requested):
    header = ("QUESTION FROM THE USER:\n" + question.strip() + "\n\n" +
              ("The user asks for a specification: use SPECIFICATION-TEMPLATE.md headings and expose every missing production field explicitly.\n\n" if spec_requested else "") +
              "Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. "
              "Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.\n\n")
    return header + bundle_for_prompt(bundle)


def cmd_topics(args):
    lib = EvidenceLibrary()
    index = build_topic_index(lib)
    TOPIC_INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"routes": len(index["routes"]), "sections": len(index["sections"]), "blocked_topics": len(index["blocked_question_types"]), "written": str(TOPIC_INDEX.relative_to(ROOT))}))


def load_index():
    if not TOPIC_INDEX.exists():
        cmd_topics(None)
    return json.loads(TOPIC_INDEX.read_text())


def cmd_route(args):
    index = load_index()
    contexts, notes = deterministic_route(args.question, index)
    print(json.dumps({"question": args.question, "contexts": contexts, "router": "deterministic-keyword", "notes": notes}, ensure_ascii=False, indent=2))


def cmd_retrieve(args):
    lib = EvidenceLibrary()
    contexts = json.loads(args.contexts) if args.contexts else json.loads(Path(args.contexts_file).read_text())
    bundle = retrieve_bundle(lib, contexts)
    if args.out:
        Path(args.out).write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
    if args.prompt:
        print(bundle_for_prompt(bundle))
    else:
        print(json.dumps({"statuses": [r["status"] for r in bundle["results"]], "sections": sorted({s["id"] for r in bundle["results"] for s in r["evidence"]}), "out": args.out}, indent=2))


def cmd_check(args):
    answer = Path(args.answer).read_text()
    bundle = json.loads(Path(args.bundle).read_text())
    report = check_answer(answer, bundle, args.question or "")
    if args.out:
        Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2))


def cmd_ask(args):
    lib = EvidenceLibrary()
    index = load_index()
    question = args.question
    if args.contexts:
        contexts, notes = json.loads(args.contexts), {"router": "caller-supplied"}
    else:
        contexts, notes = deterministic_route(question, index)
    bundle = retrieve_bundle(lib, contexts)
    spec = bool(re.search(r"specif|spec\b|technical design|functional design|acceptance criteria", question, re.I))
    system_prompt = SYSTEM_PROMPT.read_text()
    user_prompt = build_user_prompt(question, bundle, spec)
    TRACES.mkdir(exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    trace_dir = TRACES / f"{stamp}-{hashlib.sha256(question.encode()).hexdigest()[:8]}"
    trace_dir.mkdir()
    (trace_dir / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
    (trace_dir / "prompt.system.md").write_text(system_prompt)
    (trace_dir / "prompt.user.md").write_text(user_prompt)
    trace = {"question": question, "contexts": contexts, "router_notes": notes, "runtime": args.runtime, "model": args.model,
             "statuses": [r["status"] for r in bundle["results"]], "retrieved_sections": sorted({s["id"] for r in bundle["results"] for s in r["evidence"]}),
             "build_manifest_sha256": bundle["build_manifest_sha256"], "started_utc": stamp}
    if args.runtime == "manual":
        trace["answer"] = None
        trace["instructions"] = ("Manual/agent runtime: compose the answer from prompt.user.md under prompt.system.md, save it as answer.md in this folder, "
                                 "then run: settlement_agent.py check --answer answer.md --bundle bundle.json --question '...' --out checks.json")
        (trace_dir / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"trace_dir": str(trace_dir.relative_to(ROOT)), "statuses": trace["statuses"], "retrieved_sections": trace["retrieved_sections"], "next": trace["instructions"]}, indent=2))
        return
    runner = run_cli if args.runtime == "cli" else run_api
    try:
        answer, meta = runner(system_prompt, user_prompt, args.model)
    except Exception as exc:  # the runtime is an external dependency; record and stop, never fabricate an answer
        trace.update(answer=None, runtime_error=str(exc))
        (trace_dir / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"trace_dir": str(trace_dir.relative_to(ROOT)), "runtime_error": str(exc)}, indent=2))
        sys.exit(2)
    (trace_dir / "answer.md").write_text(answer)
    report = check_answer(answer, bundle, question)
    (trace_dir / "checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    trace.update(answer_path="answer.md", runtime_meta=meta, checks=report["summary"])
    (trace_dir / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n")
    print(answer)
    print("\n---\nCHECKS: " + json.dumps(report["summary"]))
    print("TRACE: " + str(trace_dir.relative_to(ROOT)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("topics", help="rebuild topic-index.json from the current reviewed build").set_defaults(fn=cmd_topics)
    p = sub.add_parser("route", help="deterministic routing of a question to explicit contexts"); p.add_argument("question"); p.set_defaults(fn=cmd_route)
    p = sub.add_parser("retrieve", help="run explicit contexts through the enforced retriever"); p.add_argument("--contexts"); p.add_argument("--contexts-file"); p.add_argument("--out"); p.add_argument("--prompt", action="store_true", help="print the evidence bundle as prompt text"); p.set_defaults(fn=cmd_retrieve)
    p = sub.add_parser("check", help="deterministic checks of an answer against its bundle"); p.add_argument("--answer", required=True); p.add_argument("--bundle", required=True); p.add_argument("--question"); p.add_argument("--out"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("ask", help="route, retrieve, compose and check"); p.add_argument("question"); p.add_argument("--runtime", choices=["cli", "api", "manual"], default="manual"); p.add_argument("--model"); p.add_argument("--contexts", help="JSON list of explicit contexts to use instead of the router"); p.set_defaults(fn=cmd_ask)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
