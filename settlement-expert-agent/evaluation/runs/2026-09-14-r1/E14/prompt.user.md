QUESTION FROM THE USER:
Can ISIN FR0000120271 settle cross-CSD today between Monte Titoli and Euroclear France, and through which link?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:58:16.039532+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "instrument_eligibility"}
STATUS: blocked — Current ISIN, CSD-link, account, currency and MT23/static-data evidence required.
GAP IDS: ['G04']

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_rule"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-cross-csd-disclosure]] — Cross-CSD settlement rule and disclosure of settlement progress (Articles 77–78) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 77–78 with footnote 8; PDF 54, printed 53 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Article 77(2) excludes cross-CSD settlement when the issuer CSD is outside T2S unless both investor CSDs hold a link avoiding realignment with it; actual links per ISIN are not certified.
EXCERPT (Articles 77–78 with footnote 8; PDF 54, printed 53):
Article 77 – Cross CSD Settlement

1.  If the settlement Instructions are to be settled between a Participant in Monte
    Titoli, different from another CSD in T2S and a participant in another CSD in
   T2S (cross CSD), T2S shall automatically carry out the movements between
   the securities accounts of the participants involved, of the Investor CSDs and
   of the Issuer CSD.
2. Monte Titoli does not envisage the possibility of carrying out a cross CSD
   settlement on securities  if the Issuer CSD  is outside of T2S, unless both
   investor CSDs have in place a link with another CSD in T2S so that the
   realignment with the Issuer CSD outside T2S is not necessary.

Article 78 – Disclosure regarding the progress of the process

1.  If requested by the Participants, Monte Titoli makes available the events that
   change the balance in their securities account, supplying in real time the
   settlement status of each transaction being processed,  all the information
   useful for monitoring it, as well as the settlement of the whole transaction. This
   disclosure is made available through the direct link channel to T2S, or through
   the X-TRM Service.
2.  If requested by the participants, Monte Titoli also makes available to the
   participants and/or to their agent bank the cash balance disclosure. This
   disclosure is processed and made available, according to the format and with
   the channels indicated in the Services Manuals.8

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_link_guide"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-gateway-links-guide]] — T2S Gateway settlement links guide: link inventory (MT23 codes), how to identify the issuer CSD and instruction rules (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: T2S GATEWAY - Euronext Securities Milan Settlement Links - Valid from 1st May 2026 | Table of contents, Introduction, §1 and §1.1.1 notes; PDF 2–9 | version T2S Gateway settlement links, valid from 1 May 2026 | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2026-04/T2S%20GATEWAY%20-%20ES%20MIL%20Settlement%20links%20-%20Web%20site%20review%20May%202026.pdf
LIMITATION: Route-specific SWIFT/XTRM templates (PDF 10–109) are not admitted; the index proves which issuer-CSD/counterparty combinations the guide covers on 1 May 2026, not per-ISIN eligibility.
LIMITATION: Document footers read PRIVATE although the file is on the public T2S Gateway page; ES-MIL disclaims responsibility for instruction correctness.
EXCERPT (Table of contents, Introduction, §1 and §1.1.1 notes; PDF 2–9):
TABLE OF CONTENTS




 INTRODUCTION ............................................................................................. 5

  1.    Settlement overview ............................................................................ 6

    1.1.1 How to use this Document and further instructions .................................... 7

  2. Issuer CSD: SWITZERLAND - (MT23 81551) .............................................. 9

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) ..................................... 9

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 10

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 11

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 12

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 13

  3. Issuer CSD: GREECE (MT23 85679) ......................................................... 14

    Counterparty in Greece (BOGS – BNGRGRAASSS) ............................................ 14

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 15

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 16

  4. Issuer CSD: BELGIUM NBB (MT23 85680) ............................................... 17

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) .................................... 17

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 18

    Counterparty in Belgium (NBB – NBBEBEBB216) .............................................. 19

    Counterparty in France (ESES FR – SICVFRPPXXX) ........................................... 20

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 21

    Counterparty Euroclear Bank (EOC – MGTCBEBEECL) ....................................... 22

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 23

  5.    Issuer CSD: BELGIUM ESES (MT23 85668) ........................................ 24

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) .................................... 24

    Counterparty in Belgium Eses (ESES BE – CIKBBEBBCLR) ................................. 25

    Counterparty in Germany (CEU Clearstream Europe – DAKVDEFFXXX) ................ 26

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 27

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 28

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 29

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 30


1


                                        PRIVATE



