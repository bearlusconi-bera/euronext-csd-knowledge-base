You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Taking 13 September 2026 as both the knowledge date and the business date, what does Euronext Securities Copenhagen require from a directly connected participant (DCP)?

# Case category: adversarial-same-date (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Part 5: ECB certification plus VP participation agreement, authorisation/set-up and successful tests; permissions may differ between markets.",
  "Publication description at the review date; operative effective date not established.",
  "Same answer whether or not the business date is repeated."
]
Fail conditions (must NOT appear):
[
  "Claim an operative effective date.",
  "Say the certificate alone suffices."
]
Expected sections (if any): ['copenhagen-dcp']
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
# What Euronext Securities Copenhagen (VP) requires from a directly connected participant (DCP)

## Direct answer

On the retrieved evidence, VP requires two things of a DCP at once. First, the **contractual and access baseline of an ordinary VP Settlement Participant**: a signed Participation Agreement for access as Settlement Participant, an LEI, compliance with the VP Rule Book, and — on request — legal opinions; a DCP remains bound by the same terms as a participant acting only as an ICP unless the DCP Rules provide otherwise, and must in addition enter into a **separate DCP agreement** with VP. Second, the **direct-technical layer**: a valid Eurosystem T2S certificate that the participant alone is responsible for obtaining and maintaining, connection through the technical channel and communication interface prescribed by the Eurosystem or VP from time to time, compliance with VP's own T2S technical characteristics, successful performance of all acts and tests reasonably requested by VP or the Eurosystem, and delivery of any information, documents and assurances VP may reasonably require. The *entitlement* detail — which message types and transaction types are granted, which service tests are accepted, what the VP-specific characteristics actually are — sits in the form "Request for DCP-access to T2S" and in the VP User Guidelines, and **is not in reviewed evidence**.

## The two dates in your question (read this before the requirement list)

You asked me to take 13 September 2026 as **both** the knowledge date and the business date. Those two roles behave differently, and neither is fully satisfiable here.

1. **Knowledge date — partially met.** The bundle header states the available review dates are **13 September 2026 and 14 September 2026**. Two of the four retrievals were run as of 13 September 2026 and returned sections reviewed **13 September 2026** ([[copenhagen-dcp]], [[copenhagen-day]]). Two were run as of 14 September 2026 and returned sections reviewed **14 September 2026** ([[copenhagen-t2s-settlement]], whose underlying source was reviewed 13 September 2026, and [[copenhagen-access-links]], whose underlying source was reviewed 14 September 2026). So the Part 2 access-rule content in particular carries a review date **one day after** your stated knowledge date and is not inside a strict 13 September 2026 knowledge state. *(Reasoned inference from the review dates and source-review dates printed in the bundle.)* All four retrievals returned status `evidence_only`; no retrieval in this bundle was blocked, needs_context or needs_refresh.
2. **Business date — not established, and it does no work here.** In the civil calendar, 13 September 2026 falls on a Sunday. *(Reasoned inference from the ordinary calendar, not from the bundle; background arithmetic, not documented evidence.)* Part 4 makes settlement run on **VP Business Days** and **T2S Business Days**, and adds that VP will only execute settlement in a currency on days on which the central bank responsible for that currency is open for settlement [[copenhagen-day]] Part 4 §§2.2.3–2.2.4; PDF 3; reviewed 13 September 2026. **The bundle contains no VP or T2S operating calendar for September 2026**, so whether 13 September 2026 is a VP or T2S Business Day is an **Unresolved requirement**, not something I can assert. The business-day retrieval is marked **SCHEDULE KIND: baseline**: the hours below are rulebook baseline values, not appointments, not local participant deadlines, and no dated-event or deviation overlay for any specific date was retrieved — I therefore make no statement at all about what did or did not happen on 13 September 2026.
3. **Why it does not change the answer.** Everything VP requires of a DCP in the retrieved evidence is an **admission and continuing-participation** requirement, not a per-business-date obligation. *(Reasoned inference from the structure of Part 5 §§1–3 and Part 4 §11.2.1, which express conditions of access rather than daily duties.)*

## 1. Documented requirements — the DCP-specific layer (VP Rule Book Part 5)

Source qualification carried by every row in this table: **[[copenhagen-dcp]]** — VP Rule Book **Part 5 — T2S DCP Service Rules**, locator **Part 5 §§1–3; PDF 2–3**, version "Part 5 DCP rules: published August 2023; still linked in current rulebook", **reviewed 13 September 2026** (source reviewed 13 September 2026). Basis: **publication description** — this is a qualified description of the **published** requirements at the review date; the **operative effective date is not established** and this does not certify current legal applicability. Body language English; no authoritative-language statement was reviewed and translation status is not independently established. Approval: source identity checked only; no independent whole-edition supervisory approval certification. LIMITATION carried into every row: *published requirements; the exact User Guidelines and the accepted service tests are unverified*.

