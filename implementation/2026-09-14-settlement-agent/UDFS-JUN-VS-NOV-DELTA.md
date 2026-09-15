# June (R2026.JUN) versus November (R2026.NOV) UDFS — normalised sentence comparison of selected settlement sections

Research date 2026-09-14. Method: both texts derived with pdftotext -layout; margin line numbers, running headers/footers, section numbers, cross-reference page numbers, footnote number tokens, bullet glyphs and figure-caption formatting removed; text lower-cased, re-flowed and split into sentences; sentence-level unified diff. Limits: textual comparison of the listed ranges only; diagrams and image-rendered tables are not compared; the message table §2.3.8/§4.3.8 was excluded because its column layout extracts differently in the two files; residual differences may be normalisation artefacts and must be read against the originals. This comparison does not establish that R2026.NOV is deployed.

## matching
- June 1.6.1.2 Matching (PDF 267–272, 38 sentences) vs November 3.6.1.2 Matching (PDF 279–284, 39 sentences); similarity 0.8987; 31 residual sentence differences (inspect below)
```
-193 the under insolvency situation will be activated upon request of a csd or cb as explained in the manual of operational procedures (mop).
-diagram 54 - matching application pocess 2 overview t2s provides t2s actors matching services for settlement instructions that require to be matched in t2s (i.e.
+figure 54:
+matching application pocess overview t2s provides t2s actors matching services for settlement instructions that require to be matched in t2s (i.e.
-the matching of cancellation instructions does not follow the rules presented in this section and is presented in section instruction cancellation  280).
+the matching of cancellation instructions does not follow the rules presented in this section and is presented in section instruction cancellation).
-mandatory matching fields are those fields that must be present in the instruction and which values should be the same in both settlement instructions except settlement amount for dvp/pfod for which a tolerance might be applied and for credit/debit code (crdt/dbit) and securities movement type deliver/receiver (deli/rece), whose values match opposite.
+mandatory matching fields are those fields that must be present in the instruction and which values should be the same in both settlement instructions except settlement amount for dvp/pfod for which a tolerance might be applied and for credit/debit code (crdt/dbit) and securities movement type deliver/ receiver (deli/rece), whose values match opposite.
-mandatory matching fields per transaction type and example 21 194 upper and lower case letters are considered as different when comparing the values of two different instructions.
-in case a given matching field is filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not subject to matching.
-non mandatory matching fields per transaction type figure 56:
-additional matching fields and example 3 non mandatory matching fields per transaction type figure 57:
-optional matching fields and example 6 if all the matching fields on both instructions match, except for the settlement amount, t2s checks if the difference between both settlement amounts is compliant with the tolerance amount configured in t2s.
+mandatory matching fields per transaction type and example non mandatory matching fields per transaction type figure 56:
+additional matching fields and example non mandatory matching fields per transaction type figure 57:
+optional matching fields and example if all the matching fields on both instructions match, except for the settlement amount, t2s checks if the difference between both settlement amounts is compliant with the tolerance amount configured in t2s.
-table 57 - tolerance amount for matching for euro 2 countervalue for the cash amount tolerance  eur eur 2  eur eur 25 in case there is more than one potentially matching settlement instruction, t2s chooses the one having the smallest settlement amount difference.
+countervalue for the cash amount tolerance  eur eur 2  eur eur 25 table 57:
+tolerance amount for matching for euro in case there is more than one potentially matching settlement instruction, t2s chooses the one having the smallest settlement amount difference.
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
-the allegement process is described below (see section allegement  271), the dialogue is reflected in section send settlement instruction.
-t2s automatically cancels settlement instructions that remain unmatched after a certain period of time (see section instruction cancellation  280 and section instructions recycling  296).
-21 parameter synthesis no specific configuration from t2s actor is needed.
+the allegement process is described below (see section allegement), the dialogue is reflected in section send settlement instruction.
+t2s automatically cancels settlement instructions that remain unmatched after a certain period of time (see section instruction cancellation and section instructions recycling).
+footnotes 1 upper and lower case letters are considered as different when comparing the values of two different instructions.
+in case a given matching field is filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not subject to matching.
+parameter synthesis no specific configuration from t2s actor is needed.
-25 concerned parameter created by updated by mandatory/ possible standard or de- process optional values fault value matching tolerance t2s operator t2s operator m to be defined 100.000 €  2€ amount 100.000 €  25€
+concerned mandatory/ possible standard or default parameter created by updated by process optional values value matching tolerance t2s operator t2s operator m to be defined 100.000 €  2€ amount 100.000 €  25€
```

## allegement
- June 1.6.1.3 Allegement (PDF 271–278, 45 sentences) vs November 3.6.1.3 Allegement (PDF 283–290, 50 sentences); similarity 0.9294; 35 residual sentence differences (inspect below)
```
-diagram 58 - allegement application process 5 overview t2s applies the allegement process for unmatched settlement instructions and unmatched cancellation instructions that require matching.
+figure 58:
+allegement application process overview t2s applies the allegement process for unmatched settlement instructions and unmatched cancellation instructions that require matching.
-diagram 59 - allegement process 2 allegement process settlementallegement if a settlement instruction does not match after the first matching attempt (see section matching  267), the counterparty is informed through an allegement message after a predefined period of time (standard delay period, that is configured in t2s reference data by the t2s operator).
+figure 59:
+allegement process allegement process settlement allegement if a settlement instruction does not match after the first matching attempt (see section matching), the counterparty is informed through an allegement message after a predefined period of time (standard delay period, that is configured in t2s reference data by the t2s operator).
-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section message subscription).
-diagram 60 - scenario a:
-standard delay period 2 scenario b:
+figure 60:
+scenario a:
+standard delay period scenario b:
-diagram 61 - scenario b:
-standard delay period exceeds isd cut off 2 cancellationofanallegementmessage if an unmatched settlement instruction is cancelled by the t2s actor, the counterparty receives a cancellation of the allegement message automatically generated by t2s.
+figure 61:
+scenario b:
+standard delay period exceeds isd cut off cancellation of an allegement message if an unmatched settlement instruction is cancelled by the t2s actor, the counterparty receives a cancellation of the allegement message automatically generated by t2s.
-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section message subscription).
-scenario a for sending a cancellation of the allegement message 9 if an unmatched settlement instruction is automatically cancelled by t2s (cancellation by the system), the counterparty receives a cancellation of the allegement message automatically generated by t2s.
-the cases that may trigger cancellation by the system of an unmatched settlement instruction as described in section instruction cancellation  280 are the following:
+scenario a for sending a cancellation of the allegement message if an unmatched settlement instruction is automatically cancelled by t2s (cancellation by the system), the counterparty receives a cancellation of the allegement message automatically generated by t2s.
+the cases that may trigger cancellation by the system of an unmatched settlement instruction as described in section instruction cancellation are the following:
-scenario b for sending a cancellation of the allegement message 4 removalofanallegementmessage in case the counterparty sends its corresponding settlement instruction to t2s, and if both instructions are matched, the counterparty receives a removal of allegement message, since the previously sent allegement is no longer valid.
+scenario b for sending a cancellation of the allegement message removal of an allegement message in case the counterparty sends its corresponding settlement instruction to t2s, and if both instructions are matched, the counterparty receives a removal of allegement message, since the previously sent allegement is no longer valid.
-interested parties can also be informed depending on their message subscription preferences (see section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section message subscription).
-scenario for sending a removal of the allegement message 12 cancellationallegement if a t2s actor sends a cancellation instruction that requires the cancellation of both legs of a settlement instruction and the counterparty has not sent its cancellation instruction, t2s sends a status advice message to the t2s actor (with no delay period) informing that its cancellation is pending and another one
+scenario for sending a removal of the allegement message cancellation allegement if a t2s actor sends a cancellation instruction that requires the cancellation of both legs of a settlement instruction and the counterparty has not sent its cancellation instruction, t2s sends a status advice message to the t2s actor (with no delay period) informing that its cancellation is pending and another one t
-diagram 65 - scenario for sending a cancellation allegement status advice 21 parameters synthesis the following parameters are specified by the t2s operator:
+figure 65:
+scenario for sending a cancellation allegement status advice parameters synthesis the following parameters are specified by the t2s operator:
-11 concerned parameter created by updated by mandatory/ possible val- standard or process optional ues default value settlement standard delay t2s operator t2s operator m to be defined 1 hour allegement period settlement before cut-off t2s operator t2s operator m to be defined 5 hours allegement
+concerned mandatory/ possible standard or parameter created by updated by process optional values default value settlement standard delay t2s operator t2s operator m to be defined 1 hour allegement period settlement before cut-off t2s operator t2s operator m to be defined 5 hours allegement
```

