"""Export only explicitly reviewed evidence sections. Does not fetch or approve sources."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def clip(text, start=None, end=None):
    # Keep the original typography; tolerate whitespace changes across wrapped lines.
    def pattern(s):
        return r"\s+".join(re.escape(p) for p in s.split())
    if start:
        m = re.search(pattern(start), text)
        if not m:
            raise ValueError(f"Missing start anchor: {start}")
        text = text[m.start():]
    if end:
        m = re.search(pattern(end), text)
        if not m:
            raise ValueError(f"Missing end anchor: {end}")
        text = text[:m.start()]
    return text.strip()


def extract(spec, sources):
    source = sources[spec["source_id"]]
    path = ROOT / spec.get("path", source["text_path"])
    text = path.read_text()
    if spec["kind"] == "pdf_pages":
        pages = dict((int(n), body) for n, body in re.findall(
            r"^## PDF page (\d+)\n(.*?)(?=^## PDF page \d+\n|\Z)", text, re.M | re.S))
        text = "\n\n".join(f"[PDF page {n}]\n{pages[n]}" for n in spec["pages"])
    elif spec["kind"] == "article":
        m = re.search(r"(?m)^Article\s+" + str(spec["article"]) + r"\s*$", text)
        if not m:
            raise ValueError(f"Missing article: {spec}")
        rest = text[m.end():]
        end = re.search(r"(?m)^Article\s+\d+\s*$", rest)
        text = text[m.start():m.end() + end.start()] if end else text[m.start():]
    elif spec["kind"] == "structured":
        text = json.dumps(json.loads(text), ensure_ascii=False, indent=2)
    elif spec["kind"] != "text":
        raise ValueError(f"Unknown extractor: {spec['kind']}")
    return clip(text, spec.get("start"), spec.get("end"))


def build():
    config = read_json(ROOT / "retrieval/section-decisions.json")
    sources = read_json(ROOT / "retrieval/source-register.json")
    for key, s in sources.items():
        for path_key, hash_key in [("local_path", "sha256"), ("text_path", "text_sha256")]:
            if sha(ROOT / s[path_key]) != s[hash_key]:
                raise ValueError(f"Source changed; new review required: {key} {path_key}")
    chunks = []
    for s in config["sections"]:
        if s["decision"] != "admit":
            continue
        parts = []
        citations = []
        for part in s["extracts"]:
            source = sources[part["source_id"]]
            if part.get("path") and sha(ROOT / part["path"]) != part["derivative_sha256"]:
                raise ValueError(f"Reviewed derivative changed: {s['id']}")
            body = extract(part, sources)
            if not body or len(body) < 40:
                raise ValueError(f"Empty/short evidence: {s['id']}")
            parts.append({"source_id": part["source_id"], "locator": part["locator"], "text": body})
            citations.append({"source_id": part["source_id"], "title": source["title"],
                              "source_url": source["url"], "source_sha256": source["sha256"],
                              "source_path": source["local_path"], "locator": part["locator"],
                              "pdf_pages": part.get("pages", []),
                              "body_language": source["actual_content_language"],
                              "authoritative_language": source.get("authoritative_language"),
                              "translation_status": source.get("translation_status"),
                              "approval_status": source.get("approval_status"),
                              "source_verified_as_of": source["verified_as_of"],
                              "document_version": source.get("document_version"),
                              "publication_date": source.get("publication_date"),
                              "revision_date": source.get("revision_date")})
        chunk = dict(s, evidence=parts, citations=citations)
        chunk["content_sha256"] = hashlib.sha256(json.dumps(parts, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        chunks.append(chunk)
    ids = {s["id"] for s in chunks}
    assert len(ids) == len(chunks), "Duplicate section IDs"
    for s in chunks:
        assert set(s["dependency_ids"]).issubset(ids), s["id"]
        for dep in s["dependency_ids"]:
            d = next(c for c in chunks if c["id"] == dep)
            assert d["verified_as_of"] == s["verified_as_of"], "Dependency review-date mismatch: " + s["id"]
        if "current" in s["modes"] and not s["effective_from"] and not s.get("event_scope"):
            assert s.get("applicability_basis") == "publication_description", "Unqualified current admission: " + s["id"]
    review_dates = sorted({s["verified_as_of"] for s in chunks})
    target = ROOT / "retrieval/admitted-sections.jsonl"
    target.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks))
    exports = ROOT / "retrieval/exports"
    exports.mkdir(exist_ok=True)
    for mode in ["current", "reference", "future"]:
        (exports / f"{mode}.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks if mode in c["modes"]))
        for review_date in review_dates:
            folder = exports / review_date
            folder.mkdir(exist_ok=True)
            (folder / f"{mode}.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks
                                                         if mode in c["modes"] and c["verified_as_of"] == review_date))
    index = ["# Reviewed evidence sections", "", f"Base review: {config['as_of']}; available scoped review dates: {', '.join(review_dates)}. {len(chunks)} bounded sections; no whole-document admission.", "",
             "Use the local retrieval command to enforce entity, service, question type, mode and date constraints. Exporting these files to another AI does not enforce the controls by itself.", "",
             "| ID | Section | Permitted questions | Scope / mode | Review date |", "|---|---|---|---|---|"]
    for c in chunks:
        index.append(f"| {c['id']} | {c['title']} | {', '.join(c['question_types'])} | {', '.join(c['entities'])}; {', '.join(c['modes'])} | {c['verified_as_of']} |")
    (ROOT / "retrieval/README.md").write_text("\n".join(index) + "\n")
    manifest = {"as_of": config["as_of"], "section_count": len(chunks), "source_count": len(sources),
                "whole_document_admission": False, "review_dates": review_dates,
                "verification_output_dir": config.get("verification_output_dir", "implementation/2026-09-13/verification"),
                "files": {str(p.relative_to(ROOT)): sha(p) for p in [target, ROOT / "retrieval/section-decisions.json", ROOT / "retrieval/source-register.json",
                          ROOT / "scripts/retrieve_evidence.py", ROOT / "scripts/build_retrieval.py", *sorted(exports.rglob("*.jsonl"))]}}
    (ROOT / "retrieval/build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({k: v for k, v in manifest.items() if k != "files"}))


if __name__ == "__main__":
    build()
