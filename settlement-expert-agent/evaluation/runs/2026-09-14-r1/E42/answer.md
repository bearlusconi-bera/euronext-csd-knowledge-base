# Athens (ATHEXCSD) DSS settlement cycle times

## Direct answer

**The settlement cycle times are not in the reviewed evidence, and no answer for "today" can be given.** The retrieval for the DSS technical cycles returned **`blocked`**: "DSS technical announcements defining cycles, cut-offs and formats are not in reviewed evidence" (**gap G12**). What the reviewed evidence does establish is *why* they are absent from the rulebook material: ATHEXCSD's Resolution 5 expressly delegates the number and duration of settlement cycles — and the business hours and the settlement algorithm specifics — to ATHEXCSD's own technical procedures, which are announced to Participants through the DSS.

## Retrieval statuses (disclosure)

| Retrieval | Context | Status | Consequence |
|---|---|---|---|
| 1 | Athens / settlement / participant / `current` / `athens_dss_technical_cycles`, as of 13 September 2026 | **blocked** — gap **G12** | No cycle count, no cycle start/end times, no cut-offs and no DSS message formats may be stated. I do not fill this gap from memory. |
| 2 | Athens / settlement / participant / `reference` / `athens_settlement_methods`, as of 14 September 2026 | `evidence_only` | Supports only the delegation rule and the cash-blocking description below, as a qualified *reference* description. |

I also corrected the routing for this question: the case arrived with no retrieval at all, so I re-ran the enforced retriever against the Athens DSS-cycles topic (which is a listed blocked topic and returns the controlled block above) and against the Athens settlement-methods route. No evidence was widened by doing so.

## What the reviewed evidence does say

**Documented requirement — cycle timing is delegated to DSS announcements, not fixed in the Resolution.**
"Any procedural or technical details relating to settlement operations … for instance with respect to settlement methods, the business hours and performance of settlement, the particular specifications of the settlement algorithm, or the number and duration of settlement cycles, shall be determined in accordance with the technical procedures of ATHEXCSD which are announced by ATHEXCSD to Participants through the DSS or by any other appropriate means of notifying and communicating with them."
[[athens-settlement-methods]] ATHEXCSD Resolution 5, Part 2 §2.2, PDF page 4; version "Resolution 5: effective 8 December 2025", codified to 24 November 2025; section reviewed 14 September 2026, source reviewed 13 September 2026; informational English translation — **the Greek text prevails**; approval status: source identity checked, no independent whole-edition supervisory approval certification; applicability basis is a *reference description*, not an operative schedule.
LIMITATION carried with this claim: "Business hours, cycles and algorithm specifics are announced through the DSS and are not in the library (gap G12)."

**Documented requirement — settlement methods and cash blocking (context only, not timing).**
ATHEXCSD settles transactions on the basis of the settlement methods laid down in Section V of the Rulebook and the provisions of Commission Delegated Regulation (EU) 2017/392 and Commission Implementing Regulation (EU) 2017/394. For cash settlement, ATHEXCSD blocks cash balances in the Cash Settlement Accounts; specifically, where cash settlement is carried out in TARGET-GR with the participation of Settlement Banks, those balances are blocked through TARGET-GR in the respective Sub-accounts kept by Settlement Banks for Participants. [[athens-settlement-methods]] ATHEXCSD Resolution 5, Part 2 §2.1, PDF page 4; reviewed 14 September 2026; English translation, Greek text prevails. This says nothing about when cycles run.

*Term explanation (not a documented requirement): a "settlement cycle" here means a scheduled processing run in which the CSD attempts settlement of the eligible instructions in its queue; "DSS" is the ATHEXCSD system through which the CSD notifies Participants of technical procedures. These explanations are background, not evidence.*

## Why "today" makes the gap worse, not better

**Reasoned inference — derived from the status of retrieval 1, the LIMITATION on [[athens-settlement-methods]] and the delegation rule in Part 2 §2.2.** Because the cycle timetable lives in ATHEXCSD technical announcements rather than in the Resolution, the operative answer for any specific business date is whatever DSS announcement is in force on that date. The library holds no reviewed Athens DSS announcement at all, so there is no baseline timetable to state and no dated overlay to apply to 14 September 2026. Stating a nominal or remembered set of cycle times and calling it "today's" would be fabrication on two counts: the times are not in reviewed evidence, and a nominal schedule is not a dated one.

**Unresolved requirement.** Number of settlement cycles; start, end and cut-off times of each cycle; ATHEXCSD business hours; settlement algorithm specifics; whether any deviation applied on the requested date. All of these are gap **G12** and none may be inferred from the material above.

A further caution on dates: the reviewed evidence in this bundle carries review dates 13 and 14 September 2026, and Resolution 5 is codified to 24 November 2025 with effect from 8 December 2025. A review date is not a statement that nothing has changed since; and the English text used here is an informational translation whose Greek original governs.

## Open items

1. **Gap G12 — ATHEXCSD DSS technical announcements** defining the number and duration of settlement cycles, business hours, cut-offs and formats. This is the single document class that would answer the question. Official route: the ATHEXCSD announcements published to Participants through the DSS, and the Euronext Securities Athens public documentation pages; an operating Participant receives them directly through the DSS.
2. **Confirmation of the intended business date and, if relevant, currency** (euro settlement in TARGET-GR versus non-euro arrangements), since the delegated technical procedures may differ and any dated answer needs the announcement in force on that date.
3. **Greek-language source check.** If the cycle times are later admitted, the Greek text of Resolution 5 and of the DSS announcement governs; the English rendering is informational only.
