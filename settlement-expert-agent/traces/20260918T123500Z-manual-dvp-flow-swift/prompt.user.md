EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-18T12:38:26.241379+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_service_access"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-xtrm-service]] — X-TRM service: operation, communications and access methods (§§3.1–3.4 opening, with the access-method table transcribed from the page image) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §§3.1–3.4.1 opening; PDF 36–38, printed 32–34 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §3.3 access-method table, transcribed from the rendered PDF 37 (text extraction column-garbled) | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Message codes (G50–G58, MT540–MT548, MT598) are listed as printed; their layouts are in the client-only Standard for X-TRM Users.
EXCERPT (§§3.1–3.4.1 opening; PDF 36–38, printed 32–34):
3 IMPLEMENTING PROVISIONS OF THE
SERVICE X-TRM


3.1 OPERATION OF THE SERVICE

The X-TRM provides auxiliary functionality:

    •  settlement of transactions in the Settlement Service (intra and cross-CSD
      settlement);

    •  settlement of transactions  in the Foreign Settlement Service (external
      settlement);

    •  forwarding operations to foreign settlement systems (routing)

    •  to the activity of central counterparty


The Service is available on working days as indicated in the TARGET operational
calendar.

Dates indicated in operations acquired by the X-TRM Service can also refer to
other  calendars  (e.g.  the  Borsa  calendar)  and  therefore  be  determined
independently by the system of origin, but must in any case be compatible with
the TARGET calendar.

The architecture of the Services requires that the relevant operation timetables
take account of the availability of the systems that the Service interacts with,
(i.e. Settlement System or the Foreign Settlement System)



3.2 COMMUNICATIONS

X-TRM Participants receive communications:

•  through the company website for communications of general nature
•  by registered post with return receipt, telegram, fax, post or other means
   that provide documentary evidence  of  receipt  of the communication  for
   communications of an individual nature
•  by  telematics means  for  operational-type communications regarding the
   ordinary administration of the Service.





32



[PDF page 37]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Members of the service communicate with Monte Titoli in writing by registered
letter with return receipt, telegram, fax, courier or other means that provide
documentary evidence of receipt of the communication. Communications of an
operational nature may also be sent by electronic means.


3.3 ACCESS METHOD


Members may use any  of the  following  interactive methods to access the
Service:

                       TECHNICAL TERMS OF USE

                           RNI                 SWIFT                MT-X/X-   FEATURES
                                                       TRM   ON-
                                                            FIN    E/O                              M.S.        F.T.                         FILEACT      LINE
                                                        INTERACT

    ACQUISITION/CHANGING   X        X         X          X         X
    TRANSACTIONS
                        G52      G50       MT540      G50
                        G53      G51       MT541      G51
                                            MT542
                                            MT543
                                            MT548

    RESULTS         OF            X                    X         X
   OPERATIONS
   TRANSMISSION                  G56                  G56
    (ROM/ACB)



   ALIGNMENT  ON-LINE    X                  X
   SYSTEM USER
                        G57                MT598
                        G58                MT548

3.4 FUNCTIONALITY OF THE X-TRM SERVICE FOR TRANSACTION TO
BE SETTLED IN THE SETTLEMENT SERVICE (IN T2S)

In  relation  to  the  transactions  to be  settled between  participants  to  the
Settlement Service operated by the T2S platform, the X-TRM provides the
following features:

    •  acquisition of operations
        o  validation of settlement instructions
        o  valorisation of settlement instructions




33



[PDF page 38]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





    •  operations Management
        o  amendment of settlement Instructions
        o  deletion of settlement instruction
        o  doubling
        o  hold/release
        o  routing to Settlement Service
        o  post-trading reporting


  3.4.1 Acquisition of operations

The types of operations that can be entered into the X-TRM Service can be
summarised as follows:

TABLE 1

                                TRANSAC
 OPERATIONS                                ORIGIN7               ACRONYM          TION
                                 TYPE

 Sale/purchase of                            Guaranteed and unguaranteed
 securities                                    Markets
                                                   also  on   behalf   of  X-TRM               CVT             DVP/RVP
                                                    Participants

                                       X-TRM Participants

                                            Guaranteed and unguaranteed
                                             Markets
               PCT   (Buy     sell                                                   also  on   behalf   of  X-TRM
 Repurchase       back)                               DVP/RVP  Participants
 agreement
               PCR (Classic repo)

                                       X-TRM Participants

                                   FOP,                                                  Central Bank
                              DWP,RV Securities/cash
               CTC                 P,  RWP,
 transfer                                X-TRM Participants                                 PFOD,
                                             Automatic
                               FOP


When operations are entered into the X-TRM Service, regardless of their origin, a
check is made that counterparty does not thereby assume exclusive mandate for
release to another person. In the latter case, if there is no match between X-TRM
Participant photo which the counterparty is associated and the subject who place
the operation the operation is rejected.


7 The origins listed are those that are valid on the date of publication of this document.




