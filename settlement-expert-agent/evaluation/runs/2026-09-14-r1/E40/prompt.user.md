QUESTION FROM THE USER:
Give me the RNI G50 message layout used to send X-TRM instructions to Monte Titoli.

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:52:45.913345+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_message_layout"}
STATUS: blocked — Standard for X-TRM Users (A2A MT / RNI, VER.01.09) is client-only in MT-X; only the published field correspondence table is admitted.
GAP IDS: ['G03']

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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_service_access"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "milan_xtrm_standard_versions"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-xtrm-standard-versions]] — Standard for XTRM Users (A2A and RNI): VER.01.09 under review in April 2026 and the 11 September 2026 update for Vorvel, Certificates TLX and IPO markets (reviewed 2026-09-14; modes ['reference', 'future']; entities ['Milan']; basis reference_description)
CITATION: ON_11/2026 Update Standards for XTRM Users in A2A and RNI mode (10 April 2026) | ON_11/2026 PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_Unfreeze%20ISO%2020022_Clearing%20Migration_ENG_v4_0.pdf
CITATION: Update Standard for XTRM Users for Vorvel, Certificates TLX and IPO markets | ON_36/2026 PDF 1 | version ON_36/2026, 11 September 2026 | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/MKT_ON%20pubblicazione%20SPU%20v.%201.0_ENG.pdf?VersionId=iyNI_tyfEEJGTrLzby2A1xml68X1iSR_ 
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Identifies document titles, versions and MT-X folders only; the standards' content is client-only (gap G03).
LIMITATION: ON_36/2026 planned changes take effect 30 November 2026 subject to testing.
EXCERPT (ON_11/2026 PDF 1–2):
[PDF page 1]

10 April 2026
ON_11/2026




Unfreeze ISO20022 and
Clearing Bond and Repo
Migration projects: update
Standards for XTRM Users in
A2A and RNI Mode.
   To the attention of:                            All Participants


   Priority:                                       Medium


   Topic:                                          Update Standards for XTRM Users in A2A and
                                                   RNI Mode


Dear Client,


We are pleased to inform you that, as anticipated in the PTPC meeting of Euronext Clearing
for Clearing Bond and Repo Migration project, and in the PTPC meeting of Euronext
Securities for Unfreeze ISO20022 project, it has become necessary to update the
"Standards for XTRM Users in A2A and RNI Mode" documentation.

The relevant technical documentation, both in Italian and English, in track changes mode, is
available in the MT-X in the folder:


This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 2

                                                             PRIVATE



[PDF page 2]

       -    "Docs > Live Services > Technical Documentation > Under Review > Clearing
            Bond and Repo Migration
        - “Docs > Live Services > Technical Documentation > Under Review > Unfreeze
            ISO 20022"
Specifically, the documents updated are as follows:

• ES-MIL-A2A X-TRM Standard per utente X-TRM modalità MT A2A VER.01.09 ENG (TC

• ES-MIL-A2A X-TRM Standard per utente X-TRM modalità MT A2A VER.01.09 ITA (TC);

 • ES-MIL-RNI X-TRM Standard per utente X-TRM modalità RNI VER.01.09 ITA (TC).




For any clarification requests, please refer to the following address: MT-T2S-
TEST@euronext.com




| 2 of 2


                                          PRIVATE
EXCERPT (ON_36/2026 PDF 1):
[PDF page 1]

11 September 2026
ON_36/2026

Update Standard for XTRM
Users for Vorvel, Certificates
TLX and IPO markets


  To the attention of:          All Participants


   Priority:              Low


  Topic:                 Update Standard for XTRM Users for Vorvel,
                              Certificates TLX and IPO markets

Dear Client,

to ensure continued support for trading activities, starting from 30 November 2026,
subject to successful testing, new sources and market identifiers will be released.

The updates are shown in track changes in the document “Standard for Users X-
TRM A2A and RNI mode”.

The relevant technical documentation, both in Italian and English is available on
MT-X Platform in the folder: “Documentation – Live Services – Technical
Documentation – Under review – Market Request”.

For any clarification requests, please refer to the following address:


  MT-helpdesk.settlement@euronext.com





This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damages of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
 shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary
 rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.

| 1 of 1


                                           PRIVATE

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