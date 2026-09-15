QUESTION FROM THE USER:
The R2026.NOV UDFS has now been published. Should our November project assume the new matching rules are live from today, and did the matching section change?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:56:42.525861+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "release_status", "release": "R2026.NOV"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[november-final-release]] — November final publication confirmed on 14 September; deployment unverified (reviewed 2026-09-14; modes ['reference', 'future']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: Cover Note | PDF page 1: final-publication statement, dated 14 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf?1d8ee68f0593cb88571835efb7cd5ed8
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) | PDF page 1: document identity/date, 11 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: Final publication is established; November production deployment is not verified.
LIMITATION: The 14 September cover/listing, 11 September UDFS date and earlier target are separate facts.
LIMITATION: Only cover-page statements are admitted. No November operational provisions, payloads or changed message versions are admitted.
EXCERPT (PDF page 1: final-publication statement, dated 14 September 2026):
[PDF page 1]
              
                 
 
 
 
 
ECB-PUBLIC 
 
14 September 2026 
 
Delivery of the T2S UDFS R2026.NOV and UHB R2026.NOV 
As envisaged in the T2S Plan, we have published final versions of the: 
• 
T2S User Detailed Functional Specifications R2026.NOV (UDFS R2026.NOV) 
• 
T2S User Handbook R2026.NOV (UHB R2026.NOV) 
• 
T2S General Functional Specifications R2026.NOV (GFS R2026.NOV) 
• 
T2S Data Migration Tool R2026.NOV (DMT R2026.NOV) 
• 
T2S User Requirements Document R2026.NOV (URD R2026.NOV) 
• 
T2S Business Functionality for T2S Graphical User Interface R2026.NOV (BFD R2026.NOV) 
• 
BDM User Detailed Functional Specifications R2026.NOV 
• 
BILL User Detailed Functional Specifications R2026.NOV 
• 
CRDM User Detailed Functional Specifications R2026.NOV 
• 
ESMIG User Detailed Functional Specifications R2026.NOV 
• 
BDM User Handbook R2026.NOV 
• 
BILL User Handbook R2026.NOV 
• 
CRDM User Handbook Book 1 R2026.NOV 
• 
CRDM User Handbook Book 2 R2026.NOV 
 
For the convenience of the readers, all changes in the documents were highlighted in revision marks. 
Additionally, we added the appropriate CR references. 
The draft intermediate versions of these documents were published on 31 July and were reviewed from 03 
August 2026 to 21 August 2026. The comments from the market participants have been taken into account for 
the final versions to be published on 11 September 2026. 
Scope of the delivery 
These new versions incorporate Change Requests in the scope of the T2S Release 2026.NOV, including the 
editorial Change Requests approved by the CSD Steering Group (CSG) until 23 July 2026.  
The exhaustive list of all Change Requests is provided as Annex A to this cover note.  
Complementing the information provided in the Service Transition Plans, the Release Notes and the UDFS 
itself, a list containing all the T2S messages with their respective links to MyStandards is provided as Annex 
B to the Cover Note.
EXCERPT (PDF page 1: document identity/date, 11 September 2026):
[PDF page 1]
Author
Version
Identifier
Date
4CB
R2026.NOV
T2S UDFS
11 September 2026
User Detailed Functional Specifications

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "future", "question_type": "release_status", "release": "R2026.NOV"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[november-final-release]] — November final publication confirmed on 14 September; deployment unverified (reviewed 2026-09-14; modes ['reference', 'future']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: Cover Note | PDF page 1: final-publication statement, dated 14 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf?1d8ee68f0593cb88571835efb7cd5ed8
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) | PDF page 1: document identity/date, 11 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: Final publication is established; November production deployment is not verified.
LIMITATION: The 14 September cover/listing, 11 September UDFS date and earlier target are separate facts.
LIMITATION: Only cover-page statements are admitted. No November operational provisions, payloads or changed message versions are admitted.
EXCERPT (PDF page 1: final-publication statement, dated 14 September 2026):
[PDF page 1]
              
                 
 
 
 
 
ECB-PUBLIC 
 
14 September 2026 
 
Delivery of the T2S UDFS R2026.NOV and UHB R2026.NOV 
As envisaged in the T2S Plan, we have published final versions of the: 
• 
T2S User Detailed Functional Specifications R2026.NOV (UDFS R2026.NOV) 
• 
T2S User Handbook R2026.NOV (UHB R2026.NOV) 
• 
T2S General Functional Specifications R2026.NOV (GFS R2026.NOV) 
• 
T2S Data Migration Tool R2026.NOV (DMT R2026.NOV) 
• 
T2S User Requirements Document R2026.NOV (URD R2026.NOV) 
• 
T2S Business Functionality for T2S Graphical User Interface R2026.NOV (BFD R2026.NOV) 
• 
BDM User Detailed Functional Specifications R2026.NOV 
• 
BILL User Detailed Functional Specifications R2026.NOV 
• 
CRDM User Detailed Functional Specifications R2026.NOV 
• 
ESMIG User Detailed Functional Specifications R2026.NOV 
• 
BDM User Handbook R2026.NOV 
• 
BILL User Handbook R2026.NOV 
• 
CRDM User Handbook Book 1 R2026.NOV 
• 
CRDM User Handbook Book 2 R2026.NOV 
 
For the convenience of the readers, all changes in the documents were highlighted in revision marks. 
Additionally, we added the appropriate CR references. 
The draft intermediate versions of these documents were published on 31 July and were reviewed from 03 
August 2026 to 21 August 2026. The comments from the market participants have been taken into account for 
the final versions to be published on 11 September 2026. 
Scope of the delivery 
These new versions incorporate Change Requests in the scope of the T2S Release 2026.NOV, including the 
editorial Change Requests approved by the CSD Steering Group (CSG) until 23 July 2026.  
The exhaustive list of all Change Requests is provided as Annex A to this cover note.  
Complementing the information provided in the Service Transition Plans, the Release Notes and the UDFS 
itself, a list containing all the T2S messages with their respective links to MyStandards is provided as Annex 
B to the Cover Note.
EXCERPT (PDF page 1: document identity/date, 11 September 2026):
[PDF page 1]
Author
Version
Identifier
Date
4CB
R2026.NOV
T2S UDFS
11 September 2026
User Detailed Functional Specifications

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "november_matching_text", "release": "R2026.NOV"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[november-matching-text]] — R2026.NOV UDFS matching section (published future release text) (reviewed 2026-09-14; modes ['future', 'reference']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) — full-text derivative | §3.6.1.2; PDF 279–283 of the R2026.NOV clean UDFS | version R2026.NOV final publication (11 September 2026); deployment not verified | body language en | authoritative language en | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: R2026.NOV is a published future release: Milan's notices plan production deployment on 14 November effective 16 November 2026; deployment is not verified.
LIMITATION: Only the listed pages are admitted; the release's change requests and other sections are unreviewed.
EXCERPT (§3.6.1.2; PDF 279–283 of the R2026.NOV clean UDFS):
3.6.1.2 Matching

3.6.1.2.1 Concept


T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in a
standardised way, according to the T2S rules, which are compliant with the European Central Securities
Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.




Figure 54: Matching application pocess


3.6.1.2.2 Overview


T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
(i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
presented in section Instruction Cancellation).


All rights reserved.                     T2S UDFS - R2026.NOV - Clean                          Page 279 of 2349



[PDF page 280]

                                                                                         General Features of T2S
                                                                                Application Processes Description


T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD.
Instructions that enter into T2S as already matched are created with the matching fields as if they were
matched in T2S (i.e. follow the same matching rules as in T2S).


3.6.1.2.3 Matching process


When a new instruction enters T2S, the matching process compares[1] each of the Mandatory and Non-
mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain
unmatched in T2S:

I Mandatory matching fields are those fields that must be present in the instruction and which values
   should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
   tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliver/
   Receiver (DELI/RECE), whose values match opposite.
I Non-mandatory matching fields can be Additional or Optional:
  – Additional matching fields are initially not mandatory but their values have to match when one of the
       counterparties provides a value for them in its instruction. Consequently, once an Additional matching
       field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in
       Additional matching field cannot match with a field with no value.
  – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike
       Additional matching fields), but when both Parties provide a value, the values have to match.

Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
below. The following tables and illustrations provide examples of the use of the mandatory, optional and
additional fields in the matching process.

Exhaustive List of Matching Fields




Figure 55: Mandatory Matching Fields per Transaction Type and Example




All rights reserved.                       T2S UDFS - R2026.NOV - Clean                        Page 280 of 2349



[PDF page 281]

                                                                                        General Features of T2S
                                                                               Application Processes Description


Non Mandatory Matching Fields per Transaction Type




Figure 56: Additional Matching Fields and Example


Non Mandatory Matching Fields per Transaction Type




Figure 57: Optional Matching Fields and Example


If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
value. ECSDA proposal for Euro is the following:




All rights reserved.                        T2S UDFS - R2026.NOV - Clean                      Page 281 of 2349



[PDF page 282]

                                                                                                                       General Features of T2S
                                                                                                           Application Processes Description


              Countervalue for the cash amount                                                             Tolerance

                            ≤ EUR 100.000                                                                    EUR 2


                            > EUR 100.000                                                                    EUR 25

Table 57: Tolerance amount for matching for Euro


In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruction
with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Settlement
Instructions with different Settlement Amount are matched, the amount that T2S submits for settlement as
Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securities.

After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference
assigned to both Settlement Instructions that have been matched by T2S and the T2S Reference and
Account Owner Reference of the counterparty´s instruction. Interested parties can also be informed
depending on their message subscription preferences (see Section Status Management and section
Message subscription).

In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Allegement
message (after having waited a certain period of time) to the Counterparty informing that there is a
Settlement Instruction alleged against it. The Allegement process is described below (See section
Allegement), the dialogue is reflected in section Send Settlement Instruction.

