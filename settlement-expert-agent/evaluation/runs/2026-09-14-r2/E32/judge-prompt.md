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
# T2S on 14 April 2026 — was anything unusual, and can it be said to be EUR-specific?

## Direct answer

**Yes, the reviewed evidence records non-routine events attributed to T2S business date 14 April 2026, but nothing in it is specific to the euro.** The ECB status history captured on 14 September 2026 carries four evening entries (displayed under calendar date 13 April 2026, attributed to the 14 April settlement day by a labelled inference) describing a **long Start-of-Day phase incident that delayed the start of the Night-Time Settlement phase**, its resolution with night-time settlement starting late, and a **separate change to the operating day schedule requested by a Central Securities Depository** affecting the overall duration of one Night-Time Settlement phase; the first entry carrying calendar date 14 April 2026 itself says only "T2S is operating normally." The derivative's stated schedule impact for the date is **"stated: schedule changed or delayed"**. **Documented requirement / recorded status** — [[t2s-events-2026-04-14]] ECB T2S status history 2026 (capture of 14 September 2026), entries listed in the derivative for 2026-04-14; reviewed 2026-09-14 (source reviewed 2026-09-14); body language en, no authoritative language recorded, **provenance "not independently established"**; approval: source identity checked, no independent whole-edition supervisory approval certification.

**The EUR qualifier cannot be honoured from this bundle.** Every entry has `currency_mentioned: null` and the derivative's `currency_scope` is **ALL**, which the bundle LIMITATION defines as concerning the operating day as a whole; and the retrieval that would have supplied the dated schedule baseline was **blocked**. So: unusual events are evidenced for the day, but no statement can be made about the euro specifically, and no deviation can be measured against a reviewed baseline.

## Retrieval statuses — one of two retrievals was blocked

| Retrieval | Context | Status | Consequence |
|---|---|---|---|
| 1 | T2S / settlement / participant / `current` / `dated_t2s_schedule`, currency EUR, business date 2026-04-14, as_of 2026-09-14 | **`blocked`** — "The requested business date is outside a verified effective period; historical/future applicability needs separate evidence." No section returned. | **No nominal T2S schedule baseline is available for 14 April 2026.** I therefore cannot state the baseline phase times that applied on that date, cannot quantify how far any phase ran late against a baseline, and cannot confirm which schedule variant was in force. This gap is not filled from memory. |
| 2 | T2S / settlement / participant / `current` / `t2s_status_history`, currency EUR, business date 2026-04-14, as_of 2026-09-14 | `evidence_only` — only the named propositions and their conditions are supported | Supplies the dated ECB status entries below, section [[t2s-events-2026-04-14]], reviewed **2026-09-14**, modes `current`, entity T2S, applicability basis `reference_description`. |

The bundle's own LIMITATION on [[t2s-events-2026-04-14]] confirms the split: the section is "retrievable on its own through `t2s_status_history` (14 September revision v1.1); the nominal baseline is added only when the `dated_t2s_schedule` route applies and the reviewed baseline was effective on that date." Here that route returned **blocked**, so the day is described by its published status entries alone. Available review dates in this bundle: 2026-09-13 and 2026-09-14; the evidence used carries review date **2026-09-14**, which is a fact about the review and the capture, not a claim about any later date.

## What the reviewed entries say

All rows are **Documented requirement** in the narrow sense that the reviewed capture records this published text — [[t2s-events-2026-04-14]] ECB T2S status history 2026 (capture of 14 September 2026), entries listed in the derivative for 2026-04-14; reviewed 2026-09-14; source reviewed 2026-09-14; provenance not independently established; approval: source identity checked, no independent whole-edition supervisory approval certification. Times are **as displayed by the ECB page**; the derivative's own `timezone_note` states that displayed ECB timestamps are preserved, **the time zone is not stated on the page and the UTC conversion is not verified**, so these are displayed labels, not verified clock references and not participant deadlines.

