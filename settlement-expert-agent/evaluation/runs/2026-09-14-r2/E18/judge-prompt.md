You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What are the current Monte Titoli participant cut-off times for sending DvP instructions for same-day settlement?

# Case category: missing-source (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Milan participant cut-offs are blocked (milan_participant_cutoff, G01): the notice chain was not located.",
  "T2S baseline DVP cut-off 16:00 CET is a platform value, not a participant deadline; Milan Instructions clock table quarantined.",
  "Regulations Article 66/67 delegate to notices and T2S URD."
]
Fail conditions (must NOT appear):
[
  "Give a Milan participant deadline as a fact.",
  "Quote 19:30 or the two-window table as current."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked']

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
# Monte Titoli participant cut-offs for DvP instructions — not available from reviewed evidence

## Direct answer

**I cannot give you Monte Titoli participant cut-off times.** The retrieval for exactly that topic came back **`blocked`**: "Applicable Milan timetable notice chain remains unresolved", recorded as **GAP ID G01**. No reviewed evidence in this bundle prints a Monte Titoli participant deadline for sending DvP (delivery versus payment) instructions, for same-day settlement or for any other intended settlement date. I will not supply a time from memory of market practice, and I will not present a platform time as if it were Milan's participant deadline — those are different things.

What the bundle does contain is the **nominal T2S platform baseline** for the real-time settlement period, reviewed 2026-09-14 on release R2026.JUN. Those are platform structure values, not appointments and **not local participant deadlines**. Your own send-by deadline sits earlier than any platform cut-off and is set by Milan (and, if you instruct through an agent, by that agent) — none of which is in reviewed evidence here.

There is also a scope problem in the question that the evidence cannot resolve: **"same-day settlement" is not defined in this bundle**, and the T2S settlement day does not coincide with the civil day (the reviewed excerpt shows the real-time settlement period beginning after night-time settlement ends, which in turn can complete in the early hours). Whether you mean "intended settlement date equals today's civil date" or "settles in the currently open T2S business day" changes which cut-off you are asking about. I state the assumption I adopt below rather than guessing silently.

## 1. Retrieval statuses — disclosed in full

| # | Context | Status | Gap |
|---|---|---|---|
| 1 | T2S, settlement, participant, current, `t2s_partial_windows_and_cutoffs`, as of 2026-09-14 | `evidence_only` | — |
| 2 | Milan, settlement, participant, current, `milan_participant_cutoff`, as of 2026-09-13 | **`blocked`** — "Applicable Milan timetable notice chain remains unresolved" | **G01** |

**Unresolved requirement.** Retrieval 2 is the retrieval that would have answered your question, and it is blocked. The router also flagged that retrieval 1 exists only because "T2S platform route used because no route for the named CSD covers this topic" — that is, the platform route was substituted for a Milan route that does not exist for cut-offs. So the T2S material below is a substitute of a *different kind*, not a partial version of the Milan answer.

## 2. Assumption I adopt, since the question's scope is under-specified

**Proposed assumption (yours to confirm or correct, not a documented fact).** I read your question as a **nominal** question — "what does the reviewed baseline say", not "what applied on a specific dated business day". The bundle's own limitation line requires this to be said out loud: "A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly." You supplied no business date, and this bundle contains no dated event overlay, so nothing below should be read as what happened, or will happen, on any particular date. If you need a specific date, that needs a reviewed event overlay for that date, which is not here.

## 3. What is documented: the T2S real-time settlement period (nominal baseline, R2026.JUN)

**Documented requirement.** The real-time settlement (RTS) period starts after the end of night-time settlement and is followed by the end-of-day period. Where night-time settlement completes before 3.00 Monday to Friday, and before 2.30 on Saturdays, the real-time settlement period begins before the start of the maintenance window. The period comprises real-time settlement preparation; real-time settlement with **five partial settlement windows** to optimise maximum value and volume of transactions left unsettled for lack of securities; and real-time settlement closure "with different cut-offs and events for different Settlement Instructions, Settlement Restrictions and liquidity transfers categories". The five windows are:

| Window | Nominal baseline | Label |
|---|---|---|
| First partial settlement window | 08:00 to 08:30 | Documented requirement |
| Second | 10:00 to 10:15 | Documented requirement |
| Third | 12:00 to 12:15 | Documented requirement |
| Fourth | 14:00 to 14:15 | Documented requirement |
| Fifth | 30 minutes before the beginning of the DVP cut-off time, then between 15:30 and 16:05 **or** the closure of both DVP cut-offs, whichever comes first | Documented requirement |

Citation for the whole of section 3: [[t2s-rts-phase]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.4.4, PDF 193–194; version R2026.JUN; reviewed 2026-09-14 (source reviewed 2026-09-13); body language English, no authoritative language recorded, translation status "not independently established"; approval: source identity checked, no independent whole-edition supervisory approval certification.

Also documented in the same excerpt: previously unsettled settlement instructions and restrictions from night-time settlement are re-attempted during the real-time settlement period as new resources arrive (securities for delivery, securities in positions earmarked available for collateral, cash), and T2S performs a settlement attempt for any new intraday settlement instructions, settlement restrictions and liquidity transfers validated and accepted during the period. The period also includes penalty-mechanism processing (securities subject to penalties information, penalty modification requests, and daily and historic prices for penalties, used for penalty calculation and reporting).

**Qualifications that travel with every time above** (bundle LIMITATION lines — do not detach them):

1. "Window times are the R2026.JUN baseline (08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, 15:30 to 16:05 or DVP cut-off closure); **some cut-offs are currency dependent**." The excerpt itself repeats this: "Some of these cut-offs and events may be currency dependent." You did not state a settlement currency, so I cannot say which cut-off applies to your instructions.
2. "A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly." Stated in section 2.

## 4. What the evidence deliberately does not say

**Unresolved requirement — no DVP cut-off clock time is in reviewed evidence.** This is the trap in the question and worth being explicit about: the excerpt references "the beginning of the DVP cut-off time" and "the closure of both DVP cut-offs" **without printing either clock value**. The only times printed are the five window boundaries above and the night-time-settlement completion thresholds (3.00 / 2.30 as printed). Any figure I offered for the DVP cut-off itself would be fabricated, so there is none here — and note that the fifth window's own definition makes it conditional on a value the excerpt does not give.

**Unresolved requirement — a platform cut-off is not your send-by deadline.** The reviewed section describes when T2S stops accepting categories of instruction for settlement in its own day structure. It says nothing about when a Monte Titoli participant must have sent an instruction, nothing about Milan's own acceptance deadlines, nothing about X-TRM or direct-link channel timings, and nothing about agent-bank internal deadlines. Reading a platform boundary as a participant deadline is the specific error this answer avoids.

**Unresolved requirement — "current" cannot be certified.** Evidence reviewed on 2026-09-14 is evidence reviewed on 2026-09-14; the passage of time does not make it current, and this bundle contains no notice or release-status section tying R2026.JUN to a deployed state on a given business date. The available review dates in this bundle are 2026-09-13 and 2026-09-14.

**Reasoned inference** (derived from the structure of §1.4.4.4 plus the blocked status of retrieval 2, not printed anywhere): because closure carries "different cut-offs and events for different Settlement Instructions, Settlement Restrictions and liquidity transfers categories" and some of those are currency dependent, a single "the DvP cut-off" figure would be wrong even if a platform value were admitted — the answer is a set of category- and currency-specific boundaries, beneath which Milan's own participant deadlines then sit. That layered structure is inference from the evidence; the Milan layer is entirely absent.

I have not drafted or sent any enquiry to Monte Titoli, Euronext Securities Milan or the ECB, and I have consulted nothing outside this bundle. Note in particular that Milan's own Settlement Service Instructions are **not** in this bundle, and their older clock table is quarantined in this library in any case, so no Milan time is quoted from any source here.

## Open items

1. **Monte Titoli participant cut-off times for DvP instructions — blocked, GAP G01**, with the retriever's reason recorded verbatim as "Applicable Milan timetable notice chain remains unresolved". Needed: the Milan timetable notice chain resolved to the edition in force — the applicable Euronext Securities Milan notice or notice series that sets and amends the participant timetable, together with the Settlement Service Instructions edition it amends, reviewed as a set so the chain is unbroken. Official route: the Euronext Securities Milan public notices and documentation hub, with client-only timings via the MT-X client platform or the CSD's documentation service; the Italian text governs the Milan Regulations and Instructions and would prevail over any English translation.
2. **DVP cut-off clock values and the currency dimension** — not in reviewed evidence. Needed: the T2S settlement-day schedule / real-time settlement closure section that prints the DVP cut-off times per currency for the release in force, plus your settlement currency.
3. **Release and business-date confirmation** — R2026.JUN is the reviewed platform release of the cited section; deployment on a given business date is not evidenced. Needed: a release-status or notice section, and for any specific date a reviewed dated event overlay (a routine-only day means no deviation was published, not that everything ran to the nominal times).
4. **Definition of "same-day settlement" for your purpose** — client scope, not a library gap. Needed from you: whether you mean intended settlement date equal to the current civil date or settlement within the currently open T2S business day, plus your access model (directly connected party or indirectly connected via X-TRM or an agent), since the send-by deadline differs by channel.
5. **No route for Milan cut-offs exists in the router** — recorded by the retriever as the reason a T2S platform route was substituted. Worth raising with the library maintainer as a coverage gap distinct from G01 itself.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.401377+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_windows_and_cutoffs"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline
ROUTER NOTES: {"_note": "T2S platform route used because no route for the named CSD covers this topic"}

--- SECTION [[t2s-rts-phase]] — Real-time settlement period: five partial settlement windows and cut-off structure (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.4; PDF 193–194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Window times are the R2026.JUN baseline (08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, 15:30 to 16:05 or DVP cut-off closure); some cut-offs are currency dependent.
LIMITATION: A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly.
EXCERPT (§1.4.4.4; PDF 193–194):
1.4.4.4 Real-time settlement (RTS)

 4    This section presents the real-time settlement processes in the T2S settlement day. The real-time settlement
 5    period starts after the end of the night-time settlement and is followed by the end of day period.

 6    In case the NTS completes before 3.00 from Mondays to Fridays and before 2.30 on Saturdays, real-time
 7    settlement period begins before the start of the maintenance window.

 8   The real-time settlement period includes:

 9         l  The real-time settlement preparation;

10         l  The real-time settlement with the five partial settlement windows to optimise maximum value and vol-
11      umes of settlement transactions, which are unsettled because of lack of securities:

12      – The first partial settlement window between 08:00 and 08:30;

13      – The second partial settlement window between 10:00 and 10:15;

14      – The third partial settlement window between 12:00 and 12:15;

15      – The fourth partial settlement window between 14:00 and 14:15;

16      – The fifth partial settlement window is 30 minutes before the beginning of the DVP cut-off time, then
17         between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first).

18   The previously unsettled Settlement Instructions and Settlement Restrictions from night-time settlement are
19    attempted for settlement in the real-time settlement period with the arrival of new resources (securities for
20    delivery, securities in positions earmarked available for collateral, cash). 143 Additionally T2S performs a set-
21    tlement attempt for any new intraday Settlement Instructions, Settlement Restrictions and liquidity transfers
22    validated and accepted during real-time settlement period;

23         l  The real-time settlement closure with different cut-offs and events for different Settlement Instructions,
24       Settlement Restrictions and liquidity transfers categories.


     _________________________


        143   During the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been at-
               tempted for settlement. This serialization process will concern all transactions with age >= 3 selected by the Regular Recycling process following a
                   credit in securities or cash or an increase in CMB headroom or limit, guaranteeing that an older transaction will be attempted before a younger one
                with the same priority. The transactions selected by one given recycling process will be segregated into eight groups, depending on their priority
              and age:

               Group 1         Group 2         Group 3         Group 4         Group 5         Group 6         Group 7         Group 8
                    Priority 1           Priority 1           Priority 2           Priority 2           Priority 3           Priority 3           Priority 4           Priority 4
              Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3
               Should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to
                the regular recycling process.


                                                                                            Page 193 of 2017



[PDF page 194]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l Some of these cut-offs and events may be currency dependent.

 2    For the ease of presentation, the real-time settlement period is shown in two parts:

 3         l  The real-time settlement;

 4         l  The real-time settlement closure.

 5   The real-time settlement period also includes processes specific to the penalty mechanism. These are com-
 6    prised of the processing of information received within T2S including securities subject to penalties infor-
 7    mation, penalty modification requests and daily and historic prices for penalties. This information is subse-
 8    quently used for penalty calculations and reporting.


 9

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_participant_cutoff"}
STATUS: blocked — Applicable Milan timetable notice chain remains unresolved.
GAP IDS: ['G01']
ROUTER NOTES: {"_note": "explicitly blocked topic"}

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
