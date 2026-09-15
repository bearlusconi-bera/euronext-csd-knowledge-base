# Euronext CSD knowledge library

**Audit controls implemented 14 September 2026; reviewed evidence snapshot 13 September 2026.** Covers Athens, Copenhagen, Milan, Oslo and Porto, T2S and selected EU regulatory provisions.

The original archive of **800 documents** is preserved. Retrieval now uses **30 reviewed sections from 24 source identities**, with explicit scope, citations, dates and source qualifications. Whole documents are no longer admitted by default. This supports bounded evidence retrieval, not unrestricted production instructions.

| Need | Open |
|---|---|
| What changed and what remains unresolved | [Implementation report](IMPLEMENTATION-REPORT.md) |
| Retrieve or import reviewed evidence | [Knowledge-base instructions](KNOWLEDGE-BASE-DESIGN.md) |
| See precisely which sections are admitted | [Section index](retrieval/README.md) |
| Copy the reviewed export and controls | [Reviewed evidence pack](reviewed-evidence-pack.zip) |
| Understand CSD functions and requirements | [How CSDs work](HOW-CSD-WORKS.md) · [Requirements map](REQUIREMENTS-MAP.md) |
| Understand investor/issuer CSD messages and timing | [Bounded cross-CSD flow](CROSS-CSD-FLOW.md) |
| Check versions and future applicability | [Currentness register](CURRENTNESS-REGISTER.md) |
| Find the wider inventory | [Full document list](FULL-DOCUMENT-LIST.md) · [Reading guide](READING-GUIDE.md) |
| Inspect the independent audit | [Audit report](audits/2026-09-13/AUDIT-REPORT.md) |

The library separates current local rules, bounded reference material, European Offering, Convergence, future laws/releases, history and unresolved claims. Group branding is not proof that a rule applies to every CSD.

Remaining dependencies include the Milan timetable notice chain, Oslo edition approval, national approval/implementation evidence, instrument-specific static data and unreviewed or client-only production specifications. Exact tax/fee quotes and complete incident/default/onboarding procedures require additional scoped evidence. The implementation report tracks all 17 dependencies.

Originals are in `sources/`, original text derivatives in `extracted/`, audit additions in `audits/2026-09-13/`, and implementation evidence/repairs in `implementation/2026-09-13/`. The original audit and source bytes are preserved. **The old `starter-pack.zip` is reference-only; do not import it as an unrestricted knowledge base.**

The curated manifest remains a reading guide. Use the section export for retrieval. The local command enforces reviewed metadata; no hosted chatbot, LLM answer service or automatic monitor is installed. Recheck sources before advancing the knowledge snapshot date.
