You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Did anything unusual happen in T2S on 14 April 2026, in EUR?

# Case category: dated-event (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Entries attributed to business date 14 April 2026: long SOD on the evening of 13 April, NTS started with a delay at 22:02, schedule change affecting one NTS phase; attribution is a labelled inference; no incident on other functionality stated."
]
Fail conditions (must NOT appear):
[
  "Attribute the events to 13 April's settlement day without the inference label.",
  "Claim settlement outcomes."
]
Expected sections (if any): ['t2s-events-2026-04-14', 't2s-schedule-r2']
Expected retrieval statuses: ['evidence_only']

# Rubric
# Evaluation rubric — Settlement Expert Agent

Each end-to-end case is scored on the dimensions below. Three sources of judgement are kept apart and reported separately:

| Source | What it produces | Limits |
|---|---|---|
| Deterministic checks (`settlement_agent.py check`) | Citation ids exist in the retrieved bundle; non-`evidence_only` statuses disclosed; governing-language and publication-description qualifications present; review date stated; no clock times, message versions, EUR amounts or XML absent from the bundle | Pattern-based; cannot judge meaning |
| Independent judge (separate model instance, sees the question, the answer, the actual retrieved passages, the hidden expected points and fail conditions) | Scores 0–2 per dimension with a quoted reason | Same model family as the responder; not a human review |
| Maintainer inspection | For a sample of cases the maintainer reads the source passages against the answer and records agreement or disagreement with the judge | Same assistant that built the library; not independent |

## Dimensions (judge scores 0 = fail, 1 = partial, 2 = met)

1. **Routing / scope** — Did the answer address the entity, service, date and mode the question implies, split multiple intents, and resolve or explicitly assume ambiguous scope?
2. **Evidence selection** — Were the right sections used (compared with the expected sections), including dependency/qualification sections (for example Oslo edition reservation, Milan bilateral cancellation)?
3. **Citation entailment and locator accuracy** — Does each cited passage actually say what the answer attributes to it, with a correct locator (article/section/PDF page) and review date?
4. **Preserved qualifications** — Authoritative language, translation status, approval reservations, publication-description basis, release identity, currency/date scope, LIMITATION lines.
5. **Completeness** — Are the expected key points present, and are the unanswerable parts identified with the missing source named?
6. **No unsupported operational claims** — No invented fields, cardinalities, versions, times, fees, eligibility, deployment or legal effects. Illustrative content labelled.
7. **Justified abstention** — For negative cases: did it decline/limit correctly without refusing the supportable part? For positive cases: did it avoid blanket refusal when evidence was sufficient?
8. **Label discipline** — Documented requirement / reasoned inference / proposed design choice / unresolved requirement used where they matter.

A case **passes** when: no dimension scores 0; dimensions 3, 4 and 6 score 2; and every hidden `must_not` condition is absent. A case is **partial** when it has no 0 but at least one of dimensions 3, 4 or 6 scores 1. Otherwise it **fails**.

Judges must quote the passage that supports or contradicts each key point and must not rely on their own knowledge of CSD rules; if the bundle does not contain a fact, the correct behaviour of the answer is to say so.


# The answer under review
<<<ANSWER
# T2S on 14 April 2026 (EUR): not answerable from reviewed evidence

**Direct answer.** I cannot tell you. The single retrieval made for this question returned **`blocked`**, with no sections and no excerpts, so there is nothing in the reviewed evidence that says what did or did not happen in T2S on 14 April 2026 in EUR. Please do not read this as "nothing unusual happened": the answer is *unknown*, not *normal*.

## Status disclosure

| Retrieval | Context | Status | Reason given by the retriever |
|---|---|---|---|
| 1 | `dated_t2s_schedule`, entity T2S, service settlement, role participant, mode current, currency EUR, business date 2026-04-14, knowledge date 2026-09-14 | **blocked** | "The requested business date is outside a verified effective period; historical/future applicability needs separate evidence." |

The bundle records the review dates available as 13 September 2026 and 14 September 2026, and attaches **no gap id** to this block. **No section was returned, so there is no section identifier available to cite** — every statement below is about the state of the evidence, not about T2S operations.

## What this means, and what it does not

- **Unresolved requirement.** Whether any incident, delay, schedule change or currency-specific deviation was published for the T2S business date 14 April 2026 in EUR is not established by reviewed evidence. Neither the affirmative ("there was an incident") nor the negative ("the day was routine") is supported.
- **Reasoned inference** (derived from the retriever's stated reason, not from any excerpt): the reviewed current-mode T2S schedule evidence carries a *verified effective interval* that does not extend back to 14 April 2026, so even a dated overlay for that day could not be admitted on top of a baseline that is not verified as applicable then. A past business date needs evidence reviewed as applicable to that date; a knowledge date of 14 September 2026 does not retroactively cover April.
- **Documented requirement — none.** There is no admitted excerpt behind any operational claim here, so no nominal cut-off, night-time cycle, phase time or status entry may be quoted for that date. Restating a nominal T2S timetable would also not answer the question: a nominal schedule is a baseline, never a record of what actually occurred on a given day.
- **Not a re-labelling.** An actual-date question cannot be converted into a nominal one. Retrieving the baseline day structure and presenting it as "the schedule on 14 April 2026" would misrepresent baseline evidence as an operational record, so I have not done that.

## What would establish an answer

1. A **reviewed T2S operational status / incident record covering the business date 14 April 2026**, captured and reviewed as applicable to that date (the ECB T2S status history for 2026 is the natural public source, but it must be captured, hashed and reviewed before it counts here).
2. A **reviewed T2S schedule baseline whose verified effective interval includes April 2026** — the release-specific day-phase evidence in the library is verified for a later interval, which is what the block reports; a dated overlay is only admissible together with a baseline that is verified for the same date and review date.
3. If the question is about a specific transaction rather than the platform, the **participant's or CSD's own settlement reporting** for that date, which is client data and is not library evidence at all.

## Open items

- **Missing source:** reviewed T2S status/incident evidence for business date 2026-04-14, currency EUR, plus a baseline schedule section verified as effective for that date. **Gap id:** none is named in this bundle for this block.
- **Official route:** the ECB's public T2S pages (T2S status history and the T2S operational communications for 2026) for the platform record, and the T2S User Detailed Functional Specifications edition that was in force in April 2026 for the day structure of that period; both must be added to the reviewed library before they can be cited. Any Milan/Copenhagen/Porto/Athens/Oslo consequence of that day would additionally need the relevant CSD's own notice for the date.
- **Client data:** for an individual instruction, the participant's settlement confirmations and status advices for 14 April 2026, obtained from your CSD's client platform.
- I have not contacted, and will not contact, the ECB or any CSD on your behalf; the items above are the documents to request through the official routes.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.328619+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule", "currency": "EUR", "business_date": "2026-04-14"}
STATUS: blocked — The requested business date is outside a verified effective period; historical/future applicability needs separate evidence.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
