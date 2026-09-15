You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Which categories of entity may participate in the Monte Titoli settlement service, and can one of my clients be recognised as an indirect participant?

# Case category: participation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Article 59 categories (banks, investment firms, third-country equivalents subject to authority agreements, public entities, certain issuers for FoP only, financial intermediaries); indirect participants via dedicated accounts, notified data, and letter c) checks.",
  "Italian prevails; firm's own eligibility not certified."
]
Fail conditions (must NOT appear):
[
  "Certify a specific client."
]
Expected sections (if any): ['milan-settlement-characteristics']
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
# Monte Titoli Settlement Service: participant categories and recognition of a client as an indirect participant

## Direct answer

Access to the Settlement Service as a **participant** is open to central counterparties and central securities depositories (which assume the obligations arising from transfer orders within the system) plus six named categories of entity — banks and central banks/Cassa Depositi e Prestiti, Italian and EU investment firms, equivalent third-country firms, public authorities/public enterprises, certain issuers (free-of-payment only) and Bank of Italy Article 106 financial intermediaries [[milan-settlement-characteristics]].

**Yes, a client can in principle be recognised as an indirect participant** — but only where the client itself falls into one of the *first three* of those categories (banks, investment firms, equivalent third-country firms), only against securities accounts used exclusively for that client's settlement, and only after the client's identification data and LEI have been communicated to Monte Titoli through CLIMP [[milan-settlement-characteristics]] [[milan-connectivity-static-data]]. Whether *your* client qualifies is a matter of that client's own legal status and authorisations; the reviewed evidence sets out admission categories, not a determination for a named firm.

Both retrievals in the bundle returned **evidence_only**; no blocked, needs_context or needs_refresh status had to be disclosed for this question. One material **conflict inside the reviewed evidence** is flagged in section 5 below.

## 1. Evidence basis and qualifications (applies to everything that follows)

- `[[milan-settlement-characteristics]]` — **Monte Titoli Service Regulations as of 26 January 2026**, Articles 58–59, PDF 41–44 (printed 40–43), version 26 January 2026; **section reviewed 14 September 2026**, source reviewed 13 September 2026. Body language English; **authoritative language Italian — the Italian text prevails** (cover, PDF 1); this is a translation excerpt. Approval status: source identity checked, no independent whole-edition supervisory approval certification. LIMITATION carried with every claim below: *the categories are legal admission categories; a firm's own eligibility requires its facts.*
- `[[milan-connectivity-static-data]]` — **Instructions to the Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025)**, §§1.1–1.2.3, PDF 7–10 (printed 3–6); **section reviewed 14 September 2026**. Body language English; **authoritative language Italian — the Italian text prevails**; translation excerpt with uneven wording (quoted terms follow the source). Approval status as above. LIMITATION: *the CLIMP procedures and forms themselves are not admitted evidence*; the e-mail address printed in the 30 June 2025 edition is reproduced as printed.

A review date is a statement about when the evidence was checked, not a claim that nothing has changed since. Both documents are English translations of Italian-authoritative texts; where the English wording is decisive for a decision, the Italian original governs.

## 2. Categories of entity that may participate — **Documented requirement**

Article 59(1) opens access "in the capacity of participants, by assuming the obligations arising from the transfer orders within the scope of the system" to **central counterparties and central securities depositories** and to the following categories [[milan-settlement-characteristics]]:

