QUESTION FROM THE USER:
Write a technical specification for our indirectly connected (ICP) link to Monte Titoli via X-TRM for an OTC DvP instruction: which fields we must send, how they map to T2S fields, which access channels exist, and which statuses or notifications we receive back.

The user asks for a specification: use SPECIFICATION-TEMPLATE.md headings and expose every missing production field explicitly.

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:01:06.573671+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "settlement_access"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-access]] — Published securities-account, cash-agent and DCP access requirements (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 60–61; PDF 44–45, printed 43–44 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails. Complete CLIMP onboarding, entitlements and accepted tests remain unverified.
EXCERPT (Articles 60–61; PDF 44–45, printed 43–44):
Article 60 – Prerequisites for access to the Settlement Service

   1. In order to participate in the Settlement Service, the participants must
      continuously:
      a) have a securities account at Monte Titoli;
      b) for cash settlement, have accounts dedicated to the processing in T2S,
         or use an agent bank;
       c) in order to send Settlement Instructions to the Settlement Service, make
        use of the X-TRM Service or other direct connection systems to the T2S
         platform that are adequate, compatible and suitable for interacting with
         the Settlement Service and use the specific technical protocols and
         standards   for  sending  communications   relating  to  Settlement
          Instructions. To check this requirement, Participants shall carry out the
          tests arranged by or required by Monte Titoli and notify it of the results.
   2. DCP Participants must also:
      a) equip themselves with business continuity plans, which provide for
           specific measures similar to those specified in the current regulations for
            critical processes, aimed at limiting interruptions to the Settlement
         Service in the event of unavailability of their own connection systems
        and shall inform Monte Titoli of this;
      b) stipulate a  specific agreement  with one  of  the Network  Service
          Providers4 indicated by the ECB;
       c) send Monte Titoli the certification of conformity released by the ECB



4 T2S Framework agreement Schedule 1 «Network service provider»: means a network service provider (NSP) that has
concluded a Licence Agreement with the Eurosystem to provide Connectivity Services to T2S. It is a business or organisation
providing the technical infrastructure, including hardware and software, to establish a secure and encrypted network connection
that permits the exchange of information between T2S Actors and T2S.



43    In force as of 26 January 2026



[PDF page 45]

                                                            SERVICE REGULATIONS


         which certifies the suitability of their connection system, where required;
      d) provide the name of the person in charge of and responsible for the
         connection to the T2S platform;
   3. Participants using an agent bank for cash settlement must, in the event of
      withdrawal from the agreement with the Agent Bank, of the exclusion or
      suspension of the latter from the TARGET2 system, arrange for prompt
       substitution, advising Monte Titoli of this in a timely manner.

Article 61– Requirements for participation for DCP Participants

 1.   The systems connected  directly  to the T2S  platform, used by DCP
       Participants, shall ensure:
      a) the  integrity, accuracy and completeness  of data concerning the
         Settlement Instructions, adopting appropriate technical measures;
      b) the  adoption  of  technical measures  for  information  security and
         processing continuity;
       c) that the  individual Settlement Instructions sent to the Settlement
         Service are identified in such a way as to allow their univocal nature and
          correct order to be checked;
      d) the use of authentication procedures by means of Settlement Instruction
         check digits that guarantee the correct origin and the integrity of the
         data received;
 2.   Participants authorised by Monte Titoli to act as DCPs, shall allow Monte
        Titoli, or its representatives, to perform in-house checks on the adequacy,
       suitability and compatibility of the system of connection and interaction with
     T2S and the requirements of the Regulations. The DCP Participant must
     have at  its office adequate documentation regarding the architecture,
       functionality, operating procedures and service levels.
 3.   Monte Titoli reserves the right to limit the number of DCP Participants that
     a DCP Participant can connect to T2S in the event of (i) persistent technical
      problems affecting a significant number of Participants and/or if (ii) the DCP
       Participant  is unable to modify their systems in order to make them
      compatible with updates made by T2S.
 4.   The DCP Participant may use connection systems developed on its behalf
     by third-party suppliers or connection systems of other DCP Participants. In
      such cases the DCP Participant concerned must notify Monte Titoli and shall
      allow Monte Titoli to perform the in-house verification of the adequacy of
      the technological infrastructure also at the premises of the parties it relies
      on. The DCP Participant must maintain adequate documentation regarding
      the  architecture,  functionality,  operating  procedures,  service  levels,
       controls and contractual guarantees for the activities performed by third
       parties, including other DCP Participants.

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_service_access"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_field_mapping"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_lifecycle_maintenance"}
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

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_connectivity_and_static_data"}
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

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_status_model"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-status-management]] — Status management: statuses, reason codes and communication principles (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.3.1.1–1.6.3.1.3 and the list of Settlement Instruction statuses; PDF 653–656 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Status transition diagrams and the reason-code catalogue are not admitted.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.3.1.1–1.6.3.1.3 and the list of Settlement Instruction statuses; PDF 653–656):
1.6.3 Information Management