| # | What VP requires | Locator | Label |
|---|---|---|---|
| 1 | The Participant must have **signed a Participation Agreement with VP for access as Settlement Participant**, and is bound by the same terms as a participant acting only as an ICP unless the DCP Rules provide otherwise | §3.1; PDF 2 | Documented requirement |
| 2 | The Participant must **possess a valid T2S certification from the Eurosystem**, and must perform the Eurosystem certification tests and other acts the Eurosystem requires from time to time; the test scenarios are identical for all markets and are defined solely by the Eurosystem, but may vary with the connectivity channel used, plans to connect to multiple CSDs, and similar factors | §2.3; PDF 2 | Documented requirement |
| 3 | Obtaining **and maintaining** the T2S certificate is **solely the Participant's responsibility** | §2.4; PDF 2 | Documented requirement |
| 4 | The Participant must **connect to T2S using the technical connection and communication interface set forth by the Eurosystem or VP from time to time** | §3.2; PDF 2 | Documented requirement |
| 5 | The Participant must **comply with VP's own T2S-specific technical characteristics**, which are described further in the User Guidelines | §3.5; PDF 3 | Documented requirement |
| 6 | The Participant must **perform all acts and tests reasonably requested by VP or the Eurosystem from time to time**, and the tests must be performed **successfully to a level satisfactory to VP or the Eurosystem** as the case may be | §3.3; PDF 2 | Documented requirement |
| 7 | VP **may request information, documents and assurances** it may reasonably require, to ensure the Participant's IT platform does not harm T2S through inappropriate technical communication or procedures and that T2S operates safely and efficiently | §3.6; PDF 3 | Documented requirement |
| 8 | Authorised scope is **what VP grants**: from the date VP decides to give access, VP authorises direct network access to T2S for the services, privileges and T2S functions **described in the User Guidelines**, and the Participant is authorised to use the **message types and transaction types specified in the form "Request for DCP-access to T2S"**, unless otherwise agreed | §2.1; PDF 2 | Documented requirement |
| 9 | The Participant **acknowledges** that being a DCP via VP may differ, in available services and functions and in the acts and tests to be conducted, from other markets | §2.2; PDF 2 | Documented requirement |
| 10 | VP sets up the access in T2S in accordance with that authorisation; the set-up process is described in the User Guidelines | §2.5; PDF 2 | Documented requirement (obligation on VP, not on the participant) |
| 11 | Where the Participant runs **its own** tests and needs VP's help, VP assists **on a best-efforts basis only** | §3.4; PDF 3 | Documented requirement (limits what a DCP may rely on from VP) |
| 12 | Rule hierarchy: the DCP Rules are Part 5 of the VP Rule Book and **prevail** over other parts of the Participation Agreement in case of inconsistency; Part 1 definitions apply | §§1.1–1.3; PDF 2 | Documented requirement |

**Separate agreement.** Part 4 states the same admission gate from the settlement side: a Settlement Participant may instruct a Transfer Order to T2S either via VP as an ICP or directly via the T2S platform as a DCP, and **"in order to become a DCP the Settlement Participant must enter into a separate agreement with VP"** — [[copenhagen-t2s-settlement]] VP Rule Book Part 4 — Settlement Rules, §11.2.1; PDF 14; version "Part 4 Settlement Rules: 1 May 2025"; **reviewed 14 September 2026** (source reviewed 13 September 2026); English rulebook text, **Danish law governs the VP system and no authoritative-language statement was reviewed**; source identity checked, no independent whole-edition supervisory approval certification. **Documented requirement.**

## 2. Documented requirements a DCP also carries as an ordinary VP participant

These come from Part 2 and Part 4. They are not DCP-specific, but Part 5 §3.1 expressly keeps a DCP bound by them (*Reasoned inference: from Part 5 §3.1 read with the Part 2 and Part 4 clauses cited below — the rulebook does not restate them inside Part 5*).

Source qualification for the Part 2 rows: **[[copenhagen-access-links]]** — VP Rule Book **Part 2 — General Terms and Conditions**, locator **Part 2 §§2.1–2.2; PDF 2–3**, version "cover 3 August 2026; footer version labels 12/13 conflict", **reviewed 14 September 2026** (source reviewed 14 September 2026 — i.e. one day after your stated knowledge date). Basis **publication description**: these are the **published** requirements at the review date; the **operative effective date is not stated on the reviewed pages** and the footer version labels conflict. English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.

| # | What VP requires | Locator | Label |
|---|---|---|---|
| 13 | Any legal person intending to become a Participant must **comply with the Participation Agreement and the VP Rule Book**; access is also restricted by the Danish Capital Markets Act, and VP complies with those restrictions | §§2.1.1–2.1.2; PDF 2 | Documented requirement |
| 14 | The Participant must provide VP with its **legal entity identifier (LEI)** in accordance with Article 55(2) of Delegated Regulation (EU) 2017/392, and the LEI of **all Issuers for whom it acts as Issuing Agent** | §2.1.4; PDF 2 | Documented requirement |
| 15 | On VP's request, the Participant must submit a **duly signed legal opinion** from a nationally or internationally recognised law firm in the relevant jurisdiction, in form and substance satisfactory to VP, establishing corporate power and capacity to enter into the Participation Agreement and that the Agreement is legal, valid and binding under the law of its country of incorporation | §2.1.5; PDF 2 | Documented requirement |
| 16 | For Participants registered in jurisdictions that have **not implemented Directive 98/26/EC** (Settlement Finality Directive) or are not subject to national rules implementing it, VP **may require a second legal opinion** confirming that the Settlement Rules — including netting, postponement of securities transactions and, where relevant, immediate realisation — are enforceable in insolvency against the foreign Participant and its estate; the opinion may be general or Participant-specific | §§2.1.6–2.1.8; PDF 2–3 | Documented requirement |
| 17 | Refusal of access to a Participant that meets the criteria is possible **only** on a written justified refusal based on a comprehensive risk assessment under CSDR Article 33(3) | §2.1.3; PDF 2 | Documented requirement (a limit on VP, not on the participant) |
| 18 | **Only if the DCP is itself a CSD**: participation by Participation Agreement (standard link) or Participation Agreement plus a separate agreement for additional services (customised link, chargeable); before the link goes operational the CSD and VP must run **end-to-end tests required by VP** and the CSD must deliver an **emergency plan** satisfactory to VP; the link must be **reviewed and risk assessed annually** | §§2.2.1–2.2.4; PDF 3 | Documented requirement, conditional on the participant being a CSD |

Row 18 is scoped deliberately: the excerpt applies these terms to "a CSD" becoming a participant in the VP Clearing & Settlement system, not to every DCP. A bank DCP that is not a CSD is not shown by this evidence to owe the emergency plan or the annual link review. **Reasoned inference** from the clause heading "Specific terms for CSDs" and the wording of §2.2.1.