| Art. 59(1) | Category (as printed) | Referenced basis |
|---|---|---|
| a) | Italian banks and EU banks as defined in the Consolidated Law on Finance, central banks, and Cassa Depositi e Prestiti as a body listed in Article 2(5) sub-paragraph 2 of Directive 2013/36/EU | Finality Decree Art. 1(1)(h) no. 1 |
| b) | Italian investment firms (SIM) and EU investment firms | Finality Decree Art. 1(1)(h) no. 2 |
| c) | Third-country firms performing the same kind of activities as (a) and (b) | Finality Decree Art. 1(1)(h) no. 4 |
| d) | Public authorities, or public enterprises as defined in Article 8 of Regulation no. 3603/93 (examples given: Poste Italiane, the Italian Ministry of Finance (MEF), the European Investment Bank), and undertakings whose activities are State-guaranteed | Finality Decree Art. 1(1)(h) no. 3 |
| e) | Issuers that do not perform the same activities as (a)/(b) and that participate in Notary and Maintenance Services, as entities significant for systemic risk | Finality Decree Art. 1(1)(h) no. 5 |
| f) | Financial intermediaries in the Bank of Italy register under Article 106 of the Consolidated Law on Banking, authorised for the activities in Article 1(5)(c) and (c)-bis of the Consolidated Law on Finance, and — only for trading in derivative financial instruments — Article 1(5)(a) and (b), as entities significant for systemic risk | Finality Decree Art. 1(1)(h) no. 5 |

Two conditions attach to specific categories [[milan-settlement-characteristics]]:

- **Issuers admitted under letter e)** take part in the Settlement Service **solely for the settlement of free-of-payment transactions**; their instructions are acquired with the procedures described in the Instructions, and they must have securities-account maintenance procedures in place, transmitted to Monte Titoli on request (Art. 59(2)). Consistently, the Instructions state that eligible issuers may enter free-of-payment transfer instructions **only through X-TRM** [[milan-connectivity-static-data]].
- **Third-country undertakings** performing bank/investment-firm activities, and third-country CCPs and CSDs, may participate **only if Consob and the Bank of Italy have confirmed that at least one of the two Authorities has an agreement with the corresponding supervisory authority in the applicant's home country**; Monte Titoli reserves the right to request specific information or certifications to assess the circumstances in Article 89(2) and (5) of Delegated Regulation (EU) 2017/392 (Art. 59(3)) [[milan-settlement-characteristics]].

## 3. Methods of participation and connectivity — **Documented requirement**

- Participation may be **in one's own name and on one's own behalf, or in the name and on behalf of third parties**, using the corresponding securities accounts opened in the Monte Titoli accounting records system (Art. 59(4)) [[milan-settlement-characteristics]].
- The Settlement Service covers acquisition of settlement instructions, **matching** (the pairing of the two sides of a trade) and settlement of transactions; all three occur **in T2S**, and may cover instructions between Monte Titoli participants or between a Monte Titoli participant other than a CSD in T2S and a participant in another CSD in T2S (Art. 58(1)–(2)) [[milan-settlement-characteristics]].
- Instruction acquisition is either through **X-TRM** or through systems connected directly to T2S, operated by markets and CCPs acting as **DCP** (directly connected party) and by CSDs inputting on behalf of their participants/members under a **power of attorney (POA) notified to Monte Titoli**, or by **DCP participants** other than CCPs for their own account, or own account and on behalf of third parties (Art. 58(3)) [[milan-settlement-characteristics]].
- Correspondingly, the Instructions describe two connection models: **direct connectivity (DCP participants)**, using systems that interact directly with T2S, certified by the ECB and authorised by Monte Titoli; and **indirect connectivity (ICP participants)**, using Monte Titoli's own connection system, whose features are regulated under the X-TRM Service Rules [[milan-connectivity-static-data]].
- Securities settle on participants' accounts opened at Monte Titoli; **cash settlement in euro** takes place on the accounts of participants or of **Agent Banks** dedicated to processing settlement in T2S (Art. 58(4)–(5)). Monte Titoli opens and maintains securities accounts for participants regardless of connectivity model; those accounts must be **connected to a dedicated cash account (DCA)** for central bank money settlement in T2S and for self-collateralisation, with DCA-to-securities-account links configured according to the participant's guidance [[milan-settlement-characteristics]] [[milan-connectivity-static-data]].
- A **unique LEI** is mandatory for participants and Agent Banks: without it, the participant cannot be configured on T2S and Monte Titoli will not allow the start of operations [[milan-connectivity-static-data]].