[PDF page 3]

  6.    Issuer CSD: NETHERLAND (MT23 81501) ........................................... 31

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) .................................... 31

    Counterparty in Netherland (ESES NL – NECINL2AXXX) .................................... 32

    Counterparty in Germany (CEU – DAKVDEFFXXX) ............................................ 33

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 34

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 35

    Counterparty in Spain (IBERCLEAR – IBRCESMMXXX) ....................................... 36

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 37

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 38

  7. Issuer CSD : FRANCE (MT23 81346) ........................................................ 39

    Counterparty in France (ESES FR – SICVFRPPXXX) ........................................... 39

    Counterparty in Germany (CEU – DAKVDEFFXXX) ............................................ 40

    Counterprty in Austria (OEKB CSD – OCSDATWWXXX) ...................................... 41

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 42

    Counterparty in Spain (IBERCLEAR – IBRCESMMXXX) ...................................... 43

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 44

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 45

  8. Issuer CSD : GERMANY (MT23 81318) ..................................................... 46

    Counterparty in France (ESES FR – SICVFRPPXXX) ........................................... 46

    Counterparty in Germany (CEU – DAKVDEFFXXX) ............................................ 47

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 48

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 49

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 50

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 51

  9. Issuer CSD : AUSTRIA (MT23 81451) ...................................................... 52

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 52

    Counterparty in ITALY (ES-MIL – MOTIITMMXXX) ............................................. 53

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 54

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 55

  10. Issuer CSD: ITALY ................................................................................. 56

    Counterparty in France – Bonds, Exor and Euronext equities- (ESES FR –
    SICVFRPPXXX) ............................................................................................. 56

    Counterparty in France – Equities only - FOP ONLY - (ESES FR – SICVFRPPXXX) .. 57

    Counterparty in Netherland – Equities only - FOP ONLY - (ESES NL – NECINL2AXXX)
          58

2


                                        PRIVATE



[PDF page 4]

    Counterparty in Germany (CEU – DAKVDEFEXXX) ............................................ 59

    Counterparty in Austria (OEKB CSD – OCSDATWWXXX) .................................... 60

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 61

    Counterparty in Spain (IBERCLEAR – IBRCESMMXXX) ....................................... 62

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 63

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 64

    Counterparty in Norway (VPS – VPSNNOKKXXX) .............................................. 65

  11. Issuer CSD : SPAIN (MT23: 81488)- Bonds Only ................................... 66

    Counterparty in France (ESES FR – SICVFRPPXXX) ........................................... 66

    Counterparty in Germany (CEU – DAKVDEFFXXX) ............................................ 67

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 68

    Counterparty in Spain (IBERCLEAR – IBRCESMMXXX) ....................................... 69

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 70

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 71

  12. Issuer CSD: UNITED STATES – DTCC       (MT23 : 81626) US Securities
  held in DTCC ................................................................................................ 72

    Counterparty in Netherland - DELIVER FREE ONLY - (ESES NL – NECINL2AXXX) .. 72

    Counterparty in France - DELIVER FREE ONLY - (ESES FR – SICVFRPPXXX) DO NOT
   USE FOR STELLANTIS ................................................................................... 73

    Counterparty in France STELLANTIS shares via T2S cross csd (ESES FR –
    SICVFRPPXXX) ............................................................................................. 74

    Counterparty in Germany - DELIVER FREE ONLY - (CEU – DAKVDEFEXXX) .......... 75

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) .............................................. 76

    Counterparty in United States – DELIVER FREE ONLY (DTCC – DTCYUS33XXX) .... 77

    Counterparty in Euroclear Bank – DELIVER FREE ONLY - (EOC - MGTCBEBEECL) .. 78

    Counterparty in Clearstream - DELIVER FREE ONLY - (CBL – CEDELULLXXX) ....... 79

  13. Issuer CSD: UNITED STATES – EOC (MT23: 12934) US Securities held in
  Euroclear Bank ............................................................................................ 80

    Counterparty in Germany - FOP ONLY - (CEU – DAKVDEFFXXX) ......................... 80

    Counterparty in Switzerland - FOP ONLY - (SIX SIS – INSECHZZXXX) ................. 81

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 82

    Counterparty in United States - FOP ONLY - (DTCC –DTCYUS33XXX) .................. 83

    Counterparty in Euroclear Bank (EOC – MGTCBEBEECL) .................................... 84

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 85

  14. Issuer ICSD: EUROCLEAR BANK (MT23: 12934) .................................... 86


3


                                        PRIVATE



