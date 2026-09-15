QUESTION FROM THE USER:
What are the DSS settlement cycle times in Athens today?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.952922+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_nts_processing"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
SCHEDULE KIND: baseline
ROUTER NOTES: {"_note": "T2S platform route used because no route for the named CSD covers this topic"}

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

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "reference", "question_type": "athens_settlement_methods"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[athens-settlement-methods]] — Settlement methods, cash blocking and delegation of technical details to DSS announcements (Part 2) (reviewed 2026-09-14; modes ['reference']; entities ['Athens']; basis reference_description)
CITATION: ATHEXCSD Resolution 5 | Resolution 5 Part 2 §§2.1–2.2; PDF 4 | version Resolution 5: effective 8 December 2025. | body language en | authoritative language el | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://athens.euronext.com/sites/default/files/2025-12/RESOLUTION_Nr5-ATHEXCSD_383_24.11.2025_FORCE%208.12.2025.DOC.pdf
LIMITATION: Informational English translation; the Greek text prevails. Resolution 5 codified to 24 November 2025 (effective 8 December 2025).
LIMITATION: Business hours, cycles and algorithm specifics are announced through the DSS and are not in the library (gap G12).
EXCERPT (Resolution 5 Part 2 §§2.1–2.2; PDF 4):
PART 2. Settlement Methods

2.1 Settlement methods
ATHEXCSD settles transactions on the basis of the settlement methods laid down in Section V of the
Rulebook and the provisions of Commission Delegated Regulation (EU) 2017/392 and Commission
Implementing Regulation (EU) 2017/394.

For the purposes of cash settlement, ATHEXCSD blocks cash balances in the Cash Settlement Accounts.
Specifically in the case of cash settlement carried out in TARGET-GR with the participation of Settlement
Banks, the aforesaid balances are blocked through TARGET-GR in the respective Sub-accounts kept by
Settlement Banks for Participants.


2.2 Technical details
Any procedural or technical details relating to settlement operations, as set forth in the Rulebook and this
Resolution, for instance with respect to settlement methods, the business hours and performance of
settlement, the particular specifications of the settlement algorithm, or the number and duration of
settlement cycles, shall be determined in accordance with the technical procedures of ATHEXCSD which
are announced by ATHEXCSD to Participants through the DSS or by any other appropriate means of
notifying and communicating with them.

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Athens", "service": "settlement", "role": "participant", "mode": "current", "question_type": "athens_dss_technical_cycles"}
STATUS: blocked — DSS technical announcements defining cycles, cut-offs and formats are not in reviewed evidence.
GAP IDS: ['G12']
ROUTER NOTES: {"_note": "explicitly blocked topic"}