34
EXCERPT (§3.3 access-method table, transcribed from the rendered PDF 37 (text extraction column-garbled)):
{
  "source_id": "dd1cf7cb930b",
  "source_title": "Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025",
  "source_sha256": "see source register",
  "verified_as_of": "2026-09-14",
  "actual_content_language": "en",
  "authoritative_language": "it",
  "translation_note": "English version; the Italian text prevails (cover, PDF 1).",
  "review": "Transcribed from the rendered page images (110 dpi) implementation/2026-09-14-settlement-agent/evidence/dd1cf7cb930b-p37-37.png and p39–p41; text extraction of these tables was column-garbled, so the images are the reference.",
  "locator": "§3.3 Access method, PDF 37 (printed 33)",
  "table": "TECHNICAL TERMS OF USE",
  "columns": [
    "RNI M.S.",
    "RNI F.T.",
    "SWIFT FIN e/o InterAct",
    "SWIFT FileAct",
    "MT-X/X-TRM On-line"
  ],
  "rows": [
    {
      "feature": "Acquisition/changing transactions",
      "RNI M.S.": [
        "X",
        "G52",
        "G53"
      ],
      "RNI F.T.": [
        "X",
        "G50",
        "G51"
      ],
      "SWIFT FIN e/o InterAct": [
        "X",
        "MT540",
        "MT541",
        "MT542",
        "MT543",
        "MT548"
      ],
      "SWIFT FileAct": [
        "X",
        "G50",
        "G51"
      ],
      "MT-X/X-TRM On-line": [
        "X"
      ]
    },
    {
      "feature": "Results of operations transmission (ROM/ACB)",
      "RNI M.S.": [],
      "RNI F.T.": [
        "X",
        "G56"
      ],
      "SWIFT FIN e/o InterAct": [],
      "SWIFT FileAct": [
        "X",
        "G56"
      ],
      "MT-X/X-TRM On-line": [
        "X"
      ]
    },
    {
      "feature": "Alignment on-line system user",
      "RNI M.S.": [
        "X",
        "G57",
        "G58"
      ],
      "RNI F.T.": [],
      "SWIFT FIN e/o InterAct": [
        "X",
        "MT598",
        "MT548"
      ],
      "SWIFT FileAct": [],
      "MT-X/X-TRM On-line": []
    }
  ],
  "notes": [
    "Codes are reproduced as printed (RNI message codes G50–G58; SWIFT MT540–MT543, MT548, MT598). Their field-level layouts are in the client-only 'Standard for X-TRM Users' (A2A MT / RNI, VER.01.09 per ON_20/2026), which is not in the library.",
    "An 'X' marks availability of the feature on that channel as printed."
  ]
}

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_field_mapping"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-xtrm-field-mapping]] — X-TRM fields versus T2S fields: mandatory, additional and optional matching information (§3.4.1 Table 2, transcribed from the page images) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §3.4.1 Table 2 and additional information list; PDF 39–41, printed 35–37 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | Table 2 transcription from rendered PDF 39–41 with recorded anomalies | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Functional correspondence only: not the A2A/RNI message layouts, not a T2S XSD, and two source cells are truncated in the original layout (recorded).
LIMITATION: Footnote (1) referenced in the table was not located on the reviewed pages.
EXCERPT (§3.4.1 Table 2 and additional information list; PDF 39–41, printed 35–37):
Operations must contain  all information  indicated  in the  following table as
mandatory. For convenience the related T2S filed are included

