QUESTION FROM THE USER:
Explain market claims at Monte Titoli: when are CLAI instructions generated, and can they be partially settled?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.499922+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-partial-settlement]] — Partial settlement conditions, thresholds and procedure (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Cash-value thresholds are configured per currency by the T2S Operator; actual values are not in this excerpt.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345):
1.6.1.9.3 Partial Settlement

 2   Concept

 3   T2S provides partial settlement process, i.e. settles only a fraction of the original quantity or amount when
 4     full settlement is not possible due to lack of securities or cash, in order to increase the volume and value of
 5    settlement.

 6   Overview

 7     Partial settlement applies under conditions and procedures that differ whether they apply to:

 8         l  Settlement Instructions;

 9         l  Settlement Restrictions;

10         l  Liquidity transfers.

11    Partialsettlementprocess

12     Partial settlement process for Settlement Instructions

13   A Settlement Instruction is partially settled 224, in case there are insufficient securities to settle the full quan-
14     tity and provided the following conditions are met:

15         l  The partial settlement window is currently running; 225

16         l  The Settlement Instructions are eligible to settle partially;

17         l  The partial settlement threshold criteria are fulfilled.

18    Partial settlement window

19     Partial settlement is active in T2S within the dedicated partial settlement windows 226.

20    Partial settlement eligibility

21   The settlement eligibility depends notably on conditions set by the T2S parties on their matched Settlement
22    Instructions.

23   A matched pair of Settlement Instructions is eligible to partial settlement, when these Settlement Instruc-
24    tions are entered by the T2S parties with the following characteristics:

25         l  They are related to Free Of Payment or to Delivery Versus Payment or Delivery With Payment; 227

26         l  The partial settlement indicator is not set to "No" in any of the Settlement Instructions;

27         l  They are not linked to any other Settlement Instruction or Settlement Restriction by the T2S parties by a
28         link type “Before”, “After” “With” or by a pool reference.

     _________________________


        224    Partial settlement is triggered only in case of lack of securities (i.e. lack of securities only or lack of securities and cash) but not in case of lack of
               cash only.

        225    Partially released Settlement Instructions can be submitted for settlement attempts for the total partially released quantity also when the partial
                settlement window is not running. Partially released Settlement Instructions can be submitted for settlement attempts for a part of the partially
                released quantity only when the partial settlement window is running.

        226   For details about the schedule of partial settlement window, see section Settlement Day [ 155]

        227    Including such Settlement Instructions which are on Party Hold and have been partially released.


                                                                                            Page 343 of 2017



[PDF page 344]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1     Partial settlement of Partially Released Settlement Instructions

 2   A Settlement Instruction on Party Hold may be partially released to allow the partial settlement of a specified
 3    quantity. This Partially Released Settlement Instruction must conform to all the conditions of partial settle-
 4   ment as for any other Settlement Instruction. During the real-time period the partial settlement of Partially
 5    Released Settlement Instructions can occur outside a partial settlement window for the total partially re-
 6    leased quantity, as well as during a partial settlement window for the total or part of the partially released
 7    quantity and until the relevant cut-off time (partial release is only valid for the current business day) at
 8    which point the partial release will be cancelled and the underlying Settlement Instruction set back on Party
 9    Hold for the full unsettled quantity. For partial release to be considered during sequence C2SX of the night
10    time settlement the partial release must occur as of the start of day.

11    Partial settlement threshold

12     Partial settlement is conditioned by thresholds, below which it cannot apply, and that are determined in T2S
13   when the settlement occurs, on the basis of the following content of the Settlement Instructions:

14         l  The instruction type (FOP or DVP or DWP);

15         l  The instruction threshold type (see table below);

16         l  The underlying ISIN;

17         l  The currency of the cash amount of the Settlement Instruction.

18   These contents of the Settlement Instructions allow T2S to determine the type of partial settlement thresh-
19    old applicable on the Settlement Instructions being processed. The following types of partial settlement
20    thresholds are possible:

21         l A threshold in “quantity”: meaning the partial settlement cannot take place for a quantity lower than an
22        applicable value;

23         l A threshold in “cash value”: meaning the partial settlement cannot take place for an amount lower than
24      an applicable value.25





                                                                                            Page 344 of 2017



