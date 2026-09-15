"""Local evidence retrieval with explicit scope. No LLM or trading-system integration.

Example:
python3 scripts/retrieve_evidence.py --context '{"as_of":"2026-09-13",
 "entity":"Milan","service":"settlement","role":"participant",
 "mode":"current","question_type":"matching_concept"}'

Question type is an explicit routing input, not an automatic natural-language classifier.
Returned excerpts are evidence, never certification that an arbitrary question is answered.
"""
import argparse
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["as_of", "entity", "service", "role", "mode", "question_type"]
BLOCKED = {
    "milan_participant_cutoff": ("G01", "Applicable Milan timetable notice chain remains unresolved."),
    "production_xtrm_fields": ("G03", "Current production X-TRM standard and service entitlements required; future notice is not a payload specification."),
    "instrument_eligibility": ("G04", "Current ISIN, CSD-link, account, currency and MT23/static-data evidence required."),
    "production_matching_fields": ("G14", "Functional diagrams repaired; production MyStandards/XSD usage dependencies not validated."),
    "athens_production_interface": ("G12", "Current DSS technical notices and exact interface specifications required."),
    "athens_tax_deadline": ("G17", "The four-CSD handbook does not establish Athens tax deadlines."),
    "fee_amount": ("G17", "Exact tariff row, service, charging basis, currency and transaction date must be reviewed."),
    "securities_swap_atomicity": ("G04", "Two-security structure, actual eligible links and supported instruction linkage require separate evidence."),
    "unconditional_oslo_approval": ("G07", "Edition-specific approval has not been established."),
    "incident_reporting_procedure": ("G06", "Current RTS/ITS and national reporting chain not completely reviewed."),
}


