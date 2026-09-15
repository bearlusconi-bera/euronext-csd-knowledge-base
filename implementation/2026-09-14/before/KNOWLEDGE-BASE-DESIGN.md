# Using the reviewed knowledge library

Controls implemented 14 September 2026. Evidence snapshot: **13 September 2026**. This is a local evidence library and retrieval command; no hosted chatbot, LLM answer service or monitor has been deployed.

## Import boundary

For current questions, start with `retrieval/exports/current.jsonl`, with `retrieval/section-decisions.json` and `retrieval/source-register.json` as policy/provenance. Keep `reference.jsonl` and `future.jsonl` separate and select them only for an explicit reference/future request. The combined `retrieval/admitted-sections.jsonl` requires the same mode filters. Across the exports there are 30 distinct bounded sections from 24 source identities. All whole-document `default_retrieval` flags are false.

`curated-manifest.json` is a reading guide: 84 document candidates and 15 legal captures, including the English DORA replacement. It is not an admission list. The original 800 documents remain intact; audit/implementation additions are separately identified.

The old `starter-pack.zip` contains complete reference documents and is unsuitable for unrestricted ingestion. `reviewed-evidence-pack.zip` contains the reviewed exports and controls. A receiving platform must enforce the metadata: uploading files alone does not enforce policy. The pack is an ingestion bundle; running the local retrieval command and its original-source hash checks requires this full workspace.

## Local retrieval

Run from the library root:

```sh
python3 scripts/retrieve_evidence.py --context '{"as_of":"2026-09-13","entity":"Milan","service":"settlement","role":"participant","mode":"current","question_type":"matching_concept"}' --summary
```

Omit `--summary` to receive excerpts. [The section index](retrieval/README.md) lists question types. The command requires explicit routing context; it does not classify natural-language questions or generate answers.

Entity values are `Milan`, `Copenhagen`, `Porto`, `Athens`, `Oslo`, `T2S` and `EU`. `T2S` selects platform scope; `EU` selects reviewed legal provisions, without assuming Norway incorporation. Service, actor role and mode must also match. Modes are `current`, `reference` and `future`.

A qualified description from an English translation or uncertain edition can be admitted in reference mode without asserting an unconditional current legal duty. Exact production XML, local interfaces, tax/fee amounts and instrument permissions remain blocked until their dependencies are reviewed.

The cross-CSD illustration requires `release: R2026.JUN`, `access_model: ICP`, `currency: EUR` and `link_model: direct-both-in-T2S`. These are scenario assumptions, not verified real instrument eligibility. Dated T2S schedules need `business_date` and `currency`; only the reviewed 8 September 2026 EUR event set is admitted. Another date cannot inherit the nominal schedule as an actual schedule.

A different knowledge `as_of` returns `needs_refresh`. Calendar rollover never promotes future material or certifies unchanged currentness. This is intentionally a dated snapshot.

## Evidence controls

- Original bytes, text derivatives and structured repairs are bound to SHA-256 hashes. Changed evidence blocks retrieval pending review.
- Filters apply before selection and to required dependent sections. Oslo liquidity descriptions include the edition reservation; Milan SF2 retains Article 70(2) bilateral cancellation.
- Current, reference and future sections are separate. The Offering workbook is scope evidence, not universal Milan eligibility. A November publication target is not proof of release deployment.
- Citations identify source URL/hash, document, section/article and PDF index. Printed page numbers are recorded when checked; no offset is invented.
- Missing context or governing evidence produces a block or context request. AI-written explanations remain derivatives, never independent authority.

A downstream answer must preserve entity/service/date, conditions, exceptions and source qualifications. Distinguish explicit source text, labelled inference and unsupported claims. The retrieval command supplies evidence; it cannot guarantee a downstream AI classifies questions or reasons correctly.

## Extraction repairs

`implementation/2026-09-13/structured/` holds three matching-field diagrams with notes, dated ECB events, the Offering workbook with cell coordinates, the GLEIF-backed Interbolsa identifier, ESMA decision rows and controlled archive-member records. Only explicitly admitted derivatives enter the export.

PDF 269 and 270 matching diagrams were visually checked. The functional matrix is not a certified production schema. Archive members were staged and XML/import references inspected; unreviewed semantic rules and unresolved dependencies still prevent production-field admission. Text volume does not prove diagram/table completeness.

The French DORA capture is preserved and tagged correctly. English Articles 2 and 64 use the English OJ replacement. Full incident-reporting answers require the applicable RTS/ITS and national chain.

## Rebuild, verify and refresh

```sh
python3 scripts/build_retrieval.py
python3 scripts/verify_audit_implementation.py
python3 scripts/package_reviewed_evidence.py
```

The builder exports already reviewed decisions; it does not approve new sources. `configure_audit_sections.py` records initial editorial decisions and refuses to overwrite configuration. `apply_audit_controls.py` reapplies catalogue corrections. `prepare_audit_repairs.py` regenerates structured derivatives; changed derivatives need reviewed hash updates before export.

Historical collection/synthesis builders stop when reviewed controls exist, preventing restoration of broad defaults or old guides. Refresh into a new dated snapshot, compare source versions/hashes and current notices, document the review, then explicitly update decisions and their evidence date. Preserve superseded evidence. No polling is scheduled.

The audit's 34 expected-answer cases remain unchanged. Implementation verification separately runs scoped evidence-selection/control cases and integrity checks. These are not LLM answer-quality scores. See [implementation results](IMPLEMENTATION-REPORT.md).