## amendment
- June 1.6.1.4 Instruction Amendment (PDF 277–281, 29 sentences) vs November 3.6.1.4 Instruction Amendment (PDF 289–293, 32 sentences); similarity 0.7465; 19 residual sentence differences (inspect below)
```
-diagram 66 - instruction amendment application process 2 overview t2s accepts and processes an amendment instruction sent by a t2s actor when it successfully passes the business validation process (see section business validation  218), unless any of the following conditions is fulfilled:
+figure 66:
+instruction amendment application process overview t2s accepts and processes an amendment instruction sent by a t2s actor when it successfully passes the business validation process (see section business validation), unless any of the following conditions is fulfilled:
-the referenced settlement instruction is identified as cosd and the amendment instruction does not aim to remove a linkage having the csd as the instructing party (see section conditional settlement  452);
+the referenced settlement instruction is identified as cosd and the amendment instruction does not aim to remove a linkage having the csd as the instructing party (see section conditional settlement);
-an amendment instruction can be used to amend a process indicator of both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the amendment instruction refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types  86).
-table 58 - references for amendment instruction 6 already matched settlement settlement instructions instruction matched in t2s amendment instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference amendment instruction of both legs of t2s actor reference x the settlement instruction for amendment instructions referring to both legs of the settlement in
+an amendment instruction can be used to amend a process indicator of both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the amendment instruction refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types).
+already matched settlement settlement instructions matched in instruction t2s amendment instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference amendment instruction of both legs of t2s actor reference x the settlement instruction table 58:
+references for amendment instruction for amendment instructions referring to both legs of the settlement instruction (i.e.
-linkages block (see section linked instructions  442).
+linkages block (see section linked instructions).
-linkages block (see section linked instructions  442).
+linkages block (see section linked instructions).
-table 59 - process indicators allowed for amendment 2 “partial settlement “linkages block” “priority” indicator” settlement instruction yes yes yes settlement restriction no yes yes partially settled instruction no no yes t2s informs the t2s actor on the result of the amendment process through a status advice message, as described in sections send amendment instruction of a settlement instruction
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+“partial settlement “linkages block” “priority” indicator” settlement instruction yes yes yes “partial settlement “linkages block” “priority” indicator” settlement restriction no yes yes partially settled instruction no no yes table 59:
+process indicators allowed for amendment t2s informs the t2s actor on the result of the amendment process through a status advice message, as described in sections send amendment instruction of a settlement instruction or of a settlement restriction on securities position and send amendment instruction of a settlement restriction on cash balance.
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
```

