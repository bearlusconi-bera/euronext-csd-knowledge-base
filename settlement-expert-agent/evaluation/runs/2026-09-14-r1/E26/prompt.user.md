QUESTION FROM THE USER:
How does a Porto ICP put an instruction on hold and then partially release it, and which STD or ISO messages carry the status?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.264062+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_hold_release_process"}
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


        198    Internally generated instructions are not considered for Hold/Release default.


                                                                                            Page 292 of 2017



[PDF page 293]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Changes in Reference Data of the “Hold Release Default” of a Securities Account do not trigger the revalida-
 2    tion of the instructions that include such Securities Account (i.e. the change of the “Hold Release Default”
 3    only affects instructions received after such a change).


 4    1.6.1.6.6 Partial Release process

 5   When a T2S Actor sends a Release Instruction, he has the option to only release part of the quantity of the
 6    referenced Settlement Instruction in case a set of given conditions are met.

 7    In order to trigger this process the T2S Actor must specify, in the Release Instruction, a quantity which shall
 8   be lower than the quantity indicated in the referenced Settlement Instruction.

 9   To validate this particular type of Release Instruction, T2S checks that:

10         l  The Referenced Instruction exists;

11         l  The quantity to be released is lower than the original quantity of the Referenced Instruction;

12         l  The quantity to be released complies with the Settlement Unit Multiple.

13         l  The number of decimals of the quantity to be released is equal or lower than the number of decimals of
14       the Settlement Unit Multiple of the related Security

15         l  The quantity is expressed using the same Settlement Type as the one specified in T2S Reference Data
16         for the ISIN Code of the referenced Settlement Instruction.

17         l  The Intended Settlement Date of the referenced Settlement Instruction has been reached.

18         l  The Securities Movement Type of the referenced Settlement Instruction is ‘DELI’.

19         l  The referenced Settlement Instruction is not a T2S generated Settlement Instruction

20     If any of these conditions is not met the Release Instruction is rejected and T2S does not undertake the
21     Partial Release Process.

22     If the Release Instruction is successfully validated by T2S, the Partial Release Process will then carry on an-
23    other subset of checks in order to execute the partial release:

24         l  The Referenced Instruction is matched;

25         l  The Referenced Instruction is not awaiting approval or revoked;

26         l  The Referenced Instruction is not settled;

27         l  The Referenced Instruction is not cancelled;

28         l  The Referenced Instruction is not identified with CoSD Flag;

29         l  The Referenced Instruction is on Party Hold;

30         l  The quantity to be released complies with partial settlement rules regarding MSU, SUM and cash thresh-
31        old;

32         l No other hold applies to the Referenced Instruction or its counterparty instruction;

33         l  None of the related Realignment instructions is on Hold

34         l  The Referenced Instruction and its counterparty instruction allow partial settlement;

35         l  The Referenced Instruction and its counterparty instruction are not constrained by any settlement link;

                                                                                            Page 293 of 2017



[PDF page 294]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1         l  The Referenced Instruction and its counterparty instruction are not constrained by any non-reciprocal
 2         link;

 3         l  The Referenced Instruction and its counterparty instruction have not reached their cut-off time.

 4     If the conditions for partial release are no longer present the ongoing partial release process is cancelled.

 5     If the quantity released is higher than the remaining quantity of the Referenced Instruction the partial re-
 6    lease will be handled as a full Release Instruction.

 7   Once T2S successfully executes the partial release, the T2S Actor is informed through a message communi-
 8    cating the execution of the maintenance instruction and through a Status Advice message informing that the
 9    Referenced Instruction is still on Party Hold and that the partial release has been executed. Interested par-
10     ties can also be informed depending on their message subscription preferences (see section Status Man-
11   agement [ 653] and section Message subscription [ 135]).

12   Once executed, a partially released Settlement Instruction will be submitted to a settlement attempt depend-
13    ing on the phase of the day (see section Partial Settlement [ 343])

14         l   If it is executed during the Night Time Settlement, the partially released Settlement Instruction will only
15       be submitted to a settlement attempt when the corresponding sequence runs.

16         l   If it is executed during the Real Time Settlement, the partially released Settlement Instruction will be
17       submitted to settlement attempts either for the total partially released quantity outside a partial settle-
18      ment window or for part or the total of the partially released quantity if a partial settlement window is
19        running.