[PDF page 345]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                            TABLE 68 - APPLICABLE THRESHOLD TYPES FOR PARTIAL SETTLEMENT
 2

               CONTENT OF SETTLEMENT INSTRUCTION            RESULTING     RESULTING APPLICABLE
                                                                 APPLICABLE      THRESHOLD VALUE
       INSTRUCTION     INSTRUCTION         ISIN     CURRENCY
                                                         THRESHOLD
           TYPE       THRESHOLD TYPE
                                                                 TYPE

      FOP 228          n/a                     applicable    n/a          Quantity    Minimum settlement unit (only for
                                                                                                                         first partial settlement) and set-
     DVP/DWP        Set to “Quantity” for
                                                                                      tlement unit multiple are used.
                       both matched Settle-
                     ment Instructions

     DVP/DWP        Not set to “Quantity”   Unit-quoted  applicable    Cash value   Amount configured in the currency
                             for both matched Set-                                              specified (for quantity, minimum
                        tlement Instructions                                            settlement unit and settlement
                                                                                                  unit multiple are used).

                                             Nominal-                          Amount configured in the currency
                                            quoted                                     specified (for quantity, minimum
                                                                                        settlement unit and settlement
                                                                                                  unit multiple are used).

 3   The parameters determining the threshold applicable above are set:

 4         l  By T2S Actors from the content of their Settlement Instructions for the instruction type and instruction
 5        threshold type mentioned in the table above;

 6         l  By the T2S Operator inside the Static Data for the applicable threshold in cash value. This parameter is
 7      common to all T2S Parties, and set per T2S settlement currency, and separate for unit-quoted or nomi-
 8        nal quoted ISIN;

 9         l  By the T2S Actors in charge of the administration of the relevant ISIN in the Static Data for the applica-
10        ble threshold in quantity (See section Concept of securities in T2S [ 71]).

11    Partial settlement procedure

12    Settlement Instructions are submitted to a full settlement attempt before being submitted to a partial set-
13    tlement attempt. 229

14    In case the Settlement Instruction does not settle, the Settlement Instruction is submitted to Optimising
15    application process. The Optimising application process tries to settle the failed Settlement Instruction with
16    other Settlement Instructions in T2S based on different technical optimisations. In case the Optimising appli-
17    cation process is not able to find a solution for a full settlement, T2S tries to submit the Settlement Instruc-
18    tion for partial settlement provided the above conditions are met.

     _________________________


        228   Cash value thresholds are not considered for FOP regardless of the partial settlement threshold type (partial settlement indicator PARC, PART)
                defined within the settlement instruction. This also applies for FOP instructions related to a foreign currency transaction (non-EUR amount).

        229    Partially Released Settlement Instructions are only submitted to partial settlement attempts for the released quantity.


                                                                                            Page 345 of 2017

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_market_claims_transformations"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-caof]] — Corporate actions on flow: market claims and transformations (§1.4) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §1.4 including footnotes 4–5; PDF 17–25, printed 13–21 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Buyer protection references market practice and market/CCP rules, which are not admitted.
EXCERPT (§1.4 including footnotes 4–5; PDF 17–25, printed 13–21):
1.4 MANAGEMENT OF OPERATIONS IN CASE OF CORPORATE
EVENTS (CD CORPORATE ACTION ON FLOW)

The management of unsettled transactions in financial instruments of corporate
actions includes the following processes based on the corporate event on the
financial instrument:

    a) Management of Market Claim

    b) Management of Transformation

The management of these processes is available only through X-TRM.

The management process of Market Claim allows to recognize to the receiving
counterparty in an unregulated transaction (fail) the income distributed as part
of a corporate action relating to the securities subject to the transaction in fail.

The management process of Transformation allows to recognize to the receiving
counterparty in an unregulated transaction (fail), the securities or the proceed
resulting as part of a corporate action relating to the securities subject to the
transaction in fail.

The management processes of Market Claim & Transformation are not available if
the regulation underlying transaction involving a CSD outside T2S (cd external
settlement) and in cases where the corporate operation is not managed within
the Monte Titoli systems. In this latter case, participants must provide for the
management of Market Claims and Transformation by deleting the fail settlement
instructions and entering the corresponding settlement instructions, in line with
the procedures described below.

The Settlement  Service  operates  solely Market Claim & Transformation  in
currencies allowed in T2S and cleared on the same cash account on which the
settlement of the pending transaction is provided4.

Both processes require identification by Monte Titoli - according to specific rules
for each process - of transactions in financial instruments which may result in a
Market Claim or a Transformation (cd pending transactions).

The  identification process  is  carried out  at the  close  of Operating Day  of
Settlement Service and before the stage night-time settlement (NTS).





