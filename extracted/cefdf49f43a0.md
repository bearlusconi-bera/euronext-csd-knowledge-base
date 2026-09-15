# Place of settlement change guidelines - March 2026 - V.3 Track changes

Source: https://www.euronext.com/sites/default/files/2026-03/euronext_securities_-_place_of_settlement_change_guidelines_-_v.3_march_2026_-_track_changes_0.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

                                 EURONEXT SECURITIES - PSET CHANGE GUIDELINES




EUO1-#2013726360-
v1 2001067813 INV 25


E
Euronext Securities

Place of Settlement
change guidelines

Trading, Clearing, Settlement


V. 3,2 FEBRUARY MARCH 2026





0

## PDF page 2

                                 EURONEXT SECURITIES - PSET CHANGE GUIDELINES


 Table of contents

1.  INTRODUCTION .......................................................................................... 1

  1.1.  Document purpose ............................................................................... 2

  1.2.  Target audience ................................................................................... 2

  1.3.  Glossary ............................................................................................... 3

  1.4.  Document history ................................................................................. 4

2. APPROACH FOR PSET CHANGE ................................................................... 5

  2.1  Scope of markets and instruments ....................................................... 6

  2.2   Technical change in referential data..................................................... 7

  2.3  Tax and legal ........................................................................................ 7

3. SETTLEMENT MODELS ................................................................................... 9

  3.1  Designated place of settlement .......................................................... 10

  3.2   Alternative place of settlement .......................................................... 10

  3.3  Models ................................................................................................ 11

    3.3.1   Settlement model for guaranteed instruments issued in Euronext
    Securities Milan ........................................................................................ 12

    3.3.2   Settlement model for guaranteed instruments issued in another T2S
   CSD   12

    3.3.3   Settlement model for guaranteed instruments issued in non-T2S
   CSD   14

  3.4  Settlement for OTC ............................................................................. 14

4. CHANGE of PSET – plan............................................................................... 16

  4.1  PSET change high level timeline ......................................................... 17

4.1.1 Production environment ........................................................................ 17

4.1.2 Test environment .................................................................................. 17

  4.2  Framework of PSET change ................................................................ 18

4.2.1 Pre-requisites for the settlement in Euronext Securities Milan .............. 18

4.2.2 PSET change weekend ........................................................................... 18

  4.3   Specific processes impacted by PSET change ..................................... 19

4.3.1 Pending/Failing transactions ................................................................. 19

4.3.2 Corporate actions .................................................................................. 19

4.3.3 Deferred Settlement Service (DSS) ....................................................... 20

  4.4   Testing ............................................................................................... 21



1

## PDF page 3

                                 EURONEXT SECURITIES - PSET CHANGE GUIDELINES




4.4.3 Supporting documentation and events .................................................. 22

  4.5  Freeze period ..................................................................................... 24

  4.6  Communication and support............................................................... 25

4.6.1 Communication ...................................................................................... 25

4.6.2 Support contacts ................................................................................... 25

5.  SPECIFIC ACTIONS FOR SETTLEMENT AGENT, CLEARING MEMBER ACTING
AS Settlement agents and custodians ............................................................. 27

  5.1 Onboarding of new clients ..................................................................... 28

  5.2 Configuration for new and existing clients ............................................ 28

  5.3 Position transfer .................................................................................... 28

....................................................................................................................... 29

6. CLIENT JOURNEY ........................................................................................ 29

6.1 Purpose of the client journey .................................................................... 30

6.2   Client journey for the settlement in Euronext Securities ...................... 30

6.2.1 For trading members ............................................................................ 30

6.2.2 For General Clearing Members not acting as settlement agents .......... 30

6.2.3 For General Clearing Members acting as settlement agents ................ 31

6.2.4 For settlement agent ............................................................................ 32

6.2.5 For custodian ........................................................................................ 33

1.  INTRODUCTION .......................................................................................... 1

  1.1.  Document purpose ............................................................................... 2

  1.2.  Target audience ................................................................................... 2

  1.3.  Glossary ............................................................................................... 3

  1.4.  Document history ................................................................................. 4

2. APPROACH FOR PSET CHANGE ................................................................... 5

  2.1  Scope of markets and instruments ....................................................... 6

  2.2   Technical change in referential data..................................................... 7

  2.3  Tax and legal ........................................................................................ 7

3. SETTLEMENT MODELS ................................................................................... 9

  3.1  Designated place of settlement .......................................................... 10

  3.2   Alternative place of settlement .......................................................... 10

  3.3  Models ................................................................................................ 10

    3.3.1   Settlement model for guaranteed instruments issued in Euronext
    Securities Milan ........................................................................................ 12




2

## PDF page 4

                                 EURONEXT SECURITIES - PSET CHANGE GUIDELINES




    3.3.2   Settlement model for guaranteed instruments issued in another T2S
   CSD   12

    3.3.3   Settlement model for guaranteed instruments issued in non-T2S
   CSD   13

  3.4  Settlement for OTC ............................................................................. 14

4. CHANGE of PSET – plan............................................................................... 16

  4.1  PSET change high level timeline ......................................................... 17

4.1.1 Production environment ........................................................................ 17

4.1.2 Test environment .................................................................................. 17

  4.2  Framework of PSET change ................................................................ 18

4.2.1 Pre-requisites for the settlement in Euronext Securities Milan .............. 18

4.2.2 PSET change weekend ........................................................................... 18

  4.3   Specific processes impacted by PSET change ..................................... 19

4.3.1 Pending/Failing transactions ................................................................. 19

4.3.2 Corporate actions .................................................................................. 19

4.3.3 Deferred Settlement Service (DSS) ....................................................... 20

  4.4   Testing ............................................................................................... 21

4.4.1 Mandatory testing ................................................................................. 21

4.4.2 Conditional testing ................................................................................ 21

4.4.3 Supporting documentation .................................................................... 22

  4.5  Freeze period ..................................................................................... 22

  4.6  Communication and support............................................................... 22

4.6.1 Communication ...................................................................................... 22

4.6.2 Support contacts ................................................................................... 23

5.  SPECIFIC ACTIONS FOR SETTLEMENT AGENT, CLEARING MEMBER ACTING
AS Settlement agents and custodians ............................................................. 24

  5.1 Onboarding of new clients ..................................................................... 25

  5.2 Configuration for new and existing clients ............................................ 25

  5.3 Position transfer .................................................................................... 25

....................................................................................................................... 26

6. CLIENT JOURNEY ........................................................................................ 26

6.1 Purpose of the client journey .................................................................... 27

6.2   Client journey for the settlement in Euronext Securities Milan ............. 27

6.2.1 For trading members ............................................................................ 27

6.2.2 For General Clearing Members not acting as settlement agents .......... 27



3

## PDF page 5

                                 EURONEXT SECURITIES - PSET CHANGE GUIDELINES




6.2.3 For General Clearing Members acting as settlement agents ................ 28

6.2.4 For settlement agent ............................................................................ 29

6.2.5 For custodian ........................................................................................ 30





4

## PDF page 6

                                  EURONEXT SECURITIES - PSET CHANGE GUIDELINES





  1. INTRODUCTION





1 │ V.3,2 February March 2026

## PDF page 7

                                  EURONEXT SECURITIES - PSET CHANGE GUIDELINES





Euronext Securities Milan will become the designated place of settlement for all
equities and exchange-traded product trades in euros executed on the Euronext
Amsterdam, Brussels and Paris markets.



1.1. Document purpose


Euronext is addressing post-trade fragmentation by integrating markets and offering the
transition from a structure of multiple domestic central securities depositories (CSDs) to a
global European CSD solution, known as Euronext Securities. This centralisation aims to
streamline the settlement and safekeeping for multiple markets within one CSD.