It  is noted that  for the matching purposes the T2S platform distinguishes
between (see Table 2):

    •  mandatory information (if not specified can assume default values);
    •  optional information, divided into:
       o  additional (if specified by a counterparty are considered mandatory
              fields feedback and therefore must also be specified by the other
            party);
       o  optional (considered fields of feedback required only  if specified by
           both counterparties).



                                          TYPE            DEFAULT
      X-TRM FIELDS      T2S FIELDS
                                         INFORMATION    VALUE
        Issuer                Delivering    /               NO
                             Receiving                                             NO
                              Party     BIC
        Counterparty        (based     on
                                Securities
                        Movement
                                             NO
                      CSD         of
                               Delivering    /       Code  of System
                             Receiving        Custody Issuer
                              Party   (based
                         on   Securities
                        Movement      Mandatory      NO       Code  of System
                           Type)        Custody
         Counterparty(1)


                            Intended
        Settlement Date      Settlement
                           Date



                                                        Date of release of       Data Executed       Trade Date
                                                             the contract  in X-
                                              TRM





35



[PDF page 40]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





                                          TYPE            DEFAULT
      X-TRM FIELDS      T2S FIELDS
                                         INFORMATION    VALUE
                                             NO

        Object     Code
                            ISIN
        Negotiated


                            Settlement                  NO
        Quantity
                             Quantity
                            Settlement                  NO
        Countervalue
                        Amount
        Settlement                                 NO
                            Currency
        Currency
                                Securities                   NO
       Mark              Movement
                          Type
        Countervalue         Credit  / Debit               NO
        Verse                 Indicator
                         Payment Type               NO
         n.a.                    (this fields will
                          be                 fill
                                             NO                            Settlement
        Settlement
                              Transaction
        Transaction
                              Condition
         Condition(1)
                            (Opt Out)                                                  Additional
                           Trade                     NO        Trade
                              Transaction        Transaction
                              Condition        Condition
                       (CUM   /   Ex
                                 Client        of               NO
                               Delivering    /         Beneficiary
                             Receiving        Issuer Code BIC
                              Party   (based
         Beneficiary         on   Securities               NO
                                               Optional        Counterpart Code    Movement
       BIC                 Type)
                     Common                   NO
      Common   Trade
                           Trade
        Reference
                            Reference





36



[PDF page 41]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





                                          TYPE            DEFAULT
      X-TRM FIELDS      T2S FIELDS
                                         INFORMATION    VALUE
                                Securities                   NO
                            Account     of
                               Delivering    /
        Counterpart
                             Receiving
        Settlement
                              Party
         Securities
                            (based     on
        Account
                                Securities
                        Movement
                           Type)


In addition to the information set out above, in X-TRM it is possible to specify the
following additional information:
    •  ISO code of the operation
    •   partial settlement indicator
    •   priority settlement indicator
    •  indicator for the connection of settlement Instructions
    •  indicator of the changeability of settlement instructions
    •   identification code of the "pool" of settlement ‘’Pool reference ID’’
    •   identification code of the settlement Instructions associates "Reference ID
       for Settlement Instructions"
    •   identification code of settlement restrictions ‘’Reference ID for Settlement
       Restrictions’’
    •   identification  code  for  the  suspension,  cancellation,  modification  of
      settlement instruction.
EXCERPT (Table 2 transcription from rendered PDF 39–41 with recorded anomalies):
{
  "source_id": "dd1cf7cb930b",
  "source_title": "Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025",
  "source_sha256": "see source register",
  "verified_as_of": "2026-09-14",
  "actual_content_language": "en",
  "authoritative_language": "it",
  "translation_note": "English version; the Italian text prevails (cover, PDF 1).",
  "review": "Transcribed from the rendered page images (110 dpi) implementation/2026-09-14-settlement-agent/evidence/dd1cf7cb930b-p37-37.png and p39–p41; text extraction of these tables was column-garbled, so the images are the reference.",
  "locator": "§3.4.1 Table 2 (X-TRM fields vs T2S fields), PDF 39–41 (printed 35–37)",
  "type_semantics": {
    "Mandatory": "mandatory information (if not specified can assume default values)",
    "Additional": "if specified by a counterparty, considered mandatory feedback fields and therefore must also be specified by the other party",
    "Optional": "considered feedback fields required only if specified by both counterparties"
  },
  "rows": [
    {
      "xtrm_field": "Issuer",
      "t2s_field": "Delivering / Receiving Party BIC (based on Securities Movement Type)",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Counterparty",
      "t2s_field": "Delivering / Receiving Party BIC (based on Securities Movement Type)",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Code of System Custody Issuer",
      "t2s_field": "CSD of Delivering / Receiving Party (based on Securities Movement Type)",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Code of System Custody Counterparty (footnote 1 marker)",
      "t2s_field": "CSD of Delivering / Receiving Party (based on Securities Movement Type)",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Settlement Date",
      "t2s_field": "Intended Settlement Date",
      "type": "Mandatory",
      "default": "(blank as printed)"
    },
    {
      "xtrm_field": "Data Executed",
      "t2s_field": "Trade Date",
      "type": "Mandatory",
      "default": "Date of release of the contract in X-TRM"
    },
    {
      "xtrm_field": "Object Code Negotiated",
      "t2s_field": "ISIN",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Quantity",
      "t2s_field": "Settlement Quantity",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Countervalue",
      "t2s_field": "Settlement Amount",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Settlement Currency",
      "t2s_field": "Currency",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Mark",
      "t2s_field": "Securities Movement Type",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Countervalue Verse",
      "t2s_field": "Credit / Debit Indicator",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "n.a.",
      "t2s_field": "Payment Type (this field will be fill… — cell text truncated in the original layout)",
      "type": "Mandatory",
      "default": "NO"
    },
    {
      "xtrm_field": "Settlement Transaction Condition (footnote 1 marker)",
      "t2s_field": "Settlement Transaction Condition (Opt Out)",
      "type": "Additional",
      "default": "NO"
    },
    {
      "xtrm_field": "Trade Transaction Condition",
      "t2s_field": "Trade Transaction Condition (CUM / Ex — cell text truncated in the original layout)",
      "type": "Additional",
      "default": "NO"
    },
    {
      "xtrm_field": "Beneficiary Issuer Code BIC",
      "t2s_field": "Client of Delivering / Receiving Party (based on Securities Movement Type)",
      "type": "Optional",
      "default": "NO"
    },
    {
      "xtrm_field": "Beneficiary Counterpart Code BIC",
      "t2s_field": "Client of Delivering / Receiving Party (based on Securities Movement Type)",
      "type": "Optional",
      "default": "NO"
    },
    {
      "xtrm_field": "Common Trade Reference",
      "t2s_field": "Common Trade Reference",
      "type": "Optional",
      "default": "NO"
    },
    {
      "xtrm_field": "Counterpart Settlement Securities Account",
      "t2s_field": "Securities Account of Delivering / Receiving Party (based on Securities Movement Type)",
      "type": "Optional",
      "default": "NO"
    }
  ],
  "additional_information_fields": [
    "ISO code of the operation",
    "partial settlement indicator",
    "priority settlement indicator",
    "indicator for the connection of settlement Instructions",
    "indicator of the changeability of settlement instructions",
    "identification code of the pool of settlement (Pool reference ID)",
    "identification code of the settlement Instructions associates (Reference ID for Settlement Instructions)",
    "identification code of settlement restrictions (Reference ID for Settlement Restrictions)",
    "identification code for the suspension, cancellation, modification of settlement instruction"
  ],
  "anomalies": [
    "Footnote marker (1) appears on two rows; the footnote text was not located on PDF 39–41 in the text extraction or the rendered images.",
    "Two T2S-field cells are visibly truncated in the original page layout ('this fields will be fill…', 'CUM / Ex…'); the truncated wording is preserved as an anomaly, not completed."
  ],
  "counts": {
    "mandatory": 13,
    "additional": 2,
    "optional": 4
  },
  "scope": "Functional field correspondence as published by Milan for ICP/X-TRM users. Not the client-only Standard for X-TRM Users message layouts; not a production XSD; not certification of T2S message paths."
}

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_connectivity_and_static_data"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_instruction_processing_rules"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-instruction-processing]] — Acquisition, validation, linked/CoSD instructions, partial settlement, priority, collateral, processing phases and CAoF (Articles 68, 73–76) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Article 68; PDF 49–50, printed 48–49 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
CITATION: Regulations as of 26 January 2026 | Articles 73–76; PDF 52–53, printed 51–52 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Articles 69–72 (matching, cancellation, hold, finality) are the 13 September section milan-finality.
EXCERPT (Article 68; PDF 49–50, printed 48–49):
Article 68 – Acquisition of settlement Instructions

1. Settlement instructions are acquired by the Settlement Service regarding:
      a) individual transactions (DVP or FOP);
      b) bilateral netting of securities and cash balances;
       c) securities and cash balances, netted via interposition of a Central
         Counterparty.
