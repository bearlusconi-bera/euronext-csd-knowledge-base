QUESTION FROM THE USER:
Porto's operational manual says the FOP cut-off is 17:00. Isn't the T2S FOP cut-off 18:00? Which is right?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.735700+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_windows_and_cutoffs"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-rts-phase]] — Real-time settlement period: five partial settlement windows and cut-off structure (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.4; PDF 193–194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Window times are the R2026.JUN baseline (08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, 15:30 to 16:05 or DVP cut-off closure); some cut-offs are currency dependent.
LIMITATION: A supplied business date requires a reviewed event overlay; a nominal question must say so explicitly.
EXCERPT (§1.4.4.4; PDF 193–194):
1.4.4.4 Real-time settlement (RTS)

 4    This section presents the real-time settlement processes in the T2S settlement day. The real-time settlement
 5    period starts after the end of the night-time settlement and is followed by the end of day period.

 6    In case the NTS completes before 3.00 from Mondays to Fridays and before 2.30 on Saturdays, real-time
 7    settlement period begins before the start of the maintenance window.

 8   The real-time settlement period includes:

 9         l  The real-time settlement preparation;

10         l  The real-time settlement with the five partial settlement windows to optimise maximum value and vol-
11      umes of settlement transactions, which are unsettled because of lack of securities:

12      – The first partial settlement window between 08:00 and 08:30;

13      – The second partial settlement window between 10:00 and 10:15;

14      – The third partial settlement window between 12:00 and 12:15;

15      – The fourth partial settlement window between 14:00 and 14:15;

16      – The fifth partial settlement window is 30 minutes before the beginning of the DVP cut-off time, then
17         between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first).

18   The previously unsettled Settlement Instructions and Settlement Restrictions from night-time settlement are
19    attempted for settlement in the real-time settlement period with the arrival of new resources (securities for
20    delivery, securities in positions earmarked available for collateral, cash). 143 Additionally T2S performs a set-
21    tlement attempt for any new intraday Settlement Instructions, Settlement Restrictions and liquidity transfers
22    validated and accepted during real-time settlement period;

23         l  The real-time settlement closure with different cut-offs and events for different Settlement Instructions,
24       Settlement Restrictions and liquidity transfers categories.


     _________________________


        143   During the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been at-
               tempted for settlement. This serialization process will concern all transactions with age >= 3 selected by the Regular Recycling process following a
                   credit in securities or cash or an increase in CMB headroom or limit, guaranteeing that an older transaction will be attempted before a younger one
                with the same priority. The transactions selected by one given recycling process will be segregated into eight groups, depending on their priority
              and age:

               Group 1         Group 2         Group 3         Group 4         Group 5         Group 6         Group 7         Group 8
                    Priority 1           Priority 1           Priority 2           Priority 2           Priority 3           Priority 3           Priority 4           Priority 4
              Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3        Age >= 3       Age < 3
               Should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to
                the regular recycling process.


                                                                                            Page 193 of 2017



[PDF page 194]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l Some of these cut-offs and events may be currency dependent.

 2    For the ease of presentation, the real-time settlement period is shown in two parts:

 3         l  The real-time settlement;

 4         l  The real-time settlement closure.

 5   The real-time settlement period also includes processes specific to the penalty mechanism. These are com-
 6    prised of the processing of information received within T2S including securities subject to penalties infor-
 7    mation, penalty modification requests and daily and historic prices for penalties. This information is subse-
 8    quently used for penalty calculations and reporting.


 9

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_instruction_registration"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-rts-registration]] — Real-time settlement system: instruction types, channels (STD/SWIFT/ISO 20022), references, SF1/SF2 and matching tolerance (§§12–12.1) (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Operational Manual of INTERBOLSA | Chapter 12 opening and §12.1; PDF 116–120, printed 115–119 | version Operational Manual V43. Internal date 26 January 2026; filename 16 February 2026; posted April 2026. | body language en | authoritative language pt | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf
LIMITATION: English version of the Operational Manual V43 (internal date 26 January 2026); Portuguese text governs and the manual's operative effective date is unresolved.
LIMITATION: Tolerance values are on the website, not in the excerpt.
EXCERPT (Chapter 12 opening and §12.1; PDF 116–120, printed 115–119):
CHAPTER 12.  SETTLEMENT OF TRANSACTIONS - REAL TIME SETTLEMENT SYSTEM
                    (cf. Articles 40 to 47 INTERBOLSA Regulation No 2/2016)