For clients active on the relevant Euronext markets, this transformation is expected to
lower costs and reduce the complexity of post-trade operations, enhance cross-border
trading opportunities.

This document provides:

    -   Information and a target timeline for the change of place of settlement (“change of
      PSET”) for all instruments in scope;
    -  Guidance on how the change of PSET will be rolled out and what will be expected
      from clients (trading members, clearing members, settlement agents, custodians);
    -  Guidance on the migration process including the migration of safekeeping to
      Euronext Securities Milan.

This document is for informational purposes only and should be consulted alongside other
documents about the change of place of settlement.



1.2. Target audience


This document  is intended for trading members, clearing members, central clearing
counterparties (CCPs) and settlement agents who are active in the affected markets and
who need to establish the necessary settlement arrangements with Euronext Securities
Milan. Additionally, the document serves to update other market participants, including
issuing agents and custodians, on the changes in Euronext’s post-trade infrastructure.





2 │ V.3,2 February March 2026

## PDF page 8

                                   EURONEXT SECURITIES - PSET CHANGE GUIDELINES



 1.3. Glossary


  Below is a definition of the key terms used in the document. If not otherwise specified:


    Key term                                    Definition

                      Central Security Depository that can be used alternatively to EuronextAlternative CSD
                       Securities Milan to settle transactions in scope.

                      Central Securities Depository.CSD

                    Banks,   financial   institutions,  central  counterparties  (CCP),  stockCSD Participant
                    exchanges, multilateral trade platforms (MTFs).

                 A custodian is a financial institution or entity that safeguards financialCustodian
                       assets, such  as  stocks and  bonds, and manages  tasks  like  trade
                      settlement, dividend collection, and asset reporting. In the context of
                    Euronext Securities Milan, Custodians are clients of the settlement agents.

                    Euronext Securities Milan.ES-MIL

                 A Central Securities Depository (CSD) that accepts a security into its ownInvestor CSD
                   books for the purpose of settlement and safekeeping, even though it is not
                     the original Issuer CSD. The Investor CSD enables its participants to hold
                  and settle securities issued in another CSD, typically through a link or
                        interoperability arrangement with the Issuer CSD.

                       International Securities Identification Number – ISO standard 6166, aISIN
                    unique code to identify a financial instrument. Allocated by the National
                   Numbering Agency.

                 A company or legal entity that creates and issues shares to raise capital.Issuer
                   The  Issuer  is  responsible  for  registering  the  shares,  maintaining
                     shareholder records and complying with regulatory requirements related
                       to the issuance and management of those securities.

                 A Central Securities Depository (CSD) where all the securities are initiallyIssuer CSD
                     recorded and from which they are created and distributed. The Issuer CSD
                             is  responsible  for  the  initial  registration,  safekeeping, and  central
                      administration of the securities on behalf of the Issuer.

                  Opened by an investor CSD in its books to represent its holding on theMirror account
                       investor CSD’s omnibus account in the issuer CSDs.





  3 │ V.3,2 February March 2026

## PDF page 9

                                   EURONEXT SECURITIES - PSET CHANGE GUIDELINES





                 A security account in the books of the issuer CSD for the investor CSDOmnibus account
                    which holds the security positions owned by all the participants of the
                       investor CSD for the relevant security.

                    Throughout the document, the “previous place of settlement”  will bePrevious place of
                       referred to as the place of settlement that is used by clients prior to thesettlement
                      designation of Euronext Securities Milan for settlement.

                      Place of settlement.PSET

                 An  institution  which  manages  the  settlement  process  (e.g.  theSettlement agent
                     determination  of  settlement  positions,  monitoring  the exchange  of
                   payments and securities, etc.) for transfer systems or manages other
                    arrangements which require settlement, and provides related services.

                     TARGET2-Securities.T2S



 1.4.  Document history


   Document Version         Date               Change description


V.1                                 1st August 2025   Initial version of the document


V. 2                           19th   February  Section 3.2 Alternative place of settlement
                       2026XX


V. 3                              6th March 2026   Section 3.2 Alternative place of settlement

                                              Section 4 Update of Testing section

                                              Section 6 Update of Client Journey





  4 │ V.3,2 February March 2026

## PDF page 10

                                  EURONEXT SECURITIES - PSET CHANGE GUIDELINES





 2. APPROACH FOR PSET CHANGE





5 │ V.3,2 February March 2026

## PDF page 11

                                   EURONEXT SECURITIES - PSET CHANGE GUIDELINES





 Today, Euroclear CSDs are designated for settlement of equity and exchange-
 traded products trades executed in euros on Euronext’s markets in Amsterdam,
  Brussels and Paris.

 Following the change of place of settlement effective from 21 September 2026,
 Euronext Securities Milan will, by default, be the designated place of settlement
  for the trades executed on the relevant Euronext trading venues.



 2.1  Scope of markets and instruments


  Euronext will designate Euronext Securities Milan as the settlement organisation for all
  trades in euros executed on the following markets for the following instruments:


         Market               MIC                  Instrument

                                                                           equities,
                                                       exchange-traded products
Euronext Amsterdam              XAMS                                                             (including international ETPs)

                                                                           equities,
                                                       exchange-traded products
Euronext Paris                    XPAR                                                             (including international ETPs)

                                                                          equities
Euronext Access Paris                XMLI
                                                                          equities
Euronext Growth Paris               ALXP
                                                                           equities,
Euronext Brussels                 XBRU              exchange-traded products

                                                                          equities
Euronext Access Brussels           MLXB
                                                                          equities
Euronext Growth Brussels            ALXB



  All equities and exchange-traded products that are cleared and traded  in euros on
  applicable markets are in scope of the place of settlement change.

  Equities include shares and equity like instruments, e.g. stock warrants, that belong to the
  category Equities, field <instrument category> = 1 in Euronext cash standing data files.





  6 │ V.3,2 February March 2026

## PDF page 12

                                  EURONEXT SECURITIES - PSET CHANGE GUIDELINES





Exchange-traded products (ETPs) include exchange-traded funds (ETFs), exchange-traded
notes (ETNs), exchange-trades certificates (ETCs) that belong to the category Trackers,
field <instrument category> = 6 in Euronext cash standing data files.

In addition, Euronext has published the instrument list on the Euronext website (CSD
Expansion Documentation page) containing the list of ISINs affected by the change of place
of settlement. The document is dynamic and will be updated on a regular basis with newly
listed or delisted securities.

Note 1: For physically settled equity derivatives products, the place of settlement used will
be the same as for the underlying, therefore the physical settlement will be managed via
Euronext Securities Milan whenever applicable.

Note 2: The settlement set-up and procedures designated for transactions executed on
other instrument types (e.g., bonds, warrants and certificates, etc.) across Euronext
markets are not impacted by the PSET change described in this document.

2.2  Technical change in referential data


According to article 4601/1 of the Euronext trading rulebook, “Transactions executed on a
Euronext Securities Market shall be cleared in accordance with the rules and procedures
set forth in the Clearing Rule Book of the relevant Clearing Organisation, and settlement
shall be arranged through the settlement organisations designated by Euronext.”

As a trading venue, Euronext designates a settlement organisation for each instrument (at
Symbol Index level) and shares this information with trading members using the field
<MainDepositary>1 in the cash standing data files.