2. During acquisition, the Settlement Services checks:
    ▪ the completeness of the settlement instruction and its formal correctness to
     ensure the ensuing processing by the Service; and
    ▪ the matching of the settlement instruction data with personal data found in
     T2S (common static data), as well as with any restrictions, including the
     matching of the financial instruments involved with the provisions of Article
      86.
3. The validated settlement Instructions are forwarded to the subsequent phases
   of the service. Non-validated Settlement Instructions are rejected.
4. Settlement Instructions can establish that the settlement:
    ▪  is connected to the settlement of linked instructions; or
    ▪  is  conditional on  the  occurrence  of  specific  conditions  outside T2S
      (Conditional Securities Delivery CoSD7).
5. Participants may also specify:
    ▪ the possibility of a partial settlement, within the limits allowed by the T2S
      system’s functionalities; and
    ▪ the rule priority of the settlement instruction entered, within the limits
      allowed by the functionalities of T2S and taking into account that Monte
       Titoli  assigns  priority  to  the  settlement  Instructions  in  which  the
      counterparty is the Italian Ministry of Finance, those involving monetary


7 Conditional securities delivery in T2S refers to a procedure in which the final posting of securities and/or cash is dependent on
the successful completion of an additional action or event external to T2S and confirmed by an administering party.

48    In force as of 26 January 2026



[PDF page 50]

                                                            SERVICE REGULATIONS


      policy transactions and those concerning transfer of collateral by the Bank
      of  Italy  and,  subsequently,  those coming from Market Management
     Companies.
6. Participants are informed of the result of the validation process.
EXCERPT (Articles 73–76; PDF 52–53, printed 51–52):
Article 73– Automatic mechanisms for posting Collateral

1.   The participants to the Settlement Service and/or their Agent Banks that
    have previously communicated their intention to avail themselves of the
     automatic mechanisms for posting Collateral must, with the methods and
     time frames provided for in the Instructions, indicate the securities accounts
     and/or the positions that can be used for collateralisation and the exposure
      limits to be considered in the settlement process.
2.   The activation of the collateralisation mechanisms causes the automatic
     generation  of  settlement  instructions by  the Settlement  Service. The
     settlement instructions arising from collateralisation are settled jointly with
     the original Settlement Instructions, relative to which the mechanism for
     posting Collateral was activated.

Article 74 – Processing of the settlement Instructions

1. The settlement process includes a night-time phase and a day-time phase. In
   each phase the Settlement Instructions are processed on a gross basis.
2. In  each  phase,  according  to  the  eligibility  criteria  of  the  settlement
   Instructions, Monte Titoli settles:
      a) the new settlement Instructions entered before each phase during the
         night-time settlement phase and in real-time during the daytime phase,
          including the instructions for realignment and those resulting from any
         corporate actions; and
      b) the Settlement Instructions that remained unsettled in the previous
         phase.

51    In force as of 26 January 2026



[PDF page 53]

                                                            SERVICE REGULATIONS