[PDF page 5]

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 86

    Counterparty in Euroclear Bank (EOC - MGTCBEBEECL) .................................... 87

    Counterparty in Germany (CEU – DAKVDEFFXXX) ............................................ 88

    Counterparty in UK (EOC UK & Ireland – CREST) .............................................. 89

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) .................................... 90

    Counterparty in Netherland (ESES NL – NECINL2AXXX) .................................... 91

    Counterparty in France (ESES FR – SICVFRPPXXX) ........................................... 92

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 93

    Counterparty in Portugal (ES-PTO – IBLSPTPPXXX) ........................................... 94

    Counterparty in EOC Finland (APKE CSD – APKEFIHHXXX) ................................. 95

  15. Issuer CSD: CLEARSTREAM (MT23: 12932) ........................................... 96

    Counterparty in Clearstream (CBL – CEDELULLXXX) ......................................... 96

    Counterparty in Euroclear Bank (EOC - MGTCBEBEECL) .................................... 97

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................... 98

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) International Funds Only 99

    Counterparty in Germany (CEU – DAKVDEFFXXX) International Funds Only ....... 100

    Counterparty in France (ESES FR – SICVFRPPXXX)  International Funds Only ... 101

  16. Issuer CSD:UNITED KINGDOM (MT23: 85667) .................................... 102

    Counterparty in Italy (ES-MIL – MOTIITMMXXX) ............................................. 102

    Counterparty in Euroclear Bank (EOC - MGTCBEBEECL) .................................. 103

    Counterparty in Clearstream (CBL – CEDELULLXXX) ....................................... 104

    Counterparty in UK (EOC UK & Ireland – CREST) ............................................ 105

    Counterparty in Switzerland (SIX SIS – INSECHZZXXX) .................................. 106

    Counterparty in Germany (CEU – DAKVDEFFXXX) .......................................... 107

    Counterparty in Netherland (ESES NL – NECINL2AXXX) .................................. 108

    Counterparty in France (ESES FR – SICVFRPPXXX) ......................................... 109





4


                                        PRIVATE



[PDF page 6]

INTRODUCTION




Clients of Euronext Securities Milan (ES-MIL) are allowed to move securities between
their ES-MIL’s account and an account on a different CSD through the links that ES-MIL
has established with several foreign CSDs, in T2S and outside T2S.

While T2S helped to standardize cross csd instructions, there are still several cases,
especially on external transactions, which may require the usage of specific settlement
formats.

In addition, ES-MIL’s Clients, also need to provide their counterparties with their correct
SSI (Securities Settlement Instructions) in order to settle a transaction.

This document is designed with the aim to provide Client’s with a useful tool that
summarizes all the information needed to execute a transfer from/to ES-MIL, versus
another CSD, in a single page.

This Document contains:

    •  Information on how to identify the CSD where ES-MIL holds a foreign security
    •  Templates for allowed external settlement instructions in Swift 15022 and XTRM
    •  Templates for T2S allowed cross csd settlement instructions in Swift 15022 and
     XTRM
    •  Settlement restrictions
    •  SSI to be shared with Counterparties to help them matching ES-MIL’s Clients
       instructions where applicable

We aim to keep this Document updated reflecting the latest changes in the market.

ES-MIL is not responsible for the correctness of your settlement instruction, the
counterparty will always have to provide you with their most updated SSI, we kindly ask
you to get in touch with ES-MIL in case of doubts.





5


                                        PRIVATE



[PDF page 7]

 1. Settlement overview




Securities can be settled by ES-MIL’s Clients against counterparties:

    •   In ES-MIL : such transactions are defined Intra CSD settlement

ES-MIL’s Client will instruct against a counterparty in ES-MIL and the counterparty will do
the same



    •   In another T2S CSD: such transactions are defined Cross CSD settlement

ES-MIL’s Client will instruct against a counterparty’s CSD different from ES-MIL but
participating in T2S and the counterparty will instruct from the other CSD against ES-MIL



    •   In another CSD outside T2S: such transactions are defined External CSD
       settlement

ES-MIL’s Client will instruct against a counterparty’s CSD based on the links between ES-
MIL and the other CSD outside T2S and the counterparty will instruct from the other CSD
against ES-MIL





6


                                        PRIVATE



[PDF page 8]

  1.1.1 How to use this Document and
  further instructions




The correct page for retrieving the format for your instruction can be found in the Table
of Contents of this document, following the next steps:



   1.  Identify where ES-MIL holds the security and select the correspondent chapter
        in the Table of Contents of this Document


This information can be found in MTX → Lists → MT23 List of Financial Instruments →
Search ISIN

When the value in the column issuer/Investor is “Investor” then the value in the
Issuer Code column identifies the Issuer CSD. If the value is “Issuer” then the
Issuer CSD is ES-MIL. This is where ES-MIL holds the mentioned security.

The same value can be found in the Table of Contents of this document and is used to
identify the correct chapter.