For all instruments2 in scope of the PSET change this field will be updated to Euronext
Securities Milan (value: '00012’ - Monte Titoli) on the effective date of the change.

2.3  Tax and legal


The below table provides the overview of the applicable company, securities and tax laws
for the various markets.

From a tax perspective, the table below details tax regimes as they relate to the PSET
change only. The PSET change brings in scope taxation on transactions in certain equities,
including those issued by certain French and UK issuers. These tax regimes as well as the




1 Identifies the default (or main) depository organisation of the used by priority for the settlement.
2 Exception made for international ETPs and ISINs where the current place of settlement is not the
domestic CSD, where technically the field <MainDepositary> will remain unchanged, even though
the designated CSDs is Euronext Securities.

7 │ V.3,2 February March 2026

## PDF page 13

                                   EURONEXT SECURITIES - PSET CHANGE GUIDELINES





  tax regimes as they apply on cross-border income taxation on shares are covered by
  existing and new tax services offered by Euronext Securities Milan to ensure clients can
  easily accommodate the requirements.

  All tax services offered by Euronext Securities Milan are described in greater detail in
  Service Description Documents (SDD) that are available on the Euronext website (CSD
  Expansion Documentation page).



                                                                UK/Ireland
   Model type       Law type    France  Belgium  Netherlands   (for multi-
                                                                                 listed)

Investor CSD                             Applicable law is the country of legal residence of
model              Company Law                      the Issuer

Issuer CSD model

Investor CSD                             Applicable law is the country of legal residence of                           Securities
model                                                    the Issuer                      Corporate Law
Issuer CSD model
                                            Applicable law is the law of the country of taxInvestor CSD
                                       residence of the Issuer and the law of the country ofmodel                  Withholding
                                        tax residence of the beneficial owner receiving the                       Tax Law
                                                      incomeIssuer CSD model

Investor CSD                                                                n/a                                              in scope3     n/a          n/a
model                         FTT
                                                                            n/a
Issuer CSD model                          in scope2     n/a          n/a
                                                                                            in scope
Investor CSD model                     n/a       n/a          n/a
                    Stamp Duty
                                                                                            in scope
Issuer CSD model                       n/a       n/a          n/a





  3 Not applicable for ETPs

  8 │ V.3,2 February March 2026

## PDF page 14

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





3. SETTLEMENT MODELS





9 │ V.3, March.2 February 2026

## PDF page 15

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





The following section outlines settlement models that will be possible once the
designation of Euronext Securities Milan for settlement is implemented.

Each  of  these models  represents  different  settlement  processes  for  the
instruments in scope. Furthermore, the settlement section of these operating
models will reflect the set up for clients selecting an alternative CSD for their
settlement activities.



3.1  Designated place of settlement


Following the change, Euronext Securities Milan will, by default, be the designated place
of settlement for the equities and exchange-traded products trades executed in euros on
the relevant Euronext trading venues.

3.2  Alternative place of settlement


Euronext Amsterdam, Paris and Brussels new settlement model offers their members the
right to designate a system for the settlement of transactions other than Euronext
Securities.

For  this purpose, Euronext has put  in place the following framework to recognize
alternative settlement venues, in line with the applicable regulatory. . The conditions for
this framework are currently under review and will be published in due time.

Trading members may choose an alternative CSD that has been validated and specified in
the Appendix A – Alternative settlement system applications document available on the
Connect portal.

Euronext confirmed on the 06/03/2026 that clients will be able to use Clearstream Banking
Europe AG or certain Euroclear CSDs as alternative CSDs.

Other settlement

Trading members may choose an alternative CSD that have been validated and specified
in the Appendix A – Alternative settlement system applications document available on the
Connect portal.

Other systems may apply with the relevant Euronext markets to become eligible subject
to the accomplishment of the procedure laid out by Article 53 of CSDR and the ESMA
Guidelines dated 8 June 2017.





10 │ V.3, March.2 February 2026

## PDF page 16

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES



3.3  Models


Trading:


    •  Two clients send trade orders to trading members.
    •  Trading members execute the transactions on the Euronext venue. The transaction
         is matched at the venue and subsequently sent for clearing.


Clearing:


    •  The trade is directed to Euronext Clearing, or a preferred CCPpreferred CCP that
      guarantees the transaction.
    •  Euronext Clearing handles the trades in real time, calculating margin and report
       executions, daily margin calls and relevant information to clearing members.
    •  Euronext  Clearing performs trade date  netting and  releases the  settlement
       instructions to Euronext Securities Milan.





Note:

    -   Please note that the trading and clearing process outlined above applies to all
       settlement models.
    -  Euronext Clearing is one of the counterparties for all guaranteed trades and has its
      account in Euronext Securities Milan.





11 │ V.3, March.2 February 2026

## PDF page 17

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES




  3.3.1  Settlement model for guaranteed instruments
         issued in Euronext Securities Milan


Euronext Securities Milan is the Issuer CSD.





 Scenario 1: Settlement in Euronext Securities Milan.

    •  Trading Member directly or indirectly (through  its clearing member/settlement
       agents) Settlement agent has an account in Euronext Securities Milan, allowing the
       settlement to be executed as T2S intra-CSD settlement.

Scenario 2: Settlement with alternative CSD within T2S.

    •  Settlement agent has an account in alternative CSD within T2S
    •  The settlement is executed as T2S Cross-CSD settlement.

  3.3.2  Settlement model for guaranteed instruments
         issued in another T2S CSD


The Issuer CSD is any other T2S CSD than Euronext Securities Milan.

   A. The alternative CSD is not the Issuer CSD





Scenario 1: Settlement in Euronext Securities Milan.




12 │ V.3, March.2 February 2026

## PDF page 18

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





    •  Settlement agent has an account  in Euronext  Securities Milan, allowing the
       settlement to be executed as T2S intra-CSD settlement.

Scenario 2: Settlement with alternative CSD within T2S.



    •  Settlement agent has an account in the alternative CSD.
    •  Settlement can either:
         o  (1) takes place via the alternative CSD acting as an investor CSD in Euronext
               Securities Milan as T2S cross-CSD settlement.
         o  2) or takes place via the alternative CSD acting as an investor CSD to the
              Issuer CSD, (where Euronext Securities Milan is also acting as Investor CSD
              to the Issuer CSD), and T2S automatic realignment taking place in the Issuer
           CSD.

   B. The Alternative CSD is the Issuer CSD





Scenario 1: Settlement in Euronext Securities Milan.

    •  Settlement agent has an account  in Euronext  Securities Milan, allowing the
       settlement to be executed as T2S intra-CSD settlement.

Scenario 2: Settlement with alternative CSD within T2S.



    •  Settlement agent has an account in the alternative CSD.
    •  The settlement is executed as T2S Cross-CSD settlement.





13 │ V.3, March.2 February 2026

## PDF page 19

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES




  3.3.3  Settlement model for guaranteed instruments
         issued in non-T2S CSD


The Issuer CSD is outside of T2S. Euronext Securities Milan is connected to the Issuer CSD
via its direct account with the Issuer CSD or through its account with an ICSD acting as
the technical issuer in T2S.





                                                   INVESTOR CSD LINK



Scenario 1: Settlement in Euronext Securities Milan.

    •  Settlement agent has an account  in Euronext  Securities Milan, allowing the
       settlement to be executed as T2S intra-CSD settlement.

Scenario 2: Settlement with alternative CSD within T2S.

    •  Settlement agent has accountan account in the alternative CSD.
    •   Either Euronext Securities or the alternative CSD appoint the other as technical
       issuer CSD Milan holds the securities on behalf of the alternative CSD.
    •  Settlement takes place is executed as T2S cross-CSD settlement.


3.4  Settlement for OTC


OTC transactions will remain available in Euronext Securities Milan thanks to the active
links in place with Euronext Securities Milan and other CSD and ICSD.

The exhaustive list of Euronext Securities Milan CSD direct links can be found in the table
below:





14 │ V.3, March.2 February 2026