## cancellation
- June 1.6.1.5 Instruction Cancellation (PDF 280–285, 45 sentences) vs November 3.6.1.5 Instruction Cancellation (PDF 292–298, 47 sentences); similarity 0.5031; 36 residual sentence differences (inspect below)
```
-diagram 67 - instruction cancellation application process 2 overview after its validation, t2s processes cancellation instructions sent by a t2s actor to cancel previously sent settlement instructions or settlement restrictions, unless it fulfils any of the following conditions:
+figure 67:
+instruction cancellation application process overview after its validation, t2s processes cancellation instructions sent by a t2s actor to cancel previously sent settlement instructions or settlement restrictions, unless it fulfils any of the following conditions:
-the referenced settlement instruction is identified as cosd, and the instructing party is not the relevant csd or the relevant administering party (see section conditional settlement  452);
+the referenced settlement instruction is identified as cosd, and the instructing party is not the relevant csd or the relevant administering party (see section conditional settlement);
-if the cancellation instruction fulfils any of these conditions, the cancellation instruction is denied and t2s communicates its denial together with the relevant reason code to the t2s actor or any interested party, depending on their message subscription preferences (see section status management  653).
+if the cancellation instruction fulfils any of these conditions, the cancellation instruction is denied and t2s communicates its denial together with the relevant reason code to the t2s actor or any interested party, depending on their message subscription preferences (see section status management).
-cancellation process instructioncancellationprocess t2s actors can send cancellation instructions to cancel previously sent settlement instructions or settlement restrictions.
+cancellation process instruction cancellation process t2s actors can send cancellation instructions to cancel previously sent settlement instructions or settlement restrictions.
-if the referenced settlement instruction is matched, t2s requires bilateral cancellation and the cancellation is only possible if both counterparties send their cancellation instructions to cancel each leg separately or if the cancellation instruction is sent with the information of both legs by an authorised t2s party .
-a cancellation instruction can be used to cancel both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the cancellation request refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types  86).
-195 in case the csd and the party send their respective cancellation instructions for the same leg, and both remain pending in the system awaiting for their counterparty in order to match and be executed, t2s matching process prioritises for the matching the csd cancellation instruction over the party cancellation instruction.
-table 60 - references used in cancellation scenarios 2 already matched settlement settlement instructions instruction matched in t2s cancellation instruction of one leg of t2s reference t2s actor reference the settlement instruction (two cancelor lations needed) t2s reference cancellation instruction of both legs of t2s actor reference x the settlement instruction for cancellation instructions re
+if the referenced settlement instruction is matched, t2s requires bilateral cancellation and the cancellation is only possible if both counterparties send their cancellation instructions to cancel each leg separately or if the cancellation instruction is sent with the information of both legs by an authorised t2s party.
+a cancellation instruction can be used to cancel both legs at the same time or only one leg of a settlement instruction that entered t2s as already matched depending if the reference used in the cancellation request refers to the information of one leg or both legs of the settlement instruction as shown in the table below (see section instruction types).
+already matched settlement settlement instructions matched in instruction t2s cancellation instruction of one leg of t2s reference t2s actor reference the settlement instruction (two or cancellations needed) t2s reference cancellation instruction of both legs of t2s actor reference x the settlement instruction table 60:
+references used in cancellation scenarios for cancellation instructions referring to both legs of the settlement instruction (i.e.
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
-cancellationofcosdprocess when a settlement instruction is identified as cosd, only administering parties or the relevant csd can cancel it under certain circumstances:
+cancellation of cosd process when a settlement instruction is identified as cosd, only administering parties or the relevant csd can cancel it under certain circumstances:
-the administering parties only have to send one cancellation instruction regardless if more than one cosd rule applies) (see section conditional settlement  452), or;
+the administering parties only have to send one cancellation instruction regardless if more than one cosd rule applies) (see section conditional settlement), or;
-cancellationbythesystemprocess t2s automatically cancels pending instructions in the system under the following conditions:
-settlement instructions, settlement restrictions and cancellation instructions once they exceed their recycling period in t2s (see section instructions recycling  296).
-settlement instructions when the realignment chain cannot be built (see section realignment  373).
+cancellation by the system process t2s automatically cancels pending instructions in the system under the following conditions:
+settlement instructions, settlement restrictions and cancellation instructions once they exceed their recycling period in t2s (see section instructions recycling).
+settlement instructions when the realignment chain cannot be built (see section realignment).
-the revalidation process is triggered at the start of day in t2s and by a change in the reference data that affects the instruction (see section business validation  218).
-settlement instructions that during the start of day revalidation process it is detected that the realignment chain used for settlement has become invalid for the current settlement day and while a new valid realignment chain can be built, the transaction is already partially settled (see section realignment  373) pending cancellation instruction in the system when one of the conditions for the d
-(see section send cancellation instruction of a settlement instruction or a settlement restriction on securities position and section send cancellation instruction of a settlement restriction on cash balance.) parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.
+the revalidation process is triggered at the start of day in t2s and by a change in the reference data that affects the instruction (see section business validation).
+settlement instructions that during the start of day revalidation process it is detected that the realignment chain used for settlement has become invalid for the current settlement day and while a new valid realignment chain can be built, the transaction is already partially settled (see section realignment) pending cancellation instruction in the system when one of the conditions for the denial
+(see section send cancellation instruction of a settlement instruction or a settlement restriction on securities position and section send cancellation instruction of a settlement restriction on cash balance.) footnotes 1 in case the csd and the party send their respective cancellation instructions for the same leg, and both remain pending in the system awaiting for their counterparty in order to
+parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.
```