T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
section Instruction Cancellation and section Instructions Recycling).


Footnotes

1     Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given
      matching field is filled in two different instructions with the same reference but a different combination of upper and lower case letters, this
      matching field is not subject to matching.




All rights reserved.                                 T2S UDFS - R2026.NOV - Clean                                               Page 282 of 2349



[PDF page 283]

                                                                                              General Features of T2S
                                                                                  Application Processes Description


3.6.1.2.4 Parameter Synthesis


No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S
Operator.

  Concerned                                                      Mandatory/     Possible        Standard or default
                       Parameter   Created by     Updated by
   process                                                        Optional       values               value

   Matching            Tolerance   T2S Operator   T2S Operator       M        To be defined       ≤100.000 € = 2€
                        amount                                                                   >100.000 € = 25€

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "november_text_comparison"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[november-text-comparison]] — June versus November UDFS: normalised sentence comparison of selected settlement sections (reviewed 2026-09-14; modes ['reference', 'future']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) — full-text derivative | Derived comparison of the June and November clean UDFS texts (method and limits inside) | version R2026.NOV final publication (11 September 2026); deployment not verified | body language en | authoritative language en | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: A derivative produced by the library maintainer, not ECB text: textual comparison after normalisation; diagrams and image tables are not compared; residual differences listed are formatting artefacts unless stated otherwise.
LIMITATION: No sentence-level substantive change was detected in the compared ranges (matching, allegement, amendment, cancellation, hold/release, recycling, posting overview, partial settlement, realignment concept, linked, CoSD, status management, schedule, RTS phase, validation, NTS processing). The realignment sentence flagged by the diff exists in both texts with a line-break difference.
LIMITATION: The comparison does not review the change requests actually delivered by R2026.NOV; Milan lists 11 change requests and six defects in ON_28/2026.
EXCERPT (Derived comparison of the June and November clean UDFS texts (method and limits inside)):
[
  {
    "section": "matching",
    "june": {
      "heading": "1.6.1.2 Matching",
      "pdf_pages": [
        267,
        272
      ],
      "sentences": 38
    },
    "november": {
      "heading": "3.6.1.2 Matching",
      "pdf_pages": [
        279,
        284
      ],
      "sentences": 39
    },
    "similarity_ratio": 0.8987,
    "residual_differences": [
      "-193 the under insolvency situation will be activated upon request of a csd or cb as explained in the manual of operational procedures (mop).",
      "-diagram 54 - matching application pocess 2 overview t2s provides t2s actors matching services for settlement instructions that require to be matched in t2s (i.e.",
      "+figure 54:",
      "+matching application pocess overview t2s provides t2s actors matching services for settlement instructions that require to be matched in t2s (i.e.",
      "-the matching of cancellation instructions does not follow the rules presented in this section and is presented in section instruction cancellation  280).",
      "+the matching of cancellation instructions does not follow the rules presented in this section and is presented in section instruction cancellation).",
      "-mandatory matching fields are those fields that must be present in the instruction and which values should be the same in both settlement instructions except settlement amount for dvp/pfod for which a tolerance might be applied and for credit/debit code (crdt/dbit) and securities movement type deliver/receiver (deli/rece), whose values match opposite.",
      "+mandatory matching fields are those fields that must be present in the instruction and which values should be the same in both settlement instructions except settlement amount for dvp/pfod for which a tolerance might be applied and for credit/debit code (crdt/dbit) and securities movement type deliver/ receiver (deli/rece), whose values match opposite.",
      "-mandatory matching fields per transaction type and example 21 194 upper and lower case letters are considered as different when comparing the values of two different instructions.",
      "-in case a given matching field is filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not subject to matching.",
      "-non mandatory matching fields per transaction type figure 56:",
      "-additional matching fields and example 3 non mandatory matching fields per transaction type figure 57:",
      "-optional matching fields and example 6 if all the matching fields on both instructions match, except for the settlement amount, t2s checks if the difference between both settlement amounts is compliant with the tolerance amount configured in t2s.",
      "+mandatory matching fields per transaction type and example non mandatory matching fields per transaction type figure 56:",
      "+additional matching fields and example non mandatory matching fields per transaction type figure 57:",
      "+optional matching fields and example if all the matching fields on both instructions match, except for the settlement amount, t2s checks if the difference between both settlement amounts is compliant with the tolerance amount configured in t2s.",
      "-table 57 - tolerance amount for matching for euro 2 countervalue for the cash amount tolerance  eur eur 2  eur eur 25 in case there is more than one potentially matching settlement instruction, t2s chooses the one having the smallest settlement amount difference.",
      "+countervalue for the cash amount tolerance  eur eur 2  eur eur 25 table 57:",
      "+tolerance amount for matching for euro in case there is more than one potentially matching settlement instruction, t2s chooses the one having the smallest settlement amount difference.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "-the allegement process is described below (see section allegement  271), the dialogue is reflected in section send settlement instruction.",
      "-t2s automatically cancels settlement instructions that remain unmatched after a certain period of time (see section instruction cancellation  280 and section instructions recycling  296).",
      "-21 parameter synthesis no specific configuration from t2s actor is needed.",
      "+the allegement process is described below (see section allegement), the dialogue is reflected in section send settlement instruction.",
      "+t2s automatically cancels settlement instructions that remain unmatched after a certain period of time (see section instruction cancellation and section instructions recycling).",
      "+footnotes 1 upper and lower case letters are considered as different when comparing the values of two different instructions.",
      "+in case a given matching field is filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not subject to matching.",
      "+parameter synthesis no specific configuration from t2s actor is needed.",
      "-25 concerned parameter created by updated by mandatory/ possible standard or de- process optional values fault value matching tolerance t2s operator t2s operator m to be defined 100.000 €  2€ amount 100.000 €  25€",
      "+concerned mandatory/ possible standard or default parameter created by updated by process optional values value matching tolerance t2s operator t2s operator m to be defined 100.000 €  2€ amount 100.000 €  25€"
    ],
    "verdict": "31 residual sentence differences (inspect below)"
  },
  {
    "section": "allegement",
    "june": {
      "heading": "1.6.1.3 Allegement",
      "pdf_pages": [
        271,
        278
      ],
      "sentences": 45
    },
    "november": {
      "heading": "3.6.1.3 Allegement",
      "pdf_pages": [
        283,
        290
      ],
      "sentences": 50
    },
    "similarity_ratio": 0.9294,
    "residual_differences": [
      "-diagram 58 - allegement application process 5 overview t2s applies the allegement process for unmatched settlement instructions and unmatched cancellation instructions that require matching.",
      "+figure 58:",
      "+allegement application process overview t2s applies the allegement process for unmatched settlement instructions and unmatched cancellation instructions that require matching.",
      "-diagram 59 - allegement process 2 allegement process settlementallegement if a settlement instruction does not match after the first matching attempt (see section matching  267), the counterparty is informed through an allegement message after a predefined period of time (standard delay period, that is configured in t2s reference data by the t2s operator).",
      "+figure 59:",
      "+allegement process allegement process settlement allegement if a settlement instruction does not match after the first matching attempt (see section matching), the counterparty is informed through an allegement message after a predefined period of time (standard delay period, that is configured in t2s reference data by the t2s operator).",
      "-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section message subscription).",
      "-diagram 60 - scenario a:",
      "-standard delay period 2 scenario b:",
      "+figure 60:",
      "+scenario a:",
      "+standard delay period scenario b:",
      "-diagram 61 - scenario b:",
      "-standard delay period exceeds isd cut off 2 cancellationofanallegementmessage if an unmatched settlement instruction is cancelled by the t2s actor, the counterparty receives a cancellation of the allegement message automatically generated by t2s.",
      "+figure 61:",
      "+scenario b:",
      "+standard delay period exceeds isd cut off cancellation of an allegement message if an unmatched settlement instruction is cancelled by the t2s actor, the counterparty receives a cancellation of the allegement message automatically generated by t2s.",
      "-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section message subscription).",
      "-scenario a for sending a cancellation of the allegement message 9 if an unmatched settlement instruction is automatically cancelled by t2s (cancellation by the system), the counterparty receives a cancellation of the allegement message automatically generated by t2s.",
      "-the cases that may trigger cancellation by the system of an unmatched settlement instruction as described in section instruction cancellation  280 are the following:",
      "+scenario a for sending a cancellation of the allegement message if an unmatched settlement instruction is automatically cancelled by t2s (cancellation by the system), the counterparty receives a cancellation of the allegement message automatically generated by t2s.",
      "+the cases that may trigger cancellation by the system of an unmatched settlement instruction as described in section instruction cancellation are the following:",
      "-scenario b for sending a cancellation of the allegement message 4 removalofanallegementmessage in case the counterparty sends its corresponding settlement instruction to t2s, and if both instructions are matched, the counterparty receives a removal of allegement message, since the previously sent allegement is no longer valid.",
      "+scenario b for sending a cancellation of the allegement message removal of an allegement message in case the counterparty sends its corresponding settlement instruction to t2s, and if both instructions are matched, the counterparty receives a removal of allegement message, since the previously sent allegement is no longer valid.",
      "-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section message subscription).",
      "-scenario for sending a removal of the allegement message 12 cancellationallegement if a t2s actor sends a cancellation instruction that requires the cancellation of both legs of a settlement instruction and the counterparty has not sent its cancellation instruction, t2s sends a status advice message to the t2s actor (with no delay period) informing that its cancellation is pending and another one to the counterparty informing that its cancellation instruction is requested.",
      "+scenario for sending a removal of the allegement message cancellation allegement if a t2s actor sends a cancellation instruction that requires the cancellation of both legs of a settlement instruction and the counterparty has not sent its cancellation instruction, t2s sends a status advice message to the t2s actor (with no delay period) informing that its cancellation is pending and another one to the counterparty informing that its cancellation instruction is requested.",
      "-diagram 65 - scenario for sending a cancellation allegement status advice 21 parameters synthesis the following parameters are specified by the t2s operator:",
      "+figure 65:",
      "+scenario for sending a cancellation allegement status advice parameters synthesis the following parameters are specified by the t2s operator:",
      "-11 concerned parameter created by updated by mandatory/ possible val- standard or process optional ues default value settlement standard delay t2s operator t2s operator m to be defined 1 hour allegement period settlement before cut-off t2s operator t2s operator m to be defined 5 hours allegement",
      "+concerned mandatory/ possible standard or parameter created by updated by process optional values default value settlement standard delay t2s operator t2s operator m to be defined 1 hour allegement period settlement before cut-off t2s operator t2s operator m to be defined 5 hours allegement"
    ],
    "verdict": "35 residual sentence differences (inspect below)"
  },
  {
    "section": "amendment",
    "june": {
      "heading": "1.6.1.4 Instruction Amendment",
      "pdf_pages": [
        277,
        281
      ],
      "sentences": 29
    },
    "november": {
      "heading": "3.6.1.4 Instruction Amendment",
      "pdf_pages": [
        289,
        293
      ],
      "sentences": 32
    },
    "similarity_ratio": 0.7465,
    "residual_differences": [
      "-diagram 66 - instruction amendment application process 2 overview t2s accepts and processes an amendment instruction sent by a t2s actor when it successfully passes the business validation process (see section business validation  218), unless any of the following conditions is fulfilled:",
      "+figure 66:",
      "+instruction amendment application process overview t2s accepts and processes an amendment instruction sent by a t2s actor when it successfully passes the business validation process (see section business validation), unless any of the following conditions is fulfilled:",
      "-the referenced settlement instruction is identified as cosd and the amendment instruction does not aim to remove a linkage having the csd as the instructing party (see section conditional settlement  452);",
      "+the referenced settlement instruction is identified as cosd and the amendment instruction does not aim to remove a linkage having the csd as the instructing party (see section conditional settlement);",
      "-an amendment instruction can be used to amend a process indicator of both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the amendment instruction refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types  86).",
      "-table 58 - references for amendment instruction 6 already matched settlement settlement instructions instruction matched in t2s amendment instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference amendment instruction of both legs of t2s actor reference x the settlement instruction for amendment instructions referring to both legs of the settlement instruction (i.e.",
      "+an amendment instruction can be used to amend a process indicator of both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the amendment instruction refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types).",
      "+already matched settlement settlement instructions matched in instruction t2s amendment instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference amendment instruction of both legs of t2s actor reference x the settlement instruction table 58:",
      "+references for amendment instruction for amendment instructions referring to both legs of the settlement instruction (i.e.",
      "-linkages block (see section linked instructions  442).",
      "+linkages block (see section linked instructions).",
      "-linkages block (see section linked instructions  442).",
      "+linkages block (see section linked instructions).",
      "-table 59 - process indicators allowed for amendment 2 “partial settlement “linkages block” “priority” indicator” settlement instruction yes yes yes settlement restriction no yes yes partially settled instruction no no yes t2s informs the t2s actor on the result of the amendment process through a status advice message, as described in sections send amendment instruction of a settlement instruction or of a settlement restriction on securities position and send amendment instruction of a settlement restriction on cash balance.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+“partial settlement “linkages block” “priority” indicator” settlement instruction yes yes yes “partial settlement “linkages block” “priority” indicator” settlement restriction no yes yes partially settled instruction no no yes table 59:",
      "+process indicators allowed for amendment t2s informs the t2s actor on the result of the amendment process through a status advice message, as described in sections send amendment instruction of a settlement instruction or of a settlement restriction on securities position and send amendment instruction of a settlement restriction on cash balance.",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription)."
    ],
    "verdict": "19 residual sentence differences (inspect below)"
  },
  {
    "section": "cancellation",
    "june": {
      "heading": "1.6.1.5 Instruction Cancellation",
      "pdf_pages": [
        280,
        285
      ],
      "sentences": 45
    },
    "november": {
      "heading": "3.6.1.5 Instruction Cancellation",
      "pdf_pages": [
        292,
        298
      ],
      "sentences": 47
    },
    "similarity_ratio": 0.5031,
    "residual_differences": [
      "-diagram 67 - instruction cancellation application process 2 overview after its validation, t2s processes cancellation instructions sent by a t2s actor to cancel previously sent settlement instructions or settlement restrictions, unless it fulfils any of the following conditions:",
      "+figure 67:",
      "+instruction cancellation application process overview after its validation, t2s processes cancellation instructions sent by a t2s actor to cancel previously sent settlement instructions or settlement restrictions, unless it fulfils any of the following conditions:",
      "-the referenced settlement instruction is identified as cosd, and the instructing party is not the relevant csd or the relevant administering party (see section conditional settlement  452);",
      "+the referenced settlement instruction is identified as cosd, and the instructing party is not the relevant csd or the relevant administering party (see section conditional settlement);",
      "-if the cancellation instruction fulfils any of these conditions, the cancellation instruction is denied and t2s communicates its denial together with the relevant reason code to the t2s actor or any interested party, depending on their message subscription preferences (see section status management  653).",
      "+if the cancellation instruction fulfils any of these conditions, the cancellation instruction is denied and t2s communicates its denial together with the relevant reason code to the t2s actor or any interested party, depending on their message subscription preferences (see section status management).",
      "-cancellation process instructioncancellationprocess t2s actors can send cancellation instructions to cancel previously sent settlement instructions or settlement restrictions.",
      "+cancellation process instruction cancellation process t2s actors can send cancellation instructions to cancel previously sent settlement instructions or settlement restrictions.",
      "-if the referenced settlement instruction is matched, t2s requires bilateral cancellation and the cancellation is only possible if both counterparties send their cancellation instructions to cancel each leg separately or if the cancellation instruction is sent with the information of both legs by an authorised t2s party .",
      "-a cancellation instruction can be used to cancel both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the cancellation request refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types  86).",
      "-195 in case the csd and the party send their respective cancellation instructions for the same leg, and both remain pending in the system awaiting for their counterparty in order to match and be executed, t2s matching process prioritises for the matching the csd cancellation instruction over the party cancellation instruction.",
      "-table 60 - references used in cancellation scenarios 2 already matched settlement settlement instructions instruction matched in t2s cancellation instruction of one leg of t2s reference t2s actor reference the settlement instruction (two cancelor lations needed) t2s reference cancellation instruction of both legs of t2s actor reference x the settlement instruction for cancellation instructions referring to both legs of the settlement instruction (i.e.",
      "+if the referenced settlement instruction is matched, t2s requires bilateral cancellation and the cancellation is only possible if both counterparties send their cancellation instructions to cancel each leg separately or if the cancellation instruction is sent with the information of both legs by an authorised t2s party.",
      "+a cancellation instruction can be used to cancel both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the cancellation request refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types).",
      "+already matched settlement settlement instructions matched in instruction t2s cancellation instruction of one leg of t2s reference t2s actor reference the settlement instruction (two or cancellations needed) t2s reference cancellation instruction of both legs of t2s actor reference x the settlement instruction table 60:",
      "+references used in cancellation scenarios for cancellation instructions referring to both legs of the settlement instruction (i.e.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "-cancellationofcosdprocess when a settlement instruction is identified as cosd, only administering parties or the relevant csd can cancel it under certain circumstances:",
      "+cancellation of cosd process when a settlement instruction is identified as cosd, only administering parties or the relevant csd can cancel it under certain circumstances:",
      "-the administering parties only have to send one cancellation instruction regardless if more than one cosd rule applies) (see section conditional settlement  452), or;",
      "+the administering parties only have to send one cancellation instruction regardless if more than one cosd rule applies) (see section conditional settlement), or;",
      "-cancellationbythesystemprocess t2s automatically cancels pending instructions in the system under the following conditions:",
      "-settlement instructions, settlement restrictions and cancellation instructions once they exceed their recycling period in t2s (see section instructions recycling  296).",
      "-settlement instructions when the realignment chain cannot be built (see section realignment  373).",
      "+cancellation by the system process t2s automatically cancels pending instructions in the system under the following conditions:",
      "+settlement instructions, settlement restrictions and cancellation instructions once they exceed their recycling period in t2s (see section instructions recycling).",
      "+settlement instructions when the realignment chain cannot be built (see section realignment).",
      "-the revalidation process is triggered at the start of day in t2s and by a change in the reference data that affects the instruction (see section business validation  218).",
      "-settlement instructions that during the start of day revalidation process it is detected that the realignment chain used for settlement has become invalid for the current settlement day and while a new valid realignment chain can be built, the transaction is already partially settled (see section realignment  373) pending cancellation instruction in the system when one of the conditions for the denial of a cancellation instruction is fulfilled.",
      "-(see section send cancellation instruction of a settlement instruction or a settlement restriction on securities position and section send cancellation instruction of a settlement restriction on cash balance.) parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.",
      "+the revalidation process is triggered at the start of day in t2s and by a change in the reference data that affects the instruction (see section business validation).",
      "+settlement instructions that during the start of day revalidation process it is detected that the realignment chain used for settlement has become invalid for the current settlement day and while a new valid realignment chain can be built, the transaction is already partially settled (see section realignment) pending cancellation instruction in the system when one of the conditions for the denial of a cancellation instruction is fulfilled.",
      "+(see section send cancellation instruction of a settlement instruction or a settlement restriction on securities position and section send cancellation instruction of a settlement restriction on cash balance.) footnotes 1 in case the csd and the party send their respective cancellation instructions for the same leg, and both remain pending in the system awaiting for their counterparty in order to match and be executed, t2s matching process prioritises for the matching the csd cancellation instruction over the party cancellation instruction.",
      "+parameters synthesis no specific configuration from t2s actor is needed in t2s reference data."
    ],
    "verdict": "36 residual sentence differences (inspect below)"
  },
  {
    "section": "hold_release",
    "june": {
      "heading": "1.6.1.6 Hold and Release",
      "pdf_pages": [
        284,
        297
      ],
      "sentences": 147
    },
    "november": {
      "heading": "3.6.1.6 Hold and Release",
      "pdf_pages": [
        297,
        311
      ],
      "sentences": 156
    },
    "similarity_ratio": 0.8312,
    "residual_differences": [
      "-table 61 - references used for hold/release instruction 2 already matched settlement settlement instructions instruction matched in t2s hold/release instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference hold/release instruction of both legs t2s actor reference x of the settlement instruction for hold/release instructions referring to both legs of the settlement instruction (i.e.",
      "+already matched settlement settlement instructions matched in instruction t2s hold/release instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference hold/release instruction of both legs t2s actor reference x of the settlement instruction table 61:",
      "+references used for hold/release instruction for hold/release instructions referring to both legs of the settlement instruction (i.e.",
      "-additionally, t2s automatically puts a settlement instruction on hold if it fulfils any restriction defined by the csds, known as csd validation hold or party hold (see section business validation  218) or if it is identified as a cosd on the intended settlement date (see section conditional settlement  452).",
      "+additionally, t2s automatically puts a settlement instruction on hold if it fulfils any restriction defined by the csds, known as csd validation hold or party hold (see section business validation) or if it is identified as a cosd on the intended settlement date (see section conditional settlement).",
      "-nevertheless, these instructions can be matched, amended or cancelled (however settlement instructions on cosd hold cannot be amended and can only be cancelled following specific rules - see section instruction cancellation  280).",
      "-diagram 68 - hold and release application process 2 overview the hold/release instruction has two hold indicators that can be filled by the t2s actor:",
      "+nevertheless, these instructions can be matched, amended or cancelled (however settlement instructions on cosd hold cannot be amended and can only be cancelled following specific rules - see section instruction cancellation).",
      "+figure 68:",
      "+hold and release application process overview the hold/release instruction has two hold indicators that can be filled by the t2s actor:",
      "-in case of a settlement instruction put on hold by t2s due to a csd validation hold, it can only be released by the relevant csd that defined the rule (see section business validation  218).",
      "+in case of a settlement instruction put on hold by t2s due to a csd validation hold, it can only be released by the relevant csd that defined the rule (see section business validation).",
      "-(see section conditional settlement  452).",
      "+(see section conditional settlement).",
      "-nevertheless, t2s does not allow t2s actors to put on hold settlement instructions already identified as cosd (see section conditional settlement  452).",
      "+nevertheless, t2s does not allow t2s actors to put on hold settlement instructions already identified as cosd (see section conditional settlement).",
      "-table 62 - hold /release exhaustive scenarios for a settlement instruction 22 settlement instruction party hold csd hold csd validation cosd hold result hold no no no no eligible for settlement yes yes yes yes no settlement attempt can be performed yes yes yes no no settlement attempt can be performed yes yes no no no settlement attempt can be performed party hold indicator can be i) instructed by the t2s actor ii) put automatically by t2s upon the fulfilment of a restriction type case 1 or, iii) put automatically by t2s if it has not been set and the “hold release default” value of the securities account included in the instruction is set to “hold”.",
      "-settlement instruction party hold csd hold csd validation cosd hold result hold yes no no yes no settlement attempt can be performed no no yes yes no settlement attempt can be performed no yes yes yes no settlement attempt can be performed no yes no no no settlement attempt can be performed yes no no no no settlement attempt can be performed no no yes no no settlement attempt can be performed yes no yes no no settlement attempt can be performed no yes yes no no settlement attempt can be performed yes yes no yes no settlement attempt can be performed no yes no yes no settlement attempt can be performed yes no yes yes no settlement attempt can be performed no no no yes no settlement attempt can be performed no party / csd hold is allowed.",
      "-if an instruction remains on hold at the end of its intended settlement date, t2s recycles the instruction following the t2s recycling rules (see section instructions recycling  296).",
      "-197 no settlement attempt can be performed unless the settlement instruction is under partial release process and partial settlement of settlement instructions under partial release process is allowed (i.e.",
      "-real time settlement or sequence x of night time settlement is running) (see section partial settlement  343).",
      "+settlement instruction csd validation party hold csd hold cosd hold result hold 1 no no no no eligible for settlement 2 yes yes yes yes no settlement attempt can be performed 3 yes yes yes no no settlement attempt can be performed 4 yes yes no no no settlement attempt can be performed 5 yes no no yes no settlement attempt can be performed settlement instruction csd validation party hold csd hold cosd hold result hold 6 no no yes yes no settlement attempt can be performed 7 no yes yes yes no settlement attempt can be performed 8 no yes no no no settlement attempt can be performed 9 yes no no no no settlement attempt can be performed no no yes no no settlement attempt can be performed yes no yes no no settlement attempt can be performed no yes yes no no settlement attempt can be performed yes yes no yes no settlement attempt can be performed no yes no yes no settlement attempt can be performed yes no yes yes no settlement attempt can be performed no no no yes no settlement attempt can be performed no party / csd hold is allowed.",
      "+table 62:",
      "+hold /release exhaustive scenarios for a settlement instruction if an instruction remains on hold at the end of its intended settlement date, t2s recycles the instruction following the t2s recycling rules (see section instructions recycling).",
      "+footnotes 1 party hold indicator can be i) instructed by the t2s actor ii) put automatically by t2s upon the fulfilment of a restriction type case 1 or, iii) put automatically by t2s if it has not been set and the “hold release default” value of the securities account included in the instruction is set to “hold”.",
      "+2 no settlement attempt can be performed unless the settlement instruction is under partial release process and partial settlement of settlement instructions under partial release process is allowed (i.e.",
      "+real time settlement or sequence x of night time settlement is running) (see section partial settlement).",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "-example 78 - hold instruction this example illustrates the execution of two different hold instructions for the settlement instruction “x”, which is matched with settlement instruction “y”, before the intended settlement date:",
      "+example 78:",
      "+hold instruction this example illustrates the execution of two different hold instructions for the settlement instruction “x”, which is matched with settlement instruction “y”, before the intended settlement date:",
      "-diagram 69 - both the t2s party and the relevant csd send a hold instruction 2 release process when a t2s actor sends a release instruction, t2s proceeds to execute it, once checked that the referenced instruction is not:",
      "+figure 69:",
      "+both the t2s party and the relevant csd send a hold instruction release process when a t2s actor sends a release instruction, t2s proceeds to execute it, once checked that the referenced instruction is not:",
      "-if t2s successfully executes the release instruction, the t2s actor is informed through a message communicating the execution of the release instruction and a status advice message informing if other hold remains as described in send hold/release instruction.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+if t2s successfully executes the release instruction, the t2s actor is informed through a message communicating the execution of the release instruction and a status advice message informing if other hold remains as described in send hold/release instruction .",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "-example 79 - release instruction continuing with the previous, this one illustrates the case when the t2s party sends its release instruction for settlement instruction “x”, leaving the instruction “x” on csd hold until the release from the csd is received and executed:",
      "+example 79:",
      "+release instruction continuing with the previous, this one illustrates the case when the t2s party sends its release instruction for settlement instruction “x”, leaving the instruction “x” on csd hold until the release from the csd is received and executed:",
      "-then, settlement instruction “x” changes from scenario 4 to scenario 8 in table - hold /release exhaustive scenarios for a settlement instruction  287.",
      "+then, settlement instruction “x” changes from scenario 4 to scenario 8 in hold/release exhaustive scenarios for a settlement instruction.",
      "-the party sends a release instruction 17 the csd sends a release instruction for csd hold, t2s validates successfully the instruction and proceeds to release the referenced settlement instruction putting “no” in its csd hold indicator.",
      "+the party sends a release instruction the csd sends a release instruction for csd hold, t2s validates successfully the instruction and proceeds to release the referenced settlement instruction putting “no” in its csd hold indicator.",
      "-thus, settlement instruction “x” changes from scenario 8 to scenario 1 in table - hold /release exhaustive scenarios for a settlement instruction  287.",
      "-diagram 71 - the t2s party sends a release instruction 6 hold/release default for settlement instructions when a t2s actor sends a settlement instruction, t2s checks if the settlement instruction has the party hold status set (i.e.",
      "+thus, settlement instruction “x” changes from scenario 8 to scenario 1 in hold/release exhaustive scenarios for a settlement instruction.",
      "+figure 71:",
      "+the t2s party sends a release instruction hold/release default for settlement instructions when a t2s actor sends a settlement instruction, t2s checks if the settlement instruction has the party hold status set (i.e.",
      "-in case the party hold status is not set, t2s checks in reference data the “hold release default” value of the securities account included in the instruction 198:",
      "+in case the party hold status is not set, t2s checks in reference data the “hold release default” value of the securities account included in the instruction:",
      "-198 internally generated instructions are not considered for hold/release default.",
      "+footnotes 1 internally generated instructions are not considered for hold/release default.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "-once executed, a partially released settlement instruction will be submitted to a settlement attempt depending on the phase of the day (see section partial settlement  343) if it is executed during the night time settlement, the partially released settlement instruction will only be submitted to a settlement attempt when the corresponding sequence runs.",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "+once executed, a partially released settlement instruction will be submitted to a settlement attempt depending on the phase of the day (see section partial settlement) if it is executed during the night time settlement, the partially released settlement instruction will only be submitted to a settlement attempt when the corresponding sequence runs.",
      "-areleaseinstruction over the referenced instruction is received;",
      "+a release instruction over the referenced instruction is received;",
      "-example 80 - partial release process this example illustrates the execution of a release instruction that aims to partially release settlement instruction “x”, which has its party hold indicator already set to “yes”.",
      "+example 80:",
      "+partial release process this example illustrates the execution of a release instruction that aims to partially release settlement instruction “x”, which has its party hold indicator already set to “yes”.",
      "-the settlement instruction “x” remains in scenario 9 of table - hold /release exhaustive scenarios for a settlement instruction  287 throughout the entire partial release process and also after its ending.",
      "-diagram 72 - the party sends a release instruction to partially release a settlement instruction 21 parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.",
      "+the settlement instruction “x” remains in scenario 9 of hold/release exhaustive scenarios for a settlement instruction throughout the entire partial release process and also after its ending.",
      "+figure 72:",
      "+the party sends a release instruction to partially release a settlement instruction parameters synthesis no specific configuration from t2s actor is needed in t2s reference data."
    ],
    "verdict": "69 residual sentence differences (inspect below)"
  },
  {
    "section": "recycling",
    "june": {
      "heading": "1.6.1.7 Instructions Recycling",
      "pdf_pages": [
        296,
        304
      ],
      "sentences": 48
    },
    "november": {
      "heading": "3.6.1.7 Instructions Recycling",
      "pdf_pages": [
        310,
        318
      ],
      "sentences": 54
    },
    "similarity_ratio": 0.9097,
    "residual_differences": [
      "-instructions recycling concept at each end of a settlement day (see section settlement day  155), t2s recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in t2s, before being cancelled by the system.",
      "-diagram 73 - instruction recycling application process 7 overview the recycling of an instruction in t2s triggers the revalidation process at the start of day, as described in section business validation  218.",
      "+instructions recycling concept at each end of a settlement day (see section settlement day), t2s recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in t2s, before being cancelled by the system.",
      "+figure 73:",
      "+instruction recycling application process overview the recycling of an instruction in t2s triggers the revalidation process at the start of day, as described in section business validation.",
      "-for more information on status changes see section status management  653.",
      "+for more information on status changes see section status management.",
      "-recycling period for unmatched settlement instructions 11 unmatched cancellation instructions that need to be matched in t2s are recycled for a period of working days configured by the t2s operator, starting from its reception in t2s until its matching occurs.",
      "-199 current recycling period for unmatched instructions of working days.",
      "+recycling period for unmatched settlement instructions unmatched cancellation instructions that need to be matched in t2s are recycled for a period of working days configured by the t2s operator, starting from its reception in t2s until its matching occurs.",
      "-recycling period for unmatched cancellation instructions 2 pending matched instructions and settlement restrictions are recycled in t2s for a period of working days configured by the t2s operator until its settlement or cancellation occurs (see section instruction cancellation  280).",
      "+recycling period for unmatched cancellation instructions pending matched instructions and settlement restrictions are recycled in t2s for a period of working days configured by the t2s operator until its settlement or cancellation occurs (see section instruction cancellation).",
      "-12 13 14 200 current recycling period for matched instructions of working days.",
      "-diagram 76 - recycling period for matched instructions 2 t2s does not send a daily message to the t2s actors informing about the result of the recycling process.",
      "+figure 76:",
      "+recycling period for matched instructions t2s does not send a daily message to the t2s actors informing about the result of the recycling process.",
      "-the dialogue is reflected in section send settlement instruction.",
      "-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).",
      "+the dialogue is reflected in section send settlement instruction .",
      "+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).",
      "-diagram 77 - recycling period for unmatched settlement instructions (entry date the same day of isd and without any status update during its lifecycle) 3 a settlement instruction enters in t2s on business day .04.2016 as unmatched and with isd same day (27.04.2016).",
      "+figure 77:",
      "+recycling period for unmatched settlement instructions (entry date the same day of isd and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched and with isd same day (27.04.2016).",
      "-diagram 78 - recycling period for unmatched settlement instructions (isd in the future and without any status update during its lifecycle) 11 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).",
      "+figure 78:",
      "+recycling period for unmatched settlement instructions (isd in the future and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).",
      "-diagram 79 - recycling period for unmatched settlement instructions (isd in the future and a hold status update during its lifecycle) 7 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).",
      "+figure 79:",
      "+recycling period for unmatched settlement instructions (isd in the future and a hold status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).",
      "-diagram 80 - recycling period for unmatched settlement instructions (isd in the past and without any status update during its lifecycle) 3 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the past (26.04.2016).",
      "+figure 80:",
      "+recycling period for unmatched settlement instructions (isd in the past and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the past (26.04.2016).",
      "-9 parameters synthesis no specific configuration from t2s actor is needed.",
      "+footnotes 1 current recycling period for unmatched instructions of working days.",
      "+2 current recycling period for matched instructions of working days.",
      "+parameters synthesis no specific configuration from t2s actor is needed.",
      "-13 concerned parameter created by updated by mandatory/ possible val- standard or process optional ues default value recycling recycling period t2s operator t2s operator m n/a 20 working days for unmatched instructions recycling recycling period t2s operator t2s operator m n/a 60 working days for matched instructions",
      "+concerned mandatory/ possible standard or parameter created by updated by process optional values default value recycling recycling t2s operator t2s operator m n/a 20 working period for days unmatched instructions recycling recycling t2s operator t2s operator m n/a 60 working period for days matched instructions"
    ],
    "verdict": "38 residual sentence differences (inspect below)"
  },
  {
    "section": "posting_overview",
    "june": {
      "heading": "1.6.1.8 Posting",
      "pdf_pages": [
        303,
        306
      ],
      "sentences": 31
    },
    "november": {
      "heading": "3.6.1.8 Posting",
      "pdf_pages": [
        317,
        321
      ],
      "sentences": 33
    },
    "similarity_ratio": 0.8685,
    "residual_differences": [
      "-it may resort to the optimising application process if needed for the settlement (see section optimising  335).",
      "+it may resort to the optimising application process if needed for the settlement (see section optimising).",
      "-diagram 81 - settlement application processes / posting 13 overview settlement instructions, settlement restrictions and liquidity transfers, sent by the t2s actors or automatically generated by t2s, are submitted to the posting application process at the intended settlement date.",
      "-they can be submitted to the posting application process individually or grouped with other settlement instructions or settlement restrictions or liquidity transfers due to links set by t2s actors or by t2s application processes (see section linked instructions  442).",
      "+figure 81:",
      "+settlement application processes / posting overview settlement instructions, settlement restrictions and liquidity transfers, sent by the t2s actors or automatically generated by t2s, are submitted to the posting application process at the intended settlement date.",
      "+they can be submitted to the posting application process individually or grouped with other settlement instructions or settlement restrictions or liquidity transfers due to links set by t2s actors or by t2s application processes (see section linked instructions).",
      "-in case of failure 201:",
      "+in case of failure:",
      "-they are then submitted to the posting application process including an optimisation in order to identify sets that can settle successfully (see section settlement day  155).",
      "+they are then submitted to the posting application process including an optimisation in order to identify sets that can settle successfully (see section settlement day).",
      "-in case of a high-volume event of corporate actions, failing transactions will be submitted to a dedicated process for optimisation triggered at regular time intervals the provision check, which determines the relevant securities positions, cash balances and limits on the involved accounts and the associated credit memorandum balance.",
      "-in case of lack of cash, lack of securities or insufficient external guarantee headroom, partial settlement (see section partial settlement  343) and auto-collateralisation (see section auto-collateralisation  352) can be used under specific conditions;",
      "+the provision check, which determines the relevant securities positions, cash balances and limits on the involved accounts and the associated credit memorandum balance.",
      "+in case of lack of cash, lack of securities or insufficient external guarantee headroom, partial settlement (see section partial settlement) and auto-collateralisation (see section auto-collateralisation) can be used under specific conditions;",
      "+footnotes 1 in case of a high-volume event of corporate actions, failing transactions will be submitted to a dedicated process for optimisation triggered at regular time intervals"
    ],
    "verdict": "16 residual sentence differences (inspect below)"
  },
  {
    "section": "partial_settlement",
    "june": {
      "heading": "1.6.1.9.3 Partial Settlement",
      "pdf_pages": [
        343,
        353
      ],
      "sentences": 116
    },
    "november": {
      "heading": "3.6.1.9.3 Partial Settlement",
      "pdf_pages": [
        362,
        371
      ],
      "sentences": 125
    },
    "similarity_ratio": 0.4183,
    "residual_differences": [
      "-partialsettlementprocess partial settlement process for settlement instructions a settlement instruction is partially settled , in case there are insufficient securities to settle the full quantity and provided the following conditions are met:",
      "+partial settlement process partial settlement process for settlement instructions a settlement instruction is partially settled, in case there are insufficient securities to settle the full quantity and provided the following conditions are met:",
      "-partial settlement window partial settlement is active in t2s within the dedicated partial settlement windows .",
      "+partial settlement window partial settlement is active in t2s within the dedicated partial settlement windows.",
      "-224 partial settlement is triggered only in case of lack of securities (i.e.",
      "-lack of securities only or lack of securities and cash) but not in case of lack of cash only.",
      "-225 partially released settlement instructions can be submitted for settlement attempts for the total partially released quantity also when the partial settlement window is not running.",
      "-partially released settlement instructions can be submitted for settlement attempts for a part of the partially released quantity only when the partial settlement window is running.",
      "-226 for details about the schedule of partial settlement window, see section settlement day  155 227 including such settlement instructions which are on party hold and have been partially released.",
      "-partial settlement of partially released settlement instructions a settlement instruction on party hold may be partially released to allow the partial settlement of a specified quantity.",
      "+partial settlement of partially released settlement instructions the following two cases can be distinguished:",
      "+partial release when only a party hold is present on the instruction partial release when both a party hold and a cosd hold are present on the instruction in the case where only a party hold is present on the instruction, it may be partially released to allow the partial settlement of a specified quantity.",
      "+in the case where both a party hold and a cosd hold are present on the instruction, the party hold may be partially released which will trigger the blocking of securities.",
      "+if the blocking of the securities is successful, the partial release will be kept pending even at cut-off, until the corresponding blocked quantity is partially cosd released and settled.",
      "+at this time the partial release is considered settled, and an additional release is possible.",
      "+if the attempt to block the securities is unsuccessful (in case the available quantity is lower than the quantity to be blocked), it is recycled until the applicable cut-off, after which the partial release will be cancelled, and the underlying settlement instruction is set back on party hold for the full unsettled quantity.",
      "-meaning the partial settlement cannot take place for an amount lower than an applicable value.25 table 68 - applicable threshold types for partial settlement 2 content of settlement instruction resulting resulting applicable applicable threshold value instruction instruction isin currency threshold type threshold type type fop 228 n/a applicable n/a quantity minimum settlement unit (only for first partial settlement) and set- dvp/dwp set to “quantity” for tlement unit multiple are used.",
      "-both matched settlement instructions dvp/dwp not set to “quantity” unit-quoted applicable cash value amount configured in the currency for both matched setspecified (for quantity, minimum tlement instructions settlement unit and settlement unit multiple are used).",
      "-nominal- amount configured in the currency quoted specified (for quantity, minimum settlement unit and settlement unit multiple are used).",
      "-the parameters determining the threshold applicable above are set:",
      "+meaning the partial settlement cannot take place for an amount lower than an applicable value.",
      "+content of settlement instruction resulting applicable resulting applicable instruction instruction threshold threshold value isin currency type threshold type type fop n/a applicable n/a quantity minimum settlement unit (only for first partial settlement) and settlement unit multiple are used.",
      "+dvp/dwp set to “quantity” for both matched settlement instructions dvp/dwp not set to “quantity” unit-quoted applicable cash value amount configured in the for both matched currency specified (for quantity, settlement minimum settlement unit and instructions settlement unit multiple are used).",
      "+nominal- amount configured in the quoted currency specified (for quantity, minimum settlement unit and settlement unit multiple are used).",
      "+table 68:",
      "+applicable threshold types for partial settlement the parameters determining the threshold applicable above are set:",
      "-by the t2s actors in charge of the administration of the relevant isin in the static data for the applicable threshold in quantity (see section concept of securities in t2s  71).",
      "+by the t2s actors in charge of the administration of the relevant isin in the static data for the applicable threshold in quantity (see section concept of securities in t2s).",
      "-229 in case the settlement instruction does not settle, the settlement instruction is submitted to optimising application process.",
      "+in case the settlement instruction does not settle, the settlement instruction is submitted to optimising application process.",
      "-228 cash value thresholds are not considered for fop regardless of the partial settlement threshold type (partial settlement indicator parc, part) defined within the settlement instruction.",
      "-this also applies for fop instructions related to a foreign currency transaction (non-eur amount).",
      "-229 partially released settlement instructions are only submitted to partial settlement attempts for the released quantity.",
      "-in both cases, the status of each matched settlement instruction and the related reporting are sent to the t2s parties, as described in section send settlement instruction and in chapter 3 for the related content of the message.",
      "+in both cases, the status of each matched settlement instruction and the related reporting are sent to the related content of the message.",
      "-or cancelled for its pending leg (see section instruction cancellation  280).",
      "+or cancelled for its pending leg (see section instruction cancellation).",
      "-the partial release process is cancelled when the released quantity has not fully settled by the relevant cut-off time.",
      "+in case there is only a party hold on the settlement instruction, the partial release process is cancelled when the released quantity has not fully settled by the relevant cut-off time.",
      "+in case there is both a party hold and a cosd hold on the settlement instruction, the partial release process is not cancelled at the relevant cut-off time.",
      "+the partial release process is only cancelled, and the settlement instruction is put back on hold if the activation of the cosd rule set is still unsuccessful (the securities cannot be blocked) at cut-off or if the related settlement restriction is cancelled during revalidation.",
      "-example 90 - partial settlement 2 result fop set to “yes - “quanti- minimum n/a 55 n/a status of the settlement instruc- quantity” by ty” settlement tion is “partially settled”.",
      "-the both t2s parunit set to settled part of the settlement ties “50” and instruction is “55”.",
      "-the pending settlement part of the settlement instruction unit multiple is “45” which becomes the reset to “5” maining quantity.",
      "+example 90:",
      "+partial settlement result fo set to “yes - “quantit minimum n/a 55 n/a status of the settlement p quantity” by y” settlement instruction is “partially settled”.",
      "+both t2s unit set to the settled part of the parties “50” and settlement instruction is “55”.",
      "+settlement the pending part of the unit multiple settlement instruction is “45” set to “5” which becomes the remaining quantity.",
      "-fop set to “yes - “quanti- minimum n/a 57 n/a status of the settlement instruc- quantity” by ty” settlement tion is “partially settled”.",
      "-the only one t2s unit set to settled part of the settlement parties “50” and instruction is “55”.",
      "-the pending settlement part of the settlement instruction unit multiple is “45” which becomes the reset to “5” maining quantity.",
      "+fo set to “yes - “quantit minimum n/a 57 n/a status of the settlement p quantity” by y” settlement instruction is “partially settled”.",
      "+only one t2s unit set to the settled part of the parties “50” and settlement instruction is “55”.",
      "+settlement the pending part of the unit multiple settlement instruction is “45” set to “5” which becomes the remaining quantity.",
      "-result fop set to “yes - “quanti- minimum n/a 49 n/a impossible to apply the partial quantity” by ty” settlement settlement, since the quantity both t2s parunit set to available for a partial settlement ties “50” and is “49” where the minimum setsettlement tlement multiple is set to “50”.",
      "-unit multiple status of the settlement instrucset to “5” tion is “unsettled”.",
      "-result dvp/ set to “yes - “quanti- minimum 100, .0 55 1, ,0 status of the settlement instruc- dwp quantity” by ty” settlement 0 00.00 tion is “partially settled”.",
      "-the both t2s parunit set to settled part of the settlement ties “50” and instruction is “55” for the quantisettlement ty and “55, .00” for the unit multiple amount.",
      "-the pending part of the set to “5” settlement instruction is “45” which becomes the remaining quantity and “45, .00” which becomes the remaining amount.",
      "+fo set to “yes - “quantit minimum n/a 49 n/a impossible to apply the partial p quantity” by y” settlement settlement, since the quantity both t2s unit set to available for a partial settlement parties “50” and is “49” where the minimum settlement settlement multiple is set to unit multiple “50”.",
      "+status of the settlement set to “5” instruction is “unsettled”.",
      "+result dv set to “yes - “quantit minimum 100, .",
      "+55 1, , status of the settlement p/ quantity” by y” settlement instruction is “partially settled”.",
      "+dw both t2s unit set to the settled part of the p parties “50” and settlement instruction is “55” for settlement the quantity and “55, .00” for unit multiple the amount.",
      "+the pending part of set to “5” the settlement instruction is “45” which becomes the remaining quantity and “45, .00” which becomes the remaining amount.",
      "-dvp/ set to “yes - “cash .000€ 100 100, .0 55 60, .",
      "-status of the settlement instruc- dwp quantity” by value” 0 00 tion is “partially settled”.",
      "-the only one t2s settled part of the settlement parties instruction is “55” for the quantity and “55, .00” for the amount.",
      "+dv set to “yes - “cash .000€ 100 100, .",
      "+55 60, status of the settlement p/ quantity” by value” 00 .00 instruction is “partially settled”.",
      "+dw only one t2s the settled part of the p parties settlement instruction is “55” for the quantity and “55, .00” for the amount.",
      "-dvp/ set to “yes - “quanti- minimum 100, .0 49 1, ,0 impossible to apply the partial result dwp quantity” by ty” settlement 0 00.00 settlement, since the quantity both t2s parunit set to available for a partial settlement ties “50” and is “49” where the minimum setsettlement tlement unit is set to “50”.",
      "-status unit multiple of the settlement instruction is set to “5” “unsettled”.",
      "+dv set to “yes - “quantit minimum 100, .",
      "+49 1, , impossible to apply the partial p/ quantity” by y” settlement 000.00 settlement, since the quantity dw both t2s unit set to available for a partial settlement p parties “50” and is “49” where the minimum settlement settlement unit is set to “50”.",
      "+unit multiple status of the settlement set to “5” instruction is “unsettled”.",
      "-in all cases, the statuses of the settlement restrictions and the related reporting are sent to the t2s parties, as described in section send settlement restriction on securities position and section send settlement restriction on cash balance and in chapter 3 for the related content of the message.",
      "-partial settlement process for liquidity transfers t2s settles liquidity transfer for a partial amount in case sufficient cash is not available on the t2s dedicated cash account, without submitting it to the optimising application process.",
      "+in all cases, the statuses of the settlement restrictions and the related reporting are sent to the t2s parties, as described in section send settlement restriction on securities position and section send settlement partial settlement process for liquidity transfers t2s settles liquidity transfer for a partial amount in case sufficient cash is not available on the t2s dedicated cash account, without submitting it to the optimising application process.",
      "-when the liquidity transfer is initiated by a t2s actor different from the account holder (see section liquidity management  575).",
      "+when the liquidity transfer is initiated by a t2s actor different from the account holder (see section liquidity management).",
      "-in all cases, the statuses of the liquidity transfer and the related reporting are sent to the t2s parties, as described in sections send immediate liquidity transfer, execution of liquidity transfer from rtgs to t2s and execution of standing and predefined liquidity transfer orders from t2s to rtgs for dialogue related to liquidity transfer, and in chapter 3 for the related content of the message.",
      "-parameters synthesis 2 concerned parameter created by updated by mandato- possible standard or de- process ry/ op- values fault value tional partial settlement threshold in cash t2s operator t2s operator m amount per currency:",
      "-on settlement value for unit quotequivalent to instructions ed securities , .00€ partial settlement threshold in cash t2s operator t2s operator m amount per currency:",
      "-on settlement value for nominal equivalent to instructions amount quoted , .00€ securities partial settlement threshold in quan- t2s actor t2s actor m quantity to be defined per on settlement tity:",
      "-minimum maintaining isin maintaining instructions settlement unit the isin the isin partial settlement threshold in quan- t2s actor t2s actor m quantity to be defined per on settlement tity:",
      "-settlement unit maintaining isin maintaining instructions multiple the isin the isin",
      "+in all cases, the statuses of the liquidity transfer and the related reporting are sent to the t2s parties, as described in sections send immediate liquidity transfer, execution of liquidity transfer from rtgs to t2s and execution of standing and predefined liquidity transfer orders from t2s to rtgs for dialogue related parameters synthesis concerned mandatory possible standard or parameter created by updated by process / optional values default value partial threshold in cash t2s operator t2s operator m amount per currency:",
      "+settlement on value for unit equivalent to settlement quoted securities , .00€ instructions partial threshold in cash t2s operator t2s operator m amount per currency:",
      "+settlement on value for nominal equivalent to settlement amount quoted , .00€ instructions securities partial threshold in t2s actor t2s actor m quantity to be defined per settlement on quantity:",
      "+minimum maintaining maintaining isin settlement settlement unit the isin the isin instructions partial threshold in t2s actor t2s actor m quantity to be defined per settlement on quantity:",
      "+maintaining maintaining isin settlement settlement unit the isin the isin instructions multiple footnotes 1 partial settlement is triggered only in case of lack of securities (i.e.",
      "+lack of securities only or lack of securities and cash) but not in case of lack of cash only.",
      "+2 partially released settlement instructions can be submitted for settlement attempts for the total partially released quantity also when the partial settlement window is not running.",
      "+partially released settlement instructions can be submitted for settlement attempts for a part of the partially released quantity only when the partial settlement window is running.",
      "+3 for details about the schedule of partial settlement window, see section settlement day 4 including such settlement instructions which are on party hold and have been partially released.",
      "+5 cash value thresholds are not considered for fop regardless of the partial settlement threshold type (partial settlement indicator parc, part) defined within the settlement instruction.",
      "+this also applies for fop instructions related to a foreign currency transaction (non-eur amount).",
      "+6 partially released settlement instructions are only submitted to partial settlement attempts for the released quantity."
    ],
    "verdict": "99 residual sentence differences (inspect below)"
  },
  {
    "section": "realignment_concept",
    "june": {
      "heading": "1.6.1.10 Realignment",
      "pdf_pages": [
        373,
        377
      ],
      "sentences": 47
    },
    "november": {
      "heading": "3.6.1.10 Realignment",
      "pdf_pages": [
        393,
        396
      ],
      "sentences": 48
    },
    "similarity_ratio": 0.9924,
    "residual_differences": [
      "-diagram 85 - realignment application process 11 overview upon the matching of settlement instructions, or upon the validation of already matched settlement instructions, the realignment application process verifies if the incoming business settlement instructions are requiring realignment settlement instructions on securities accounts other than those of the submitting t2s actors (e.g.",
      "+figure 85:",
      "+realignment application process overview upon the matching of settlement instructions, or upon the validation of already matched settlement instructions, the realignment application process verifies if the incoming business settlement instructions are requiring realignment settlement instructions on securities accounts other than those of the submitting t2s actors (e.g.",
      "-realignment process parametersnecessaryforrealignment role and links between csds for cross-csd and external-csd settlement irrespective of whether it is a cross-csd or an external-csd settlement, a csd is defined for the realignment process as:",
      "+realignment process parameters necessary for realignment role and links between csds for cross-csd and external-csd settlement irrespective of whether it is a cross-csd or an external-csd settlement, a csd is defined for the realignment process as:",
      "-for a given isin, an investor csd can define several such investor-type csd links, meaning that it can define several technical issuer csds for a given isin.",
      "+for a given isin, an investor csd can define several such investortype csd links, meaning that it can define several technical issuer csds for a given isin.",
      "-2 parameters definition security csd links each investor csd has to define at least one technical issuer csd per securities it intends to set as eligible for settlement (see section securities reference data  71).",
      "+parameters definition security csd links each investor csd has to define at least one technical issuer csd per securities it intends to set as eligible for settlement (see section securities reference data).",
      "-(see section configuration of securities accounts for cross-csd settlement and external csd settlement  97) this set-up is used by t2s to derive the realignment chain applicable to matched settlement instructions starting either from both investor csds (delivering and receiving) up to the issuer csd(s) of the traded securities when default links are used, or from the delivering investor csd up to the receiving investor csd (or vice versa) when alternative links are used.",
      "+(see section configuration of securities accounts for cross-csd settlement and external csd settlement) this set-up is used by t2s to derive the realignment chain applicable to matched settlement instructions starting either from both investor csds (delivering and receiving) up to the issuer csd(s) of the traded securities when default links are used, or from the delivering investor csd up to the receiving investor csd (or vice versa) when alternative links are used."
    ],
    "verdict": "11 residual sentence differences (inspect below)"
  },
  {
    "section": "linked_overview",
    "june": {
      "heading": "1.6.1.11 Linked Instructions",
      "pdf_pages": [
        442,
        443
      ],
      "sentences": 7
    },
    "november": {
      "heading": "3.6.1.11 Linked Instructions",
      "pdf_pages": [
        467,
        468
      ],
      "sentences": 7
    },
    "similarity_ratio": 1.0,
    "residual_differences": [],
    "verdict": "no sentence-level difference after normalisation"
  },
  {
    "section": "cosd_concept",
    "june": {
      "heading": "1.6.1.12 Conditional Settlement",
      "pdf_pages": [
        452,
        455
      ],
      "sentences": 26
    },
    "november": {
      "heading": "3.6.1.12 Conditional Settlement",
      "pdf_pages": [
        478,
        482
      ],
      "sentences": 32
    },
    "similarity_ratio": 0.9207,
    "residual_differences": [
      "-252 for details about the pre-emption, see section securities blocking/reservation/earmarking  486.",
      "-diagram 121 - conditional settlement application process 2 t2s automatically detects and performs conditional settlement, based on cosd rules defined and maintained by each csd in the static data.",
      "+figure 121:",
      "+conditional settlement application process t2s automatically detects and performs conditional settlement, based on cosd rules defined and maintained by each csd in the static data.",
      "-253 the matched settlement instructions (and their linked t2s generated realignment settlement instructions if any) remain pending and the securities and/or cash remain blocked until t2s receives:",
      "+the matched settlement instructions (and their linked t2s generated realignment settlement instructions if any) remain pending and the securities and/or cash remain blocked until t2s receives:",
      "+if the cosd rule set is flagged to allow for partial release, it is also possible for the administering parties to perform a partial cosd release.",
      "+the partial cosd release is only allowed for rule sets which block securities only.",
      "+it cannot be applied on cosd rule sets which block securities and cash or cash only.",
      "-t2s may also cancel the settlement instruction and/or the t2s generated settlement instruction following the revalidation process (see section business validation  218) and changes in the realignment chain (see section realignment  373).",
      "+t2s may also cancel the settlement instruction and/or the t2s generated settlement instruction following the revalidation process (see section business validation) and changes in the realignment chain (see section realignment).",
      "+footnotes 1 in case a settlement instruction meets the cosd rule and there is no securities (resp.",
      "+no cash) to be blocked due to a pfod (rep.",
      "+due to a a fop), then no cosd blocking occurs."
    ],
    "verdict": "14 residual sentence differences (inspect below)"
  },
  {
    "section": "status_mgmt_concept",
    "june": {
      "heading": "1.6.3.1 Status Management",
      "pdf_pages": [
        653,
        657
      ],
      "sentences": 9
    },
    "november": {
      "heading": "3.6.3.1 Status Management",
      "pdf_pages": [
        700,
        704
      ],
      "sentences": 9
    },
    "similarity_ratio": 1.0,
    "residual_differences": [],
    "verdict": "no sentence-level difference after normalisation"
  },
  {
    "section": "schedule",
    "june": {
      "heading": "1.4.2 T2S schedule",
      "pdf_pages": [
        156,
        159
      ],
      "sentences": 45
    },
    "november": {
      "heading": "3.4.2 T2S schedule",
      "pdf_pages": [
        169,
        172
      ],
      "sentences": 45
    },
    "similarity_ratio": 0.9994,
    "residual_differences": [
      "-t2s schedule the t2s schedule is under the control of the t2s operator, for creation of any new timelines, changing and/or deletion of existing time for a period or event.",
      "+t2s schedule the t2s schedule is under the control of the t2s operator, for creation of any new timelines, changing and/ or deletion of existing time for a period or event.",
      "-t2s manages the transition between the various periods (see section settlement day high level schedule  158) as an event.",
      "+t2s manages the transition between the various periods (see section settlement day high level schedule) as an event."
    ],
    "verdict": "4 residual sentence differences (inspect below)"
  },
  {
    "section": "rts_phase",
    "june": {
      "heading": "1.4.4.4 Real-time settlement (RTS)",
      "pdf_pages": [
        193,
        195
      ],
      "sentences": 25
    },
    "november": {
      "heading": "3.4.4.4 Real-time settlement (RTS)",
      "pdf_pages": [
        204,
        206
      ],
      "sentences": 25
    },
    "similarity_ratio": 0.7135,
    "residual_differences": [
      "-143 additionally t2s performs a settlement attempt for any new intraday settlement instructions, settlement restrictions and liquidity transfers validated and accepted during real-time settlement period;",
      "+additionally t2s performs a settlement attempt for any new intraday settlement instructions, settlement restrictions and liquidity transfers validated and accepted during real-time settlement period;",
      "-143 during the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been attempted for settlement.",
      "-this serialization process will concern all transactions with age  3 selected by the regular recycling process following a credit in securities or cash or an increase in cmb headroom or limit, guaranteeing that an older transaction will be attempted before a younger one with the same priority.",
      "-the transactions selected by one given recycling process will be segregated into eight groups, depending on their priority and age:",
      "-group 1 group 2 group 3 group 4 group 5 group 6 group 7 group 8 priority 1 priority 1 priority 2 priority 2 priority 3 priority 3 priority 4 priority 4 age  3 age  3 age  3 age  3 age  3 age  3 age  3 age  3 should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to the regular recycling process.",
      "+footnotes 1 during the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been attempted for settlement.",
      "+this serialization process will concern all transactions with age  3 selected by the regular recycling process following a credit in securities or cash or an increase in cmb headroom or limit, guaranteeing that an older transaction will be attempted before a younger one with the same priority.",
      "+the transactions selected by one given recycling process will be segregated into eight groups, depending on their priority and age:",
      "+group 1 group 2 group 3 group 4 group 5 group 6 group 7 group 8 priority 1 priority 1 priority 2 priority 2 priority 3 priority 3 priority 4 priority 4 age  3 age  3 age  3 age  3 age  3 age  3 age  3 age  3 should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to the regular recycling process."
    ],
    "verdict": "10 residual sentence differences (inspect below)"
  },
  {
    "section": "validation_concept",
    "june": {
      "heading": "1.6.1.1 Business Validation",
      "pdf_pages": [
        218,
        220
      ],
      "sentences": 4
    },
    "november": {
      "heading": "3.6.1.1 Business Validation",
      "pdf_pages": [
        229,
        231
      ],
      "sentences": 5
    },
    "similarity_ratio": 0.992,
    "residual_differences": [
      "-diagram 53 - business validation application process 2 overview when a t2s actor sends any of the above mentioned instructions, this process checks the consistency of the instruction and verifies that it successfully passes the applicable validation checks.",
      "+figure 53:",
      "+business validation application process overview when a t2s actor sends any of the above mentioned instructions, this process checks the consistency of the instruction and verifies that it successfully passes the applicable validation checks."
    ],
    "verdict": "3 residual sentence differences (inspect below)"
  },
  {
    "section": "nts_processing",
    "june": {
      "heading": "1.4.4.2 Night-time settlement (NTS)",
      "pdf_pages": [
        167,
        170
      ],
      "sentences": 30
    },
    "november": {
      "heading": "3.4.4.2 Night-time settlement (NTS)",
      "pdf_pages": [
        180,
        183
      ],
      "sentences": 30
    },
    "similarity_ratio": 0.9998,
    "residual_differences": [
      "-ntsprocessing during the night-time settlement period, t2s processes the settlement instructions, settlement restrictions and liquidity transfers in sequences within two settlement cycles.",
      "+nts processing during the night-time settlement period, t2s processes the settlement instructions, settlement restrictions and liquidity transfers in sequences within two settlement cycles.",
      "-ntsreporting at the end of each night-time sequence, t2s generates full or delta reports as per the report configuration setup of the relevant t2s actors.",
      "+nts reporting at the end of each night-time sequence, t2s generates full or delta reports as per the report configuration setup of the relevant t2s actors."
    ],
    "verdict": "4 residual sentence differences (inspect below)"
  }
]

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "future", "question_type": "milan_t2s_release_plan_nov"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-r2026nov-plan]] — R2026.NOV plan: UTEST from 28 September, tests to 28 October, production deployment planned 14 November effective 16 November 2026, XSD documentation in MT-X (reviewed 2026-09-14; modes ['future', 'reference']; entities ['Milan']; basis reference_description; subject release R2026.NOV)
CITATION: ON_28/2026 T2S Release R2026.NOV and non-binding XSDs (21 July 2026) | ON_28/2026 PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/T2S%20R2026.NOV%20e%20Non-binding%20XSDs%20V0.1%20rev%20OPP_ENG.pdf
CITATION: Operational notice: T2S Release R2026.NOV and binding XSDs (dated 10 August 2026, hub date 07/08/2026) | Binding-XSD notice of 10 August 2026, PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/T2S%20R2026.NOV%20-%20binding%20XSDs%20V0.1%20ENG.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Planned dates are not deployment evidence; ON_28 page 2 contains an internal inconsistency ('from Tuesday 29 April' for UTEST re-tests) preserved as printed.
LIMITATION: The MyStandards XSD documentation is client-only.
EXCERPT (ON_28/2026 PDF 1–2):
[PDF page 1]

