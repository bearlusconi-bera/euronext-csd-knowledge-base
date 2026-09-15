QUESTION FROM THE USER:
Porto's operational manual says the FOP cut-off is 17:00. Isn't the T2S FOP cut-off 18:00? Which is right?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T10:02:59.253048+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_baseline_schedule"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline

--- SECTION [[t2s-schedule-r2]] — Baseline day phases and preceding-day/event dependencies (14 September re-verification) (reviewed 2026-09-14; modes ['current']; entities ['T2S']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.2 and exception conditions; PDF 156–158 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Table 37; PDF 160–163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.4.4.1; PDF 163 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Same pages as the 13 September section t2s-schedule; source bytes re-fetched and hash-identical on 14 September 2026.
LIMITATION: CET is the source convention; no UTC conversion.
LIMITATION: Nominal schedule is not guaranteed execution or a local participant cut-off. Dated queries require a reviewed event overlay for the same review date.
EXCERPT (§1.4.2 and exception conditions; PDF 156–158):
1.4.2 T2S schedule

18   The T2S schedule is under the control of the T2S operator, for creation of any new timelines, changing
19    and/or deletion of existing time for a period or event. The T2S Operator has the necessary privileges by
20    default to perform temporary or permanent changes to the T2S schedule. T2S ensures that the T2S sched-
21    ule always conforms to the T2S operating day calendar by currency for any changes.

22   T2S manages the transition between the various periods (see section Settlement day high level schedule
23    [ 158]) as an event. For each such event, T2S manages a planned time, a revised time and an effective
24    time:

25         l  The planned time corresponds to the standard schedule applied by default by T2S for every settlement
26       day. The T2S Operator can update this planned time in case of a permanent change in the regular
27        schedule;

28         l  The revised time is the foreseen time for the current settlement day, which usually coincides with the
29       planned time except when a delay has occurred. In contingency situations, the T2S Operator updates
30       the revised time while the planned time remains unchanged;


                                                                                            Page 156 of 2017



[PDF page 157]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         l  The effective time is the time of the actual occurrence of the event during the current settlement day.

 2   T2S foresees the maintenance of individual T2S settlement currency dependent cut-offs and events. Howev-
 3     er, the T2S operator manages the overall processing of a settlement day based on a common T2S schedule
 4    configured for each T2S settlement currency. There is no schedule of a settlement day defined per currency
 5     in T2S, but distinct individual cut-offs and events per currency are defined.

 6    This multi-currency configuration allows for some flexibility within the boundaries of the real-time settlement
 7    closure (start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET
 8    with FOP cut-off).

 9   The T2S Operator is entitled to change some cut-offs and events (deadlines for receiving Settlement Instruc-
10    tions/Settlement Restrictions for same day settlement) of a settlement day. This can be done independently
11    for a T2S settlement currency, in exceptional circumstances or contingency situations, based on a request
12    from the relevant T2S dependent external system (eg. RTGS, CSD platform, CMS). This exceptional proce-
13    dure is to be defined in the T2S Manual of Operational Procedure (T2S MOP). These currency dependent
14    cut-offs and events are specific events within the T2S daily schedule that have a cash component and are
15    not a cut-off related to the T2S centralised processing such as the start of day and end of day. Such curren-
16    cy dependent cut-offs and events are:

17         l DVP cut-off (IDVP / EDVP) –remains harmonised for all currencies at 16h00;

18         l  Cash Settlement Restriction cut-off;

19         l  Settlement restrictions release

20         l  Reimbursement of intraday credit

21         l BATM (Bilaterally Agreed Treasury Management) cut-off;

22         l CBO (Central Bank Operation) cut-off;

23         l  Optional cash sweep;

24         l  Inbound liquidity transfer cut off;

25         l  Automated cash sweep.

26    This change in cut-offs and events are valid only for the current T2S settlement day. When a currency de-
27    pendent cut-off or event is extended for a currency, then the start of its dependent processes (e.g. cash
28   sweep) is automatically extended for the same currency.

29   T2S allows such a change under the following conditions:

30         l  The sequence and order of events (predecessors and/or successors events) in T2S must remain un-
31       changed, i.e. a currency dependent cut-off cannot be delayed beyond a successor scheduling event if
32         this would have an impact on T2S processing (e.g. a CBO cut-off for Danish Krone cannot be extended
33       beyond the EOD cut-off for T2S, which is the successor in the scheduling). This includes no additions or
34       removals of events, no changes in event ordering and no change in event dependencies;

35         l  In the exceptional cases that T2S experiences a general issue across all currencies, it could be necessary
36        that the T2S Operator would need to extend the EOD cut-off (e.g. the T2S revised times would apply).
37        In this case, T2S ensures the sequence of currency independent cut-offs (securities Settlement Re-



                                                                                            Page 157 of 2017



[PDF page 158]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day

 1         striction cut-off and FOP cut-off) is not changed. The procedures to apply in case of such an event are to
 2       be defined in the T2S MOP.

 3    In the exceptional cases that T2S experiences the arrival of late peak volume transactions on Friday evening
 4    that are not available for settlement at the regular NTS, the T2S Operator would need to process into addi-
 5    tional NTS cycles. The procedure to apply in case of such an event are defined in the T2S MOP.

 6   T2S controls the execution of the processes so that the start of a subsequent process depends on:

 7         l  The completion of the current process and/or;

 8         l  The occurrence of a cut-off.

 9   However, for the start of a process, which is under the dependency of a preceding process and cut-off, T2S
10    ensures that this process cannot start until the completion of the previous process and until the cut-off time
11     is reached.

12
EXCERPT (Table 37; PDF 160–163):
[PDF page 160]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                                        Settlement Day

1                                  TABLE 37 - SETTLEMENT DAY HIGH LEVEL PROCESSES
2

      T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
         LINE

        18:45 –      Start of day  The start of day period including:
         20:00        (SOD)                                                             l  Change of business date in T2S;

                                                             l  Taking the common Snapshot (T2S and T2);

                                                             l  Preparation for night-time settlement:

                                 –  Revalidation of Settlement Instructions/Settlement Restrictions/amendments/hold
                                    and release instructions that failed to settle or to be executed as of their Intended
                                         Settlement date;

                                 –  At 19:00, final deadline to accept data feeds 131, effective for the current business
                                            date, from collateral management systems and payment/settlement banks; CBs
                                    and Payment Banks can send their Securities Valuation as soon as possible, ideally
                                     by 17:45, but in any case T2S will accept Securities Valuations until 19:00.

                                 –  At 20:00, final deadline to accept settlement instructions for processing in the se-
                                     quence 1 of the first night time cycle.

                                 –  Valuation of securities positions;

                                 –  Valuation of collateral eligible Settlement Instructions.

      20:00 – 3:00   Night-time   The night-time settlement period including two cycles:
                      settlement                                                             l  The first night-time cycle with reporting and processing of static data maintenance
                      (NTS)                                       instructions/maintenance instructions at the end of each settlement sequences in-
                                         cluding 5 sequences:

                                 – The sequence 0 (liquidity transfers from RTGS systems and from a T2S Dedicated
                                     Cash Account to another T2S dedicated cash account of the same T2S party, cash
                                         Settlement Restrictions regeneration related to the CoSD blocking and any cash
                                         Settlement Restrictions);

                                 – The sequence 1 (Corporate Actions on stock, new liquidity transfers, new cash
                                         Settlement Restrictions and all cash Settlement Restrictions not settled in the pre-
                                           vious sequence);

                                 – The sequence 2 (FOP for rebalancing purpose, new liquidity transfers, new cash
                                         Settlement Restrictions, new Corporate Actions on stock and all Settlement In-
                                               structions/restrictions which failed to settle in the previous sequences);

                                 – The sequence 3 (Central Bank Operations, new liquidity transfers, new cash Set-


    _________________________


       131   T2S processes these data feeds as soon as they are available. If data feeds are not received at the 19:00 deadline, T2S bases its processes on the
                 latest information received from the previous settlement days.


                                                                                          Page 160 of 2017



[PDF page 161]

                                                            T2S User Detailed Functional Specifications
                                                                                       General Features of T2S
                                                                                                 Settlement Day


T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
   LINE

                                  tlement Restrictions, new Corporate Actions on stock, new FOP for rebalancing
                                purpose and all Settlement Instructions/restrictions which failed to settle in the
                                   previous sequences);

                            – And the sequence 4 (new liquidity transfers and all the remaining Settlement In-
                                        structions/restrictions which are new or failed to settle in the previous sequences);

                            – The duration of the first night-time settlement cycle is dependent on settlement
                               volumes but should finish by 20:20(target objective) as long as standard peak
                               volumes are not exceeded.

                                                  l  The last night-time cycle, including partial settlement, with reporting and processing
                                   of static data maintenance instructions/maintenance instructions at the end of each
                                settlement sequences including 4 sequences:

                            – The sequence 4 (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in previous cycle);

                            – The sequence X (new liquidity transfers and all the Settlement Instruc-
                                        tions/restrictions which are new or failed to settle in the previous sequences and
                                          partial settlement on all unsettled Settlement Instructions, if eligible to partial set-
                                  tlement processing);

                            – The sequence Y (reimbursement of the “multiple liquidity providers”);

                            – The sequence Z (liquidity transfers).

                            – The duration of the last night-time settlement cycle is dependent on settlement
                               volumes but should finish by 00:00 (target objective) as long as standard peak
                               volumes are not exceeded.

3:00 – 5:00   Maintenance  The maintenance optional daily window.
           window (MWI)





                                                                                     Page 161 of 2017



[PDF page 162]

                                                             T2S User Detailed Functional Specifications
                                                                                        General Features of T2S
                                                                                                  Settlement Day


 T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
    LINE

 2:30 Satur-   Maintenance  The mandatory weekend maintenance window.
 day – 2:30  window (MWI)
  Monday

   5:00 (or    Real-time set- The real-time settlement period including:
 after NTS if  tlement (RTS)                                                    l  The real-time settlement preparation;
  NTS ends
                                                    l  Penalty mechanism processing:
 before 3:00)
                             –  At 7:30 , a final deadline for provision to accept penalty reference data to be used  – 18:00
                                           in current day´s penalty calculation and recalculation processes:

                                                   (i) Securities subject to penalties information;

                                      (ii)Updated historic (former) prices for penalties;

                                                           (iii) Daily prices for penalties.

                             –  At 7:30 , start of the penalty reference data preparation processing 132;

                             –  At 8:30 , a final deadline for completing the penalty eligibility 133 (starting at 19:30
                                     or after the end of the Start of Day processes if they are completed afterwards);

                             –  At 8:30 of the 14th business day of the month, start of the monthly reporting of
                                  aggregated amounts of penalties (to be completed by 21:30);

                             –  After the completion of the penalty reference data preparation, a final deadline for
                                      provision of penalty modification requests to be considered in current day´s pen-
                                           alty processes;

                             –  After the processing of penalty modification requests submitted before the dead-
                                              line, and the penalty eligibility, but not before 9:15 , start of the Calculation, Re-
                                        calculation and reporting of new and modified penalties;

                             – On the 13th business day of the month, after the Recalculation is completed, start
                                    the end of appeal period process followed by the calculation of monthly aggregat-
                               ed amounts of penalties (to be completed by 8:30 on the next business day);

                                                    l  The real-time settlement with 5 partial settlement windows;

                                                    l  The real-time settlement closure.

   18:00 –     End of day   The end of day period including:
    18:45        (EOD)                                                    l  The stop of settlement engine;


_________________________


132   Preparation processing is comprised of Static data processing of reference data for the penalty calculation and recalculation.

133    Penalty eligibility is comprised of an analysis of failed matched settlement instructions from the previous business day to determine their eligibility
        for penalties.


                                                                                      Page 162 of 2017



[PDF page 163]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                         Settlement Day


       T2S TIME-   T2S PERIODS                         HIGH LEVEL DESCRIPTION
          LINE

                                                               l  The internal T2S securities accounts consistency check;

                                                               l  The recycling and purging;

                                                               l  The end of day reporting and statements 134.


 1
EXCERPT (§1.4.4.1; PDF 163):
1.4.4.1 Start of day (SOD)

 5    This section presents the start of day processes.

 6   The SOD period starts after the successful completion of the previous EOD period and after 18:45, and is
 7    followed by the night-time settlement period.

 8   The SOD period concentrates on the change of T2S business date, the taking of the common Snapshot and
 9    preparation of the night-time settlement period. It includes the processing of the feeds from collateral man-
10   agement systems (CMS) and payment/settlement banks for the reference prices and eligible assets (for val-
11    uation purposes).


12

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_windows_and_cutoffs"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "timetable_document_scope"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-timetable]] — Porto timetable notice and source clock convention (reviewed 2026-09-13; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: porto-timetable-notice | Notice 394/2024 §§1–15; effective 17 April 2024 | version None | body language en | authoritative language pt | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/en/media/11820/download
LIMITATION: English translation expressly not legally binding. Preserve source clock values; conversion and dated exceptions are not certified.
EXCERPT (Notice 394/2024 §§1–15; effective 17 April 2024):
[PDF page 1]

This translation has been prepared with the best of our knowledge and does not represent a legally
binding document.
In case of legal matters the original documents written in Portuguese, and other Portuguese
legislation should be consulted.




                                    INTERBOLSA NOTICE 394/2024


                                              Timetables
It is hereby made public, the opening hours of the systems managed by INTERBOLSA – Sociedade
Gestora de Sistemas de Liquidação e de Sistemas Centralizados de Valores Mobiliários, S.A., as well
as the timetable related to certain moments of the settlement process, which are as follows:


1. The centralized securities systems and the settlement systems (Systems) are open from Monday to
Friday, except on the following days: January 1st, May 1st, Good Friday, Easter Monday, December
25th and December 26th; Interbolsa publishes annually any exception to the provisions of this
paragraph.
2. The operating timetable of the Systems, which is based on the operation hours adopted by the
TARGET2-Securities (T2S) platform and also defined in the T2S rules, is as follows:
        a) Opening: 17h45m the previous working day (start of day);
        b) Closing: 17h00m (end of day) being 15h00m for instructions with financial component.