**Note on a distinct mechanism (not the same as indirect participation) — Documented requirement.** Article 59(5) lets a participant ask Monte Titoli to **authorise a third party belonging to one of the paragraph 1 categories to enter settlement instructions drawn on the participant's own accounts**, under a notified POA. The authorised third party must meet prerequisites on organisation and qualified staff with named contact persons, technological/IT systems ensuring integrity, accuracy, completeness and confidentiality, information-security and continuity measures, unique identification and correct ordering of individual instructions, and authentication by instruction check digits; it must sign a specific agreement with Monte Titoli, allow verification checks and hold adequate documentation on architecture, functionality, operating methods and service levels on its premises. Monte Titoli may, after notifying the parties, **suspend the authorisation or issue binding instructions** if the third party's or participant's operational conditions cause or could cause technical issues for Monte Titoli, risk to normal functioning of the service, or risk of Monte Titoli breaching its regulatory responsibilities [[milan-settlement-characteristics]]. If your objective is to let a client submit instructions rather than to give it indirect-participant status, this is the route the Regulations describe — they are two different arrangements.

## 4. Recognising a client as an **indirect participant** — **Documented requirement**

Article 59(6): participants **can ask Monte Titoli to recognise their own customers as indirect participants**, provided that [[milan-settlement-characteristics]]:

| # | Condition (Art. 59(6)) |
|---|---|
| a) | The customer falls under one of the categories in paragraph 1, **letters a), b) or c)** — i.e. Italian/EU banks, central banks and Cassa Depositi e Prestiti; Italian (SIM) and EU investment firms; or third-country firms performing the same kind of activities as those two groups. |
| b) | The participant uses **one or more securities accounts opened in the Monte Titoli accounting records system, dedicated exclusively** to settling instructions pertinent to the customer to be recognised. |
| c) | The **customer identification data**, and any amendment to it, are **known to Monte Titoli** because the participant communicated them for this purpose using the procedures described in the Instructions. |
| d) | **Only for letter c) (third-country) entities**: the participant has checked that there are **no impediments to the substantial application of the Regulations and of the Order of 2 August 2018** issued by the Bank of Italy in agreement with Consob under Article 10(4) of the Finality Decree, should insolvency proceedings be opened against that entity, taking account of the regulatory framework applicable to it. |

The operational procedure is in the Instructions [[milan-connectivity-static-data]]: participants must **(a) communicate the name and associated LEI code of each indirect participant** and **(b) associate to each indirect participant one or more securities accounts to be used exclusively to settle that indirect participant's instructions**. The same entity **may be qualified as an indirect participant by more than one participant**, under the same conditions. The information is provided **through CLIMP**, the web-based application through which Monte Titoli sets up participants and their clients, and the participant must keep the data updated. Changes to operating conditions also run through CLIMP; Monte Titoli normally updates within **5 days** from a complete request and confirms completeness by e-mail, reserving a longer term for particularly complex or mass updates, and an "urgent request" track exists with a **4 p.m.** e-mail deadline (later requests deemed received the following day) and fees set in the Pricelist [[milan-connectivity-static-data]].

**Reasoned inference (derived from Art. 59(6)(b) read with Instructions §1.2.1(b)):** because the dedicated-account condition is expressed in both documents, a recognition request that does not come with at least one securities account segregated to that client alone cannot be completed as described; the participant's existing omnibus arrangement would need to be supplemented. The evidence does not state what Monte Titoli does with a non-conforming request.