21 July 2026
ON_28/2026


T2S Release R2026.NOV and
Non-binding XSDs
   To the attention of:                           DCPs, ICPs


   Priority:                                      Medium


   Topic:                                         T2S Release R2026.NOV e Non-binding XSDs



Dear Client

Please find below the updates regarding the T2S Release R2026.NOV and the non-binding XSDs



Test Plan

We wish to inform you that the upcoming T2S Release R2026.NOV will be available in the external
test environment (UTEST) on 28 September 2026.

With this release, the update process for T2S messages to the latest release (2026) will be
completed, finalising alignment with the annual releases that will be maintained from now onwards.

The release comprises 11 change requests (CR-0798, CR-0828, CR-0840, CR-0841, CR-0842, CR-
0843, CR-0850, CR-0854, CR-0856, CR-0859, T2S-CHN-003) and the resolution of six defects.

External tests for participants using ES-MIL systems may be conducted from Monday 28
September until Wednesday 28 October 2026.

Directly connected participants (DCPs) are invited to retest all defects and change requests
applicable to their operational model, indicating their intention to proceed with retesting in the
dedicated form “R2026.NOV PBI and CRs content incl declaration to test v0.1.xls”, and providing
weekly updates on the progress of verification activities to MT-T2S-test@euronext.com using the
same form.

