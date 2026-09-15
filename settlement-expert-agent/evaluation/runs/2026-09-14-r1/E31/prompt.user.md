QUESTION FROM THE USER:
Legally, what must a CSD define about the moments of entry and irrevocability of transfer orders, and how does Monte Titoli implement those moments?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.326597+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-finality]] — Matching, cancellation, hold and SF1/SF2/SF3 (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.
LIMITATION: No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted.
EXCERPT (Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50):
Article 69 – Matching of Settlement Instructions

1. The matching is carried out to check that the information corresponds to the
   settlement instructions entered.
2. The T2S system supplies the participants with complete disclosure regarding
   the  status  of  the  settlement  instructions  entered and  the  settlement
   instructions entered by the counterparty awaiting matching (alledgement).
3. The matching checks referred to in paragraph 1 cover mandatory matching
    fields, but may also regard the non-mandatory matching fields.
4. Unmatched settlement instructions may be changed by the Participants, but
   only as regards status indicators.

Article 70 - Cancellation of the settlement Instructions

1. Settlement Instructions may be unilaterally cancelled by the Participant which
   entered them up to the time of the matching, on condition that such Settlement
   Instructions were not entered as non-changeable.
2. Matched settlement Instructions may be cancelled bilaterally, with the consent
   of both Participants, or upon request of an entity acting on their behalf, subject
   to the prior submission to Monte Titoli of the relevant mandate.
3. Cancellations are sent by the Participants with the methods and the time
   frames provided for in the Instructions. They then go through the acquisition
   phase and,  if referring to matched settlement Instructions, the matching
   phase. When  the  cancellations  are  matched,  the  original  settlement
   Instructions are cancelled.
4. Market Management Companies and central counterparties may ask Monte
    Titoli to block these functionalities with regard to their settlement Instructions,
   according to the methods and conditions provided for in the operating rules for
   these systems and in accordance with the provisions for T2S.
5. Cancellations may also be entered by Monte  Titoli at the request of the
   Participants and in the other cases established by the Rules, in accordance with
   the provisions above.
6. CoSD Settlement Instructions may only be cancelled by Monte Titoli.
7. Automatic cancellation of settlement instructions from the T2S platform is
   disposed when instructions:
   a) have not passed the daily validation phase;
   b) are not matched or are not settled within the time limits provided in the
       Instructions;

8. Participants are informed of the progress and outcome of the cancellation
   process and of any automatic cancellation of settlement Instructions, pursuant
   to the previous paragraph.


49    In force as of 26 January 2026



[PDF page 51]

                                                            SERVICE REGULATIONS


Article 71 – Hold of the Settlement Instructions

1. The participant may hold the settlement of the settlement instructions entered
   by it so as not to subject them to settlement or hold the re-proposal of the
   Settlement Instructions not regulated, also partially, until there is a specific
   release, on condition that these Settlement Instructions have not been entered
   as non-changeable.
2. Market management companies and central counterparties may ask Monte
    Titoli to block the use of this functionality with regard to their settlement
   instructions, according to the methods and conditions provided for in the
   operating rules for these systems and in accordance with the provisions for
   T2S.
3. The settlement may also be put on hold by Monte Titoli, at the request of the
   participants and in the other cases established by the Rules, in accordance with
   the provisions above.

Article 72 – Input into the Settlement System and irrevocability of
settlement Instructions

1. Settlement Instructions are deemed “entered” into the Settlement System,
   pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the
   validation time in T2S ends (SF1).
2. Settlement Instructions cannot be revoked by a participant or a third party
   from the time of their matching in T2S (SF2), without prejudice to the bilateral
   cancellation of settlement Instructions provided for under Article 70 (2).
3. The transfer of securities and cash become final from the time of the debiting
   of the cash, or of the securities when settlement by cash is not provided for.
   (SF3)

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "csdr_definitions"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[csdr-2-definitions]] — CSDR Article 2 definitions (settlement, participant, CSD link, ISD, settlement fail, DVP and others) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: CSDR: consolidated 17 January 2026 | CSDR Article 2; consolidation 17 January 2026 | version None | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
EXCERPT (CSDR Article 2; consolidation 17 January 2026):
Article 2

Definitions

1.   

For the purposes of this Regulation, the following definitions apply:

(1) 

‘central securities depository’ or ‘CSD’ means a legal person that operates a securities settlement system referred to in point (3) of Section A of the Annex and provides at least one other core service listed in Section A of the Annex;

(2) 

‘third-country CSD’ means any legal entity established in a third country that provides a similar service to the core service referred to in point (3) of Section A of the Annex and performs at least one other core service listed in Section A of the Annex;

(3) 

‘immobilisation’ means the act of concentrating the location of physical securities in a CSD in a way that enables subsequent transfers to be made by book entry;

(4) 

‘dematerialised form’ means the fact that financial instruments exist only as book entry records;

(5) 

‘receiving CSD’ means the CSD which receives the request of another CSD to have access to its services through a CSD link;

(6) 

‘requesting CSD’ means the CSD which requests access to the services of another CSD through a CSD link;

(7) 