## PDF page 20

                                    EURONEXT SECURITIES – PSET CHANGE GUIDELINES





                                                         Investor CSD    Issuer CSD
                                           T2S   (account held by   (account heldCountry        CSD name         Acronym
                                       CSD   ES-MIL in other  by other CSD in
                                                          CSD)          ES-MIL)
  AT    OeKB CSD Gmbh              OeKB      Yes         Yes           No
  BE     Euroclear Bank                 EB       No          Yes             Yes
  BE     Euroclear Belgium               EBE       Yes         Yes           No
  BE     National Bank of Belgium        NBB       Yes         Yes           No
  CH    SIX SIS Ltd                    SIX SIS     Yes         Yes           No
  DE    Clearstream Banking AG          CBF       Yes         Yes             Yes
  ES     Iberclear                          Iberclear     Yes         Yes             Yes
   FR     Euroclear France                 EF        Yes         Yes             Yes

         Bank of Greece securities
  GR                            BOGS      Yes         Yes           No          settlement system

  LU     Clearstream Banking SA          CBL      No          Yes             Yes
  NL     Euroclear Nederland             ENL       Yes         Yes           No
  UK     Euroclear UK & Ireland            EUI      No          Yes           No

          Depository Trust & Clearing  US                              DTCC      No          Yes           No
          Corporation

    All services offered by Euronext Securities Milan are described on the Euronext webpage,
   information on the coverage per asset class and jurisdiction can be provided upon request.





   15 │ V.3, March.2 February 2026

## PDF page 21

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





  4. CHANGE OF PSET – PLAN





16 │ V.3, March.2 February 2026

## PDF page 22

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES



4.1  PSET change high level timeline


Below are the key milestones to facilitate the place of settlement change.





    -  Open of client testing window: 5 March 2026
         o  Front to Back testing - 5 March 2026 to 31 July 2026
         o  Position transfer – 5 March 2026 to 31 July 2026
         o  Corporate actions - 4 May 2026 to 31 July 2026
         o   Fiscal services - 4 May 2026 to 31 July 2026
         o  General Meeting and Proxy Voting - 4 May 2026 to 31 July 2026
         o  Registered securities - 4 May 2026 to 31 July 2026
         o  Post trade confirmation system - 5 March 2026 to 31 July 2026
    -  End of client testing window: 31 July 2026
    -   Place of Settlement change go-live: 21 September 2026


       4.1.1 Production environment

The place of settlement change to Euronext Securities Milan  will take place on 21
September 2026 for all instruments in scope (specified in section 2.1) with a contingency
date of 12 October 2026.


       4.1.2 Test environment

The place of settlement change for the subset of instruments will take place on 5 March
2026 in EUA (test) environment. All the documentation to support testing has been
published on the European Offering Documentation.





17 │ V.3, March.2 February 2026

## PDF page 23

                                     EURONEXT SECURITIES – PSET CHANGE GUIDELINES



  4.2  Framework of PSET change

          4.2.1 Pre-requisites for the settlement in Euronext
          Securities Milan

    Settlement agents must have an account at Euronext Securities Milan in order to settle in
    the designated place of settlement. This also entails the following:

        1.  Connectivity: Formal membership request for connectivity validated and approved.
        2.  Production access: All production access must have been tested and validated.
        3. Onboarding: Test and Production account structure must have been finalised in
          advance of the date when the change will take place.
        4.  Testing: Mandatory test to be performed and confirmed by returning to Euronext a
           readiness form.


          4.2.2 PSET change weekend

   The following timeline highlights the impact on the place of settlement of equities and
    exchange-traded products.


     Trade date     Euronext actions  Place of settlement  Day of settlement


                                             Previous place of
  Wednesday (D-3)         N/A                                        Friday
                                               settlement


                                             Previous place of
  Thursday (D-2)           N/A                               Monday
                                               settlement


                                             Previous place of
  Friday (D-1)             N/A                                  Tuesday
                                               settlement


                   Change of place of
                         settlement to
  Weekend (D)                               N/A                N/A
                          Euronext
                          Securities Milan


  Monday (D+1)           N/A              ES-MIL           Wednesday


All details related to the weekend when the change will take place will be shared in due course.





    18 │ V.3, March.2 February 2026

## PDF page 24

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES



4.3  Specific processes impacted by PSET
    change

       4.3.1 Pending/Failing transactions

If a pending/failing transaction is positioned during the transfer, the place of settlement is
to be the original one.

     -   Pending transactions: market instructions in progress, matched that can still settle
      on their intended settlement date.
     -   Failing transactions: market instructions that are no longer eligible for settlement
      on their intended settlement date.

              Date of trade                                      Final place of
                                   Original place of settlement
                 execution                                     settlement

                                                                     Previous place of
              Before PSET change    Previous place of settlement
 Pending                                                               settlement
 transaction
                 After PSET change             ES-MIL                 ES-MIL

                                                                     Previous place of
              Before PSET change    Previous place of settlement
                                                                       settlement Failing
 transactions                                                                     Previous place of
                 After PSET change    Previous place of settlement*
                                                                     settlement*

*Only for failing market instructions will be possible to still settle in the previous place of
settlement although there might be exceptions where market instructions will be rebooked
having PSET ES-MIL.

It is impossible for the CSD to cancel market instructions. Clients will have to deal with the
pending transactions as usual (for example: penalties for late settlement).


       4.3.2 Corporate actions

In the following models, the different scenarios highlight the fact that the change of PSET
does not impact the corporate action processes.

The scope of this analysis only concerns the mandatory corporate actions.

To understand the process of corporate actions, three key dates should first be highlighted:

    •  Ex date (date on which a stock starts trading without the benefits of corporate
       actions),



19 │ V.3, March.2 February 2026

## PDF page 25

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





    •  Record date (date at which the company lists the shareholders that are eligible for
       corporate action),
    •  Payment date (date at which the dividends or other proceeds are paid out).

In this sense, if a trade (that is negotiated before the ex-date) is effectively settled passed
the record date, then there will be a case of market claim or transformation. Regardless,
the original place of settlement will process the market claim/transformation (hence the
change of PSET does not impact corporate action).





The testing will be open as of 5 March 2026 on a subset of instruments. The  list of
instruments will be communicated in due course.

The above planning highlights the Client test phases that will be supported by Euronext.
Testing outside of the Client test phases remain available whenever Test platform is open
and will be supported by Euronext on best effort basis.


       4.3.3 Deferred Settlement Service (DSS)

Information on the process for deferred settlement following the PSET change will be
provided in due course.





20 │ V.3, March.2 February 2026

## PDF page 26

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES



4.4  Testing


The scope of testing for the European Offering covers the key functional and operational
changes introduced across the post-trade value chain. Testing is designed to validate
that these changes operate correctly on a standalone basis and, where relevant, end-to-
end across multiple actors. The overall scope includes services covering issuance,
trading, clearing, settlement, safekeeping, corporate actions, and fiscal services. Testing
focuses on areas where new services are introduced, or interfaces and message flows are
materially impacted.

Testing scope vary depending on the type of market participant and the services they
use. To support this, a service-by-participant matrix for Euronext clients is provided
below, indicating the expected level of testing per combination. For clients of Euronext
Markets (Trading Members) and Euronext Clearing (Clearing Members), front-to-back
testing are applicable. For clients of Euronext Securities (Settlement Agents and
Custodians), testing includes a greater set of services in addition to front-to-back. Where
relevant, clients are expected to align testing needs with their providers.