3. The night time settlement period starts at 19h00m, followed by a daytime settlement period,
which runs from the end of the night time settlement period until 17h00m.
4. Regarding the maintenance periods occurring in the T2S platform and the Interbolsa systems
        a) There is a mandatory maintenance period occurring between 01h30m on Saturday and
01h30m on Monday;
        b) On the other days of the week there may be an (optional) maintenance period between
2h00m and 4h00m., only in those cases in which the T2S platform operator considers it necessary to
implement an urgent development on the platform. In this case, T2S will duly inform Interbolsa and,
consequently, Interbolsa will inform its participants;
        c) On a daily basis, Interbolsa's systems will have a brief technical interruption, which will
occur around 2h00m.
5. Instructions can be recorded in the System whenever a maintenance period is not active.



[PDF page 2]

6. The partial settlement occurs in the last settlement cycle of the night time settlement period and
between 07h00m and 07h30m, 09h00m and 09h15m, 11h00m and 11h15m, 13h00m and 13h15m
and 14h30m and 15h00m in the day time settlement period.
7. The timetable for registration of operations related to collateral provided to the Investor
Compensation System and the Deposit Guarantee Fund occurs between 06h00m and 17h00m.
8. In the corporate actions processing, whenever concerned with payments in euro or in other
currency accepted by T2S, INTERBOLSA sends, on the day before payment day, in the case of debt
instruments, or at 8h30m, on payment day, in the case of other securities, to the T2S platform the
information needed for the financial settlement of cash distributions, mandatory reorganisations
with cash distribution, payment of the subscription and payment of the allotment in operations
related to the subscription of capital, under the terms of INTERBOLSA Circulars related to corporate
actions of debt instruments and other securities.
9. In what concerns the operation of the SLME – Sistema de Liquidação em Moeda Estrangeira (non-
euro currency settlement system), INTERBOLSA sends to CGD, on payment day, at 9h30m the
necessary information for the financial settlement of cash distributions and mandatory
reorganisations with cash distribution, under the terms of INTERBOLSA Circulars related to corporate
actions of debt instruments and other securities.
10. The procedures related to the functioning of the centralized securities services, particularly those
related to requests for deposit and withdrawal of certificated securities, sending a file to identify the
holders and the fortnightly reconciliation of balances, occur between 8h30m and 17h00m.
11. The subscription requests referred to in paragraphs 3 and 4 of Article 17 of INTERBOLSA Circular
related to corporate actions are sent by the participants to INTERBOLSA local systems between
8h30m and 16h00m.
12. In accordance with the terms set forth in INTERBOLSA Circular related to the registration and
order routing service of subscription and redemption operations in open investment funds, the
opening hours follow the specific rules as detailed next:
        a) The registration of subscription and redemption orders may be carried out between