4 Where necessary, the countervalue of the CLAI instruction is calculated on the basis of the exchange rate fixing of the ECB
recorded at the record date.





13



[PDF page 18]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The management processes of Claim Market and Transformation apply to  all
types of transactions processed by the Settlement Service except instructions
realignment generated automatically by T2S.

The  Participants, markets and  central  counterparties may  exclude  certain
transactions from the management process of Market Claim or Transformation,
valuing the appropriate indicator OPT-OUT.


1.4.1 Market Claim

    •  Operations that originate a Market Claim

The process of managing the Market Claim  is executed when the following
corporate transactions (cd. Distributions) occurs:

    •  Payment of dividends (including mixed dividends);
    •  payment income units of closed-end funds;
    •  coupon payment ;
    •  free share allocation;
    •  option rights assignment (related to capital increase free or paid)
    •  reimbursement with pool factor.

The transaction giving rise to the Market Claim are identified according to the
following rules.

For  transactions  involving  financial instruments denominated  in  units  (e.g.
Shares and similar securities)

   Monte Titoli identifies relevant transactions:

    •   for  transactions coming from guaranteed  or non-guaranteed market,
      according to the EX-date established according to the trading calendar of
      the markets. All contracts negotiated by the end of the accounting day
      previous  of  the  EX-date (ED-1)  relate  to  securities CUM.  Contracts
      negotiated from the EX-date relate to securities EX,
    •   for transactions concluded OTC according to the CUM or EX indicator
      entered by the counterparties, for the management of Market Claim. In
      that case is not taken into account the trading date for the identification of
      pending transactions.

   In this context, the transaction giving rise to Market Claims are:

    a) matched and not settled by the Record Date;





14



[PDF page 19]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





    b) not matched  at the Record Date, but matched  within the period  of
       identification;
    c) submitted to the T2S system after the Record Date, referred to securities
     CUM, and matched within the period of identification.

For transactions involving bonds and similar securities ("nominal")


   The Market Claim are only generated for transactions with the Intended
   Settlement Date preceding or coinciding with the Record Date and not settled
   by that date.

The  Market  Claim  are  also  generated  by  transactions  involving  financial
instruments traded EX and settled before the Record Date (cd. Reverse Market
Claim), unless such operations bear an indicator CUM. In this case the gain is
recognized to the deliverying party.

The process of managing the Market Claim can be excluded according to the
rules specified:

    •  by the markets, for all transactions therein negotiated if not guaranteed by
       central counterparties;
    •  by the CCP for all guaranteed transactions;
    •  by the Participants for each OTC contract.

The operations that bear the indicator "OPT-OUT = Y" are excluded from the
management of Market Claim or Claim Reverse Market.

    •  Timing of identification process

Monte Titoli identifies the Settlement Instructions potentially subject to Market
Claim, cd. pending operations, from the Record Date of the corporate action for
the twenty following Settlement Service Operating Days(RD+20).

The identification process is repeated daily with batch mode at the same time,
for the duration of the period of the identification (detection period), in order to
verify the  possible change  of  state (from "unmatched  "  to "matched")  of
contracts involving securities CUM unmatched on Record Date (as evidence
produced to the same Record Date), or to identify any transactions entered after
the Record Date but with Trade Date before Ex Date (or indicator CUM = Yes) .

    •  Generation of the settlement Instructions  for the management of the
      Market Claim





15



[PDF page 20]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Settlement Instructions generated for the management of Market Claim are
coded as ‘’CLAI’’.

The process of generating Market Claim will not erase the original operation in
fail.
At the Record Date Monte  Titoli download data of matched transactions not
settled at that date. CLAI Settlement instructions are generated before the
beginning of the night time settlement cycle.

Pending transactions unmatched at Record Date generate Market Claims at the
end of the day in which they are matched (before the end of the detection
period).

For the purposes of the reconciliation process, the instruction "CLAI" contains at
least the following information:

    ▪  Participant's ID counterpart in the transaction that generates the Market
      Claim;
    ▪  the identification of the transaction that generates the Market Claim;
    ▪  the identifier of the corporate action , as assigned by the Issuer CSD;
    ▪  the trade date, Trade Date (TD), coinciding with the Trade Date of the
       original transaction;
    ▪  the  Intended  Settlement Date  (ISD),  coinciding  with  the  scheduled
     payment date of the corporate action;
    ▪  the value or the amount of financial instruments covered by the Market
      Claim5.
    ▪  the same  indicator  of  the  original  transaction  for  partial  settlement
       (applicable only in case of Market Claim on financial instruments because
      the Market Claim for cash amounts can not be partially settled);
    ▪  the same status on-hold / released of the original transaction whatever is
      the origin of the transaction (the market, CCP, OTC). Participants in the
      event of a change of the status of the original transaction are expected to
     change in the same way the status of the CLAI transaction.