20   To cancel the Partial Release Process, a Party Hold instruction should be sent.

21    Additionally, the Partial Release Process will be automatically cancelled when:

22         l  Any new holds apply to the Referenced Instruction or the counterparty instruction;

23         l Areleaseinstruction over the Referenced Instruction is received;

24         l  The Partial Settlement of the Referenced Instruction or the counterparty instruction is disallowed i.e.
25         Partial Settlement Indicator set to ‘NPAR’;

26         l A Business Link is added through an amendment or a non-reciprocal link;

27         l  The Partial Release Process has not fully settled the released quantity by the relevant cut-off time.

28         l  The released quantity is less than the quantity resulting from the cash threshold equivalent in the under-
29         lying settlement instruction;

30     If the Partial Release Process is cancelled the T2S Actor will be informed through a Status Advice message.

31    In case a T2S Actor wants to amend the Partial Release Process and increase or decrease the quantity to be
32     partially released, the T2S Actor shall cancel the current process by sending a Party Hold instruction and
33   send a new partial release with the new desired quantity to be released.

34    During the whole Partial Release Process, the referenced Settlement Instruction will remain on Party Hold.

35   The Partial Release Process will terminate when the partially released quantity is completely settled or if the
36    process is cancelled, either by the T2S Actor or by T2S.



                                                                                            Page 294 of 2017



[PDF page 295]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                     EXAMPLE 80 - PARTIAL RELEASE PROCESS

 2    This example illustrates the execution of a Release Instruction that aims to partially release Settlement In-
 3    struction “X”, which has its Party Hold indicator already set to “Yes”.

 4   On the Start of Day period of the Intended Settlement Date for Settlement Instruction “X”, a T2S Party
 5    sends a Release Instruction for Party Hold, in order to partially release the referenced Settlement Instruc-
 6     tion. For this, the T2S Party indicates a specific quantity in the Release Instruction which is lower than the
 7    original quantity of Settlement Instruction “X”. T2S successfully validates the instruction, and proceeds to
 8    execute the partial release, leaving the Party Hold indicator of the referenced Settlement Instruction set to
 9    “Yes”. Additionally, T2S notifies the execution of the Release Instruction and the Status Advice of the Set-
10    tlement Instruction to the T2S Actor and other interested parties, depending on their message subscription
11    preferences.

12    After the execution of the Release Instruction, Settlement Instruction “X” will only be submitted to a settle-
13   ment attempt when Partial Settlement is allowed.

14    After the effective settlement of the partially released quantity, the referenced Settlement Instruction will
15    remain on Party Hold until the T2S Actor sends a standard Party Hold Release Instruction (i.e. without speci-
16    fying a quantity) or another Release Instruction indicating a quantity equal or higher than the quantity re-
17    maining on Party Hold.

18   The Settlement Instruction “X” remains in scenario 9 of Table 62 - Hold /Release Exhaustive Scenarios for a
19    Settlement Instruction [ 287] throughout the entire partial release process and also after its ending.

20          DIAGRAM 72 - THE PARTY SENDS A RELEASE INSTRUCTION TO PARTIALLY RELEASE A SETTLEMENT INSTRUCTION





21

22

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_status_model"}
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

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_hold_release_amendment"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-hold-release-amend]] — Hold, total and partial release, and amendment functionalities with STD/ISO message references (§12.2) (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Operational Manual of INTERBOLSA | §12.2; PDF 127–131, printed 126–130 | version Operational Manual V43. Internal date 26 January 2026; filename 16 February 2026; posted April 2026. | body language en | authoritative language pt | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf
LIMITATION: English version of the Operational Manual V43 (internal date 26 January 2026); Portuguese text governs and the manual's operative effective date is unresolved.
LIMITATION: Reason codes (001–027) are STD SLRT codes as printed.
EXCERPT (§12.2; PDF 127–131, printed 126–130):
12.2  HOLD, RELEASE AND AMENDMENT FUNCTIONALITIESS

        (cf. Articles 45 and 46 of INTERBOLSA Regulation No 2/2016)



12.2.1 HOLD/RELEASE

EURONEXT SECURITIES PORTO allows the settlement instructions to be placed in a state of "Hold"

and subsequently "released", either totally or partially.

