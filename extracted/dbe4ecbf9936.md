# General Meetings (Layouts)

Source: https://www.euronext.com/sites/default/files/2023-07/general-meetings-layouts.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

                   GENERAL MEETINGS





                                             Layouts





General Meetings – November 2021                                                                         Page 1

## PDF page 2

1. General Meetings – NOTEVT



MEET, BMET, OMET and XMET Messages


Common part to all non-Narrative Messages




 Length   Type                               Description                                    Field SWIFT

   16     N   SEME - Reference of the Message                                 A / 20C

   1      A   Tab ‘;’

   16      A    Corporate Action Code “COAF”                                   A / 20C

   1      A   Tab ‘;’

   4      A   Message Function NEWM, REPL, CANC                             A / 23G

   1      A   Tab ‘;’

   4      A   Event Category (BMET, MEET, OMET, XMET)                         A / 22F

   1      A   Tab ‘;’

   4      A   Event Type (VOLU)                                           A / 22F

   1      A   Tab ‘;’

   8      D   Date of the Message Creation - format YYYYMMDD                    A / 98A

   1      A   Tab ‘;’

   4      A    Processing Status (COMP)                                      A / 25D

   1      A   Tab ‘;’

   16      A   COAF of the Linked Message, in multiple events                        A1 / 20C

   1      A   Tab ‘;’

   4      A    Link Type (AFTE - After or BEFO - Before)                             A1 / 22F

   1      A   Tab ‘;’

   3      A   Type of Linked Message (MT 568)                                   A1 / 13A

   1      A   Tab ‘;’

   12      A   Security Identification - ISIN Code                                   B / 35B

   1      A   Tab ‘;’

   1      A   Tab ‘;’





General Meetings – November 2021                                                                         Page 2

## PDF page 3

  BMET, MEET, OMET, XMET Messages



Length     Type                                 Description                                    Field SWIFT

    4      A   Safekeeping Account - GENR (without account)                        B2 / 97A

    1      A   Tab ‘;’

    1      A   Tab ‘;’

    1      A   Tab ‘;’

    8      N   Record Date - format YYYYMMDD                              D / 98A

    1      A   Tab ‘;’

   14     N   Date/Time of the Meeting (WET) - format YYYYMMDDHHMMSS          D / 98C

    1      A   Tab ‘;’

   14     N   Date/Time of the 2nd Meeting (WET) - format YYYYMMDDHHMMSS        D / 98C

    1      A   Tab ‘;’

   255     A   Meeting location                                         D / 94E

    1      A   Tab ‘;’

   255     A   Second Meeting location                                    D / 94E

    1      A   Tab ‘;’

    1      A   SRDC indicator (Y or N or not filled)                            D / 17B (2)

    1      A   Tab ‘;’

   256     A  WEB Site Address (URL)                                    D / 70E

    1      A   Tab ‘;’

   350     A   Additional Text                                                        F / 70E (1)

    1      A   Tab ‘;’



    (1) Additional Text: the information is separated by ”()”:
   Mandatory – (MeetQR X)(MeetQty 35d) (Met2QR X)(Met2Qty 35d)  or
             (MeetQR X)(MeetPct 12d) (Met2QR X)(Met2Pct 12d)

   Voluntary – (NewResolution X YYYYMMDD)( (NewAgendaItem X YYYYMMDD)

   Example:
         (MeetQR Y)(MeetQty 9999) )(Met2QR Y)(Met2Qty 9999)( NewResolution Y 20210423)( NewAgendaItem Y 20210423)

    (2) Y - Securities within the scope of the Shareholders Rights Directive (Shares)
    N - Securities outside the scope
     Not filled - Other securities





   General Meetings – November 2021                                                                         Page 3

## PDF page 4

 2. General Meetings – ISO 15022 MT564


Field Name/Description              M/O     Tag            Qualifier &          Format or      Note
                                                                         Delimiter            Content

Sequence A General Information start     M     :16R:                       GENL
 Sender's Message Reference            M     :20C:        :SEME//             16x
 Corporate Action Reference             M     :20C:        :CORP//             16x
 Corporate Action Event Reference        M     :20C:        :COAF//             16x
 Function of the Message               M     :23G:                                    4!c        1
 Corporate Action Event Indicator         M     :22F:        :CAEV//                4!c        2
 Mandatory/Voluntary Indicator           M     :22F:        :CAMV//                4!c        3
 Preparation Date                     M     :98C:        :PREP//              8!n6!n      *
 Processing Status                    M     :25D:        :PROC//                4!c        4