The matrix should be read as a guide to support planning and coordination of testing
activities and to ensure consistent expectations across participant categories.


 Services            Trading       Clearing     Settlement    Custodian
                Member     Member       Agent


 Front-to-back     Mandatory    Mandatory    Mandatory    Mandatory
 testing


 Registered            N/A           N/A          Conditional      Conditional
 Shares and
 Information on
 Registered
 Investors (IRI)


 Stamp Duty           N/A           N/A          Conditional      Conditional


 Post Trade            Conditional        N/A          Conditional      Conditional
 Confirmation
 System (PTCS)


 Portfolio              N/A           N/A          Conditional      Conditional
 Migration and
 Position Transfer





21 │ V.3, March.2 February 2026

## PDF page 27

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





 Services            Trading       Clearing     Settlement    Custodian
                Member     Member       Agent


 Fiscal Services         N/A           N/A      Recommended  Recommended
 (Tax)


 Corporate Events       N/A           N/A      Recommended  Recommended


 General Meetings       N/A           N/A      Recommended  Recommended
 and Proxy Voting




The following definitions apply:

Mandatory to Test
Testing is mandatory. Participants must execute the relevant tests and provide a formal
sign-off document as evidence of successful testing and operational readiness.

Recommended to Test
Testing is not mandatory but is strongly advised for participants seeking to reduce
operational risk or gain confidence in using the new service. No formal sign-off is
required.

Conditional to Test
Testing is mandatory only for participants of Euronext Securities who are impacted by
the change or who have explicitly requested the service.


       4.4.3 Supporting documentation and events

Supportive documentation

To support structured and consistent testing, each Euronext entity will publish relevant
client test documentation and/or communication specifically for their clients and services.
The client test documentation includes will typically include:

    -  Guide to support test execution
    -   Test scenarios and test sets
    -   Test data and reference information to be used across test environments, where
       applicable
    -  Relevant readiness and sign-off forms to be completed, where applicable

   The detailed client test documentation from each Euronext entity can be found by
    following the links below:



22 │ V.3, March.2 February 2026

## PDF page 28

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





    •  Euronext Markets: Connect - Euronext Securities European Offering
    •  Euronext Clearing: Connect - European Offering / Choice of CSD
    •  Euronext Securities: European Offering Documentation

Supportive events

We will prepare and support the client testing window by the next events and meetings:

     -  A second related Webinar on 29/1/2026 to present the deeper details on the client
       testing
     -  A series of preparatory meetings to capture questions and remarks in the period
        prior to the start of testing.
     -   During the test execute (Client Testing Window) we will have regular touch point
      meetings to capture and discuss progress and status.

       4.4.1 Mandatory testing

End-to-end market flow testing is mandatory for all market participants.

Trading members, their clearing members and settlement agents are required to co-
ordinate end-to-end testing to ensure the successful flow of trade information and
reporting is in place, to facilitate reconciliations and ensure the completeness of data
throughout the post-trade chain.

All market participants will be expected to confirm that the end-to-end test has been
completed successfully via a dedicated form by 1 June 2026.

    -   Client test phase supported by Euronext.
    -  End-to-end market flow - 5 March 2026 to 1 June 2026


       4.4.2 Conditional testing

As part of the transition to Euronext Securities Milan, we are committed to ensuring a
seamless experience for our clients by offering a suite of services equivalent to those
currently available at the existing place of settlement. These include:

           -   Shareholder  Identification  services. Euronext  Securities Milan  will provide
            efficient Shareholder ID services, compliant with CSD Regulations, to enable
           issuers to identify their shareholders.
           -   Post trade confirmation services. To support clients in managing the settlement
           of their transactions regarding market trades, Euronext  will implement an
            efficient Post Trade Confirmation System that will ease the settlement process
           of their trades, including a Deferred Settlement Service.
           -   Registered Securities management. Euronext Securities Milan will implement a
        new platform that will allow custodians and registrars to manage registered
           securities in compliance with existing national regulations.
           -   Corporate Events processing. A comprehensive Corporate Events service will be
           available, covering mandatory and voluntary corporate events in line with the


23 │ V.3, March.2 February 2026

## PDF page 29

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





         needs of stakeholders in the Asset Services space, including issuers, their agents
         and custodian banks for all markets in scope covering their specificities
           -   Fiscal services.

Service descriptions documents (SDD) for each of these services are provided on the
Euronext website (CSD Expansion Documentation).

Clients that choose to make use of these services are able to perform the testing during
Client test phases supported by Euronext.

    -   Position transfer – 5 March 2026 to 1 May 2026
    -   Post trade confirmation system - 5 March 2026 to 1 May 2026
    -  Corporate actions - 4 May 2026 to 30 June 2026
    -   Fiscal services - 4 May 2026 to 30 June 2026
    -  General Meeting and Proxy Voting - 4 May 2026 to 30 June 2026
    -   Registered securities - 4 May 2026 to 30 June 2026

* ES-MIL will offer clients the possibility to test portfolio migration to reap the benefits of
the integrated model. Either ICP or DCP can provide portfolio details and ES-MIL will enter
the receiving instruction leg automatically on behalf of clients directly in the accounts
opened in ES-MIL.


       4.4.3 Supporting documentation

Supporting documentation will be made available on the Euronext website (CSD Expansion
Documentation page) and will include:

    -   List of instruments for end-to-end market flow testing
    -   Details of available services and the timeline for the testing
    -   Guidelines for testing and recommended test scenarios

The above documentation will be available one month before the client testing starts.
Clients would need to submit the client readiness form to confirm the completion of testing.

4.5  Freeze period


Euronext will apply a freeze period to the management of membership changes before the
place of settlement change to ensure the configuration stability.

Details will be provided in due course.





24 │ V.3, March.2 February 2026

## PDF page 30

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES



4.6  Communication and support

       4.6.1 Communication

Regular updates are shared via e-mail notification and dedicated technical webinars. Latest
documentation are published on the the Euronext website – CSD Expansion Documentation
page.

The progress and updates on PSET change will be addressed in the local industry groups.

Additionally, Euronext will maintain regular dialogue with all impacted clients to answer
questions, monitor progress and support the tests.

       4.6.2 Support contacts

For any additional queries, clients can contact:



Trading members:

Email: clientsupport@euronext.com

Telephone:

Belgium +32 2620 0585      Netherlands +31 20 721 9585

France +33 1 8514 8585      Norway +31 20 721 9585

Ireland +353 1 6174 289      Portugal +351 2 1060 8585

Italy +39 02 4541 1399     UK +44 207 660 8585

Service hours: 08:00 – 19:00 CET/CEST



Clearing members:

Euronext Clearing Client Readiness Team

Email: CCP-readiness@euronext.com

Telephone: +39 06 32 39 52 30

Service hours: 08:30 – 18:00 CET/CEST





25 │ V.3, March.2 February 2026

## PDF page 31

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





Settlement agents and custodians:

Email: CSD.Onboarding@euronext.com

Service hours: 08:30 – 18:00 CET/CEST





26 │ V.3, March.2 February 2026

## PDF page 32

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





 5. SPECIFIC ACTIONS FOR SETTLEMENT
   AGENT, CLEARING MEMBER ACTING AS
   SETTLEMENT AGENTS AND CUSTODIANS





27 │ V.3, March.2 February 2026

## PDF page 33

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





Starting from 23 September 2026, market settlement instructions will settle in
Euronext Securities Milan as intra or cross-CSD instructions. Clients are invited
to guarantee the sufficient position of asset inventories in order to settle market
instructions in accordance with the account structure defined with clearing
members.

5.1 Onboarding of new clients


To provide a smooth onboarding process for new  clients, Euronext  will provide the
necessary support to allow clients to receive and provide all the information needed. The
onboarding process will be overseen by a dedicated team and described in the Onboarding
handbook detailing available on the Euronext Securities Milan webpage.



