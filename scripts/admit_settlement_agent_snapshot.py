"""One-time reviewed admissions for the 14 September 2026 settlement-expert-agent snapshot.

Records editorial decisions taken after reading the cited pages (see implementation/2026-09-14-settlement-agent/
DISCOVERY-LOG.md). It refuses to run twice, backs up the previous controls, dry-runs every extract with the
builder's own extractor, and never edits archived source bytes. Run build_retrieval.py afterwards.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "implementation/2026-09-14-settlement-agent"
REVISION = "2026-09-14-settlement-agent-v1"
D = "2026-09-14"
sys.path.insert(0, str(ROOT / "scripts"))
from build_retrieval import extract  # noqa: E402  (dry-run anchors with the real extractor)

CAT = {d["id"]: d for d in json.loads((ROOT / "catalogue.json").read_text())}
CURATED = json.loads((ROOT / "curated-manifest.json").read_text())
LEGAL = {d["id"]: d for d in CURATED["legal_texts"]}
SOURCES, SECTIONS = {}, []


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(p):
    return str(Path(p).resolve().relative_to(ROOT))


def register(id, title, url, local_path, text_path, lang="en", auth=None, **meta):
    if id in SOURCES:
        return id
    local, text = ROOT / local_path, ROOT / text_path
    rec = {"id": id, "title": title, "url": url, "local_path": rel(local), "sha256": sha(local),
           "text_path": rel(text), "text_sha256": sha(text), "actual_content_language": lang, "authoritative_language": auth,
           "publication_date": None, "revision_date": None, "effective_from": None, "effective_to": None, "verified_as_of": D,
           "document_version": None, "approval_status": "Source identity checked; no independent whole-edition supervisory approval certification",
           "date_evidence": None, "provenance_note": "Only specified excerpts are admitted; original preserved. Reviewed for the 2026-09-14 settlement-agent snapshot."}
    rec.update(meta)
    rec["translation_status"] = ("translation; authoritative language differs" if auth in ["it", "el", "no", "pt"] and auth != lang
                                  else "original or official-language text" if auth == lang or auth == "EU official languages"
                                  else "not independently established")
    SOURCES[id] = rec
    return id


def from_catalogue(id, lang="en", auth=None, **meta):
    d = CAT[id]
    return register(id, d["title"], d["url"], d["local_path"], d["text_path"], lang, auth, **meta)


def legal(id, auth="EU official languages", **meta):
    d = LEGAL[id]
    return register(id, d["title"], d["url"], d["text_path"], d["text_path"], "en", auth, **meta)


def notice(stem, title, url, lang="en", auth="it", **meta):
    return register("milan-" + stem, title, url, SNAP / "sources" / ("milan-" + stem + ".pdf"), SNAP / "extracted" / ("milan-" + stem + ".md"), lang, auth, **meta)


def part(source_id, pages=None, start=None, end=None, article=None, path=None, locator=None):
    x = {"source_id": source_id, "kind": "pdf_pages" if pages else "article" if article else "structured" if path and str(path).endswith(".json") else "text",
         "locator": locator or (f"PDF pages {pages}" if pages else f"Article {article}" if article else "Reviewed structured derivative")}
    for k, v in [("pages", pages), ("start", start), ("end", end), ("article", article)]:
        if v is not None:
            x[k] = v
    if path:
        x["path"] = rel(ROOT / path)
        x["derivative_sha256"] = sha(ROOT / path)
    return x


def add(id, title, extracts, topics, entities, *, services=None, modes=None, roles=None, notes=None, deps=None, required=None,
        effective=None, effective_to=None, publication_description=False, platform_release=None, subject_release=None, **extra):
    basis = "reviewed_effective_interval" if effective else "publication_description" if publication_description else "reference_description"
    modes = modes or ["current"]
    if "current" in modes and not effective and not extra.get("event_scope"):
        assert publication_description, id + ": current admission needs an effective interval or an explicit publication-description basis"
    SECTIONS.append({"id": id, "title": title, "decision": "admit", "verified_as_of": D, "entities": entities,
                     "services": services or ["settlement"], "roles": roles or ["participant", "csd_operator"], "modes": modes,
                     "question_types": topics, "extracts": extracts, "dependency_ids": deps or [], "required_context": required or [],
                     "effective_from": effective, "effective_to": effective_to,
                     "applicability_rule": "Verified knowledge snapshot only; earlier/later applicability requires a separate reviewed decision. Event business dates are separately scoped.",
                     "review_depth": "Specified excerpts read on 2026-09-14; not whole-document certification", "permitted_use": title,
                     "limitations": notes or [], "security_link_context": "No individual ISIN, entitlement, account or custody chain is certified",
                     "platform_release": platform_release, "subject_release": subject_release, "applicability_basis": basis, **extra})


def main():
    config_path = ROOT / "retrieval/section-decisions.json"
    config = json.loads(config_path.read_text())
    if config.get("snapshot_revision") == REVISION:
        raise SystemExit("Settlement-agent snapshot already recorded; review later changes explicitly.")
    register_path = ROOT / "retrieval/source-register.json"
    existing = json.loads(register_path.read_text())
    before = SNAP / "before"
    before.mkdir(parents=True, exist_ok=True)
    for name in ["retrieval/section-decisions.json", "retrieval/source-register.json", "retrieval/build-manifest.json",
                 "retrieval/admitted-sections.jsonl", "retrieval/README.md", "curated-manifest.json", "metadata/legal-browser-sources.json",
                 "reviewed-evidence-pack.zip"]:
        dest = before / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copyfile(ROOT / name, dest)
    for p in (ROOT / "retrieval/exports").rglob("*.jsonl"):
        dest = before / p.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copyfile(p, dest)

    # ---------------------------------------------------------------- sources
    T = "aa3d5a3b94c9"          # June UDFS (already registered)
    M = "8719262f5e8b"          # Milan Service Regulations (already registered)
    EU = "02014R0909-20260117"  # CSDR consolidated (already registered)
    SI = from_catalogue("dd1cf7cb930b", auth="it", document_version="Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025)", effective_from="2025-06-30",
                        date_evidence="Cover: 30 June 2025; Market Notice MN_10/2025 of 18 June 2025 gives entry into force on 30 June 2025.",
                        quarantine_note="PDF 12-16 operational-day clock values (NTS 19:30, two partial windows) remain quarantined: they conflict with the deployed R2026.JUN T2S schedule.")
    GW = from_catalogue("1bd67deaace2", document_version="T2S Gateway settlement links, valid from 1 May 2026", effective_from="2026-05-01",
                        date_evidence="Cover: valid from May 1st 2026; page footers read PRIVATE although the file is published on the public T2S Gateway page.")
    CC = from_catalogue("d548b6c97bae", lang="it", document_version="Client configurations for settlement in T2S, September 2026 edition", date_evidence="Hub date 07/09/2026; document states it replaces previous versions.")
    CP2 = from_catalogue("cbdf3c1f8b51", document_version="Rule Book Part 2, cover 3 August 2026; footer version labels 12/13 conflict", date_evidence="Cover 3 August 2026; effective date not stated on the reviewed pages.")
    ON36 = from_catalogue("de2d312169fc", document_version="ON_36/2026, 11 September 2026", date_evidence="Notice dated 11 September 2026; planned changes 30 November 2026 subject to testing.")
    SDR = legal("02018R1229-20240902", document_version="Consolidated 2 September 2024", date_evidence="EUR-Lex consolidation 02018R1229-20240902; browser capture 11 September 2026; language check: English.")
    SFD = legal("01998L0026-20240408", document_version="Consolidated 8 April 2024", date_evidence="EUR-Lex consolidation 01998L0026-20240408; browser capture 11 September 2026; language check: English.")
    RTS392 = register("32017R0392-en-article1", "Commission Delegated Regulation (EU) 2017/392 — English OJ text, Article 1 definitions (browser excerpt)",
                      "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0392",
                      SNAP / "sources/32017R0392-EN-article1-browser-excerpt.txt", SNAP / "sources/32017R0392-EN-article1-browser-excerpt.txt",
                      "en", "EU official languages", document_version="OJ L 65, 10.3.2017", publication_date="2017-03-10",
                      date_evidence="OJ publication 10 March 2017; excerpt captured 14 September 2026 through the in-app browser (full-page innerText SHA-256 recorded alongside).",
                      provenance_note="Partial browser capture: preamble end to Article 2 only. The library's consolidated capture 02017R0392-20170310 contains German text and is not used for English quotation.")
    ECB = register("ecb-status-2026-20260914", "ECB T2S status history 2026 (capture of 14 September 2026)",
                   "https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html",
                   SNAP / "hubs/ecb-t2s-status-2026.html", SNAP / "extracted/ecb-t2s-status-2026.txt", date_evidence="Captured 14 September 2026; page lists entries up to 14/09/2026 02:30.")
    PW = register("porto-working-days-20260914", "Euronext Securities Porto — Working Days & Operating hours (web page, capture of 14 September 2026)",
                  "https://www.euronext.com/en/post-trade/euronext-securities/porto/about-us/working-days-operating-hours",
                  SNAP / "hubs/porto-working-days.html", SNAP / "extracted/porto-working-days.txt", date_evidence="Captured 14 September 2026; page states hours follow Notice 0394/2024 and lists CET values with a WET note.")
    NOVF = register("ecb-november-final-udfs-fulltext-20260914", "T2S User Detailed Functional Specifications R2026.NOV (UDFS) — full-text derivative",
                    "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0",
                    ROOT / "implementation/2026-09-14/sources/november-final-udfs.pdf", SNAP / "extracted/november-final-udfs-full.md", "en", "en",
                    document_version="R2026.NOV final publication (11 September 2026); deployment not verified", publication_date="2026-09-14", revision_date="2026-09-11",
                    provenance_note="Same original bytes as ecb-november-final-udfs-20260914; this identity binds the full pdftotext derivative used for the selected future-release sections and the June/November text comparison.")
    N = {}
    for stem, title, url, kw in [
        ("on-t2s-r2026jun-production", "ON_20/2026 T2S Release R2026.JUN – Production release (11 June 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON%20T2S%20RELEASE%20R2026.JUN%20PROD_RevPP_10062026_ENG.pdf", dict(publication_date="2026-06-11")),
        ("on-t2s-r2026jun-utest", "ON_09/2026 T2S Release R2026.JUN – Release in UTEST (27 March 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/T2S%20R2026.JUN%20-%20rilascio%20in%20UTEST%20ENG_Rev.pdf", dict(publication_date="2026-03-27")),
        ("on-t2s-r2026nov-nonbinding-xsds", "ON_28/2026 T2S Release R2026.NOV and non-binding XSDs (21 July 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/T2S%20R2026.NOV%20e%20Non-binding%20XSDs%20V0.1%20rev%20OPP_ENG.pdf", dict(publication_date="2026-07-21")),
        ("on-t2s-r2026nov-binding-xsds", "Operational notice: T2S Release R2026.NOV and binding XSDs (dated 10 August 2026, hub date 07/08/2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/T2S%20R2026.NOV%20-%20binding%20XSDs%20V0.1%20ENG.pdf", dict(publication_date="2026-08-10", date_evidence="Letter dated 10 August 2026; hub lists 07/08/2026; PDF creation 10 August 2026. Notice number not printed.")),
        ("on-mtx-tls13", "ON_35/2026 MT-X access: enabling TLS 1.3 in production (10 September 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/Euronext%20Securities%20Milan%20OPS%20Notice_accesso_MTX_eng_0.pdf", dict(publication_date="2026-09-10")),
        ("on-repo-settlement-messages", "ON_27/2026 Update to settlement messages for repo transactions (21 July 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_Informativa%20Settlement_v0.2_ENG.pdf", dict(publication_date="2026-07-21", effective_from="2026-07-20")),
        ("on-swift-annual-release-2026", "ON_30/2026 SWIFT Annual Release 2026 (24 July 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_SWIFT%20Annual%20Release%202026_ENGv1.pdf", dict(publication_date="2026-07-24")),
        ("on-may1-business-day-2026", "ON_13/2026 May 1st as a business day: impact on ES-MIL systems (24 April 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_primo_maggio_eng_2026_0.pdf", dict(publication_date="2026-04-24")),
        ("on-participation-requirements-2026", "ON_12/2026 Confirmation of requirements for participation (21 April 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/TF-ALC2404010v-EN-lf-conferma_requisiti_partecipazione%20_2.pdf", dict(publication_date="2026-04-21")),
        ("on-cab-account-fields-t2s-payers", "ON_04/2026 Introduction of CAB and Account Number fields for T2S payers (6 February 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON%20042026%20ENG.pdf", dict(publication_date="2026-02-06", effective_from="2026-02-09")),
        ("on-unfreeze-iso20022-spu", "ON_11/2026 Update Standards for XTRM Users in A2A and RNI mode (10 April 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_Unfreeze%20ISO%2020022_Clearing%20Migration_ENG_v4_0.pdf", dict(publication_date="2026-04-10")),
        ("on-penalties-calendar-2026", "ON_01/2026 Penalties Calendar 2026 (8 January 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/Penalties%20Calendar_2026_ENG.pdf", dict(publication_date="2026-01-08")),
        ("on-securities-migration-3107", "ON_31/2026 Securities migration on 23 September 2026 (31 July 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/EE_ON%20pubblicazione_31.07%20v.%200.1%20ENG_1.pdf", dict(publication_date="2026-07-31")),
        ("mn-european-offering-golive", "MN_07/2026 Euronext European Offering: go-live confirmation (8 September 2026)", "https://www.euronext.com/sites/default/files/notices/monte-titoli/20260903%20Euronext%20Securities%20Milan%20Market%20Notice%20-%20EE_0.pdf", dict(publication_date="2026-09-08")),
    ]:
        N[stem] = notice(stem, title, url, **kw)
    NOTICE_NOTE = "Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication."

    # ------------------------------------------------------------- T2S (June UDFS, re-verified pages)
    tcsds = ["T2S", "Milan", "Copenhagen", "Porto"]
    T2S_NOTE = "T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline."
    add("t2s-schedule-r2", "Baseline day phases and preceding-day/event dependencies (14 September re-verification)",
        [part(T, [156, 157, 158], "1.4.2 T2S schedule", "1.4.3 Overview", locator="§1.4.2 and exception conditions; PDF 156–158"),
         part(T, [160, 161, 162, 163], end="1.4.4 Detailed description", locator="Table 37; PDF 160–163"),
         part(T, [163], "1.4.4.1 Start of day", "1.4.4.1.1", locator="§1.4.4.1; PDF 163")],
        ["t2s_baseline_schedule", "business_day_timeline", "dated_t2s_schedule"], ["T2S"], effective="2026-06-14", platform_release="R2026.JUN", schedule_model="T2S",
        notes=["Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026.", "CET is the source convention; no UTC conversion.",
               "Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date."])
    add("t2s-nts-processing", "Night-time settlement processing: cycles, sequences and reporting", [part(T, [167, 168, 169], "1.4.4.2 Night-time settlement (NTS)", "1.4.4.2.1 Application processes", locator="§1.4.4.2 NTS processing and reporting; PDF 167–169")],
        ["t2s_nts_processing"], ["T2S"], effective="2026-06-14", platform_release="R2026.JUN", schedule_model="T2S",
        notes=["Cycle durations are volume dependent; the 22:20/00:00 targets are objectives, not commitments.", T2S_NOTE])
    add("t2s-rts-phase", "Real-time settlement period: five partial settlement windows and cut-off structure", [part(T, [193, 194], "1.4.4.4 Real-time settlement (RTS)", "1.4.4.4.1 Application processes", locator="§1.4.4.4; PDF 193–194")],
        ["t2s_partial_windows_and_cutoffs"], ["T2S"], effective="2026-06-14", platform_release="R2026.JUN", schedule_model="T2S",
        notes=["Window times are the R2026.JUN baseline (08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, 15:30 to 16:05 or DVP cut-off closure); some cut-offs are currency dependent.", "A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly."])
    add("t2s-validation", "Business validation concept and overview", [part(T, [218, 219], "1.6.1.1 Business Validation", "1.6.1.1.3 Validation process", locator="§1.6.1.1.1–1.6.1.1.2; PDF 218–219")],
        ["t2s_validation_concept"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Validation rule catalogue (§1.6.1.1.3 onwards) and CSD-specific restriction rules are not admitted.", T2S_NOTE])
    add("t2s-allegement", "Allegement process and standard delay parameters", [part(T, [271, 272, 273, 274, 275, 276, 277], "1.6.1.3 Allegement", "1.6.1.4 Instruction Amendment", locator="§1.6.1.3 including Table of parameters (1 hour / 5 hours); PDF 271–277")],
        ["t2s_allegement_rules"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Parameter values are the T2S Operator defaults printed in the UDFS; local CSDs relay allegements through their own channels (see local sections).", T2S_NOTE])
    add("t2s-amendment", "Instruction amendment: permitted process indicators and denial conditions", [part(T, [277, 278, 279, 280], "1.6.1.4 Instruction Amendment", "1.6.1.5 Instruction Cancellation", locator="§1.6.1.4 with Tables 58–59; PDF 277–280")],
        ["t2s_instruction_amendment"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=[T2S_NOTE])
    add("t2s-cancellation", "Instruction cancellation: bilateral cancellation, CoSD cancellation and system cancellation", [part(T, [280, 281, 282, 283, 284], "1.6.1.5 Instruction Cancellation", "1.6.1.6 Hold and Release", locator="§1.6.1.5 with Table 60 and footnote 195; PDF 280–284")],
        ["t2s_cancellation_process"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Local legal effects of cancellation (e.g. Milan Article 70) are separate sections at their own review date.", T2S_NOTE])
    add("t2s-hold-release", "Hold and release: indicators, exhaustive scenarios, hold/release default and partial release",
        [part(T, [284, 285, 286, 287, 288, 289], "1.6.1.6 Hold and Release", locator="§1.6.1.6.1–1.6.1.6.3 with Tables 61–62 and footnotes 196–197; PDF 284–289"),
         part(T, [292, 293, 294, 295], "1.6.1.6.5 Hold/Release Default", "1.6.1.6.7 Parameters Synthesis", locator="§1.6.1.6.5–1.6.1.6.6 partial release conditions; PDF 292–295")],
        ["t2s_hold_release_process"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["The release process narrative (§1.6.1.6.4, PDF 290–291) is not admitted.", T2S_NOTE])
    add("t2s-recycling", "Instruction recycling periods (20 and 60 working days) and automatic cancellation", [part(T, [296, 297, 298, 299], "1.6.1.7 Instructions Recycling", "The following examples consider", locator="§1.6.1.7 with footnotes 199–200; PDF 296–299")],
        ["t2s_recycling_periods"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["External-CSD exception to automatic cancellation is stated; individual configurations are not certified.", T2S_NOTE])
    add("t2s-partial-settlement", "Partial settlement conditions, thresholds and procedure", [part(T, [343, 344, 345], "1.6.1.9.3 Partial Settlement", locator="§1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345")],
        ["t2s_partial_settlement"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Cash-value thresholds are configured per currency by the T2S Operator; actual values are not in this excerpt.", T2S_NOTE])
    add("t2s-linked-instructions", "Linked instructions: BEFO/AFTE/WITH links, pools and T2S-generated links", [part(T, [442, 443, 444], "1.6.1.11 Linked Instructions", locator="§1.6.1.11.1–1.6.1.11.3 with footnote 243; PDF 442–444")],
        ["t2s_linked_instructions"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Table 71 validation rules for links (PDF 448) are not admitted.", T2S_NOTE])
    add("t2s-conditional-settlement", "Conditional settlement (CoSD): concept and overview", [part(T, [452, 453, 454], "1.6.1.12 Conditional Settlement", "1.6.1.12.3 Conditional settlement process", locator="§1.6.1.12.1–1.6.1.12.2 with footnote 253; PDF 452–454")],
        ["t2s_conditional_settlement"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["CoSD rules are CSD-specific static data; none is admitted.", T2S_NOTE])
    add("t2s-status-management", "Status management: statuses, reason codes and communication principles", [part(T, [653, 654, 655, 656], "1.6.3 Information Management", locator="§1.6.3.1.1–1.6.3.1.3 and the list of Settlement Instruction statuses; PDF 653–656")],
        ["t2s_status_model"], tcsds, effective="2026-06-14", platform_release="R2026.JUN", notes=["Status transition diagrams and the reason-code catalogue are not admitted.", T2S_NOTE])
    add("t2s-sese023-scope", "sese.023.001.11 Settlement Instruction: scope and building blocks", [part(T, [1233, 1234], "3.3.6.4 SecuritiesSettlementTransactionInstructionV11", "Businessrulesapplicabletotheschema", locator="§3.3.6.4.1–3.3.6.4.2 outline of the schema; PDF 1233–1234")],
        ["t2s_message_sese023_scope"], tcsds, required=["release"], effective="2026-06-14", platform_release="R2026.JUN",
        notes=["Business rules table (PDF 1235 onwards) and message examples are not admitted; the T2S-specific schema is published on MyStandards, which requires an account.", "This is the CSD/DCP-to-T2S message, not a bank-to-CSD interface."])
    add("t2s-sese024-usages", "sese.024.001.12 Status Advice: scope and hold-related message usages", [part(T, [1257, 1258], "3.3.6.5 SecuritiesSettlementTransactionStatusAdviceV12", locator="§3.3.6.5.1 with footnotes 417–424; PDF 1257–1258")],
        ["t2s_message_sese024_usages"], tcsds, required=["release"], effective="2026-06-14", platform_release="R2026.JUN",
        notes=["Only the usages printed on these pages are admitted; the complete usage list continues beyond PDF 1258.", "Local relays of statuses to ICPs are service dependent."])

    # ---------------------------------------------------------- dated ECB events (14 September capture)
    ev_dir = SNAP / "structured/ecb-events-2026"
    for f in sorted(ev_dir.glob("2026-*.json")):
        rec = json.loads(f.read_text())
        bd = rec["business_date"]
        add(f"t2s-events-{bd}", f"ECB status entries attributed to {bd} ({rec['schedule_impact']})",
            [part(ECB, path=f, locator=f"ECB T2S status history, entries listed in the derivative for {bd}; capture of 14 September 2026")],
            ["dated_t2s_schedule"], ["T2S"], required=["business_date", "currency"], deps=["t2s-schedule-r2"],
            event_scope={"schedule_model": "T2S", "business_date": bd, "currency": "ALL"},
            notes=["Entries are not currency-specific unless the text names a currency (recorded per entry); scope ALL applies to the operating day as a whole.",
                   "Business-date attribution of evening entries follows a labelled inference from the UDFS schedule; the displayed calendar date and time are preserved.",
                   "An announced change is not proof of an individual transaction's execution time."] + (["Calendar date falls on a weekend; the entries concern closure or maintenance, not a settlement day."] if not rec["is_weekday"] else []))
    routine = ev_dir / "routine-only-dates.json"
    add("t2s-status-routine-2026", "T2S business dates with only routine ECB status entries (14 September capture)",
        [part(ECB, path=routine, locator="Derived list of weekday business dates with routine-only entries; capture of 14 September 2026")],
        ["dated_t2s_schedule"], ["T2S"], required=["business_date", "currency"], deps=["t2s-schedule-r2"],
        event_scope={"schedule_model": "T2S", "business_dates": json.loads(routine.read_text())["business_dates"], "currency": "ALL"},
        notes=["Supports only the proposition that no incident or schedule change was published on the status page for that date; it does not prove every event ran exactly on time.",
               "Weekday public holidays appear only if the page carried a routine entry for them; check the T2S calendar separately."])

    # ---------------------------------------------------------- November release (future) and text comparison
    NOV_NOTE = ["R2026.NOV is a published future release: Milan's notices plan production deployment on 14 November effective 16 November 2026; deployment is not verified.", "Only the listed pages are admitted; the release's change requests and other sections are unreviewed."]
    add("november-matching-text", "R2026.NOV UDFS matching section (published future release text)", [part(NOVF, [279, 280, 281, 282, 283], "3.6.1.2 Matching", "3.6.1.3 Allegement", locator="§3.6.1.2; PDF 279–283 of the R2026.NOV clean UDFS")],
        ["november_matching_text"], ["T2S"], modes=["future", "reference"], required=["release"], subject_release="R2026.NOV", notes=NOV_NOTE)
    add("november-posting-text", "R2026.NOV UDFS posting concept and overview (published future release text)", [part(NOVF, [317, 318, 319, 320], "3.6.1.8 Posting", "3.6.1.8.3 Eligibility check process", locator="§3.6.1.8.1–3.6.1.8.2; PDF 317–320")],
        ["november_posting_text"], ["T2S"], modes=["future", "reference"], required=["release"], subject_release="R2026.NOV", notes=NOV_NOTE)
    add("november-realignment-text", "R2026.NOV UDFS realignment concept and reference data (published future release text)", [part(NOVF, [393, 394, 395, 396], "3.6.1.10 Realignment", "The following example illustrates", locator="§3.6.1.10.1–3.6.1.10.3 opening; PDF 393–396")],
        ["november_realignment_text"], ["T2S"], modes=["future", "reference"], required=["release"], subject_release="R2026.NOV", notes=NOV_NOTE)
    add("november-text-comparison", "June versus November UDFS: normalised sentence comparison of selected settlement sections",
        [part(NOVF, path=SNAP / "structured/udfs-jun-vs-nov-delta.json", locator="Derived comparison of the June and November clean UDFS texts (method and limits inside)")],
        ["november_text_comparison"], ["T2S"], modes=["reference", "future"], subject_release="R2026.NOV",
        notes=["A derivative produced by the library maintainer, not ECB text: textual comparison after normalisation; diagrams and image tables are not compared; residual differences listed are formatting artefacts unless stated otherwise.",
               "No sentence-level substantive change was detected in the compared ranges (matching, allegement, amendment, cancellation, hold/release, recycling, posting overview, partial settlement, realignment concept, linked, CoSD, status management, schedule, RTS phase, validation, NTS processing). The realignment sentence flagged by the diff exists in both texts with a line-break difference.",
               "The comparison does not review the change requests actually delivered by R2026.NOV; Milan lists 11 change requests and six defects in ON_28/2026."])

    # ---------------------------------------------------------- Milan Service Regulations (26 January 2026)
    MREG_NOTE = "Italian text prevails (cover, PDF 1). English translation excerpt."
    add("milan-settlement-characteristics", "Settlement Service characteristics, participant categories and indirect participants (Articles 58–59)", [part(M, [41, 42, 43, 44], "Article 58", "Article 60", locator="Articles 58–59; PDF 41–44, printed 40–43")],
        ["milan_settlement_scope_and_participants"], ["Milan"], effective="2026-01-26", notes=[MREG_NOTE, "Categories are legal admission categories; a firm's own eligibility requires its facts."])
    add("milan-agent-bank-penalties", "Agent banks, penalty mechanism and suspension of systematically failing participants (Articles 62–63-bis)", [part(M, [45, 46, 47], "Article 62", "Article 64", locator="Articles 62, 63 and 63-bis; PDF 45–47, printed 44–46")],
        ["milan_agent_bank_and_penalties"], ["Milan"], effective="2026-01-26", notes=[MREG_NOTE, "Penalty rates and the SDR calculation itself are not in this excerpt; procedural deadlines are in the Instructions section milan-penalties-procedure."])
    add("milan-conduct-instruments-notices", "Rules of conduct, admitted instruments, service information notices and reference to the T2S URD (Articles 64–67)", [part(M, [47, 48, 49], "Article 64", "Article 68", locator="Articles 64–67; PDF 47–49, printed 46–48")],
        ["milan_instruments_notices_urd"], ["Milan"], effective="2026-01-26", notes=[MREG_NOTE, "Article 66 delegates calendar/operating hours to service notices and Article 67(2) defers functioning to the T2S User Requirements; the notice that restates participant cut-offs after R2026.JUN was not located publicly (see gap G01)."])
    add("milan-instruction-processing", "Acquisition, validation, linked/CoSD instructions, partial settlement, priority, collateral, processing phases and CAoF (Articles 68, 73–76)",
        [part(M, [49, 50], "Article 68", "Article 69", locator="Article 68; PDF 49–50, printed 48–49"), part(M, [52, 53], "Article 73", locator="Articles 73–76; PDF 52–53, printed 51–52")],
        ["milan_instruction_processing_rules"], ["Milan"], effective="2026-01-26", notes=[MREG_NOTE, "Articles 69–72 (matching, cancellation, hold, finality) are the 13 September section milan-finality."])
    add("milan-cross-csd-disclosure", "Cross-CSD settlement rule and disclosure of settlement progress (Articles 77–78)", [part(M, [54], "Article 77", "TITLE IV", locator="Articles 77–78 with footnote 8; PDF 54, printed 53")],
        ["milan_cross_csd_rule"], ["Milan"], effective="2026-01-26", notes=[MREG_NOTE, "Article 77(2) excludes cross-CSD settlement when the issuer CSD is outside T2S unless both investor CSDs hold a link avoiding realignment with it; actual links per ISIN are not certified."])

    # ---------------------------------------------------------- Milan Settlement Service Instructions (30 June 2025)
    SI_NOTE = "Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source."
    add("milan-connectivity-static-data", "Connectivity models, static data, LEI, indirect participants, account/DCA structure and updating operating conditions (§§1.1–1.2.3)", [part(SI, [7, 8, 9, 10], "1. IMPLEMENTING PROVISIONS", "1.2.4 Fees and procedures", locator="§§1.1–1.2.3; PDF 7–10, printed 3–6")],
        ["milan_connectivity_and_static_data"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "CLIMP procedures and forms themselves are not admitted; the mdm@lseg.com address is as printed in the 30 June 2025 edition."])
    add("milan-service-scope", "Settlement Service scope: intra-CSD and cross-CSD, ICP versus DCP processing (§1.3 excluding the operational-day clock table)", [part(SI, [12], "1.3 OPERATION OF THE SETTLEMENT SERVICE", "1.3.1 Operational Day", locator="§1.3 opening; PDF 12, printed 8")],
        ["milan_settlement_service_scope"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "§1.3.1 (PDF 12–16) is quarantined: its clock values (NTS 19:30, two partial windows) conflict with the deployed R2026.JUN schedule; use the T2S schedule sections and the notice chain instead."])
    add("milan-caof", "Corporate actions on flow: market claims and transformations (§1.4)", [part(SI, [17, 18, 19, 20, 21, 22, 23, 24, 25], "1.4 MANAGEMENT OF OPERATIONS IN CASE OF CORPORATE", "1.5 PENALTY SYSTEM", locator="§1.4 including footnotes 4–5; PDF 17–25, printed 13–21")],
        ["milan_market_claims_transformations"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Buyer protection references market practice and market/CCP rules, which are not admitted."])
    add("milan-penalties-procedure", "Penalty procedure deadlines, collection/redistribution and automatic cancellation of instructions (§§1.5–1.6)", [part(SI, [25, 26, 27], "1.5 PENALTY SYSTEM", locator="§§1.5–1.6; PDF 25–27, printed 21–23")],
        ["milan_penalty_procedure_auto_cancellation"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Deadlines are expressed in penalties business days; the dated 2026 calendar is the section milan-penalties-calendar-2026."])
    add("milan-external-settlement", "Foreign Settlement Service (external settlement): channels, cancellation, pre-positioning/pre-funding with CoSD, routing and reporting (Title 2)", [part(SI, [28, 30, 31, 32, 33, 34, 35], "2 IMPLEMENTING PROVISIONS OF", locator="Title 2 §§2.1–2.3.6 (PDF 29 is blank); PDF 28–35, printed 24–31")],
        ["milan_external_settlement"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Per-system Operating Documents and their cut-offs are not admitted."])
    add("milan-xtrm-service", "X-TRM service: operation, communications and access methods (§§3.1–3.4 opening, with the access-method table transcribed from the page image)",
        [part(SI, [36, 37, 38], "3 IMPLEMENTING PROVISIONS OF THE", locator="§§3.1–3.4.1 opening; PDF 36–38, printed 32–34"),
         part(SI, path=SNAP / "structured/milan-xtrm-access-methods.json", locator="§3.3 access-method table, transcribed from the rendered PDF 37 (text extraction column-garbled)")],
        ["milan_xtrm_service_access"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Message codes (G50–G58, MT540–MT548, MT598) are listed as printed; their layouts are in the client-only Standard for X-TRM Users."])
    add("milan-xtrm-field-mapping", "X-TRM fields versus T2S fields: mandatory, additional and optional matching information (§3.4.1 Table 2, transcribed from the page images)",
        [part(SI, [39, 40, 41], "Operations must contain", "3.4.2 Validation in X-TRM Service", locator="§3.4.1 Table 2 and additional information list; PDF 39–41, printed 35–37"),
         part(SI, path=SNAP / "structured/milan-xtrm-t2s-field-mapping.json", locator="Table 2 transcription from rendered PDF 39–41 with recorded anomalies")],
        ["milan_xtrm_field_mapping"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Functional correspondence only: not the A2A/RNI message layouts, not a T2S XSD, and two source cells are truncated in the original layout (recorded).", "Footnote (1) referenced in the table was not located on the reviewed pages."])
    add("milan-xtrm-lifecycle", "X-TRM lifecycle for T2S-settled transactions: validation, enrichment, doubling, routing, allegement disclosure, maintenance (modify/cancel/hold-release) and reporting (§§3.4.2–3.4.8)", [part(SI, [41, 42, 43, 44, 45, 46, 47, 48], "3.4.2 Validation in X-TRM Service", "3.5 FUNCTIONALITY OF THE X-TRM SERVICE FOR TRANSACTIONS", locator="§§3.4.2–3.4.8; PDF 41–48, printed 37–44")],
        ["milan_xtrm_lifecycle_maintenance"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Market/CCP-specific maintenance permissions are published in Service Notices, which are not admitted."])
    add("milan-default-procedure", "Default management procedure: notification, blocks, cancellation table and cross-CSD hold (Title 4)", [part(SI, [71, 72, 73, 74, 75], "4 DEFAULT MANAGEMENT PROCEDURE", locator="Title 4 §§4–4.4; PDF 71–75, printed 67–71")],
        ["milan_default_procedure"], ["Milan"], effective="2025-06-30", notes=[SI_NOTE, "Cross-references to Article 57/59 numbering reflect the 2025 Instructions; the 2026 Regulations renumbered articles (e.g. Article 59 categories)."])

    # ---------------------------------------------------------- Milan operational documents and notices
    add("milan-gateway-links-guide", "T2S Gateway settlement links guide: link inventory (MT23 codes), how to identify the issuer CSD and instruction rules", [part(GW, [2, 3, 4, 5, 6, 7, 8, 9], "TABLE OF CONTENTS", locator="Table of contents, Introduction, §1 and §1.1.1 notes; PDF 2–9")],
        ["milan_cross_csd_link_guide"], ["Milan"], effective="2026-05-01", notes=["Route-specific SWIFT/XTRM templates (PDF 10–109) are not admitted; the index proves which issuer-CSD/counterparty combinations the guide covers on 1 May 2026, not per-ISIN eligibility.", "Document footers read PRIVATE although the file is on the public T2S Gateway page; ES-MIL disclaims responsibility for instruction correctness."])
    add("milan-party2-rule", "Client configurations for T2S settlement: Party 2 BIC population rule (header note of the September 2026 list)", [part(CC, [1], "(*) Se il Codice CED", "NEGOZIATORE/", locator="Bilingual header note; PDF 1")],
        ["milan_party2_configuration_rule"], ["Milan"], publication_description=True, notes=["Static-data list dated 7 September 2026 that replaces previous versions; the per-participant rows (BIC, CED/ABI codes, SAC T2S accounts) are not admitted.", "Bilingual Italian/English note; the Italian and English texts were both read."])
    add("milan-r2026jun-production", "R2026.JUN production release confirmed (12 June, effective 15 June 2026) and final X-TRM standards VER.01.09", [part(N["on-t2s-r2026jun-production"], [1, 2], locator="ON_20/2026 PDF 1–2")],
        ["milan_t2s_release_deployment"], ["Milan"], modes=["current", "reference"], effective="2026-06-15", subject_release="R2026.JUN",
        notes=[NOTICE_NOTE, "The ECB status page separately records deployment completion on 14 June 2026 (see t2s-events-2026-06-14).", "The named X-TRM standards live in MT-X (client platform) and are not in the library."])
    add("milan-r2026jun-utest", "R2026.JUN test plan: UTEST availability, test window and planned production dates (ECB statement relayed by Milan)", [part(N["on-t2s-r2026jun-utest"], [1, 2], locator="ON_09/2026 PDF 1–2")],
        ["milan_t2s_release_test_plan_jun"], ["Milan"], modes=["reference"], subject_release="R2026.JUN", notes=[NOTICE_NOTE, "Historical planning notice; the production release was later confirmed by ON_20/2026."])
    add("milan-r2026nov-plan", "R2026.NOV plan: UTEST from 28 September, tests to 28 October, production deployment planned 14 November effective 16 November 2026, XSD documentation in MT-X",
        [part(N["on-t2s-r2026nov-nonbinding-xsds"], [1, 2], locator="ON_28/2026 PDF 1–2"), part(N["on-t2s-r2026nov-binding-xsds"], [1, 2], locator="Binding-XSD notice of 10 August 2026, PDF 1–2")],
        ["milan_t2s_release_plan_nov"], ["Milan"], modes=["future", "reference"], subject_release="R2026.NOV",
        notes=[NOTICE_NOTE, "Planned dates are not deployment evidence; ON_28 page 2 contains an internal inconsistency ('from Tuesday 29 April' for UTEST re-tests) preserved as printed.", "The MyStandards XSD documentation is client-only."])
    add("milan-mtx-tls13", "MT-X access: TLS 1.3 and outbound port 8443 required in production from 26 October 2026", [part(N["on-mtx-tls13"], [1], locator="ON_35/2026 PDF 1")],
        ["milan_mtx_connectivity_change"], ["Milan"], modes=["future"], notes=[NOTICE_NOTE, "Scheduled go-live, not a completed change."])
    add("milan-repo-comm-field", "Common reference field population for repo settlement instructions from 20 July 2026 (Euronext Clearing, relayed by Milan)", [part(N["on-repo-settlement-messages"], [1], locator="ON_27/2026 PDF 1")],
        ["milan_settlement_message_field_change"], ["Milan"], effective="2026-07-20", notes=[NOTICE_NOTE, "Field :20C::COMM// / <CmonId> population is a CCP behaviour reflected in Milan settlement information; it is not a change to matching rules."])
    add("milan-swift-sr2026", "SWIFT Annual Release 2026: change requests implemented by ES-MIL, 16 November 2026 go-live and 5 October 'future mode'", [part(N["on-swift-annual-release-2026"], [1, 2, 3], locator="ON_30/2026 PDF 1–3")],
        ["milan_swift_release_2026"], ["Milan"], modes=["future"], notes=[NOTICE_NOTE, "Mostly corporate-action and meeting messages; the only settlement item is CR 003149 (semt.014 intra-position reason codes)."])
    add("milan-may1-2026", "1 May 2026 treated as a business day: T2S open for FOP only in EUR, T2 closed, X-TRM limitations and custody impacts", [part(N["on-may1-business-day-2026"], [1, 2, 3, 4, 5, 6], locator="ON_13/2026 PDF 1–6")],
        ["milan_calendar_exception"], ["Milan"], required=["business_date", "payment_type"], effective="2026-05-01", effective_to="2026-05-01",
        calendar_scope={"from": "2026-05-01", "to": "2026-05-01", "payment_types": ["FOP", "DVP", "PFOD"]},
        notes=[NOTICE_NOTE, "Applies to 1 May 2026 only; impact tables are reproduced from a layout-heavy PDF and should be read against the original for row alignment."])
    add("milan-participation-confirmation", "Annual confirmation of participation requirements and duty to notify changes (ON_12/2026)", [part(N["on-participation-requirements-2026"], [1, 2], locator="ON_12/2026 PDF 1–2")],
        ["milan_participation_requirement_notification"], ["Milan"], modes=["reference"], notes=[NOTICE_NOTE, "Reminder of contractual duties; the General Conditions themselves are not admitted."])
    add("milan-cab-account-fields", "Optional CAB and Account Number fields in MT-X instructions for T2S payers from 9 February 2026", [part(N["on-cab-account-fields-t2s-payers"], [1], locator="ON_04/2026 PDF 1")],
        ["milan_mtx_payment_fields"], ["Milan"], effective="2026-02-09", notes=[NOTICE_NOTE, "Concerns issuer payment instructions in MT-X, not settlement instruction matching."])
    add("milan-xtrm-standard-versions", "Standard for XTRM Users (A2A and RNI): VER.01.09 under review in April 2026 and the 11 September 2026 update for Vorvel, Certificates TLX and IPO markets",
        [part(N["on-unfreeze-iso20022-spu"], [1, 2], locator="ON_11/2026 PDF 1–2"), part(ON36, [1], locator="ON_36/2026 PDF 1")],
        ["milan_xtrm_standard_versions"], ["Milan"], modes=["reference", "future"], notes=[NOTICE_NOTE, "Identifies document titles, versions and MT-X folders only; the standards' content is client-only (gap G03).", "ON_36/2026 planned changes take effect 30 November 2026 subject to testing."])
    add("milan-penalties-calendar-2026", "Penalties calendar 2026: appeal closing, monthly report dispatch and PFOD payment dates", [part(N["on-penalties-calendar-2026"], [1, 2], locator="ON_01/2026 PDF 1–2")],
        ["milan_penalties_calendar"], ["Milan"], effective="2026-01-08", effective_to="2027-01-27", notes=[NOTICE_NOTE, "Dates may change on ECSDA instruction, as the notice states."])
    add("milan-securities-migration-sep23", "ETP issuer-CSD migration on 23 September 2026 and handling of pending cross-CSD/external instructions", [part(N["on-securities-migration-3107"], [1, 2], locator="ON_31/2026 PDF 1–2")],
        ["milan_securities_migration_event"], ["Milan"], modes=["future"], notes=[NOTICE_NOTE, "The ISIN list referenced by the notice is not admitted."])
    add("milan-european-offering-golive", "European Offering go-live confirmed for 21 September 2026: scope, MICs, alternative CSD choice and first ISD 23 September", [part(N["mn-european-offering-golive"], [1, 2], locator="MN_07/2026 PDF 1–2")],
        ["european_offering_go_live"], ["Milan"], modes=["future"], notes=[NOTICE_NOTE, "Announced go-live, not proof of live operation; place-of-settlement details for individual instruments require the programme documents."])

    # ---------------------------------------------------------- Copenhagen
    CPH_NOTE = "English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed."
    C4 = "3d76a327339b"
    add("copenhagen-routing", "Transfer orders, VP versus T2S settlement days and routing conditions (Part 4 §§2.2–2.3)", [part(C4, [3, 4], "2.2 Transfer Orders", "2.4 Settlement Discipline", locator="Part 4 §§2.2–2.3; PDF 3–4")],
        ["copenhagen_settlement_routing"], ["Copenhagen"], effective="2025-05-01", notes=[CPH_NOTE, "T2S-eligibility of a security is defined by the User Guidelines, which are not in the library."])
    add("copenhagen-penalties", "Settlement discipline: penalties, appeals, monthly reporting, PFOD collection, buy-in and suspension (Part 4 §2.4)", [part(C4, [4, 5, 6], "2.4 Settlement Discipline", "3. VP Settlement", locator="Part 4 §2.4; PDF 4–6")],
        ["copenhagen_penalty_procedure"], ["Copenhagen"], effective="2025-05-01", notes=[CPH_NOTE, "Deadlines are in penalties business days (PBD); rates come from the SDR RTS and ECSDA framework, not this excerpt."])
    add("copenhagen-vp-matching-finality", "VP settlement: entry, matching, moment of irrevocability, settlement and finality (Part 4 §§4–6.2)", [part(C4, [7, 8, 9], "4. VP Settlement - Entering", locator="Part 4 §§4–6.2.1; PDF 7–9")],
        ["copenhagen_vp_settlement_finality"], ["Copenhagen"], effective="2025-05-01", notes=[CPH_NOTE, "Applies to the VP (non-T2S) settlement route; the T2S route is the section copenhagen-t2s-settlement."])
    add("copenhagen-t2s-settlement", "T2S settlement at VP: access (ICP/DCP), eligibility, accounts, auto-collateral, pre-match, moments of entry, irrevocability, finality and insolvency (Part 4 §11)", [part(C4, [14, 15, 16, 17], "11. T2S Settlement", locator="Part 4 §11; PDF 14–17")],
        ["copenhagen_t2s_settlement"], ["Copenhagen"], effective="2025-05-01", notes=[CPH_NOTE, "The clause links an outdated T2S UHB URL (v2.1, 2015); use the current UDFS sections for platform mechanics.", "Pre-match by VP creates a consolidated already-matched instruction: moments of entry differ for pre-matched and non-pre-matched orders."])
    add("copenhagen-access-links", "Access rules: LEI, legal opinions for foreign participants and conditions for CSD links (Part 2 §§2.1–2.2)", [part(CP2, [2, 3], "2. Access rules", "2.3 Approval of persons", locator="Part 2 §§2.1–2.2; PDF 2–3")],
        ["copenhagen_access_and_links"], ["Copenhagen"], publication_description=True, notes=[CPH_NOTE, "Published requirements at the review date (cover 3 August 2026); operative effective date not stated on the reviewed pages and footer version labels conflict."])

    # ---------------------------------------------------------- Porto
    PM = "089b7aaef991"
    PTO_NOTE = "English version of the Operational Manual V43 (internal date 26 January 2026); Portuguese text governs and the manual's operative effective date is unresolved."
    add("porto-rts-registration", "Real-time settlement system: instruction types, channels (STD/SWIFT/ISO 20022), references, SF1/SF2 and matching tolerance (§§12–12.1)", [part(PM, [116, 117, 118, 119, 120], "CHAPTER 12.", "Information format for registering", locator="Chapter 12 opening and §12.1; PDF 116–120, printed 115–119")],
        ["porto_instruction_registration"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "Tolerance values are on the website, not in the excerpt."])
    add("porto-rts-fields", "STD settlement instruction fields: format, mandatory and matching flags and field notes 1–23 (§12.1 table)", [part(PM, [120, 121, 122, 123, 124, 125, 126, 127], "Information format for registering", "12.2 HOLD, RELEASE", locator="§12.1 field table and notes; PDF 120–127, printed 119–126 (columns visually checked on PDF 121–122)")],
        ["porto_instruction_fields"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "The SLRTfile/SLRTmsg layout (STD Manual Appendix A1) is not admitted; this is the manual's field description, not the file layout."])
    add("porto-hold-release-amend", "Hold, total and partial release, and amendment functionalities with STD/ISO message references (§12.2)", [part(PM, [127, 128, 129, 130, 131], "12.2 HOLD, RELEASE", locator="§12.2; PDF 127–131, printed 126–130")],
        ["porto_hold_release_amendment"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "Reason codes (001–027) are STD SLRT codes as printed."])
    add("porto-cancellation-allegement", "Cancellation rules, automatic cancellation and allegement timing/messages (§§12.3–12.4)", [part(PM, [132, 133, 134], "12.3 CANCELLATION", "12.5 SETTLEMENT OF INSTRUCTIONS", locator="§§12.3–12.4; PDF 132–134, printed 131–133")],
        ["porto_cancellation_allegement"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "The FOP cut-off is printed as 17:00 WET here (18:00 CET); time zone conventions differ across Porto documents."])
    add("porto-settlement-processing", "Settlement processing, failures/PENF reporting and partial settlement rules and limits (§§12.5–12.5.3)", [part(PM, [134, 135, 136, 137, 138], "12.5 SETTLEMENT OF INSTRUCTIONS", "12.5.4 PRIORITY", locator="§§12.5–12.5.3; PDF 134–138, printed 133–137")],
        ["porto_settlement_processing_partial"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "Default partial-settlement limits (EUR 10,000 shares / EUR 100,000 debt) are as printed; T2S Operator parameters govern."])
    add("porto-cross-csd-links", "Cross-CSD links: indirect links via interlinking intermediaries, direct T2S links and realignment (Chapter 15)", [part(PM, [183, 184], "CHAPTER 15.", locator="Chapter 15; PDF 183–184, printed 182–183")],
        ["porto_cross_csd_links"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "Link inventory as described in the manual (Euroclear France, Euroclear Netherlands, NBB-SSS via Euroclear France, Clearstream Banking Frankfurt; intended Iberclear and Monte Titoli); the separate links document is not admitted."])
    add("porto-slme", "Foreign currency settlement system (SLME/SPME): CoSD-conditioned securities settlement and additional FOP matching fields (Chapter 16–16.2)", [part(PM, [185, 186], "CHAPTER 16.", locator="Chapter 16 §§16–16.2; PDF 185–186, printed 184–185")],
        ["porto_foreign_currency_settlement"], ["Porto"], modes=["reference"], notes=[PTO_NOTE, "Usable currencies and tolerances are website data, not admitted."])
    add("porto-operating-hours-web", "Published operating hours table (T2S-based, CET) with the WET note and reference to Notice 0394/2024", [part(PW, start="The operating hours of the centralised systems", end="Company", locator="Working Days & Operating hours page, operating-hours section; capture of 14 September 2026")],
        ["porto_operating_hours_published"], ["Porto"], modes=["reference"], notes=["Web page reproduction of the T2S schedule; the binding source is Notice 0394/2024 (section porto-timetable) and dated exceptions need event evidence.", "The page's 2025 closing-day list was visible at capture; the 2026 calendar is Notice 25/1162 (section porto-calendar)."])

    # ---------------------------------------------------------- Oslo (reference, edition reservation attached)
    OS = "14dc34b8e54e"
    add("oslo-edition-r2", "VPO NOK Rules cover: edition approval reservation (14 September re-verification)", [part(OS, [1], locator="VPO NOK Rules cover, 2 September 2024")],
        ["approval_status"], ["Oslo"], modes=["reference"], notes=["Same page as the 13 September section oslo-edition; hub link and hash unchanged on 14 September 2026.", "System approval is not edition-specific approval. Independent edition approval remains unresolved (gap G07)."])
    OSL_NOTE = "English translation; Norwegian text governs and the edition's approval reservation applies."
    add("oslo-submission-settlement", "Submitting settlement instructions, settlement groups and settlement in VPO NOK (§§21–22.1)", [part(OS, [33, 34, 35], "21 SUBMITTING", locator="VPO NOK Rules §§21–22.1; PDF 33–35")],
        ["oslo_instruction_submission_settlement"], ["Oslo"], modes=["reference"], deps=["oslo-edition-r2"], notes=[OSL_NOTE, "User Documentation referenced for formats and times is not in the library (gap G11)."])
    add("oslo-finality-moments", "VPO NOK: irrevocability on matching, CCP close-out exception, hold provisions and the moment of entry (§§23.1–23.3)", [part(OS, [36, 37], "23 PROCESSING OF SETTLEMENT INSTRUCTIONS", "23.4 PRELIMINARY CALCULATION", locator="VPO NOK Rules §§23.1–23.3; PDF 36–37")],
        ["oslo_finality_moments"], ["Oslo"], modes=["reference"], deps=["oslo-edition-r2"], notes=[OSL_NOTE, "VPO NOK is a Norwegian netting system outside T2S; T2S lifecycle rules do not apply."])
    add("oslo-priority-clearing", "VPO NOK: preliminary calculation, priority rules, linked instructions, liquidity duties and clearing (§§23.4–23.8)", [part(OS, [37, 38, 39], "23.4 PRELIMINARY CALCULATION", locator="VPO NOK Rules §§23.4–23.8; PDF 37–39")],
        ["oslo_preliminary_calculation_priority"], ["Oslo"], modes=["reference"], deps=["oslo-edition-r2"], notes=[OSL_NOTE, "Cycle times are in the User Documentation, not admitted."])

    # ---------------------------------------------------------- Athens (reference, Greek prevails)
    AR5 = "410859953fce"
    ATH_NOTE = "Informational English translation; the Greek text prevails. Resolution 5 codified to 24 November 2025 (effective 8 December 2025)."
    add("athens-settlement-methods", "Settlement methods, cash blocking and delegation of technical details to DSS announcements (Part 2)", [part(AR5, [4], "PART 2. Settlement Methods", "Resolution 5 (24/11/2025)", locator="Resolution 5 Part 2 §§2.1–2.2; PDF 4")],
        ["athens_settlement_methods"], ["Athens"], modes=["reference"], notes=[ATH_NOTE, "Business hours, cycles and algorithm specifics are announced through the DSS and are not in the library (gap G12)."])
    add("athens-mio-settlement", "Settlement on the instructions of market infrastructure operators: settlement file, ATHEXClear multilateral and bilateral settlement (Part 3 §§3.1–3.4)", [part(AR5, [5, 6, 7], "PART 3.", "3.5 Settlement in connection with the Derivatives", locator="Resolution 5 Part 3 §§3.1–3.4; PDF 5–7")],
        ["athens_market_infrastructure_settlement"], ["Athens"], modes=["reference"], notes=[ATH_NOTE])
    add("athens-instruction-content", "Participant settlement instructions: operation reasons, mandatory and optional data, acceptance windows (60/365 days), matching and tolerance (Part 4 §§4.1–4.3)", [part(AR5, [9, 10, 11, 12], "PART 4.", locator="Resolution 5 Part 4 §§4.1–4.3(3) with footnotes 17–28; PDF 9–12")],
        ["athens_instruction_content_matching"], ["Athens"], modes=["reference"], notes=[ATH_NOTE, "Annex II operation reasons and the tolerance values are outside the excerpt."])

    # ---------------------------------------------------------- EU law
    LAW_NOTE = "Legal context, not local procedures or Norway incorporation. Future amendments remain separate."
    add("csdr-2-definitions", "CSDR Article 2 definitions (settlement, participant, CSD link, ISD, settlement fail, DVP and others)", [part(EU, article=2, locator="CSDR Article 2; consolidation 17 January 2026")],
        ["csdr_definitions"], ["EU"], services=["regulatory"], effective="2026-01-17", notes=[LAW_NOTE])
    add("csdr-33-35", "CSDR participation requirements and communication standards (Articles 33 and 35)", [part(EU, article=33, locator="CSDR Article 33"), part(EU, article=35, locator="CSDR Article 35")],
        ["participation_and_communication_law"], ["EU"], services=["regulatory"], effective="2026-01-17", notes=[LAW_NOTE])
    add("csdr-39-40", "CSDR settlement finality and cash settlement (Articles 39 and 40)", [part(EU, article=39, locator="CSDR Article 39"), part(EU, article=40, locator="CSDR Article 40, including the ▼M4 amended paragraph 2")],
        ["finality_and_cash_settlement_law"], ["EU"], services=["regulatory"], effective="2026-01-17", notes=[LAW_NOTE, "Article 39 refers to Directive 98/26/EC Articles 3 and 5 (section sfd-3-5); the system-specific moments are defined in each CSD's rules."])
    add("sfd-3-5", "Settlement Finality Directive: enforceability of transfer orders and the moments of entry and irrevocability (Articles 3 and 5)", [part(SFD, article=3, locator="Directive 98/26/EC Article 3; consolidation 8 April 2024"), part(SFD, article=5, locator="Article 5")],
        ["sfd_entry_irrevocability"], ["EU"], services=["regulatory"], effective="2024-04-08", notes=[LAW_NOTE, "National transposition and designation of each system are not admitted."])
    add("sdr-matching-fields", "Settlement discipline RTS: matching functionality, mandatory matching fields, transaction-type field and tolerance levels (Articles 5–6)", [part(SDR, article=5, locator="Regulation 2018/1229 Article 5; consolidation 2 September 2024"), part(SDR, article=6, locator="Article 6")],
        ["sdr_matching_fields"], ["EU"], services=["regulatory"], effective="2024-09-02", notes=[LAW_NOTE, "Article 5(3)(l) allows CSDs to require other matching fields; T2S and local field lists are separate sections."])
    add("sdr-facilities", "Settlement discipline RTS: bilateral cancellation facility, hold and release, partial settlement, allegement timing, status information and batches (Articles 7, 8, 10, 11)",
        [part(SDR, article=7, locator="Article 7"), part(SDR, article=8, locator="Article 8"), part(SDR, article=10, locator="Article 10"), part(SDR, article=11, locator="Article 11")],
        ["sdr_settlement_facilities_information"], ["EU"], services=["regulatory"], effective="2024-09-02", notes=[LAW_NOTE, "Article 12 derogations for low-fail systems are not admitted here."])
    add("rts392-issuer-investor-csd", "RTS 2017/392 Article 1 definitions: issuer CSD and investor CSD (English OJ text)", [part(RTS392, start="Article 1", end="CHAPTER II", locator="Regulation 2017/392 Article 1(a)–(g); OJ L 65, 10.3.2017; browser excerpt")],
        ["issuer_investor_csd_definitions"], ["EU"], services=["regulatory"], modes=["reference"], notes=[LAW_NOTE, "Partial browser capture of the original act; the consolidated EN page returned German text on 14 September 2026, so the library's consolidated capture is language-mislabelled.", "Roles depend on the security and relationship: one CSD can be issuer CSD for one issue and investor CSD for another."])

    # ---------------------------------------------------------- dry-run every extract with the real extractor
    all_sources = dict(existing)
    all_sources.update(SOURCES)
    lengths = {}
    for s in SECTIONS:
        for x in s["extracts"]:
            body = extract(x, all_sources)
            assert body and len(body) >= 40, (s["id"], x["locator"])
            lengths[s["id"]] = lengths.get(s["id"], 0) + len(body)
    ids = [s["id"] for s in SECTIONS]
    assert len(ids) == len(set(ids)) and not set(ids) & {s["id"] for s in config["sections"]}, "duplicate section id"
    for s in SECTIONS:
        for dep in s["dependency_ids"]:
            assert dep in ids, (s["id"], dep)

    # ---------------------------------------------------------- write controls
    config["sections"].extend(SECTIONS)
    config["snapshot_revision"] = REVISION
    config["verification_output_dir"] = "implementation/2026-09-14-settlement-agent/verification"
    config.setdefault("snapshot_admissions", {})["2026-09-14"] = {"snapshot": "2026-09-14-settlement-agent", "admission_record": "implementation/2026-09-14-settlement-agent/source-admission.json"}
    config["quarantines"].extend(["Milan Settlement Instructions §1.3.1 operational-day clock table (PDF 12–16) pending the notice chain",
                                  "RTS 2017/392 consolidated capture as English quotation (German text)",
                                  "Per-participant rows of Milan static-data lists as evidence of any firm's configuration"])
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    register_path.write_text(json.dumps(all_sources, ensure_ascii=False, indent=2) + "\n")
    admission = {"snapshot": "2026-09-14-settlement-agent", "review_date": D, "research_date": D,
                 "new_sections": ids, "new_sources": sorted(SOURCES), "section_count_added": len(ids), "source_count_added": len(SOURCES),
                 "older_section_review_dates_unchanged": True, "production_deployment_of_R2026_NOV_verified": False, "whole_document_admission": False,
                 "extract_characters_by_section": lengths,
                 "notes": ["All admitted pages were read on 14 September 2026; tables on Milan Instructions PDF 37 and 39–41 and Porto manual PDF 121–122 were checked against rendered page images.",
                           "Sections reviewed on 14 September never depend on 13 September sections; the answer layer combines review dates explicitly.",
                           "Dated ECB overlays use currency scope ALL where the ECB text is not currency-specific; the retriever treats ALL as matching any requested currency."]}
    (SNAP / "source-admission.json").write_text(json.dumps(admission, indent=2, ensure_ascii=False) + "\n")

    # ---------------------------------------------------------- language correction for the RTS 2017/392 legal capture
    corrected = 0
    for collection_path, collection in [(ROOT / "curated-manifest.json", CURATED["legal_texts"])]:
        for d in collection:
            if d["id"] == "02017R0392-20170310":
                d.update(actual_content_language="de", navigation_language="en", capture_issue="German operative text beneath English navigation (verified in browser 14 September 2026); do not quote as English.",
                         english_replacement_id="32017R0392-en-article1", knowledge_layer="language-qualified-reference")
                corrected += 1
        collection_path.write_text(json.dumps(CURATED, ensure_ascii=False, indent=2) + "\n")
    captures_path = ROOT / "metadata/legal-browser-sources.json"
    captures = json.loads(captures_path.read_text())
    for d in captures:
        if d.get("id") == "02017R0392-20170310":
            d.update(actual_content_language="de", capture_issue="German operative text beneath English navigation; English Article 1 excerpt registered as 32017R0392-en-article1.")
            corrected += 1
    captures_path.write_text(json.dumps(captures, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"sections_added": len(ids), "sources_added": len(SOURCES), "total_sections": len(config["sections"]), "total_sources": len(all_sources), "language_corrections": corrected}))


if __name__ == "__main__":
    main()