Sub Sequence A1 Linkages start         O     :16R:                            LINK
Linked Message                     M     :13A:        :LINK//                3!c
Corporate Action Event Reference        M     :20C:        :COAF//             16x
Sub Sequence A1 Linkages end          M     :16S:                            LINK
Sub Sequence A1 Linkages start         O     :16R:                            LINK
Linked Message                     M     :13A:        :LINK//                3!c
Corporate Action Event Reference        M     :20C:        :PREV//             16x
Sub Sequence A1 Linkages end          M     :16S:                            LINK
Sequence A General Information end       M     :16S:                       GENL
Sequence B Underlying Securities start    M     :16R:                     USECU
  ISIN                             M     :35B:                              ISIN1!e12!c
 Sub Sequence B2 Account Information
                                  M     :16R:                      ACCTINFO
start
 Safekeeping Account                  M     :97A:       :SAFE//              35x       5
 Sub Sequence B2 Account Information
                                  M     :16S:                      ACCTINFO
end
Sequence B Underlying Securities end      M     :16S:                     USECU
Sequence D Corporate Action Details
                                  M     :16R:                      CADETL
start
 Record Date                        M     :98A:        :RDTE//               8!n
 Meeting Date/Time                   O     :98C:        :MEET//              8!n6!n          *
 Second Meeting Date/Time             O     :98C:        :MET2//              8!n6!n          *
 Meeting Place                       O     :94E:        :MEET//            10*35x
 Second Meeting Meeting Place        O       :94E:           :MET2//             10*35x
Shareholder Rights Directive Indicator      O     :17B:        :SRDC//                4!c        6
 Web Site Address                    O     :70E:        :WEBB//            10*35x
Sequence D Corporate Action Details end   M     :16S:                      CADETL
Sequence F Additional Information start   M     :16R:                      ADDINFO
 Additional Text                       M     :70E:        :ADTX//            10*35x       7
Sequence F Additional Information end      M     :16S:                      ADDINFO

       * the time indicated in the messages is always West European Time (WET)





 General Meetings – November 2021                                                                         Page 4

## PDF page 5

Notes:

1 - Function of the Message – NEWM, REPL, CANC

2 - Event Indicator – BMET, MEET, OMET, XMET

3 - Mandatory/Voluntary Indicator – VOLU

4 - Processing Status – COMP

5 - Safekeeping Account – GENR

6 - Shareholder Rights Directive Indicator (Y/N)

