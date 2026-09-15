# Adversarial repairs — 14 September 2026

**All six reproduced defects are fixed. The unchanged 31 adversarial cases now pass, compared with 20 before the repairs.** The original 34 routing cases, 39 integrity checks and 30 additional repair checks also pass. The package passed its integrity, date, mode and dependency checks.

There are now **31 bounded sections from 26 source identities**. All **800 original documents** and **428 historical audit/evaluation files** remain unchanged. The previous reviewed package and changed implementation files are backed up in `implementation/2026-09-14/before/`.

## What changed

| Finding | Resolution | Verification |
|---|---|---|
| F01 — Dated timeline bypass | Event evidence is enforced for every selected schedule, including dependency paths. A business date defaults to actual operations; explicit nominal requests retain `schedule_kind: baseline`. | Original failing A02–A04 pass; extra tests cover baseline/actual separation, missing context and inherited schedules. |
| F02 — Wrong release evidence | Subject-release identity is distinct from the operational platform release; both constrain selection. June and unknown release-status queries cannot receive November material. | A09–A10 pass; both historical and new publication dates are tested. |
| F03 — Lost Italian qualification | Citations now carry authoritative language, translation status, approval qualification and source review date. Summary mode preserves them. Oslo's source registry also reflects its explicit Norwegian-language reservation. | A15 passes; a separate CLI test checks summary output. |
| F04 — Inconsistent same-date treatment | Copenhagen and Porto DCP excerpts are explicitly qualified publication descriptions. Omitting or repeating the review date produces the same result. No operative start date is invented. | A16–A17 pass; historical applicability remains blocked and the qualification is asserted. |
| F05 — Calendar-year bypass | Only canonical `YYYY-MM-DD` dates are accepted. Calendar/effective-period boundaries use parsed dates. | A18–A19 pass; compact, empty and impossible dates are also checked. |
| F06 — Missing-file exception | Missing originals or derivatives return a controlled block. Changed bytes still block. | A31 passes; missing structured derivatives are also tested. |
| F07 — New final delivery | Added cover-page publication/identity evidence with its own 14 September review date. The earlier 13 September draft-status evidence remains available only for that historical review. | New-date final selection, old-date isolation and no operational promotion are tested. |

## Publication refresh and date boundaries

The new review uses the [ECB final-delivery cover](https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf?1d8ee68f0593cb88571835efb7cd5ed8) and the final UDFS cover. It establishes November document publication and identity. The cover/listing date is 14 September; the UDFS document date is 11 September. **November production deployment remains unverified.**

Only PDF page 1 of each new source is admitted. The final UDFS is retained as an original, but its technical changes, operational procedures, schemas and message-version changes have not been reviewed for admission. [Admission record](implementation/2026-09-14/source-admission.json) · [saved cover](implementation/2026-09-14/sources/november-final-cover.pdf) · [saved UDFS](implementation/2026-09-14/sources/november-final-udfs.pdf).

| Requested review date | Available reviewed scope |
|---|---|
| 13 September | The existing 30 sections, including June operational evidence and historical November draft status |
| 14 September | One additional November final-publication section in reference/future modes |

An operational question at 14 September still requires revalidation of its governing sources. This is a scoped publication refresh, not a claim that every local CSD rule or notice is current on that date.

## Use and verify

Use [the updated instructions](KNOWLEDGE-BASE-DESIGN.md) and [section index](retrieval/README.md). The [rebuilt evidence package](reviewed-evidence-pack.zip) includes exports partitioned by exact review date and mode. Its 14 September current-operational file is deliberately empty.

```sh
python3 scripts/build_retrieval.py
python3 scripts/verify_audit_implementation.py
python3 scripts/verify_adversarial_repairs.py
python3 scripts/package_reviewed_evidence.py
```

The unchanged adversarial case generator is replayed into a new output folder, preserving the earlier failed results. The build manifest now also binds the retrieval code. Packaging refuses verification results from a different build.

[Original/integrity verification](implementation/2026-09-14/verification/VERIFICATION.md) · [31-case replay](implementation/2026-09-14/verification/adversarial/results.json) · [repair checks](implementation/2026-09-14/verification/repair-verification.json) · [package verification](implementation/2026-09-14/verification/package-verification.json).

## Remaining limits

These results verify explicit-context evidence selection and preservation. There is still no natural-language router or deployed answer generator, so generated-answer accuracy has not been measured. The 12-question manual answerability review remains an inspection by the same assistant, not an independent benchmark.

The wider source gaps remain: Milan participant timetable authority, edition-specific approval evidence, actual instrument/account/link eligibility, client specifications and complete production/tax/fee/reporting chains. The original [17-dependency register](implementation/2026-09-13/REMAINING-DEPENDENCIES.md) is historical; G15's final-publication component is now resolved by this review, while its deployment/operational-review component remains open.

Importing the ZIP into another AI does not execute its controls. A receiving system must enforce exact review dates, entity/service/role, mode, releases, event/calendar constraints, dependencies and qualifications. The supplied local retrieval command enforces them against the full workspace; no hosted service or automatic monitor was created.