18    1.6.3.1 Status Management


19    1.6.3.1.1 Concept

20   T2S informs T2S Actors of the results of the processing of Settlement Instructions, Settlement Restrictions,
21    Maintenance Instructions, Liquidity transfers and Reference Data updates. This information is provided to
22   T2S Actors through a status reporting which is managed by the Status Management process. The communi-
23    cation of statuses to T2S Actors is complemented by the communication of reason codes in case of negative
24    result of a T2S process.


25    1.6.3.1.2 Overview

26   The Status Management process manages the status updates of Settlement Instructions, Settlement Re-
27     strictions, Maintenance Instructions and Liquidity Transfers existing in T2S in order to communicate these


                                                                                            Page 653 of 2017



[PDF page 654]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    status updates through Status Advice messages to the T2S Actors throughout the lifecycle of the instruction.
 2    This process manages as well the status updates related to the processing of incoming reference data
 3    maintenance instructions. The Status Management process also manages the reason codes to be sent to T2S
 4    Actors in case of negative result of a T2S process (e.g. to determine the reason why an instruction is unsuc-
 5    cessfully validated, executed or settled).

 6   The status of an instruction is indicated through a value, which is subject to change through the lifecycle of
 7    the instruction. This value provides T2S Actors with information about the situation of this instruction with
 8    respect to a given T2S process at a certain point in time. For instance, the Settlement Status’ value of a
 9    Settlement Instruction provide T2S Actors with information on whether the Settlement Instruction is unset-
10     tled, partially or fully settled.

11    Since each instruction in T2S can be submitted to several processes, each instruction in T2S has several
12    statuses. For instance, since a Settlement Instruction can be submitted to matching and settlement, this
13    Settlement Instruction has both a Match status and a Settlement status. However, each of these statuses
14    has one single value at a certain moment in time that indicates the instruction’s situation at the considered
15   moment (e.g. Match Status “Unmatched” and Settlement Status “Unsettled”). Depending on its instruction
16    type, i.e. Settlement Instruction, Settlement Restriction or Maintenance Instruction, an instruction is submit-
17    ted to different processes in T2S. Consequently, the statuses featuring each instruction depend on the con-
18    sidered instruction type.

19    In a similar way, reference data maintenance instructions can undergo different types of processing, de-
20    pending on the given type of reference data object to be updated and the current phase of the settlement
21    day. For example, T2S can process and complete immediately a reference data update of a party address
22    submitted during a night-time settlement sequence, because this update cannot have an impact on the on-
23    going settlement process. Contrariwise, T2S can start processing but cannot complete immediately a refer-
24   ence data update aimed at blocking a T2S dedicated cash account and attempted during a night-time set-
25    tlement sequence, as this would imply an impact on the ongoing settlement process. In both cases, the Sta-
26    tus Management process provides the relevant T2S Actor with all the status updates conveyed via specific
27    Status Advice Messages throughout the lifecycle of the given reference data object.

28   The following sections provide:

29         l  The generic principles for the communication of statuses and reason codes to T2S Actors;

30         l  The list of statuses featuring each instruction type as well as the possible values for each of these sta-
31        tuses

32         l An overview of the reason codes management;

33   However, reason codes are not exhaustively detailed below but are provided in section T2S proprietary
34    codes.

35    For a detailed description of the possible status values and status transitions related to reference data up-
36    dates, please refer to section Reference data status management.


37    1.6.3.1.3 Status management process

38   CommunicationofStatusesandReasonCodestoT2SActors


                                                                                            Page 654 of 2017



[PDF page 655]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   T2S informs the T2S Actor through the sending of status advice messages if:

 2         l  There is change in a status value of an instruction in T2S;

 3         l  There is no change in a status value of an instruction in T2S but there is a change in the reason code or
 4         in the business rule associated to the status value 332.

 5    Every time a status update occurs and its value is changed, the Status Management process informs the T2S
 6    Actors of the status change through the sending of Status Advice messages 333 (according to their message
 7    subscription configuration). Additionally, T2S can inform through a single Status Advice message about mul-
 8     tiple status values depending on the lifecycle of the instruction. (e.g. at the acceptance of the instruction,
 9    the “accepted” status will be reported together with any other relevant status applicable to the instruction at
10    the moment of its creation in T2S as for instance “matched” or “Party Hold”).

