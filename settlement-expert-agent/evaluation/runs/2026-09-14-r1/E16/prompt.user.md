QUESTION FROM THE USER:
Under T2S release R2026.NOV, what does the UDFS say about the building blocks of the sese.023 settlement instruction?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:02:55.170572+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_message_sese023_scope", "release": "R2026.NOV"}
STATUS: blocked — Requested release does not match the reviewed platform evidence.
GAP IDS: ['G15']

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "native_message_overview", "release": "R2026.NOV"}
STATUS: blocked — Requested release does not match the reviewed platform evidence.
GAP IDS: ['G15']

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_message_sese023_scope", "release": "R2026.JUN"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "native_message_overview", "release": "R2026.JUN"}
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

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "release_status", "release": "R2026.NOV"}
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

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "november_text_comparison"}
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

=== RETRIEVAL 7: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "future", "question_type": "milan_t2s_release_plan_nov"}
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