5.2  Configuration  for new  and  existing
clients


To settle in Euronext Securities Milan, clients would need to ensure the relevant account
structure is in place. For all clients of Euronext Securities Milan, this phase will ensure the
readiness of clients for the testing phase that will start in March 2026. This phase will allow
clients to determine their specific needs in line with the migration.

Clients are recommended,  for  registered  shares,  to  activate the usual process  of
registration/deregistration.



5.3 Position transfer


Clients who would like to centralise custody with Euronext Securities Milan would need to
perform a position transfer from their current place of safekeeping to Euronext Securities
Milan.  Euronext will provide all necessary support including the client test phase for
position transfer, including dedicated support on settlement depo realignment cross-CSD
between relevant CSD and ES-MIL beneficiary accounts.

Direct Connected Participants (DCP) can leverage on T2S functionalities in order to transfer
assets from the CSD.

More details will be communicated in due course.




28 │ V.3, March.2 February 2026

## PDF page 34

                                 EURONEXT SECURITIES – PSET CHANGE GUIDELINES





6. CLIENT JOURNEY





29 │ V.3, March.2 February 2026

## PDF page 35

                                       EURONEXT SECURITIES – PSET CHANGE GUIDELINES



   6.1 Purpose of the client journey

     The client journey provides a step-by-step overview of the actions required from clients to
      complete their onboarding and setup across trading, clearing and CSD levels. It is tailored
       to reflect the specific requirements of each client type and aims to support a coordinated
      process of PSET change.

     More details on the corresponding trading and clearing related actions will be shared in the
      next version in September 2025.

   6.2  Client journey  for the settlement  in
        Euronext Securities

           6.2.1    For trading members



Phase              Actions              Set up for      Action status          How to                   Deadline


             Align on the settlement set up                                                          Recommended date: by 1
set up                                                   mandatory         Contact clearing member                with cleating member                                                                      December 2025

                                     On              Client decision on settlement                                           Confirmation via applicable
set up                                    exchange        mandatory                                     By 1 June 2026                    system                                                           form
                                     OTC

           Complete end-to-end market       On                                      Client's confirmation via test                                                    mandatory                                       by 31 July 2026                       flow test              exchange                                    applicable form

             Update / share the SSIs
set up          (Securities Settlement         OTC              optional            Contact counterparties         By September 2026
                      Instructions)



           6.2.2    For General Clearing Members not acting
                  as settlement agents



Phase              Actions              Set up for      Action status          How to                   Deadline


             Align on the settlement set up                                                           Recommended date: by 1set up                                                   mandatory         Contact trading members
                with trading members                                                                     December 2025

           Provide a the updated clearing
                                     On            account structure for testing                      mandatory               Contact CCP              By 1 April 2026
set up                                    exchange                     (EUA)

             Provide the updated clearing
set up    account structure for production       All clients        mandatory               Contact CCP              By 1 June 2026
                   (PROD)

           Complete end-to-end market       On                                      Client's confirmation via
 test                                                    mandatory                                       by 31 July 2026                       flow test              exchange                                  readiness form




      30 │ V.3, March.2 February 2026

## PDF page 36

                                      EURONEXT SECURITIES – PSET CHANGE GUIDELINES





           6.2.3    For General Clearing Members acting as
                   settlement agents





Phase             Actions                 Set up for       Action status          How to                   Deadline


         Onboarding to ES-Milan
          (contractual):

              •  Fill in the form: Request for                                            Contact onboarding team via:     Recommendation: Q1
set up        Services                    New clients        mandatory     CSD.Onboarding@euronext.com           2026
                                                                                                        Recommendation: Q1
              •  Self-certification form                                                                                                           2026
              • Specimen Signature                                                                           Recommendation: Q1
              • Fatca CRS                                                                                       2026
         Onboarding to ES-Milan
                                                                                   Contact onboarding team via:     Recommendation: Q1set up   (connectivity) - Account            New clients        mandatory
                                                                          CSD.Onboarding@euronext.com           2026          Structure - RMA Exchange

          Setting up the accounts in CSD                                             Contact onboarding team via:     Recommendation: Q1set up                               New clients        mandatory
          (ES-Milan)                                                         CSD.Onboarding@euronext.com           2026

          Setting up the accounts in CSD                                                                                   Contact onboarding team via:     Recommendation: Q1
set up   (ES-Milan) if not leveraging on         Existing clients       mandatory                                                                          CSD.Onboarding@euronext.com           2026
          existing account structure
          Provide the updated clearing
set up   account structure for testing                 All clients         mandatory              Contact CCP              By 1 April 2026
         (EUA)
          Provide the updated clearing
set up   account structure for production            All clients         mandatory              Contact CCP              By 1 June 2026
        (PROD)

        Complete end-to-end market                                                           Client's confirmation via test                                                         All clients         mandatory                                    By 31 July 2026
          flow test                                                                           readiness form

        Complete functional tests for        Depends on the                       Contact onboarding team via:                                                                           optional                                     By 30 June 2026          additional services                    selected service                    CSD.Onboarding@euronext.com

              • Post-Trade Confirmation         All clients who want                                                         Testing: 5 March 2026 –
                                                                           optional          Contact onboarding team              Service (PTCS)                 to access the service                                                   31 July 2026

                                                          All clients who want                                                         Testing: 4 May 2026 – 31
              • Registered securities                                       optional          Contact onboarding team
                                               to access the service                                                                    July 2026

                                                          All clients who want                                                         Testing: 4 May 2026 – 31
 test       • Corporate events                                          optional          Contact onboarding team                                               to access the service                                                                    July 2026

                                                          All clients who want                                                         Testing: 4 May 2026 – 31
              • General meeting services                                  optional          Contact onboarding team                                               to access the service                                                                    July 2026

                                                          All clients who want                                                         Testing: 4 May 2026 – 31
              • Proxy voting                                               optional          Contact onboarding team
                                               to access the service                                                                    July 2026

              •  Fiscal services and Stamp        All clients who want                                                         Testing: 4 May 2026 – 31                                                                           optional          Contact onboarding team             Duty                           to access the service                                                                    July 2026


set up      • Update/share the SSIs                  All clients         mandatory          Contact counterparties         By September 2026





     31 │ V.3, March.2 February 2026

## PDF page 37

                                      EURONEXT SECURITIES – PSET CHANGE GUIDELINES




          6.2.4    For settlement agent





Phase              Actions                 Set up for       Action status          How to                  Deadline


          Onboarding to ES-Milan
           (contractual):

               •  Fill in the form: Request for                                            Contact onboarding team via:    Recommendation: Q1
set up        ServicesContact              New clients        mandatory     CSD.Onboarding@euronext.com          2026
                                                                                                        Recommendation: Q1
               •  Self-certification form
                                                                                                           2026
               • Specimen Signature                                                                           Recommendation: Q1
               • Fatca CRS                                                                                      2026
          Onboarding to ES-Milan
                                                                                    Contact onboarding team via:    Recommendation: Q1set up    (connectivity) - Account            New clients        mandatory
                                                                           CSD.Onboarding@euronext.com          2026           Structure - RMA Exchange

           Setting up the accounts in CSD                                             Contact onboarding team via:    Recommendation: Q1
set up                                New clients        mandatory          (ES-Milan)                                                         CSD.Onboarding@euronext.com          2026

           Setting up the accounts in CSD                                                                                    Contact onboarding team via:    Recommendation: Q1