Source qualification for the Part 4 rows below: **[[copenhagen-t2s-settlement]]**, Part 4 §11; PDF 14–17; version 1 May 2025; **reviewed 14 September 2026**; English rulebook text, Danish law governs the VP system, no authoritative-language statement reviewed; LIMITATION — the clause links an **outdated T2S UHB URL (v2.1, 2015)**, so platform mechanics should be taken from current UDFS sections and not from that link.

| # | What VP requires | Locator | Label |
|---|---|---|---|
| 19 | The **T2S User Guidelines** (T2S UDFS and T2S User Handbook) **apply to the Settlement Participant** unless the VP Rule Book provides otherwise | §11.1.1; PDF 14 | Documented requirement (subject to the outdated-URL limitation above) |
| 20 | The Settlement Participant must have **access to at least one T2S Account with VP**, unless it does not need to settle T2S Settlement Required Transactions | §11.4.1; PDF 15 | Documented requirement |
| 21 | Settlement via T2S requires, for DvP/DwP/FoP, that the securities are **T2S-eligible and made available on T2S** per the User Guidelines **and book-entered with VP**; for DvP/DwP/PFoD, that the settlement currency is a **T2S currency** settled in **central bank money**, unless specifically agreed otherwise with VP | §§11.3.2 A–B; PDF 14–15 | Documented requirement |
| 22 | Securities registered on a **T2S Account** may be used for T2S settlement and **cannot** be used for VP settlement unless transferred to a VP Account; how and when such transfers may happen is in the User Guidelines | §11.6.1; PDF 15 | Documented requirement |
| 23 | **T2S auto-collateral** requires all three of: a T2S Auto-Collateral agreement between the Cash Settlement Agent and the relevant central bank, a form delivered to VP electing its use, and earmarking of the T2S Account by registration of a restrictive right in the VP Clearing and Settlement system; the participant must initiate set-up of the account structure with VP and the central bank must instruct T2S | §§11.5.1–11.5.2; PDF 15 | Documented requirement, conditional on electing auto-collateral |
| 24 | Where an order is instructed **to VP**, VP validates it against T2S technical rules on receipt, first checking that the sending party is **authorised to instruct via VP**; unsuccessful validation causes rejection with a reason sent to the submitting party | §§11.6.2–11.6.3; PDF 15 | Documented requirement |
| 25 | Instructions may be submitted for same-day settlement, for settlement **up to 13 months in advance**, and for a past settlement day if all relevant static data were valid on that past day | §11.6.8; PDF 16 | Documented requirement |
| 26 | If the transaction amounts differ between the two sides, the **delivering** participant's amount prevails, provided the difference is within the T2S tolerance match rules | §11.6.6; PDF 15 | Documented requirement |

## 3. Boundaries a DCP must design around (matching, finality, insolvency)

- **Matched is not settled.** A Transfer Order that has reached status "Matched" on the T2S platform — pre-matched by VP or not — **cannot be unilaterally cancelled or revoked** (the Moment of Irrevocability); but from that moment until settlement, **Hold & Release** may still be applied by each party and the parties may **bilaterally agree to cancel** — [[copenhagen-t2s-settlement]] Part 4 §11.7.1; PDF 16; reviewed 14 September 2026. **Documented requirement.** Irrevocability here is therefore protection against *unilateral* withdrawal, not completion of the transfer.
- **Finality.** A Transfer Order is finally settled (unconditional, irrevocable and enforceable) **as from the account entry crediting the securities to the receiving Settlement Participant's securities account on the T2S platform**; the entry is thereafter **mirrored** in the VP Clearing and Settlement System — §11.8.2.1; PDF 17. **Documented requirement.** Unmatched orders are recycled per T2S terms (§11.7.2); matched-but-uncovered orders are recycled per the User Guidelines (§11.8.1.2).
- **Moment of entry differs by route.** A validated **and pre-matched** order is "entered" into the VP system at the moment **VP** declared it compliant with T2S technical rules; an order **not** pre-matched but passed to T2S is "entered" at the moment **the T2S platform** declared it compliant — §11.6.7; PDF 16. VP's right to pre-match rests on a Collective Agreement with the ECB (§11.6.5), and a successful pre-match produces a **new consolidated Transfer Order** sent to T2S already matched (§11.6.4). This is carried as an explicit LIMITATION on the section.
- **Whether pre-match touches a DCP's own instructions is not resolved.** §11.6 describes validation and pre-match for orders **received by VP**; the excerpt does not state whether an instruction a DCP sends directly to T2S is pre-matched or how its moment of entry is determined. **Unresolved requirement** — the Moment of Entry for a DCP-submitted instruction is not established by the retrieved text, and it matters for the insolvency rules below.
- **Insolvency.** Settlement continues until VP receives an authoritative insolvency notice from the Danish FSA or another public authority and has started its T2S insolvency procedures; VP may also issue a default notice earlier and demand a status statement. Orders where **both** sides reached Moment of Entry before the opening of proceedings are attempted; orders that reached Moment of Entry after opening but were matched before VP knew or should have known, for settlement the same T2S business day, are attempted but **cancelled if unsettled at end of day**; everything else is **cancelled immediately** once VP becomes aware — §§11.8.3.1–11.8.3.6; PDF 17. **Documented requirement.**

## 4. Day and timing frame (baseline values only)

From [[copenhagen-day]] VP Rule Book Part 4 — Settlement Rules, §§1–2.2.6; PDF 3; version 1 May 2025; **reviewed 13 September 2026**; English rulebook text, no authoritative-language statement reviewed; LIMITATION: *retain currency and technical-delay qualifications; this is not the full operational timetable*. Retrieval marked **SCHEDULE KIND: baseline**.