‘settlement’ means the completion of a securities transaction where it is concluded with the aim of discharging the obligations of the parties to that transaction through the transfer of cash or securities, or both;

(8) 

‘financial instruments’ or ‘securities’ means financial instruments as defined in point (15) of Article 4(1) of Directive 2014/65/EU;

(9) 

‘transfer order’ means transfer order as defined in the second indent of point (i) of Article 2 of Directive 98/26/EC;

(10) 

‘securities settlement system’ means a system under the first, second and third indents of point (a) of Article 2 of Directive 98/26/EC that is not operated by a central counterparty whose activity consists of the execution of transfer orders;

(11) 

‘settlement internaliser’ means any institution, including one authorised in accordance with Directive 2013/36/EU or with Directive 2014/65/EU, which executes transfer orders on behalf of clients or on its own account other than through a securities settlement system;

(12) 

‘intended settlement date’ means the date that is entered into the securities settlement system as the settlement date and on which the parties to a securities transaction agree that settlement is to take place;

(13) 

‘settlement period’ means the time period between the trade date and the intended settlement date;

(14) 

‘business day’ means business day as defined in point (n) of Article 2 of Directive 98/26/EC;

(15) 

‘settlement fail’ means the non-occurrence of settlement, or partial settlement of a securities transaction on the intended settlement date, due to a lack of securities or cash and regardless of the underlying cause;

(16) 

‘central counterparty’ or ‘CCP’ means a CCP as defined in point (1) of Article 2 of Regulation (EU) No 648/2012;

(17) 

‘competent authority’ means the authority designated by each Member State in accordance with Article 11, unless otherwise specified in this Regulation;

(18) 

‘relevant authority’ means any authority referred to in Article 12;

(19) 

‘participant’ means any participant, as defined in point (f) of Article 2 of Directive 98/26/EC in a securities settlement system;

(20) 

‘participation’ means participation within the meaning of the first sentence of point (2) of Article 2 of Directive 2013/34/EU, or the ownership, direct or indirect, of 20 % or more of the voting rights or capital of an undertaking;

(21) 

‘control’ means the relationship between two undertakings as described in Article 22 of Directive 2013/34/EU;

(22) 

‘subsidiary’ means a subsidiary undertaking within the meaning of Article 2(10) and Article 22 of Directive 2013/34/EU;

(23) 

‘home Member State’ means the Member State in which a CSD is established;

(24) 

‘host Member State’ means the Member State, other than the home Member State, in which a CSD has a branch or provides CSD services;

(25) 

‘branch’ means a place of business other than the head office which is a part of a CSD, which has no legal personality and which provides CSD services for which the CSD has been authorised;

▼M4

(26) 

‘default’ means, in relation to a participant, a situation where insolvency proceedings, as defined in Article 2, point (j), of Directive 98/26/EC, are opened against a participant or an event defined in the CSD’s internal rules as constituting a default;

▼B

(27) 

‘delivery versus payment’ or ‘DVP’ means a securities settlement mechanism which links a transfer of securities with a transfer of cash in a way that the delivery of securities occurs if and only if the corresponding transfer of cash occurs and vice versa;

(28) 

‘securities account’ means an account on which securities may be credited or debited;

(29) 

‘CSD link’ means an arrangement between CSDs whereby one CSD becomes a participant in the securities settlement system of another CSD in order to facilitate the transfer of securities from the participants of the latter CSD to the participants of the former CSD or an arrangement whereby a CSD accesses another CSD indirectly via an intermediary. CSD links include standard links, customised links, indirect links, and interoperable links;

(30) 

‘standard link’ means a CSD link whereby a CSD becomes a participant in the securities settlement system of another CSD under the same terms and conditions as applicable to any other participant in the securities settlement system operated by the latter;

(31) 

‘customised link’ means a CSD link whereby a CSD that becomes a participant in the securities settlement system of another CSD is provided with additional specific services to the services normally provided by that CSD to participants in the securities settlement system;

(32) 

‘indirect link’ means an arrangement between a CSD and a third party other than a CSD, that is a participant in the securities settlement system of another CSD. Such link is set up by a CSD in order to facilitate the transfer of securities to its participants from the participants of another CSD;

(33) 

‘interoperable link’ means a CSD link whereby CSDs agree to establish mutual technical solutions for settlement in the securities settlement systems that they operate;

(34) 

‘international open communication procedures and standards’ means internationally accepted standards for communication procedures, such as standardised messaging formats and data representation, which are available on a fair, open and non-discriminatory basis to any interested party;

(35) 

‘transferable securities’ means transferable securities as defined in point (44) of Article 4(1) of Directive 2014/65/EU;

(36) 

‘shares’ means securities specified in point (44)(a) of Article 4(1) of Directive 2014/65/EU;

(37) 

‘money-market instruments’ means money-market instruments as defined in point (17) of Article 4(1) of Directive 2014/65/EU;

(38) 

‘units in collective investment undertakings’ means units in collective investment undertakings as referred to in point (3) of Section C of Annex I to Directive 2014/65/EU;

(39) 

‘emission allowance’ means emission allowance as described in point (11) of Section C of Annex I to Directive 2014/65/EU, excluding derivatives in emission allowances;

