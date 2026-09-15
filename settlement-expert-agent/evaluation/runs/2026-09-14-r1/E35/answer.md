# Pending instructions facing an insolvent Monte Titoli counterparty

## Direct answer

If your counterparty is a Monte Titoli Participant or Indirect Participant that is declared in default, Monte Titoli activates its default management procedure: it blocks new instructions and amendments from that entity, **cancels** the intra-CSD settlement instructions attributable to it (on a timetable keyed to the time of insolvency and the intended settlement date), and **puts cross-CSD instructions on hold** instead of cancelling them, later flagging them so that a bilateral cancellation can be processed. In practice your pending instructions against that counterparty do not settle: the intra-CSD ones fall away by Monte Titoli's own cancellation, and the cross-CSD ones stop at hold until they are cancelled [[milan-default-procedure]] Instructions to Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025), Title 4 §§4–4.4, PDF 71–75 (printed 67–71); reviewed 14 September 2026; English translation with uneven wording, **Italian text prevails**.

## Retrieval status

One retrieval was made (Milan, settlement service, participant role, current mode, question type `milan_default_procedure`, as of 2026-09-14) and it returned **evidence_only** — no `blocked`, `needs_context` or `needs_refresh` status applies to this answer. Everything below therefore rests on the single reviewed section named above, reviewed 14 September 2026.

Qualifications that travel with every claim below:
- The source is the **English translation** of Monte Titoli's Instructions; the **Italian text is authoritative and prevails** (cover, PDF 1). The translation is uneven in places and quoted terms follow the source.
- The cross-references to Article 57 and Article 59 in the excerpt reflect the **2025 Instructions**; the **2026 Regulations renumbered articles** (for example the Article 59 categories), so the article numbers cited here should be re-mapped against the current Regulations before being used normatively.
- Source identity was checked, but there is **no independent whole-edition supervisory approval certification** for this document.

## What Monte Titoli does — Documented requirement

**Scope.** The procedure applies to all settlement instructions relating to trades, repurchase agreements and compensation securities and/or cash, arising from guaranteed market transactions, non-guaranteed market transactions and OTC, entered for settlement in the Monte Titoli Settlement System and related to Participants and/or Indirect Participants, pursuant to Article 59(5) of the Service Regulations [[milan-default-procedure]] Title 4 §4, PDF 71; reviewed 14 September 2026; English translation, Italian prevails.

**Two defined moments.** "Time of insolvency" (**TOI**) is the moment an insolvency proceeding is opened pursuant to Article 3 of Legislative Decree 210/2001; "time of awareness" (**TOA**) is the moment Monte Titoli becomes aware of the insolvency of one of its Participants or Indirect Participants. The procedure runs in two phases: receipt of the declaration of default, then interventions on the settlement system [[milan-default-procedure]] Title 4 §4, PDF 71; reviewed 14 September 2026.

**How the procedure is triggered.** On notification from the Bank of Italy; or when Monte Titoli becomes aware of the insolvency through the crisis-management operational procedures agreed with the T2S System Operator; or by written note from a Participant or a central counterparty, made by the legal and/or contractual representative and stating, under its own responsibility, that an insolvency procedure under Legislative Decree 210/2001 has been opened against the named entity (name, LEI, CED and ABI codes). Monte Titoli has a dedicated notification channel in place with the Bank of Italy for notices under Article 3(6) and (9) of that decree [[milan-default-procedure]] Title 4 §4.1, PDF 71–72; reviewed 14 September 2026; English translation, Italian prevails.

**Immediate interventions.** Immediately upon receiving the notification Monte Titoli [[milan-default-procedure]] Title 4 §4.1, PDF 72–73; reviewed 14 September 2026:

| # | Intervention |
|---|---|
| a | For an insolvent **Participant**: blocks acquisition of new settlement instructions attributable to it and blocks amendments to its instructions already in the Settlement System; for direct connections, prevents it from sending new instructions or amending existing ones. |
| b | For an insolvent **Indirect Participant**: blocks acquisition of instructions attributable to it, but allows the Participant that settles on its behalf to issue, on its own responsibility and within 2 business days (excluding the day of notification), new instructions on the accounts under Article 57(5)(b) of the Regulation, for the sole purpose of exercising retention and guarantee rights within the limits permitted by law. |
| c | **Cancels** the intra-CSD settlement instructions already acquired by the Settlement System that are attributable to the insolvent entity, per the §4.2 table below. |
| d | **Holds** the cross-CSD settlement instructions attributable to the insolvent entity, per §4.3. |
| e | **Cancels** the settlement instructions from the **X-TRM Service** attributable to the insolvent entity that have not yet been input into the Settlement System. |
| f | **Informs the Participants** of the Settlement Service that the default procedure has been activated, specifying the TOI and the TOA. |

