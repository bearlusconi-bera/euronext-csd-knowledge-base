QUESTION FROM THE USER:
Specify the settlement flow, messages and timing for a DvP in EUR between a Monte Titoli participant selling as ICP and a buyer at another T2S CSD with a direct link, on release R2026.JUN. Include what is not verified.

The user asks for a specification: use SPECIFICATION-TEMPLATE.md headings and expose every missing production field explicitly.

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:59:40.015196+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "cross_csd_message_flow", "release": "R2026.JUN", "access_model": "ICP", "currency": "EUR", "link_model": "direct-both-in-T2S"}
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

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "realignment_mechanism"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_rule"}
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

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_link_guide"}
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

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_connectivity_and_static_data"}
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

=== RETRIEVAL 7: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_xtrm_lifecycle_maintenance"}
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

=== RETRIEVAL 8: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_message_sese023_scope", "release": "R2026.JUN"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-sese023-scope]] — sese.023.001.11 Settlement Instruction: scope and building blocks (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §3.3.6.4.1–3.3.6.4.2 outline of the schema; PDF 1233–1234 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Business rules table (PDF 1235 onwards) and message examples are not admitted; the T2S-specific schema is published on MyStandards, which requires an account.
LIMITATION: This is the CSD/DCP-to-T2S message, not a bank-to-CSD interface.
EXCERPT (§3.3.6.4.1–3.3.6.4.2 outline of the schema; PDF 1233–1234):
3.3.6.4 SecuritiesSettlementTransactionInstructionV11 (sese.023.001.11)


 2    3.3.6.4.1 Overview and scope of the message

 3    This chapter illustrates the SecuritiesSettlementTransactionInstructionV11 message.

 4   The SecuritiesSettlementTransactionInstructionV11, also known as a Settlement Instruction within T2S is
 5    sent by a CSD or a directly connected T2S party to T2S. The Settlement Instruction allows the Instructing
 6    party to request a transfer of securities, relating to a securities transaction (e.g. an OTC trade, a corporate
 7    action, a repo), with or without a cash payment.

 8    In response to the Settlement Instruction, T2S sends a sese.024.001.12 [ 1257] when validation, matching
 9   and settlement are carried out and a sese.025.001.11 [ 1332] when settlement is successful.


10    3.3.6.4.2 The T2S-specific schema

11   Outlineoftheschema

12   The SecuritiesSettlementTransactionInstructionV11 message is composed of the following message building
13    blocks:

14   Transaction Identification

15    This building block is mandatory and not repetitive. It contains an identification assigned by the instructing
16    party to uniquely and unambiguously identify the transaction.

17   SettlementTypeAndAdditionalParameters

18    This building block is mandatory and non repetitive. It contains settlement type and identification infor-
19    mation.

20   NumberCounts

21    This building block is optional and non repetitive. It contains the number of transactions linked.

22   Linkages

23    This building block is optional and repetitive. It is used to link instructions and specify settlement sequences
24    (e.g. after/before/with etc.).

25   TradeDetails

26    This building block is mandatory and non repetitive. It contains detailed information related to the Settle-
27   ment Instruction.

28   FinancialInstrumentIdentification

29    This building block is mandatory and non repetitive. It identifies the financial instrument for which the trans-
30    action is being settled.

31   FinancialInstrumentAttributes

32     It contains elements characterising the financial instrument for which the transaction is being settled. It is
33    not required in T2S.

34   QuantityAndAccountDetails



                                                                                           Page 1233 of 2017



[PDF page 1234]

                                                                   T2S User Detailed Functional Specifications
                                                                                                Catalogue of messages
                                                                                                                                    List of Messages

 1    This building block is mandatory and non repetitive. It contains the details related to the account and quanti-
 2    ty involved in the transaction.

 3   SettlementParameters

 4    This building block is mandatory and non repetitive. It contains parameters which explicitly state the condi-
 5    tions that must be fulfilled before a particular transaction of a financial instrument can be settled. These
 6    parameters are defined by the Instructing party in compliance with settlement rules in the market the trans-
 7    action settles in.

 8   DeliveringSettlementParties

 9    This building block is optional and non repetitive. It contains the chain of delivering settlement parties.

10   ReceivingSettlementParties

11    This building block is optional and non repetitive. It contains the chain of receiving settlement parties.

