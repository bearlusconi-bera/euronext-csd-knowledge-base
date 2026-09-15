# Euronext CSD knowledge library

**Settlement Expert Agent snapshot added 14 September 2026, revision v1.1 the same day** (`settlement-expert-agent/`; evaluation run r1 on v1, regression run r2 on v1.1 — see `settlement-expert-agent/AGENT-SPEC.md` §9): a routed, evidence-bound answer and specification layer over the reviewed library, plus 93 additional reviewed sections (Milan rules and notices, T2S process chapters, Copenhagen, Porto, Athens, Oslo excerpts, EU law, dated ECB events). **Adversarial repairs completed 14 September 2026.** The original operational evidence retains its **13 September** review date; sections admitted on **14 September** carry that date. Covers Athens, Copenhagen, Milan, Oslo and Porto, T2S and selected EU regulatory provisions.

The original archive of **800 documents** is preserved. Retrieval now uses **124 reviewed sections from 51 source identities**, with explicit scope, citations, dates and source qualifications. Whole documents are not admitted. This supports bounded evidence retrieval; complete production instructions remain outside the reviewed coverage.

| Need | Open |
|---|---|
| Ask a settlement question or draft a specification with cited evidence | [Settlement Expert Agent](settlement-expert-agent/README.md) · [Evaluation report](settlement-expert-agent/evaluation/EVALUATION-REPORT.md) · [Coverage and gaps](settlement-expert-agent/COVERAGE-REGISTER.md) |
| What was researched and admitted on 14 September | [Discovery log](implementation/2026-09-14-settlement-agent/DISCOVERY-LOG.md) · [Admission record](implementation/2026-09-14-settlement-agent/source-admission.json) · [June vs November UDFS comparison](implementation/2026-09-14-settlement-agent/UDFS-JUN-VS-NOV-DELTA.md) |
| Latest repairs, results and remaining limits | [Adversarial repair report](ADVERSARIAL-REPAIRS.md) |
| Earlier implementation and source-gap register | [Initial implementation report](IMPLEMENTATION-REPORT.md) |
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

Originals are in `sources/`, original text derivatives in `extracted/`, and dated audit/implementation additions are in `audits/` and `implementation/`. The original audits, failed-case results and source bytes are preserved. **The old `starter-pack.zip` is reference-only; do not import it as an unrestricted knowledge base.**

The curated manifest remains a reading guide. Prefer section exports partitioned by review date and mode. The local command enforces reviewed metadata; no hosted chatbot or automatic monitor is installed. The Settlement Expert Agent is a local pipeline that calls the same retriever and checks its own answers; its model runtimes (Claude Code CLI, Anthropic API) run only when the user provides credentials. Recheck the relevant sources before advancing their review date.
