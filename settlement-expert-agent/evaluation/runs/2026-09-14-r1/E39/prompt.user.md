QUESTION FROM THE USER:
Milan's Settlement Service Instructions say night-time settlement starts at 19:30 but T2S says 20:00. Which applies to Monte Titoli participants today?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:02:36.358797+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_nts_processing"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-nts-processing]] — Night-time settlement processing: cycles, sequences and reporting (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.2 NTS processing and reporting; PDF 167–169 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Cycle durations are volume dependent; the 22:20/00:00 targets are objectives, not commitments.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.4.4.2 NTS processing and reporting; PDF 167–169):
1.4.4.2 Night-time settlement (NTS)

2    This section presents the night-time settlement processes in the T2S settlement day.

3    For the ease of presentation, the night-time settlement period is shown in two parts of batch settlement,
4   each one referring to a settlement cycle.

5   The NTS period starts after the successful completion of the SOD period and is followed by the maintenance
6   window and the real-time settlement period.




                                                                                          Page 167 of 2017



[PDF page 168]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1    In the exceptional cases that T2S experience the late arrival of late peak volume transactions on Friday
 2    evening that are not available for settlement at the regular NTS, the peak volume transactions should be
 3    sent after the NTS. In that case, short NTS cycles are triggered by the T2S Operator during the injection of
 4    the late peak volume transactions put under Intraday Restriction. At the end of the injection, the T2S Opera-
 5    tor triggers an Additional NTS cycle. The exact procedure with the timing to apply in case of such an event
 6    are defined in the T2S MOP.

 7    Note: The exact timing needed to perform the sequences and the time available for the sequence reporting
 8     will be defined at a later stage, but the dependencies defined are ensured.

 9  NTSProcessing

10    During the night-time settlement period, T2S processes the Settlement Instructions, Settlement Restrictions
11   and liquidity transfers in sequences within two settlement cycles. T2S submits Settlement Instructions, Set-
12    tlement Restrictions and liquidity transfers for settlement according to an automatic pre-defined order, called
13    “sequence”.

14   A settlement cycle may consist of more than one sequence (for settlement of different types of Settlement
15    Instructions, Settlement Restrictions and liquidity transfers).

16    In each NTS sequence, T2S:

17         l  Processes those new Settlement Instructions, Settlement Restrictions and liquidity transfers received be-
18        fore the start of the sequence which are eligible for settlement at this sequence (and for the first Se-
19       quence all the ones received in T2S before 20:00 even though the cycle starts after 20:00);

20         l  Includes pending Settlement Instructions not settled during previous sequences.

21     If a Settlement Instruction/Settlement Restriction selected for a sequence is linked “with” or “after” a Set-
22    tlement Instruction/Settlement Restriction which does not correspond to the sequence criteria, these Settle-
23   ment Instruction(s)/Settlement Restriction(s) are excluded from this sequence.

24   T2S validates and accepts the static data maintenance instructions and maintenance instructions during the
25    night-time settlement period on a continuous basis. However, T2S processes these updates only during the
26    processing periods between the different sequences. T2S sends the information on the status of the static
27    data maintenance instructions and maintenance instructions to T2S Actors immediately after end of their
28    processing (i.e. acceptance/execution).

29    For all static data updates, i.e. immediate updates and updates with future date, T2S also performs a revali-
30    dation of all Settlement Instructions and Settlement Restrictions to ensure that they are valid for the consid-
31    ered static data update. Maintenance instructions (i.e. Amendment Instructions, Cancellation Instructions,
32    Hold/Release/Partial Release Instructions) are only revalidated at the SOD revalidation process. In case the
33    underlying Settlement Instruction or Settlement Restriction to be maintained is cancelled due to their revali-
34    dation, the maintenance instruction is denied when trying to be executed but not cancelled.

35     Similarly, T2S processes any instruction query received and validated during a settlement cycle run with a
36    query response back to the relevant T2S Actor.

37  NTSReporting





                                                                                            Page 168 of 2017



[PDF page 169]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1    At the end of each night-time sequence, T2S generates full or delta reports as per the report configuration
 2    setup of the relevant T2S Actors.

 3   T2S sends also to the T2S Actors messages such as settlement status advices, settlement confirmation,
 4    posting notification, etc that were queued due to an execution of a settlement sequence.

 5   The duration of the night-time settlement cycles are dependent on settlement volumes. The target objective
 6    for the first and last night-time cycles should finish by 22:20 and 00:00 respectively, as long as volumes do
 7    not exceed standard peak volumes.


 8

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_instruction_processing_rules"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_participant_cutoff"}
STATUS: blocked — Applicable Milan timetable notice chain remains unresolved.
GAP IDS: ['G01']