You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Which test cases in the Copenhagen DCP User Guidelines must we pass before going live as a DCP?

# Case category: missing-source (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Copenhagen DCP entitlements/User Guidelines are blocked (G10); Part 5 requires tests but the guide is not public.",
  "Publication-description basis of Part 5 preserved."
]
Fail conditions (must NOT appear):
[
  "List test cases."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked', 'evidence_only']

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
# Copenhagen (VP) DCP go-live: which test cases must be passed

## Direct answer

**Unresolved requirement — the test cases cannot be listed.** The Copenhagen DCP User Guidelines are not in reviewed evidence, and the retrieval aimed at them returned **blocked**. What the reviewed rulebook does establish is the *obligation structure*: you must hold a valid Eurosystem T2S certification, whose test scenarios are defined solely by the Eurosystem (not by VP), and you must additionally perform all acts and tests reasonably requested by VP or the Eurosystem, successfully and to their satisfaction. The individual test cases sitting behind those obligations are named in documents this bundle does not contain. (DCP — directly connected participant: a participant that sends instructions straight to the T2S platform rather than through the CSD; ICP — indirectly connected participant, which instructs via the CSD.)

## Retrieval statuses (disclosure)

| Retrieval | Context | Status | Consequence |
|---|---|---|---|
| 1 | Copenhagen / settlement / current / `copenhagen_dcp_entitlements` | **blocked** — gap **G10** | Retriever reason: "Copenhagen DCP User Guidelines and accepted service tests are not public; Part 5 states requirements only." No test-case list, no acceptance criteria per test, no service-entitlement matrix is admitted. |
| 2 | Copenhagen / settlement / current / `dcp_admission` (as of 13 September 2026) | evidence_only | Supports the certification and testing *obligations* in Part 5. |
| 3 | Copenhagen / settlement / current / `copenhagen_t2s_settlement` (as of 14 September 2026) | evidence_only | Supports the access rule that DCP status requires a separate agreement with VP. |

Any count, name, identifier or pass/fail threshold of a specific test case would be fabrication and is therefore absent from this answer.

## Documented requirements (what you must satisfy, from the reviewed rulebook)

All rows below rest on [[copenhagen-dcp]] Euronext Securities Copenhagen VP Rule Book Part 5 — T2S DCP Service Rules, §§1–3, PDF 2–3, Version 01, published August 2023 and still linked in the current rulebook; section reviewed 13 September 2026, source reviewed 13 September 2026; applicability basis is **publication_description** — this is a qualified description of the **published** requirements at the review date, the operative **effective date** is **not established**, and it does not certify current legal applicability; body language English, no authoritative language independently established; source identity checked, with no independent whole-edition supervisory approval certification.

| # | Obligation | Label | Locator |
|---|---|---|---|
| 1 | The Participant must be in possession of a valid T2S certification received from the Eurosystem. | Documented requirement | Part 5 §2.3 |
| 2 | For that purpose the Participant must perform such Eurosystem certification tests and other acts as required by the Eurosystem from time to time (the clause cross-refers to clause 4, which is **not in the reviewed excerpt**). | Documented requirement | Part 5 §2.3 |
| 3 | The test scenarios are identical for all markets and are **solely defined by the Eurosystem**, but may vary depending on the connectivity channel used, on the Participant's plans to connect to multiple CSDs, and similar factors. | Documented requirement | Part 5 §2.3 |
| 4 | Obtaining and maintaining the T2S certificate is solely the Participant's responsibility. | Documented requirement | Part 5 §2.4 |
| 5 | The Participant must perform all such acts and tests as may be reasonably requested by VP or the Eurosystem from time to time; the tests must be performed successfully to a level satisfactory for VP or the Eurosystem, as the case may be. | Documented requirement | Part 5 §3.3 |
| 6 | The Participant must have signed a Participation Agreement with VP for access as Settlement Participant and is bound by the same terms as an ICP-only Participant unless the DCP Rules provide otherwise; where the DCP Rules and other parts of the Participation Agreement are inconsistent, the DCP Rules prevail. | Documented requirement | Part 5 §§1.2, 3.1 |
| 7 | The Participant must connect to T2S using the technical connection and communication interface set forth by the Eurosystem or VP from time to time. | Documented requirement | Part 5 §3.2 |
| 8 | VP's set-up to T2S has VP-specific technical characteristics with which the Participant must comply; these are **further described in the User Guidelines**. | Documented requirement (content of the characteristics: **not in reviewed evidence**) | Part 5 §3.5 |
| 9 | Authorisation covers the securities-related services, privileges and T2S functions described in the User Guidelines, and the message types and transaction types specified in the form "Request for DCP-access to T2S". | Documented requirement (the service list, the message types and the form itself: **not in reviewed evidence**) | Part 5 §2.1 |
| 10 | Being a DCP via VP may differ from other markets in available services and functions and in the **acts and tests to be conducted**. | Documented requirement | Part 5 §2.2 |
| 11 | The Participant may run its own tests; VP assists on a best-effort basis only. | Documented requirement | Part 5 §3.4 |
| 12 | VP may request such information, documents and assurances as it may reasonably require, to ensure the Participant's IT platform does not harm T2S. | Documented requirement | Part 5 §3.6 |

**Documented requirement.** To become a DCP, a Settlement Participant must enter into a **separate agreement with VP**; a Settlement Participant may instruct a Transfer Order to T2S either via VP as an ICP or directly via the T2S platform as a DCP — [[copenhagen-t2s-settlement]] VP Rule Book Part 4 — Settlement Rules, §11.2.1, PDF 14–17, Version 13, version date 1 May 2025; section reviewed 14 September 2026, source reviewed 13 September 2026; English rulebook text, **Danish law governs the VP system** and no authoritative-language statement was reviewed; source identity checked, no independent whole-edition supervisory approval certification.

## Two "User Guidelines" — a terminology trap in your question

**Reasoned inference (derived from comparing [[copenhagen-dcp]] Part 5 §§2.1, 2.5, 3.5 with [[copenhagen-t2s-settlement]] Part 4 §11.1.1).** The phrase "User Guidelines" carries two different referents in this rulebook:

1. In Part 4 §11.1.1, "the T2S User Guidelines" is defined as the **T2S User Detailed Functional Specification and the T2S User Handbook** published on the ECB webpage. LIMITATION attached: the clause links an outdated T2S User Handbook URL (v2.1, 2015); the current UDFS sections should be used for platform mechanics, and neither the UDFS nor the UHB is in this bundle.
2. In Part 5 (§§2.1, 2.5, 3.5), "the User Guidelines" is the document describing **VP's own** set-up process, VP-specific technical characteristics and the DCP service scope.

Your question presumes a VP-issued "DCP User Guidelines" containing an enumerated test-case catalogue. The reviewed text does not show that such a catalogue exists there: Part 5 §2.3 places the *certification* test scenarios with the **Eurosystem**, while Part 5 §3.3 leaves VP's additional tests open-ended ("as may be reasonably requested … from time to time"). Whether the VP User Guidelines nevertheless enumerate named VP tests is **not in reviewed evidence** — this is an inference about where the requirement lives, not a finding that no list exists.

## Proposed design choices (for your go-live plan; not infrastructure rules)

- Split your test plan into two tracks that have different owners: the **Eurosystem certification track** (scenarios defined solely by the Eurosystem, varying with connectivity channel and multi-CSD ambitions per Part 5 §2.3) and the **VP acceptance track** (open-ended, satisfaction-based per Part 5 §3.3). Do not assume a single combined checklist.
- Because Part 5 §3.3 sets a satisfaction standard rather than an objective pass mark, obtain VP's written statement of what "successfully … to a level satisfactory" means for your scope **before** you baseline a go-live date. The rulebook gives you no entitlement to a fixed criterion.
- Record your connectivity channel and whether you will connect to multiple CSDs early: Part 5 §2.3 makes both of these variables that change the test scenarios that apply to you.

## Unresolved requirements

- The enumerated **test cases**, their identifiers, sequencing, environments, data prerequisites and pass criteria — **not in reviewed evidence** (blocked, gap G10).
- Part 5 **clause 4**, cross-referenced by §2.3 as the certification clause, is outside the reviewed excerpt — **not in reviewed evidence**.
- The **"Request for DCP-access to T2S" form** and the message types and transaction types it specifies — **not in reviewed evidence**; do not infer a message set from T2S documentation.
- The **service entitlements and privileges** a VP DCP receives, and the VP-specific technical characteristics of §3.5 — **not in reviewed evidence**.
- Whether the published Part 5 text is the version legally in force at your intended go-live date — **not established**; the section's applicability basis is a description of the published document at the review date, with no operative effective date established.

## Open items

1. **Gap G10 (blocked topic `copenhagen_dcp_entitlements`)** — the Copenhagen DCP User Guidelines and the accepted service tests are not public; Part 5 states requirements only. Needed: the VP DCP User Guidelines edition applicable at your go-live date, with its version and effective date.
2. **Eurosystem certification test scenarios** — per Part 5 §2.3 these are defined by the Eurosystem, not by VP; the scenario catalogue applicable to your connectivity channel is not in reviewed evidence and must come from the Eurosystem/ECB certification material.
3. **Part 5 clause 4 and the "Request for DCP-access to T2S" form** — both are referenced by the reviewed text but not contained in it.
4. **Effective-date confirmation** for VP Rule Book Part 5 (Version 01, published August 2023) and Part 4 (Version 13, 1 May 2025), since Part 5's operative effective date is not established in reviewed evidence.
5. **Official route** — request items 1–4 through the Euronext Securities Copenhagen client documentation/relationship channel for the non-public DCP material, and through the Eurosystem's T2S certification process for the certification scenarios. I do not draft or send that request.

Review dates of the evidence used: 13 September 2026 for the Part 5 DCP section, 14 September 2026 for the Part 4 T2S settlement section (both sourced from reviews dated 13 September 2026). Nothing here is asserted as verified beyond those dates.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:57:12.098932+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_dcp_entitlements"}
STATUS: blocked — Copenhagen DCP User Guidelines and accepted service tests are not public; Part 5 states requirements only.
GAP IDS: ['G10']

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "dcp_admission"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_t2s_settlement"}
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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