## hold_release
- June 1.6.1.6 Hold and Release (PDF 284–297, 147 sentences) vs November 3.6.1.6 Hold and Release (PDF 297–311, 156 sentences); similarity 0.8312; 69 residual sentence differences (inspect below)
```
-table 61 - references used for hold/release instruction 2 already matched settlement settlement instructions instruction matched in t2s hold/release instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference hold/release instruction of both legs t2s actor reference x of the settlement instruction for hold/release instructions referring to both legs of 
+already matched settlement settlement instructions matched in instruction t2s hold/release instruction of one leg of t2s reference t2s actor reference the settlement instruction or t2s reference hold/release instruction of both legs t2s actor reference x of the settlement instruction table 61:
+references used for hold/release instruction for hold/release instructions referring to both legs of the settlement instruction (i.e.
-additionally, t2s automatically puts a settlement instruction on hold if it fulfils any restriction defined by the csds, known as csd validation hold or party hold (see section business validation  218) or if it is identified as a cosd on the intended settlement date (see section conditional settlement  452).
+additionally, t2s automatically puts a settlement instruction on hold if it fulfils any restriction defined by the csds, known as csd validation hold or party hold (see section business validation) or if it is identified as a cosd on the intended settlement date (see section conditional settlement).
-nevertheless, these instructions can be matched, amended or cancelled (however settlement instructions on cosd hold cannot be amended and can only be cancelled following specific rules - see section instruction cancellation  280).
-diagram 68 - hold and release application process 2 overview the hold/release instruction has two hold indicators that can be filled by the t2s actor:
+nevertheless, these instructions can be matched, amended or cancelled (however settlement instructions on cosd hold cannot be amended and can only be cancelled following specific rules - see section instruction cancellation).
+figure 68:
+hold and release application process overview the hold/release instruction has two hold indicators that can be filled by the t2s actor:
-in case of a settlement instruction put on hold by t2s due to a csd validation hold, it can only be released by the relevant csd that defined the rule (see section business validation  218).
+in case of a settlement instruction put on hold by t2s due to a csd validation hold, it can only be released by the relevant csd that defined the rule (see section business validation).
-(see section conditional settlement  452).
+(see section conditional settlement).
-nevertheless, t2s does not allow t2s actors to put on hold settlement instructions already identified as cosd (see section conditional settlement  452).
+nevertheless, t2s does not allow t2s actors to put on hold settlement instructions already identified as cosd (see section conditional settlement).
-table 62 - hold /release exhaustive scenarios for a settlement instruction 22 settlement instruction party hold csd hold csd validation cosd hold result hold no no no no eligible for settlement yes yes yes yes no settlement attempt can be performed yes yes yes no no settlement attempt can be performed yes yes no no no settlement attempt can be performed party hold indicator can be i) instructed b
-settlement instruction party hold csd hold csd validation cosd hold result hold yes no no yes no settlement attempt can be performed no no yes yes no settlement attempt can be performed no yes yes yes no settlement attempt can be performed no yes no no no settlement attempt can be performed yes no no no no settlement attempt can be performed no no yes no no settlement attempt can be performed yes
-if an instruction remains on hold at the end of its intended settlement date, t2s recycles the instruction following the t2s recycling rules (see section instructions recycling  296).
-197 no settlement attempt can be performed unless the settlement instruction is under partial release process and partial settlement of settlement instructions under partial release process is allowed (i.e.
-real time settlement or sequence x of night time settlement is running) (see section partial settlement  343).
+settlement instruction csd validation party hold csd hold cosd hold result hold 1 no no no no eligible for settlement 2 yes yes yes yes no settlement attempt can be performed 3 yes yes yes no no settlement attempt can be performed 4 yes yes no no no settlement attempt can be performed 5 yes no no yes no settlement attempt can be performed settlement instruction csd validation party hold csd hold 
+table 62:
+hold /release exhaustive scenarios for a settlement instruction if an instruction remains on hold at the end of its intended settlement date, t2s recycles the instruction following the t2s recycling rules (see section instructions recycling).
+footnotes 1 party hold indicator can be i) instructed by the t2s actor ii) put automatically by t2s upon the fulfilment of a restriction type case 1 or, iii) put automatically by t2s if it has not been set and the “hold release default” value of the securities account included in the instruction is set to “hold”.
+2 no settlement attempt can be performed unless the settlement instruction is under partial release process and partial settlement of settlement instructions under partial release process is allowed (i.e.
+real time settlement or sequence x of night time settlement is running) (see section partial settlement).
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
-example 78 - hold instruction this example illustrates the execution of two different hold instructions for the settlement instruction “x”, which is matched with settlement instruction “y”, before the intended settlement date:
+example 78:
+hold instruction this example illustrates the execution of two different hold instructions for the settlement instruction “x”, which is matched with settlement instruction “y”, before the intended settlement date:
-diagram 69 - both the t2s party and the relevant csd send a hold instruction 2 release process when a t2s actor sends a release instruction, t2s proceeds to execute it, once checked that the referenced instruction is not:
+figure 69:
+both the t2s party and the relevant csd send a hold instruction release process when a t2s actor sends a release instruction, t2s proceeds to execute it, once checked that the referenced instruction is not:
-if t2s successfully executes the release instruction, the t2s actor is informed through a message communicating the execution of the release instruction and a status advice message informing if other hold remains as described in send hold/release instruction.
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+if t2s successfully executes the release instruction, the t2s actor is informed through a message communicating the execution of the release instruction and a status advice message informing if other hold remains as described in send hold/release instruction .
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
-example 79 - release instruction continuing with the previous, this one illustrates the case when the t2s party sends its release instruction for settlement instruction “x”, leaving the instruction “x” on csd hold until the release from the csd is received and executed:
+example 79:
+release instruction continuing with the previous, this one illustrates the case when the t2s party sends its release instruction for settlement instruction “x”, leaving the instruction “x” on csd hold until the release from the csd is received and executed:
-then, settlement instruction “x” changes from scenario 4 to scenario 8 in table - hold /release exhaustive scenarios for a settlement instruction  287.
+then, settlement instruction “x” changes from scenario 4 to scenario 8 in hold/release exhaustive scenarios for a settlement instruction.
-the party sends a release instruction 17 the csd sends a release instruction for csd hold, t2s validates successfully the instruction and proceeds to release the referenced settlement instruction putting “no” in its csd hold indicator.
+the party sends a release instruction the csd sends a release instruction for csd hold, t2s validates successfully the instruction and proceeds to release the referenced settlement instruction putting “no” in its csd hold indicator.
-thus, settlement instruction “x” changes from scenario 8 to scenario 1 in table - hold /release exhaustive scenarios for a settlement instruction  287.
-diagram 71 - the t2s party sends a release instruction 6 hold/release default for settlement instructions when a t2s actor sends a settlement instruction, t2s checks if the settlement instruction has the party hold status set (i.e.
+thus, settlement instruction “x” changes from scenario 8 to scenario 1 in hold/release exhaustive scenarios for a settlement instruction.
+figure 71:
+the t2s party sends a release instruction hold/release default for settlement instructions when a t2s actor sends a settlement instruction, t2s checks if the settlement instruction has the party hold status set (i.e.
-in case the party hold status is not set, t2s checks in reference data the “hold release default” value of the securities account included in the instruction 198:
+in case the party hold status is not set, t2s checks in reference data the “hold release default” value of the securities account included in the instruction:
-198 internally generated instructions are not considered for hold/release default.
+footnotes 1 internally generated instructions are not considered for hold/release default.
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
-once executed, a partially released settlement instruction will be submitted to a settlement attempt depending on the phase of the day (see section partial settlement  343) if it is executed during the night time settlement, the partially released settlement instruction will only be submitted to a settlement attempt when the corresponding sequence runs.
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
+once executed, a partially released settlement instruction will be submitted to a settlement attempt depending on the phase of the day (see section partial settlement) if it is executed during the night time settlement, the partially released settlement instruction will only be submitted to a settlement attempt when the corresponding sequence runs.
-areleaseinstruction over the referenced instruction is received;
+a release instruction over the referenced instruction is received;
-example 80 - partial release process this example illustrates the execution of a release instruction that aims to partially release settlement instruction “x”, which has its party hold indicator already set to “yes”.
+example 80:
+partial release process this example illustrates the execution of a release instruction that aims to partially release settlement instruction “x”, which has its party hold indicator already set to “yes”.
-the settlement instruction “x” remains in scenario 9 of table - hold /release exhaustive scenarios for a settlement instruction  287 throughout the entire partial release process and also after its ending.
-diagram 72 - the party sends a release instruction to partially release a settlement instruction 21 parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.
+the settlement instruction “x” remains in scenario 9 of hold/release exhaustive scenarios for a settlement instruction throughout the entire partial release process and also after its ending.
+figure 72:
+the party sends a release instruction to partially release a settlement instruction parameters synthesis no specific configuration from t2s actor is needed in t2s reference data.
```