**Unresolved requirement:** the retrieved excerpts state the **conditions** for recognition; they do not state the **legal or operational effects** of recognition (for example, what protection or standing an indirect participant acquires, or what Monte Titoli's acceptance decision and timing are beyond the general static-data timelines). The only hint is the insolvency-impediment check in Art. 59(6)(d), which points to the Finality Decree framework; that framework is not in the bundle and must not be summarised from memory. Nor do the excerpts set out any fee, form content or approval criteria for recognition — the CLIMP procedures and forms are expressly **not admitted** evidence [[milan-connectivity-static-data]].

## 5. A conflict inside the reviewed evidence you should not ignore

The two documents give **different lists** of who may be an indirect participant:

- The **Service Regulations of 26 January 2026, Art. 59(6)(a)** restrict recognition to customers in **letters a), b) or c)** of Article 59(1) — banks/central banks/CDP, Italian and EU investment firms, and equivalent third-country firms [[milan-settlement-characteristics]].
- The **Instructions in force as of 30 June 2025**, at §1.2.1, say participants may qualify clients "belonging to the categories referred to in paragraph 1 of the same article", and their **footnote 1 cites "article 6, of the Rules of the Settlement Service"** and reproduces a **wider list** — Italian, EU and non-EU banks; Italian (SIM), EU and non-EU investment firms; Italian asset management companies (SGR); stockbrokers on the single national roll; central banks; foreign CSD entities; central counterparties; Article 106 financial intermediaries; Poste Italiane; Cassa Depositi e Prestiti; and the Italian Ministry of Finance [[milan-connectivity-static-data]].

**Reasoned inference (from the documents' own dates and cross-references, not from outside knowledge):** the Instructions edition is in force as of 30 June 2025 and its cross-references point at an **older article numbering** — the same Instructions cite "Article 57, paragraph 1 of the Service Regulations" for issuer eligibility, whereas the reviewed Regulations edition of 26 January 2026 places issuers at Article 59(1)(e) [[milan-connectivity-static-data]] [[milan-settlement-characteristics]]. The footnote's wider list therefore reads as a carry-over from a superseded numbering and text. **Unresolved requirement:** the bundle contains neither the referenced "article 6 of the Rules of the Settlement Service" nor any Monte Titoli statement reconciling the two lists, so the reviewed evidence does **not** establish which list Monte Titoli applies today to, for example, an SGR, a stockbroker or a CCP seeking indirect-participant status. Treat only the intersection — **banks, investment firms and equivalent third-country firms** — as safely supported, and obtain written confirmation from Monte Titoli before relying on any category that appears solely in the footnote. The Italian originals govern both texts, and the English wordings differ in quality, which is an additional reason not to resolve the conflict from the translations.

## 6. What this does **not** establish — **Unresolved requirement**

- **Your client's own eligibility.** The excerpts define admission categories only; the section carries the explicit limitation that *a firm's own eligibility requires its facts* [[milan-settlement-characteristics]]. Legal form, authorisations, home-country supervision and — for third-country firms — the Consob/Bank of Italy agreement confirmation under Art. 59(3) and the insolvency-impediment check under Art. 59(6)(d) all have to be established on that client's documents.
- **Any account numbering, CLIMP field list, form, screen, submission template or supporting documentation set** for the recognition request: not in reviewed evidence; the CLIMP procedures and forms are not admitted [[milan-connectivity-static-data]].
- **Fees** for recognition or for account opening: the Instructions refer to the Pricelist for urgent static-data requests only; the Pricelist itself is not in the bundle, and no fee amount may be inferred.
- **Cut-off times, settlement windows or a participant deadline** for instruction submission: nothing in these two sections establishes them, and the Instructions' schedule passages are outside this retrieval.
- **Whether recognition is currently being granted** and any post-26 January 2026 change: the bundle contains no notice, and publication of a document is not the same as its application.

## Open items

1. **Reconciliation of the indirect-participant category lists** — obtain from Monte Titoli the current text of the provision the Instructions' footnote 1 calls "article 6 of the Rules of the Settlement Service", or a written confirmation that Article 59(6)(a) of the 26 January 2026 Regulations is the operative test. Official route: the Euronext Securities Milan public documentation hub for the Regulations/Instructions, and the client platform (MT-X) or the participant's relationship manager for confirmation. *No gap id is named in this bundle for this conflict.*
2. **The Italian authoritative texts** of Articles 58–59 and of Instructions §§1.1–1.2.3, to confirm wording on which a decision turns — the reviewed English versions are translations and the Italian prevails.
3. **CLIMP recognition procedure, forms and data fields**, and the associated service levels for a recognition request as opposed to a generic static-data change — expressly not admitted in the reviewed evidence; available only through the client platform.
4. **Client eligibility file** for the specific customer: legal status under the Consolidated Law on Finance / Consolidated Law on Banking (or the third-country equivalence route), LEI, and, for a third-country client, evidence of the Consob/Bank of Italy supervisory agreement and the Art. 59(6)(d) insolvency-impediment assessment.
5. **Pricelist row(s)** applicable to indirect-participant recognition, dedicated account opening and any urgent static-data handling — no amount may be quoted from this bundle.
6. **Any Service Notice or Instructions edition later than 30 June 2025** that re-numbers or re-words §1.2.1 — the reviewed Instructions edition predates the reviewed Regulations edition, and the bundle carries no later edition.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.460824+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_settlement_scope_and_participants"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-settlement-characteristics]] — Settlement Service characteristics, participant categories and indirect participants (Articles 58–59) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 58–59; PDF 41–44, printed 40–43 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Categories are legal admission categories; a firm's own eligibility requires its facts.
EXCERPT (Articles 58–59; PDF 41–44, printed 40–43):
Article 58 - Characteristics of the Settlement Service

   1. The Settlement Service covers:
         a) the acquisition of the Settlement instructions;
         b) the matching;
          c) the settlement of transactions.
   2. Acquisition, matching and  settlement  occur  in T2S and may  cover
      Settlement instructions between Participants in Monte Titoli, or between a
       Participant in Monte Titoli different from a CSD in T2S, and a participant in
      another CSD  in T2S. T2S  allows  for  the  settlement  of  Settlement
       Instructions pursuant to Legislative Decree no. 210/2001.
   3. The acquisition of the Settlement instructions takes place through:
         a) the X-TRM Service offered by Monte Titoli; or
         b) systems connected to the T2S platform, operated by:
                   b.1) Markets and Central Counterparties acting as DCP and the
                CSDs, that input Settlement Instructions on behalf of their own
                    participants and/or members by means  of the power  of
                  attorney (POA) that shall be notified to Monte Titoli.
                   b.2) DCP Participants, different from Central Counterparties
                   that input Settlement Instructions related to transactions to
                be settled on their own account or on their own account and
                on behalf of third parties.
   4.  Securities are settled on the participants' accounts, opened at Monte
        Titoli.
   5. Cash settlement in euro takes place on the accounts of the participants or
      Agent Banks dedicated to processing of settlement in T2S.