EURONEXT SECURITIES PORTO Real Time Settlement system processes the registration, matching

and respective settlement of purchase and sale transactions (OTC - Over the Counter), primary

market transactions, among others.

The Real Time settlement system allows the settlement of the following types of instructions:

    • DVP - Delivery versus Payment;

    • FOP - Free of Payment;

    • DWP - Delivery with Payment;

    • PFoD - Payment Free of Delivery.



Some of the features available in the settlement system are:

    • Suspension of settlement (Hold);

    • Full or partial release of the suspension of settlement (Release);

    • Partial Settlement (in the night-time settlement cycle and during the day at defined times);

    • Links between settlement instructions;

    • Settlement priority setting;

    • Amendment: partial settlement indicator, priority indicator and instruction link;

    • Cancellation of settlement instructions.



Settlement of instructions takes place on the T2S platform, physical settlement takes place in the

participants' securities accounts and financial settlement takes place in the cash accounts (DCAs),

for eligible currencies in T2S, currently the Euro and Danish Krone - DKK ( 1).

In the case of transactions with a financial component in a currency other than the euro that is not

eligible in T2S, physical settlement takes place in T2S, but financial settlement takes place in the

Foreign Exchange Payment System (SPME). More detailed information on the SPME can be found

in the chapter on the "Foreign Currency Settlement System".

Direct participants (DCPs), i.e. EURONEXT SECURITIES PORTO participants with direct access to

the T2S platform can send settlement instructions directly to the T2S platform, either via ISO 20022




( 1) Since October 2018


Operational Manual                                                                        2026-01-26            Page 115



[PDF page 117]

messages or via the T2S GUI. On the other hand, participants with indirect access to the T2S

platform (ICPs) send the instructions to EURONEXT SECURITIES PORTO through files or messages:

    • Via STD: via messages - SLRTmsg or via SLRTfile; or

    • Via ISO 15022- MT530/MT540/MT541/MT542/MT543 messages.



Information on the settlement/status of the instructions is made available:

    ▪ Via STD:

         o  SLRT-PND - this file is available before the start of night-time settlement in T2S

            (NTS)  and  contains  information  on  the   instructions  that  are  pending

              confirmation/settlement (unmatched and matched status);

         o  SLRT - message available during the whole settlement day and containing the

              information of the unmatched, settled, matched, cancelled and rejected instructions;

         o  SLRT-RES - a file available after the end-of-day (EOD) in T2S containing information

            on settled and cancelled instructions during the day;

         o  SLRTqryS - query that allows obtaining all information on settlement instructions

             through the messages "SLRTinfo" and "SLRTdet" - see Chapter 19 - "Interactive

            Data Query - STD").

    ▪ Via SWIFT for participants who have subscribed to ISO 15022 messages:

            •  MT536 (Statement of Transactions);

            •  MT537 (Statement of Pending Transactions);

            •  MT544/MT545/MT546/MT547 (Settlement Confirmation);

            •  MT548 (Settlement Status and Processing Advice).



DCPs, in addition to the information available via the STD, may receive settlement information

directly from T2S:

         o  Through ISO 20022 messages:

                    •  semt.017 (Securities Transaction Posting Report);

                    •  semt.018 (Securities Transaction Pending report);

                    •  sese.024 (Securities Settlement Transaction Status Advice);

                    •  sese.025 (Securities Settlement Transaction Confirmation);

         o   Through consultation - T2S GUI: Settlement Instructions.



Operational Manual                                                                        2026-01-26            Page 116



[PDF page 118]

12.1 REGISTRATION OF SETTLEMENT INSTRUCTIONS



The operating schedule of the systems and respective timetables are available in Chapter 4 -