As reported in Euronext Clearing Migration FAQ, Operational Notice 22/2023 published on
July 17th and Operational Notice 28/2023, certain Financial Instruments have been
transferred from the home issuer CSD to the technical issuer ESES CSDs. With
Operational Notice 07/2024 the Austrian Bonds have been moved back to OeKB as Issuer
CSD therefore chapter 9 of this guide can be used for all indicated counterparty’s CSD,
the following sentence does not apply to Austrian Bonds.
Clients should remind that those securities can be transferred, according to the Issuer
CSD chapter of reference in this Guide, as Intra or Cross CSD between ESMIL and the
Technical issuer CSD.

The gateway has been updated on 31st October 2025 in order to reflect the new
denomination of Cleastream Banking Frankfurt in Cleastream Europe.





   2. Determine the CSD of your counterparty and select the appropriate Issuer
      CSD/Counterparty combination from the Table of Contents of this
      Document


This information is based on your counterparty’s SSI and will be used to find the correct
settlement combination in the Table of Contents of this document.

PLEASE NOTE:



7


                                        PRIVATE



[PDF page 9]

    •   For each settlement combination we have also included the SSI that you will share
       with your counterparty
    •  Each page will also specify whether the transaction can be executed only FOP or if
       the market executes DUMP trades
    •   Please always use 11 digits bic codes when instructing trades
    •   Please note that Party 2 in T2S is optional and if populated in one of the two
       instructions involved in a securities transaction then it becomes a matching
        criteria and has to be quoted on both instructions
    •   Delivery Swift instructions should always contain also the field DEAG (15022 or
       corresponding MT20022 field)
    •  Receive Swift instructions should always contain also the field REAG (15022 or
       corresponding MT20022 field)
    •  XTRM Cross-csd and External instructions should always be instructed using the
      BIC code in the field “Trading member code”
    •   External instructions can not be instructed with HOLD/RELEASE indicators
    •   If a client will incorrectly instruct a security not available in the MT23, please be
      aware that any possible fail and related CSDR penalties will not be cancel and
       they will be computed as current procedure described
    •  XTRM Cross-csd should always be instructed with a “Ctrp Settl. Account” filled in
      where “Cod. Ctrp” is filled in with a no default BIC
    •  Cross-csd and External settlement instruction when searched, will have the CTRP
       cod. field populated by the internal code (SIA/CED) instead of the BIC used in the
       input function
    •   External Settlement is subject to CoSD rule in the following case: prepositioning
      (DFOP and DVP) and prefunding (RVP). More information could be find in the
        Istruzioni al Servizio di Liquidazione





8


                                        PRIVATE

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_settlement_service_scope"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-service-scope]] — Settlement Service scope: intra-CSD and cross-CSD, ICP versus DCP processing (§1.3 excluding the operational-day clock table) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §1.3 opening; PDF 12, printed 8 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: §1.3.1 (PDF 12–16) is quarantined: its clock values (NTS 19:30, two partial windows) conflict with the deployed R2026.JUN schedule; use the T2S schedule sections and the notice chain instead.
EXCERPT (§1.3 opening; PDF 12, printed 8):
1.3 OPERATION OF THE SETTLEMENT SERVICE

The Settlement Service is operated by the T2S platform and enables settlement
of transactions:

    •  between two Participants in Monte Titoli (cd. Intra CSD Settlement);

    •  between a Participant in Monte Titoli and a participant in another CSD in
     T2S (cross-CSD settlement), within the limits laid down in Article 27 of the
      Operating Rules;

Participants may enter settlement instructions to be settled in modality intra and
cross CSD through connectivity models directly or indirectly.

Settlement Instructions entered through indirect connection, before forwarding
to T2S shall be subject to the processes specified in the subsequent chapter
relating to the X-TRM Service.

Settlement Instructions entered through a direct connection are subject only to
the processes provided by T2S platform.

Although not expressly specified or detailed in this document, with reference to
the acquisition mode, matching and settlement of transactions, please refer to
Document Operating T2S User Requirements.

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_external_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-external-settlement]] — Foreign Settlement Service (external settlement): channels, cancellation, pre-positioning/pre-funding with CoSD, routing and reporting (Title 2) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | Title 2 §§2.1–2.3.6 (PDF 29 is blank); PDF 28–35, printed 24–31 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Per-system Operating Documents and their cut-offs are not admitted.
EXCERPT (Title 2 §§2.1–2.3.6 (PDF 29 is blank); PDF 28–35, printed 24–31):
2 IMPLEMENTING PROVISIONS OF
REGULATION OF FOREIGN SERVICE
(EXTERNAL SETTLEMENT)