7 - Additional Text in the sequence F, the information is separated by ”()”:


    Mandatory – (MeetQR X)(MeetQty 35d) (Met2QR X)(Met2Qty 35d)  or
              (MeetQR X)(MeetPct 12d) (Met2QR X)(Met2Pct 12d)

     Voluntary – (NewResolution X YYYYMMDD)( (NewAgendaItem X YYYYMMDD)

Example:
:70E::ADTX//(MeetQR Y)(MeetQty 9999) )(Met2QR Y)(Met2Qty 9999)( NewResolution Y 20210423)( NewAgendaItem Y 20210423)





General Meetings – November 2021                                                                         Page 5

## PDF page 6

3. General Meetings – ISO 15022 MT568




Field Name/Description              M/O     Tag            Qualifier &          Format or      Note
                                                                         Delimiter            Content

Sequence A General Information start     M     :16R:                       GENL
 Sender's Message Reference            M     :20C:        :SEME//             16x
 Corporate Action Reference             M     :20C:        :CORP//             16x
 Corporate Action Event Reference        M     :20C:        :COAF//             16x
 Function of the Message               M     :23G:                                    4!c           1
 Corporate Action Event Indicator         M     :22F:        :CAEV//                4!c           2
 Preparation Date                     M     :98C:        :PREP//              8!n6!n          *
 Sub Sequence A1 Linkages start         O     :16R:                            LINK
 Linked Message                     M     :13A:        :LINK//                3!c           3
 Previous Message Reference           M     :20C:        :PREV//             16x
 Sub Sequence A1 Linkages end          M     :16S:                            LINK
Sequence A General Information end       M     :16S:                       GENL
Sequence B Underlying Securities start    M     :16R:                     USECU
 Safekeeping Account                  M     :97A:       :SAFE//              35x           4
  ISIN                             M     :35B:                              ISIN1!e12!c
Sequence B Underlying Securities end      M     :16S:                     USECU
Sequence C Additional Information start   M     :16R:                       ADDINFO
 Additional Text                       M     :70F:        :ADTX//            8000z          5
Sequence C Additional Information end     M     :16S:                       ADDINFO

                                 * the time indicated in the messages is always West European Time



Notes:

1 - Function of the Message – NEWM

2 - Event Indicator – BMET, MEET, OMET, XMET

3 - Linked Message - 564

4 - Safekeeping Account – GENR

5 - Additional Text – In this sequence, the information is separated by ”<>”:

    Mp - Participation Methods separated by #
    Px – Agenda Points;
    Vx – Voting
    Sx - Status
    VOx – Other Voting Codes

   Example:

    :70F::ADTX//<Mp>MAIL#PHYS#PHNV#PRXY#VIRT#EVOT</Mp><DtMp>20210423#20210423#20210423#20210423
     #20210423#20210423</DtMp><Agenda>
     <P1>Orçamento 2021</P1><V1>ADVI</V1><S1>ACTV</S1><VO1>CAGS#CFOR#ABST#NOAC</VO1>
     <P2>Contas 2020</P2><V2>BNDG</V2><S1>WDRA</S1><VO2>CAGS#CFOR#ABST</VO2>





General Meetings – November 2021                                                                         Page 6

## PDF page 7

Participation Methods:

EVOT= Electronic Voting;
PHYS = Participation in person;
PRXY = Participation through proxy;
VIRT = Virtual participation;
PHNV =Not Voting;
MAIL= Correspondence.

Voting Codes:

BNDG –Binding voting;
ADVI–Advisory voting.

Status Codes:

ACTV = Active
WDRA = Withdraw

If the item on the agenda is not subject to a vote, the field is blank.

Other Voting Codes:

ABST- Abstention;
CAGS - Vote against;
CFOR- Vote in favour;
NOAC- No action





General Meetings – November 2021                                                                         Page 7

## PDF page 8

     4. General Meetings – ISO 20022 seev.001

                                                     Mandatory
                       Field                    Type Length                         Description
                                                                / Optional
<Document xmlns="urn:iso:std:iso:20022:
tech:xsd:seev.001.001.08
"xmlns:xsi="http://www.w3.org/2001/                     -         -     M
XMLSchemainstance">


  <MtgNtfctn>                                                   -         -     M
     <NtfctnGnlInf>                                             -         -     M
        <NtfctnTp></NtfctnTp>                            NEWM - New - New notification
                                                                   REPL - Replace- Notification
                                      A     4    M
                                                                                replacing a previously sent
                                                                                       notification.
       <NtfctnSts>                                              -         -     M
          <EvtCmpltnsSts></EvtCmpltnsSts>                       COMP - Complete - Event details
                                      A     4    M
                                                                          are complete
          <EvtConfSts></EvtConfSts>                              CONF - Confirmed - Occurrence of
                                      A     4    M
                                                                         the event has been confirmed
       </NtfctnSts>                                              -         -     M
<ShrhldrRghtsDrctvInd></ShrhldrRghtsDrctvInd>    A     5      O      "TRUE" or "FALSE"
     </NtfctnGnlInf>                                            -         -     M
     <NtfctnUpd>                                               -         -      O
          <PrvsNtfctnId></PrvsNtfctnId>         A    35     M/O        If message REPL
                                                                                 Indicates whether a meeting
                                                                                  instruction must be resent in case
                                                                         the parameters of the meeting are
                                                                   changed and the meeting
          <RcnfrmInstrs></RcnfrmInstrs>         A     5     M/O                                                                                  instruction has already been sent:
                                                                   "TRUE"
                                                                           or
                                                                        "FALSE"
     </NtfctnUpd>                                              -         -      O
     <Mtg>                                                       -         -     M
        <MtgId></MtgId>                   A    35    M     COAF
         <IssrMtgId></IssrMtgId>              A    35    M     COAF

                                                        XMET - Extraordinary
                                                     GMET - General - Includes annual
         <Tp></Tp>                       A     4    M
                                                                 and ordinary meetings
                                                       BMET - BondHolder Meeting
  <AnncmntDt>
                                                                        -         -

     <Dt></Dt>                                                      Meeting announcement date -
                                      A    10      O
                                                            YYYY-MM-DD format
  </AnncmntDt>
                                                                        -         -


   General Meetings – November 2021                                                                         Page 8

## PDF page 9

                                                     Mandatory
Field                                      Type Length              Description
                                                                / Optional
          <Prtcptn>                                            One entry for each method of
                                                                        -         -     M
                                                                                   participation
           <PrtcptnMtd>
                                                                        -         -     M     Type of participation

                                                               MAIL – Correspondence
                                                               PHYS – In person
                                                        PHNV – Not voting
               <Cd></Cd>                 A     4    M
                                                                PRXY – Proxy
                                                                       VIRT – Virtual

                                                            EVOT – Electronic voting
            </PrtcptnMtd>                                  -         -     M
             <IssrDdlnForVtng>                                                                        -         -     M      Deadline for participation method

             <DtOrDtTm>                                 -         -     M
                                                                    Date and hour (format AAAA-MM-
                                                            DDTHH:MM:SSZ – UTC time) for
                                                                    each Participation method:
                                                                                                            - meeting date and time for
                <DtTm></DtTm>           A    23    M       participation methods PHYS,
                                                        PHNV & VIRT

                                                                                                            - issuer deadline for participation
                                                                methods MAIL, PRXY & EVOT

              </DtOrDtTm>                               -         -     M
             </IssrDdlnForVtng>                            -         -     M
         </Prtcptn>                                             -         -     M
                                                                               Additional information about the
                                      A    256     O
<AddtlDcmnttnURLAdr></AddtlDcmnttnURLAdr>                             meeting.
         <AddtlPrcdrDtls>
            <AddtlRght>
                                                                Agenda Item Proposal [AIPS]
               <Cd></Cd>                 A     4      O
                                                                            Resolution Proposal [RSPS]

            </AddtlRght>
           <AddtlRghtMktDdln>
              <DtOrDtTm>

                                                                    Date for each option: AIPS and / or
                 <Dt></Dt>
                                                                   RSPS
                                      A    10      O
              </DtOrDtTm>
           </AddtlRghtMktDdln>
          </AddtlPrcdrDtls>

  <EntitlmntFxgDt>                                                                        -         -     M

    <Dt>                                                            -         -     M
                                                                     Record Date - formato YYYY-MM-
     <Dt></Dt>                          A    10    M
                                                     DD


   General Meetings – November 2021                                                                         Page 9

## PDF page 10

                                                     Mandatory
Field                                      Type Length              Description
                                                                / Optional
    </Dt>                                                           -         -     M
  </ EntitlmntFxgDt>
                                                                        -         -     M

    </Mtg>                                                                        -         -     M

                                                                                Repetitive block for 2 meetings:
   <MtgDtls>                                                     -         -    M (x2)    2 dates: 1st and 2nd meeting,
                                                                               respective Addresses
     <DtAndTm>                                                -         -     M
         <DtOrDtTm>                                         -         -     M
            <DtTm></DtTm>                                         Meeting Date and hour (format
                                      A    23    M     AAAA-MM-DDTHH:MM:SSZ – UTC
                                                                            time)
        </DtOrDtTm>                                        -         -     M
     </DtAndTm>                                               -         -     M
    <QrmReqrd></QrmReqrd>               A     5    M     "TRUE" or "FALSE"
     <Lctn>                                                        -         -     M
      <Adr>                                                       -         -     M
                                                        ADDR - Postal - Address is the
                                                                     complete postal address.
      <AdrTp></AdrTp>                    A     4      O
                                                                            BIZZ - Business - Address is the
                                                                            business address.
                                                                           Information that locates and
                                                                                        identifies a specific address, as
      <AdrLine></AdrLine>                  A    70      O
                                                                          defined by postal services, that is
                                                                        presented in free format text.
      <StrtNm></StrtNm>                   A    70      O      Address/Street
      <BldgNb></BldgNb>                   A    16      O     Number
      <PstCd></PstCd>                     A    16      O       Postal Code
     <TwnNm></TwnNm>                  A    35      O       City
      <Ctry></Ctry>                       A     2    M      Country
    </Adr>                                                        -         -     M
   </Lctn>                                                          -         -     M
  <QrmQty>                                                           Only when QuorumRequired is
                                                                        -         -      O       true, and only one field can be
                                                                                                     filled: in Quantity or in Percentage
<QrmQty></QrmQty>             OR                          Minimum amount of quorum (18
                                  N    18     M/O
                                                                                  integers)
<QrmQtyPctg></QrmQtyPctg>                                    Minimum percentage of quorum
                                  N     6     M/O
                                                                                 (3 integers + 2 decimals)
  </QrmQty>                                                     -         -      O
  <URLAdr></URLAdr>                     A   2048     O      Address in case of virtual meeting
 </MtgDtls>                                                       -         -     M
  <Issr>                                                              -         -     M
    <Id>                                                             -         -     M
      <LEI></LEI>                                      A    20    M       LEI


   General Meetings – November 2021                                                                        Page 10

## PDF page 11

                                                     Mandatory
Field                                      Type Length              Description
                                                                / Optional
    </Id>                                                           -         -     M
  </Issr>                                                             -         -     M
  <Scty>                                                             -         -     M
    <FinInstrmId>                                                 -         -     M
      <ISIN></ISIN>                        A    12    M       ISIN
    </FinInstrmId>                                               -         -     M
  </Scty>                                                           -         -     M
  <Rsltn>                                                                       Repetitive block with a maximum
                                                                        -         -     M
                                                                               of 15 occurrences / Agenda points
     <IssrLabl></IssrLabl>                    A    35    M
   <Desc>                                                          -         -      O
      <Lang></Lang>                                                     Country Language - Agenda Item
                                      A     2    M
                                                                               (ISO 639-1 standard)
      <Desc></Desc>                      A   1025     O
   </Desc>                                                        -         -      O
    <ForInfOnly></ForInfOnly>                A     5    M     "TRUE" or "FALSE"
                                                                 ADVI - Advisory
    <VoteTp></VoteTp>                     A     4    M
                                                      BNDG - Binding
                                                             ACTV - Active
    <Sts></Sts>                           A     4    M
                                                  WDRA - Withdrawn
    <VoteInstrTp>                                                             Repetitive block with 4
                                                                        -         -      O
                                                                          occurrences
       <VoteInstrTpCd>                                       -         -     M/O
                                                              ABST - Abstain
                                                           CAGS - Against
          <Tp></Tp>                      A     4     M/O
                                                           CFOR - Vote in favour
                                                     NOAC - No Action
       </VoteInstrTpCd>                                       -         -     M/O
    </VoteInstrTp>                                              -         -      O
    <Entitlmnt>                                                   -         -      O
        <EntitlmntRatio></EntitlmntRatio>                                      Ratio: number of votes per share
                                  N    18     M/O
                                                                           (12 integers + 5 decimals)
   </Entitlmnt>                                                   -         -      O
  </Rsltn>                                                          -         -     M
   <AddtlInf>                                                       -         -      O
     <Dsclmr>                                                    -         -      O
        <Lang></Lang>                                                   Country Language – Disclaimer
                                      A     2    M
                                                                               (ISO 639-1 standard)
         <AddtlInf></AddtlInf>                A    350    M       Additional information
     </Dsclmr>                                                  -         -      O
   </AddtlInf>                                                     -         -      O
 </MtgNtfctn>                                                    -         -     M
</Document>                                                      -         -     M





   General Meetings – November 2021                                                                        Page 11

## PDF page 12

     5. General Meetings – ISO 20022 seev.002

                                                 Mandatory
Field                                Type  Length                            Description
                                                           / Optional
<Documentxmlns="urn:iso:std:iso:20022:
tech:xsd:seev.002.001.07
                                                              -          -     M
"xmlns:xsi="http://www.w3.org/2001
/XMLSchema-instance">
 <MtgCxl>                                                -          -     M
    <MtgRef>                                            -          -     M
      <MtgId></MtgId>                A     35    M     COAF
      <IssrMtgId></IssrMtgId>           A     35    M     COAF
                                                               Meeting Date and hour (format AAAA-
     <MtgDtAndTm ></MtgDtAndTm >    A     20    M
                                                     MM-DDTHH:MM:SSZ – UTC time)
                                                    XMET - Extraordinary
                                                  GMET - General - Includes annual and
        <Tp></Tp>                  A      4     M
                                                                       ordinary meetings.
                                                   BMET - BondHolder Meeting
     </MtgRef>                                         -          -     M
     <Scty>                                              -          -     M
        <FinInstrmId>                                 -          -     M
           <ISIN></ISIN>               A     12    M       ISIN
        </FinInstrmId>                                -          -     M
     </Scty>                                              -          -     M
    <Rsn>                                                -          -     M
       <CxlRsnCd>                                     -          -     M
                                             QORM - Quorum - Cancellation due to
                                                                                 insufficient
                                                      PROC - Processing - Cancellation due to
         <Cd></Cd>                  A      4     M
                                                                a processing error
                                                      WITH - Withdrawal - Meeting cancelled
                                                               by the issuer.
      </CxlRsnCd>                                     -          -     M
                                                                      Provides more information on the
      <CxlRsn></CxlRsn>               A     140     O      reason for cancelling a meeting in free
                                                                  format form
  </Rsn>                                                  -          -     M
 </MtgCxl>                                              -          -     M
</Document>                                            -          -     M





   General Meetings – November 2021                                                                        Page 12