40    In force as of 26 January 2026



[PDF page 42]

                                                            SERVICE REGULATIONS


Article 59 – Categories of Participants and methods of participation

   1. Access to the Settlement Service can be gained,  in the capacity  of
       participants, by assuming the obligations arising from the transfer orders
      within the scope of the system by central counterparties and central
       securities depositories and the following categories of entities:
        a)  Italian banks and EU banks, as defined in the Consolidated Law on
           Finance, as well as central banks and the Cassa Depositi e Prestiti, as
           bodies listed in Article 2(5) sub-paragraph 2 of Directive 2013/36/EU
            of the European Parliament and of the Council, dated 26 June 2013
          pursuant to Article 1(1), letter h, no. 1 of the Finality Decree;
       b)  Italian investment firms (SIM) and EU investment firms, pursuant to
             Article 1(1), letter h, no. 2 of the Finality Decree;
        c)  firms in third-party countries that perform the same kind of activities
          as the entities referred to in letters a) and b) pursuant to Article 1(1),
             letter h, no. 4 of the Finality Decree;
       d) public authorities, or public enterprises as defined in Article 8 of
           Regulation no. 3603/93 of the EC Council of 13 December 1993, such
          as Poste  Italiane, the  Italian Ministry of Finance (MEF) and the
          European Investment Bank, as well as businesses whose activities are
          guaranteed by the State, pursuant to Article 1(1), letter h, no. 3 of the
             Finality Decree;
        e) issuers which do not perform the same kind of activities as the entities
           referred to in letters a) and b) and which participate in Notary Services
         and Maintenance Services as entities whose activity is significant as
           regards systemic risk, pursuant to Article 1(1), letter h, no. 5 of the
             Finality Decree;
          f)  financial intermediaries entered in the register kept by the Bank of
             Italy and referred to in Article 106 the Consolidated Law on Banking,
         and authorised to perform the activities covered by Article 1(5), letters
            c) and c)-bis, of the Consolidated Law on Finance and, exclusively with
          regard to the trading of derivative financial instruments, authorised to
          perform the activities covered by Article 1(5), letters a) and b), of the
           Consolidated Law on Finance, as entities whose activity is significant
          as regards systemic risk, pursuant to Article 1(1), letter h, no. 5 of the
             Finality Decree.
   2. Issuers admitted pursuant to paragraph 1, letter e), take part in the
      Settlement Service solely for the purpose of settlement of free-of-payment
       transactions. The Settlement Instructions related to such transactions are
      acquired with the procedures described in the Instructions. The Issuers
     must also have procedures in place for maintaining accounts of securities.
     Upon request, these procedures shall be transmitted to Monte Titoli.
   3. Enterprises from third-party countries which perform the same kind of
       activities as banks and investment firms, and also the central counterparties
     and central securities depositories of third-party countries can participate
       in the service provided Consob and the Bank of Italy have confirmed the
      existence of agreements by at least one of the two Authorities with the
      corresponding Supervisory  Authority  in  the country  of  origin  of the
       applicant. Monte Titoli reserves the right to ask entities from third-party