2.1 GENERAL PROVISIONS


    2.1.1 OPERATIVE Documentation

Monte Titoli operates within the Foreign Settlement Services pursuant to their
corresponding regulations.

Monte  Titoli also provides  for the Operating Documents, which contain the
operating provisions regarding each Foreign Settlement System.

Such Operating Documents shall be read together with these provisions and are
available to the participants through publication in the dedicated  section of
Monte Titoli’s web site (www.montetitoli.it).



    2.1.2 Relationship between Monte Titoli and Participants

Participants  to the Service   provide,  directly  or  indirectly, the information
regarding  their  clients and the transactions carried out on their behalf,     if
required by the Foreign Settlement Systems in which Monte Titoli participates, or
by any other authority/body entitled to request such information.

Whereas the Foreign Settlement  Systems connected to Monte  Titoli apply
penalties (including but not limited to:  failing settlement when due, or late
matching with respect to time limits envisaged by the Cross-Border System),
Monte  Titoli reiterates the charge of the Foreign Settlement System on the
account of the intermediary to whom the penalty is to be applied. If the penalty
is in currencies other than Euro, Monte Titoli charges as a matter of course the
account  of  the  intermediary  for  the  corresponding amount based on  the
exchange rate in force at the charging date6. Penalties will be charged to the
intermediaries’ accounts without any further charge, and  upon prior notice by
Monte Titoli, based on the penalties charged from time to time by the Foreign
Settlement System.

As  for the fees  for the  provision  of the Service  applies the provisions  of
paragraph 1.2.4


6 The exchange rate is the market exchange rate, as of the closing of the accounting day preceding the charging date.




24



[PDF page 30]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





     2.1.3 Agent Bank

If the participant uses an Agent Bank for cash settlement, the participant  is
required to:

a. appoint the same Agent Bank appointed  for the  settlement  within the
   Settlement Service;
b. request  the Agent Bank to communicate Monte Titoli the acceptance of its
   appointment as Agent Bank, also with reference to the Foreign Settlement
   Service;
c.  in case  of withdrawal, exclusion or suspension  of the Agent Bank from
  TARGET 2, arrange for prompt substitution, notifying Monte Titoli in a timely
   manner.


2.2 SERVICE FUNCTIONALITIES AND COMMUNICATIONS
CHANNELS

The Service requires Monte  Titoli to operate within the Foreign Settlement
Systems, on behalf of its participants, in compliance with the functioning rules of
the relevant Foreign Settlement Systems.

The Service functions are made available through the X-TRM Service or through
RNI.

If the participant is unable to input the transactions through the above specified
telematics channels due to contingent situations, the participant is required to
immediately  notify Monte  Titoli.  In such a  case, Monte  Titoli accepts the
instructions submitted in a written form, for the time required to restore the
connection.

Whereas Monte  Titoli communicates a contingency situation, participants are
required to operate in compliance with the guidance provided from time to time
by Monte Titoli.



    2.2.1 Operational Communications

Monte Titoli communicates to participants, through the information posted on its
website, any operational aspects related to the ordinary management of the
Service.
Communications regarding extraordinary events may be transmitted by Monte




26



[PDF page 31]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Titoli  through  telematics  channels  (including,  but  not  limited  to:  e-mail
messages, RNI 097 free narrative messages, broadcast through the X-TRM On-
Line Service).
The procedures and the timing for the notifications depend on their content and
on the urgency with which they must be disclosed.





27



[PDF page 32]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





2.3 OPERATION OF CROSS-BORDER SETTLEMENT SERVICE

2.3.1 Transactions input

Participants to the Service must enter instructions to be settled in the Foreign
Settlement Systems (that do not use the T2S platform) via the X-TRM Service.

DVP  transactions are disposed by entering  transfer orders  into the X-TRM
Service. FOP transactions are disposed by entering transfer orders into the X-
TRM Service or, for securities delivery transactions, also through RNI messages.

The  specific procedures  for entering the transactions used  for each Foreign
Settlement System are illustrated in the Operating Documents.

DVP and FOP transactions entered via X-TRM:

       a. may not be modified;
      b. may envisage an ISD preceding the date of entering into the Service.


2.3.2 Cancellation of settlement Instruction

Cancellation of transactions which are not matched on ISD or not settled on ISD
may be requested by participants in accordance to the rules of the Foreign
Settlement System to which such instructions have been routed for settlement.

Cancellation of instructions entered via X-TRM may be sent to Monte Titoli (for
subsequent  routing  to Foreign Settlement Systems)  if compatible with the
deadlines indicated in the Operating Documents.

Requests for cancellations of non-matched instructions must be sent via X-TRM.