| Displayed calendar date | Displayed time | Substance of the published text | Business-date attribution | Currency named |
|---|---|---|---|---|
| 2026-04-13 | 20:35 | T2S "currently facing a long duration of the Start of Day phase"; as a result the **Night-Time Settlement phase has been impacted and has not started yet**; no impact on Connectivity / Life Cycle Management and Matching / Settlement / Penalty Mechanism processing / Reference Data Management; Eurosystem taking all necessary measures; update promised by 21:30 | inferred (evening entry) → 2026-04-14 | none |
| 2026-04-13 | 21:30 | Same long Start-of-Day duration; Night-Time Settlement still not started; **no impact on any other T2S functionality**; "**There is no foreseen impact on the operating day schedule**"; update promised by 22:45 | inferred (evening entry) → 2026-04-14 | none |
| 2026-04-13 | 22:05 | "T2S is operating normally and the earlier incident impacting the Start-of-day phase has been resolved. As a result of the incident, the T2S night-time settlement phase **started with a delay at 22:02**." | inferred (evening entry) → 2026-04-14 | none |
| 2026-04-13 | 22:55 | "There is currently **no incident** in T2S. However, the **operating day schedule has been changed, due to a request by a Central Securities Depository**, affecting the overall duration of **one Night-Time Settlement phase**." Update promised by 23:45 | inferred (evening entry) → 2026-04-14 | none |
| **2026-04-14** | 05:00 | "T2S is operating normally." | calendar date used as business date (daytime entry, or routine/closure status) | none |

Derivative metadata for the date, from the same section: `business_date` 2026-04-14, `is_weekday` true, `currency_scope` ALL, `schedule_impact` "stated: schedule changed or delayed". The capture is identified as `ecb-status-2026-20260914` from the ECB T2S status history 2026 page, captured on 2026-09-14 with a recorded SHA-256 of the captured file.

**Two documented distinctions worth holding apart.** First, the **incident** (long Start-of-Day phase, delaying the start of night-time settlement) and the **schedule change** are attributed by the source to different causes: the 22:55 entry expressly says there is no incident at that point and attributes the change of the operating day schedule to **a request by a Central Securities Depository**. Second, the 21:30 entry states there was **no foreseen** impact on the operating day schedule, while the 22:55 entry records that the schedule **was** changed — on the source's own wording, for the CSD-request reason rather than as a consequence of the incident. **Reasoned inference** (from the sequence of the two entries): the reviewed text does not state whether the CSD request was itself prompted by the earlier delay, so no causal link between the incident and the schedule change may be asserted.

Terms, offered as **explanation** and not as documented requirements: the *Start-of-Day* phase is the opening phase of a T2S settlement day and *Night-Time Settlement* is the batch settlement phase that follows it; a *settlement day* in T2S opens on the previous calendar evening, which is why evening entries can belong to the next business date.

## Answering the question as asked

1. **"Did anything unusual happen?" — Yes, on the business-date reading.** The evidence records an incident affecting the Start-of-Day phase, a delayed start of night-time settlement, and a change to the operating day schedule at a CSD's request. The derivative's own classification of the date is "stated: schedule changed or delayed", i.e. a deviation was **published**, not merely suspected.
2. **On a strict calendar-date reading, almost nothing is evidenced.** The only entry actually displayed under 14 April 2026 is "T2S is operating normally." at 05:00. The four substantive entries are displayed under **13 April 2026** and reach 14 April only through the derivative's attribution rule. That rule is explicitly a **labelled inference, not source text**: the bundle LIMITATION states "Business-date attribution of evening entries follows a labelled inference from the UDFS schedule; the displayed calendar date and time are preserved", and the per-entry `attribution_basis` cites UDFS §1.4 (settlement day opening at SOD 18:45 the previous evening) as its basis. **UDFS §1.4 is not in this bundle**, and the schedule retrieval that would have carried a reviewed baseline was **blocked** — so the attribution is a reasonable, disclosed inference rather than an evidenced fact, and a reader who means the calendar date should be told which reading is being used.
3. **"In EUR?" — Unresolved requirement.** No reviewed entry names a currency (`currency_mentioned` is null for all five), and the bundle LIMITATION states that "Entries are not currency-specific unless the text names a currency (recorded per entry); scope ALL applies to the operating day as a whole." The evidence therefore supports a statement about the **T2S operating day**, not about euro settlement as distinct from any other T2S settlement currency. I am not treating the operating-day statements as euro-specific findings, and no EUR-denominated figure, volume or value appears in the evidence.
4. **What the events do not prove.** The bundle LIMITATION is explicit: "An announced change is not proof of an individual transaction's execution time." So nothing here establishes when any particular instruction settled, whether any specific participant or CSD was affected, whether any transaction failed, or what penalties arose. "T2S is operating normally" is a **platform status statement**, not a settlement outcome for any instruction — **Reasoned inference** from the wording of the entries, which describe phases and functionalities, not instruction outcomes.
5. **No clock time here is a deadline.** The times above are ECB display labels with an unstated time zone and an unverified UTC conversion; the promised-update times (21:30, 22:45, 23:45) are the ECB's own commitments to publish, and 22:02 is the reported late start of the night-time settlement phase. None of them is a participant cut-off, and because retrieval 1 is blocked, none can be compared with a reviewed nominal baseline for that date.