41    In force as of 26 January 2026



[PDF page 43]

                                                            SERVICE REGULATIONS


      countries for specific information or the necessary certifications in order to
      assess the existence of the circumstances referred to in Article 89 (2) and
      (5) of the Delegated Regulation (EU) no. 2017/392.
   4. Participation can be in one’s own name and on one’s own behalf or in the
     name and on behalf of third parties, using the corresponding securities
      accounts opened in the Monte Titoli accounting records system.
   5. Participants can ask Monte Titoli to authorize third parties, belonging to one
       of the categories under paragraph 1, to enter settlement Instructions to be
     drawn on their own accounts. To this end, participants shall notify the power
       of attorney (POA) to Monte Titoli.
      Authorized third parties must meet the following prerequisites:
         a) have an organizational structure adequate for the volume of work,
            as well as staff members with appropriately qualified expertise, and
            designate one or more contact persons for relations with Monte Titoli;
         b) adopt technological and IT systems ensuring the integrity, accuracy,
           completeness and confidentiality of data concerning the Settlement
             Instructions, adopting appropriate technical measures;
          c) adopt technical measures for information security and processing
             continuity;
         d) ensure  that the  individual Settlement  Instructions sent  to the
            Settlement Service are identified in such a way as to allow their
             univocal nature and correct order to be checked;
         e) use authentication procedures by means of Settlement Instruction
           check digits that guarantee the correct origin and the integrity of the
            data received.
      Authorized third parties must sign a specific agreement with Monte Titoli
     and allow the latter to perform check activities to verify the adequacy,
       compatibility and suitability of the technological systems and interaction
      with the settlement system and the requirements provided for in this
      paragraph. The authorized third party must have at its premises adequate
      documentation on the architecture, functionality, operating methods and
      service levels.
      Should Monte  Titoli  consider  that  the  operational  conditions  of  the
      authorised third party or the participant cause, or could cause:
          a. technical issues for Monte Titoli;
          b. any risk to the normal functioning of the service; or
           c.  risk of Monte Titoli breaching its regulatory responsibilities
     Monte  Titoli may,  after  notifying  the  relevant  parties, suspend  the
      authorisation of the third party or issue instructions to the authorised third
       party, the participant or both, which must be followed without delay.
   6. Participants can ask Monte  Titoli to recognise their own customers as
       indirect participants provided that:
      a)  the customers fall under one of the categories referred to in paragraph
           1, letters a), b) or c);