It is possible to put the instructions in a "hold" state:

   ▪  At the time of registration of the instruction.

É possível colocar as instruções em estado de “suspensão” (Hold):

   ▪ No momento do registo da instrução.




( 1) In case of instructions sent directly to the T2S settlement platform, the following fields are also optional matching fields: 'Client of
the delivering party', 'Client of the receiving party ', 'Securities account of the delivering party' and 'Securities account of the receiving
party'.


Operational Manual                                                                        2026-01-26            Page 126



[PDF page 128]

     To do this, when recording the instruction via STD (function "I" - Inclusion), "H" must be

      included in the "Hold" field:

          •   In the STD message 'SLRT' the status NMAT with reason code 001 (Operation

             registered) and 002 (Operation registered by counterparty) and the status MACH with

           reason code 003 (Matched transaction, pending settlement) are sent when the match

            occurs.

   ▪  After registration of the instruction (unmatched or matched).

     For this purpose, when recording via STD, the 'H' (Hold) function shall be used and 'H' shall

    be included in the 'Hold' field:

          •   In the STD message 'SLRT' the NMAT/MACH status is sent with reason code 023

             (instruction placed on Hold) and 024 (counterpart instruction placed on Hold).

   ▪ EURONEXT SECURITIES PORTO  participants can also perform the Hold/Release  of an

       instruction using ISO 15022 messages by sending an MT530 message.

   ▪ DCPs can perform Hold/Release of an instruction directly in T2S by sending the ISO message

     20022 - sese.030.

   ▪  The Hold function can be used at any time before the (physical and financial) settlement of

      the transaction in question, i.e. it can be used when the transaction is registered, before

      matching, after matching, or during the settlement day.

   ▪  Instructions (unmatched or matched) can put on Hold until the instruction is settled or until

          it is cancelled. An instruction that is pending partial settlement can be placed in Hold.

   ▪  The "release" can be total or partial;

   ▪  Total release:

        o  The total Release of the quantity in Hold can be made before matching, after

            matching, during the settlement day or after ISD;

        o  When recording via STD, the function "R" (Release) shall be used and " " (blank)

           must be included in the "Hold" field;

        o  In the STD message "SLRT" the status NMAT/MACH is sent with reason code 025

              (instruction Released) and 026 (counterpart instruction released).

   ▪  Partial Release:

         o  When registering via STD, the function "R" (Release) shall be used and " " (blank)

           must be included in the "Hold" field;

         o   Partial Release is possible for securities delivery instructions (DVP, DFP, DWP):

                  •  Matched and not cancelled;



Operational Manual                                                                        2026-01-26            Page 127



