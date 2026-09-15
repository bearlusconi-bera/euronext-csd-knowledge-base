You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
What happens to my pending instructions if my counterparty at Monte Titoli becomes insolvent?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Milan default procedure: TOI/TOA definitions; blocks on new instructions; intra-CSD cancellation table by ISD/TOI/TOA; cross-CSD instructions put on hold then unilateral cancellation status; X-TRM cancellations.",
  "Article 72(5)-(6) Regulations (13 September) if retrieved.",
  "Italian prevails."
]
Fail conditions (must NOT appear):
[
  "Invent timelines beyond the table."
]
Expected sections (if any): ['milan-default-procedure']
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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.454728+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_default_procedure"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-default-procedure]] — Default management procedure: notification, blocks, cancellation table and cross-CSD hold (Title 4) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | Title 4 §§4–4.4; PDF 71–75, printed 67–71 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Cross-references to Article 57/59 numbering reflect the 2025 Instructions; the 2026 Regulations renumbered articles (e.g. Article 59 categories).
EXCERPT (Title 4 §§4–4.4; PDF 71–75, printed 67–71):
4 DEFAULT MANAGEMENT PROCEDURE


The procedure applies to  all the settlement instructions (related to trades),
repurchase agreements and compensation securities and / or cash and resulting
from guaranteed market transactions, non guaranteed market transactions and
OTC) entered for settlement on Monte Titoli Settlement System and related to
the  Participants and  /  or  indirect  participants, pursuant the  to  Article 59,
paragraph 5 of the Service Regulations.

If a Participant or Indirect Participant defaults, the procedure activated by Monte
Titoli is divided into the following phases:
      1.  Receipt of the declaration of default;
      2.  Interventions on the  settlement system  in  order  to manage  the
      transactions of the insolvent entity.
 The following definitions apply for managing insolvencies:
 -   “time of insolvency” or “TOI”, the moment an insolvency proceeding is
    opened pursuant to article 3 of Legislative Decree 210/2001;
 -   “time of awareness” or “TOA”, the moment Monte Titoli becomes aware of
     the insolvency status of one of its Participants or Indirect Participants.

4.1 RECEIPT OF THE DECLARATION OF DEFAULT

This procedure applies when Monte Titoli is notified of a default, declared in Italy
or another EU country or extra-EU, pursuant to Article 3(6) of Legislative Decree
210/2001.

The procedure is activated by Monte Titoli:

    •  upon receipt of the notification from the Bank of Italy, or

    •  when Monte Titoli is aware of insolvency in the manner required by the
      operational procedures for crisis management, defined in agreement with
      the T2S System Operator; or by written note by a Participant or of a
       central counterparty provided that the notice specifies that the sender "
      under its own responsibility gives notice of the opening of an insolvency
      procedure under Legislative Decree 210/2001 against [name, LEI code,
     CED code, ABI code of the insolvent participant]. This communication must
     be made by the legal and/or contract representative of the Participant or
       central counterparty.





67



[PDF page 72]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





To this end Monte Titoli has a procedure in place with the Bank of Italy that
provides for  it to receive notifications ex art. 3 comma 6 e 9 del D. Lgs. N.
210/2001 at the following dedicated address:

BINnotifyMT@lseg.com

so as to ensure the prompt receipt and appropriate handling of notifications and
the timely communication of the moment and the way in which Monte Titoli has
been informed of the opening of default proceedings and the operations that
follow:

 Immediately upon receiving notification, Monte Titoli:
 a)  in the case of the insolvency of a Participant, actives the Settlement System
    technical  procedures  to  block:   i)  the  acquisition  of new  settlement
    instructions in the Settlement System that are attributable to the insolvent
    Participant; and  ii) amendments to settlement instructions already in the
    Settlement System that are attributable to the same entity;
   To this end, Monte Titoli: (i) blocks the acquisition of settlement instructions
     in the Settlement System that are attributable to the insolvent Participant;
      (ii) for direct connections, prevents the insolvent Participant from sending
   new settlement instructions to the Settlement System, or from amending
    Instructions already in the System;
 b)  in the case of insolvency of an Indirect Participant, blocks the acquisition of
    settlement instructions in the Settlement System that are attributable to
    the  insolvent  Indirect  Participant;  allows  the  Participant  that  settles
    transactions on behalf of the Indirect  Participant to issue, on  its own
    responsibility and  within 2  business  days  (not  including  the day  of
     notification), new settlement  instructions on the accounts pursuant  to
     article 57, paragraph 5, letter b) of the Regulation, for the sole purpose of
    exercising retention rights and guarantee rights, within the limits permitted
   by law;
 c)  cancels the intra-CSD settlement instructions already in the Settlement
   System  that  are  attributable  to  the  insolvent  Participant  or  Indirect
    Participant that have already been acquired by the Settlement System,
    according to methods and timing set out in Chapter 4.2;
 d) puts a hold on the cross-CSD settlement instructions attributable to the
    insolvent  Participant  or  Indirect  Participant  already  in  the  Settlement
    System, according to methods and timing set out in Chapter 4.3;
 e) cancels  the  settlement  instructions from  the X-TRM  Service  that  are
    attributable to the insolvent Participant or Indirect Participant that have not
    yet been input in the Settlement System;
 f)  informs the Participants in the Settlement Service of the activation of the
    default management procedure, specifying the TOI and the TOA.