3. The settlement Instructions are processed through the following steps:
      a) check on the settlement status of the instruction;
      b) check on the counterparties’ securities and cash account capacities. This
          includes  verifying whether resources are  available as a  result  of
           collateralisation, as well as checking any exposure limits set by the
          Participant or its Agent Bank in the TARGET2 system;
       c)  if there is securities and cash capacity, T2S settles the securities by
          debiting the Seller and crediting the Purchaser with the amount of the
          transaction.
4.  If a number of settlement instructions are handled jointly in the same phase
    for reasons of optimisation, T2S makes the checks referred to in letter b) of
   the previous paragraph, based on the net balance following the relevant
   settlement Instructions.  If there  is not enough capacity to settle the net
   balance, T2S identifies the settlement Instructions that cannot be settled and
   then, taking into account their characteristics:
        -  checks the possibility of settling them through a collateralisation process,
         in the event of a cash deficit;
        -  checks the possibility of partially settling them, in the event of a
        securities deficit.
5. Settlement Instructions that have not been settled because of insufficient
   securities or cash are re-proposed in the subsequent phase of the same
   settlement day or for settlement on the subsequent day, until they are settled
   or cancelled in accordance with the Article 70.
6. Participants may change settlement Instructions that have been proposed
   again, also partially, but only with regard to the status indicators, on condition
   that such settlement Instructions have not been entered as non-changeable.

Article 75 – Sequence in Processing Settlement Instructions

1. To improve  the  efficiency  of  the  settlement  process, TS2 implements
   optimisation mechanisms aimed at maximising its outcome.
2.  If several settlement Instructions make use of the resources available on the
  same securities or cash account, the optimisation process takes into account
   the priority criteria for the management of settlement Instructions referred to
    in Article 68, paragraph 5. In the event of equal priority, the settlement
   Instructions with the  earlier settlement date are settled  first within the
   functioning limits of the T2S platform.

Article 76 – Management of non-settled Settlement Instructions
(Corporate Action of Flow - CAoF)

1. Monte Titoli may change or cancel the settlement Instructions that have not
   been  settled on  the  established  settlement date and concern  financial
   instruments involved in corporate actions or, in relation to such Instructions,
     it may  enter  additional  settlement  Instructions aimed  at  rectifying the
   distorting impacts of the event. The operating procedures for the management
   of these settlement Instructions are set out in the Instructions.



52    In force as of 26 January 2026

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_lifecycle_maintenance"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-xtrm-lifecycle]] — X-TRM lifecycle for T2S-settled transactions: validation, enrichment, doubling, routing, allegement disclosure, maintenance (modify/cancel/hold-release) and reporting (§§3.4.2–3.4.8) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §§3.4.2–3.4.8; PDF 41–48, printed 37–44 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Market/CCP-specific maintenance permissions are published in Service Notices, which are not admitted.
EXCERPT (§§3.4.2–3.4.8; PDF 41–48, printed 37–44):
3.4.2 Validation in X-TRM Service

Validation is the process specific for each type of operation, which  executes
formal, logical and congruency checks on the elementary data of each individual
settlement instruction.

If the operation is not validated in X-TRM, the service sends a rejection message
to the subject that entered it.

If the operation exceeds correctly the validation process in X-TRM, the Service
forwards the settlement instruction to the subsequent phases of the process.





37



[PDF page 42]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





  3.4.3 Valorisation (c.d.“Enrichment”)

The  valorization  is  the X-TRM  process  that  allows  to add  the  necessary
information to complete the settlement instructions.

The additional information consist of the data in the database of the X-TRM (e.g.
relations between the parties, securities account and other default information)
and other data calculated according to the algorithm defined.

The functionality of enhancement allows, according to predefined algorithms, of:

    •  calculate the cash amount of a CVT operation, using the details available
       in the messages and other information stored in the database of the X-
     TRM;

    •  create the settlement instructions ("spot" and "forward") of an operation
     PCT / PCR valued using data available in the transaction originally entered
     by the participant.

Valorisation  is performed only  if no  errors have been detected during the
validation phase.





38



[PDF page 43]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The valorisation relates to the following fields:


                 DEFAULT        NOTE   FIELD
                 VALUE

   EXPENSES               NO                Entered only for OTC operations
  AMOUNT

   EXCHANGE                         Represents the conversion ration between the
                  1   RATE                                 trading currency and the settlement currency.

   PRICE        NO

   TOTAL                          Can be expressed as a total amount or as a
   COMMISSIO    NO                percentage.   It   is  entered  only   for  OTC
  N                                     operations.

                      Interest
   UNIT            accrued   from
   ACCRUAL         the last coupon
                   detachment

   TYPE
               NO
   OPERATION



Accounting values (countervalues, interest, etc.) are calculated according to the
codified rules for each type of operation.

Chapter 5 entitled “METHODS OF CALCULATION” sets out all the formulas for
data calculated by the Service.



  3.4.4 Doubling operations

All trades sent from markets, central banks and central counterparties, which by
definition are already matched, are submitted to the doubling process.

The process consists of duplicating individual communications received by the X-
TRM Service into two matched operations, so that each counterparty can fully
visualise their operations.

The X-TRM Service attributes a reference code to each individual operation.





39



[PDF page 44]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





  3.4.5 Routing of settlement instructions to the Settlement Service