12   CashParties

13    This building block is optional and non repetitive. It contains the cash parties involved in the transaction if
14    different for the securities settlement parties.

15   SettlementAmount

16    This building block is optional and non repetitive. It contains the total amount of money to be paid or re-
17    ceived in exchange for the securities.

18   OtherAmounts

19    This building block contains other amounts than the settlement amount. It is not required in T2S.

20   OtherBusinessParties

21    This building block contains other business parties relevant to the transaction. It is not required in T2S.

22   AdditionalPhysicalOrRegistrationDetails

23    This building block contains information required for the registration or physical settlement. It is not required
24     in T2S.

25    References/Links

26   The T2S-specific schema and documentation in HTML/PDF format as well as the message examples are pro-
27    vided outside of this document under the following link:

28    http://www.swift.com/mystandards/T2S/sese.023.001.11_T2S

29

=== RETRIEVAL 9: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_message_sese024_usages", "release": "R2026.JUN"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-sese024-usages]] — sese.024.001.12 Status Advice: scope and hold-related message usages (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §3.3.6.5.1 with footnotes 417–424; PDF 1257–1258 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Only the usages printed on these pages are admitted; the complete usage list continues beyond PDF 1258.
LIMITATION: Local relays of statuses to ICPs are service dependent.
EXCERPT (§3.3.6.5.1 with footnotes 417–424; PDF 1257–1258):
3.3.6.5 SecuritiesSettlementTransactionStatusAdviceV12 (sese.024.001.12)


25    3.3.6.5.1 Overview and scope of the message

26    This chapter illustrates the SecuritiesSettlementTransactionStatusAdviceV12 message. The SecuritiesSettle-
27   mentTransactionStatusAdviceV12message, also known as Settlement Instruction Status Advice, is sent by
28   T2S to a CSD or other directly connected T2S party. It is used to inform about the current status of a Set-
29    tlement Instruction (sese.023.001.11) which has been previously sent to T2S. The status may be a pro-
30    cessing, matching, or settlement status.

31    This message is sent by T2S in the following message usages:

32         l  Rejected;

33         l  Accepted;

34         l  Accepted with Hold; 417



     _________________________



                                                                                           Page 1257 of 2017



[PDF page 1258]

                                                                  T2S User Detailed Functional Specifications
                                                                                               Catalogue of messages
                                                                                                                                  List of Messages

1         l  Party Hold; 418

2         l CSD Hold; 419

3         l  Accepted with CSD Validation Hold; 420

4         l CoSD Hold;

5         l CoSD awaiting from Administering Party;

6         l  Counterparty’s Settlement Instruction on Hold 421, 422;

7         l No Hold remain; 423