## recycling
- June 1.6.1.7 Instructions Recycling (PDF 296–304, 48 sentences) vs November 3.6.1.7 Instructions Recycling (PDF 310–318, 54 sentences); similarity 0.9097; 38 residual sentence differences (inspect below)
```
-instructions recycling concept at each end of a settlement day (see section settlement day  155), t2s recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in t2s, before being cancelled by the system.
-diagram 73 - instruction recycling application process 7 overview the recycling of an instruction in t2s triggers the revalidation process at the start of day, as described in section business validation  218.
+instructions recycling concept at each end of a settlement day (see section settlement day), t2s recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in t2s, before being cancelled by the system.
+figure 73:
+instruction recycling application process overview the recycling of an instruction in t2s triggers the revalidation process at the start of day, as described in section business validation.
-for more information on status changes see section status management  653.
+for more information on status changes see section status management.
-recycling period for unmatched settlement instructions 11 unmatched cancellation instructions that need to be matched in t2s are recycled for a period of working days configured by the t2s operator, starting from its reception in t2s until its matching occurs.
-199 current recycling period for unmatched instructions of working days.
+recycling period for unmatched settlement instructions unmatched cancellation instructions that need to be matched in t2s are recycled for a period of working days configured by the t2s operator, starting from its reception in t2s until its matching occurs.
-recycling period for unmatched cancellation instructions 2 pending matched instructions and settlement restrictions are recycled in t2s for a period of working days configured by the t2s operator until its settlement or cancellation occurs (see section instruction cancellation  280).
+recycling period for unmatched cancellation instructions pending matched instructions and settlement restrictions are recycled in t2s for a period of working days configured by the t2s operator until its settlement or cancellation occurs (see section instruction cancellation).
-12 13 14 200 current recycling period for matched instructions of working days.
-diagram 76 - recycling period for matched instructions 2 t2s does not send a daily message to the t2s actors informing about the result of the recycling process.
+figure 76:
+recycling period for matched instructions t2s does not send a daily message to the t2s actors informing about the result of the recycling process.
-the dialogue is reflected in section send settlement instruction.
-interested parties can also be informed depending on their message subscription preferences (see section status management  653 and section message subscription  135).
+the dialogue is reflected in section send settlement instruction .
+interested parties can also be informed depending on their message subscription preferences (see section status management and section message subscription).
-diagram 77 - recycling period for unmatched settlement instructions (entry date the same day of isd and without any status update during its lifecycle) 3 a settlement instruction enters in t2s on business day .04.2016 as unmatched and with isd same day (27.04.2016).
+figure 77:
+recycling period for unmatched settlement instructions (entry date the same day of isd and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched and with isd same day (27.04.2016).
-diagram 78 - recycling period for unmatched settlement instructions (isd in the future and without any status update during its lifecycle) 11 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).
+figure 78:
+recycling period for unmatched settlement instructions (isd in the future and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).
-diagram 79 - recycling period for unmatched settlement instructions (isd in the future and a hold status update during its lifecycle) 7 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).
+figure 79:
+recycling period for unmatched settlement instructions (isd in the future and a hold status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the future (04.05.2016).
-diagram 80 - recycling period for unmatched settlement instructions (isd in the past and without any status update during its lifecycle) 3 a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the past (26.04.2016).
+figure 80:
+recycling period for unmatched settlement instructions (isd in the past and without any status update during its lifecycle) a settlement instruction enters in t2s on business day .04.2016 as unmatched with isd in the past (26.04.2016).
-9 parameters synthesis no specific configuration from t2s actor is needed.
+footnotes 1 current recycling period for unmatched instructions of working days.
+2 current recycling period for matched instructions of working days.
+parameters synthesis no specific configuration from t2s actor is needed.
-13 concerned parameter created by updated by mandatory/ possible val- standard or process optional ues default value recycling recycling period t2s operator t2s operator m n/a 20 working days for unmatched instructions recycling recycling period t2s operator t2s operator m n/a 60 working days for matched instructions
+concerned mandatory/ possible standard or parameter created by updated by process optional values default value recycling recycling t2s operator t2s operator m n/a 20 working period for days unmatched instructions recycling recycling t2s operator t2s operator m n/a 60 working period for days matched instructions
```

## posting_overview
- June 1.6.1.8 Posting (PDF 303–306, 31 sentences) vs November 3.6.1.8 Posting (PDF 317–321, 33 sentences); similarity 0.8685; 16 residual sentence differences (inspect below)
```
-it may resort to the optimising application process if needed for the settlement (see section optimising  335).
+it may resort to the optimising application process if needed for the settlement (see section optimising).
-diagram 81 - settlement application processes / posting 13 overview settlement instructions, settlement restrictions and liquidity transfers, sent by the t2s actors or automatically generated by t2s, are submitted to the posting application process at the intended settlement date.
-they can be submitted to the posting application process individually or grouped with other settlement instructions or settlement restrictions or liquidity transfers due to links set by t2s actors or by t2s application processes (see section linked instructions  442).
+figure 81:
+settlement application processes / posting overview settlement instructions, settlement restrictions and liquidity transfers, sent by the t2s actors or automatically generated by t2s, are submitted to the posting application process at the intended settlement date.
+they can be submitted to the posting application process individually or grouped with other settlement instructions or settlement restrictions or liquidity transfers due to links set by t2s actors or by t2s application processes (see section linked instructions).
-in case of failure 201:
+in case of failure:
-they are then submitted to the posting application process including an optimisation in order to identify sets that can settle successfully (see section settlement day  155).
+they are then submitted to the posting application process including an optimisation in order to identify sets that can settle successfully (see section settlement day).
-in case of a high-volume event of corporate actions, failing transactions will be submitted to a dedicated process for optimisation triggered at regular time intervals the provision check, which determines the relevant securities positions, cash balances and limits on the involved accounts and the associated credit memorandum balance.
-in case of lack of cash, lack of securities or insufficient external guarantee headroom, partial settlement (see section partial settlement  343) and auto-collateralisation (see section auto-collateralisation  352) can be used under specific conditions;
+the provision check, which determines the relevant securities positions, cash balances and limits on the involved accounts and the associated credit memorandum balance.
+in case of lack of cash, lack of securities or insufficient external guarantee headroom, partial settlement (see section partial settlement) and auto-collateralisation (see section auto-collateralisation) can be used under specific conditions;
+footnotes 1 in case of a high-volume event of corporate actions, failing transactions will be submitted to a dedicated process for optimisation triggered at regular time intervals
```