## What is missing — Unresolved requirements

- **The reviewed nominal T2S schedule effective on 14 April 2026** — retrieval 1 returned **blocked** because the requested business date is outside a verified effective period. Without it there is no baseline for the Start-of-Day or Night-Time Settlement phases on that date, so the size of the delay and the shape of the changed schedule cannot be stated.
- **Any entry between the 22:55 promise and the 05:00 status line** — the 22:55 entry promises updated information by 23:45, and the reviewed derivative contains no entry between it and the 05:00 "operating normally" line. Whether a 23:45 update was published and is simply absent from the capture, or was not published, is **not in reviewed evidence**; I am not asserting either.
- **The identity of the requesting Central Securities Depository**, the substance of its request, and the revised phase durations — the source names none of these.
- **Currency-level, CSD-level or instrument-level effects** — including any impact on Euronext Securities Milan, Copenhagen, Porto, Athens or Oslo, and any effect on matching, penalties, realignments or cash. No such evidence is in the bundle; the entries explicitly state no impact on the listed functionalities, which is a statement about platform functions and not a reconciliation of outcomes.
- **Settlement statistics, fails or penalty data for the date** — none in the bundle.
- **Provenance strength.** The citation records the authoritative language as none and translation status as **"not independently established"**, with approval limited to "source identity checked; no independent whole-edition supervisory approval certification". The section's applicability basis is `reference_description`: it describes captured status text, it is not a normative rule.
- No instruction-like content appeared in the retrieved excerpt; the JSON derivative's notes and fields were treated as data.

## Open items