8         l  Other Hold remain(s); 424

    _________________________

       417   The rule R7 (SettlementStatusAndMatchedRule) defined by ISO for the sese.024 states that if settlement status/reason is used alone, then it
            means that the transaction is matched. Currently there are four exceptions to this rule in T2S as the sese.024 status advice message may report a
               settlement/reason status of an unmatched instruction in the following scenarios:
                            l   Put on party hold (PREA),
                            l   Put on CSD hold (CSDH),
                            l   Put on CSD validation hold (CVAL)
                            l  No hold exists or last applicable hold indicator is released (FUTU/CYCL depending whether the instruction is pending or failing).

       418   The rule R7 (SettlementStatusAndMatchedRule) defined by ISO for the sese.024 states that if settlement status/reason is used alone, then it
            means that the transaction is matched. Currently there are four exceptions to this rule in T2S as the sese.024 status advice message may report a
               settlement/reason status of an unmatched instruction in the following scenarios:
                            l   Put on party hold (PREA),
                            l   Put on CSD hold (CSDH),
                            l   Put on CSD validation hold (CVAL)
                            l  No hold exists or last applicable hold indicator is released (FUTU/CYCL depending whether the instruction is pending or failing).

       419   The rule R7 (SettlementStatusAndMatchedRule) defined by ISO for the sese.024 states that if settlement status/reason is used alone, then it
            means that the transaction is matched. Currently there are four exceptions to this rule in T2S as the sese.024 status advice message may report a
               settlement/reason status of an unmatched instruction in the following scenarios:
                            l   Put on party hold (PREA),
                            l   Put on CSD hold (CSDH),
                            l   Put on CSD validation hold (CVAL)
                            l  No hold exists or last applicable hold indicator is released (FUTU/CYCL depending whether the instruction is pending or failing).

       420   The rule R7 (SettlementStatusAndMatchedRule) defined by ISO for the sese.024 states that if settlement status/reason is used alone, then it
            means that the transaction is matched. Currently there are four exceptions to this rule in T2S as the sese.024 status advice message may report a
               settlement/reason status of an unmatched instruction in the following scenarios:
                            l   Put on party hold (PREA),
                            l   Put on CSD hold (CSDH),
                            l   Put on CSD validation hold (CVAL)
                            l  No hold exists or last applicable hold indicator is released (FUTU/CYCL depending whether the instruction is pending or failing).

       421   When the settlement instruction on hold is a business instruction and its counterparty´s instruction is a realignment instruction, no hold status
               advice will be sent to the counterparty. The realignment instruction will be informed about the hold status of the business instruction via LINK

       422   When the settlement instruction on hold is a realignment instruction and its counterparty´s instruction is a business instruction, no hold status
               advice will be sent to the counterparty. The business instruction will be informed about the hold status of the realignment instruction via LINK

       423   The rule R7 (SettlementStatusAndMatchedRule) defined by ISO for the sese.024 states that if settlement status/reason is used alone, then it
            means that the transaction is matched. Currently there are four exceptions to this rule in T2S as the sese.024 status advice message may report a
               settlement/reason status of an unmatched instruction in the following scenarios:
                            l   Put on party hold (PREA),
                            l   Put on CSD hold (CSDH),
                            l   Put on CSD validation hold (CVAL)
                            l  No hold exists or last applicable hold indicator is released (FUTU/CYCL depending whether the instruction is pending or failing).


                                                                                         Page 1258 of 2017

=== RETRIEVAL 10: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_allegement_rules"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-allegement]] — Allegement process and standard delay parameters (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.3 including Table of parameters (1 hour / 5 hours); PDF 271–277 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Parameter values are the T2S Operator defaults printed in the UDFS; local CSDs relay allegements through their own channels (see local sections).
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.3 including Table of parameters (1 hour / 5 hours); PDF 271–277):
1.6.1.3 Allegement


27    1.6.1.3.1 Concept

28   The Allegement process consists in sending a message in order to advise an account owner that another T2S
29    Actor has instructed against it, whereas the account owner has no corresponding instruction. In case the


                                                                                            Page 271 of 2017



[PDF page 272]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   CSD of the Counterparty is an external CSD, T2S sends the allegement message to this external CSD since it
 2   behaves as a Participant of a CSD which is in T2S and therefore, the information to contact the external CSD
 3     is available in T2S.

 4                               DIAGRAM 58 - ALLEGEMENT APPLICATION PROCESS





 5

 6    1.6.1.3.2 Overview

 7   T2S applies the Allegement process for Unmatched Settlement Instructions and Unmatched Cancellation
 8    Instructions that require matching. The Allegement process for Unmatched Settlement Instructions and the
 9    Allegement process for Unmatched Cancellation Instructions are described below. T2S only sends one Al-
10    legement message per instruction. However, under specific conditions described below, this Allegement can
11   be cancelled or removed.





                                                                                            Page 272 of 2017



[PDF page 273]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                    DIAGRAM 59 - ALLEGEMENT PROCESS





 2

 3    1.6.1.3.3 Allegement process

 4   SettlementAllegement

 5     If a Settlement Instruction does not match after the first matching attempt (See section Matching [ 267]),
 6    the Counterparty is informed through an Allegement message after a predefined period of time (standard
 7    delay period, that is configured in T2S Reference Data by the T2S Operator). T2S does not send an Al-
 8    legement message in case the Settlement Instruction includes an ISO Transaction Code related to a type of
 9    transaction that is meant to be instructed as already matched (i.e. an ISO Transaction Code that is not pre-
10    sent in the Allegement message). This dialogue is reflected in Send Settlement Instruction. Interested par-
11     ties can also be informed depending on their message subscription preferences (see section Message sub-
12    scription [ 135]).

13   The Counterparty receives the Allegement according to two different scenarios.

14    Scenario A: A certain time after the first matching attempt (standard delay period), to avoid early transmis-
15    sion of the message.





                                                                                            Page 273 of 2017



