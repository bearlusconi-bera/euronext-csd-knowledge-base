# Implementation verification

These are actual local evidence-selection and integrity results. The audit's original expected-answer fixtures remain unchanged; no LLM answer-quality evaluation was run.

```json
{
  "evidence_as_of": "2026-09-13",
  "build_manifest_sha256": "070d9793e16f9a3d074f724e4e3ac5e1a52037cfc2f4cf304f566f186182a7d6",
  "routing_cases": 34,
  "routing_passed": 34,
  "routing_actual_statuses": {
    "evidence_only": 28,
    "blocked": 6
  },
  "integrity_checks": 39,
  "integrity_passed": 39,
  "originals_verified_unchanged": 800,
  "failures": [],
  "llm_answer_evaluation": "NOT_RUN \u2014 no language-model answer service is deployed",
  "scope": "Manual question routing, actual local evidence selection and controls. Not semantic answer accuracy or production readiness."
}
```

| Case | Routing result | Retrieved sections |
|---|---|---|
| E01 | PASS: evidence_only | milan-finality, t2s-matching, t2s-posting |
| E02 | PASS: evidence_only | milan-finality |
| E03 | PASS: evidence_only | t2s-matching, t2s-posting, t2s-realignment |
| E04 | PASS: evidence_only | t2s-messages, t2s-posting, t2s-realignment |
| E05 | PASS: evidence_only | copenhagen-dcp |
| E06 | PASS: evidence_only | milan-access |
| E07 | PASS: evidence_only | t2s-schedule |
| E08 | PASS: evidence_only | t2s-events-sep08, t2s-schedule |
| E09 | PASS: evidence_only | t2s-schedule |
| E10 | PASS: evidence_only | csdr-5 |
| E11 | PASS: evidence_only | t1-law |
| E12 | PASS: evidence_only | november-release |
| E13 | PASS: evidence_only | offering-workbook-scope |
| E14 | PASS: blocked | None — blocked |
| E15 | PASS: evidence_only | athens-edition |
| E16 | PASS: evidence_only | oslo-edition |
| E17 | PASS: evidence_only | oslo-edition, oslo-liquidity |
| E18 | PASS: blocked | None — blocked |
| E19 | PASS: evidence_only | copenhagen-day |
| E20 | PASS: evidence_only | porto-dcp |
| E21 | PASS: evidence_only | porto-report-families |
| E22 | PASS: evidence_only | porto-calendar |
| E23 | PASS: evidence_only | athens-cash |
| E24 | PASS: evidence_only | athens-csa |
| E25 | PASS: evidence_only | csdr-37 |
| E26 | PASS: evidence_only | csdr-38 |
| E27 | PASS: evidence_only | dora-scope |
| E28 | PASS: blocked | None — blocked |
| E29 | PASS: evidence_only | interbolsa-identity |
| E30 | PASS: evidence_only | esma-decision |
| E31 | PASS: blocked | None — blocked |
| E32 | PASS: blocked | None — blocked |
| E33 | PASS: evidence_only | future-rts-dates |
| E34 | PASS: blocked | None — blocked |
