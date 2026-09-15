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