[PDF page 274]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                               Application Processes Description

1                              DIAGRAM 60 - SCENARIO A: STANDARD DELAY PERIOD





2

3    Scenario B: Or at the latest a specified time (standard delay period) before the cut-off time of the Intended
4    Settlement Date, i.e. in case the end of the standard delay period would leave less than the standard delay
5    period before the cut-off.





                                                                                          Page 274 of 2017



[PDF page 275]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                      DIAGRAM 61 - SCENARIO B: STANDARD DELAY PERIOD EXCEEDS ISD CUT OFF





 2

 3    CancellationofanAllegementMessage

 4     If an Unmatched Settlement Instruction is cancelled by the T2S Actor, the Counterparty receives a Cancella-
 5    tion of the Allegement message automatically generated by T2S. This dialogue is reflected in section Send
 6    Settlement Instruction. Interested parties can also be informed depending on their message subscription
 7    preferences (see section Message subscription [ 135]).

 8                  DIAGRAM 62 - SCENARIO A FOR SENDING A CANCELLATION OF THE ALLEGEMENT MESSAGE





 9

10     If an Unmatched Settlement Instruction is automatically cancelled by T2S (Cancellation by the system), the
11    Counterparty receives a Cancellation of the Allegement message automatically generated by T2S.

12   The cases that may trigger cancellation by the system of an Unmatched Settlement Instruction as described
13     in section Instruction Cancellation [ 280] are the following:

14   When the pending Unmatched Settlement Instruction exceeds the recycling period;


                                                                                            Page 275 of 2017



[PDF page 276]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    Unsuccessful revalidation: In case the instruction is affected by a reference data update or during the Start
 2    of day revalidation.

 3                  DIAGRAM 63 - SCENARIO B FOR SENDING A CANCELLATION OF THE ALLEGEMENT MESSAGE





 4

 5   RemovalofanAllegementMessage

 6    In case the Counterparty sends its corresponding Settlement Instruction to T2S, and if both Instructions are
 7    matched, the Counterparty receives a Removal of Allegement message, since the previously sent Allegement
 8     is no longer valid. This dialogue is reflected in section Send Settlement Instruction. Interested parties can
 9    also be informed depending on their message subscription preferences (see section Message subscription
10    [ 135]).

11                    DIAGRAM 64 - SCENARIO FOR SENDING A REMOVAL OF THE ALLEGEMENT MESSAGE





12

13    CancellationAllegement

14     If a T2S Actor sends a Cancellation Instruction that requires the cancellation of both legs of a Settlement
15    Instruction and the Counterparty has not sent its Cancellation Instruction, T2S sends a Status Advice mes-
16    sage to the T2S Actor (with no delay period) informing that its cancellation is pending and another one to
17    the Counterparty informing that its Cancellation Instruction is requested. This dialogue is reflected in section
18   Send Cancellation Instruction of a Settlement Instruction or a Settlement Restriction on Securities Position
19   and in section Send Cancellation Instruction of a Settlement Restriction on cash balance.

20                   DIAGRAM 65 - SCENARIO FOR SENDING A CANCELLATION ALLEGEMENT STATUS ADVICE





21




                                                                                            Page 276 of 2017



[PDF page 277]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.3.4 Parameters Synthesis

 2   The following parameters are specified by the T2S Operator:

 3         l  Allegement for first unsuccessful matching attempt (Standard delay period): Defined as the standard de-
 4        lay period from the first unsuccessful matching attempt of a settlement instruction. It is calculated in
 5       hours and minutes.

 6         l  Allegement before Intended Settlement Date (Before cut-off): Defined as the standard delay period
 7      measured backwards from the FOP cut-off time on the intended settlement date. It is calculated in hours
 8      and minutes. T2S sends out an allegement at the earliest point in time between this period and the peri-
 9      od defined by the allegement for first unsuccessful matching.

10   No specific configuration from T2S Actor is needed.
11

       CONCERNED   PARAMETER   CREATED BY   UPDATED BY   MANDATORY/  POSSIBLE VAL-  STANDARD OR
        PROCESS                                             OPTIONAL       UES     DEFAULT VALUE

          Settlement    Standard delay  T2S Operator   T2S Operator      M       To be defined      1 hour
         Allegement        period

          Settlement     Before cut-off   T2S Operator   T2S Operator      M       To be defined     5 hours
         Allegement