Requests for cancellations of settlement instructions already matched in the
Foreign Settlement Systems and of settlement instructions not-matched can be
performed  if provided by the Foreign Settlement Systems, on the participant's
request and on condition that the counterparty matches the cancellation.



2.3.3 Pre-positioning / Pre-funding

Settlement Instructions are forwarded to the Foreign Settlement Systems that do
not use  the T2S  platform,  after  the  creation  of  securities  funding  (pre-
positioning) or cash funding (pre-funding) by the Participants respectively in the
Participants securities accounts in Monte Titoli or in the DCA cash accounts .





28



[PDF page 33]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





For securities deliveries (DVP or FOP), the funding of securities (pre-positioning)
is created through the use of the  functionality of the T2S platform "CoSD
Securities Blocking" in the accounts of the Participant in delivery.

For securities receipt (RVP) the settlement is managed sending two settlement
instructions: a receive-free-of payment (RFP) for the securities and a payment
free-of-delivery (PFOD) to debit the cash on the DCA account of the Participant
who buy the  securities and to  credit the Monte  Titoli cash account  . The
settlement  of  this Instruction  is subject to regulation  of the corresponding
Instruction receive-free-of-payment (RFP) of the original operation in receipt.

The processes of pre-funding and pre-positioning are performed at 7 am (CET)
on the settlement date. These processes are entirely managed by Monte Titoli
that provides full information to the participants through the X-TRM.

The process is put on hold by Monte Titoli until ISD and released to the Foreign
Settlement System for settlement at ISD, only on condition that the coverage is
made available and taken into account the opening hours of the relevant Foreign
Settlement System.

The  availability of securities or cash on the participants’ accounts does not
ensure the settlement of the transaction, since, should the counterparty not
match the transactions in due time, or should it not provide the cash or securities
required  for the settlement, the transaction  will remain pending within the
Foreign Settlement System.

The provision of securities or cash remains blocked  until settlement of the
transaction. If the participant wishes to make use of the funding  it is necessary
to cancel the transaction.

The cancellation request may be input by the participant, in compliance with the
operating  rules  of  the  Foreign  Settlement  System  and  as  provided  for
cancellation requests sent through X-TRM.



2.3.4 Routing of transactions to the Cross-Border Settlement Systems.

The transactions input into the Service are final and irrevocable according to
timings and rules in force within the Foreign Settlement Systems within which
the transactions are to be settled.

The transactions are routed   to the Foreign Settlement Systems  for  their
settlement at ISD.





29



[PDF page 34]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In case of unavailability of  the balance on the accounts, the transaction will be
put on hold and re-processed daily until the until the creation of the balance on
the account.

The instructions with a deferred ISD will be put on hold when entered into Monte
Titoli service.

Instructions  received  at  ISD  after  the  hours  specified  in  the  Operating
Documents sent  to the  Foreign Settlement System  for  settlement on  the
following business day. Instructions received after the hours specified in the
Operating Documents, to be settled the same day may nonetheless be routed by
Monte Titoli to the Foreign Settlement System, if this is allowed by the automatic
routing procedures.

The partial execution of transactions (so-called partial delivery)  is possible  if
allowed by the rules of the Foreign Settlement Systems, and the corresponding
procedures are set out in the Operating Documents.

Transactions are managed individually, i.e. without netting.

DVP transactions can only be settled in Euro.

If the transfer of cash related to settlement of a securities selling transaction, or
to the  cancellation  of a purchase  transaction  already sent  to the  Foreign
Settlement System but still awaiting settlement cannot be carried out within the
settlement/cancellation accounting day due to expiry of the Service cut-off times,
cash  will be  transferred on  the  following  business day  without  overnight
interests.

The Service does not carry out any verification regarding holding restrictions or
the enforceability of rights deriving from the possession of financial instruments
which may be envisaged by the issuers.



2.3.5 Reporting on the transactions submitted for settlement

The  Service  provides the  reporting regarding the  capturing, matching and
settlement of the transactions and movements on securities accounts through
the same channels used by participants to input the transactions.

Cash settlement reporting is transmitted by T2S.

The reporting referring to the cancellation of transaction is provided through the
same channels used by the participants to submit the transactions.





30



[PDF page 35]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





2.3.6 DVP and FOP  transactions  related  to  financial  instruments
undergoing corporate actions

In case of transactions related to financial instruments undergoing corporate
actions, Monte  Titoli may  apply  time  limits  (cut-off). Such  limits  will be
communicated from time to time through Service Notices.

In case of transactions traded “cum”,  for which the settlement is carried out
“ex”, the related claim will be managed by the counterparties, unless Monte Titoli
is involved in the processing of the market claim carried out by the Foreign
Settlement System.