"Schedule and Timetables".

    ▪ The introduction of the instructions must be carried out by a participant  affiliated to

     EURONEXT SECURITIES PORTO and empowered to physically and financially settle the

       operations:

     o  by DCPs directly in the T2S platform, including CCPs (Central Counterparties);

     o  By ICPs and, when required, by DCPs, through the local EURONEXT SECURITIES PORTO

        systems. In this case, a pre-validation is performed and the information required for the

        subsequent submission of settlement instructions to T2S is incorporated. The final and

         ultimate validation of the instructions is performed in T2S - Settlement Finality 1 (SF1) -

        accepted;

    ▪ EURONEXT SECURITIES PORTO allows the registration of the following types of settlement

       instructions:

    o  Delivery instructions against payment - DVP:

      DVP - Delivery versus Payment;

      RVP - Receive versus Payment;

    o  Free of payment delivery instructions - FOP:

       DFP - Delivery free of Payment;

       RFP - Receive Free of Payment;

    o  Delivery instructions with payment - DWP:

     DWP - Deliver with Payment;

      RWP - Receive with Payment;

    o  Payment free of delivery instructions - PFD:

       PFD - Payment Free of Delivery (to the delivery and receive).





Operational Manual                                                                        2026-01-26            Page 117



[PDF page 119]

    ▪ Instructions can be entered via STD in two ways:

        o  by sending a file using the mnemonic 'SLRTfile' from the ‘Liquidação’ menu.

           Response messages are received also in the STD using the mnemonic "SLRT";

        o  Through messaging:

                  •  From the participant's own applications to the EURONEXT SECURITIES PORTO

                 system - This form of sending allows participants to have a STP (Straight

                 Through  Processing)  solution,  for  sending  and  cancelling  settlement

                     instructions and receiving messages (acceptance, rejection, matching notice,

                      etc.), which increases the automation of the services provided.

                  Connection by this means with the EURONEXT SECURITIES PORTO system is

                    possible from an application of the participant that has TCP/IP connectivity with

                   the EURONEXT SECURITIES PORTO STD server, using an application protocol

                 based on messages with a defined layout, described and exemplified in the

                    Technical  Manual  (available  in  the STD  "Manuais" menu  - mnemonic

                  STDTecxx).

                    In practice,  this solution consists of  directly connecting the participant's

                     application to the STD system, without using the STD  client application

                   provided by EURONEXT SECURITIES PORTO;

                  •  By the mnemonic "SLRTmsg" from the STD ("Liquidação " menu).

    ▪  The input of instructions may also be carried out via the SWIFT network by means of

      messages in ISO 15022 format:

           o  MT540/MT541/MT542/MT543;

           o  MT530.

          Note: Participants wishing to communicate via the SWIFT network may only do so

             after subscribing to the service and carrying out tests (see the document

            "Subscription to ISO 15022 messages via the SWIFT network", available on the

         EURONEXT SECURITIES PORTO website under " Documentation"/"Operational

           Documentation" https://www.euronext.com/en/post-trade/euronext-securities/porto.

    ▪ The minimum allowed quantity is equal to one security unit (Minimum Settlement Unit - MSU);

    ▪ The introduction of instructions in nominal amount (FAMT) is exclusively allowed for debt

       instruments;

    ▪ FOP (Free of Payment) operations are allowed by entering a zero cash amount in the "Financial

      Amount to be settled" field and " " (blank) in the "Currency" field;

    ▪ The entry of instructions to settle at a future date (forward transactions) is possible;


Operational Manual                                                                        2026-01-26            Page 118



[PDF page 120]

    ▪ Forward transactions are submitted for settlement on the contractual settlement date (ISD -

      Intended Settlement Date), during the night-time settlement period, except if they are in

       the "Hold" state, in accordance with the registration and matching time criterion;

    ▪   All instructions, entered in the systems for settlement purposes, are validated in the

      TARGET2-Securities (T2S) platform, according to the rules of the platform and the mentions

      and static data included by EURONEXT SECURITIES PORTO;

    ▪  If instructions have been registered through EURONEXT SECURITIES PORTO, a registration

      number, (IB Reference) is assigned;

    ▪ Upon acceptance of the registration of an instruction by the T2S platform, the T2S platform

       assigns a registration number, T2S Reference. In the case of instructions sent directly to

       the settlement platform, applicable to DCPs, only the T2S Reference is assigned. The

       numberings/references of the settlement instruction are sequential and can never be

       repeated;

    ▪ Instructions are matched on the T2S platform. When the platform detects two matching

       settlement instructions, it automatically confirms the transaction (matching), and these are

      then ready to be settled through the settlement platform - Settlement Finality 2 (SF2) -

      matched;

    ▪ When the T2S platform matches an instruction, it also assigns a matching number, Matching

      Reference - Settlement Finality 2 (SF2) - matched.



   Matching tolerance

   Two instructions with different financial amounts can match, provided that the amounts are

   within the matching tolerance, in which case the transaction settles with the value indicated by

   the seller.

  EURONEXT SECURITIES PORTO adopts the tolerance values defined by T2S in line with ECSDA

    rules.



   The matching tolerances are available on the EURONEXT SECURITIES PORTO website (link).

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_operating_hours_published"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-operating-hours-web]] — Published operating hours table (T2S-based, CET) with the WET note and reference to Notice 0394/2024 (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Euronext Securities Porto — Working Days & Operating hours (web page, capture of 14 September 2026) | Working Days & Operating hours page, operating-hours section; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/en/post-trade/euronext-securities/porto/about-us/working-days-operating-hours
LIMITATION: Web page reproduction of the T2S schedule; the binding source is Notice 0394/2024 (section porto-timetable) and dated exceptions need event evidence.
LIMITATION: The page's 2025 closing-day list was visible at capture; the 2026 calendar is Notice 25/1162 (section porto-calendar).
EXCERPT (Working Days & Operating hours page, operating-hours section; capture of 14 September 2026):
The operating hours of the centralised systems and settlement systems managed by Euronext Securities Porto are based on the operating hours of the T2S platform – TARGET2-Securities and are set out in the notice no. 0394/2024 Timetables.Schedule T2STime CETStart of Day – SoD Change of business date18:45Preparation for Night Time Settlement18:45 – 20:00Night Time Settlement (NTS) Start of NTS20:00First Cycle, with five sequences Last Cycle, with partial settlement in sequence X Real time Settlement (Starts if the NTS ends before 03:00 CET / 02:00 WET) Maintenance Window in weekday (optional)03:00 – 05:00Maintenance Window from Saturday until Monday (required)02:30 – 02:30Real time Settlement05:00 – 18:00Partial Settlement Cycle 108:00 – 08:30Cycle 210:00 – 10:15Cycle 312:00 – 12:15Cycle 414:00 – 14:15Cycle 515:30 – 16:00DVP (Delivery versus Payment) cut-off16:00Collateral reimbursement16:30BATM / CBO cut-off17:40Inbound LTO cut-off / Automatic cash sweep17:45FOP (Free of Payment) cut-off18:00End of Day – EoD18:00Please Note: Portugal uses WET (Western European Time), which is -1 hour than CET (Central European Time).Acronyms:BATM – Bilaterally Agreed Treasury ManagementCBO – Central Bank OperationsLTO – Liquidity Transfer Orders

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_cancellation_allegement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-cancellation-allegement]] — Cancellation rules, automatic cancellation and allegement timing/messages (§§12.3–12.4) (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Operational Manual of INTERBOLSA | §§12.3–12.4; PDF 132–134, printed 131–133 | version Operational Manual V43. Internal date 26 January 2026; filename 16 February 2026; posted April 2026. | body language en | authoritative language pt | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf
LIMITATION: English version of the Operational Manual V43 (internal date 26 January 2026); Portuguese text governs and the manual's operative effective date is unresolved.
LIMITATION: The FOP cut-off is printed as 17:00 WET here (18:00 CET); time zone conventions differ across Porto documents.
EXCERPT (§§12.3–12.4; PDF 132–134, printed 131–133):
12.3 CANCELLATION OF SETTLEMENT INSTRUCTIONS

        (cf. Article 47 of INTERBOLSA Regulation No 2/2016)



It is possible for participants to cancel:

       ▪ Unilaterally - unmatched instructions;

       ▪ Bilaterally - matched instructions. In this case each of the involved parties has to register

             its cancellation instruction, which will have to match.

  Unmatched instructions (inclusion or cancellation), according to the rules of the T2S settlement

  platform, are automatically cancelled 20 business days after their intended settlement date (ISD)

  or after the last modification date of the instruction, whichever is the earliest.

  A transaction in a "Hold", unmatched or matched situation is subject to the cancellation rules

  referred to above (cancellation made by the participants or automatic cancellation).

  The cancellation of instructions, unmatched or matched, can also be performed by CSDs/CCPs or

  the settlement platform if certain events occur, for example maturity of a security.



For the Exclusion, Amendment, Hold, Release, Link, Unlink functions only the following fields

must be filled via STD (SLRTmsg/SLRTfile):

    •   Instruction reference (Participant Reference, EURONEXT SECURITIES PORTO Reference or

      T2S Reference);
    •   Indicator of the type of reference of the instruction;
    •  ISIN Code;
    •   Securities account;
    •  Type of instruction;

    •   Participant;
    •  Quantity and Quantity type, in case of partial Release.





Operational Manual                                                                        2026-01-26            Page 131



[PDF page 133]

12.4 ALLEGEMENT FUNCTIONALITY



The Allegement is a "warning" sent to the instruction counterpart, to inform that there is an

instruction registered in the system waiting for the corresponding instruction for its confirmation

(matching).

The Allegement messages for settlement instructions and cancellation instructions (unmatched,

pending matching), are sent to participants according to the following rules:

   ▪    If a settlement instruction fails to match after the 1st attempt, the counterparty is informed

       via an Allegement message after a defined period of time:

     o  Standard: 1-hour period, measured from the first unsuccessful attempt of matching a

         settlement instruction;

     o  Before the cut-off: a period of 5 hours measured backwards from the cut-off time of the

       FOP (17:00 WET), if the contracted settlement date is the same day;

   ▪    If an instruction is cancelled before matching after the 1st matching attempt, the counterparty

        is immediately informed via an Allegement message.



EURONEXT SECURITIES PORTO participants (DCPs and ICPs) receive the Allegement messages:

  ▪  After 1 hour: if the instruction is entered before the contracted settlement date (ISD) or on

     the contracted settlement date (ISD) until 12:00 noon WET;

  ▪  Immediately:

         o  on the contracted settlement (ISD) day, if the instruction is registered after 12.00

            noon WET;

         o  In case of a cancellation instruction, subject to bilateral cancellation (instruction in

            matched state).



Allegement messages are sent by EURONEXT SECURITIES PORTO to its participants:

    •   Via STD: message 'SLRT', status NMAT/motive 002;

    •   Via SWIFT  for  participants who have subscribed  to ISO 15022 messages: MT578

       (Settlement Allegement).



Allegement messages, if subscribed, are sent directly by T2S to the DCPs:

    •   Via ISO 20022 messages: sese.028 (Securities Settlement Allegement Notification);


Operational Manual                                                                        2026-01-26            Page 132



[PDF page 134]

    •   Via T2S GUI: Securities/Settlement/Settlement Instruction Allegements.



In the case of DCPs, it is possible to subscribe at the T2S platform for the cancellation of allegements

(sese.029 - Securities Settlement Allegement Removal Advice) to be sent,  if the unmatched

settlement instructions that generated the allegements are cancelled.

EURONEXT SECURITIES PORTO informs its participants if the unmatched settlement instructions

that generated the Allegements are cancelled:

        ▪  Immediately after the cancellation of an instruction, in the case of instructions sent

         between EURONEXT SECURITIES PORTO participants;

        ▪  Immediately after receiving from T2S the cancellation of the Allegement, in the case

         where the instruction  is registered by a participant of another Central Securities

          Depository (CSD) with an EURONEXT SECURITIES PORTO participant as counterparty

          ('cross-CSD' settlement).