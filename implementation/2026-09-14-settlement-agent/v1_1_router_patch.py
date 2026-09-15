"""Router revision v1.1 for settlement-expert-agent/settlement_agent.py (apply after evaluation run 2026-09-14-r1 is frozen).

Findings from run r1 (prepared-route hit rate 29/46; responders corrected routing in 23 cases; four prepared bundles were
empty: E18, E29, E41, E42): missing keyword patterns for Athens, Oslo, Copenhagen, Porto and EU routes; blocked topics only
matched their literal names; T2S-generic topics were dropped when the question named a CSD but no T2S entity; dated status
entries were unreachable when the nominal schedule blocked; future dates blocked both schedule routes; no default release for
message routes when the deployed release was evidently meant. Guarded: applies once.
"""
from pathlib import Path
ROOT = Path("/Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base")
P = ROOT / "settlement-expert-agent/settlement_agent.py"
s = P.read_text()
if "ROUTER_REVISION = \"v1.1\"" in s:
    raise SystemExit("router v1.1 already applied")

# 1. extra topic patterns (appended to TOPIC_PATTERNS) -----------------------------------------------------------------
old_tail = '''    ("entity_identity", "Porto", r"\\blei\\b|legal name|identity"),
]
'''
new_tail = '''    ("entity_identity", "Porto", r"\\blei\\b|legal name|identity"),
    # --- revision v1.1 (14 September 2026): patterns added after evaluation run 2026-09-14-r1 ---
    ("t2s_status_history", "T2S", r"unusual|incident|disrupt|outage|delay|operating normally|anything happen|status (entr|notice|histor)|went wrong|as normal"),
    ("t2s_recycling_periods", None, r"how long|how many (working |business )?days|before (it is|being|they are) (automatically )?cancel|keeps? an? (unmatched|matched)|survive|remain in t2s"),
    ("cross_csd_message_flow", None, r"(another|other|different) (t2s )?csd.*(flow|message|timing|settle)|between .* (two|2)? ?csds\\b|seller.*buyer.*csd"),
    ("realignment_mechanism", None, r"(another|other|different) (t2s )?csd|cross-?csd"),
    ("native_message_overview", None, r"which messages|messages? (exchanged|involved|used)|message (list|table)|settlement flow, messages"),
    ("t2s_message_sese023_scope", None, r"settlement instruction (message|fields)|which fields.*(send|instruction)|xml element|cardinalit"),
    ("release_status", "T2S", r"published|publication|release status|deployed|is .* live|go-?live|in production|r2026\\.nov"),
    ("november_text_comparison", "T2S", r"\\bchang(e|es|ed)\\b.*(section|text|udfs|rules?)|has .* changed|what (has )?changed|same as (june|before)"),
    ("milan_t2s_release_plan_nov", "Milan", r"november|r2026\\.nov|deploy(ed|ment)?"),
    ("milan_t2s_release_deployment", "Milan", r"r2026\\.jun|deployed|which release|current release|in production"),
    ("milan_xtrm_lifecycle_maintenance", "Milan", r"x-?trm.*(lifecycle|status|modif|cancel|hold|report|valid|enrich|rout)|icp.*(instruction|flow|spec)|otc.*(instruction|dvp)|what (can|may) (i|we) (modify|amend|change)|reject|acceptance message"),
    ("milan_xtrm_service_access", "Milan", r"\\bicp\\b|indirectly connected|technical specification|interface"),
    ("milan_xtrm_field_mapping", "Milan", r"\\bicp\\b|x-?trm|fields? (we|to) (must )?send|field mapping|which fields"),
    ("milan_connectivity_and_static_data", "Milan", r"\\bicp\\b|\\bdcp\\b|indirectly connected|directly connected|technical specification|onboard|set-?up|static data|account structure"),
    ("milan_cross_csd_link_guide", "Milan", r"which link|link guide|gateway|euroclear|clearstream|iberclear|counterparty csd|cross-?csd (link|settle)|settle cross-?csd"),
    ("milan_settlement_scope_and_participants", "Milan", r"who (can|may) (be|become|participate)|participat|eligible (to|for) (join|participate)|indirect participant|categor"),
    ("milan_default_procedure", "Milan", r"insolven|default(ing)? (participant|procedure)|goes bust|bankrupt"),
    ("milan_calendar_exception", "Milan", r"1 may|may 1|public holiday|bank holiday|open on|closed on|business day on"),
    ("european_offering_go_live", "Milan", r"euronext (paris|amsterdam|brussels)|european offering|designated place of settlement|new (settlement )?model|migration of|migrat"),
    ("milan_securities_migration_event", "Milan", r"migrat|transfer of securities to|european offering"),
    ("finality", "Milan", r"insolven|revok|irrevocab|final"),
    ("milan_instruction_processing_rules", "Milan", r"pending instruction|unsettled|partial(ly)? settle|priorit|swap|exchange"),
    ("copenhagen_t2s_settlement", "Copenhagen", r"t2s|irrevocab|final|match|transfer order|moment of entry|dcp"),
    ("copenhagen_settlement_routing", "Copenhagen", r"t2s|\\bvp\\b|route|which system|\\bdkk\\b|\\beur\\b|where (does|do) .* settle"),
    ("copenhagen_vp_settlement_finality", "Copenhagen", r"\\bvp\\b|pre-?match|batch|irrevocab|final|moment of entry"),
    ("copenhagen_access_and_links", "Copenhagen", r"access|participant|link|require|admission|join"),
    ("copenhagen_penalty_procedure", "Copenhagen", r"penalt|fail"),
    ("porto_cancellation_allegement", "Porto", r"cancel|allegement|cut-?off|deadline|closing"),
    ("porto_operating_hours_published", "Porto", r"cut-?off|hours|schedule|closing|timetable|open"),
    ("porto_hold_release_amendment", "Porto", r"\\bhold\\b|release|amend|modif"),
    ("porto_instruction_fields", "Porto", r"field|content|data|matching"),
    ("porto_instruction_registration", "Porto", r"regist|submit|enter|\\bstd\\b|instruction"),
    ("porto_settlement_processing_partial", "Porto", r"partial|settlement (cycle|process)|settle"),
    ("porto_cross_csd_links", "Porto", r"link|cross-?csd|foreign|realign|euroclear|clearstream|iberclear|monte titoli"),
    ("porto_foreign_currency_settlement", "Porto", r"foreign currency|non-?eur|\\busd\\b|\\bgbp\\b|currency"),
    ("porto_calendar", "Porto", r"calendar|holiday|working day|business day"),
    ("athens_instruction_content_matching", "Athens", r"data|content|fields?|include|intended settlement date|match|instruction"),
    ("athens_settlement_methods", "Athens", r"settle|cycle|cash|method|dss|block"),
    ("athens_market_infrastructure_settlement", "Athens", r"infrastructure|target-gr|payment|cash|settlement bank"),
    ("cash_arrangements", "Athens", r"cash|settlement bank|target-gr"),
    ("oslo_instruction_submission_settlement", "Oslo", r"submit|instruction|settle|netting|vpo|nok|match|tolerance"),
    ("oslo_finality_moments", "Oslo", r"revok|final|irrevocab|\\bhold\\b|entry|match"),
    ("oslo_preliminary_calculation_priority", "Oslo", r"priorit|preliminary|clearing|calculat"),
    ("approval_status", "Oslo", r"approv|edition|in force"),
    ("liquidity_duties", "Oslo", r"liquidity|cash|norges bank"),
    ("finality_and_cash_settlement_law", "EU", r"final|irrevocab|moment of entry|cash settlement|central bank money|csdr"),
    ("participation_and_communication_law", "EU", r"participat|access|communication|iso 20022|open access"),
    ("sfd_entry_irrevocability", "EU", r"moment of entry|irrevocab|transfer order|finality directive|\\bsfd\\b|legally"),
    ("csdr_definitions", "EU", r"defin|what is a|meaning of|csdr"),
    ("settlement_cycle", "EU", r"t\\+2|t\\+1|settlement cycle|intended settlement date|article 5"),
    ("sdr_settlement_facilities_information", "EU", r"facilit|information|penalt|fail"),
    ("issuer_investor_csd_definitions", "EU", r"investor csd|issuer csd|both at the same time|in relation to a securities issue"),
]
'''
assert old_tail in s, "TOPIC_PATTERNS tail not found"
s = s.replace(old_tail, new_tail, 1)