[PDF page 129]

                  •  Pending, in Hold by participant;
                  •  That allow partial settlement;
                  •  On which ISD (Intended Settlement Date) has been reached (i.e., a request for

                      partial release can only be submitted as of SoD, which occurs at 18:45 CET);

           o  The quantity to be released must be less than the original quantity of the

                settlement instruction;

           o   If there is an indication of no authorisation for partial settlement (NPAR) in at least

              one of the instructions ('delivery' or 'receive'), the request for partial release shall

                not be accepted;

           o   If the partial settlement indicator PARQ (quantity) has not been included and the

                  instruction involves cash (DVP, DWP), the minimum threshold of 10,000 EUR for

                stocks and 100,000 EUR for debt must be adhered to for partial settlement to take

                 place;

           o  The partial release process only has one life cycle during the release day, i.e. if a

                 quantity is partially released and it does not settle by the end of the settlement

                   cut-off, T2S automatically cancels the process, i.e. the instruction returns to its

                   original state (Hold of initial quantity);

           o   Partial Release is allowed for instructions with ISD in the past;

           o   If the counterparty instruction (receive) is set to 'Hold', the request for partial

                 release is rejected by the T2S platform;

           o  The partial release process is activated by sending an amendment request by

                  selecting the 'Release' function and filling in the desired quantity to be released:

                  •  DCPs:

                                    -   via ISO message 20022: sese.030 - "Securities Settlement Condition

                           Modification Request";

                  •   ICPs:

                                     -   via STD: SLRTmsg/SLRTfile;

                                     -   via message ISO15022: MT530 "Transaction Processing Command"

                                 (field "Quantity of Financial Instrument to be settled" :36B::SETT// );

           o  The response to a partial release of accepted quantity, is sent to the:

                   •  DCPs:
                                     -   via ISO 20022 messages:

                                   •  sese.031  -  "Securities  Settlement  Condition  Modification

                                 Request", informing the acceptance of the request with the

                                   status 'completed';




Operational Manual                                                                        2026-01-26            Page 128



[PDF page 130]

                                   •  sese.024 - 'Securities Settlement Transaction Status Advice' -

                                    stating the partial quantity released and the quantity remaining

                                      in 'Hold';

                   •   ICPs: In case of partial 'Release', the quantity partially released and the

                   remaining quantity in 'Hold' is reported in the following fields:

                                    -   via STD: SLRT message - reports the partial amount released and the

                         remaining quantity in 'Hold' in the field 'Participant Remarks'*;
                                    -   via ISO message 15022: MT548 "Settlement Status and Processing

                          Advice"  -  reports  the  Partially  Released  Quantity and  Quantity

                       Remaining on Hold, in field :70E::SPRO// (Partially Released Quantity

                      and Quantity Remaining on Hold)

                                             *Field         format:        R99999999999999,99

                                    H999999999999,99

                                      Example: R123456789012.99 H123456789012.99

                                                     •  R = Released quantity
                                                     •  H = remaining quantity in Hold


           o  The 'Partial Release' process can be cancelled by the participant by placing the

                  instruction back into Hold;

           o  Multiple 'Partial Releases' are not permitted for the same instruction at the same

                time; only one new 'Partial Release' may be made after the previous order has

              been settled;

           o  When an instruction is partially released, the instruction will attempt to settle by

                the released quantity..

   ▪ When a "MACH" (matched) transaction changes to released (one of the parties uses the

      Release function and the counterparty is already released), it is sent for settlement in real

      time (unless the contracted settlement date is in the future or the settlement cut-off time

      has been exceeded, in which case the transaction will be submitted for settlement as soon

      as  possible). EURONEXT SECURITIES PORTO informs the issuing  participant and the

      counterparty participant of the status of the instruction, as well as any changes in status

      (from Hold to Release and vice versa).




12.2.2 AMENDEMENT

EURONEXT SECURITIES PORTO allows participants to change an instruction that is registered in

the system in unmatched or matched status.

Participants are allowed to change the following indicators (Amendment) of an instruction:


Operational Manual                                                                        2026-01-26            Page 129



[PDF page 131]

    • Partial settlement (only for settlement instructions);

    • Link to an instruction (Link);

    • Settlement priority.

Instruction changes are made via the STD using the 'A' (Amendment) function, and only the

participant who made the change receives information on the change (reason code 027 - partial

settlement, priority and instruction link - changed) in the STD's 'SLRT' message.

EURONEXT SECURITIES PORTO participants can also send an instruction change via ISO 15022

messages by sending an MT530 message.

On the T2S platform the Amendment mechanism can be used voluntarily by participants DCPs, if

the instructions have the indicator 'YES' in the field 'Allowed Modification Flag'; for this purpose

participants have to send a message ISO 20022 - sese.030.

It is possible to change only one processing indicator per instruction and you can change indicators

of the instruction until the instruction is partially or fully settled or until its cancellation occurs.

However, you can only change the settlement priority of the outstanding part of a partially settled

instruction.

The change is only possible if:

 ▪  the settlement instruction or settlement restriction has not yet been settled or cancelled;

 ▪  The settlement instruction is not identified as CoSD (Conditional Securities Delivery);

 ▪  The settlement instruction or settlement constraint is partially settled, in which case the change

    can be made only for the 'Priority' indicator.





Operational Manual                                                                        2026-01-26            Page 130

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Porto", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "porto_settlement_processing_partial"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[porto-settlement-processing]] — Settlement processing, failures/PENF reporting and partial settlement rules and limits (§§12.5–12.5.3) (reviewed 2026-09-14; modes ['reference']; entities ['Porto']; basis reference_description)
CITATION: Operational Manual of INTERBOLSA | §§12.5–12.5.3; PDF 134–138, printed 133–137 | version Operational Manual V43. Internal date 26 January 2026; filename 16 February 2026; posted April 2026. | body language en | authoritative language pt | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf
LIMITATION: English version of the Operational Manual V43 (internal date 26 January 2026); Portuguese text governs and the manual's operative effective date is unresolved.
LIMITATION: Default partial-settlement limits (EUR 10,000 shares / EUR 100,000 debt) are as printed; T2S Operator parameters govern.
EXCERPT (§§12.5–12.5.3; PDF 134–138, printed 133–137):
12.5 SETTLEMENT OF INSTRUCTIONS



