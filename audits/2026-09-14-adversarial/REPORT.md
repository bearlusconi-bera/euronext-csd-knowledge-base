# Adversarial review — 14 September 2026

**Verdict: the evidence controls are materially better, but the setup is not yet reliable as an autonomous CSD question-answering system.** I reproduced six implementation issues and found a new official publication that the dated library does not contain. The existing tests substantially overstated the breadth of the verification if read as an answer-quality result; their recorded, narrower claim of scoped routing success remains true.

The original **34 routing cases still pass**. Of **31 adversarial probes, 20 pass and 11 fail**, covering six distinct defects. These cases intentionally target weaknesses; 11/31 is not an estimated failure rate for ordinary questions. No deployed answer model was available for a blind end-to-end comparison.

All **800 original documents** and the **14 checked production artifacts** remained unchanged. This review adds evidence and reproducible tests, without repairing or refreshing the reviewed snapshot.

## What improved

| Area | Before implementation | Verified now |
|---|---|---|
| Default evidence exposure | 49 full-document candidates and 12 legal captures enabled by default | Zero whole-document defaults; 30 bounded sections from 24 source identities |
| Matching-field evidence | Missing diagram content was an audit gap | Diagrams 55–57 are represented by 23 rows and qualifications; visually compared again with PDF 269–270 |
| Matching versus settlement | Explanations already discussed the distinction | Retrieval now assembles matching, posting and Milan finality evidence, retaining bilateral cancellation |
| Known exceptional timetable | Dated operational exceptions were missing from the original core evidence | Dedicated route returns all five reviewed 8 September updates, distinguishing announcement from actual completion |
| Oslo liquidity | Approval reservation could be separated from the substantive clause | Liquidity retrieval includes the cover reservation as a required dependency |
| DORA language | English-labelled capture contained French text | The scoped English OJ provisions are selected; French capture remains preserved and excluded |
| Unsupported production detail | Broad source exposure could invite extrapolation | Exact production matching payloads, unsupported cross-CSD access models and wrong-market questions are blocked in tested routes |
| Freshness | Source-date warnings depended on the consumer | An explicit 14 September knowledge date returns `needs_refresh`; the snapshot does not silently claim currency |

The improvements primarily concern evidence selection and containment. They are not a measured improvement in generated-answer accuracy. [Comparison and counts](summary.json) · [original-case rerun](evidence/existing-routing-rerun.json).

## Findings

| ID | Priority | Finding | Evidence |
|---|---|---|---|
| F01 | High | A dated timeline route omits the required incident overlay | A02–A04 |
| F02 | High | Release-status filtering returns November evidence for June or unknown releases | A09–A10 |
| F03 | Medium | Known authoritative-language qualification is lost in Milan finality output | A15 |
| F04 | Medium | Adding the snapshot date changes otherwise identical current questions into blocks | A16–A17 |
| F05 | Medium | ISO week dates cross calendar years but pass Porto's string-prefix guard | A18–A19 |
| F06 | Low | A missing selected source raises an unhandled exception instead of a controlled block | A31 |
| F07 | Refresh required | New November final documents were published after the stored snapshot | Live official check; separate from the 31 code probes |

### F01 — Required event evidence depends on the question label