# 2. blocked-topic keyword patterns + Paris alias -------------------------------------------------------------------------
old_fh = '''FIELD_HINTS = {'''
new_fh = '''ROUTER_REVISION = "v1.1"
# Keyword triggers for controlled blocks (revision v1.1). The literal topic-name match is kept as well.
BLOCKED_PATTERNS = {
    "milan_participant_cutoff": ("Milan", r"cut-?off|deadline|latest time|by when|timetable|night-?time settlement (starts?|begins?)|19:30|same-day"),
    "milan_xtrm_message_layout": ("Milan", r"layout|record (format|structure)|\\bg5\\d\\b|mt5\\d\\d (layout|format|structure)|field (list|layout)|message (layout|format|specification)"),
    "production_xtrm_fields": ("Milan", r"production (x-?trm|field|payload)"),
    "instrument_eligibility": (None, r"\\bisin\\s+[a-z]{2}[a-z0-9]{9}\\d\\b|can isin|is (this|the) isin|eligible (isin|instrument|security)|settle cross-?csd today|through which link|which link applies"),
    "fee_amount": (None, r"\\bfees?\\b|tariff|price ?list|how much (does|will) .* cost|\\bcharges?\\b"),
    "copenhagen_dcp_entitlements": ("Copenhagen", r"test case|user guideline|entitlement|go(ing)? live as a dcp|certification test|before going live"),
    "oslo_operational_calendar": ("Oslo", r"calendar|cycle time|opening hours|cut-?off|deadline"),
    "athens_dss_technical_cycles": ("Athens", r"cycle|cut-?off|dss (time|announce|technical)|settlement (window|time)"),
    "athens_production_interface": ("Athens", r"interface|message format|file format"),
    "athens_tax_deadline": ("Athens", r"\\btax"),
    "porto_std_file_layout": ("Porto", r"std (file|layout|record)|appendix a1|file layout|record layout"),
    "mystandards_usage_rules": (None, r"\\bxsd|cardinalit|xml element|mystandards|schema|usage guideline"),
    "production_matching_fields": (None, r"production (xml|schema|matching)"),
    "november_operational_provisions": (None, r"(r2026\\.nov|november release).*(provision|rule|behaviou?r|how does|what does|what will)"),
    "unconditional_oslo_approval": ("Oslo", r"approv"),
    "incident_reporting_procedure": ("EU", r"incident report|report.*incident|dora"),
    "cmvm_information_duties": ("Porto", r"cmvm|information dut"),
}
FIELD_HINTS = {'''
assert old_fh in s
s = s.replace(old_fh, new_fh, 1)

