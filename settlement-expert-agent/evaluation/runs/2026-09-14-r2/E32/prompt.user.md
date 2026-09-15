QUESTION FROM THE USER:
Did anything unusual happen in T2S on 14 April 2026, in EUR?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

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