Once  completed  the  Valorization  process  the X-TRM  forwards  settlement
instructions to the Settlement Service.


The forwarding of operations to the Settlement Service occurs in two different
methods:

•  batch method: before the starting of the night-time settlement phase;

•  real-time: at the moment when the instructions are entered, during the
   opening hours of the X-TRM Service.

Settlement instructions  relating to operations acquired from Markets and/or
Central Counterparties are forwarded to the Settlement Service according to the
timing agreed respectively with the Central Counterparties and the Markets and
indicated in the Service Notice.

Settlement Instructions relating to OTC transactions are sent in real time to the
Settlement Service as they must be subjected to matching.

T2S platform conducts  its own validation applying specific rules to check the
required fields and optional fields and / or additional possibly used.

If the settlement instruction  is not validated in T2S, X-TRM Service sends a
rejection message to the subject that entered it.

Only if the settlement instruction passes also the Validation process in T2S the X-
TRM Service confers a univocal reference code (reference ID) and sends a
message of acceptance to the person who posted it.



  3.4.6 Matching Disclosure


Subsequently the X-TRM Service provides, the disclosure on the acknowledgment
of the settlement Instructions (allegement) in T2S platform.

In particular X-TRM Participants receive the following messages:

    •  allegement notification: is provided to the counterpart of an settlement
       instruction not found;
    •  allegement  remove:   if  settlement  instruction   is  matched  by  the
      counterpart





40



[PDF page 45]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





    •  allegement cancellation: when the settlement instruction is not matched
     and has been canceled the counterpart.
    •  allegment  reporting:  disclosure concerning  all  instructions  waiting  for
      confirmation

The operations to be settled intra-CSD entered by the Central Banks, Markets
and CCP on behalf of  its participants are forwarded to the T2S platform as
already matched.



  3.4.7 Management (Maintenance) of settlement instructions routed to
  T2S platform.

The X-TRM allows participants to use the following features of management of
settlement instructions routed to T2S:

    •  modification
    •  cancellation
    •  hold/release

For OTC transactions functionality maintenance are made available to X-TRM
Participants.

For  market  operations  not  guaranteed  or  guaranteed  by  the  Central
Counterparty, the use of the maintenance functionality is subject to the rules of
Markets or of the Central Counterparties.

The Markets and Central Counterparties that allow the use of the functionality of
maintenance are indicated in the Communications of Service.


   A. MODIFICATION OF SETTLEMENT INSTRUCTION


Pursuant to the Service Regulations, X-TRM Service allows the editing of the
settlement instructions forwarded to the T2S platform in the manner and within
the limits specified in the document T2S User Requirements.

In particular, the Participants to the X-TRM Service can edit only the following
process indicators:

    •   partialisation indicator;
    •   priorities of Regulation;
    •  blocks for connections between Settlement Instructions (linkages blocks).




41



[PDF page 46]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The change  is done by sending a modification instruction. For any change a
single Settlement Instruction have to be entered. Instructions of modification are
accepted and processed unless:

    •  settlement instruction that must be modified  is not already settled or
      canceled;
    •  settlement instruction that must be modified is not identified as ‘’CoSD’’

Settlement instruction partially settled can be changed only with reference to the
indicator "priority of regulation."

Outside of the cases identified by the T2S User Requirements, any other changes
of the settlement Instructions must be performed by deleting and re-entering it
by the X-TRM Participant.

X-TRM Participants can modify operations submitted by Markets and Central
Counterparties, provided that the management company of the markets and
central counterparties communicate to Monte  Titoli to make this functionality
available.

The modification of operations from the central bank is not allowed to X-TRM
Participants and it is allowed only to the systems from which they originate.

Modification  instructions  are  subject  to  the  processes  of  validation  and
valorization in X-TRM.

The Service sends the X-TRM  Participant an acceptance message  for each
formally valid update request or an error message if invalid. In addition to all the
data corresponding  to  the  operation,  the  operator must  also  provide  the
reference code given by the X-TRM Service during the entry phase.


   B. CANCELLATION OF OPERATIONS FROM SETTLEMENT SERVICE

The X-TRM Service allows the cancellation of settlement instructions sent to the
T2S platform, in the manner and within the limits specified in the document T2S
User Requirements.

The cancellation of the trades originating from the central bank is not allowed to
X-TRM participants and  it  is allowed only to the systems from which they
originate.

The cancellation  of operations entered by the Markets and by the Central
Counterparties  it  is possible for X- TRM Participants only  if the management





42



[PDF page 47]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





company of the markets and the central counterparties have communicated to
Monte Titoli to make this functionality available



   C. HOLD AND RELEASE FUNCTIONALITY

The X-TRM Service allows the suspension of settlement instructions sent to the
Settlement  Service,  in  the manner and  within  the  limits  specified  in  the
document T2S User Requirements.

To the settlement instructions is attributed to the state of ‘’release’’ unless one of
the four indicators "hold" provided by the T2S platform (Party Hold, Hold CSD,
CSD Validation Hold, Hold cOsd) is activated.

The enabling to the use of H&R functionality can be configured based on the role
(Party)  of  the  Participant  or  at  the  level  of  securities  account  (default
configuration).