As soon as the match (confirmation) occurs, the settlement instructions are immediately sent for

settlement and, if possible, processed immediately - Settlement Finality 3 (SF3) - settlement.




12.5.1 SETTLEMENT PROCESSING

       ▪   In the case of DVP (Delivery versus Payment) settlement upon validation of the existence

           of securities in the  seller's securities account and cash in the counterparty's DCA

         (Dedicated Cash Account), the seller's securities account are debited against the buyer's

           securities account. Simultaneously, the buyer's DCA is debited by the amount of cash to

        be settled against the seller's DCA.

       ▪   In the case of the settlement of FOP (Free of Payment) instructions, only the transfer of

           securities between the seller's account and the buyer's account takes place, provided that

         they are available.

       ▪   In the case of settlement of PFoD (Payment free of delivery) instructions, the DCA to be

         debited being provisioned, settlement will be effected by transferring the cash from the

       DCA to be debited to the DCA to be credited.




Operational Manual                                                                        2026-01-26            Page 133



[PDF page 135]

       ▪   In the case of Delivery with Payment (DWP) instruction settlement, as the securities and

         cash move in the same direction (debit or credit), settlement takes place only when both

           securities and cash are available.





12.5.2 FAILURES


    ▪  Securities failures:

     o  The operation remains pending settlement and is automatically re-submitted for a further

         settlement attempt when sufficient securities are available. This can happen in real-time,

         overnight settlement processing or during one of the partial settlement windows,  if

          allowed.



    ▪  Cash failures:

     o  In the case of Euro settlement, or in any T2S-eligible currency, the transaction is pending

         settlement and automatically resubmitted for a new settlement attempt when sufficient

         cash is available.

     o  In the event  of a cash  failure,  it may be overcome by  resorting  to the auto-

           collateralisation feature,  if duly authorised, permitted and parameterised. For further

           details on auto-collateralisation see point 11.6 - "Auto-collateralisation".



If the Intended Settlement Date (ISD) has been exceeded, i.e. if the instruction has not settled on

ISD, the status PENF (pending settlement failing on intended settlement date) is reported.

    •   For ICPs:

         o  the status 'PENF' and reason 050 ('Instruction can no longer settle on ISD') is

             informed via the STD in the mnemonics SLRT ('PENF', '050') and SLRT-PND

            ('PENF')

                 o  For an instruction registered after ISD, or in ISD after the corresponding

                          cut-off, the following is reported: NMAT -'001;050

                 o  For an instruction which matches after ISD, or in ISD after its cut-off, the

                        following is reported: MACH - "003; 050".

               •  the status 'PENF' is informed via SWIFT - ISO 15022, in messages MT537 and
             MT548





Operational Manual                                                                        2026-01-26            Page 134



[PDF page 136]

    •   For DCPs, the status 'pending settlement failing on intended settlement date' is reported in

       the messages:

                 o  sese.024 - Settlement Instruction Status Advice

                 o  semt.014 - Intra Position Movement Status Advice

                 o  semt.018 - Securities Transaction Pending Report




12.5.3 PARTIAL SETTLEMENT

          (cf. Article 57 of INTERBOLSA Regulation No 2/2016)

    ▪   Partial settlement, if allowed, is applied to all settlement instructions, when full settlement

         is not possible due to securities failure, in the following settlement periods:

      o  In the night settlement period: in the last settlement run;

      o  In the daytime settlement period, in partial settlement "windows" (see chapter 4 -

          "Timetable and Schedules").

    ▪  An instruction is partially settled even though there are insufficient securities to settle the

         full quantity under the following conditions:

         o  The partial settlement window is occurring;

         o  The instructions were "flagged" for partial settlement;

         o  The partial settlement limit is satisfied.

    ▪  For a settlement instruction to be considered for partial settlement,  it must meet the

       following requirements:

        o  The instruction type to be FOP, DVP or DWP;

        o  The partial settlement indicator must not be 'NPAR' in any of the instructions;

        o  Instructions must not be linked with any other instruction by means of the LINK

               'Before', 'After', 'With' or with a pool reference;

        o  the financial amount of the instructions is in T2S-eligible currency.

    ▪  EURONEXT SECURITIES PORTO participants have the possibility to send the following partial

       settlement indicators:

          o  NPAR - partial settlement not allowed;

          o  PARC - partial settlement allowed, with a minimum limit criterion expressed in

                 financial amount;

          o  PARQ - partial settlement allowed, with a minimum limit criterion expressed in

               quantity of securities;


