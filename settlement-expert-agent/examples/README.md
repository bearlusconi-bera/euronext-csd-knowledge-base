# Worked examples

Three representative, fully sourced answers written by the library maintainer on 14 September 2026 from bundles retrieved with `settlement_agent.py retrieve`. They show the answer contract (direct answer, cited sections with locator, review date and qualifications, the four labels, exposure of what is not in reviewed evidence). They are not model outputs and are not part of the held-out evaluation.

| Folder | Kind | Question | Bundle statuses |
|---|---|---|---|
| `01-issuer-investor-csd/` | Explanation | Issuer CSD vs investor CSD; can Monte Titoli be both? | 5 sections, all `evidence_only` |
| `02-cross-csd-dvp-flow/` | Scoped specification | Cross-CSD DvP in EUR, Monte Titoli ICP seller, direct link, R2026.JUN: flow, messages, timing | 8 sections `evidence_only`; per-ISIN eligibility `blocked` (G04) |
| `03-xtrm-icp-technical-spec/` | Technical specification | ICP interface to X-TRM for OTC DvP: connectivity, fields and T2S mapping, lifecycle, maintenance, what is not published | 9 sections `evidence_only`; three `blocked` retrievals (G03, G14) |

Each folder holds `bundle.json` (the retrieved evidence), `answer.md` and `checks.json` (deterministic checker output; all three pass every check). Reproduce a check with:

```bash
python3 settlement-expert-agent/settlement_agent.py check --answer settlement-expert-agent/examples/01-issuer-investor-csd/answer.md --bundle settlement-expert-agent/examples/01-issuer-investor-csd/bundle.json --question "In plain terms, what is the difference between an issuer CSD and an investor CSD, and can a CSD such as Monte Titoli be both at the same time?"
```

Known limits visible in the examples: message layouts for Milan's X-TRM channels and the T2S XSDs are client-only or account-gated and therefore blocked; per-ISIN eligibility and link inventories are static data outside reviewed evidence; the Milan participant cut-off timetable after R2026.JUN is an open gap.
