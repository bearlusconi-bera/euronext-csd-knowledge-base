"""Apply reviewed metadata corrections without editing any archived source bytes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPL = ROOT / "implementation/2026-09-13"


def dump(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def apply():
    before = IMPL / "before"
    before.mkdir(parents=True, exist_ok=True)
    names = ["curated-manifest.json", "catalogue.json", "metadata/legal-browser-sources.json"]
    for name in names:
        dest = before / name
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((ROOT/name).read_bytes())
    manifest = json.loads((ROOT / names[0]).read_text())
    catalogue = json.loads((ROOT / names[1]).read_text())
    captures = json.loads((ROOT / names[2]).read_text())
    corrections = {
        "ac385b0f3106": {
            "group": "European Offering", "knowledge_layer": "programme-scoped-reference",
            "why_read": "European Offering listing scope and future designated/alternative places; not universal Milan instrument eligibility.",
            "version_date_evidence": "Workbook snapshot 11 September 2026; listing data through 10 September; designated/alternative columns apply from 21 September.",
            "structured_extract_path": "implementation/2026-09-13/structured/european-offering-workbook.json",
            "review_scope": "Introduction, headers and sampled rows checked. All cells preserved mechanically; per-ISIN eligibility not validated."},
        "dd1cf7cb930b": {"quarantined_locators": ["PDF 13 / printed 9: NTS 19:30", "PDF 15 / printed 11: two partial windows"],
                          "conflict_note": "English and Italian clock passages conflict with R2026.JUN UDFS 20:00/five windows. Current Milan notice chain unresolved; remaining sections require separate review."},
        "02022R2554-20221227": {"actual_content_language": "fr", "navigation_language": "en",
                               "capture_issue": "French operative text beneath English navigation; do not quote as English.",
                               "english_replacement_id": "dora-english-oj", "knowledge_layer": "language-qualified-reference"},
        "535f6a23062a": {"structured_extract_path": "extracted/535f6a23062a-rows.json",
                         "normalised_entity_reference": "implementation/2026-09-13/structured/interbolsa-identity.json",
                         "identity_join_quarantine": {"sheet": "1- CSD authorisations", "cell": "C25", "value": "529900LG70TCA"}},
        "d89c56df8c5a": {"conflict_note": "Probable edition-versus-amendment labelling (inference), not an established operative-text contradiction. Greek/English sampled histories identify seven amendments; independent approval chain remains incomplete.",
                         "knowledge_layer": "unresolved-source-identity", "review_scope": "Identity/history only admitted via section register. Operational clauses not automatically admitted."},
        "14dc34b8e54e": {"approval_status": "Edition-specific reservation unresolved in both English and Norwegian covers; system approval is not edition approval.",
                         "review_scope": "Qualified cover/identity evidence only admitted; do not infer unconditional operative status."},
        "089b7aaef991": {"effective_from": None, "version_date_evidence": "V43; internal 26 January 2026, filename 16 February, upload April. Operative effective date not established.",
                         "field_anomalies": ["PDF 66 prints semt.07; exact production identifier not normalised without specification."]},
        "cbdf3c1f8b51": {"version_date_evidence": "Cover 3 August 2026; conflicting footer version labels 12/13 retained. Identify by cover and hash."},
        "aa3d5a3b94c9": {"platform_release": "R2026.JUN", "publication_date": "2026-01-22", "deployment_date": "2026-06-14",
                         "structured_extract_path": "implementation/2026-09-13/structured/t2s-matching-fields.json",
                         "review_scope": "Selected matching/posting/realignment/message/day-phase excerpts admitted only via section register; Diagrams 55–57 visually repaired."},
    }
    for d in catalogue + manifest["documents"] + manifest["legal_texts"] + captures:
        if "previous_default_retrieval" not in d:
            d["previous_default_retrieval"] = d.get("default_retrieval")
        d["default_retrieval"] = False
        d["retrieval_admission"] = "Explicit section decisions only; this whole document is not admitted"
        d["section_decisions_path"] = "retrieval/section-decisions.json"
        d.update(corrections.get(d["id"], {}))
    source = json.loads((ROOT / "retrieval/source-register.json").read_text())["dora-english-oj"]
    text = ROOT / source["text_path"]
    replacement = {"id": "dora-english-oj", "title": "DORA English OJ text — reviewed Articles 2 and 64",
                   "url": source["url"], "local_path": source["local_path"], "original_sha256": source["sha256"],
                   "text_path": source["text_path"], "sha256": hashlib.sha256(text.read_bytes()).hexdigest(),
                   "actual_content_language": "en", "retrieved_at": "2026-09-13", "characters": len(text.read_text()),
                   "complete_text_capture": True, "default_retrieval": False, "knowledge_layer": "bounded-legal-context",
                   "why_read": "English source for CSD inclusion and the general DORA application date.",
                   "review_scope": "Only Articles 2 and 64 substantively admitted; no complete incident-reporting chain.",
                   "section_decisions_path": "retrieval/section-decisions.json"}
    for collection in [manifest["legal_texts"], captures]:
        if not any(d["id"] == replacement["id"] for d in collection):
            collection.append(replacement.copy())
    manifest.update(retrieval_policy_updated="2026-09-14", whole_document_admission=False,
                    admitted_sections_path="retrieval/admitted-sections.jsonl", policy_path="retrieval/section-decisions.json")
    dump(ROOT/names[0], manifest); dump(ROOT/names[1], catalogue); dump(ROOT/names[2], captures)
    dump(IMPL/"source-corrections.json", corrections)
    print(json.dumps({"whole_document_defaults_enabled": sum(bool(d.get('default_retrieval')) for d in catalogue+manifest['documents']+manifest['legal_texts']),
                      "curated_documents": len(manifest['documents']), "legal_captures":len(manifest['legal_texts']), "correction_groups":len(corrections)}))


if __name__ == "__main__":
    apply()