12

=== RETRIEVAL 11: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_status_model"}
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

=== RETRIEVAL 12: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_hold_release_process"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-hold-release]] — Hold and release: indicators, exhaustive scenarios, hold/release default and partial release (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.6.1–1.6.1.6.3 with Tables 61–62 and footnotes 196–197; PDF 284–289 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.6.5–1.6.1.6.6 partial release conditions; PDF 292–295 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: The release process narrative (§1.6.1.6.4, PDF 290–291) is not admitted.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.6.1–1.6.1.6.3 with Tables 61–62 and footnotes 196–197; PDF 284–289):
1.6.1.6 Hold and Release


18    1.6.1.6.1 Concept

19   T2S Hold/Release process provides T2S Actors the functionality to hold and release Settlement Instructions,
20    at any time during its lifecycle until they are settled or cancelled. It is also possible to hold the pending part
21    of a partially settled Settlement Instruction and, under specific conditions, to partially release a Settlement
22    Instruction.

23   T2S Actors who want to hold, release or partially release an existing Settlement Instruction need to send a
24    Hold/Release Instruction including only one modification per instruction. T2S Actors can also send a Settle-
25   ment Instruction initially on Hold.

26   A Hold/Release Instruction can be used to put on hold both legs at the same time or only one leg of a Set-
27    tlement Instruction that entered T2S as already matched depending if the reference used in the Hold In-
28    struction refers to the information of one leg or both legs of the Settlement Instruction as shown in the table
29   below (see section Instruction Types).





                                                                                            Page 284 of 2017



[PDF page 285]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                             TABLE 61 - REFERENCES USED FOR HOLD/RELEASE INSTRUCTION
 2

                                      ALREADY MATCHED SETTLEMENT      SETTLEMENT INSTRUCTIONS
                                              INSTRUCTION                 MATCHED IN T2S

       Hold/Release Instruction of one leg of            T2S Reference                  T2S Actor Reference
       the Settlement Instruction                                                                                                         or

                                                                               T2S Reference

       Hold/Release Instruction of both legs          T2S Actor Reference                      X
        of the Settlement Instruction

 3    For Hold/Release Instructions referring to both legs of the Settlement Instruction (i.e. if the T2S Actor In-
 4    struction Reference refers to a Settlement Instruction sent as already matched to T2S), T2S splits the infor-
 5    mation of the Hold/Release Instruction into two separate maintenance instructions, one per each leg of the
 6    referenced Settlement Instruction. As the inbound message related to the already matched maintenance
 7    instruction is split internally, two different Hold/Release Instructions are created in T2S.

 8    Additionally, T2S automatically puts a Settlement Instruction on Hold if it fulfils any restriction defined by the
 9   CSDs, known as CSD Validation Hold or Party Hold (See section Business Validation [ 218]) or if it is identi-
10    fied as a CoSD on the Intended Settlement Date (See section Conditional Settlement [ 452]).

11    Settlement Instructions on Hold are not eligible for the settlement process and are kept pending until they
12    are released by all the involved parties. Nevertheless, these instructions can be matched, amended or can-
13    celled (however Settlement Instructions on CoSD Hold cannot be amended and can only be cancelled follow-
14    ing specific rules - see section Instruction Cancellation [ 280]).





                                                                                            Page 285 of 2017



[PDF page 286]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                             DIAGRAM 68 - HOLD AND RELEASE APPLICATION PROCESS





 2

 3    1.6.1.6.2 Overview

 4   The Hold/Release Instruction has two hold indicators that can be filled by the T2S Actor:

 5         l  “Party Hold”;

 6         l  “CSD Hold”.

 7    In order to hold an instruction, the T2S Actor needs to put “Yes” in the relevant hold indicator of the
 8    maintenance instruction (Hold Instruction). If the T2S Actor wants to send a Settlement Instruction initially
 9   on Hold, the relevant hold indicator must be also filled in. If the T2S Actor sends an already matched Set-
10    tlement Instruction fulfilling “Yes” in the party hold indicator, it can put only the instructed leg on party hold,
11    only the counter-leg on party hold, or both legs on party hold (using the codes PTYH, BOTH or PRCY). For
12   CSD Hold, in already matched Settlement Instructions, only the instructed leg can be put on CSD Hold.

