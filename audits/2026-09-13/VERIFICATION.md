# Verification results — 13 September 2026

These are static artifact/preservation checks, not retrieval tests or proof that the entire source library is correct.

| Check | Result | Evidence |
| --- | --- | --- |
| All retained originals preserved | PASS | {'checked': 800, 'changed_or_missing': []} |
| Root manifests and explanations preserved | PASS | {'checked': 15, 'changed_or_missing': []} |
| One decision for every catalogue entry | PASS | 918 |
| Unique decision IDs | PASS | 1335 |
| No whole-document operational defaults | PASS | All decision rows false; section proposals separate. |
| Source local paths resolve | PASS | [] |
| At least 20 unique evidence-backed fixtures | PASS | 34 |
| Retrieval results honestly NOT RUN | PASS | No fabricated retrieval/model outcomes. |
| All five markets represented | PASS | Counter({'Milan': 15, 'Copenhagen': 15, 'Porto': 15, 'Oslo': 15, 'Athens': 15, 'EU trading venues / participants': 1, 'EU future settlement cycle': 1, 'T2S native infrastructure': 1, 'Two T2S CSDs': 1, 'Two securities legs': 1, 'T2S dated operations': 1, 'T2S November 2026 release': 1, 'European Offering / Convergence': 1}) |
| Coverage rows complete | PASS | Counter({'partial': 60, 'covered': 14, 'unresolved': 6, 'access-restricted': 2, 'missing': 1}) |
| Recorded PDF sample indices resolve | PASS | [] |
| Relationship and allowlist sources resolve | PASS | [] |
| Saved live evidence hashes match | PASS | {'checked': 114, 'mismatch': []} |
| User attachment identity | PASS | Identity only; no full substantive audit of attachment. |
| CSV/JSON source decision parity | PASS | 1335 |

## Existing library defects and blocked checks

- **FAIL — content completeness:** UDFS PDF 269 field diagram absent from text extraction (F05).
- **FAIL — metadata/language integrity:** English-labelled DORA capture contains French operative text (F06).
- **FAIL — safe operational selection:** current Milan timing sources conflict; whole-document defaults cannot isolate the affected clauses (F01/F04).
- **BLOCKED — independent authority confirmation:** HCMC route refused connection; Oslo edition approval not found. This does not imply the underlying rules are invalid.
- **NOT RUN — 34 retrieval evaluations:** no retrieval runtime/index located; see EVALUATION-SET.json.
- **NOT RUN — full schema validation, authenticated client-interface testing, complete legal and whole-document review:** outside accessible/selected evidence.

All recommended changes remain proposals. No tests were added to a production application because none was present.