The hold & release functionality is not avaible for settlement instructions entered
in CoSD modality.

The change of the indicator may occur during the opening of the X-TRM Service.

The X-TRM  Service  informs  the  counterparty  of  the  Participant who  has
requested the suspension "hold" of a settlement instruction, on the ISD and only
if the corresponding settlement instruction is in the "release" state.

The valorisation of the hold/release indicator for the repurchase agreements
applies both to the spot and to the forward transactions and  it is possible to
change it distinctly for each of the two operations, also after the settlement of
the spot transaction.

The hold and release functionality of operations entered by the Markets and by
the Central Counterparties,  it  is possible for X- TRM Participants only  if the
management  company  of  the  markets  and  central  counterparties  have
communicated to Monte Titoli to make this functionality available.

  3.4.8 Post Trading reporting

Pursuant to the Service Regulations, the X-TRM Service makes available upon
request of Participants report regarding operations entered directly by members
themselves or originating from markets/central banks/central counterparties, by
the following methods:

•  Report on request





43



[PDF page 48]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





   This is made available at any time of the day during the opening hours of the
  X-TRM Service.  It enables members to verify the status of  all operations
   entered during the day or on the preceding days.

   The main criteria that can be used to customise the selection of relevant
   operations are:

     -  Counterparty code
     -  Object code traded
     -  Operation type
     -  Settlement date
     -  Execution date
     -  Date entered
     -  Status of the operation (valid or cancelled)
     -  Matching status (matched, outbound, acknowledged)
     -  Origin (user system, market)
     -  Settlement system
     -  Status of the hold/release indicators;
     -  Status of the bilateral cancellation indicators.

•  Online report

   Enables members of the Service to obtain a real time report on all operations
   present in the system.

•  Original entry on-screen report

   This  function enables  selected  operations  to be  displayed on-screen  or
   printed, including the hold/release indicator. In addition to enquiries, the on-
   screen function allows the operations displayed to be updated or cancelled.

