# Using the reviewed knowledge library

Controls repaired 14 September 2026; settlement-agent snapshot admitted the same day. Snapshot revision v1.1 (same day, after evaluation run r1) added the `t2s_status_history` route for the dated ECB entries and a revised deterministic router in the agent; no evidence text changed (see `settlement-expert-agent/AGENT-SPEC.md` §9). Base evidence review: **13 September 2026**. Sections reviewed on **14 September 2026** cover November final publication, Milan rules/notices, T2S process chapters, other-CSD excerpts, EU law and dated ECB events (see `implementation/2026-09-14-settlement-agent/source-admission.json`). This is a local evidence library and retrieval command; the `settlement-expert-agent/` layer adds routing, answer composition and checks but no hosted service or monitor.

## Import boundary

Start with `retrieval/exports/2026-09-13/current.jsonl` for the existing operational review. For the new publication status, use `retrieval/exports/2026-09-14/reference.jsonl` or the same date's future-mode export. The 14 September current-operational file is deliberately empty. Keep review dates and modes separate; the combined mode files and `retrieval/admitted-sections.jsonl` require both filters. Across the exports there are 124 distinct bounded sections from 51 source identities (31 reviewed on 13 September, 93 on 14 September). Use `retrieval/section-decisions.json` and `retrieval/source-register.json` as policy/provenance. All whole-document `default_retrieval` flags are false.

`curated-manifest.json` is a reading guide: 84 document candidates and 15 legal captures, including the English DORA replacement. It is not an admission list. The original 800 documents remain intact; audit/implementation additions are separately identified.

The old `starter-pack.zip` contains complete reference documents and is unsuitable for unrestricted ingestion. `reviewed-evidence-pack.zip` contains the reviewed exports and controls. A receiving platform must enforce the metadata: uploading files alone does not enforce policy. The pack is an ingestion bundle; running the local retrieval command and its original-source hash checks requires this full workspace.

## Local retrieval

Run from the library root:

```sh
python3 scripts/retrieve_evidence.py --context '{"as_of":"2026-09-13","entity":"Milan","service":"settlement","role":"participant","mode":"current","question_type":"matching_concept"}' --summary
```

Omit `--summary` to receive excerpts. [The section index](retrieval/README.md) lists question types. The command requires explicit routing context; it does not classify natural-language questions or generate answers.

Entity values are `Milan`, `Copenhagen`, `Porto`, `Athens`, `Oslo`, `T2S` and `EU`. `T2S` selects platform scope; `EU` selects reviewed legal provisions, without assuming Norway incorporation. Service, actor role and mode must also match. Modes are `current`, `reference` and `future`.

A qualified description from an English translation or uncertain edition can be admitted in reference mode without asserting an unconditional current legal duty. Copenhagen's DCP admission and Porto's DCP relationship sections are explicitly marked `applicability_basis: publication_description`: they describe published requirements at their review date and do not establish an operative effective interval. Repeating that review date as `business_date` gives the same qualified result. Other historical/future operative claims require evidence. Exact production XML, local interfaces, tax/fee amounts and instrument permissions remain blocked until their dependencies are reviewed.

The cross-CSD illustration requires `release: R2026.JUN`, `access_model: ICP`, `currency: EUR` and `link_model: direct-both-in-T2S`. These are scenario assumptions, not verified real instrument eligibility. Actual schedules need `business_date` and `currency`; only the reviewed 8 September 2026 EUR event set is admitted. A supplied business date defaults to `schedule_kind: actual` across schedule routes and dependencies. An explicitly nominal question can specify `schedule_kind: baseline`; the result preserves that label. A dedicated actual-date question cannot be relabelled as nominal. Dates must be canonical `YYYY-MM-DD`.