## partial_settlement
- June 1.6.1.9.3 Partial Settlement (PDF 343–353, 116 sentences) vs November 3.6.1.9.3 Partial Settlement (PDF 362–371, 125 sentences); similarity 0.4183; 99 residual sentence differences (inspect below)
```
-partialsettlementprocess partial settlement process for settlement instructions a settlement instruction is partially settled , in case there are insufficient securities to settle the full quantity and provided the following conditions are met:
+partial settlement process partial settlement process for settlement instructions a settlement instruction is partially settled, in case there are insufficient securities to settle the full quantity and provided the following conditions are met:
-partial settlement window partial settlement is active in t2s within the dedicated partial settlement windows .
+partial settlement window partial settlement is active in t2s within the dedicated partial settlement windows.
-224 partial settlement is triggered only in case of lack of securities (i.e.
-lack of securities only or lack of securities and cash) but not in case of lack of cash only.
-225 partially released settlement instructions can be submitted for settlement attempts for the total partially released quantity also when the partial settlement window is not running.
-partially released settlement instructions can be submitted for settlement attempts for a part of the partially released quantity only when the partial settlement window is running.
-226 for details about the schedule of partial settlement window, see section settlement day  155 227 including such settlement instructions which are on party hold and have been partially released.
-partial settlement of partially released settlement instructions a settlement instruction on party hold may be partially released to allow the partial settlement of a specified quantity.
+partial settlement of partially released settlement instructions the following two cases can be distinguished:
+partial release when only a party hold is present on the instruction partial release when both a party hold and a cosd hold are present on the instruction in the case where only a party hold is present on the instruction, it may be partially released to allow the partial settlement of a specified quantity.
+in the case where both a party hold and a cosd hold are present on the instruction, the party hold may be partially released which will trigger the blocking of securities.
+if the blocking of the securities is successful, the partial release will be kept pending even at cut-off, until the corresponding blocked quantity is partially cosd released and settled.
+at this time the partial release is considered settled, and an additional release is possible.
+if the attempt to block the securities is unsuccessful (in case the available quantity is lower than the quantity to be blocked), it is recycled until the applicable cut-off, after which the partial release will be cancelled, and the underlying settlement instruction is set back on party hold for the full unsettled quantity.
-meaning the partial settlement cannot take place for an amount lower than an applicable value.25 table 68 - applicable threshold types for partial settlement 2 content of settlement instruction resulting resulting applicable applicable threshold value instruction instruction isin currency threshold type threshold type type fop 228 n/a applicable n/a quantity minimum settlement unit (only for firs
-both matched settlement instructions dvp/dwp not set to “quantity” unit-quoted applicable cash value amount configured in the currency for both matched setspecified (for quantity, minimum tlement instructions settlement unit and settlement unit multiple are used).
-nominal- amount configured in the currency quoted specified (for quantity, minimum settlement unit and settlement unit multiple are used).
-the parameters determining the threshold applicable above are set:
+meaning the partial settlement cannot take place for an amount lower than an applicable value.
+content of settlement instruction resulting applicable resulting applicable instruction instruction threshold threshold value isin currency type threshold type type fop n/a applicable n/a quantity minimum settlement unit (only for first partial settlement) and settlement unit multiple are used.
+dvp/dwp set to “quantity” for both matched settlement instructions dvp/dwp not set to “quantity” unit-quoted applicable cash value amount configured in the for both matched currency specified (for quantity, settlement minimum settlement unit and instructions settlement unit multiple are used).
+nominal- amount configured in the quoted currency specified (for quantity, minimum settlement unit and settlement unit multiple are used).
+table 68:
+applicable threshold types for partial settlement the parameters determining the threshold applicable above are set:
-by the t2s actors in charge of the administration of the relevant isin in the static data for the applicable threshold in quantity (see section concept of securities in t2s  71).
+by the t2s actors in charge of the administration of the relevant isin in the static data for the applicable threshold in quantity (see section concept of securities in t2s).
-229 in case the settlement instruction does not settle, the settlement instruction is submitted to optimising application process.
+in case the settlement instruction does not settle, the settlement instruction is submitted to optimising application process.
-228 cash value thresholds are not considered for fop regardless of the partial settlement threshold type (partial settlement indicator parc, part) defined within the settlement instruction.
-this also applies for fop instructions related to a foreign currency transaction (non-eur amount).
-229 partially released settlement instructions are only submitted to partial settlement attempts for the released quantity.
-in both cases, the status of each matched settlement instruction and the related reporting are sent to the t2s parties, as described in section send settlement instruction and in chapter 3 for the related content of the message.
+in both cases, the status of each matched settlement instruction and the related reporting are sent to the related content of the message.
-or cancelled for its pending leg (see section instruction cancellation  280).
+or cancelled for its pending leg (see section instruction cancellation).
-the partial release process is cancelled when the released quantity has not fully settled by the relevant cut-off time.
+in case there is only a party hold on the settlement instruction, the partial release process is cancelled when the released quantity has not fully settled by the relevant cut-off time.
+in case there is both a party hold and a cosd hold on the settlement instruction, the partial release process is not cancelled at the relevant cut-off time.
+the partial release process is only cancelled, and the settlement instruction is put back on hold if the activation of the cosd rule set is still unsuccessful (the securities cannot be blocked) at cut-off or if the related settlement restriction is cancelled during revalidation.
-example 90 - partial settlement 2 result fop set to “yes - “quanti- minimum n/a 55 n/a status of the settlement instruc- quantity” by ty” settlement tion is “partially settled”.
-the both t2s parunit set to settled part of the settlement ties “50” and instruction is “55”.
-the pending settlement part of the settlement instruction unit multiple is “45” which becomes the reset to “5” maining quantity.
+example 90:
+partial settlement result fo set to “yes - “quantit minimum n/a 55 n/a status of the settlement p quantity” by y” settlement instruction is “partially settled”.
+both t2s unit set to the settled part of the parties “50” and settlement instruction is “55”.
+settlement the pending part of the unit multiple settlement instruction is “45” set to “5” which becomes the remaining quantity.
-fop set to “yes - “quanti- minimum n/a 57 n/a status of the settlement instruc- quantity” by ty” settlement tion is “partially settled”.
-the only one t2s unit set to settled part of the settlement parties “50” and instruction is “55”.
-the pending settlement part of the settlement instruction unit multiple is “45” which becomes the reset to “5” maining quantity.
+fo set to “yes - “quantit minimum n/a 57 n/a status of the settlement p quantity” by y” settlement instruction is “partially settled”.
+only one t2s unit set to the settled part of the parties “50” and settlement instruction is “55”.
+settlement the pending part of the unit multiple settlement instruction is “45” set to “5” which becomes the remaining quantity.
-result fop set to “yes - “quanti- minimum n/a 49 n/a impossible to apply the partial quantity” by ty” settlement settlement, since the quantity both t2s parunit set to available for a partial settlement ties “50” and is “49” where the minimum setsettlement tlement multiple is set to “50”.
-unit multiple status of the settlement instrucset to “5” tion is “unsettled”.
-result dvp/ set to “yes - “quanti- minimum 100, .0 55 1, ,0 status of the settlement instruc- dwp quantity” by ty” settlement 0 00.00 tion is “partially settled”.
-the both t2s parunit set to settled part of the settlement ties “50” and instruction is “55” for the quantisettlement ty and “55, .00” for the unit multiple amount.
-the pending part of the set to “5” settlement instruction is “45” which becomes the remaining quantity and “45, .00” which becomes the remaining amount.
+fo set to “yes - “quantit minimum n/a 49 n/a impossible to apply the partial p quantity” by y” settlement settlement, since the quantity both t2s unit set to available for a partial settlement parties “50” and is “49” where the minimum settlement settlement multiple is set to unit multiple “50”.
+status of the settlement set to “5” instruction is “unsettled”.
+result dv set to “yes - “quantit minimum 100, .
+55 1, , status of the settlement p/ quantity” by y” settlement instruction is “partially settled”.
+dw both t2s unit set to the settled part of the p parties “50” and settlement instruction is “55” for settlement the quantity and “55, .00” for unit multiple the amount.
+the pending part of set to “5” the settlement instruction is “45” which becomes the remaining quantity and “45, .00” which becomes the remaining amount.
-dvp/ set to “yes - “cash .000€ 100 100, .0 55 60, .
-status of the settlement instruc- dwp quantity” by value” 0 00 tion is “partially settled”.
-the only one t2s settled part of the settlement parties instruction is “55” for the quantity and “55, .00” for the amount.
+dv set to “yes - “cash .000€ 100 100, .
+55 60, status of the settlement p/ quantity” by value” 00 .00 instruction is “partially settled”.
+dw only one t2s the settled part of the p parties settlement instruction is “55” for the quantity and “55, .00” for the amount.
-dvp/ set to “yes - “quanti- minimum 100, .0 49 1, ,0 impossible to apply the partial result dwp quantity” by ty” settlement 0 00.00 settlement, since the quantity both t2s parunit set to available for a partial settlement ties “50” and is “49” where the minimum setsettlement tlement unit is set to “50”.
-status unit multiple of the settlement instruction is set to “5” “unsettled”.
+dv set to “yes - “quantit minimum 100, .
+49 1, , impossible to apply the partial p/ quantity” by y” settlement 000.00 settlement, since the quantity dw both t2s unit set to available for a partial settlement p parties “50” and is “49” where the minimum settlement settlement unit is set to “50”.
+unit multiple status of the settlement set to “5” instruction is “unsettled”.
-in all cases, the statuses of the settlement restrictions and the related reporting are sent to the t2s parties, as described in section send settlement restriction on securities position and section send settlement restriction on cash balance and in chapter 3 for the related content of the message.
-partial settlement process for liquidity transfers t2s settles liquidity transfer for a partial amount in case sufficient cash is not available on the t2s dedicated cash account, without submitting it to the optimising application process.
+in all cases, the statuses of the settlement restrictions and the related reporting are sent to the t2s parties, as described in section send settlement restriction on securities position and section send settlement partial settlement process for liquidity transfers t2s settles liquidity transfer for a partial amount in case sufficient cash is not available on the t2s dedicated cash account, with
-when the liquidity transfer is initiated by a t2s actor different from the account holder (see section liquidity management  575).
+when the liquidity transfer is initiated by a t2s actor different from the account holder (see section liquidity management).
-in all cases, the statuses of the liquidity transfer and the related reporting are sent to the t2s parties, as described in sections send immediate liquidity transfer, execution of liquidity transfer from rtgs to t2s and execution of standing and predefined liquidity transfer orders from t2s to rtgs for dialogue related to liquidity transfer, and in chapter 3 for the related content of the messag
-parameters synthesis 2 concerned parameter created by updated by mandato- possible standard or de- process ry/ op- values fault value tional partial settlement threshold in cash t2s operator t2s operator m amount per currency:
-on settlement value for unit quotequivalent to instructions ed securities , .00€ partial settlement threshold in cash t2s operator t2s operator m amount per currency:
-on settlement value for nominal equivalent to instructions amount quoted , .00€ securities partial settlement threshold in quan- t2s actor t2s actor m quantity to be defined per on settlement tity:
-minimum maintaining isin maintaining instructions settlement unit the isin the isin partial settlement threshold in quan- t2s actor t2s actor m quantity to be defined per on settlement tity:
-settlement unit maintaining isin maintaining instructions multiple the isin the isin
+in all cases, the statuses of the liquidity transfer and the related reporting are sent to the t2s parties, as described in sections send immediate liquidity transfer, execution of liquidity transfer from rtgs to t2s and execution of standing and predefined liquidity transfer orders from t2s to rtgs for dialogue related parameters synthesis concerned mandatory possible standard or parameter creat
+settlement on value for unit equivalent to settlement quoted securities , .00€ instructions partial threshold in cash t2s operator t2s operator m amount per currency:
+settlement on value for nominal equivalent to settlement amount quoted , .00€ instructions securities partial threshold in t2s actor t2s actor m quantity to be defined per settlement on quantity:
+minimum maintaining maintaining isin settlement settlement unit the isin the isin instructions partial threshold in t2s actor t2s actor m quantity to be defined per settlement on quantity:
+maintaining maintaining isin settlement settlement unit the isin the isin instructions multiple footnotes 1 partial settlement is triggered only in case of lack of securities (i.e.
+lack of securities only or lack of securities and cash) but not in case of lack of cash only.
+2 partially released settlement instructions can be submitted for settlement attempts for the total partially released quantity also when the partial settlement window is not running.
+partially released settlement instructions can be submitted for settlement attempts for a part of the partially released quantity only when the partial settlement window is running.
+3 for details about the schedule of partial settlement window, see section settlement day 4 including such settlement instructions which are on party hold and have been partially released.
+5 cash value thresholds are not considered for fop regardless of the partial settlement threshold type (partial settlement indicator parc, part) defined within the settlement instruction.
+this also applies for fop instructions related to a foreign currency transaction (non-eur amount).
+6 partially released settlement instructions are only submitted to partial settlement attempts for the released quantity.
```

