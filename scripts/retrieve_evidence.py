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
import re
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
    # 2026-09-14 settlement-agent snapshot: additional unsupported topics recorded against the audit dependency register.
    "copenhagen_dcp_entitlements": ("G10", "Copenhagen DCP User Guidelines and accepted service tests are not public; Part 5 states requirements only."),
    "oslo_operational_calendar": ("G11", "Current VPO NOK operating calendar, cycle times and MyVPS specifications are not in reviewed evidence."),
    "athens_dss_technical_cycles": ("G12", "DSS technical announcements defining cycles, cut-offs and formats are not in reviewed evidence."),
    "porto_std_file_layout": ("G13", "STD Manual Appendix A1 layouts and full field semantics are not admitted; only the manual's published field table is."),
    "mystandards_usage_rules": ("G14", "MyStandards usage guidelines and XSDs require an account; T2S-native usage rules are not admitted field by field."),
    "november_operational_provisions": ("G15", "R2026.NOV operational provisions are unreviewed and the release is not deployed; only publication status, the Milan deployment plan and text-comparison evidence are admitted."),
    "cmvm_information_duties": ("G16", "CMVM Regulation 5/2018 as amended is not captured; the official Gazette response was an application shell."),
    "milan_xtrm_message_layout": ("G03", "Standard for X-TRM Users (A2A MT / RNI, VER.01.09) is client-only in MT-X; only the published field correspondence table is admitted."),
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
        self.review_dates = manifest.get("review_dates", [self.as_of])
        self.sections = [json.loads(line) for line in (self.root / "retrieval/admitted-sections.jsonl").read_text().splitlines()]
        self.by_id = {s["id"]: s for s in self.sections}
        self.sources = json.loads((self.root / "retrieval/source-register.json").read_text())

    @staticmethod
    def _overlay_matches(scope, model, context):
        """An event overlay applies to exactly one schedule model and business date (or a reviewed list of dates).
        Currency must match exactly, or the overlay must be reviewed as currency-neutral ("ALL")."""
        if not scope or scope.get("schedule_model") != model:
            return False
        dates = scope.get("business_dates") or [scope.get("business_date")]
        if context["business_date"] not in dates:
            return False
        return scope.get("currency") in (context["currency"], "ALL")

    def retrieve(self, context):
        def result(status, reason, **extra):
            return {"status": status, "reason": reason, "knowledge_as_of": self.as_of,
                    "available_review_dates": self.review_dates,
                    "context": context, "evidence": [], "answer_generated": False, **extra}
        if not isinstance(context, dict):
            return result("needs_context", "Context must be a JSON object.")
        missing = [k for k in REQUIRED if not context.get(k)]
        if missing:
            return result("needs_context", "Material scope is missing.", missing_fields=missing)
        string_fields = REQUIRED + ["business_date", "currency", "release", "access_model", "link_model", "payment_type", "schedule_kind"]
        if any(k in context and not isinstance(context[k], str) for k in string_fields):
            return result("needs_context", "Scope fields must be strings.")
        try:
            dates = {}
            for key in ["as_of", "business_date"]:
                if key in context:
                    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", context[key]):
                        raise ValueError("Non-canonical date")
                    dates[key] = date.fromisoformat(context[key])
        except (ValueError, TypeError):
            return result("needs_context", "Dates must be valid ISO YYYY-MM-DD values.")
        if context["as_of"] not in self.review_dates:
            return result("needs_refresh", "No reviewed evidence for this knowledge date. Revalidate the relevant sources before advancing their review date.")
        if context.get("schedule_kind") not in [None, "baseline", "actual"]:
            return result("needs_context", "schedule_kind must be baseline or actual.")
        topic = context["question_type"]
        if topic in BLOCKED:
            gap, reason = BLOCKED[topic]
            return result("blocked", reason, gap_ids=[gap])
        if topic == "cross_csd_message_flow":
            needs = [k for k in ["release", "access_model", "currency", "link_model"] if not context.get(k)]
            if needs:
                return result("needs_context", "Cross-CSD message flow depends on the selected model.", missing_fields=needs)
            if context["access_model"] != "ICP" or context["currency"] != "EUR" or context["link_model"] != "direct-both-in-T2S":
                return result("blocked", "Only the explicitly assumed ICP/EUR/direct link between two T2S CSDs is covered by this message-flow selection.", gap_ids=["G04", "G14"])

        def scope_without_date(s):
            return (context["entity"] in s["entities"] and context["service"] in s["services"] and
                    context["role"] in s["roles"] and context["mode"] in s["modes"])
        def scoped(s):
            return scope_without_date(s) and s["verified_as_of"] == context["as_of"]
        matching_scope = [s for s in self.sections if topic in s["question_types"] and scope_without_date(s)]
        if topic == "t2s_status_history":
            # Revision v1.1 (14 September 2026): dated status entries are retrievable on their own. They need the business
            # date and currency, match the event scope exactly (or a reviewed currency-neutral "ALL" scope) and do not
            # pull in the nominal baseline, which the dated_t2s_schedule route continues to govern.
            missing = [k for k in ["business_date", "currency"] if not context.get(k)]
            if missing:
                return result("needs_context", "Dated status history requires business date and currency.", missing_fields=missing)
            dated = [s for s in matching_scope if scoped(s) and s.get("event_scope")]
            candidates = [s for s in dated if self._overlay_matches(s["event_scope"], s["event_scope"].get("schedule_model"), context)]
            if dated and not candidates:
                return result("blocked", "No reviewed status entry for this business date and currency. Absence from the reviewed capture is not evidence of routine operations.", gap_ids=["G02"])
        else:
            candidates = [s for s in matching_scope if scoped(s) and not s.get("event_scope")]
        if not candidates:
            if matching_scope and not any(scoped(s) for s in matching_scope):
                return result("needs_refresh", "This topic has not been reviewed for the requested date. A scoped publication update does not refresh unrelated evidence.",
                              topic_review_dates=sorted({s["verified_as_of"] for s in matching_scope}))
            return result("blocked", "No reviewed section for this question type, entity, service, role and mode. Unreviewed documents cannot fill the gap.")
        selected = {s["id"]: s for s in candidates}
        queue = list(candidates)
        def expand_dependencies():
            while queue:
                s = queue.pop()
                for dep in s["dependency_ids"]:
                    if dep not in selected:
                        d = self.by_id[dep]
                        if not scoped(d):
                            return dep
                        selected[dep] = d
                        queue.append(d)
            return None
        invalid_dependency = expand_dependencies()
        if invalid_dependency:
            return result("blocked", f"Required context evidence is outside scope: {invalid_dependency}")
        schedule_models = {s["schedule_model"] for s in selected.values() if s.get("schedule_model")}
        schedule_kind = None
        if schedule_models:
            schedule_kind = context.get("schedule_kind") or ("actual" if context.get("business_date") or topic == "dated_t2s_schedule" else "baseline")
            if topic == "dated_t2s_schedule" and schedule_kind != "actual":
                return result("needs_context", "An actual-date question cannot be relabelled as a baseline. Use an explicitly nominal question route.")
            if schedule_kind == "actual":
                missing = [k for k in ["business_date", "currency"] if not context.get(k)]
                if missing:
                    return result("needs_context", "Actual schedules require business date and currency.", missing_fields=missing)
                for model in schedule_models:
                    overlays = [s for s in self.sections if scoped(s) and self._overlay_matches(s.get("event_scope"), model, context)]
                    if not overlays:
                        return result("blocked", "No reviewed event overlay for this schedule, business date and currency. Nominal evidence alone cannot establish actual operations.", gap_ids=["G02"])
                    for s in overlays:
                        selected[s["id"]] = s
                        queue.append(s)
        invalid_dependency = expand_dependencies()
        if invalid_dependency:
            return result("blocked", f"Required context evidence is outside scope: {invalid_dependency}")
        missing = sorted({k for s in selected.values() for k in s["required_context"] if not context.get(k)})
        if missing:
            return result("needs_context", "Selected evidence needs more scope.", missing_fields=missing)
        if context.get("release") and any(value and value != context["release"] for s in selected.values()
                                           for value in [s.get("platform_release"), s.get("subject_release")]):
            return result("blocked", "Requested release does not match the reviewed platform evidence.", gap_ids=["G15"])
        for s in selected.values():
            calendar = s.get("calendar_scope")
            if calendar:
                if context.get("payment_type") not in calendar["payment_types"]:
                    return result("needs_context", "Payment type is outside the reviewed calendar scope.")
                if not date.fromisoformat(calendar["from"]) <= dates["business_date"] <= date.fromisoformat(calendar["to"]):
                    return result("blocked", "Business date is outside the published calendar interval.", gap_ids=["G09"])
            elif context["mode"] == "current" and not s.get("event_scope"):
                business_date = dates.get("business_date", dates["as_of"])
                if s.get("applicability_basis") == "publication_description":
                    if business_date != dates["as_of"]:
                        return result("blocked", "Only a qualified publication description at the review date is supported; operative applicability is not established.")
                elif (business_date > dates["as_of"] or not s["effective_from"] or
                      business_date < date.fromisoformat(s["effective_from"]) or
                      (s["effective_to"] and business_date > date.fromisoformat(s["effective_to"]))):
                    return result("blocked", "The requested business date is outside a verified effective period; historical/future applicability needs separate evidence.")
        # Verify only selected source bytes/derivatives. The immutable export's hashes were checked on load.
        for s in selected.values():
            for e in s["extracts"]:
                source = self.sources[e["source_id"]]
                try:
                    for path, expected in [(source["local_path"], source["sha256"]), (source["text_path"], source["text_sha256"])]:
                        if hashlib.sha256((self.root / path).read_bytes()).hexdigest() != expected:
                            return result("blocked", "Evidence changed after review; source must be rechecked.", changed_source=e["source_id"])
                    if e.get("path") and hashlib.sha256((self.root/e["path"]).read_bytes()).hexdigest() != e["derivative_sha256"]:
                        return result("blocked", "Structured derivative changed after review.", changed_source=e["source_id"])
                except OSError:
                    return result("blocked", "A reviewed source or derivative is unavailable; restore and verify it before answering.", unavailable_source=e["source_id"])
        evidence = [selected[k] for k in sorted(selected)]
        return result("evidence_only", "Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.",
                      evidence=evidence, knowledge_as_of=context["as_of"], schedule_kind=schedule_kind)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", required=True, help="Explicit JSON scope, including question_type")
    parser.add_argument("--summary", action="store_true", help="Print citations and limits without excerpt bodies")
    args = parser.parse_args()
    try:
        context = json.loads(args.context)
    except json.JSONDecodeError:
        result = {"status": "needs_context", "reason": "Context must be valid JSON.", "evidence": [], "answer_generated": False}
    else:
        try:
            result = EvidenceLibrary().retrieve(context)
        except (OSError, ValueError):
            result = {"status": "blocked", "reason": "Retrieval artifacts are unavailable or fail verification; rebuild and review required.", "evidence": [], "answer_generated": False}
    if args.summary:
        result["evidence"] = [{k: e.get(k) for k in ["id", "title", "citations", "limitations", "verified_as_of", "applicability_basis", "publication_status", "subject_release"]} for e in result["evidence"]]
    print(json.dumps(result, ensure_ascii=False, indent=2))