13   A Settlement Instruction on Hold can only be released when the relevant T2S Actor that put the instruction
14   on Hold or the relevant CSD sends the corresponding Release Instruction putting “No” in the relevant hold
15    indicator. The T2S Actor only needs to include this change in the Hold/Release Instruction.

16    In addition to the indicators that can be filled by the T2S Actors, there are three hold indicators that T2S
17    puts automatically:


                                                                                            Page 286 of 2017



[PDF page 287]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1         l CSD Validation Hold;

 2         l  Party Hold 196

 3         l CoSD Hold.

 4    In case of a Settlement Instruction put on Hold by T2S due to a CSD Validation Hold, it can only be released
 5   by the relevant CSD that defined the rule (See section Business Validation [ 218]).

 6    Settlement Instructions that fulfil a CoSD rule are put on CoSD Hold on the Intended Settlement Date until
 7     all the involved Administering Parties send their CoSD Release Instructions. (See section Conditional Settle-
 8   ment [ 452]).

 9   The different types of Hold statuses are independent, so T2S allows different T2S Actors to hold Settlement
10    Instructions (i.e. T2S Party Hold and CSD Hold). Nevertheless, T2S does not allow T2S Actors to put on Hold
11    Settlement Instructions already identified as CoSD (See section Conditional Settlement [ 452]). In case a
12    Settlement Instruction is put on Hold before it is identified as CoSD (e.g. Party Hold), the instruction is put
13   on CoSD Hold (and the T2S Actor is informed on the hold status of the instruction) but the CoSD blocking
14    cannot take place until the T2S Actor or CSD sends the relevant Release Instruction.

15   T2S considers an Instruction on Hold and consequently not eligible for settlement when at least one of the
16    four statuses (Party Hold, CSD Hold, CSD Validation Hold or CoSD Hold) is put to “Yes”.

17    In case the Settlement Instruction is under Partial Release Process it will remain on Hold (Party Hold). How-
18    ever T2S considers it eligible for settlement but only when Partial Settlement is allowed.

19   The different scenarios for a Settlement Instruction regarding the hold process are described in the table
20    below:

21                    TABLE 62 - HOLD /RELEASE EXHAUSTIVE SCENARIOS FOR A SETTLEMENT INSTRUCTION
22

                                        SETTLEMENT INSTRUCTION

             PARTY HOLD      CSD HOLD    CSD VALIDATION   COSD HOLD             RESULT
                                          HOLD



        1      NO         NO         NO         NO          Eligible for settlement

        2       YES           YES           YES           YES      No settlement attempt can be
                                                                                 performed

        3       YES           YES           YES         NO      No settlement attempt can be
                                                                                 performed

        4       YES           YES         NO         NO      No settlement attempt can be
                                                                                 performed


     _________________________


        196    Party Hold indicator can be i) instructed by the T2S actor ii) put automatically by T2S upon the fulfilment of a restriction type case 1 or, iii) put
                 automatically by T2S if it has not been set and the “Hold Release Default” value of the Securities Account included in the instruction is set to
                 “Hold”.


                                                                                            Page 287 of 2017



[PDF page 288]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                               Application Processes Description


                                       SETTLEMENT INSTRUCTION

            PARTY HOLD      CSD HOLD    CSD VALIDATION   COSD HOLD             RESULT
                                         HOLD



       5       YES         NO         NO           YES      No settlement attempt can be
                                                                                performed

       6      NO         NO           YES           YES      No settlement attempt can be
                                                                                performed

       7      NO           YES           YES           YES      No settlement attempt can be
                                                                                performed

       8      NO           YES         NO         NO      No settlement attempt can be
                                                                                performed

       9       YES         NO         NO         NO      No settlement attempt can be
                                                                                performed 197

      10      NO         NO           YES         NO      No settlement attempt can be
                                                                                performed

      11       YES         NO           YES         NO      No settlement attempt can be
                                                                                performed

      12      NO           YES           YES         NO      No settlement attempt can be
                                                                                performed

      13       YES           YES         NO           YES      No settlement attempt can be
                                                                                performed

      14      NO           YES         NO           YES      No settlement attempt can be
                                                                                performed

      15       YES         NO           YES           YES      No settlement attempt can be
                                                                                performed

      16      NO         NO         NO           YES      No settlement attempt can be
                                                                                performed

                                                                   No Party / CSD Hold is allowed.