CLAI Instructions relating to unsettled transactions intra-CSD are matched from
the time of generation.


5 For corporate action involving the payment of monetary amounts (called cash distribution), the countervalue of the Market
Claim is equal to the product of the quantity of shares / nominal value of the securities of the original transaction, multiplied by
the unitary value of the corporate action (gross dividend amount per unit; interest rate).

For transactions involving the allocation of financial instruments (called securities distribution) the amount of shares / nominal
value of financial instruments of CLAI instruction is equal to the amount of shares / nominal value of the original transaction,
multiplied by the number of financial instruments distributed, according to the ratio established by the issuer.




16



[PDF page 21]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





CLAI Instructions concerning transactions to be settled cross-CSD are forwarded
by Monte  Titoli to the T2S platform for the purposes of matching with the
settlement instruction generated by the CSD of the counterparty of the Monte
Titoli Participant.

CLAI Instructions related to OTC transactions can be deleted by Participants
according to the with the rules and the general conditions applicable to OTC
settlement  instructions,  while those  relating  to guaranteed  transactions  or
Market transactions are canceled by Monte Titoli according to the Markets or the
Central Counterparties request.

Central Counterparties can be counterpart in withdrawal or delivery of Market
Claim.

    •  Market Claim Settlement


The Market Claim for payment of amounts in cash can not be partially settled.

The Market Claim on financial instruments can be partially settled.

Settlement of CLAI instructions can not be connected to other CLAI instructions
(linkages).

CLAI instructions can not be included in a pool".


    •  Market Claim in connection with corporate events with Antedated Record
      Date


If during the period of identification of pending transactions the system detects:

   a) details of a new corporate event whose Record Date coincides with a date
       earlier than the current; or
   b) the change of the Record Date of a corporate event already known by the
      system, anticipated to the current date;

Monte Titoli automatically manages the Market Claim according to the state of
the underlying at the close of the accounting day coinciding with the new Record
Date.

Particularly in the case a), Monte Titoli detected the corporate event Record Date
in the past but within the detection period:

    ▪  For unmatched pending transactions at the Record Date (in the past)
      generates the Market Claim only  if the matching occurs subsequently to





17



[PDF page 22]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





      the Record Date and until the Accountig Date of the corporate action
      detection;
    ▪   for all operations settled at the Record Date (in the past), but traded from
      the Ex Date, Monte Titoli generates the Reverse Market Claim.

In the case b) Monte Titoli manages the Market Claim according to general rules,
provided that the backdating of the Record Date is within the detection period.

All other cases of modification of the Record Date:

    ▪   will be managed by manually according to what  is communicated via
     messaging service or equivalent;
    ▪    it is up to the Participants to act on the Market Claim already generated.

    •  Reporting to Monte Titoli Participants

Reporting related to the process of managing Market Claims, is made available
via the X-TRM for Participants ICP.

DCP Participants will receive the information produced by the T2S platform, as it
is provided  for information  relative to  all other transactions settled by the
Settlement Service.


For Participants that use RNI messaging, Monte Titoli will send the notification
message 7B2 of the generation of CLAI instruction (message type forecast).



1.4.2 Transformation

Monte  Titoli manages the process  of creating Transformations  of corporate
mandatory transactions (mandatory reorganization with or without options) or
voluntary (limited to the only or last period of the year and for which applies the
default option), such as:

    ▪  Total or partial reimbursement of the securities;
    ▪  exercise option right (as part of a capital increase for a fee, free or
      mixed);
    ▪  exercise of warrants (single or last exercise period);
    ▪  compulsory and optional conversion (last conversion period)
    ▪  groupings, splits, mergers and demergers.

Monte Titoli does not automatically manage the cancellation and Transformation
for the voluntary corporate event (voluntary reorganization).





18



[PDF page 23]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The Transformation are generated by transactions matched but not settled
before the Record Date (cd. Operations pending).

Monte Titoli proceeds to identify settlement instructions potentially subject to
Transformation, from the Record Date of the current corporate action until the
20th Business Day after the record date (RD+20).