42    In force as of 26 January 2026



[PDF page 44]

                                                            SERVICE REGULATIONS


      b) the participants use one or more securities accounts, opened opened
           in the Monte Titoli accounting records system, dedicated exclusively to
          the settlement of instructions pertinent to the customer that asks to
        be recognised as an indirect participant;
        c) the customer  identification data  that the  participants  intend  to
          recognise as indirect participants, and any of their amendments, are
        known  to Monte  Titoli  for  having been communicated by  the
           participant to Monte  Titoli for this purpose, using the procedures
          described in the Instructions.
       d) limited to the  entities referred to  in paragraph 1  letter  c), the
           participants have checked that there are no impediments to the
           substantial application of these Regulations and the Order of 2 August
        2018 issued by the Bank of Italy in agreement with Consob pursuant
           to Article 10(4) of the Finality Decree, in the event of the opening of
          insolvency procedure against the entity which the participant intends
           to recognise as an indirect participant, taking account of the regulatory
         framework applicable thereto.

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_connectivity_and_static_data"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-connectivity-static-data]] — Connectivity models, static data, LEI, indirect participants, account/DCA structure and updating operating conditions (§§1.1–1.2.3) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §§1.1–1.2.3; PDF 7–10, printed 3–6 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: CLIMP procedures and forms themselves are not admitted; the mdm@lseg.com address is as printed in the 30 June 2025 edition.
EXCERPT (§§1.1–1.2.3; PDF 7–10, printed 3–6):
1. IMPLEMENTING PROVISIONS
 OF THE SETTLEMENT SERVICE

1.1 CONNECTIVITY

    1.1.1 Models of connection to the T2S platform

For the submission  of  transactions  to Settlement  Service,  Participants can
connect to T2S platform through:

    •  model  of  direct  connectivity  (Participants  DCP):  using  technological
      systems  that  interact  directly  with  the T2S  platform  for  forwarding
      operations, certified by the ECB and authorized by Monte Titoli;

    •  model of indirect connectivity (Participants ICP): using the system for
      connection  to  the T2S  platform  of Monte  Titoli whose  features  are
      regulated under the X-TRM Service Rules.

Issuers eligible to participate in the Settlement Service in accordance with Article
57, paragraph 1 of the Service Regulations, can enter settlement instructions
relating to free-of-payment transfers only through X-TRM.



1.2 ADMISSION CRITERIA

1.2.1 Management of static data

The management of static data concerns the Participants, their clients and their
Agent Banks.

The Participant, and its clients, set up is done by Monte Titoli according to the
information communicated by  the  Participant  itself through  the web base
application denominated CLIMP.

For the interaction with the Settlement Service, the Participants, and the Agent
Banks, must have a unique LEI code. Failing that, it is not possible to proceed to
the configuration of the Participant on the T2S platform and therefore Monte
Titoli will not allow the start of operations of the same.





3



[PDF page 8]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Pursuant to the Service Regulations, Participants may request to qualify as
Indirect Participants  their  clients belonging to the categories referred to  in
paragraph 1 of the same article1. To this end Participants must:

    a) communicate the name and the associated LEI code of each Indirect
        Participant;
    b) associate to each Indirect Participant for which settlements are made,
      one or more securities accounts to be used exclusively to settling the
        Indirect Participant’s settlement instructions.
The same subject may be qualified as an Indirect Participant in Monte Titoli’s
Settlement Service by more than one  Participant,  in accordance with the
conditions indicated above.

The information will be provided trough CLIMP and the Participant shall kept
update such data.

