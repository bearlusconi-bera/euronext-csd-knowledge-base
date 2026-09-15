# Adversarial review

User request: be adversarial and check whether the implementation works better.

1. Reproduce the existing routing results, then test new invariants: event coverage across equivalent question routes, release identity, source qualifications, canonical dates, consistent same-day applicability and missing-source handling.
2. Compare the actual pre-implementation defaults with the new corpus; inspect difficult domain questions against retrieved passages. Do not invent an old-system answer score: it had no runnable answer service.
3. Exercise the portable ZIP as a metadata consumer and inspect the free-text boundary. Distinguish implementation defects from documented missing capabilities.
4. Save reproducible cases, outcomes and source-backed findings. Preserve the reviewed library, package and original audit. This turn is a review, so findings remain open for a subsequent repair.

This review is performed by the same assistant that implemented the controls. Its new cases and source comparisons are useful adversarial evidence, not an independent model benchmark. The knowledge snapshot stays 13 September 2026; limited live checks do not refresh the whole library.

Completed: all four review steps. The existing 34 routing cases pass; 31 new probes produce 20 passes and 11 failures across six defects. A separate official-source check found the new November final delivery. See `REPORT.md`, `ANSWERABILITY.md`, `results.json` and `CURRENTNESS-DELTA.json`. No production repair or source admission was applied during this review.
