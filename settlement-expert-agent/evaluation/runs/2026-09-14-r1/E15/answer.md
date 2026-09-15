# T2S baseline night-time settlement start time

## Direct answer

**There is no evidence reviewed as of 15 September 2026** — that retrieval returned `needs_refresh`. The review dates that exist in this library are **13 September 2026** and **14 September 2026**, and I will not relabel either of those snapshots as 15 September. On the most recent reviewed evidence (14 September 2026), the T2S baseline settlement-day schedule places the **night-time settlement (NTS) period at 20:00 – 3:00 CET**, so the baseline start of night-time settlement is **20:00 CET**.

## Retrieval statuses that are not `evidence_only` (disclosure)

| Retrieval | Context | Status |
|---|---|---|
| 1 | `as_of: 2026-09-15`, entity T2S, `question_type: t2s_baseline_schedule`, mode current | **needs_refresh** — "No reviewed evidence for this knowledge date. Revalidate the relevant sources before advancing their review date." |
| 2 | `as_of: 2026-09-14`, entity T2S, `question_type: t2s_baseline_schedule`, `schedule_kind: baseline` | evidence_only |

Advancing a review date is not something an answer can do: it requires re-fetching and re-reading the source and recording a new verification. Until that happens, 15 September 2026 has no reviewed snapshot.

## The documented baseline

**Documented requirement.** `[[t2s-schedule-r2]]` T2S User Detailed Functional Specifications R2026.JUN (UDFS), **Table 37 – Settlement Day High Level Processes, PDF 160–163**, version R2026.JUN; section reviewed **14 September 2026** (the 14 September re-verification; the underlying source was reviewed 13 September 2026); body language English, no authoritative language asserted; source identity checked, no independent whole-edition supervisory approval certification.

| T2S timeline | Period |
|---|---|
| 18:45 – 20:00 | Start of day (SOD) |
| **20:00 – 3:00** | **Night-time settlement (NTS)** |
| 3:00 – 5:00 | Maintenance window (MWI), optional daily |
| 5:00 (or after NTS if NTS ends before 3:00) | Real-time settlement (RTS) |
| 18:00 – 18:45 | End of day (EOD) |

Supporting detail from the same section and locator:

- Within SOD, "[a]t 20:00, final deadline to accept settlement instructions for processing in the sequence 1 of the first night time cycle" (Table 37, PDF 160).
- The SOD period "starts after the successful completion of the previous EOD period and after 18:45, and is followed by the night-time settlement period" (`[[t2s-schedule-r2]]`, UDFS §1.4.4.1, PDF 163, same review date and qualifications). *Explanation, not a documented requirement:* this is why a T2S settlement day opens on the previous calendar evening — the civil day and the T2S business day are not the same boundary.
- NTS contains two cycles: a first cycle of five sequences (0 to 4) whose "duration ... is dependent on settlement volumes but should finish by 20:20 (target objective) as long as standard peak volumes are not exceeded", and a last cycle of four sequences (4, X, Y, Z) including partial settlement, which "should finish by 00:00 (target objective)" on the same volume condition (Table 37, PDF 160–161).

## What "baseline" means here, and what 20:00 is not

**Documented requirement.** `[[t2s-schedule-r2]]` UDFS §1.4.2 and exception conditions, PDF 156–158, version R2026.JUN; reviewed 14 September 2026; same qualifications. T2S manages each transition between periods as an event with three times:

- the **planned time** — "the standard schedule applied by default by T2S for every settlement day", which the T2S Operator may update on a permanent change;
- the **revised time** — "the foreseen time for the current settlement day, which usually coincides with the planned time except when a delay has occurred"; in contingency the Operator updates the revised time while the planned time is unchanged;
- the **effective time** — "the time of the actual occurrence of the event during the current settlement day".

**Reasoned inference, derived from that three-time model and from the retrieval's `schedule_kind: baseline`:** the 20:00 figure is the *planned* time for the NTS transition. It is not a promise about any particular settlement day, and it is not a participant deadline at any CSD. The section's own LIMITATION lines say exactly this: "Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date." A further LIMITATION fixes the time zone: "CET is the source convention; no UTC conversion" — so 20:00 is CET and I have not converted it.

The same section also records that the schedule is under the T2S Operator's control, that currency-dependent cut-offs and events may be changed for a single settlement day within the stated ordering conditions, and that on exceptional late Friday-evening peak volumes "the T2S Operator would need to process into additional NTS cycles", with the procedure defined in the T2S Manual of Operational Procedures (MOP). The MOP itself is not in this bundle.

**Unresolved requirement:** the actual NTS start on any specific business date. That needs a reviewed event overlay for that date and currency at a matching review date; no such dated question was asked here, and none is answered.

## One note on the two schedule snapshots

`[[t2s-schedule-r2]]` carries the LIMITATION "Same pages as the 13 September section `t2s-schedule`; source bytes re-fetched and hash-identical on 14 September 2026." So the 14 September review is a re-verification of identical source bytes, not a new edition of the UDFS. That is what makes 14 September a real review date — and equally, it is why no such record exists for 15 September.

## Open items

1. **No reviewed evidence exists for 15 September 2026.** To answer at that knowledge date, the T2S UDFS R2026.JUN pages would have to be re-fetched, re-read and admitted with a new verification record. Route: the ECB's T2S professional-use documentation hub, then the library's dated-snapshot refresh procedure. Until then the answer stands on the 14 September 2026 review.
2. **T2S Manual of Operational Procedures (MOP)** — referenced by UDFS §1.4.2 for contingency cut-off changes and for additional Friday NTS cycles; not in reviewed evidence. Route: ECB T2S documentation.
3. **Dated event overlay** for any specific business date and currency, if you need the NTS start actually applied on a given day rather than the baseline. Not requested and not retrieved here.
4. **No local participant cut-off** is established by this answer. A CSD's own deadline for submitting instructions is a separate, CSD-specific document and is not in this bundle.