set up    (ES-Milan) if not leveraging on         Existing clients       mandatory                                                                           CSD.Onboarding@euronext.com          2026           existing account structure

         Complete end-to-end market                                                           Client's confirmation via test                                                          All clients         mandatory                                   By 31 July 2026
           flow test                                                                           readiness form

         Complete functional tests for        Depends on the                       Contact onboarding team via:                                                                            optional                                    By 30 June 2026           additional services                    selected service                    CSD.Onboarding@euronext.com

               • Post-Trade Confirmation         All clients who want                                                         Testing: 5 March 2026
                                                                            optional          Contact onboarding team               Service (PTCS)                 to access the service                                                 – 31 July 2026

                                                           All clients who want                                                          Testing: 4 May 2026 –
               • Registered securities                                       optional          Contact onboarding team
                                                to access the service                                                  31 July 2026

                                                           All clients who want                                                          Testing: 4 May 2026 –
 test         • Corporate events                                          optional          Contact onboarding team                                                to access the service                                                  31 July 2026

                                                           All clients who want                                                          Testing: 4 May 2026 –
               • General meeting services                                  optional          Contact onboarding team                                                to access the service                                                  31 July 2026

                                                           All clients who want                                                          Testing: 4 May 2026 –
               • Proxy voting                                               optional          Contact onboarding team
                                                to access the service                                                  31 July 2026

               •  Fiscal services and Stamp        All clients who want                                                          Testing: 4 May 2026 –                                                                            optional          Contact onboarding team             Duty                           to access the service                                                  31 July 2026


set up       • Update/share the SSIs                  All clients         mandatory          Contact counterparties        By September 2026





    32 │ V.3, March.2 February 2026

## PDF page 38

                                       EURONEXT SECURITIES – PSET CHANGE GUIDELINES




           6.2.5    For custodian
   6.2  Client journey  for the settlement  in
        Euronext Securities Milan

   Phase              Actions                Set up for       Action status          How to                  Deadline


             Onboarding to ES-Milan
               (contractual):

                   •  Fill in the form: Request                                             Contact onboarding team via:    Recommendation: Q1
   set up           for Services                New clients        mandatory     CSD.Onboarding@euronext.com          2026
                                                                                                          Recommendation: Q1
                   •  Self-certification form
                                                                                                             2026
                   • Specimen Signature                                                                         Recommendation: Q1
                   • Fatca CRS                                                                                     2026
             Onboarding to ES-Milan
                                                                                      Contact onboarding team via:    Recommendation: Q1   set up     (connectivity) - Account           New clients        mandatory
                                                                             CSD.Onboarding@euronext.com          2026               Structure - RMA Exchange

               Setting up the accounts in                                                Contact onboarding team via:    Recommendation: Q1
   set up                               New clients        mandatory           CSD (ES-Milan)                                                   CSD.Onboarding@euronext.com          2026

               Setting up the accounts in
           CSD (ES-Milan) if not                                                    Contact onboarding team via:    Recommendation: Q1   set up                                            Existing clients       mandatory               leveraging on existing account                                       CSD.Onboarding@euronext.com          2026
               structure

             Complete end-to-end market                                                         Client's confirmation via
    test                                                         All clients         mandatory                                   By 31 July 2026
               flow test                                                                         readiness form

             Complete functional tests for      Depends on the                       Contact onboarding team via:
                                                                              optional                                    By 30 June 2026                additional services                  selected service                    CSD.Onboarding@euronext.com

                   • Post-Trade Confirmation       All clients who want                                                         Testing: 5 March 2026
                                                                              optional          Contact onboarding team                   Service (PTCS)               to access the service                                                 – 31 July 2026

                                                              All clients who want                                                         Testing: 4 May 2026 –
                   • Registered securities                                     optional          Contact onboarding team
                                                  to access the service                                                  31 July 2026

                                                              All clients who want                                                          Testing: 4 May 2026 –
    test          • Corporate events                                        optional          Contact onboarding team                                                  to access the service                                                  31 July 2026

                                                              All clients who want                                                          Testing: 4 May 2026 –
                   • General meeting services                                optional          Contact onboarding team                                                  to access the service                                                  31 July 2026

                                                              All clients who want                                                          Testing: 4 May 2026 –
                   • Proxy voting                                             optional          Contact onboarding team
                                                  to access the service                                                  31 July 2026

                   •  Fiscal services and Stamp     All clients who want                                                          Testing: 4 May 2026 –
                                                                              optional          Contact onboarding team                 Duty                         to access the service                                                  31 July 2026

                                                                                      Contact onboarding team via:
 migration   Position Transfer                             All clients             optional                                          Not applicable                                                                             CSD.Onboarding@euronext.com


   set up     Update/share the SSIs                     All clients         mandatory          Contact counterparties        By September 2026


           6.2.1    For trading members



Phase              Actions              Set up for      Action status          How to                   Deadline


             Align on the settlement set up                                                          Recommended date: by 1
set up                                                   mandatory         Contact clearing member                with cleating member                                                                      December 2025




      33 │ V.3, March.2 February 2026

## PDF page 39

                                       EURONEXT SECURITIES – PSET CHANGE GUIDELINES





             Update / share the SSIs
set up          (Securities Settlement         OTC              optional            Contact counterparties            Q1 2026
                      Instructions)

                                     On
               Client decision on custodyset up                                    exchange            optional              Contact custodian             Q1 2026
                       options                                     OTC

           Complete end-to-end market       On                                      Client's confirmation via test                                                    mandatory                                       by 1 June 2026
                       flow test              exchange                                    applicable form



           6.2.2    For General Clearing Members not acting
                  as settlement agents



Phase              Actions              Set up for      Action status          How to                   Deadline


             Align on the settlement set up                                                           Recommended date: by 1set up                                                   mandatory         Contact trading members
                with trading members                                                                     December 2025

             Provide the updated clearing                                     On                                                                       Prior to the start of testing,
            account structure for testing                      mandatory               TBDset up                                    exchange                                                      by 20 February 2026
                     (EUA)

           Complete end-to-end market       On                                      Client's confirmation via
 test                                                    mandatory                                       by 1 June 2026                       flow test              exchange                                    applicable form
           6.2.3    For General Clearing Members acting as
                   settlement agents





 Phase             Actions                 Set up for       Action status          How to                   Deadline


          Onboarding to ES-Milan                                                                                             Start is not later than
           (contractual):                                                                                   1 December 2025

               •  Fill in the form: Request for                                            Contact onboarding team via:
                                                                                                       By 31 Jan 2025
 set up        Services                    New clients        mandatory     CSD.Onboarding@euronext.com

               •  Self-certification form                                                                         By 31 Jan 2025

               • Specimen Signature
                                                                                                       By 31 Jan 2025
               • Fatca CRS
          Onboarding to ES-Milan                                                                                    Contact onboarding team via:
 set up   (connectivity) - Account            New clients        mandatory                                    By 20 Feb 2025                                                                           CSD.Onboarding@euronext.com
           Structure - RMA Exchange

           Setting up the accounts in CSD                                             Contact onboarding team via:
 set up                               New clients        mandatory                                    By 20 Feb 2026           (ES-Milan)                                                         CSD.Onboarding@euronext.com

           Setting up the accounts in CSD                                                                                    Contact onboarding team via: set up   (ES-Milan) if not leveraging on         Existing clients       mandatory                                    By 20 Feb 2026
                                                                           CSD.Onboarding@euronext.com            existing account structure

 set up   Update/share the SSIs                        All clients         mandatory          Contact counterparties            Q1 2026

           Provide the updated clearing                                                                                                Prior to the start of
 set up   account structure for testing                 All clients         mandatory              TBD                    testing, by 20 February
          (EUA)                                                                                              2026

          Complete end-to-end market                                                           Client's confirmation via
  test                                                         All clients         mandatory                                     By 1 June 2026           flow test                                                                               applicable form



      34 │ V.3, March.2 February 2026