## realignment_concept
- June 1.6.1.10 Realignment (PDF 373–377, 47 sentences) vs November 3.6.1.10 Realignment (PDF 393–396, 48 sentences); similarity 0.9924; 11 residual sentence differences (inspect below)
```
-diagram 85 - realignment application process 11 overview upon the matching of settlement instructions, or upon the validation of already matched settlement instructions, the realignment application process verifies if the incoming business settlement instructions are requiring realignment settlement instructions on securities accounts other than those of the submitting t2s actors (e.g.
+figure 85:
+realignment application process overview upon the matching of settlement instructions, or upon the validation of already matched settlement instructions, the realignment application process verifies if the incoming business settlement instructions are requiring realignment settlement instructions on securities accounts other than those of the submitting t2s actors (e.g.
-realignment process parametersnecessaryforrealignment role and links between csds for cross-csd and external-csd settlement irrespective of whether it is a cross-csd or an external-csd settlement, a csd is defined for the realignment process as:
+realignment process parameters necessary for realignment role and links between csds for cross-csd and external-csd settlement irrespective of whether it is a cross-csd or an external-csd settlement, a csd is defined for the realignment process as:
-for a given isin, an investor csd can define several such investor-type csd links, meaning that it can define several technical issuer csds for a given isin.
+for a given isin, an investor csd can define several such investortype csd links, meaning that it can define several technical issuer csds for a given isin.
-2 parameters definition security csd links each investor csd has to define at least one technical issuer csd per securities it intends to set as eligible for settlement (see section securities reference data  71).
+parameters definition security csd links each investor csd has to define at least one technical issuer csd per securities it intends to set as eligible for settlement (see section securities reference data).
-(see section configuration of securities accounts for cross-csd settlement and external csd settlement  97) this set-up is used by t2s to derive the realignment chain applicable to matched settlement instructions starting either from both investor csds (delivering and receiving) up to the issuer csd(s) of the traded securities when default links are used, or from the delivering investor csd up to
+(see section configuration of securities accounts for cross-csd settlement and external csd settlement) this set-up is used by t2s to derive the realignment chain applicable to matched settlement instructions starting either from both investor csds (delivering and receiving) up to the issuer csd(s) of the traded securities when default links are used, or from the delivering investor csd up to the
```

