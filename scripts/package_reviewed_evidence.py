"""Package verified, bounded evidence exports; never include full source manuals."""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviewed-evidence-pack.zip"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def package():
    build_bytes = (ROOT / "retrieval/build-manifest.json").read_bytes()
    build = json.loads(build_bytes)
    verify = ROOT / build["verification_output_dir"]
    verification_bytes = (verify / "verification.json").read_bytes()
    results = json.loads(verification_bytes)["summary"]
    if results["failures"] or results["build_manifest_sha256"] != sha(build_bytes):
        raise ValueError("Run successful verification against the current build before packaging")
    repair_bytes = (verify / "repair-verification.json").read_bytes()
    repairs = json.loads(repair_bytes)["summary"]
    if repairs["failures"] or repairs["build_manifest_sha256"] != sha(build_bytes):
        raise ValueError("Run successful adversarial/repair verification against the current build before packaging")
    for name, expected in build["files"].items():
        if sha((ROOT / name).read_bytes()) != expected:
            raise ValueError(f"Build artifact changed after verification: {name}")

    files, counts, all_ids = {}, {}, set()
    for mode in ["current", "reference", "future"]:
        name = f"retrieval/exports/{mode}.jsonl"
        data = (ROOT / name).read_bytes()
        sections = [json.loads(line) for line in data.splitlines()]
        ids = {s["id"] for s in sections}
        if any(mode not in s["modes"] or not set(s["dependency_ids"]).issubset(ids) for s in sections):
            raise ValueError(f"Mode/dependency violation in {mode} export")
        counts[mode] = len(sections)
        all_ids.update(ids)
        files[name] = data
    date_counts = {}
    for review_date in build["review_dates"]:
        date_counts[review_date] = {}
        for mode in ["current", "reference", "future"]:
            name = f"retrieval/exports/{review_date}/{mode}.jsonl"
            data = (ROOT / name).read_bytes()
            sections = [json.loads(line) for line in data.splitlines()]
            ids = {s["id"] for s in sections}
            if any(s["verified_as_of"] != review_date or mode not in s["modes"] or
                   not set(s["dependency_ids"]).issubset(ids) for s in sections):
                raise ValueError("Date/mode/dependency violation in " + name)
            date_counts[review_date][mode] = len(sections)
            files[name] = data
    if len(all_ids) != build["section_count"]:
        raise ValueError("Mode exports do not cover the reviewed section set")
    for name in ["retrieval/section-decisions.json", "retrieval/source-register.json", "retrieval/README.md"]:
        files[name] = (ROOT / name).read_bytes()
    # Include only the reviewed matching visuals, preserving locators from the repair.
    for name in ["audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
                 "implementation/2026-09-13/evidence/t2s-p270.png"]:
        files[name] = (ROOT / name).read_bytes()
    files["verification/verification.json"] = verification_bytes
    files["verification/repair-verification.json"] = repair_bytes
    files["README.md"] = f"""# Reviewed Euronext CSD evidence pack

Base operational review: **{build['as_of']}**. Additional reviewed sections carry their own review date
(currently {', '.join(build['review_dates'])}); the 14 September 2026 date covers the scoped release-publication
update and the settlement-expert-agent snapshot admitted the same day.
{len(all_ids)} distinct reviewed sections from {build['source_count']} source identities.

## Import and retrieval

Start with [13 September current evidence](retrieval/exports/2026-09-13/current.jsonl).
The 14 September exports contain the November final-publication section and the
settlement-agent snapshot sections reviewed on that date ({date_counts.get('2026-09-14', {}).get('current', 0)} current,
{date_counts.get('2026-09-14', {}).get('reference', 0)} reference, {date_counts.get('2026-09-14', {}).get('future', 0)} future).
Choose one exact review date and mode before ingestion; sections never mix review dates through dependencies.
The combined top-level mode files contain {counts['current']} current,
{counts['reference']} reference and {counts['future']} future sections and require
the same date filtering. Some sections occur in more than one permitted mode.
Consult [the section index](retrieval/README.md) for permitted question types.

Uploading this pack does not enforce retrieval controls. The receiving system must
require the evidence date, entity, service, actor role, question type and mode;
apply those filters before retrieval, including exact `verified_as_of`; include
every dependency; enforce required context, subject/platform release, event scope,
calendar intervals and applicability basis; and preserve
limitations and source-language/approval qualifications. Block unsupported
questions. Never widen an excerpt into permission to use a whole manual.

Use the section decisions and source register as policy/provenance, not extra
answer evidence. Citation URLs and PDF/article locators point to the original
authorities. Source paths in the metadata refer to the full local workspace;
original manuals are deliberately absent from this pack. The two matching
diagram images support their reviewed functional transcription only.

This is an ingestion bundle, not a standalone executable retriever. The full
workspace supplies `scripts/retrieve_evidence.py`, context checks, originals and
source-hash verification. Do not treat package hashes as authority signatures.
No unrestricted full-document starter pack or AI-written guide is admitted here.

## Dates, scope and known gaps

Revalidate official sources and applicable notices before advancing the snapshot
date. Future laws/releases are never promoted solely because time passed.
Milan participant cut-offs, unconditional Oslo edition approval, independent
Athens approval, exact production fields/entitlements, actual ISIN eligibility
and complete reporting/tax/fee procedures remain unresolved where governing
evidence is missing or unreviewed. The full workspace's dependency register
records all 17 audit dependencies and their partial or unresolved outcomes.

The matching diagrams are functional descriptions, not certified XML schemas.
T2S-native messages are not local participant-interface specifications.
Reviewed dated ECB event overlays exist only for the business dates and currencies
listed in the section index (8 September 2026 EUR at the 13 September review; the 2026
status-history dates and the routine-only date list at the 14 September review).
Any schedule reached directly or through a dependency needs a matching overlay
for an actual-date query. An explicitly nominal request uses `schedule_kind: baseline`;
dated questions otherwise default to actual. A publication description is not proof
of operative requirements. The November final delivery does not certify deployment.

## Verification

{results['routing_passed']}/{results['routing_cases']} explicit routing cases and
{results['integrity_passed']}/{results['integrity_checks']} integrity/control checks passed.
The preserved adversarial cases passed {repairs['adversarial_passed']}/{repairs['adversarial_cases']},
plus {repairs['repair_checks_passed']}/{repairs['repair_checks']} repair-specific checks.
{results['originals_verified_unchanged']} original documents were preserved.
Routing cases with an expected block correctly blocked evidence selection ({sum(1 for x in json.loads((verify / 'retrieval-results.json').read_text()) if x['expected_status'] == 'blocked' and x['outcome'] == 'PASS')} cases).
LLM answer quality was not tested; no hosted answer service is included.

`PACKAGE-MANIFEST.json` hashes every other member of this archive. It is a
transport integrity manifest, distinct from the full workspace build manifest.
Verification metadata records the full workspace build that was tested.
""".encode()
    manifest = {"base_evidence_as_of": build["as_of"], "review_dates": build["review_dates"],
                "sections_by_review_date_and_mode": date_counts, "distinct_sections": len(all_ids),
                "source_identities": build["source_count"], "sections_by_mode": counts,
                "full_workspace_build_manifest_sha256": sha(build_bytes),
                "whole_documents_included": False,
                "files": {name: sha(data) for name, data in sorted(files.items())}}
    files["PACKAGE-MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(OUT) as z:
        if z.testzip() is not None or set(z.namelist()) != set(files):
            raise ValueError("Archive membership/CRC check failed")
        if any(sha(z.read(name)) != expected for name, expected in manifest["files"].items()):
            raise ValueError("Archive member hash check failed")
    report = {"outcome": "PASS", "archive": OUT.name, "sha256": sha(OUT.read_bytes()),
              "bytes": OUT.stat().st_size, "member_count": len(files),
              "distinct_sections": len(all_ids), "sections_by_mode": counts, "sections_by_review_date_and_mode": date_counts,
              "checks": ["Successful current-build verification", "Build artifact hashes",
                         "Mode/date/dependency containment", "Section-set coverage", "ZIP CRC",
                         "Archive membership", "Every member hash"]}
    (verify / "package-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    package()