old_ent = '''    ("T2S", r"\\bt2s\\b|target2-securities|udfs|eurosystem|\\becb\\b|sese\\.\\d{3}|realign|night-time|\\bnts\\b|\\brts\\b"),
]
'''
new_ent = '''    ("T2S", r"\\bt2s\\b|target2-securities|udfs|eurosystem|\\becb\\b|sese\\.\\d{3}|realign|night-time|\\bnts\\b|\\brts\\b"),
    ("Milan", r"euronext (paris|amsterdam|brussels)|european offering"),  # v1.1: the European offering evidence is a Milan notice
]
'''
assert old_ent in s
s = s.replace(old_ent, new_ent, 1)

old_de = '''    found = [e for e, pat in ENTITY_PATTERNS if re.search(pat, ql)]
    return found or ["T2S"]
'''
new_de = '''    found = []
    for e, pat in ENTITY_PATTERNS:
        if re.search(pat, ql) and e not in found:
            found.append(e)
    return found or ["T2S"]
'''
assert old_de in s
s = s.replace(old_de, new_de, 1)

# 3. replace deterministic_route wholesale ------------------------------------------------------------------------------
start = s.index("def deterministic_route(")
end = s.index("# --------------------------------------------------------------------------- retrieval bundle")
new_fn = '''def deterministic_route(question, index, max_contexts=8):
    """Keyword router (revision v1.1): produces candidate explicit contexts from the topic index. It never invents values that
    the index lacks. Assumptions it adopts are recorded under "_assumed"/"_note" so the answer layer can disclose them."""
    ql = question.lower()
    entities = detect_entities(question)
    route_keys = {(r["question_type"], r["entity"], r["service"], r["mode"]): r for r in index["routes"]}
    hits = []
    for qt, ent_restr, pat in TOPIC_PATTERNS:
        if not re.search(pat, ql):
            continue
        found_for_entity = False
        for ent in entities:
            if ent_restr and ent != ent_restr:
                continue
            for mode in ["current", "reference", "future"]:
                for svc in ["settlement", "regulatory", "reference"]:
                    r = route_keys.get((qt, ent, svc, mode))
                    if r:
                        hits.append((qt, ent, svc, mode, r, None))
                        found_for_entity = True
        # v1.1: a T2S-generic topic keeps its platform route when the question names only a CSD without that route
        if not found_for_entity and ent_restr in (None, "T2S") and "T2S" not in entities:
            for mode in ["current", "reference", "future"]:
                r = route_keys.get((qt, "T2S", "settlement", mode))
                if r:
                    hits.append((qt, "T2S", "settlement", mode, r, "T2S platform route used because no route for the named CSD covers this topic"))
    blocked_hits = [qt for qt in BLOCKED if re.search(qt.replace("_", "[ _-]?"), ql)]
    for qt, (ent_restr, pat) in BLOCKED_PATTERNS.items():
        if qt in BLOCKED and qt not in blocked_hits and re.search(pat, ql) and (ent_restr is None or ent_restr in entities):
            blocked_hits.append(qt)
    wants_future = bool(re.search(r"\\bfuture\\b|planned|will |upcoming|november|t\\+1|2027|go-?live|when will|new (settlement )?model|migration|european offering|from \\d{1,2} (january|february|march|april|may|june|july|august|september|october|november|december) 20\\d\\d", ql))
    wants_current = not re.search(r"\\bhistor|draft|reference only", ql)
    dates = detect_dates(question)
    knowledge_date = max(index["available_review_dates"])
    future_date = bool(dates) and max(dates) > knowledge_date
    names_release = bool(re.search(FIELD_HINTS["release"], question))
    contexts, seen = [], set()
    for qt, ent, svc, mode, r, note in hits:
        if mode == "future" and not wants_future:
            continue
        if mode == "reference" and any(h[0] == qt and h[1] == ent and h[3] == "current" for h in hits) and wants_current:
            continue  # prefer the current-mode route when one exists
        key = (qt, ent, svc, mode)
        if key in seen:
            continue
        seen.add(key)
        ctx = {"as_of": r["latest_review_date"], "entity": ent, "service": svc, "role": "participant" if "participant" in r["roles"] else r["roles"][0], "mode": mode, "question_type": qt}
        if note:
            ctx["_note"] = note
        for field, pat in FIELD_HINTS.items():
            m = re.search(pat, question)
            if m and (field in r["required_context"] or (field == "release" and qt.startswith(("t2s_message", "november", "release", "milan_t2s_release"))) or (qt == "cross_csd_message_flow" and field in ["currency", "access_model", "release"])):
                ctx[field] = m.group(1)
        # v1.1: the deployed release is the evident subject when no release is named and November is not mentioned
        if "release" in r["required_context"] and "release" not in ctx and not names_release and not re.search(r"november|\\bnov\\b", ql):
            ctx["release"] = "R2026.JUN"
            ctx.setdefault("_assumed", []).append("release=R2026.JUN (deployed release assumed; the answer must disclose it)")
        if qt == "cross_csd_message_flow" and re.search(r"direct link|both (csds )?in t2s|two t2s csds|another t2s csd|other t2s csd", ql):
            ctx["link_model"] = "direct-both-in-T2S"
            ctx.setdefault("_assumed", []).append("link_model=direct-both-in-T2S (from wording; verify the actual link)")
        if dates and (qt in ["dated_t2s_schedule", "t2s_status_history", "t2s_partial_windows_and_cutoffs", "t2s_baseline_schedule", "business_day_timeline", "t2s_nts_processing", "milan_calendar_exception", "porto_calendar"] or "business_date" in r["required_context"]):
            if future_date and qt in ["t2s_baseline_schedule", "business_day_timeline", "t2s_nts_processing", "t2s_partial_windows_and_cutoffs"]:
                ctx["schedule_kind"] = "baseline"
                ctx["_note"] = "future business date: nominal baseline retrieved without the date; the dated route reports the missing overlay separately"
            else:
                ctx["business_date"] = dates[0]
                if "currency" not in ctx and qt.startswith(("dated_t2s", "t2s_")):
                    ctx["currency"] = "EUR"  # stated assumption; the answer layer must disclose it
                    ctx.setdefault("_assumed", []).append("currency=EUR")
        if re.search(r"nominal|baseline|normal(ly)? scheduled|standard schedule", ql) and "business_date" in ctx:
            ctx["schedule_kind"] = "baseline"
        contexts.append(ctx)
    # v1.1: dated T2S questions also retrieve the reviewed dated status entries, so an admitted ECB entry is surfaced even
    # when the nominal schedule route blocks (for example a business date before the reviewed baseline's effective date).
    dated_ctx = next((c for c in contexts if c["question_type"] == "dated_t2s_schedule" and c.get("business_date")), None)
    status_route = route_keys.get(("t2s_status_history", "T2S", "settlement", "current"))
    if dated_ctx and status_route and not any(c["question_type"] == "t2s_status_history" for c in contexts):
        contexts.append({"as_of": status_route["latest_review_date"], "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current",
                         "question_type": "t2s_status_history", "business_date": dated_ctx["business_date"], "currency": dated_ctx.get("currency", "EUR"),
                         "_note": "dated status entries retrieved alongside the dated schedule route (v1.1)"})
    # v1.1: relative dates ("tomorrow", "today") on schedule questions produce a dated route without a date, so the retriever
    # asks for the canonical business date instead of the baseline being presented as the actual schedule.
    if not dates and re.search(r"\\btomorrow\\b|\\byesterday\\b|next (monday|tuesday|wednesday|thursday|friday|week)|later today|this (afternoon|evening)", ql) \\
            and any(c["question_type"] in ["t2s_baseline_schedule", "business_day_timeline", "t2s_nts_processing", "t2s_partial_windows_and_cutoffs"] for c in contexts) \\
            and route_keys.get(("dated_t2s_schedule", "T2S", "settlement", "current")) and not any(c["question_type"] == "dated_t2s_schedule" for c in contexts):
        contexts.append({"as_of": route_keys[("dated_t2s_schedule", "T2S", "settlement", "current")]["latest_review_date"], "entity": "T2S", "service": "settlement", "role": "participant",
                         "mode": "current", "question_type": "dated_t2s_schedule", "_note": "relative date in the question; business date and currency deliberately left for the retriever to request"})
    # v1.1: a future business date also pulls the release-status route so planned changes are disclosed
    if future_date and route_keys.get(("release_status", "T2S", "settlement", "future")) and not any(c["question_type"] == "release_status" for c in contexts):
        r = route_keys[("release_status", "T2S", "settlement", "future")]
        contexts.append({"as_of": r["latest_review_date"], "entity": "T2S", "service": "settlement", "role": "participant", "mode": "future", "question_type": "release_status", "_note": "future business date: release status retrieved for planned changes"})
    # v1.1: issuer/investor questions also carry the EU legal definitions (reference mode)
    if any(c["question_type"] == "investor_csd_definition" for c in contexts) and route_keys.get(("issuer_investor_csd_definitions", "EU", "regulatory", "reference")) \\
            and not any(c["question_type"] == "issuer_investor_csd_definitions" for c in contexts):
        r = route_keys[("issuer_investor_csd_definitions", "EU", "regulatory", "reference")]
        contexts.append({"as_of": r["latest_review_date"], "entity": "EU", "service": "regulatory", "role": "participant" if "participant" in r["roles"] else r["roles"][0], "mode": "reference", "question_type": "issuer_investor_csd_definitions", "_note": "EU legal definitions added to the platform definition"})
    # v1.1: questions about the November release also carry Milan's deployment plan when Milan was not named
    if re.search(r"r2026\\.nov|november release|nov release", ql) and "Milan" not in entities:
        for mode in ["reference", "future"]:
            r = route_keys.get(("milan_t2s_release_plan_nov", "Milan", "settlement", mode))
            if r and not any(c["question_type"] == "milan_t2s_release_plan_nov" for c in contexts):
                contexts.append({"as_of": r["latest_review_date"], "entity": "Milan", "service": "settlement", "role": "participant" if "participant" in r["roles"] else r["roles"][0], "mode": mode, "question_type": "milan_t2s_release_plan_nov", "_note": "Milan deployment plan for the November release"})
                break
    blocked_ctx = [{"as_of": index["knowledge_base_as_of"], "entity": entities[0], "service": "settlement", "role": "participant", "mode": "current", "question_type": qt, "_note": "explicitly blocked topic"} for qt in blocked_hits]
    if re.search(r"swap|exchange (of )?(two|2) securities|security-for-security|securities-for-securities|atomic|exchange .* (shares|bonds).* for", ql):
        if not any(c["question_type"] == "securities_swap_atomicity" for c in blocked_ctx):
            blocked_ctx.append({"as_of": index["knowledge_base_as_of"], "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "securities_swap_atomicity"})
        if not any(c["question_type"] == "realignment_mechanism" for c in contexts):
            contexts.append({"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "realignment_mechanism", "_note": "narrower supported mechanism (all-or-none realignment chain) retrieved alongside the blocked swap topic"})
        if not any(c["question_type"] == "t2s_linked_instructions" for c in contexts):
            contexts.append({"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_linked_instructions", "_note": "actor-specified WITH links are the closest supported construct"})
        if "Milan" in entities:
            for qt, as_of in (("finality", "2026-09-13"), ("milan_instruction_processing_rules", "2026-09-14")):
                if route_keys.get((qt, "Milan", "settlement", "current")) and not any(c["question_type"] == qt and c["entity"] == "Milan" for c in contexts):
                    contexts.append({"as_of": as_of, "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": qt, "_note": "Milan legal boundary for a swap between Monte Titoli participants"})
    keep = max(max_contexts - len(blocked_ctx), 1)
    contexts = contexts[:keep] + blocked_ctx
    return contexts, {"entities": entities, "topic_hits": sorted({h[0] for h in hits}), "blocked_hits": blocked_hits, "dates": dates, "router_revision": ROUTER_REVISION}


'''
s = s[:start] + new_fn + s[end:]
P.write_text(s)
import ast; ast.parse(s)
print("router v1.1 applied; syntax ok")