The requested `as_of` must equal the selected sections' `verified_as_of`. A later review does not refresh unrelated topics. For example, Milan matching at `as_of: 2026-09-14` still returns `needs_refresh` because that topic was reviewed on 13 September; the 14 September sections use their own question types (see `settlement-expert-agent/topic-index.json`). Re-verified pages are admitted as new sections with the new date (`t2s-schedule-r2`, `oslo-edition-r2`). Dated overlays reviewed on 14 September use currency scope `ALL` when the ECB text is not currency-specific, and a routine-only date list covers weekdays without published deviations. Calendar rollover never promotes future material or certifies unchanged currentness.

For the new publication status:

```sh
python3 scripts/retrieve_evidence.py --context '{"as_of":"2026-09-14","entity":"T2S","service":"settlement","role":"participant","mode":"reference","question_type":"release_status","release":"R2026.NOV"}' --summary
```

That query selects the final-publication section. The equivalent 13 September query retains the historical draft-status evidence. A June or unknown release cannot select November evidence. The final delivery does not establish production deployment, and no November operational provisions or message versions were admitted.

## Evidence controls

- Original bytes, text derivatives and structured repairs are bound to SHA-256 hashes. Changed evidence blocks retrieval pending review.
- Filters apply before selection and to required dependent sections. Oslo liquidity descriptions include the edition reservation; Milan SF2 retains Article 70(2) bilateral cancellation.
- Current, reference and future sections are separate. The Offering workbook is scope evidence, not universal Milan eligibility. A November publication target is not proof of release deployment.
- Citations identify source URL/hash, document, section/article, PDF index, authoritative language, translation status, source review date and approval qualification. These survive summary mode. Printed page numbers are recorded when checked; no offset is invented.
- Missing context or governing evidence produces a block or context request. Missing source/derivative files return a controlled block. AI-written explanations remain derivatives, never independent authority.

A downstream answer must preserve entity/service/date, conditions, exceptions and source qualifications. Distinguish explicit source text, labelled inference and unsupported claims. The retrieval command supplies evidence; it cannot guarantee a downstream AI classifies questions or reasons correctly.

## Extraction repairs

`implementation/2026-09-13/structured/` holds three matching-field diagrams with notes, dated ECB events, the Offering workbook with cell coordinates, the GLEIF-backed Interbolsa identifier, ESMA decision rows and controlled archive-member records. Only explicitly admitted derivatives enter the export.

PDF 269 and 270 matching diagrams were visually checked. The functional matrix is not a certified production schema. Archive members were staged and XML/import references inspected; unreviewed semantic rules and unresolved dependencies still prevent production-field admission. Text volume does not prove diagram/table completeness.

The French DORA capture is preserved and tagged correctly. English Articles 2 and 64 use the English OJ replacement. Full incident-reporting answers require the applicable RTS/ITS and national chain.

## Rebuild, verify and refresh

```sh
python3 scripts/build_retrieval.py
python3 scripts/verify_audit_implementation.py
python3 scripts/verify_adversarial_repairs.py
python3 scripts/package_reviewed_evidence.py
```

The builder exports already reviewed decisions; it does not approve new sources. `configure_audit_sections.py` records initial editorial decisions and refuses to overwrite configuration. `apply_adversarial_repairs.py` records the one-time reviewed repair revision and refuses to repeat it. `apply_audit_controls.py` reapplies catalogue corrections. `prepare_audit_repairs.py` regenerates structured derivatives; changed derivatives need reviewed hash updates before export. The build manifest also binds the retrieval implementation bytes, and packaging requires both verification reports to match that build.

Historical collection/synthesis builders stop when reviewed controls exist, preventing restoration of broad defaults or old guides. Refresh into a new dated snapshot, compare source versions/hashes and current notices, document the review, then explicitly update decisions and their evidence date. Preserve superseded evidence. No polling is scheduled.

The original 34 expected-answer cases and 31 adversarial case definitions remain unchanged. Repair results are written under `implementation/2026-09-14/verification/`; earlier failed results stay intact. These are evidence-selection/control tests, not LLM answer-quality scores. See [repair results](ADVERSARIAL-REPAIRS.md).