The release will be deployed in production on 14 November, effective from 16 November 2026.

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

                                                      INTERNAL USE ONLY



[PDF page 2]

Test Schedule

ES-MIL will test all defects and change requests applicable to its operational model in the EAC test
environment reserved for central securities depositories (CSDs), and will repeat these tests from
Tuesday 29 April in the UTEST environment.

In accordance with the plan established by the European Central Bank, directly connected
participants (DCPs) are requested to submit final feedback on the outcome of testing for the change
requests and problem business items (PBIs) by 10:00 on 27 October 2026 to MT-T2S-
test@euronext.com. This feedback will be included in the report sent to the T2S decision-making
bodies on the same day.

Following this date and until 14 November 2026, testing activities may continue. Any further
findings will be communicated on an ongoing basis to the aforementioned decision-making bodies
for the purpose of verifying the stability of the release.



Relevant documentation
A folder has been created within the MT-X documentation section (HOME > Docs > Projects > T2S
releases > T2S Release R2026.NOV) containing: • the form “R2026.JUN PBI and CRs content incl
declaration to test v0.1.xls” • documentation relating to the non-binding XSD schema for T2S
R2026.NOV, titled “MyStandard Link_non_binding XSD_T2S-CoCo UDFS R2026.nov”.

The final documentation for the message dictionaries mentioned above will be published on 28
July 2026 in the same folder. ES-MIL will inform you accordingly with a dedicated operational
notice.