Operational Manual                                                                        2026-01-26            Page 135



[PDF page 137]

          o  PART - partial settlement allowed, the standard limit type (with minimum limit

                 criterion expressed in financial amount) is applied;

          o  BLANK - in this case the default partial settlement rules apply (if partial settlement

                    is allowed, the limit will be applied by default).

    Once partial settlement is invoked, you are only allowed to: change the priority of the

      instructions, change the instruction in Hold for Release or cancel the instructions with pending

      partial settlements.

    When an instruction is partially cleared, the original instruction is not automatically cancelled.

     The original instruction is retained, and the quantity of the partially settled instruction and its

      status are updated according to the partial settlements that occurred.

    ▪   Partial settlement is conditional on defined limits, below which it is not applied. These limits

       are determined:

          o  By the type of instruction (FOP or DVP or DWP);

          o  By the limit type of the instruction;

          o  By the implied ISIN;

          o  By the currency of the financial amount of the settlement instruction.

    ▪  The types of partial settlement limits are:

          o  Limit on quantity: means that partial settlement does not take place for a smaller

               quantity than the applicable value;

          o  Limit on financial amount: means that partial settlement does not take place if the

            amount corresponding to the quantity of securities to be partially settled is less than

               the applicable amount.


       Content of the settlement instruction          Result
                                                     applied   Result applied to the
  Type of     Type of                                                      to limit      amount limit
  instructi    instruction      ISIN     Currency                                                    type
    on            limit

   FOP           n/a                                      Minimum settlement
                                                                            unit for the first partial
             Defined as                                                                     settlement / Multiple
             "Quantity" for     Applicable       n/a       Quantity                                                                     settlement unit for the
 DVP/DWP  both                                                                          following partial
             Settlement                                                                      settlement(s)
              Instructions
                                                        Amount configured in
            Not defined as                                        the currency specified
             "Quantity"   for     Units                     Financial  (minimum settlement
 DVP/DWP                                     Aplicável            both Settlement    (UNIT)                Amount    unit and multiple
              Instructions                                            settlement unit used for
                                                                          quantity).


Operational Manual                                                                        2026-01-26            Page 136



[PDF page 138]

       Content of the settlement instruction          Result
                                                     applied   Result applied to the
  Type of     Type of                                                      to limit      amount limit
  instructi    instruction      ISIN     Currency                                                    type
    on            limit
                                                        Amount configured in
                                                                    the currency specified
                             Nominal                                                         (minimum settlement
                           amount
                                                                            unit and multiple                             (FAMT)
                                                                     settlement unit used for
                                                                          quantity).




When an instruction is submitted for partial settlement, the maximum financial amount or quantity

of securities available in the seller's account is settled, taking into consideration the type of limit

chosen by the parties.

The part (quantity) of the transaction settled is referred to as the 'settled portion', while the part

(quantity) of the transaction that was not settled is referred to as the 'portion pending settlement'.



The limit applied to partial settlement must be expressed in value (financial amount limit) or in

quantity (quantity limit). The limit determines the amount or quantity of the instruction on which

the partial settlement will take place.

Default financial limit for instructions involving cash (DVP and DWP):

    •   More than 10,000 EUR for shares;
    •   More than 100.000 EUR for debt.



Default quantity limit for instructions involving quantity (FOP):

    •  Minimum settlement unit and multiple settlement unit.



With regard to settlement restrictions, partial settlement is always applied for reservation and

earmarking instructions.

Partial settlement is not applicable to settlement restrictions that are automatically generated by

T2S for conditional settlement (CoSD) and for blocking settlement restrictions.

Settlement restrictions (blocking, reservation, earmarking) do not apply to partial settlement

'windows' and their limits.