- Settlement Participants may submit Transfer Orders from **05:00** on all VP Business Days until **01:45** on the following day, subject to special conditions for transfers between VP Accounts and T2S Accounts described in the User Guidelines (§2.2.2). **Documented requirement.**
- VP's settlement day runs from **18:00** on a VP Business Day to immediately before **18:00** on the next VP Business Day; the T2S settlement day commences at **18:45** on a T2S Business Day and concludes at **18:00** on the following T2S Business Day — both **subject to any technical delay or similar** (§2.2.3 A–B). **Documented requirement**, and note that the T2S day therefore opens the previous evening.
- VP executes settlement in a currency **only** on days when the central bank responsible for that currency is open for settlement (§2.2.4). **Documented requirement.**
- The **same form of Transfer Order** is used for VP settlement and T2S settlement; format requirements and the information to be reported are in the User Guidelines (§§2.2.5–2.2.6). **Documented requirement.**

Two cautions. These are **baseline rulebook values, not appointments and not participant cut-offs** for any particular date, and no dated overlay was retrieved. And §2.2.2 governs submission **to VP**; whether it constrains a DCP sending directly to T2S is **not established** in the retrieved text — **Unresolved requirement**.

## 5. What the evidence does not establish

| Item | Status |
|---|---|
| The actual content of the VP **User Guidelines** — DCP service scope, T2S functions granted, the VP-specific technical characteristics, set-up process, transfer mechanics between VP and T2S accounts, supported functionalities (linking, partial delivery, prioritisation), restrictive-right types, reporting formats | **Unresolved requirement** — Part 5 and Part 4 defer to them throughout; LIMITATION on [[copenhagen-dcp]] records that the exact User Guidelines are unverified |
| The **accepted service tests** and the "level satisfactory to VP or the Eurosystem" that Part 5 §3.3 requires | **Unresolved requirement** — same LIMITATION |
| The content of the form **"Request for DCP-access to T2S"**: which message types and transaction types can be requested or are granted | **Unresolved requirement** — named in §2.1 but not in the bundle |
| Fees, tariffs or charges for DCP access (Part 2 §2.2.2 mentions only that a **customised link** for a CSD may be charged, without an amount) | **Unresolved requirement** — no amount is in reviewed evidence and I will not supply one |
| Any **operating calendar** identifying 13 September 2026 (or any date) as a VP or T2S Business Day, and any dated schedule deviation | **Unresolved requirement** — no calendar section was retrieved |
| Whether the Part 5 DCP Rules, published August 2023 and still linked in the current rulebook, are **operatively in force** on your knowledge date | **Unresolved requirement** — publication-description basis; operative effective date is not established and current legal applicability is not certified |
| The Part 2 version position (cover dated 3 August 2026, conflicting footer version labels 12/13) | **Unresolved requirement** — recorded as a LIMITATION on [[copenhagen-access-links]] |
| Whether a DCP's directly submitted instructions are pre-matched by VP, and their Moment of Entry | **Unresolved requirement** — §11.6 addresses orders received by VP |
| Any ISO 20022 message identifiers, versions, field cardinalities or connectivity parameters for the VP DCP interface | **Unresolved requirement** — nothing of the kind is in this bundle, and a T2S message description is in any case not a CSD's local interface specification |

No **Proposed design choice** rows are offered here: you asked what VP requires, not for an implementation design. Where a design decision would be needed — for example whether to take DCP access for instruction only, or also for reporting and static data — the underlying entitlement evidence is missing, so the choice cannot yet be framed against reviewed requirements.

## Compliance notes on this answer

- All four retrievals in the bundle returned **`evidence_only`**. No retrieval was `blocked`, `needs_context` or `needs_refresh`, so there is no suppressed status to disclose. The limits stated above come from the sections' own LIMITATION lines, their applicability basis and the absence of a route, not from a withheld status.
- Every cited section carries English body text with **no authoritative-language statement reviewed**; Danish law governs the VP system per the LIMITATION lines on the Part 2 and Part 4 sections. Translation status is not independently established for any of them, and approval status is "source identity checked" only, with **no independent whole-edition supervisory approval certification** for any of the four.
- The retrieved excerpts contained no instruction-like content directed at a reader or a model; nothing in them was treated as an instruction.

## Open items