8h30m (service opening time) and 16h45m;
        b) The cut-off time defined by the managing entity or by the custodian entity cannot be later
than 16h45m;
        c) The managing entity or the custodian entity, as appropriate, sends to INTERBOLSA the
accepted and rejected subscription and redemption orders between 8h30m and 16h45m, being the
deadline 11h00m of the intended settlement date of the mentioned operations.



[PDF page 3]

        d) All the orders not confirmed by the managing entity or the custodian entity, as
appropriate, until 11h00m of the intended settlement date will be cancelled by Interbolsa;
        e) Interbolsa sends to T2S until 12h00m of the intended settlement date, the necessary
instructions to the settlement of the subscription and redemption orders, as well as the update of
the static data.
13. In accordance with the terms set forth in Interbolsa Regulation concerning the Securities Lending
Management System (SGE), the opening hours follow the specific rules as detailed next:
        a) Processing of corporate actions in open lending operations (dividend compensation or
cancellation) at 07h45m;
        b) Opening of the registry of lending operations at 8h30m;
        c) Processing the opening of forward lending operations opening and updating of the
collateral at 10h30m;
        d) Processing the closing of lending operations at 13:00m;
        e) Closing of the registry of lending operations at 14h50m, for registration of lending
operations with real time opening;
        f) Closing of the registry of lending operations at 17h00m for registration of lending