▪  Timing of identification process

Monte Titoli proceeds to identify settlement instructions potentially subject to
Transformation, from the Record Date of the current corporate action until the
20th Business Day after the record date (RD+20).


The identification process is repeated daily in batch mode at the same time, for
the entire duration of the identification period (detection period), in order to
verify any change in the status (from "unmatched" to "matched") of transactions
involving that were still not matched at the Record Date.


▪  Generation  of  the  Settlement  Instructions  for  the management  of  the
   Transformation

The process  of managing Transformations  involves the  cancellation  of the
Settlement Instruction related to the original transaction and the enter of a new
Settlement Instruction (TRAN).

Unmatched pending transactions at the Record Date generate Transformation at
the close of the accounting day on which they are matched if this occurs within
the detection period.

In the case of mandatory corporate events that do not provide the exercise of
options in favor of persons entitled to participate, Monte  Titoli automatically
deletes the  original settlement instructions transaction  in  fail and enter the
Instruction TRAN.

In the case of mandatory corporate events that allow the exercise of an option to
the parties entitled to participate,  it is up to the counterparties of the original
transaction in  fail to delete  it and enter a settlement instruction which terms
must reflect the Buyer Protection. For the management of Buyer Protection it has
to make reference to the market practice for OTC transactions, and to the rules
of the Markets and of the CCPs respectively for unguaranteed and guaranteed
market transactions.

In the absence, Monte Titoli at the Market Deadline performs the process of
Transformation according to the default option provided by the Issuer.




19



[PDF page 24]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In the case of voluntary corporate actions, it is up to the original counterparties
in fail to delete and reinsert the settlement instruction. In the absence Monte
Titoli does not perform the process of Transformation.

TRAN instruction must include at least the following information:

    ▪  Reference to the counterparty of the pending transaction that generates
      the Transformation;
    ▪  The  identification  of  the  pending  transaction  that  generate  to  the
      Transformation
    ▪  The identification of the corporate action in progress
    ▪  The Trade Date, coinciding with the Trade Date of the pending transaction;
    ▪  The Settlement Date, that is the higher between the Intended Settlement
      Date of the pending transaction and the date of execution of the corporate
      event;
    ▪  the ISIN code of the new instruction is the same of the security distributed
      from the corporate event, according to the report established by the
      Issuer;
    ▪  indicator on-hold / release and partialisation equal to those of the pending
      operation.

In the event that the corporate event provides the recognition  of multiple
securities, for each security will be created an instruction TRAN. In this case  if
the original transaction was DVP, the value of the transaction will be split a
number of new DVP instructions corresponding to the number of the TRAN
operations arising from the Transformation. The value of each DVP  transaction
will be proportional to the amount / nominal value of the financial instruments
referred to each TRAN instruction.

In the event of option rights resulting from capital increases, on the Market
Deadline Monte Titoli shall cancel the original settlement instruction and shall
enter a PFOD instruction in which the participant, previously in delivery of the
right, recognizes to the counterpart an amount equal to the countervalue of the
cancelled transaction.

In the event that the corporate event provides only the recognition of a cash
amount (e.g. total reimbursement), the pending transaction it is cancelled and
replaced by two TRAN instructions, one for the countervalue of the pending
transaction and one  for the value  for the reimbursement  of the  financial
instrument  (for the possible recognition  of the coupon please  refer to the
procedure of the management of the Market Claim).

TRAN  Instructions  generated  against  unsettled  transactions  intra-CSD  are
matched from the time of generation.





20



[PDF page 25]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





TRAN Instructions generated against transactions to be settled cross-CSD are
forwarded by Monte Titoli to the T2S platform for the purposes of matching with
the settlement instruction generated by the CSD of the counterparty of the
Monte Titoli Participant.

TRAN  Instructions related to OTC transactions can be deleted by Participants
according to the  rules and the general conditions applicable to other OTC
settlement  instructions,  while those  relating  to guaranteed  transactions  or
Market transactions are canceled by Monte Titoli according to the Markets or the
Central Counterparties request.

TRAN instructions can not be connected to each other, or be part of a pool.

TRAN instructions can bear the information that the original operation was linked
to other instructions, but it does not bear the ID of the linked one.

▪  Reporting to Monte Ttitoli Participants

The reporting relating to the management of Transformation is avaible trough X-
TRM Service for the ICP Participants.

DCP Participants will receive the information produced by the T2S platform, as it
is provided for all the others transactions settled by the Settlement Service