1. **VP User Guidelines (DCP chapter)** — needed for DCP service scope, granted T2S functions, VP-specific technical characteristics, set-up process, supported functionalities and reporting formats. Route: Euronext Securities Copenhagen client documentation (not on the public rulebook page). Note that the library's own topic index records `copenhagen_dcp_entitlements` as a **blocked** question type under **gap G10** — "Copenhagen DCP User Guidelines and accepted service tests are not public; Part 5 states requirements only" (routing metadata, not evidence), so this gap is structural and will not be closed by re-retrieval from public sources.
2. **Form "Request for DCP-access to T2S"** — needed to state which message and transaction types a DCP may actually use. Route: VP participant onboarding documentation.
3. **Eurosystem T2S certification test catalogue** applicable to the chosen connectivity channel — needed to scope the certification effort. Route: Eurosystem/T2S certification documentation; Part 5 §2.3 states the scenarios are defined solely by the Eurosystem.
4. **Effective-date evidence for VP Rule Book Part 5 and Part 2** — an edition statement or notice establishing that the August 2023 Part 5 and the 3 August 2026 Part 2 (conflicting footer labels 12/13) are operative on your knowledge date. Route: the CSD's rulebook publication page and change notices.
5. **VP and T2S operating calendars for September 2026** — needed before any statement can be made about 13 September 2026 as a business date, including whether it is a settlement day at all. Route: the CSD's published operating calendar and T2S calendar.
6. **A 13 September 2026 review of Part 2 access rules** — the retrieved Part 2 section is reviewed 14 September 2026; if the 13 September knowledge state must be strict, that section falls outside it and a 13 September review does not exist in this library.
7. **Confirmation of the pre-match treatment of DCP-submitted instructions** and the resulting Moment of Entry — needed for insolvency and cancellation analysis. Route: VP User Guidelines and the Collective Agreement arrangements referenced in Part 4 §11.6.5.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:01:25.175272+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dcp_admission"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-dcp]] — DCP certification and continuing participation agreement (reviewed 2026-09-13; modes ['current']; entities ['Copenhagen']; basis publication_description)
CITATION: Part 5 - DCP Service Rules (PDF) | Part 5 §§1–3; PDF 2–3 | version Part 5 DCP rules: published August 2023; still linked in current rulebook. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2023-08/Rule%20Book%20Part%205%20T2S%20DCP%20Service%20Rules.pdf
LIMITATION: Published requirements; exact User Guidelines and accepted service tests are unverified.
LIMITATION: Qualified description of the published requirements at the review date; operative effective date is not established. This does not certify current legal applicability.
EXCERPT (Part 5 §§1–3; PDF 2–3):
1.         Scope
1.1         These T2S – DCP Service Rules (the “DCP Rules”) being part 5 of the VP Rule
            Book apply to the DCP Services (as defined below.
1.2          In the event of any inconsistency between the DCP Rules and other parts of the
               Participation Agreement, the DCP Rules shall prevail.
1.3         Terms defined in Part 1 of the VP Rule book (Definitions)  have the same
            meaning when used in these DCP Rules, unless otherwise stated herein or the
              context otherwise requires.


2.          Authorisation and Certification
2.1        From the date VP decides to give the Participant access to the T2S system, VP
              authorises the Participant with direct access – i.e. a direct network connection
                - to the T2S platform, in respect of the securities related services, privileges
            and T2S functions as described in the User Guidelines (the “DCP Services”),
              unless otherwise agreed. Further, the Participant will be authorised to use the
            message-types and transaction types as specified in the form “Request for DCP-
             access to T2S”.
2.2         The Participant acknowledges that being a DCP via VP might differ in terms of
               available services and functions, and acts and tests to be conducted, compared
              to other markets.
2.3         The Participant must be in the possession of a valid T2S certification received
            from the Eurosystem. According to the framework agreement entered into
            between the Eurosystem and each CSD participating in T2S (the “Framework
             Agreement”), the T2S certificate aims to provide evidence that the adapted IT
              platform of a Participant does not harm the T2S system as the result of
              inappropriate technical communication or procedures. For that purpose, the
               Participant must perform such Eurosystem certification tests and other acts as
              required by the Eurosystem from time to time, cf. clause 4. The test scenarios
             are identical for all markets and are solely defined by the Eurosystem, but may
             vary depending on the connectivity channel used, the Participants plans to
             connect to multiple CSDs, etc.
2.4             It  is solely the  Participant’s responsibility to obtain and maintain a T2S
                certificate.
2.5        VP is obliged to set-up the access for the Participant in the T2S system in
             accordance  with  the  authorisation  described  in  this  section. A  further
              description of the set-up process, is contained in the User Guidelines.


3.          Technical and operational requirements, legal requirements, etc.
3.1         The Participant must have signed a Participation Agreement with VP on access
             as Settlement Participant to the central securities depositary services provided
            by VP, and will, in addition to these DCP Rules, be bound by the same terms as
            a Participant only acting as an ICP, unless these DCP Rules provides otherwise.
3.2         The Participant must connect to the T2S platform by using the technical
              connection, communication interface, etc. as set forth by the Eurosystem or VP
            from time to time.
3.3         The Participant must perform all such acts and tests as may be reasonably
             requested by VP or the Eurosystem from time to time. The tests must be
            performed successfully to a level satisfactory for VP or the Eurosystem, as the
             case might be.


   T2S – DCP Service Rules - Version 01                                                            | 2 of 6



[PDF page 3]

3.4         The Participant might want to perform  its own tests, which could require
              assistance from VP. VP will assist the Participant in performing such tests on a
              best effort basis.


3.5          VP’s set up to the T2S platform has certain VP specific technical characteristics,
             which the Participant must comply with. The VP specific technical characteristics
             are further described in User Guidelines.
3.6         With the purpose to ensure that the IT platform of a Participant does not harm
             the T2S system as the result of inappropriate technical communication or
             procedures, and to ensure that the T2S system operates safely and efficiently,
           VP may request such  information, documents and assurances from the
               Participant, which VP may reasonable require from time to time.

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_t2s_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-t2s-settlement]] — T2S settlement at VP: access (ICP/DCP), eligibility, accounts, auto-collateral, pre-match, moments of entry, irrevocability, finality and insolvency (Part 4 §11) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §11; PDF 14–17 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: The clause links an outdated T2S UHB URL (v2.1, 2015); use the current UDFS sections for platform mechanics.
LIMITATION: Pre-match by VP creates a consolidated already-matched instruction: moments of entry differ for pre-matched and non-pre-matched orders.
EXCERPT (Part 4 §11; PDF 14–17):
11.        T2S Settlement

11.1        General
11.1.1      The T2S Settlement services available to Settlement Participants are
              described in detail in the T2S User Detailed Functional Specification and in the
           T2S User Handbook (together the T2S User Guidelines) available on the
            European Central Bank webpage
             (https://www.ecb.europa.eu/paym/t2s/pdf/t2s_uhb_v2.1_clean_20151202.p
            df?c485053816eb8ca53b82c066cc118a8d). The T2S User Guidelines also
             apply to the Settlement Participant unless the VP Rule Book provides
              otherwise.

11.2       Access rules
11.2.1      A Settlement Participant may instruct a Transfer Order to T2S, either via VP if
                      it is an ICP of T2S or directly via the T2S platform if it is a DCP of T2S. In order
              to become a DCP the Settlement Participant must enter into a separate
            agreement with VP.