31

=== RETRIEVAL 6: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "investor_csd_definition"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

--- SECTION [[t2s-realignment]] — Realignment generation, CSD roles and all-or-none relationship (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.10; concepts and reference-data requirements; PDF 373–376 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Actual links/accounts and ISIN eligibility require verification.
LIMITATION: Does not establish atomicity of an arbitrary two-security swap or describe every action outside T2S.
EXCERPT (§1.6.1.10; concepts and reference-data requirements; PDF 373–376):
1.6.1.10 Realignment


 2    1.6.1.10.1 Concept

 3   The realignment application process handles the cases of:

 4         l  Cross-CSD settlements, i.e. settlements between T2S Actors of different CSDs, the latter being in T2S;

 5         l  External-CSD settlements, i.e. settlements between T2S Actors of different CSDs, with some of the CSDs
 6        involved in the settlement being external to T2S.

 7    Cross-CSD settlement is achieved in T2S with the simultaneous booking of cash and securities for Settlement
 8    Instructions between participants of different CSDs. Once incoming Settlement Instructions are matched (or
 9    validated for already matched incoming Settlement Instructions), the realignment application process creates
10    automatically all the requested Settlement Instructions between the involved CSDs, referred hereafter as
11   T2S generated realignment Settlement Instructions. This automatic generation relies on links set in the ref-


                                                                                            Page 373 of 2017



[PDF page 374]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    erence data between the relevant CSDs and does not request from the T2S Actors any other action. It takes
 2    place immediately following either the validation of already matched Settlement Instructions, or the match-
 3    ing of Settlement Instructions matching in T2S.

 4    Realignment application process is also applied for external-CSD settlement.

 5    This section details the parameters required from T2S Actors to manage the realignment in T2S for cross-
 6   CSD and external-CSD settlement. It also details the resulting realignment chain with the description of the
 7   T2S generated realignment Settlement Instructions reported to the involved T2S Actors.

 8    For external-CSD settlement, only the process applying to the Settlement Instructions actually submitted to
 9   T2S is described. All actions required by the realignment but without interaction with T2S are not described.

10                               DIAGRAM 85 - REALIGNMENT APPLICATION PROCESS





11

12    1.6.1.10.2 Overview

13   Upon the matching of Settlement Instructions, or upon the validation of already matched Settlement Instruc-
14    tions, the realignment application process verifies if the incoming business Settlement Instructions are re-
15    quiring realignment Settlement Instructions on securities accounts other than those of the submitting T2S
16    Actors (e.g. on the accounts of the issuer CSD).





                                                                                            Page 374 of 2017



[PDF page 375]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   When the need to realign is identified, the realignment application process creates automatically the T2S
 2    generated realignment Settlement Instructions, based on the cross-CSD links set by CSDs in the reference
 3    data.

 4   The T2S generated realignment Settlement Instructions are then validated, and linked to the initial underly-
 5    ing Settlement Instructions through two links INFO providing the references of both business Settlement
 6    Instructions for information purposes. T2S ensures that the T2S generated realignment Settlement Instruc-
 7    tions and their business Settlement Instructions settle on an all-or-none basis.


 8    1.6.1.10.3 Realignment process

 9   Parametersnecessaryforrealignment

10    Role and links between CSDs for cross-CSD and external-CSD settlement

11    Irrespective of whether it is a cross-CSD or an external-CSD settlement, a CSD is defined for the realignment
12    process as:

13         l  The issuer CSD, when it is the CSD in which the security has been issued and distributed on behalf of
14       the Issuer;

15         l  The investor CSD, when it is the CSD of at least one party of the Settlement Instruction;

16         l  Or both, when it is the CSD in which the security has been issued and the CSD of at least one party of
17       the Settlement Instruction.

18   To manage the cross-CSD and external-CSD settlements, each investor CSD has the choice between:

19         l  Opening an omnibus account (see section below) in the books of the issuer CSD to reflect the holdings
20        of its participants for the securities, or;

21         l  Opening an omnibus account in the books of any other CSD being already an investor CSD for the same
22         financial instrument.

23    In both cases, the CSD where the omnibus account is opened is defined as the technical issuer of the inves-
24    tor CSD for the given securities. For a given ISIN, an investor CSD can define several such investor-type CSD
25     links, meaning that it can define several technical issuer CSDs for a given ISIN. However, one of those links
26    (and only one) should be given the preference for settlement under simple configurations (all CSDs in T2S,
27   no multi-issuance), this is the “default” link. Under more complex configurations (external CSD configuration,
28    multi-issuance), the preference should go first to one of the other “alternative” links, more specifically the
29   one pointing to the counterpart CSD, in case it is set up in the reference data. If T2S cannot find an alterna-
30     tive link to the counterparty CSD or if such an alternative link is found, but unusable due to a missing static
31    data (i.e. invalid or incomplete configuration of CSD Account Links), T2S reverts back to the valid default
32     links should be used also under those complex configurations.

33    Only one link, whether default or alternative, can be set up towards a given technical issuer CSD for a given
34    investor CSD and a given ISIN at the same point in time.

35   The issuer-type CSD link cannot be an alternative link, it has always to be defined as a “default” link. Only
36    investor-type links can be flagged “alternative”. Those links cannot be defined for an investor CSD outside
37   T2S and they cannot point to a technical issuer CSD outside T2S.



                                                                                            Page 375 of 2017



[PDF page 376]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   To that purpose, CSDs are required to configure the following set-up in the reference data:
 2

               PARAMETERS                                      DEFINITION

        Security CSD links                   Each investor CSD has to define at least one technical issuer CSD per securities
                                                                            it intends to set as eligible for settlement (See section Securities reference data
                                              [ 71]). This results in the creation of one or several links between the investor
                                   CSD and its technical issuer CSD(s) for a given financial instrument.

                                  Among those links, one (and only one) should be flagged “default”, the other
                                         ones being considered “alternative”.

                                      The alternative links can only be set up for T2S-in investor CSDs, pointing to a
                                             T2S-in technical issuer CSD.

                                             For a given investor CSD and a given ISIN, only one link (either default or al-
                                                  ternative) should point to a given technical issuer CSD.

                                             For a given investor CSD, the technical issuer CSD may be different for each
                                                    security. It is in most cases the issuer CSD of the security.

                                      The issuer CSD sets a CSD link with itself as issuer. This link cannot be an al-
                                                 ternative one, it is always a default one.

                                           (See section Configuration of securities accounts for cross-CSD settlement and
                                                external CSD settlement [ 97])

 3    This set-up is used by T2S to derive the realignment chain applicable to matched Settlement Instructions
 4    starting either from both investor CSDs (delivering and receiving) up to the issuer CSD(s) of the traded secu-
 5     rities when default links are used, or from the delivering investor CSD up to the receiving investor CSD (or
 6    vice versa) when alternative links are used.

 7

=== RETRIEVAL 7: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "reference", "question_type": "issuer_investor_csd_definitions"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[rts392-issuer-investor-csd]] — RTS 2017/392 Article 1 definitions: issuer CSD and investor CSD (English OJ text) (reviewed 2026-09-14; modes ['reference']; entities ['EU']; basis reference_description)
CITATION: Commission Delegated Regulation (EU) 2017/392 — English OJ text, Article 1 definitions (browser excerpt) | Regulation 2017/392 Article 1(a)–(g); OJ L 65, 10.3.2017; browser excerpt | version OJ L 65, 10.3.2017 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0392
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
LIMITATION: Partial browser capture of the original act; the consolidated EN page returned German text on 14 September 2026, so the library's consolidated capture is language-mislabelled.
LIMITATION: Roles depend on the security and relationship: one CSD can be issuer CSD for one issue and investor CSD for another.
EXCERPT (Regulation 2017/392 Article 1(a)–(g); OJ L 65, 10.3.2017; browser excerpt):
Article 1

Definitions

For the purposes of this Regulation, the following definitions apply:

(a)

	

‘review period’ means the period under review beginning on the day following the end of the previous review and evaluation period;

(b)

	

‘settlement instruction’ means a transfer order as defined in point (i) of Article 2 of Directive 98/26/EC of the European Parliament and of the Council (4);

(c)

	

‘settlement restriction’ means the blocking, reservation or earmarking of securities that make them unavailable for settlement, or the blocking or reservation of cash that make it unavailable for settlement;

(d)

	

‘exchange-traded fund’ (ETF) means a fund as defined in point (46) of Article 4(1) of Directive 2014/65/EU of the European Parliament and of the Council (5);

(e)

	

‘issuer CSD’ means a CSD which provides the core service referred to in point 1 or 2 of Section A of the Annex to Regulation (EU) No 909/2014 in relation to a securities issue;

(f)

	

‘investor CSD’ means a CSD that either is a participant in the securities settlement system operated by another CSD or that uses a third party or an intermediary that is a participant in the securities settlement system operated by another CSD in relation to a securities issue;

(g)

	

‘durable medium’ means any instrument which enables the storage of information in a way that is accessible for future reference for a period of time adequate for the purposes of the information, and allows the unchanged reproduction of the information stored.