## linked_overview
- June 1.6.1.11 Linked Instructions (PDF 442–443, 7 sentences) vs November 3.6.1.11 Linked Instructions (PDF 467–468, 7 sentences); similarity 1.0000; no sentence-level difference after normalisation

## cosd_concept
- June 1.6.1.12 Conditional Settlement (PDF 452–455, 26 sentences) vs November 3.6.1.12 Conditional Settlement (PDF 478–482, 32 sentences); similarity 0.9207; 14 residual sentence differences (inspect below)
```
-252 for details about the pre-emption, see section securities blocking/reservation/earmarking  486.
-diagram 121 - conditional settlement application process 2 t2s automatically detects and performs conditional settlement, based on cosd rules defined and maintained by each csd in the static data.
+figure 121:
+conditional settlement application process t2s automatically detects and performs conditional settlement, based on cosd rules defined and maintained by each csd in the static data.
-253 the matched settlement instructions (and their linked t2s generated realignment settlement instructions if any) remain pending and the securities and/or cash remain blocked until t2s receives:
+the matched settlement instructions (and their linked t2s generated realignment settlement instructions if any) remain pending and the securities and/or cash remain blocked until t2s receives:
+if the cosd rule set is flagged to allow for partial release, it is also possible for the administering parties to perform a partial cosd release.
+the partial cosd release is only allowed for rule sets which block securities only.
+it cannot be applied on cosd rule sets which block securities and cash or cash only.
-t2s may also cancel the settlement instruction and/or the t2s generated settlement instruction following the revalidation process (see section business validation  218) and changes in the realignment chain (see section realignment  373).
+t2s may also cancel the settlement instruction and/or the t2s generated settlement instruction following the revalidation process (see section business validation) and changes in the realignment chain (see section realignment).
+footnotes 1 in case a settlement instruction meets the cosd rule and there is no securities (resp.
+no cash) to be blocked due to a pfod (rep.
+due to a a fop), then no cosd blocking occurs.
```

## status_mgmt_concept
- June 1.6.3.1 Status Management (PDF 653–657, 9 sentences) vs November 3.6.3.1 Status Management (PDF 700–704, 9 sentences); similarity 1.0000; no sentence-level difference after normalisation

## schedule
- June 1.4.2 T2S schedule (PDF 156–159, 45 sentences) vs November 3.4.2 T2S schedule (PDF 169–172, 45 sentences); similarity 0.9994; 4 residual sentence differences (inspect below)
```
-t2s schedule the t2s schedule is under the control of the t2s operator, for creation of any new timelines, changing and/or deletion of existing time for a period or event.
+t2s schedule the t2s schedule is under the control of the t2s operator, for creation of any new timelines, changing and/ or deletion of existing time for a period or event.
-t2s manages the transition between the various periods (see section settlement day high level schedule  158) as an event.
+t2s manages the transition between the various periods (see section settlement day high level schedule) as an event.
```

## rts_phase
- June 1.4.4.4 Real-time settlement (RTS) (PDF 193–195, 25 sentences) vs November 3.4.4.4 Real-time settlement (RTS) (PDF 204–206, 25 sentences); similarity 0.7135; 10 residual sentence differences (inspect below)
```
-143 additionally t2s performs a settlement attempt for any new intraday settlement instructions, settlement restrictions and liquidity transfers validated and accepted during real-time settlement period;
+additionally t2s performs a settlement attempt for any new intraday settlement instructions, settlement restrictions and liquidity transfers validated and accepted during real-time settlement period;
-143 during the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been attempted for settlement.
-this serialization process will concern all transactions with age  3 selected by the regular recycling process following a credit in securities or cash or an increase in cmb headroom or limit, guaranteeing that an older transaction will be attempted before a younger one with the same priority.
-the transactions selected by one given recycling process will be segregated into eight groups, depending on their priority and age:
-group 1 group 2 group 3 group 4 group 5 group 6 group 7 group 8 priority 1 priority 1 priority 2 priority 2 priority 3 priority 3 priority 4 priority 4 age  3 age  3 age  3 age  3 age  3 age  3 age  3 age  3 should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to the regular recycling process.
+footnotes 1 during the regular recycling, the mechanism ensures that a transaction will not be recycled if the transaction sent just before has not been attempted for settlement.
+this serialization process will concern all transactions with age  3 selected by the regular recycling process following a credit in securities or cash or an increase in cmb headroom or limit, guaranteeing that an older transaction will be attempted before a younger one with the same priority.
+the transactions selected by one given recycling process will be segregated into eight groups, depending on their priority and age:
+group 1 group 2 group 3 group 4 group 5 group 6 group 7 group 8 priority 1 priority 1 priority 2 priority 2 priority 3 priority 3 priority 4 priority 4 age  3 age  3 age  3 age  3 age  3 age  3 age  3 age  3 should the serialization process be too long (over a predetermined adjustable maximum duration), it will be automatically stopped to come back to the regular recycling process.
```

## validation_concept
- June 1.6.1.1 Business Validation (PDF 218–220, 4 sentences) vs November 3.6.1.1 Business Validation (PDF 229–231, 5 sentences); similarity 0.9920; 3 residual sentence differences (inspect below)
```
-diagram 53 - business validation application process 2 overview when a t2s actor sends any of the above mentioned instructions, this process checks the consistency of the instruction and verifies that it successfully passes the applicable validation checks.
+figure 53:
+business validation application process overview when a t2s actor sends any of the above mentioned instructions, this process checks the consistency of the instruction and verifies that it successfully passes the applicable validation checks.
```

## nts_processing
- June 1.4.4.2 Night-time settlement (NTS) (PDF 167–170, 30 sentences) vs November 3.4.4.2 Night-time settlement (NTS) (PDF 180–183, 30 sentences); similarity 0.9998; 4 residual sentence differences (inspect below)
```
-ntsprocessing during the night-time settlement period, t2s processes the settlement instructions, settlement restrictions and liquidity transfers in sequences within two settlement cycles.
+nts processing during the night-time settlement period, t2s processes the settlement instructions, settlement restrictions and liquidity transfers in sequences within two settlement cycles.
-ntsreporting at the end of each night-time sequence, t2s generates full or delta reports as per the report configuration setup of the relevant t2s actors.
+nts reporting at the end of each night-time sequence, t2s generates full or delta reports as per the report configuration setup of the relevant t2s actors.
```