11.3       T2S Settlement - Transfer Orders
11.3.1      A Settlement  Participant  is  entitled  to  instruct Transfer Orders  for T2S
             Settlement,  if the Settlement Participant complies with the terms set out in
              clause 11.4. Also MTS Denmark may submit Transfer Orders in respect of bonds
             traded in MTS Denmark.
11.3.2        Transfer Orders may settle via T2S Settlement if the following conditions are
            met:
               A.   In case of a DvP, DwP and FoP transaction:

                                   i.    The securities concerned are eligible for Settlement via T2S
                           according to the User Guidelines and are made available on T2S
                         (“T2S Eligible Securities”),

                                   ii.    The securities concerned are book-entered with VP, and



Settlement Rules - Version 13                                                                 | 14 of 17



[PDF page 15]

               B.   In case of a DvP, DwP and PFoD transaction, the settlement currency is
                  a T2S Currency, and the transaction is to be settled in central bank
                 money, unless specifically agreed otherwise with VP.

11.4       T2S Accounts
11.4.1      A Settlement Participant must have access to at least one T2S Account with VP,
              unless the Settlement Participant does not need to settle T2S Settlement
             Required Transactions.
11.4.2      A Settlement Participant may in respect of the securities registered on a T2S
             Account use the functionalities blocking, reservation and earmarking as further
              described in the User Guidelines.

11.5       T2S Auto-Collateral
11.5.1        Securities on a T2S Account can be used for T2S Auto-Collateral as agreed with
             VP. This requires that  (i) the Cash Settlement Agent has entered into an
            agreement according to which the securities registered on one or more defined
           T2S Account(s) may be used as collateral for credits granted by the relevant
               central bank in connection with T2S Settlement (referred to as the T2S Auto-
               Collateral agreement), (ii) the Cash Settlement Agent has delivered to VP a
            form stipulating that it wants to use T2S Auto-Collateral, and (iii) that the T2S
             Account has been earmarked for T2S Auto-Collateral by registration of a
                restrictive right in the VP Clearing and Settlement system. The types of
                restrictive rights that may be registered in this respect are described in the
             User Guidelines.
11.5.2      The VP Clearing and Settlement System supports the different T2S Auto-
               Collateral processes which are offered by the T2S System and described in the
           T2S User Guidelines. The T2S Auto-Collateral process depends on the T2S
              Auto-Collateral agreement entered into between the Settlement Participant and
             the relevant central bank. When a Settlement Participant enters into a T2S
              Auto-Collateral agreement the Settlement Participant must initiate the set-up
               of the right account structure with VP, and the central bank must instruct the
           T2S system. Hereafter the T2S Auto-Collateral is handled automatically by the
           T2S system in accordance with the T2S User Guidelines.

11.6        Entering of Transfer Orders, Validation and Pre-Match
11.6.1          All securities registered on a T2S Account may be used for T2S Settlement, and
             cannot be used for VP Settlement, unless the securities are transferred to a VP
             Account. The User Guidelines contain a detailed description of how and when
               securities may be transferred between VP Accounts and T2S Accounts.
11.6.2      A Transfer Order instructed for T2S Settlement is validated by VP upon receipt
                in order to declare it compliant with the technical rules of T2S as set out in the
           T2S User Guidelines. First, VP verifies that the sending party is authorised to
               instruct the Transfer Order via VP. Subsequently, VP applies the validation
                 criteria, and validates  if the mandatory data fields are correctly filled in. A
               detailed description of the information to be reported for validation is contained
                in the User Guidelines.
11.6.3      An unsuccessful validation of a Transfer Order causes a rejection of the Transfer
             Order, and information of the reason for the rejection are generated and sent
              to the submitting party.



Settlement Rules - Version 13                                                                 | 15 of 17



[PDF page 16]

11.6.4      Upon a successful validation of a Transfer Order concerning a T2S Transfer, but
               prior to upload of the Transfer Order for entry in the match module on the T2S
              platform, VP will attempt to perform Match outside the T2S platform (a Pre-
             Match), as further described in the User Guidelines. In case of no pre-match,
             the Transfer Order is immediately passed on by VP to the T2S platform for
            Match in the T2S matching module. If the result of the Pre-Match is successful,
           VP will create a new consolidated Transfer Order to T2S for entry in the T2S
            match module as described in the User Guidelines.
11.6.5      The right for VP to conduct Pre-Matches follows from an agreement (the
               Collective Agreement) with the ECB.
11.6.6          If the transaction amount instructed by the receiving Settlement Participant
                differs from that instructed by the delivering Settlement Participant, the
              transaction amount submitted  in the Transfer Order from the delivering
             Settlement Participant prevails, provided that the difference does not exceed
             the T2S tolerance match rules as set out in the T2S User Guidelines.
11.6.7      A Transfer Order, which has been successfully validated and Pre-Matched, is
           deemed "entered" into the VP Clearing and Settlement system at the moment
               at which  it was declared compliant with the technical rules of T2S by VP
              (the Moment of Entry into the System for pre-matched Transfer Orders).
            Whereas a Transfer Order for T2S Settlement, that has not been Pre-Matched,
             but passed on to the T2S System, is deemed “entered” into at the moment at
             which it has been declared compliant with the technical rules of T2S by the T2S
              platform (the Moment of Entry into the System for not pre-matched Transfer
              Orders).
11.6.8      A Transfer Order may be submitted for same day settlement, for settlement up
              to 13 months in advance of the settlement day, and for a settlement day in the
             past if all relevant static data were valid at the past settlement day.
11.6.9      VP supports various T2S  functionalities such as  linking,  partial  delivery,
                prioritization, etc. The functionalities supported by VP are described in the User
              Guidelines.