1     If an Instruction remains on Hold at the end of its Intended Settlement Date, T2S recycles the instruction
2    following the T2S recycling rules (See section Instructions Recycling [ 296]).

    _________________________


       197   No settlement attempt can be performed unless the Settlement Instruction is under Partial Release Process and Partial Settlement of Settlement
                Instructions under Partial Release Process is allowed (i.e. Real Time Settlement or Sequence X of Night Time Settlement is running) (see section
                 Partial Settlement [ 343]).


                                                                                          Page 288 of 2017



[PDF page 289]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.6.3 Hold process

 2    After a T2S Actor sends a Hold Instruction, T2S proceeds to execute it, once checked that the referenced
 3    Settlement Instruction is not:

 4         l  Cancelled;

 5         l  Settled;

 6         l  Identified as a CoSD;

 7         l  Already put on Hold by the relevant T2S Actor (i.e. T2S Party or CSD).

 8     If the Referenced Instruction fulfils any of these conditions, the Hold Instruction is denied.

 9    In case of successful execution, the T2S Actor is informed through a message communicating the execution
10    of the Hold Instruction and a Status Advice message as described in section Send Hold/Release Instruction.
11    Interested parties can also be informed depending on their message subscription preferences (see Section
12    Status Management [ 653] and Section Message subscription [ 135]).

13    In case of already matched Hold Instructions, the status reporting derived from the lifecycle of each Hold
14    Instructions created in T2S is handled separately. Nevertheless, the T2S Actor may subscribe to the notifica-
15    tions of one of the two legs of the already matched Hold Instruction only.

16    Only on the Intended Settlement Date and if the instruction is still on Hold, the Counterparty is informed (at
17    the start of day) on the hold status of the instruction.

18                                        EXAMPLE 78 - HOLD INSTRUCTION

19    This example illustrates the execution of two different Hold Instructions for the Settlement Instruction “X”,
20    which is matched with Settlement Instruction “Y”, before the Intended Settlement Date:

21   The T2S Party of instruction “X” sends a Hold Instruction for Party Hold. T2S validates the instruction suc-
22    cessfully and proceeds to hold the referenced Settlement Instruction putting “Yes” in its Party Hold indicator.
23   The execution of the Hold Instruction and the Status Advice of the Settlement Instruction are notified to the
24   T2S Party and other interested parties, depending on their message subscription preferences.

25   The CSD of instruction “X” sends a Hold Instruction for CSD Hold. T2S validates the instruction successfully
26   and proceeds to hold the referenced Settlement Instruction putting “Yes” in its CSD Hold indicator. The exe-
27    cution of the hold instruction and the Status Advice of the Settlement Instruction are notified to the CSD and
28    other interested parties, depending on their message subscription preferences.

29   As a consequence on the execution of both Hold Instructions, Settlement Instruction “X” turns from scenario
30   1 to scenario 4 in Table above.





                                                                                            Page 289 of 2017
EXCERPT (§1.6.1.6.5–1.6.1.6.6 partial release conditions; PDF 292–295):
1.6.1.6.5 Hold/Release Default for Settlement Instructions

 8   When a T2S Actor sends a Settlement Instruction, T2S checks if the Settlement Instruction has the Party
 9    Hold status set (i.e. hold indicator has value “Yes” or “No”) or not.

10    In case the Party Hold status is not set, T2S checks in Reference Data the “Hold Release Default” value of
11    the Securities Account included in the Instruction 198:

12         l   If the “Hold Release Default” value of the Securities Account is set to “Yes”, the instruction is set auto-
13        matically On Hold through the Party Hold Status (i.e. T2S sets the value of the “Party Hold” status to
14        “Yes”) and the T2S Actor is informed through a Status Advice on the acceptance of the instruction and
15       the Party Hold status “Yes”.

16         l  In case the “Hold Release Default” value of Securities Account is set to “No”, the instruction is not set
17        automatically On Hold.

18   The “Hold Release Default” check is performed only once, upon the first validation of an instruction received
19    from a T2S Actor (i.e. it is not performed at revalidation process).




     _________________________


  
[BUNDLE TRUNCATED AT 160000 CHARACTERS — say so in the answer and do not infer omitted content]