For unambiguous identification, Monte Titoli communicates the LEI code, the CED code and/or the ABI code and the corresponding settlement account of the defaulting Participant or Indirect Participant; participants are asked to keep their default-procedure contact data up to date, collected through the CLIMP application [[milan-default-procedure]] Title 4 §4.1, PDF 73; reviewed 14 September 2026.

**Cancellation timetable for intra-CSD instructions (§4.2).** Documented requirement, reproduced as printed [[milan-default-procedure]] Title 4 §4.2, PDF 73; reviewed 14 September 2026; English translation, Italian prevails:

| Settlement instructions | Monte Titoli intervention |
|---|---|
| Entered prior to TOI, with ISD subsequent to the insolvency date | Cancelled at the end of ISD, if not settled |
| Entered prior to TOI, with ISD equal to or prior to the insolvency date | Cancelled at the end of the day of the insolvency, if unsettled |
| Entered after TOI, observed prior to TOA, with ISD subsequent to the insolvency date | Cancelled as soon as possible |
| Entered after TOI, observed prior to TOA, with ISD equal to or prior to the insolvency date | Cancelled if unsettled at the end of the day of insolvency |
| Entered after TOI and observed after TOA | Cancelled as soon as possible |

("ISD" is the intended settlement date. The table is expressed in terms of ends of days and "as soon as possible"; no clock time is given in the reviewed evidence and none should be assumed.)

**CCP-cleared instructions — carve-outs (§4.2).** For instructions attributable to transactions guaranteed by a central counterparty that uses the X-TRM Service to calculate balances [[milan-default-procedure]] Title 4 §4.2, PDF 74; reviewed 14 September 2026:
1. If the insolvent entity is an Indirect Participant that is a "client broker" (**NCM**) tied to a general clearing member (**GCM**), Monte Titoli cancels only the settlement instructions created between the NCM and the GCM that are in the Settlement System, while GCM–CCP instructions continue to be settled. Instructions created directly between NCM and CCP are cancelled and, together with the CCP, re-instructed to a securities account communicated by the GCM to the CCP.
2. If the insolvent Participant or Indirect Participant is an individual or general CCP member, Monte Titoli cancels **all** settlement instructions between that entity and the CCP present in the Settlement System as soon as possible.

**Cross-CSD instructions (§4.3).** The same interventions apply, but **settlement cancellation is replaced by suspension (hold)**. The cross-CSD instructions on hold are subsequently assigned a **unilateral cancellation status** by Monte Titoli, so that any cancellation request entered by the counterparty (bilateral cancellation) can be processed by the Settlement System. Where the defaulting entity is a participant of **another CSD in T2S**, the rules established by the CSD of the insolvent entity apply, except for the possibility for Monte Titoli participants to suspend the settlement of their offsetting instructions towards the defaulting entity (source wording: "suspend liquidation of the settlement Instructions of offsetting to the default subject") [[milan-default-procedure]] Title 4 §4.3, PDF 74; reviewed 14 September 2026; English translation with uneven wording, Italian prevails.

**Foreign Settlement Service (§4.4).** On default of a participant in the Foreign Settlement Service, Monte Titoli cancels the instructions relating to that participant in the X-TRM Service that have **not yet been forwarded to the Foreign CSD**; the same applies to instructions attributable to an insolvent entity that a Participant had identified as an Indirect Participant under Article 57(5) of the Service Regulations [[milan-default-procedure]] Title 4 §4.4, PDF 74–75; reviewed 14 September 2026.

## What this means for your side — Reasoned inference

These are derived from the text above, not stated in it as obligations of or effects on the non-defaulting party. They are inferences, and each names what it is derived from.