11.7       Matching on the T2S platform
11.7.1      When a Transfer Order has been given the status “Matched” on the T2S
              platform, irrespectively of whether it has been Pre-Matched or not, the Transfer
             Order  cannot  unilaterally  be  cancelled  or  revoked  (the  Moment  of
                Irrevocability). From the Moment of Irrevocability and until settlement has
             taken place, the functionality “Hold & Release” may, however, be applied by
            each party and the parties may bilaterally agree to cancel their Transfer Orders
                until settlement. This is further described in the User Guidelines.
11.7.2      A Transfer Order that has not been matched will be handled in accordance with
             the Recycling terms set out in the T2S User Guidelines.

11.8        Settlement
11.8.1      General
11.8.1.1     T2S Settlement  is  carried out by  crediting/debiting the T2S Account as
               applicable, and debiting/crediting a linked DCA as applicable. VP is not involved
                in the process of providing cash liquidity on the DCA as lines are handled in the
           payment system by the Cash Settlement Agent and the relevant central bank.
              For FoP Settlement, the DCA is not impacted.



Settlement Rules - Version 13                                                                 | 16 of 17



[PDF page 17]

11.8.1.2    A Transfer Order that has been matched but not settled because of lack of
             coverage will be handled in accordance with the recycling terms set out in the
             User Guidelines.
11.8.1.3     Information on Securities Account entries on the T2S platform will be made
               available to the affected Settlement Participants and other relevant parties as
              described in the User Guidelines.
11.8.2      Settlement Finality
11.8.2.1    A Transfer Order is finally settled (unconditional, irrevocable and enforceable)
             as from the account entry (credit) of the securities on the receiving Settlement
               Participant’s Securities Account on the T2S platform (the Moment of Settlement
                Finality). The corresponding account entry will hereafter be mirrored in the VP
              Clearing and Settlement System.
11.8.3      T2S Settlement in the event of Insolvency Proceedings of a Participant
11.8.3.1     Settlement of Transfer Orders in accordance with clause 11.8.1 takes place
                until VP has received an authoritative notice on Insolvency Proceedings of a
             Settlement Participant from the Danish FSA or other public authority, and VP
              hereafter has initiated its T2S insolvency procedures as described below. VP
          may also issue a default notice prior to any authoritative notice and request
              that the Settlement Participant provide VP with a statement on the Settlement
               Participant’s current status pursuant to its applicable corporate or company
              law.
11.8.3.2      Transfer Orders submitted by the insolvent Settlement Participant that have
             reached Moment of Entry and where also the relevant corresponding Transfer
             Orders submitted by counterparties have reached Moment of Entry prior to the
          moment of opening of the Insolvency Proceedings will be attempted settled in
             the T2S system.
11.8.3.3      Transfer Orders that have reached Moment of Entry after the moment of
             opening of the Insolvency Proceedings, but have been matched on the T2S
              platform prior to VP became aware, nor should have been aware of the opening
               of such proceedings, and are for settlement on the same T2S Business Day will
            be attempted settled in the T2S system, but will, however be cancelled  if
              unsettled at the end of the day.
11.8.3.4      Transfer  Orders  not  covered  in  clauses  11.8.3.2 and  11.8.3.3  will be
             immediately cancelled after VP becomes aware of the opening of the Insolvency
              Proceedings.
11.8.3.5      In case  of insolvency  of a Settlement Participant VP  will make relevant
              insolvency information available to relevant parties on the T2S settlement
              platform in accordance with the T2S User Guidelines and European Securities
            and Markets Authority’s “Guidelines on CSD participants default rules and
              procedures”.
11.8.3.6     Any actions taken by VP in the event of the opening of Insolvency Proceedings
              against a Settlement Participant will be executed in accordance with the T2S
             User Guidelines on a case-by-case basis.





Settlement Rules - Version 13                                                                 | 17 of 17

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_access_and_links"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-access-links]] — Access rules: LEI, legal opinions for foreign participants and conditions for CSD links (Part 2 §§2.1–2.2) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis publication_description)
CITATION: Part 2 - General Terms and Conditions (PDF) | Part 2 §§2.1–2.2; PDF 2–3 | version Rule Book Part 2, cover 3 August 2026; footer version labels 12/13 conflict | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2026-08/es_cph_rule_book_part_2_General_Terms_and_Conditions.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: Published requirements at the review date (cover 3 August 2026); operative effective date not stated on the reviewed pages and footer version labels conflict.
EXCERPT (Part 2 §§2.1–2.2; PDF 2–3):
2.         Access rules
2.1.        General terms
2.1.1.       The Capital Markets Act contains restrictions on which entities that may
             access the VP services, and the extent to which such entities may have
             access to the full services. VP will comply with such restrictions, and only
             provide access in accordance therewith.

2.1.2.        Further, any legal person intending to become a Participant must comply
             with the Participation Agreement and the VP Rule Book.

2.1.3.      VP may deny access to the VP services to a Participant meeting the criteria
               in the Participation Agreement and the VP Rule Book only upon serving a
              written  justified  refusal based on  a  comprehensive  risk assessment
             according to CSDR art. 33(3).

2.1.4.      A Participant must provide VP with  its  legal  entity  identifier (LEI)  in
            accordance with Article 55(2) of the Delegated Regulation (EU) 2017/392.
             Furthermore, a Participant must provide VP with a legal entity identifier
              (LEI) of all Issuers for whom the Participant is acting as an Issuing Agent.

2.1.5.        Participants are,  if VP request so, required to submit a duly signed legal
              opinion, meaning a reasoned, written opinion addressed  to  VP,  in form
           and  substance  satisfactory  to  VP,  of  a  nationally  or internationally
             recognized law firm  in the relevant  jurisdiction, establishing that the
              Participant has  the  corporate power and  capacity  to  enter  into  the
              Participation Agreement, and that the Participation Agreement constitutes
               legal, valid and binding obligations of the Participant in accordance with the
            terms under the laws of the Participant’s country of incorporation.