For any support requests during the testing phase, please refer to the following address
MT-T2S-Test
E: MT-T2S-Test@euronext.com




| 2 of 2


                                       INTERNAL USE ONLY
EXCERPT (Binding-XSD notice of 10 August 2026, PDF 1–2):
[PDF page 1]

10 August 2026

T2S Release R2026.NOV and
binding XSDs
   To the attention of:                           DCPs, ICPs


   Priority:                                      Medium


   Topic:                                         T2S Release R2026.NOV and binding XSDs



Dear Client

Please find below the updates regarding the T2S Release R2026.NOV and the binding XSDs



Test Plan

We wish to inform you that the upcoming T2S Release R2026.NOV will be available in the external
test environment (UTEST) on 28 September 2026.

With this release, the update process for T2S messages to the latest release (2026) will be
completed, finalising alignment with the annual releases that will be maintained from now onwards.

The release comprises 11 change requests (CR-0798, CR-0828, CR-0840, CR-0841, CR-0842, CR-
0843, CR-0850, CR-0854, CR-0856, CR-0859, T2S-CHN-003) and the resolution of six defects.

External tests for participants using ES-MIL systems may be conducted from Monday 28
September until Wednesday 28 October 2026.

Directly connected participants (DCPs) are invited to retest all defects and change requests
applicable to their operational model, indicating their intention to proceed with retesting in the
dedicated form “R2026.NOV PBI and CRs content incl declaration to test v0.1.xls”, and providing
weekly updates on the progress of verification activities to MT-T2S-test@euronext.com using the
same form.