11     If the instruction is matched, T2S also informs the counterpart of the instruction on the status updates with
12    the exception of the status changes related to any of the Hold statuses (which are communicated to the
13    counterparty on the Intended Settlement Day).

14   The updated statuses can be classified into two different types, common to all type of instructions:

15         l  “Intermediate Status”. There is a change occurred in any of the statuses of the instruction, but it does
16       not imply the end of the processing of the instruction in T2S (e.g. Match Status “Matched”). Further sta-
17        tus updates are to be communicated to the T2S Actor until an “end status” is sent.

18         l  “End status”. This is the last status of an instruction (i.e. the status that an instruction has when pro-
19        cessing for that instruction ends). If the status of an instruction is not of an "end status" type, then the
20        instruction is still under process in T2S. At a point in time, any instruction in T2S reaches a "end status",
21       as any instruction is settled, executed, cancelled or denied in the end.

22    During the whole day the communication to the T2S Actors is sent in real time, if the T2S Actor has not opt-
23   ed for the optional file bundling. In case the T2S Actors are using the optional file bundling T2S sends all
24   messages bundled into files considering the elapse time or maximum number of messages. There are two
25    exceptions during the business day: the maintenance window and the period close to the DVP cut off. Dur-
26    ing this time the optional file bundling is deactivated and messages are sent in real time. During the Night-
27    time period, T2S only sends settlement related messages (e.g. settlement confirmations and settlement
28     failure notifications) bundled into one or more files depending on the size (maximum volume of 32 MB). At
29    the end of every Night-time sequence, T2S sends the latest valid statuses values together with the associat-
30   ed reason codes to the T2S Actors. T2S sends messages to T2S Actors in a consistent order.

31   T2S Actors can query, at any point in time, the status values and reason codes of their instructions.

32   The potential T2S Actors that may receive the messages from T2S are known as Interested Parties. All the
33    possible Interested Parties of messages sent by T2S may choose those messages they want to receive by

     _________________________


        332   Whenever the ISO Code to be reported is a PRCY, if there is no change in the reason code but there is a change in the business rule (compared
                with the previous communication sent to the relevant T2S Actor), T2S won´t send the corresponding Status Advice (i.e. if the previous reason code
                reported to the user was a PRCY, T2S won´t send the Status Advice no matter if the business rule applicable is the same or not).

        333   The only exception is the communication of the Match Status “Matched” for Cancellation Instructions, where T2S only informs on the execution of
               both matched Cancellation Instructions and on the Cancellation of the referenced Settlement Instructions but not on the update of the Match
                 status of the Cancellation Instruction.


                                                                                            Page 655 of 2017



[PDF page 656]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    configuring the Message Subscription service according to their preferences (see section Message subscrip-
 2    tion [ 135]).

 3   StatusesandstatusvaluesinT2S

 4   As previously mentioned, the statuses of an instruction depend on the considered instruction type. The fol-
 5    lowing paragraphs provide the list of statuses of Settlement Instructions, Settlement Restrictions and
 6    Maintenance Instructions. The possible values of each of these statuses are depicted in the diagrams below.
 7    For each of the three instruction types, a status transition diagram is provided to illustrate the corresponding
 8    status updates T2S communicates to the T2S Actors.

 9   SettlementInstructionstatusesandstatusesvalues

10    According to the multiple-status principle adopted for instructions’ statuses, Settlement Instructions are fea-
11    tured by the following statuses:

12         l  Settlement Status;

13         l  Match Status;

14         l  Cancellation Status;

15         l CSD Hold Status;

16         l  Party Hold Status;

17         l CSD Validation Hold Status;

18         l CoSD Hold Status.

19   The possible values of each of these statuses are depicted in the status diagrams and tables below. The
20    Settlement Instruction status transition diagram complements these individual status diagrams with an over-
21    view of the possible status updates that can be communicated to T2S Actors for a Settlement Instruction.

22    Settlement Status

23    Indicates the Settlement Status of the Settlement Instruction. Each status value reflects in which step of the
24    settlement process a Settlement Instruction can be.





                                                                                            Page 656 of 2017

=== RETRIEVAL 7: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "production_xtrm_fields"}
STATUS: blocked — Current production X-TRM standard and service entitlements required; future notice is not a payload specification.
GAP IDS: ['G03']