## PDF page 40

                                     EURONEXT SECURITIES – PSET CHANGE GUIDELINES





       Complete functional tests for        Depends on the                       Contact onboarding team via:                                                                         optional                                     By 30 June 2026
         additional services                    selected service                    CSD.Onboarding@euronext.com

            • Post-Trade Confirmation         All clients who want                                                         Testing: 5 March 2026 –
                                                                         optional          Contact onboarding team             Service (PTCS)                 to access the service                                                   30 Apr 2026

                                                        All clients who want                                                         Testing: 1 May 2026 – 30
            • Registered securities                                       optional          Contact onboarding team                                              to access the service                                                         June 2026

                                                        All clients who want                                                         Testing: 1 May 2026 – 30
test       • Corporate events                                          optional          Contact onboarding team
                                              to access the service                                                         June 2026

                                                        All clients who want                                                         Testing: 1 May 2026 – 30
            • General meeting services                                  optional          Contact onboarding team                                              to access the service                                                         June 2026

                                                        All clients who want                                                         Testing: 1 May 2026 – 30
            • Proxy voting                                               optional          Contact onboarding team                                              to access the service                                                         June 2026

                                                        All clients who want                                                         Testing: 1 May 2026 – 30
            •  Fiscal services                                             optional          Contact onboarding team
                                              to access the service                                                         June 2026





    35 │ V.3, March.2 February 2026

## PDF page 41

                                      EURONEXT SECURITIES – PSET CHANGE GUIDELINES




          6.2.4    For settlement agent





Phase              Actions                 Set up for       Action status          How to                  Deadline


          Onboarding to ES-Milan                                                                                            Start is not later than
           (contractual):                                                                                  1 December 2025

               •  Fill in the form: Request for                                            Contact onboarding team via:
                                                                                                      By 31 Jan 2025
set up        ServicesContact              New clients        mandatory     CSD.Onboarding@euronext.com

               •  Self-certification form                                                                         By 31 Jan 2025

               • Specimen Signature                                                                                                      By 31 Jan 2025
               • Fatca CRS
          Onboarding to ES-Milan
                                                                                    Contact onboarding team via:set up    (connectivity) - Account            New clients        mandatory                                    By 20 Feb 2025
                                                                           CSD.Onboarding@euronext.com           Structure - RMA Exchange

           Setting up the accounts in CSD                                             Contact onboarding team via:
set up                                New clients        mandatory                                    By 20 Feb 2026          (ES-Milan)                                                         CSD.Onboarding@euronext.com

           Setting up the accounts in CSD                                                                                    Contact onboarding team via:
set up    (ES-Milan) if not leveraging on         Existing clients       mandatory                                    By 20 Feb 2026                                                                           CSD.Onboarding@euronext.com           existing account structure

set up    Update/share the SSIs                        All clients         mandatory          Contact counterparties           Q1 2026


         Complete end-to-end market                                                           Client's confirmation via test                                                          All clients         mandatory                                    By 1 June 2026           flow test                                                                               applicable form

         Complete functional tests for        Depends on the                       Contact onboarding team via:
                                                                            optional                                    By 30 June 2026           additional services                    selected service                    CSD.Onboarding@euronext.com

               • Post-Trade Confirmation         All clients who want                                                         Testing: 5 March 2026                                                                            optional          Contact onboarding team
               Service (PTCS)                 to access the service                                                 – 30 Apr 2026

                                                           All clients who want                                                          Testing: 1 May 2026 –
               • Registered securities                                       optional          Contact onboarding team                                                to access the service                                                  30 June 2026

                                                           All clients who want                                                          Testing: 1 May 2026 –
 test         • Corporate events                                          optional          Contact onboarding team                                                to access the service                                                  30 June 2026

                                                           All clients who want                                                          Testing: 1 May 2026 –
               • General meeting services                                  optional          Contact onboarding team
                                                to access the service                                                  30 June 2026

                                                           All clients who want                                                          Testing: 1 May 2026 –
               • Proxy voting                                               optional          Contact onboarding team                                                to access the service                                                  30 June 2026

                                                           All clients who want                                                          Testing: 1 May 2026 –
               •  Fiscal services                                             optional          Contact onboarding team                                                to access the service                                                  30 June 2026





    36 │ V.3, March.2 February 2026

## PDF page 42

                                      EURONEXT SECURITIES – PSET CHANGE GUIDELINES




           6.2.5    For custodian





  Phase              Actions                Set up for       Action status          How to                  Deadline


            Onboarding to ES-Milan                                                                                          Start is not later than
              (contractual):                                                                                 1 December 2025

                  •  Fill in the form: Request                                             Contact onboarding team via:
                                                                                                       By 31 Jan 2025
  set up           for Services                New clients        mandatory     CSD.Onboarding@euronext.com

                  •  Self-certification form                                                                       By 31 Jan 2025

                  • Specimen Signature                                                                                                       By 31 Jan 2025
                  • Fatca CRS
            Onboarding to ES-Milan
                                                                                     Contact onboarding team via:  set up     (connectivity) - Account           New clients        mandatory                                    By 20 Feb 2025
                                                                            CSD.Onboarding@euronext.com             Structure - RMA Exchange

              Setting up the accounts in                                                Contact onboarding team via:
  set up                               New clients        mandatory                                    By 20 Feb 2026          CSD (ES-Milan)                                                   CSD.Onboarding@euronext.com

              Setting up the accounts in
          CSD (ES-Milan) if not                                                    Contact onboarding team via:  set up                                            Existing clients       mandatory                                    By 20 Feb 2026             leveraging on existing account                                       CSD.Onboarding@euronext.com
              structure

  set up     Update/share the SSIs                     All clients         mandatory          Contact counterparties           Q1 2026


            Complete end-to-end market                                                         Client's confirmation via
   test                                                         All clients         mandatory                                    By 1 June 2026              flow test                                                                             applicable form

            Complete functional tests for      Depends on the                       Contact onboarding team via:
                                                                             optional                                    By 30 June 2026              additional services                  selected service                    CSD.Onboarding@euronext.com

                  • Post-Trade Confirmation       All clients who want                                                         Testing: 5 March 2026                                                                             optional          Contact onboarding team
                  Service (PTCS)               to access the service                                                 – 30 Apr 2026

                                                            All clients who want                                                         Testing: 5 March 2026
                  •  Position Transfer                                         optional          Contact onboarding team                                                 to access the service                                                 – 30 Apr 2026

                                                            All clients who want                                                          Testing: 1 May 2026 –
                  • Registered securities                                     optional          Contact onboarding team                                                 to access the service                                                  30 June 2026
   test
                                                            All clients who want                                                          Testing: 1 May 2026 –
                  • Corporate events                                        optional          Contact onboarding team
                                                 to access the service                                                  30 June 2026

                                                            All clients who want                                                          Testing: 1 May 2026 –
                  • General meeting services                                optional          Contact onboarding team                                                 to access the service                                                  30 June 2026

                                                            All clients who want                                                          Testing: 1 May 2026 –
                  • Proxy voting                                             optional          Contact onboarding team                                                 to access the service                                                  30 June 2026

                                                            All clients who want                                                          Testing: 1 May 2026 –
                  •  Fiscal services                                           optional          Contact onboarding team
                                                 to access the service                                                  30 June 2026

                                                                                     Contact onboarding team via:
migration   Position Transfer                             All clients             optional                                          Not applicable                                                                            CSD.Onboarding@euronext.com





     37 │ V.3, March.2 February 2026

## PDF page 43

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





              https://www.euronext.com/en/post-trade/euronext-securities



38 | Subtitle text, Verdana 9pt, Left aligned