The release will be deployed in production on 14 November, effective from 16 November 2026.



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

                                                      INTERNAL USE ONLY



[PDF page 2]

Test Schedule

ES-MIL will test all defects and change requests applicable to its operational model in the EAC test
environment reserved for central securities depositories (CSDs), and will repeat these tests from
Tuesday 28 September in the UTEST environment.

In accordance with the plan established by the European Central Bank, directly connected
participants (DCPs) are requested to submit final feedback on the outcome of testing for the change
requests and problem business items (PBIs) by 10:00 on 27 October 2026 to MT-T2S-
test@euronext.com. This feedback will be included in the report sent to the T2S decision-making
bodies on the same day.

Following this date and until 14 November 2026, testing activities may continue. Any further
findings will be communicated on an ongoing basis to the aforementioned decision-making bodies
for the purpose of verifying the stability of the release.



Relevant documentation
A folder has been created within the MT-X documentation section (HOME > Docs > Projects > T2S
releases > T2S Release R2026.NOV) containing: • the form “R2026.JUN PBI and CRs content incl
declaration to test v0.1.xls” • documentation relating to the binding XSD schema for T2S
R2026.NOV, titled “MyStandard Link_binding XSD_T2S-CoCo UDFS R2026-nov”.

For any support requests during the testing phase, please refer to the following address
MT-T2S-Test
E: MT-T2S-Test@euronext.com




| 2 of 2


                                       INTERNAL USE ONLY