operations with opening on a future date and for the registration of amendments to the contracting
conditions regarding lending operations in course, namely the lending operation’s closing date and
the guarantee’s remuneration rate.
14. Interbolsa’s Notice 611/2021 is hereby revoked.
15. This notice comes into force on 17 April, 2024.
                                                                                             Interbolsa
                                                                                The Managing Board

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_operating_hours_published"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-operating-hours-web]] — Published operating hours table (T2S-based, CET) with the WET note and reference to Notice 0394/2024 (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Euronext Securities Porto — Working Days & Operating hours (web page, capture of 14 September 2026) | Working Days & Operating hours page, operating-hours section; capture of 14 September 2026 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/en/post-trade/euronext-securities/porto/about-us/working-days-operating-hours
LIMITATION: Web page reproduction of the T2S schedule; the binding source is Notice 0394/2024 (section porto-timetable) and dated exceptions need event evidence.
LIMITATION: The page's 2025 closing-day list was visible at capture; the 2026 calendar is Notice 25/1162 (section porto-calendar).
EXCERPT (Working Days & Operating hours page, operating-hours section; capture of 14 September 2026):
The operating hours of the centralised systems and settlement systems managed by Euronext Securities Porto are based on the operating hours of the T2S platform – TARGET2-Securities and are set out in the notice no. 0394/2024 Timetables.Schedule T2STime CETStart of Day – SoD Change of business date18:45Preparation for Night Time Settlement18:45 – 20:00Night Time Settlement (NTS) Start of NTS20:00First Cycle, with five sequences Last Cycle, with partial settlement in sequence X Real time Settlement (Starts if the NTS ends before 03:00 CET / 02:00 WET) Maintenance Window in weekday (optional)03:00 – 05:00Maintenance Window from Saturday until Monday (required)02:30 – 02:30Real time Settlement05:00 – 18:00Partial Settlement Cycle 108:00 – 08:30Cycle 210:00 – 10:15Cycle 312:00 – 12:15Cycle 414:00 – 14:15Cycle 515:30 – 16:00DVP (Delivery versus Payment) cut-off16:00Collateral reimbursement16:30BATM / CBO cut-off17:40Inbound LTO cut-off / Automatic cash sweep17:45FOP (Free of Payment) cut-off18:00End of Day – EoD18:00Please Note: Portugal uses WET (Western European Time), which is -1 hour than CET (Central European Time).Acronyms:BATM – Bilaterally Agreed Treasury ManagementCBO – Central Bank OperationsLTO – Liquidity Transfer Orders

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_instruction_registration"}
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