1. **Reviewed T2S operating-day schedule effective on 14 April 2026** — required to lift the `blocked` status on the dated-schedule intent and to measure the delay and the changed night-time phase duration. Official route: the T2S UDFS / T2S operating-day documentation published on the ECB's T2S documentation pages, reviewed for an effective period covering April 2026.
2. **UDFS §1.4 (settlement-day opening)** — named in the derivative's `attribution_basis` as the basis for attributing evening entries to the next settlement day, but not in the bundle; needed to promote that attribution from labelled inference to reviewed evidence. Official route: same ECB T2S documentation service.
3. **A complete capture of the ECB T2S status history around 13–14 April 2026** — specifically any entry published after the 22:55 one (the promised 23:45 update) and any later same-day entries. Official route: the ECB T2S status history page already cited for [[t2s-events-2026-04-14]].
4. **Currency-scoped evidence** — the question asks about the euro, but the reviewed entries carry `currency_scope` ALL and name no currency. Confirm with the user whether an operating-day answer suffices, or obtain currency-specific ECB/CSD material before any euro-specific statement is made.
5. **Local CSD notices for the same date** — Euronext Securities Milan, Copenhagen, Porto, Athens and Oslo client communications would establish whether and how participants of each CSD were affected; none is in reviewed evidence, and these are client-channel documents.
6. **Review-date scope** — the capture and its review date are 2026-09-14 (available review dates in this bundle: 2026-09-13 and 2026-09-14). A later capture is needed before treating this as a complete account of the date, since the status page can be amended after capture.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.745273+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dated_t2s_schedule", "currency": "EUR", "business_date": "2026-04-14"}
STATUS: blocked — The requested business date is outside a verified effective period; historical/future applicability needs separate evidence.

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_status_history", "currency": "EUR", "business_date": "2026-04-14"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-events-2026-04-14]] — ECB status entries attributed to 2026-04-14 (stated: schedule changed or delayed) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reference_description)
CITATION: ECB T2S status history 2026 (capture of 14 September 2026) | ECB T2S status history, entries listed in the derivative for 2026-04-14; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html
LIMITATION: Entries are not currency-specific unless the text names a currency (recorded per entry); scope ALL applies to the operating day as a whole.
LIMITATION: Business-date attribution of evening entries follows a labelled inference from the UDFS schedule; the displayed calendar date and time are preserved.
LIMITATION: An announced change is not proof of an individual transaction's execution time.
LIMITATION: Retrievable on its own through t2s_status_history (14 September revision v1.1); the nominal baseline is added only when the dated_t2s_schedule route applies and the reviewed baseline was effective on that date.
EXCERPT (ECB T2S status history, entries listed in the derivative for 2026-04-14; capture of 14 September 2026):
{
  "source_id": "ecb-status-2026-20260914",
  "source_url": "https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html",
  "captured_on": "2026-09-14",
  "captured_file": "implementation/2026-09-14-settlement-agent/hubs/ecb-t2s-status-2026.html",
  "captured_sha256": "3377fac2c74fa893d9c8ebac5233cedd29ad73ab94fe911caa299c3ed7a24ec8",
  "timezone_note": "Displayed ECB timestamps preserved; time zone not stated on the page; UTC conversion not verified.",
  "attribution_note": "t2s_business_date follows the rule in attribution_basis. Evening entries about night processes are attributed to the next T2S settlement day; this is a labelled inference from the UDFS schedule, not source text. Weekend calendar dates carry closure/maintenance statements and are not T2S business days.",
  "business_date": "2026-04-14",
  "is_weekday": true,
  "currency_scope": "ALL",
  "currency_note": "ECB entries are not currency-specific unless the text names a currency (see currency_mentioned per entry); scope ALL means the statement concerns the operating day as a whole.",
  "schedule_impact": "stated: schedule changed or delayed",
  "entries": [
    {
      "calendar_date": "2026-04-13",
      "published_time_as_displayed": "20:35:00",
      "original_text": "T2S is currently facing a long duration of the Start of Day phase. As a result of the incident, the Night-Time Settlement phase has been impacted and has not started yet. The incident does not have any impact on Connectivity / Life Cycle Management and Matching / Settlement / Penalty Mechanism processing / Reference Data Management. The Eurosystem is taking all measures necessary to resolve the incident as soon as possible. Updated information will be provided at the latest by 21:30.",
      "attribution_basis": "inferred: evening entry about night-time/start-of-day processing attributed to the following T2S settlement day (UDFS §1.4: the settlement day opens at SOD 18:45 the previous evening); not stated by the source",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-04-13",
      "published_time_as_displayed": "21:30:00",
      "original_text": "T2S is currently facing a long duration of the Start of Day phase. As a result of the incident, the Night-Time Settlement phase has been impacted and has not started yet. The incident does not have any impact on any other T2S functionality. There is no foreseen impact on the operating day schedule. The Eurosystem is taking all measures necessary to resolve the incident as soon as possible. Updated information will be provided at the latest by 22:45.",
      "attribution_basis": "inferred: evening entry about night-time/start-of-day processing attributed to the following T2S settlement day (UDFS §1.4: the settlement day opens at SOD 18:45 the previous evening); not stated by the source",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-04-13",
      "published_time_as_displayed": "22:05:00",
      "original_text": "T2S is operating normally and the earlier incident impacting the Start-of-day phase has been resolved. As a result of the incident, the T2S night-time settlement phase started with a delay at 22:02.",
      "attribution_basis": "inferred: evening entry about night-time/start-of-day processing attributed to the following T2S settlement day (UDFS §1.4: the settlement day opens at SOD 18:45 the previous evening); not stated by the source",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-04-13",
      "published_time_as_displayed": "22:55:00",
      "original_text": "There is currently no incident in T2S. However, the operating day schedule has been changed, due to a request by a Central Securities Depository, affecting the overall duration of one Night-Time Settlement phase. Updated information will follow by 23:45.",
      "attribution_basis": "inferred: evening entry about night-time/start-of-day processing attributed to the following T2S settlement day (UDFS §1.4: the settlement day opens at SOD 18:45 the previous evening); not stated by the source",
      "currency_mentioned": null
    },
    {
      "calendar_date": "2026-04-14",
      "published_time_as_displayed": "05:00:00",
      "original_text": "T2S is operating normally.",
      "attribution_basis": "calendar date used as business date (daytime entry, or routine/closure status)",
      "currency_mentioned": null
    }
  ]
}

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