(40) 

‘regulated market’ means regulated market as defined in point (21) of Article 4(1) of Directive 2014/65/EU;

(41) 

‘multilateral trading facility’ or ‘MTF’ means multilateral trading facility as defined in point (22) of Article 4(1) of Directive 2014/65/EU;

(42) 

‘trading venue’ means a trading venue as defined in point (24) of Article 4(1) of Directive 2014/65/EU;

(43) 

‘settlement agent’ means settlement agent as defined in point (d) of Article 2 of Directive 98/26/EC;

(44) 

‘SME growth market’ means an SME growth market as defined in point (12) of Article 4(1) of Directive 2014/65/EU;

(45) 

‘management body’ means the body or bodies of a CSD, appointed in accordance with national law, which is empowered to set the CSD’s strategy, objectives and overall direction, and which oversees and monitors management decision-making and includes persons who effectively direct the business of the CSD.

Where, according to national law, a management body comprises different bodies with specific functions, the requirements of this Regulation shall apply only to members of the management body to whom the applicable national law assigns the respective responsibility;

(46) 

‘senior management’ means those natural persons who exercise executive functions within a CSD and who are responsible and accountable to the management body for the day-to-day management of that CSD;

▼M4

(47) 

‘group’ means a group within the meaning of Article 2, point (11), of Directive 2013/34/EU;

(48) 

‘close links’ means close links as defined in Article 4(1), point (35), of Directive 2014/65/EU;

(49) 

‘qualifying holding’ means a direct or indirect holding in a CSD which represents at least 10 % of the capital or of the voting rights, as set out in Articles 9, 10 and 11 of Directive 2004/109/EC of the European Parliament and of the Council ( 1 ), or which makes it possible to exercise a significant influence over the management of the CSD;

(50) 

‘deferred net settlement’ means a settlement mechanism whereby cash or securities transfer orders in relation to securities transactions of the participants in the securities settlement system are subject to netting, and whereby settlement of participants’ net claims and obligations takes place at the end of predefined settlement cycles during or at the end of the business day.

▼B

2.   The Commission shall be empowered to adopt delegated acts in accordance with Article 67 concerning measures to further specify the non-banking-type ancillary services set out in points (1) to (4) of Section B of the Annex and the banking-type ancillary services set out in Section C of the Annex.

TITLE II

SECURITIES SETTLEMENT

CHAPTER I

Book-entry form

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "sfd_entry_irrevocability"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[sfd-3-5]] — Settlement Finality Directive: enforceability of transfer orders and the moments of entry and irrevocability (Articles 3 and 5) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: Settlement Finality Directive: consolidated 8 April 2024 | Directive 98/26/EC Article 3; consolidation 8 April 2024 | version Consolidated 8 April 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408
CITATION: Settlement Finality Directive: consolidated 8 April 2024 | Article 5 | version Consolidated 8 April 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
LIMITATION: National transposition and designation of each system are not admitted.
EXCERPT (Directive 98/26/EC Article 3; consolidation 8 April 2024):
Article 3

▼M1

1.   

Transfer orders and netting shall be legally enforceable and binding on third parties even in the event of insolvency proceedings against a participant, provided that transfer orders were entered into the system before the moment of opening of such insolvency proceedings as defined in Article 6(1). This shall apply even in the event of insolvency proceedings against a participant (in the system concerned or in an interoperable system) or against the system operator of an interoperable system which is not a participant.

Where transfer orders are entered into a system after the moment of opening of insolvency proceedings and are carried out within the business day, as defined by the rules of the system, during which the opening of such proceedings occur, they shall be legally enforceable and binding on third parties only if the system operator can prove that, at the time that such transfer orders become irrevocable, it was neither aware, nor should have been aware, of the opening of such proceedings.

▼B

2.   No law, regulation, rule or practice on the setting aside of contracts and transactions concluded before the moment of opening of insolvency proceedings, as defined in Article 6(1) shall lead to the unwinding of a netting.
3.   The moment of entry of a transfer order into a system shall be defined by the rules of that system. If there are conditions laid down in the national law governing the system as to the moment of entry, the rules of that system must be in accordance with such conditions.

▼M1

4.   In the case of interoperable systems, each system determines in its own rules the moment of entry into its system, in such a way as to ensure, to the extent possible, that the rules of all interoperable systems concerned are coordinated in this regard. Unless expressly provided for by the rules of all the systems that are party to the interoperable systems, one system's rules on the moment of entry shall not be affected by any rules of the other systems with which it is interoperable.

▼M1
EXCERPT (Article 5):
Article 5

A transfer order may not be revoked by a participant in a system, nor by a third party, from the moment defined by the rules of that system.

▼M1

In the case of interoperable systems, each system determines in its own rules the moment of irrevocability, in such a way as to ensure, to the extent possible, that the rules of all interoperable systems concerned are coordinated in this regard. Unless expressly provided for by the rules of all the systems that are party to the interoperable systems, one system's rules on the moment of irrevocability shall not be affected by any rules of the other systems with which it is interoperable.

▼B

SECTION III

PROVISIONS CONCERNING INSOLVENCY PROCEEDINGS