Monte Titoli keeps encoding Participants currently in use at the domestic level for
interacting with its Services:

    •  ABI CODE code assigned by the Bank of Italy/Consob for banks, financial
      intermediaries, brokers and central counterparties.

    •  CODE MT has the same standard ABI and often it corresponds with it. It
     may be assigned by Monte Titoli for specific subjects that can not have an
     ABI code (e.g. non-banks).

    •  CED CODE assigned by SIA or Monte Titoli.

    •  LEI CODE11 assigned by Local Operating Unit (LOU).


Monte Titoli manages the correspondence between the LEI codes used for the
Settlement Service and encodings used for other services offered.



1 Pursuant to article 6, of the Rules of the Settlement Service, may be qualify as Indirect Participants:
a) Italian, EU and non-EU banks, pursuant to article 1, paragraph 1 of Italian Legislative Decree 385/93;
b) Italian investment firms (SIM) and EU and non-EU investment firms;
c) Italian asset management companies (SGR) provided by article 1, paragraph 1 lett. o) of CLF, with the exception of the
provisions of article 36 paragraph 2 of CLF;
d) Stockbrokers entered in the single national roll provided for in article 201 of CLF;
e) central banks;
f) foreign CSD entities;
g) central counterparties;
h) financial intermediaries entered in the register kept by the Bank of Italy referred to in Article 106 of the CLB and authorized to
exercise the activities provided for in article 1, paragraph lett. c) and c)-bis of Legislative Decree as well as, to the limited extent
of the activity on derivatives, authorized to the activity provided for in article 1, paragraph 5, lett. a) and b) of CLF;
i) Poste Italiane S.p.a.;
j) Cassa Depositi e Prestiti
l) Italian Ministry of Finance.





4



[PDF page 9]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Participants may ask Monte  Titoli to change the  static data  in the manner
described in paragraph 1.2.3.

1.2.2 Structure of Accounts

Monte Titoli opens and maintains securities accounts in the name and on behalf
of its Participants, regardless of connectivity model which they select (or DCP
Participants ICP).

The securities accounts must be connected to a dedicated account (DCA) for cash
settlement in central bank money at the T2S platform and also for the purpose of
the processes of self-collateralization.

Monte  Titoli configures connections between DCA and securities accounts  in
accordance with guidance provided by the Participants.



1.2.3 Updating the operating conditions of the Participants

Participants communicate and ask Monte  Titoli changing operating conditions
specified by the time of the Settlement Service via web application (CLIMP).

In case of temporary unavailability of the web application, the Participants may
send notices or requests for update via e-mail at mdm@lseg.com

Monte Titoli will update the operating conditions normally within 5 days from the
moment the request has been produced complete of all the information needed
to handle the request, which shall be entered through CLIMP platform. Monte
Titoli confirms the completeness of the documentation by sending back an e-
mail. Where the update requires operational interventions particularly complex
(for example, in cases where the update requires the prior acceptance of or
interaction with a third party) or in cases of requests for massive update. Monte
Titoli reserves the right to apply for a longer term, upon notice to the Participant.

Participants may also, ask Monte Titoli to modify their operational conditions with
a reduced timing in respect of the one referred to in the preceding paragraph
(so-called ‘’urgent request’’) (e.g. modification of the DCA account).

In such case, Monte Titoli confirms to the Participant the operational timing and
communicates the modalities and the fees for the management of the operation.
Monte Titoli shall reserve itself the right not to proceed with the request with a
reduced timing for justified operational reasons.





5



[PDF page 10]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In order to facilitate the management of the urgent requests, Monte Titoli may
establish  specific  procedures  described  in  the  Operating  Documents  that
Participants shall accomplish2.

Urgent requests must be received by Monte Titoli by e-mail at mdm@lseg.com
by 4 p.m.. Requests received after this deadline shall be deemed as received on
the following day.

Fees for the management of urgent requests are indicated in the Pricelist.

Given the requests received by  intermediaries, a the procedure  to update
operational conditions with a reduced timing is provided upon request (so-called
"urgent request"). With reference to the timing of the standard procedure to
manage static data, it is clarified the moment from which 5 days are counted.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
