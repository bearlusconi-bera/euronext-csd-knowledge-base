QUESTION FROM THE USER:
Could a Monte Titoli participant settle a FOP instruction on 1 May 2026, and a DvP in EUR on that day?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.457266+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_calendar_exception", "payment_type": "FOP", "business_date": "2026-05-01"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-may1-2026]] — 1 May 2026 treated as a business day: T2S open for FOP only in EUR, T2 closed, X-TRM limitations and custody impacts (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: ON_13/2026 May 1st as a business day: impact on ES-MIL systems (24 April 2026) | ON_13/2026 PDF 1–6 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_primo_maggio_eng_2026_0.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Applies to 1 May 2026 only; impact tables are reproduced from a layout-heavy PDF and should be read against the original for row alignment.
EXCERPT (ON_13/2026 PDF 1–6):
[PDF page 1]

24 April 2026
ON_13/2026


May 1st as a business day:
impact on ES-MIL systems
   To the attention of:                           All Clients and Account Operators


   Topic:                                         May 1st 2026 treated as a business day:
                                                  impact on ES-MIL systems


Dear Client,


Please take note that May 1st, 2026 will be treated                                   as a business day and will have
the following specific characteristics:

     •    T2S: open for FOP, but not for DVP and PFOD operations in EURO
     •    T2: closed
     •    All CSD participants in T2S (including ES-MIL): open

In particular, for Custody activities:
   • no payments in EURO may be made on May 1st; payments will be postponed
       and made on the first subsequent working day
   • securities disposal or Pool Factor adjustment for REDM, PCAL and MCAL will be
       performed at SOD in the scheduled NTS cycle following May 1st.

For Settlement activities:
   • the X-TRM service will be operational with some limitations due to the
      impossibility of settling the cash part.
   • Reports concerning penalties will be sent




This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprie tary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 6

                                                             PRIVATE



[PDF page 2]

          Impact on Custody
          The custody processes concerned are typically those that involve cash-related
          activities, including:
               •       Cash Distribution
               •       Payment of Government Bonds
               •       Payments management by the Paying Agent
               •       Late dividend collection
               •       RCC
               •       Reorganisation


          The following chart describes the expected impact on individual processes




                                              CASH              1/5/2026      1/5/2026
No.      PROCESS          SERVICE    CAEV   SECURITIES            NTS           RTS         04/05/2026               ACTION

1     payments made       Custody   INTR,   Cash/securities    securities   no payment     Deferred      Payments will be deferred until
      in central bank     ITA       REDM,                      accounting                  cash          the next business day
      money                         PCAL,                      or PF                       settlement    The deferral will also apply to
                                    PRED,                      amendment                                 securities with a “PREVIOUS
                                    MCAL                       download                                  GOOD BUSINESS DAY”
                                                                                                         convention.
                                                                                                         No impact is expected for
                                                                                                         securities with a MODIFIED
                                                                                                         FOLLOWING BUSINESS DAY
                                                                                                         convention.

2     payments made       Custody   INTR,   Cash/securities    securities   suspension     Deferred      After suspension, payments will
      in commercial       ITA       REDM,                      accounting   of payment     cash          be postponed until the next
      bank money          Custody   PCAL,                      or PF                       settlement    working day
                          EST       PRED,                      amendment
                                    MCAL                       download

3     Payment of          Custody   INTR,   Cash/securities    securities   no payment     Deferred      Payments will be postponed until
      Government          ITA       REDM                       accounting                  cash          the next working date.
      Bonds                                                    download                    settlement    in the event of partial or total
                                                                                                         redemption the securities
                                                                                                         accounting download will be
                                                                                                         performed on 1 May.

4     Payment of          Custody   DVCA,   Cash/securities    N.A.         no payment     N.A.          Issuers will be prevented from
      dividends/fund      ITA       CAPD,                                                                entering transactions with a
      units               Custody   etc.                                                                 payment date of 1 May
                          EST

5     Payments            Custody   DVCA    Cash               N.A.         No             Deferred      the sending of RIFPA, REVPA,
      management by       ITA                                               instructions   cash          RIAPA instructions on 1 May will
      the Paying                                                                           settlement    be prevented.
      Agent.                                                                                             For RIAPA instructions received
      RIFPA, REVPA,                                                                                      the day before 1 May, payments
      RIAPA                                                                                              will be postponed to the next
      (MSG7B4)                                                                                           working day.
      instructions




          | 2 of 6


                                                              PRIVATE



[PDF page 3]

                                                       CASH                 1/5/2026        1/5/2026
    No.        PROCESS          SERVICE     CAEV     SECURITIES               NTS             RTS            04/05/2026                  ACTION

    6       Late dividend      Custody     DVCA     Cash                N.A.              No payment        Deferred         Payments will be deferred until
            collection         ITA                                                                          cash             the first subsequent working date
                                                                                                            settlement       for collection instructions
                                                                                                                             received on the day before 1
                                                                                                                             May

    7       Reversal           Custody     INTR,    Cash                N.A.              No payment        N.A.             transactions will not be executed
                               ITA         REDM,                                                                             on 1 May
                               Custody     etc.
                               EST



                 Cash distribution: currency <> Eur:
                                                     CASH               1/5/2026          1/5/2026
N.           PROCESS           SERVICE     CAEV    SECURITIES             NTS               RTS            4/5/2026                   ACTION