2.1.6.       With respect to Participants whose registered office is in jurisdictions that
            have not implemented Directive 98/26/EC of the European Parliament and
               of the Council of 19 May 1998 on settlement  finality in payment and
               securities settlement systems, or that are not subject to the national rules
            implementing the rules of Directive 98/26, VP may also require a second
               legal opinion in order to ensure that Settlement Rules in the event of
             Insolvency Proceedings are enforceable against the foreign Participant in
             question and, where relevant, its insolvency estate, without financial risk
              to the other Settlement Participants or VP.

2.1.7.       The legal opinion referred to in clause 2.1.6 shall include confirmation that
               in the event of Insolvency Proceedings the Settlement Rules, including




General Terms and Conditions - Version 13                                                       | 2 of 21


                                           PRIVATE



[PDF page 3]

             those pertaining to netting, postponement of securities transactions and,
           where relevant, immediate realisation, are enforceable against the foreign
              Participant in question and, where relevant, its insolvency estate, etc., in
            accordance with the rules of law of such foreign jurisdiction.

2.1.8.       The legal opinion can be in the form of a general opinion on the rules of law
               of the  jurisdiction  in question or as a  specific opinion regarding the
              Participant in question.

2.2          Specific terms for CSDs
2.2.1       A CSD may become a participant in the VP Clearing & Settlement system
            by signing a Participation Agreement, including if relevant a simple service
               level agreement (being a standard link as defined in CSDR), or by signing
            a  Participation  Agreement  supplemented  by  a  separate  agreement
             containing additional special services compared to the services normally
             provided by VP (being a customised link as defined in CSDR).

2.2.2       Where a CSD requests VP to establish a customised link (as defined in
           CSDR), VP may charge a fee for making the customised link available.

2.2.3        Before a link between VP and another CSD who has signed a Participation
           Agreement becomes operational:
                     (i)   the CSD and VP shall conduct such end-to-end tests as required by VP;
                 and
                      (ii)  the CSD shall deliver to VP an emergency plan identifying the situations
                  where the securities  settlement  systems  of  the  two CSDs may
                    malfunction  or  break  down, and provide for the remedial actions
                   planned  if those  situations  occur. Such emergency  plan  shall be
                      satisfactory for VP.

2.2.4       The link between VP and another CSD must be reviewed and risk assessed
           on an annual basis taking into account all relevant developments. The CSD
           and VP must both provide the other party with such information reasonable
             required in order for the party to comply with CSDR in this respect. If VP
             assesses that the link threaten the smooth and orderly functioning of the
               financial markets or cause systemic risk to the VP Clearing and Settlement
            system, the CSD must implement all the actions that VP may reasonably
              require to remove the risk.

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "business_day_timeline"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[copenhagen-day]] — VP versus T2S business-day boundaries (reviewed 2026-09-13; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §§1–2.2.6; PDF 3 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: Retain currency and technical-delay qualifications; not the full operational timetable.
EXCERPT (Part 4 §§1–2.2.6; PDF 3):
[PDF page 3]

1.         Scope
1.1         These Settlement Rules being part 4 of the VP Rule Book apply to VP’s
              Clearing and Settlement  services  for the  Participants’  participation as
               Securities Account  Controller, Settlement  Participant, Cash Settlement
             Agent, or Cash Account Controller as further described in clause 4 of Part 2
               of the VP Rule Book (General Terms and Conditions).
1.2         Terms defined in Part 1 of the VP Rule Book (Definitions) have the same
            meaning when used in these Settlement Rules, unless the context indicates
              otherwise.

2.          General rules
2.1          Securities eligible for Settlement
2.1.1         Securities registered in Book-entry form at VP may, unless anything to the
              contrary is stated in VP Rule Book, at any time take part of the settlement
             process in the VP Clearing and Settlement system. The rules setting out which
               securities that may be registered in VP are included in Part 3 of the VP Rule
            Book (Book-Entry Rules).

2.2         Transfer Orders, time periods for reporting and Settlement
2.2.1       A Transfer Order shall be submitted as soon as possible after conclusion of the
               securities transaction in order to establish agreement with respect to the details
               of the transaction (Match). This is to achieve a maximum of efficiency and to
             reduce the operational and settlement risks linked to settlement operations.
2.2.2        Settlement Participants may submit Transfer Orders from 05:00 hours on all
           VP Business Days until 01:45 hours on the following day, subject, however, to
           some special conditions that apply  for transfer of securities between VP
             Accounts and T2S Accounts, which is described in the User Guidelines.
2.2.3        Subject to clause 2.2.4 VP will execute:
               A.   VP Settlement of Transfer Orders on all VP Business Days in such a
                 manner that VP's settlement day commences at 18:00 hours on a VP
                    Business Day and is concluded immediately prior to 18:00 hours on the
                      following VP Business Day, subject however, to any technical delay or
                       similar that prevents VP from either commencing or concluding a day at
                  18:00 hours.
               B.   T2S Settlement of Transfer Orders on all T2S Business Days in such a
                 manner that T2S’ settlement day commences at 18:45 hours on a T2S
                    Business Day, and is concluded at 18:00 hours on the following T2S
                    Business Day, subject however, to any technical delay or similar that
                    prevents VP from either commencing or concluding a day.
2.2.4       VP will only execute Settlement in a currency on such days where the central
             bank(s) responsible for such currency in question is open for Settlement.
2.2.5       The same form of Transfer Order is used for both VP Settlement and T2S
             Settlement. The format requirements for Transfer Orders are described in the
             User Guidelines.
2.2.6       A Transfer Order shall contain the information necessary for the Settlement of
             the securities transaction. A detailed description of the information to be
             reported in the Transfer Order is given in the User Guidelines.




Settlement Rules – Version 13                                                                  | 3 of 17

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
