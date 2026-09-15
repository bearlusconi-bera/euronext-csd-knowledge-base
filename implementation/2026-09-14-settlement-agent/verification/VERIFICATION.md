# Implementation verification

These are actual local evidence-selection and integrity results. The audit's original expected-answer fixtures remain unchanged; no LLM answer-quality evaluation was run.

```json
{
  "evidence_as_of": "2026-09-13",
  "build_manifest_sha256": "ed577c2eb315cf1592c3809547ea83f309034d3ac955896540fc39d5b0ebbf91",
  "routing_cases": 113,
  "routing_passed": 113,
  "routing_cases_original_fixture": 34,
  "routing_cases_by_fixture": {
    "evaluation-routing.json": 34,
    "evaluation-routing-2026-09-14-settlement-agent.json": 79
  },
  "routing_actual_statuses": {
    "evidence_only": 84,
    "blocked": 27,
    "needs_context": 1,
    "needs_refresh": 1
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
| S01 | PASS: evidence_only | t2s-validation |
| S02 | PASS: evidence_only | t2s-allegement |
| S03 | PASS: evidence_only | t2s-cancellation |
| S04 | PASS: evidence_only | t2s-hold-release |
| S05 | PASS: evidence_only | t2s-recycling |
| S06 | PASS: evidence_only | t2s-partial-settlement |
| S07 | PASS: evidence_only | t2s-linked-instructions |
| S08 | PASS: evidence_only | t2s-conditional-settlement |
| S09 | PASS: evidence_only | t2s-status-management |
| S10 | PASS: evidence_only | t2s-sese023-scope |
| S11 | PASS: needs_context | None — blocked |
| S12 | PASS: blocked | None — blocked |
| S13 | PASS: evidence_only | t2s-rts-phase |
| S14 | PASS: evidence_only | t2s-events-2026-09-08, t2s-rts-phase |
| S15 | PASS: evidence_only | t2s-events-2026-08-26, t2s-schedule-r2 |
| S16 | PASS: evidence_only | t2s-schedule-r2, t2s-status-routine-2026 |
| S17 | PASS: blocked | None — blocked |
| S18 | PASS: blocked | None — blocked |
| S19 | PASS: evidence_only | t2s-schedule-r2 |
| S20 | PASS: evidence_only | milan-settlement-characteristics |
| S21 | PASS: evidence_only | milan-conduct-instruments-notices |
| S22 | PASS: evidence_only | milan-instruction-processing |
| S23 | PASS: evidence_only | milan-cross-csd-disclosure |
| S24 | PASS: evidence_only | milan-connectivity-static-data |
| S25 | PASS: evidence_only | milan-service-scope |
| S26 | PASS: evidence_only | milan-xtrm-field-mapping |
| S27 | PASS: evidence_only | milan-xtrm-lifecycle |
| S28 | PASS: evidence_only | milan-default-procedure |
| S29 | PASS: evidence_only | milan-caof |
| S30 | PASS: evidence_only | milan-penalties-procedure |
| S31 | PASS: evidence_only | milan-external-settlement |
| S32 | PASS: evidence_only | milan-gateway-links-guide |
| S33 | PASS: evidence_only | milan-party2-rule |
| S34 | PASS: blocked | None — blocked |
| S35 | PASS: evidence_only | milan-r2026jun-production |
| S36 | PASS: evidence_only | milan-r2026nov-plan |
| S37 | PASS: blocked | None — blocked |
| S38 | PASS: blocked | None — blocked |
| S39 | PASS: evidence_only | milan-may1-2026 |
| S40 | PASS: blocked | None — blocked |
| S41 | PASS: evidence_only | milan-penalties-calendar-2026 |
| S42 | PASS: evidence_only | milan-european-offering-golive |
| S43 | PASS: blocked | None — blocked |
| S44 | PASS: blocked | None — blocked |
| S45 | PASS: evidence_only | copenhagen-routing |
| S46 | PASS: evidence_only | copenhagen-t2s-settlement |
| S47 | PASS: evidence_only | copenhagen-penalties |
| S48 | PASS: evidence_only | copenhagen-access-links |
| S49 | PASS: blocked | None — blocked |
| S50 | PASS: blocked | None — blocked |
| S51 | PASS: evidence_only | porto-rts-fields |
| S52 | PASS: evidence_only | porto-hold-release-amend |
| S53 | PASS: evidence_only | porto-settlement-processing |
| S54 | PASS: evidence_only | porto-cross-csd-links |
| S55 | PASS: evidence_only | porto-slme |
| S56 | PASS: evidence_only | porto-operating-hours-web |
| S57 | PASS: blocked | None — blocked |
| S58 | PASS: blocked | None — blocked |
| S59 | PASS: evidence_only | oslo-edition-r2, oslo-finality-moments |
| S60 | PASS: evidence_only | oslo-edition-r2, oslo-priority-clearing |
| S61 | PASS: blocked | None — blocked |
| S62 | PASS: evidence_only | athens-instruction-content |
| S63 | PASS: evidence_only | athens-settlement-methods |
| S64 | PASS: blocked | None — blocked |
| S65 | PASS: evidence_only | csdr-2-definitions |
| S66 | PASS: evidence_only | csdr-39-40 |
| S67 | PASS: evidence_only | sfd-3-5 |
| S68 | PASS: evidence_only | sdr-matching-fields |
| S69 | PASS: evidence_only | sdr-facilities |
| S70 | PASS: evidence_only | rts392-issuer-investor-csd |
| S71 | PASS: blocked | None — blocked |
| S72 | PASS: blocked | None — blocked |
| S73 | PASS: evidence_only | november-matching-text |
| S74 | PASS: blocked | None — blocked |
| S75 | PASS: blocked | None — blocked |
| S76 | PASS: evidence_only | november-text-comparison |
| S77 | PASS: blocked | None — blocked |
| S78 | PASS: needs_refresh | None — blocked |
| S79 | PASS: blocked | None — blocked |