At [retrieve_evidence.py:70](../../scripts/retrieve_evidence.py#L70), the date/currency guard runs only for `dated_t2s_schedule`. The same date supplied with `business_day_timeline` returns `t2s-schedule` alone. No incident dependency is added during selection at line 94.

For 8 September EUR, A02 returns baseline evidence without the known exception. A03 and A04 likewise return the baseline for an unreviewed date or DKK overlay. The section itself states that dated queries require event evidence. The dedicated route correctly blocks those unsupported combinations.

This can mislead a downstream answer about actual operations: the reviewed 15:30 ECB update announced EUR IDVP at 17:00, while baseline material says 16:00. The 18:55 update separately records IFOP completion at 18:39. The live history comparison confirms that these September 8 entries remain present. [ECB status history](https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html) · [captured comparison](evidence/ecb-status-2026-visible-text.diff).

**Fix:** represent `baseline` versus `actual` explicitly. Enforce date/currency/event dependencies for every route returning operational timelines. A request explicitly limited to the nominal baseline may still retrieve it, with that scope clearly retained. For actual-date questions, require the reviewed overlay or block.

### F02 — The release selector is ignored for release-status questions

`november-release` has `platform_release: null` in [the section decisions](../../retrieval/section-decisions.json). The generic guard at [retrieve_evidence.py:111](../../scripts/retrieve_evidence.py#L111) skips null values. As a result, both `release: R2026.JUN` and `release: R2099.NOV` return the November 2026 draft-status section in reference mode.

This is a wrong-scope retrieval, even when the caller supplies an explicit release. The native-message route's release check works; the release-status route does not. A careful answer writer could notice the mismatch, but the retrieval layer promised to enforce it.

**Fix:** give release-status evidence an explicit subject-release field and filter on it. Distinguish the release described by a document from the release operating in production. Test June, November and an unknown release across permitted modes.

### F03 — The language qualification is stored but not delivered

The Milan rules' cover says Italian prevails, and `source-register.json` correctly records `authoritative_language: it`. However, [build_retrieval.py:78](../../scripts/build_retrieval.py#L78) exports only `body_language`. The `milan-finality` limitations do not restore the qualification. A15 therefore returns the English legal passage without indicating that Italian governs discrepancies. The separate `milan-access` section includes the warning, but a finality query does not retrieve that section.

**Fix:** carry authoritative language, translation status and relevant approval qualifications into every citation/evidence result, including summary mode. The original qualification is on [PDF page 1](../../sources/documents/8719262f5e8b-Regulations-as-of-26-January-2026.pdf); the substantive excerpt covers Articles 69–72.

### F04 — Explicitly stating today's snapshot date reduces answerability

For Copenhagen DCP admission and Porto DCP relationships, a current question with `as_of: 2026-09-13` returns evidence. Adding `business_date: 2026-09-13` to that same context changes the result to `blocked`, because the selected section has no `effective_from` value. This follows [retrieve_evidence.py:115](../../scripts/retrieve_evidence.py#L115).

The issue is inconsistent treatment of equivalent present-date contexts. This does not establish that the underlying rules are operative; that is the unresolved metadata question the system should handle consistently.

**Fix:** decide explicitly whether each section supports a qualified publication description or an operative requirement. Either keep both requests qualified/reference-only, or establish the operative interval and allow both. Do not solve this by inventing a start date.

### F05 — ISO week dates bypass the calendar year boundary

`date.fromisoformat` accepts week dates, but the parsed value is discarded. Porto then uses `startswith("2026-")` at [retrieve_evidence.py:80](../../scripts/retrieve_evidence.py#L80). Two valid ISO week dates expose the mismatch:

| Supplied date | Actual civil date | Result |
|---|---|---|
| `2026-W01-1` | 29 December 2025 | Retrieves the 2026 calendar |
| `2026-W53-7` | 3 January 2027 | Retrieves the 2026 calendar |

The equivalent canonical 2027 date correctly blocks. **Fix:** enforce the documented `YYYY-MM-DD` input shape or normalise to a parsed date and compare actual date boundaries throughout.

### F06 — Missing source handling is not a structured refusal

A selected source path that no longer exists raises `FileNotFoundError` at [retrieve_evidence.py:124](../../scripts/retrieve_evidence.py#L124). A changed file correctly returns a block. The missing-file case was tested using a disposable path and an isolated in-memory registry; no actual original was moved or removed.

This fails closed, so it is an availability/error-contract defect, not a demonstrated evidence leak. **Fix:** handle expected file-read failures and return a structured `blocked` result identifying the unavailable source. Leave unexpected programming errors visible to maintainers.

### F07 — A real source update is now available

The ECB cover note dated **14 September 2026** confirms final publication of the November T2S document set. The downloaded final UDFS identifies itself as **R2026.NOV**, dated **11 September 2026**, and has **2,349 PDF pages**. The old snapshot's draft-only release-status evidence is therefore incomplete for a question asked today. [Official cover note](https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf) · [saved originals and hashes](evidence/november-final-receipts.json).

Publication does not establish production deployment. Preserve June operational evidence until the deployment/applicability chain justifies a change. The cover's body also retains the earlier 11 September publication target; keep that separate from its 14 September date.

The new files are saved as **unadmitted audit evidence**. The final UDFS was inspected only for identity/first pages; its changed technical provisions were not comprehensively reviewed. A new snapshot should update release status, compare the affected bounded sections and preserve earlier versions. The existing `needs_refresh` response is correct for this situation.

## Answer-level inspection and deployment boundaries

[ANSWERABILITY.md](ANSWERABILITY.md) records twelve concrete prompts, the faithful answer supported by the selected passages and the unresolved limits. This is a manual evidence-to-answer inspection by the same assistant, not an independent evaluation model or a measured free-form RAG run. It demonstrates that useful qualified answers are now possible, while identifying where the caller must combine routes or decline detail.

Two boundary experiments matter for deployment:

- **Free text is not interpreted.** Adding an adversarial `question` field asking for invented production XML and swap atomicity changes no selected evidence. The engine returns `answer_generated: false`; it does not itself hallucinate. A downstream router and answer layer still need explicit evaluation against misleading premises and mixed intents.
- **The ZIP does not execute controls.** A minimal consumer that applies the exported entity/service/role/mode/topic/required-field metadata selects the September 8 event section for a September 9 DKK request, while the local Python command blocks it. The pack includes prose warnings but no executable runtime. Any receiving system must also implement those predicates and limitations; basic metadata filtering or file upload alone is insufficient.

These are documented architectural limits, not extra code defects included in the failure count. [Boundary observations](evidence/boundary-observations.json).

## Recommended next work

1. Repair the route-independent event checks and subject-release filtering; preserve these adversarial cases as regression tests.
2. Refresh November publication status from the new official delivery, keeping publication, document date and deployment separate.
3. Preserve source qualifications in output, resolve date-consistency policy, normalise dates and handle unavailable files.
4. Test the actual natural-language router and answer generator, including refusals and mixed-scope questions, before calling this an autonomous knowledge assistant.

## Reproduce and inspect

From the library root:

```sh
python3 audits/2026-09-14-adversarial/scripts/run_adversarial.py
```

[Cases](cases.json) · [Actual outcomes](results.json) · [Returned evidence bundles](evidence/retrieved-bundles.json) · [Protected hashes](evidence/protected-artifact-hashes.json).

The runner writes only this review's artifacts. It records expected defects as failed cases without returning a shell error, allowing all probes and preservation checks to finish. Inspect `summary.json` and `results.json` for the actual verdict.

The live ECB HTML changed after the stored snapshot. The status page gained a September 14 normal-status entry, and the document hub gained the new final release listings. An initial browser reader returned older hub content, so I checked the direct HTTP response and downloaded the linked official PDF before concluding that publication had occurred. This illustrates why a crawler's freshness label is insufficient. [Live receipts](evidence/live-checks.json) · [normalised content differences](evidence/live-content-comparison.json).