8         payments            Custody     INTR,    cash/securities      securities        sending of         N.A.         No Action. Payment made outside
          executed in         ITA         REDM,                        accounting       final payment                                  ES-MIL
          commercial bank                 PCAL,                           or PF           messages
          money directly by               PRED,                        amendment
          the Paying Agent                MCAL                          download
          or its
          correspondent
          bank

9         payments            Custody     INTR,    cash/securities      securities           cash             N.A.         No Action. Regularly executed
          executed in         EST         REDM,                        accounting         settlement                                operations
          commercial bank                 PCAL,                           or PF
          money                           PRED,                        amendment
                                          MCAL,                         download
                                          DVCA,
                                          etc.




                 Reorganization: currency Eur:
                                                     CASH             1/5/2026          1/5/2026
N.           PROCESS          SERVICE      CAEV    SECURITIES           NTS               RTS             4/5/2026                    ACTION

10        ACPG                Custody     EXRI,    Cash              N.A.              No payment       Cash post        Issuers will be prevented from
          (accounting and     ITA         EXWA,                                                         settlement       entering transactions with a
          rolling)            Custody     DVOP,                                                                          payment date of 1 May In the case
          Warrant exercise    EST         etc,                                                                           of rolling transactions, unexecuted
          and dividend with                                                                                              instructions received on the
          option                                                                                                         business day before 1 May and
                                                                                                                         those received on 1 May will all be
                                                                                                                         settled on the next business day




                 | 3 of 6


                                                                      PRIVATE



[PDF page 4]

            Other processes:
            5
                                                CASH          1/5/2026      1/5/2026
N.       PROCESS         SERVICE    CAEV      SECURITIES        NTS           RTS        4/5/2026               ACTION

11    voluntary /        Custody   RHDI,      NO           Securities    Securities    Securities    No Action. Operations
      mandatory          ITA       CONV,                   settlement    settlement    settlement    performed regularly
      Reorganization     Custody   MRGR,
      (no cash)          EST       SPLF etc
                                   .

12    Issuance, MarkUp   Custody   N.A.       NO           Securities    Securities    Securities    No Action. Operations
      and MarkDown       ITA                               settlement    settlement    settlement    performed regularly

13    DVPIssaunce        Custody   N.A.       Cash          N.A.         No payment    Cash post     Issuers will be prevented from
                         ITA                                                           settlement    entering transactions with a
                                                                                                     payment date of 1 May


14    RCC                Custody   N.A.       Cash         N.A           No payment    Cash post     Payments will be postponed to
                         ITA                                                           settlement    the next working date.




     Settlement
     impact


              System                                                      Operation
     T2S – X-TRM                    ➢     The T2S platform will be available and therefore also the X-TRM service will be
                                          operational with some limitations due to the impossibility of settling the cash part
                                    ➢     only and exclusively Intra and Cross-CSD instructions can be settled, while “APMT”
                                          instructions will be blocked/rejected by the T2S platform




            | 4 of 6


                                                           PRIVATE



[PDF page 5]

   Intra and Cross CSD:
       TYPE OF
      OPERATION                                           Operation
NON-GUARANTEED       ➢    Any transactions with a “Trade Date” of 1/5/2026 will be rejected by X-TRM.
MARKET OPERATIONS    ➢    For transactions received on previous days and with ISD up to 26/04/2026, the
                          determination of the end-of- validity date (ISD + n days) will not take into account
                          of 1/5/2026
                     ➢    Unsettled transactions from previous days will not attempt settlement on 1/5/2026
GUARANTEED           ➢    Any transactions with a “Trade Date” of 1/5/2026 will be rejected by X-TRM.
MARKET OPERATIONS    ➢    For transactions received on previous days and with ISD up to 26/04/2026, the
                          determination of the end-of- validity date (ISD + n days) will not take into account
                          of 1/5/2026. Unsettled transactions from previous days will not attempt settlement
                          on 1/5/2026.
OTC                  ➢    “FREE” instructions already in T2S will attempt settlement, while “APMT”
                          instructions will remain blocked.
                     ➢    “FREE” instructions can be entered/reset/settled with any ISD.
                     ➢    It will be possible to enter/match “APMT” instructions with ISDs other than 1/5, but
                          they will not attempt settlement.
                     ➢    It will NOT be possible to enter “AMPT” instructions with an ISD of 1/5. Any
                          instructions will be rejected by T2S.




  | 5 of 6


                                          PRIVATE



[PDF page 6]

External CSD:
           System                                           Operation
  MARKETS                  ➢     All Markets connected to X-TRM will be closed, any trades with A ‘Trade
                                 Date’ of 1/5/2026 will be rejected by X-TRM.
                           ➢     Trades (EuroTLX and EuroMOT) received on previous days with ISD
                                 1/5/2025 will be sent to the relevant ICSDs on the trade day.


  OTC                      ➢     Pending “FREE” instructions with an ISD before 1/5/2026 will attempt
                                 settlement, while for pending “APMT” instructions:
                                      o Delivery from the ES-MIL account can be settled with the foreign
                                          CSD, but the securities will be released and debited on 2/5
                                          together with the corresponding cash credit;
                                      o Receive to the ES-MIL account will be settled at the ICSD and
                                          securities will be credited on 2/5
                           ➢     “FREE” instructions can be entered/matched/settled with any ISD.
                           ➢     It will NOT be possible to enter “AMPT” instructions with an ISD of 1/5.
                                 Any delivery or withdrawal instructions will be rejected by T2S.




For further information:

E: eam@euronext.com
MIL-clientsupport@euronext.com




| 6 of 6


                                            PRIVATE