=== RETRIEVAL 6: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "native_message_overview", "release": "R2026.JUN"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-messages]] — Native message families and realignment notification (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §2.3 realignment dialogue; PDF 753 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §2.3.8 inbound/outbound messages; PDF 778 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: T2S-native messages, not bank-to-local-CSD formats; subscriptions and privileges affect recipients.
LIMITATION: No production payload or full schema admitted.
EXCERPT (§2.3 realignment dialogue; PDF 753):
This analysis may result in the detection of the following settlement contexts:

 3         l  [Cross-CSD contexts] When the settlement context is a cross-CSD context (including external-CSD
 4        context):

 5      – [Unsuccessful generation of realignment] If T2S cannot create the necessary realignment due to
 6         erroneous links or accounts configuration or to unsuccessful validation on potential T2S generated
 7          realignment Settlement Instructions (See section Realignment), the inbound Settlement Instruction is
 8          cancelled (See section Settlement Instruction Cancellation Processing [ 773]);

 9      – [Successful generation of realignment] If T2S can create the necessary realignment:

10             ▪  T2S creates the additional T2S generated realignment Settlement Instructions corresponding to
11             the necessary securities realignment and links these additional instructions to the inbound Settle-
12           ment Instruction for a settlement on an all-or-none basis.
13             For each T2S generated realignment Settlement Instruction, a “Realignment” SecuritiesSettle-
14              mentTransactionGenerationNotification is sent to the CSD involved in the realignment chain to no-
15                  tify the creation of additional instructions to be settled on their accounts; these realignment in-
16               structions inform the corresponding cross-border business instructions that caused their genera-
17               tion as well as the T2S Matching Reference assigned to all realignment and business instructions
18             conveying a transaction.

19             ▪  The Settlement Instruction is processed further;

20         l  [Intra-CSD context] When the settlement context is an intra-CSD context, the Settlement Instruction
21          is processed further.


                                                                                            Page 753 of 2017
EXCERPT (§2.3.8 inbound/outbound messages; PDF 778):
[PDF page 778]

                                                                  T2S User Detailed Functional Specifications
                                                                                  Dialogue between T2S and T2S Actors
                                                                                Send Settlement Instruction

1    2.3.8 Inbound and Outbound messages


2    2.3.8.1 Inbound message
3

                                      ISO MESSAGE                                       ISO CODE

      SecuritiesSettlementTransactionInstruction                                                sese.023.001.11


4    2.3.8.2 Outbound messages
5

                              ISO MESSAGE/ MESSAGE USAGE                                ISO CODE

      SecuritiesSettlementTransactionStatusAdvice / “CoSD Hold”                                 sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Rejected”                                   sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted”                                  sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted with Hold"                         sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted with CSD Validation Hold”           sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Matched”                                   sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Cancelled”                                  sese.024.001.12

      SecuritiesSettlementTransactionAllegementNotification                                     sese.028.001.10

      SecuritiesSettlementAllegementRemovalAdvice                                             sese.029.001.06

      SecuritiesMessageCancellationAdvice                                                    semt.020.001.07

      SecuritiesSettlementTransactionStatusAdvice / ”No hold remain(s)”                          sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Eligibility Failure”                            sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Intraday Restriction”                         sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Provision Check Failure”                      sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Partial Settlement (unsettled part)”           sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”CoSD awaiting from Administering Party”      sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / "Counterparty´s Settlement Instruction on      sese.024.001.12
      Hold"

      SecuritiesSettlementTransactionConfirmation / “Full Settlement”                             sese.025.001.11

      SecuritiesSettlementTransactionConfirmation / “Last Partial Settlement”                      sese.025.001.11

      SecuritiesSettlementTransactionConfirmation / “Partial Settlement (settled part)”              sese.025.001.11

      SecuritiesSettlementTransactionGenerationNotification / ”Realignment”                       sese.032.001.11



                                                                                          Page 778 of 2017

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

=== RETRIEVAL 7: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "native_message_overview", "release": "R2026.JUN"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-messages]] — Native message families and realignment notification (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §2.3 realignment dialogue; PDF 753 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §2.3.8 inbound/outbound messages; PDF 778 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: T2S-native messages, not bank-to-local-CSD formats; subscriptions and privileges affect recipients.
LIMITATION: No production payload or full schema admitted.
EXCERPT (§2.3 realignment dialogue; PDF 753):
This analysis may result in the detection of the following settlement contexts:

 3         l  [Cross-CSD contexts] When the settlement context is a cross-CSD context (including external-CSD
 4        context):

 5      – [Unsuccessful generation of realignment] If T2S cannot create the necessary realignment due to
 6         erroneous links or accounts configuration or to unsuccessful validation on potential T2S generated
 7          realignment Settlement Instructions (See section Realignment), the inbound Settlement Instruction is
 8          cancelled (See section Settlement Instruction Cancellation Processing [ 773]);

 9      – [Successful generation of realignment] If T2S can create the necessary realignment:

10             ▪  T2S creates the additional T2S generated realignment Settlement Instructions corresponding to
11             the necessary securities realignment and links these additional instructions to the inbound Settle-
12           ment Instruction for a settlement on an all-or-none basis.
13             For each T2S generated realignment Settlement Instruction, a “Realignment” SecuritiesSettle-
14              mentTransactionGenerationNotification is sent to the CSD involved in the realignment chain to no-
15                  tify the creation of additional instructions to be settled on their accounts; these realignment in-
16               structions inform the corresponding cross-border business instructions that caused their genera-
17               tion as well as the T2S Matching Reference assigned to all realignment and business instructions
18             conveying a transaction.

19             ▪  The Settlement Instruction is processed further;

20         l  [Intra-CSD context] When the settlement context is an intra-CSD context, the Settlement Instruction
21          is processed further.


                                                                                            Page 753 of 2017
EXCERPT (§2.3.8 inbound/outbound messages; PDF 778):
[PDF page 778]

                                                                  T2S User Detailed Functional Specifications
                                                                                  Dialogue between T2S and T2S Actors
                                                                                Send Settlement Instruction

1    2.3.8 Inbound and Outbound messages


2    2.3.8.1 Inbound message
3

                                      ISO MESSAGE                                       ISO CODE

      SecuritiesSettlementTransactionInstruction                                                sese.023.001.11


4    2.3.8.2 Outbound messages
5

                              ISO MESSAGE/ MESSAGE USAGE                                ISO CODE

      SecuritiesSettlementTransactionStatusAdvice / “CoSD Hold”                                 sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Rejected”                                   sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted”                                  sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted with Hold"                         sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Accepted with CSD Validation Hold”           sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Matched”                                   sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Cancelled”                                  sese.024.001.12

      SecuritiesSettlementTransactionAllegementNotification                                     sese.028.001.10

      SecuritiesSettlementAllegementRemovalAdvice                                             sese.029.001.06

      SecuritiesMessageCancellationAdvice                                                    semt.020.001.07

      SecuritiesSettlementTransactionStatusAdvice / ”No hold remain(s)”                          sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Eligibility Failure”                            sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Intraday Restriction”                         sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”Provision Check Failure”                      sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / “Partial Settlement (unsettled part)”           sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / ”CoSD awaiting from Administering Party”      sese.024.001.12

      SecuritiesSettlementTransactionStatusAdvice / "Counterparty´s Settlement Instruction on      sese.024.001.12
      Hold"

      SecuritiesSettlementTransactionConfirmation / “Full Settlement”                             sese.025.001.11

      SecuritiesSettlementTransactionConfirmation / “Last Partial Settlement”                      sese.025.001.11

      SecuritiesSettlementTransactionConfirmation / “Partial Settlement (settled part)”              sese.025.001.11

      SecuritiesSettlementTransactionGenerationNotification / ”Realignment”                       sese.032.001.11



                                                                                          Page 778 of 2017

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

=== RETRIEVAL 8: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
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

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

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

=== RETRIEVAL 9: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

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

=== RETRIEVAL 10: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_fields"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

=== RETRIEVAL 11: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-finality]] — Matching, cancellation, hold and SF1/SF2/SF3 (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/defaul
[BUNDLE TRUNCATED AT 160000 CHARACTERS — say so in the answer and do not infer omitted content]
