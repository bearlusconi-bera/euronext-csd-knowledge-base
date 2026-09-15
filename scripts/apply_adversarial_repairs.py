"""Record bounded editorial corrections and a scoped publication review; no bulk refresh."""
import copy
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "implementation/2026-09-14"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    config_path = ROOT / "retrieval/section-decisions.json"
    config = json.loads(config_path.read_text())
    if config.get("repair_revision") == "2026-09-14-adversarial-v1":
        raise SystemExit("Editorial repairs already recorded; review later changes explicitly.")
    sources = json.loads((ROOT / "retrieval/source-register.json").read_text())
    by_id = {s["id"]: s for s in config["sections"]}
    config.update(schema_version=2, repair_revision="2026-09-14-adversarial-v1",
                  verification_output_dir="implementation/2026-09-14/verification")
    for s in config["sections"]:
        s["subject_release"] = "R2026.NOV" if s["id"] == "november-release" else None
        s["applicability_basis"] = "reviewed_effective_interval" if s["effective_from"] else "reference_description"
    for id in ["copenhagen-dcp", "porto-dcp"]:
        s = by_id[id]
        s["applicability_basis"] = "publication_description"
        s["limitations"].append("Qualified description of the published requirements at the review date; operative effective date is not established. This does not certify current legal applicability.")
    by_id["t2s-schedule"]["schedule_model"] = "T2S"
    by_id["copenhagen-day"]["schedule_model"] = "Copenhagen-local"
    by_id["t2s-events-sep08"]["event_scope"] = {"schedule_model": "T2S", "business_date": "2026-09-08", "currency": "EUR"}
    by_id["porto-calendar"]["calendar_scope"] = {"from": "2026-01-01", "to": "2026-12-31", "payment_types": ["FOP", "DVP"]}
    by_id["porto-calendar"]["effective_to"] = "2026-12-31"
    by_id["november-release"]["publication_status"] = "market_review_draft_at_review_date"
    by_id["november-release"]["limitations"] = [
        "Historical 13 September review: the then-captured hub listed market-review drafts; the planned final-publication date did not prove delivery.",
        "Revalidate official sources for a later review date; this snapshot does not establish subsequent publication status."]

    # Source bytes are copied without alteration from the independently preserved audit evidence.
    receipts = json.loads((ROOT / "audits/2026-09-14-adversarial/evidence/november-final-receipts.json").read_text())
    specs = [("ecb-november-final-cover-20260914", "november-final-cover", "2026-09-14"),
             ("ecb-november-final-udfs-20260914", "november-final-udfs", "2026-09-11")]
    extracts = []
    for (id, stem, revision), receipt in zip(specs, receipts):
        src = ROOT / "audits/2026-09-14-adversarial/evidence" / (stem + ".pdf")
        if sha(src) != receipt["sha256"]:
            raise ValueError("Audit source changed: " + stem)
        original = OUT / "sources" / (stem + ".pdf")
        original.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, original)
        # Only cover-page evidence is being admitted. Retain its original extracted text.
        full_text = (src.with_suffix(".txt")).read_text()
        first_page = full_text.split("## PDF page 2", 1)[0].strip() + "\n"
        text_path = OUT / "extracted" / (stem + ".md")
        text_path.parent.mkdir(exist_ok=True)
        text_path.write_text(first_page)
        sources[id] = {"id": id, "title": receipt["title"], "url": receipt["url"],
            "local_path": str(original.relative_to(ROOT)), "sha256": sha(original),
            "text_path": str(text_path.relative_to(ROOT)), "text_sha256": sha(text_path),
            "actual_content_language": "en", "authoritative_language": "en",
            "publication_date": "2026-09-14", "revision_date": revision,
            "effective_from": None, "effective_to": None, "verified_as_of": "2026-09-14",
            "document_version": "R2026.NOV final publication; no production-deployment certification",
            "approval_status": "Final document delivery confirmed; production deployment not verified",
            "date_evidence": "14 September cover/listing; UDFS cover date 11 September. Earlier target is a separate fact.",
            "provenance_note": "Only PDF page 1 is admitted for document identity/publication status; technical changes are unreviewed."}
        extracts.append({"source_id": id, "kind": "pdf_pages", "pages": [1],
                         "locator": "PDF page 1: " + ("final-publication statement, dated 14 September 2026" if stem.endswith("cover") else "document identity/date, 11 September 2026")})
    final = copy.deepcopy(by_id["november-release"])
    final.update(id="november-final-release", title="November final publication confirmed on 14 September; deployment unverified",
                 verified_as_of="2026-09-14", extracts=extracts, publication_status="final_published",
                 permitted_use="R2026.NOV document identity and final-publication status as reviewed on 14 September 2026",
                 limitations=["Final publication is established; November production deployment is not verified.",
                              "The 14 September cover/listing, 11 September UDFS date and earlier target are separate facts.",
                              "Only cover-page statements are admitted. No November operational provisions, payloads or changed message versions are admitted."])
    config["sections"].append(final)
    sources["14dc34b8e54e"]["authoritative_language"] = "no"  # Explicit original-language reservation on PDF cover.
    for source in sources.values():
        auth, body = source.get("authoritative_language"), source["actual_content_language"]
        source["translation_status"] = ("translation; authoritative language differs" if auth in ["it", "el", "no"] and auth != body
                                         else "original or official-language text" if auth == body or auth == "EU official languages"
                                         else "not independently established")
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "retrieval/source-register.json").write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n")
    (OUT / "source-admission.json").write_text(json.dumps({"new_sections": [final["id"]], "new_sources": [s[0] for s in specs],
        "review_date": "2026-09-14", "older_section_review_dates_unchanged": True,
        "production_deployment_verified": False, "whole_document_admission": False}, indent=2) + "\n")
    print(json.dumps({"sections": len(config["sections"]), "sources": len(sources), "base_review_date": config["as_of"], "new_publication_review_date": "2026-09-14"}))


if __name__ == "__main__":
    main()