class EvidenceLibrary:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        manifest = json.loads((self.root / "retrieval/build-manifest.json").read_text())
        for name, expected in manifest["files"].items():
            actual = hashlib.sha256((self.root / name).read_bytes()).hexdigest()
            if actual != expected:
                raise ValueError(f"Retrieval artifact changed: {name}; rebuild and review required")
        self.as_of = manifest["as_of"]
        self.sections = [json.loads(line) for line in (self.root / "retrieval/admitted-sections.jsonl").read_text().splitlines()]
        self.by_id = {s["id"]: s for s in self.sections}
        self.sources = json.loads((self.root / "retrieval/source-register.json").read_text())

    def retrieve(self, context):
        def result(status, reason, **extra):
            return {"status": status, "reason": reason, "knowledge_as_of": self.as_of,
                    "context": context, "evidence": [], "answer_generated": False, **extra}
        if not isinstance(context, dict):
            return result("needs_context", "Context must be a JSON object.")
        missing = [k for k in REQUIRED if not context.get(k)]
        if missing:
            return result("needs_context", "Material scope is missing.", missing_fields=missing)
        string_fields = REQUIRED + ["business_date", "currency", "release", "access_model", "link_model", "payment_type"]
        if any(k in context and not isinstance(context[k], str) for k in string_fields):
            return result("needs_context", "Scope fields must be strings.")
        try:
            date.fromisoformat(context["as_of"])
            if context.get("business_date"):
                date.fromisoformat(context["business_date"])
        except (ValueError, TypeError):
            return result("needs_context", "Dates must be valid ISO YYYY-MM-DD values.")
        if context["as_of"] != self.as_of:
            return result("needs_refresh", "This is a dated knowledge snapshot. Recheck sources and approve a new snapshot before answering a different as-of date.")
        topic = context["question_type"]
        if topic in BLOCKED:
            gap, reason = BLOCKED[topic]
            return result("blocked", reason, gap_ids=[gap])
        if topic == "dated_t2s_schedule":
            missing = [k for k in ["business_date", "currency"] if not context.get(k)]
            if missing:
                return result("needs_context", "Dated schedule needs business date and currency.", missing_fields=missing)
            if context["business_date"] != "2026-09-08" or context["currency"] != "EUR":
                return result("blocked", "No reviewed complete event overlay for this business date/currency. Baseline alone is insufficient.", gap_ids=["G02"])
        if topic == "porto_calendar":
            missing = [k for k in ["business_date", "payment_type"] if not context.get(k)]
            if missing:
                return result("needs_context", "Calendar scope missing.", missing_fields=missing)
            if not context["business_date"].startswith("2026-"):
                return result("blocked", "Only the published 2026 calendar is reviewed.", gap_ids=["G09"])
            if context["payment_type"] not in ["FOP", "DVP"]:
                return result("needs_context", "Payment type must be FOP or DVP.")
        if topic == "cross_csd_message_flow":
            needs = [k for k in ["release", "access_model", "currency", "link_model"] if not context.get(k)]
            if needs:
                return result("needs_context", "Cross-CSD message flow depends on the selected model.", missing_fields=needs)
            if context["access_model"] != "ICP" or context["currency"] != "EUR" or context["link_model"] != "direct-both-in-T2S":
                return result("blocked", "Only the explicitly assumed ICP/EUR/direct link between two T2S CSDs is covered by this message-flow selection.", gap_ids=["G04", "G14"])

        def scoped(s):
            return (context["entity"] in s["entities"] and context["service"] in s["services"] and
                    context["role"] in s["roles"] and context["mode"] in s["modes"])
        candidates = [s for s in self.sections if topic in s["question_types"] and scoped(s)]
        if not candidates:
            return result("blocked", "No reviewed section for this question type, entity, service, role and mode. Unreviewed documents cannot fill the gap.")
        selected = {s["id"]: s for s in candidates}
        queue = list(candidates)
        while queue:
            s = queue.pop()
            for dep in s["dependency_ids"]:
                if dep not in selected:
                    d = self.by_id[dep]
                    if not scoped(d):
                        return result("blocked", f"Required context evidence is outside scope: {dep}")
                    selected[dep] = d
                    queue.append(d)
        missing = sorted({k for s in selected.values() for k in s["required_context"] if not context.get(k)})
        if missing:
            return result("needs_context", "Selected evidence needs more scope.", missing_fields=missing)
        if context.get("release") and any(s["platform_release"] and s["platform_release"] != context["release"] for s in selected.values()):
            return result("blocked", "Requested release does not match the reviewed platform evidence.", gap_ids=["G15"])
        if context["mode"] == "current" and context.get("business_date") and topic not in ["dated_t2s_schedule", "porto_calendar"]:
            business_date = context["business_date"]
            if business_date > self.as_of or any(not s["effective_from"] or business_date < s["effective_from"] or
                                                (s["effective_to"] and business_date > s["effective_to"])
                                                for s in selected.values()):
                return result("blocked", "The requested business date is outside a verified effective period; historical/future applicability needs separate evidence.")
        # Verify only selected source bytes/derivatives. The immutable export's hashes were checked on load.
        for s in selected.values():
            for e in s["extracts"]:
                source = self.sources[e["source_id"]]
                for path, expected in [(source["local_path"], source["sha256"]), (source["text_path"], source["text_sha256"])]:
                    if hashlib.sha256((self.root / path).read_bytes()).hexdigest() != expected:
                        return result("blocked", "Evidence changed after review; source must be rechecked.", changed_source=e["source_id"])
                if e.get("path") and hashlib.sha256((self.root/e["path"]).read_bytes()).hexdigest() != e["derivative_sha256"]:
                    return result("blocked", "Structured derivative changed after review.", changed_source=e["source_id"])
        evidence = [selected[k] for k in sorted(selected)]
        return result("evidence_only", "Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.", evidence=evidence)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", required=True, help="Explicit JSON scope, including question_type")
    parser.add_argument("--summary", action="store_true", help="Print citations and limits without excerpt bodies")
    args = parser.parse_args()
    result = EvidenceLibrary().retrieve(json.loads(args.context))
    if args.summary:
        result["evidence"] = [{k: e[k] for k in ["id", "title", "citations", "limitations"]} for e in result["evidence"]]
    print(json.dumps(result, ensure_ascii=False, indent=2))