68



[PDF page 73]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





As regards the notification of the default to the participants, in order to ensure
the unambiguous  identification  of  the  participant  that  has been  declared
insolvent, Monte Titoli will communicate the LEI code, the CED code and/or the
ABI code and the corresponding settlement account of the default Participant or
Indirect Participant.

Again, with the aim of ensuring the adequate dissemination of the information,
Monte  Titoli asks participants to keep the data of the subjects Monte  Titoli
must/can contact for the purposes of the default management procedure for the
same Participants or the clients of Indirect Participants updated (names, mailing
list, phone numbers, etc.).

This data is collected through the CLIMP application.

4.2 CANCELLATION OF INTRA-CSD SETTLEMENT INSTRUCTIONS
Monte Titoli will proceed with cancelling the intra-CSD settlement instructions in
the Settlement System that are attributable to the insolvent Participant or
Indirect Participant according to methods and timing set out in the following
table.


       Settlement instructions              Monte Titoli interventions


Entered  prior  to  TOI  and  with  ISD   Are cancelled at the end of ISD,  if not
subsequent to the insolvency date            settled


Entered prior to TOI and with ISD equal to   Are cancelled at the end of the day of the
or prior to the insolvency date                insolvency, if unsettled


Entered after TOI, observed prior to TOA
and   with  ISD   subsequent   to   the   Are cancelled as soon as possible
insolvency date


Entered after TOI, observed prior to TOA
                                         Are cancelled if unsettled at the end of the
and with ISD equal  to or  prior to the                                      day of insolvency
insolvency date


Entered after TOI and observed after TOA    Are cancelled as soon as possible





69



[PDF page 74]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Notwithstanding  the  manner  and  timing  indicated  above,  for  settlement
instructions attributable to transactions guaranteed by a central counterparty
that uses the X-TRM Service to calculate balances (“CCP”), the following apply:

   a) In the case of insolvency of an Indirect Participant that is a “client broker”
      (“NCM”) tied to a CCP member entity (“GCM”), Monte Titoli cancels only
      those settlement instructions created between the NCM and GCM that are
       in the Settlement System, while instructions between GCM-CCP continue
       to be settled. If the settlement instructions were created directly between
    NCM - CCP, these settlement instructions are cancelled and together with
      the CCP are re-instructed to a securities account communicated by the
    GCM to the CCP;

   b) In the case of insolvency of a Participant or Indirect Participant that is an
       individual or general CCP member, Monte Titoli will cancel all settlement
       instructions between the Participant, or Indirect Participant, and the CCP,
      present in the Settlement System as soon as possible.


4.3 INTERVENTIONS ON THE SETTLEMENT INSTRUCTION CROSS-CSD

In the case of default from a Direct or Indirect Participant to the Settlement
Service, Monte  Titoli applies the interventions set out in paragraph 2 to the
cross-CSD  settlement  instructions,  substituting  settlement  cancellation  with
suspension (hold).

The cross-CSD settlement instructions on hold are subsequently assigned a
unilateral cancellation status by Monte Titoli so that any cancellation requests
entered by the counterparty (bilateral cancellation) may be processed by the
Settlement System.

In the case of default of a participant in another CSD in T2S, shall apply the rules
established by CSD  of the  insolvent  subject, except  for the  possibility  for
Participants of Monte Titoli to suspend liquidation of the settlement Instructions
of offsetting to the default subject.


4.4 INTERVENTIONS ON SETTLEMENT INSTRUCTIONS TO BE SETTLED
   WITHIN THE FOREIGN SETTLEMENT SERVICE

In the event of default of a participant in the Foreign Settlement Service, upon
receiving notice pursuant to Chapter 4.1, Monte Titoli:

- cancels the settlement instructions related to the participant in the X-TRM
Service, not yet forwarded to the Foreign CSD.




70



[PDF page 75]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In the case of default by an entity that a Participant had identified as an Indirect
Participant pursuant to article 57, paragraph 5 of the Serivice Regulations, upon
receiving notice pursuant to Chapter 4.1, Monte Titoli:

-  cancels  the  settlement  instructions  from  the X-TRM  Service  that  are
attributable  to  the  insolvent  Indirect  Participant  that have  not  yet been
forwarded to the Foreign CSD;





71

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