1. **Your instruction against that counterparty will not settle by itself.** Because every instruction between you and the insolvent entity is "attributable to" that entity on one leg, the §4.1(c) and §4.2 cancellation (intra-CSD) or the §4.3 hold (cross-CSD) removes the defaulting leg from settlement. Derived from §4.1(c)–(d) and the §4.2 table.
2. **Which regime applies to you depends on whether the instruction is intra-CSD or cross-CSD**, not on your own status: intra-CSD is cancelled by Monte Titoli; cross-CSD is held and then flagged so that a **bilateral cancellation** can go through. Derived from §4.2 versus §4.3.
3. **For cross-CSD instructions you may have to act.** The unilateral cancellation status exists precisely so that a cancellation request entered by the counterparty — i.e. by you, the non-defaulting side — can be processed. The evidence does not say the held instruction is cancelled automatically for you. Derived from §4.3.
4. **Timing is event-driven, not clock-driven.** Whether your instruction is cancelled "at the end of ISD", "at the end of the day of the insolvency" or "as soon as possible" depends on when it entered the system relative to TOI/TOA and on its ISD relative to the insolvency date. Derived from the §4.2 table.
5. **You should learn of the event from Monte Titoli itself**, which informs Settlement Service participants of the activation with the TOI, the TOA and the LEI/CED/ABI codes plus settlement account of the defaulting entity — the identifiers you need to find your own exposed instructions. Derived from §4.1(f) and the identification paragraph.
6. **If your counterparty is a participant of a different T2S CSD**, the defaulting entity's own CSD rulebook governs the treatment, and the Monte Titoli text only preserves your ability to suspend your offsetting instructions towards it. Derived from §4.3, third paragraph.

## Not in the reviewed evidence — Unresolved requirement

The retrieved section does not establish, and this answer does not assert:
- The **status messages or reports** your side receives when the defaulting leg is cancelled or held (no message type, version, status code or reason code is in the reviewed evidence); a T2S or Milan message/status specification would be needed.
- Whether, and by which mechanism, a **matched** intra-CSD instruction's surviving (non-defaulting) leg is removed — the text states that Monte Titoli cancels the instructions attributable to the insolvent entity, without describing the effect on the counterparty leg or any confirmation you must give.
- Any **clock time, cut-off or deadline** for these interventions; the reviewed text uses only "end of ISD", "end of the day of the insolvency" and "as soon as possible". Milan participant cut-off timetables are a known open gap and must not be assumed here.
- **Penalties, buy-in, settlement-discipline or claim-recovery consequences** for the failed transaction, and any treatment of your cash or securities positions, collateral or guarantees.
- The **procedural route and format** for entering the bilateral cancellation of a cross-CSD instruction on hold (interface, screen, message, entitlement).
- The **2026 renumbering**: the operative article numbers under the 2026 Service Regulations corresponding to the Article 57(5) and Article 59(5) references above.
- Any **release-specific** behaviour: no T2S release identity is attached to this section, so nothing here should be read as release-dependent behaviour of R2026.JUN or of the published-but-not-deployed R2026.NOV.

## Open items

1. **Current Service Regulations (2026 edition)** — to re-map the Article 57(5)/59(5) cross-references used by the 2025 Instructions; route: Euronext Securities Milan public documentation hub.
2. **Italian authoritative text** of the Instructions, Title 4 — to confirm the wording of the §4.2 table and the §4.3 hold/unilateral-cancellation mechanics, because the reviewed English text is a translation with uneven wording and the Italian prevails; route: the same public documentation hub.
3. **Milan/T2S status and message specification** for cancellation and hold notifications to the non-defaulting counterparty — not in reviewed evidence; route: MyStandards / Monte Titoli client documentation (client platform, not public).
4. **Participant timetable evidence** — Milan participant cut-offs are an unresolved gap in this library (gap id G01, `milan_participant_cutoff` is a blocked question type), so no time-of-day commitment can be given for the interventions above.
5. **Penalty and settlement-discipline consequences** of an instruction cancelled under the default procedure — a separate Milan penalties/CSDR settlement-discipline source would be required; not retrieved for this question.
6. **Your own instruction inventory** — client data (the LEI/CED/ABI codes and settlement account published by Monte Titoli with the default notice, matched against your pending instructions) is needed before anything specific can be said about individual instructions.
