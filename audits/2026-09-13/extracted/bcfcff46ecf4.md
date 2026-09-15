
## PDF page 1
ECSDA CSDR
Penalties Framework





Latest updated September 2024

## PDF page 2
Last updated on 11/09/2024


ECSDA SETTLEMENT FAILS PENALTIES FRAMEWORK

Contents

Glossary ................................................................................................................................................... 5

Introduction ........................................................................................................................................... 10

1   ECSDA CSDR Penalties Framework - key considerations ............................................................ 13

2    Penalties Lifecycle and Business Days Calendar .......................................................................... 15

   2.1    Intra-CSD settlement fails ..................................................................................................... 15

      2.1.1   Business Days calendars ................................................................................................... 15

      2.1.2   Penalties Business Days (PBD).......................................................................................... 16

      2.1.3   Daily calculations ............................................................................................................... 16

     2.1.4   Daily Reporting .................................................................................................................. 17

      2.1.5  Monthly Events .................................................................................................................. 18

     2.1.6  Monthly Appeal Period ..................................................................................................... 19

      2.1.7  Monthly aggregated amounts ......................................................................................... 20

     2.1.8  Monthly payment (collection & redistribution) .............................................................. 20

   2.2    Cross-CSD settlement fails (for CSD direct links to other CSDs) ......................................... 21

      2.2.1   Business Days calendars ................................................................................................... 21

     2.2.2   Penalties Business Days (PBD).......................................................................................... 22

     2.2.3   Daily calculations ............................................................................................................... 22

     2.2.4   Daily Reporting .................................................................................................................. 22

     2.2.5  Monthly Events .................................................................................................................. 23

     2.2.6  Monthly Appeal Period .................................................................................................... 24

     2.2.7  Monthly aggregated amounts .......................................................................................... 25

     2.2.8  Monthly payment (collection and redistribution) ........................................................... 25

3    Penalties Scope ............................................................................................................................ 26

   3.1     Instructions subject to cash penalties – General Scope ..................................................... 26

  3.2    Instructions subject to cash penalties - Cross-CSD Settlement Scope ............................... 27

  3.3    Instruments subject to penalties .......................................................................................... 27

4    Identification of the party to be penalised ................................................................................. 29

   4.1    Late Matching Fail Penalty (LMFP) ...................................................................................... 29

      4.1.1  LMFP special case: ‘already matched’ instructions ........................................................ 29

  4.2    Settlement fail penalty (SEFP) ............................................................................................. 30

5   Reference data required for penalty calculations ....................................................................... 31

   5.1     List of instruments subject to penalties ............................................................................... 31

                                                                                                                                                    1 | P a g e

## PDF page 3
  5.2    Daily reference price ............................................................................................................. 31

  5.3    Instrument type .................................................................................................................... 36

  5.4    Instrument liquidity/ illiquidity classification ...................................................................... 36

  5.5    Instrument trading segment ‘SME Growth Market’ - Place of Trading information ........ 38

  5.6    Instrument category penalty rate ....................................................................................... 40

  5.7    Central Bank Discount rate (penalties due to lack of cash) ................................................ 41

  5.8    Foreign Exchange Rates (FX) ............................................................................................... 42

6   Penalties Currencies Conversions Needs .................................................................................... 43

7    Calculation methods of the cash penalties ................................................................................. 45

   7.1    Settlement fail penalty (SEFP) ............................................................................................. 46

      7.1.1      Illustrative penalties calculation examples ................................................................. 48

   7.2    Late matching fail penalty (LMFP) ...................................................................................... 50

      7.2.1  Number of days considered in the computation of LMFP ............................................. 50

     7.2.2  Formulas to be used .......................................................................................................... 51

  7.3    Daily bilateral net per counterparty .................................................................................... 53

  7.4   Monthly cash penalties aggregation and global net amounts .......................................... 53

     7.4.1  Monthly bilateral net per counterparty .......................................................................... 53

     7.4.2  Global Net (monthly amount to be paid or to be received) .......................................... 54

8   Changes to previously calculated penalties ................................................................................ 56

   8.1   Removal of existing penalties ............................................................................................. 56

  8.2    Re-inclusion of a previously removed penalty .....................................................................57

  8.3    Re-allocation of an existing penalty .....................................................................................57

  8.4   Update of existing penalties ................................................................................................ 58

9   Cross-CSD settlement fails ........................................................................................................... 59

   9.1    Background ........................................................................................................................... 59

  9.2    Scenario 1A ............................................................................................................................ 60

  9.3    Scenario 1B ............................................................................................................................. 61

  9.4    Scenario 1C ............................................................................................................................ 62

  9.5    Scenario 2A ........................................................................................................................... 62

  9.6    Scenario 2B ........................................................................................................................... 63

  9.7    Scenario 2C ........................................................................................................................... 64

  9.8    Scenario 2D ........................................................................................................................... 64





DRAFT V7.0 – Publicly available to relevant stakeholders                                                              2 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 4
  9.9    Scenario 2E ............................................................................................................................ 65

  9.10   Scenario 2F ............................................................................................................................ 66

   9.11   Scenario 2X ........................................................................................................................... 66

  9.12   Scenario Bridge .................................................................................................................... 67

10   Collection & Redistribution of Penalties (Payment)................................................................... 68

   10.1   General overview.................................................................................................................. 68

      10.1.1    T2S-In CSDs payments processing ............................................................................... 69

  10.2   Step 1: Penalties Collection From CSD Participants ............................................................. 71

     10.2.1   Payment via direct debits and/ or cash transfers ........................................................ 72

     10.2.2   Payment via PFOD transactions ...................................................................................73

     10.2.3   Payment via a payment bank ........................................................................................73

  10.3   Step 2: Penalties Redistribution From Penalties Receiving CSD To Its Participants ..........73

     10.3.1    Cash transfers ................................................................................................................73

     10.3.2   Payment via PFOD transactions .................................................................................. 74

     10.3.3   Payment via a payment bank ....................................................................................... 74

11   Reporting .......................................................................................................................................75

   11.1    Reporting formats .................................................................................................................75

      11.1.1  ISO20022 messages .......................................................................................................... 76

      11.1.2    ISO15022 messages ...................................................................................................... 76

      11.1.3     Alternative reporting solutions .................................................................................... 77

   11.2   Generic Reporting content .................................................................................................. 78

      11.2.1    Information blocks for penalty reporting ................................................................... 78

      11.2.2    Mandatory fields .......................................................................................................... 79

   11.3   Message types ...................................................................................................................... 79

      11.3.1     Daily penalties report ................................................................................................... 80

      11.3.2    Monthly aggregated report ......................................................................................... 80

     11.3.3   Payment pre-advices ..................................................................................................... 81

12   Miscellaneous ............................................................................................................................... 82

   12.1    Penalties Activation process ................................................................................................ 82

   12.2   Exceptions Handling............................................................................................................. 82

      12.2.1    Delayed delivery of CSD penalties reports .................................................................. 82

     12.2.2    Exceptional situations where the cash penalties should not be applied .................. 82





DRAFT V7.0 – Publicly available to relevant stakeholders                                                          3 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 5
Annexes ................................................................................................................................................ 85

  Annex I- T2S documents .................................................................................................................. 85

  Annex II - Other documents and references ................................................................................... 85

  Annex III - Settlement Penalties Scenarios (excluding scenario 2X) ............................................. 86

  Annex IV – Penalties amounts reporting – Illustrative examples .................................................. 87

  Annex V – ECSDA Penalties Reference Data Rules & Recommendations .................................... 100





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      4 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 6
GLOSSARY


  Acronym or   Description
  abbreviation

  BD            Business day(s); see also ‘PBD’ (Penalties Business Day)

                 Settlement: Business days are those days on which an instruction can settle
                    in the CSD (and in the relevant payment system in case of settlement versus
                payment); such ‘opening days’ are excluding, for instance, week-ends.

                Note: regarding Penalties reference data, the publication of the ESMA
                databases used for penalties reference date, BDs can influence the eligibility
                  for the penalties period of a security (see Framework Annex V, Rules RE16
                  ‘Rule for the validity of reports published on days that are not business days’,
               RE18 ‘Rule for processing ESMA DB validity dates when setting up penalties´
                       eligibility’ and RE20 ‘Rule for assessing the Availability date of FITRS/Equities
                        files’).

  CA          Competent Authority(ies); relevant supervisor(s)/ regulator(s) of the CSD

   Calculating-   CSD subject to CSDR where the actual settlement (fail) is taking place; the
  CSD           Calculating-CSD will calculate, report and collect/ distribute penalties to its
                  participants (that may as well be CSDs); also in cross-CSD settlement fails
                 scenarios involving direct links, to avoid duplication of penalties calculation
              and reconciliation issues between linked CSDs, penalties shall exclusively be
                  calculated by the Calculating-CSD.

              Note for T2S: regardless of the (Investor- or Issuer-) CSD role for the financial
                instruments of the transactions subject to penalties in T2S and due to the
               absence of a ‘Calculating CSD’, it is the T2S platform that centrally calculates
              and reports to each T2S CSD (and counterparty CSD in case of cross-CSD fails)
                the penalties involving its and the counterparty CSDs´ participants. For T2S
                cross-CSD penalties the collection & redistribution is performed separately
                  for each ‘pair’ of involved T2S CSDs (i.e. the penalties amounts for fails
              between CSD A and CSD B are not commingled with the fails between CSD A
              and CSD C).

  CCP           Central Counterparty

  CSD           Central Securities Depository

  CSDR         Regulation (EU) no 909/2014 of the European Parliament and of the Council
                 of 23 July 2014 on improving securities settlement in the European Union and
              on central securities depositories and amending Directives 98/26/EC and
                2014/65/EU and Regulation (EU) No 236/2012 (‘EU CSD-Regulation’). Note





DRAFT V7.0 – Publicly available to relevant stakeholders                                                          5 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 7
  Acronym or   Description
  abbreviation

                 that CSDR applies to both, CSDs and International Central Securities
                 Depositories (ICSDs, i.e. Clearstream Banking Luxembourg or Euroclear
                 Bank).

               See https://eur-lex.europa.eu/legal-
                content/EN/TXT/?uri=CELEX%3A32014R0909.

                For the full package of related texts including standards and guidelines, see
                 https://www.esma.europa.eu/regulation/post-trading/settlement.

  DR         EU Delegated Regulation. In the Framework, and unless specified otherwise,
            DR relates to penalty reference prices and applicable rates. See http://eur-
                  lex.europa.eu/eli/reg_del/2017/389/oj

  ECB          European Central Bank

  ESMA        European Securities and Markets Authority

  Global Net    Represents the penalties ‘net’ (i.e. the gross amount to be received minus
  Amount       the gross amount to be paid) cash amount to be paid or to be received by
  (GNA)        each party for each currency and ‘actual place of settlement’ (CSD-link or
                settlement platform).

                  Different scenarios apply:

                                    -   Intra-CSD penalties: the CSD corresponds to the ‘actual place of
                        settlement’ and calculates a sole global net amount for each
                          participant and currency.

                                    -   Cross-CSD penalties – T2S:

                       For the T2S settlement platform being the ‘actual place of
                         settlement’, one global net amount is calculated per party, currency,
                     and every counterparty CSD (i.e. separate global net amounts for
                      each cross-CSD penalties payment).

                                    -   Cross-CSD penalties – non-T2S:

                     The Calculating-CSD being the ‘actual place of settlement’ calculates
                      a sole global net amount per participant (including Investor-CSDs)
                     and currency, i.e. the same approach as for ‘Intra-CSD penalties’
                           applies. Therefore, in the case of an Investor -CSD with bilateral links
                        to e.g. two Issuer-CSDs, each Issuer-CSD calculates a separate global
                       net amount towards the CSD participating in its system (i.e. the
                         Investor-CSD). As a result, the Investor-CSD may report and process
                       separate global net amounts per CSD-link towards its participants.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                    6 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 8
  Acronym or   Description
  abbreviation

  ISD           Intended Settlement Date date on which the settlement instruction shall
                   settle (same meaning as ‘Requested Settlement Date (RSD)’).

  LMFP         Late matching Fail Penalty; penalty that applies due to the matching taking
                 place after the ISD. See also ‘SEFP’.

  MiFID II/      Markets in Financial Instrument Directive II; Directive 2014/65/EU of the
  MiFIR        European Parliament and of the Council of 15 May 2014.

                   http://eur-lex.europa.eu/legal-
                content/EN/TXT/PDF/?uri=CELEX:32014L0065&from=EN

               Markets in Financial Instrument Regulation; Regulation (EU) No 600/2014 of
                the European Parliament and of the Council of 15 May 2014.

                   http://eur-lex.europa.eu/legal-
                content/EN/TXT/PDF/?uri=CELEX:32014R0600&from=en

   Partial         Redistribution of cash penalties by a CSD to receiving participants or CSDs
  redistribution  even when not all dues have been fully collected by the paying CSD on the
                     18th Penalties Business Day (PBD).

                    ‘Partial redistribution’ may be applied, e.g. to limit cash balances on a CSD´s
            own penalties cash account (including to comply with local regulations) or
                exception handling situations. Pre-condition is that the full amount expected
                to be received by a single CSD or CSD participant can be paid (i.e. no ‘partial
               payments’ apply; see also ‘Partial payment’).

   Partial       Payment of only a portion of the full amount expected to be received by a
  payment       single CSD or CSD participant; ‘partial payments’ shall not be applied for any
                  penalties payments unless required in exception handling (e.g. insolvency)
                   situations.

               See also ‘Partial redistribution’.

  Party
            A ‘party’ may be defined by a CSD either by:

                              - BIC (approach applied by the T2S platform, i.e. T2S CSDs will use the ‘T2S
                 Party BIC’ to define the ‘party’,  i.e. the ‘party  1’ from an ISO standard
                  perspective); or

                              - CSD participant securities account number; or

                              - LEI.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                            7 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 9
  Acronym or   Description
  abbreviation

              The CSD-role under national law and domestic market models or settlement
                 platforms (e.g. T2S) have to be considered as well in this respect. Hence, the
               usage of harmonised definitions across all CSDs is not achievable.

  PBD
                   ‘Penalties Business Day’; to be used for the penalties-specific monthly
                  reporting, appeals, and payment processing by a CSD.

            A “PBD” is any day of the year except for 01st January and 25th December and
                 Saturdays, Sundays.

              The term was introduced in the Framework in March 2020 at the request of
             CSD customers in order to ensure a consistent counting of days across CSDs
              and to limit differences in the penalties lifecycle across multiple CSDs.

               However,  it is not achievable that all CSDs apply the PBD concept in all
                 occasions, especially when the CSD settlement or central bank payment
               system is closed on a PBD. Therefore, if possible, the appeal deadlines and
               monthly reporting dates may be preponed to the previous BD while the
              payment date would be postponed to the next possible BD.1

  RTS           Regulatory Technical Standard, which is endorsed by the European
               Commission by means of a delegated act supplementing an EU Regulation or
               a Directive

  SDR        CSDR Settlement Discipline Regime; amongst others, prescribing CSD
                settlement functionalities, measures to prevent settlement fails (incl.
                  penalties, mandatory buy-ins and sanctions to participants), and reporting to
              be provided. The standards describing the regime in detail can be found here:

                   https://eur-lex.europa.eu/legal-
                 content/EN/TXT/?uri=uriserv:OJ.L_.2018.230.01.0001.01.ENG&toc=OJ:L:2018:2
               30:TOC

  SEFP          Settlement Fail Penalty; penalty that applies due to the non-settlement of a
              matched transaction on or after its ISD

  SFD        EU Settlement Finality Directive; Directive 98/26/EC of the European
                 Parliament and of the Council of 19 May 1998 on settlement finality in
              payment and securities settlement systems





1 Assessmemt on ECSDA level is ongoing with regard to the reporting timing aspect.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                   8 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 10
  Acronym or   Description
  abbreviation

                    http://eur-
                 lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:1998:166:0045:0050:EN:PDF

  SMPG        SWIFT Securities Market Practice Group

  SSR           Short Selling Regulation; Regulation (EU) No 236/2012 of the European
                 Parliament and of the Council of 14 March 2012

                   http://eur-lex.europa.eu/legal-
                content/EN/TXT/PDF/?uri=CELEX:32012R0236&from=EN

  T2S           Target 2 Securities; European Central Bank (ECB) centralised settlement
                platform

  T2S CSDR TF   Task Force composed of representatives from ECB, Central Banks, CSDs,
             ECSDA and the Banking community to discuss requirements towards and
                  solutions of T2S related to CSDR





DRAFT V7.0 – Publicly available to relevant stakeholders                                                    9 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 11
INTRODUCTION


On 23 July 2014, the European Parliament and the Council have issued Regulation (EU) No 909/2014
(later, CSDR2) aiming at the harmonisation of the regulatory environment of securities settlement
and Central Securities Depositories in the European Union.

On 13 September 2018, the European Commission officially published Delegated Regulation (DR)
2018/1229, supplementing Regulation (EU) No 909/2014 of the European Parliament and of the
Council with regard to regulatory technical standards (RTS) on the Settlement Discipline Regime
(later, SDR)3.

The introduction to the DR states:

“One of the main objectives of the Regulation is to improve the safety and efficiency of securities
settlement, in particular for cross-border transactions, by ensuring that buyers and sellers receive their
securities and money on time and without risks. To achieve this objective, the Regulation harmonises
the timing and framework for securities settlement in the Union. In particular, it provides for a set of
measures to prevent and address failures in the settlement of securities transactions (‘settlement
fails’), commonly referred to as settlement discipline measures.”

This ECSDA CSDR Settlement Fails Penalties Framework (later, ‘the Framework’) is the effort of
compliance with the Regulation and harmonisation of settlement penalties mechanisms across
CSDs subject to CSDR or regulation alike and constitutes a market practice for CSDs .4

The Framework solely focuses on the settlement fails penalties-related aspects of the CSDR
settlement discipline regime.

European CSDs also take into account the regulatory and contextual elements as described below
and having led the CSDs to develop the present Framework:

      (i.) The Framework recognises the importance of the provisions of CSDR Articles 6 & 7 (with
       regard to measures to prevent and to address settlement fails), as well as Delegated
       Regulation 2018/1229 detailing the Settlement Discipline Regime. The provisions aim at
        increasing settlement efficiency and harmonising settlement discipline measures across
       the Union through the following four key pillars:

           Pillar I.  Measures to prevent settlement fails:





2 Regulation (EU) No 909/2014 of the European Parliament and of the Council of 23 July 2014 on improving securities settlement in the
European Union and on central securities depositories and amending Directive 98/26/EC and 2014/65/EU and Regulation (EU) No
236/2012 (OJ L 257, 28.8.2014, p. 1). The Regulation and delegated acts can be found here:
https://www.esma.europa.eu/regulation/post-trading/settlement
3 Full text can be found here: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32018R1229
4 The CSDs involved in drafting of the Framework include members of ECSDA subject to the CSDR or aiming at compliance with
equivalent legislation, as well as NBB-SSS (the National Bank of Belgium Securities Settlement System) and BOGS (the Bank of Greece
Securities Settlement System).



DRAFT V7.0 – Publicly available to relevant stakeholders                                                             10 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 12
              ▪  Trade allocations and confirmations (obligation for Investment Firms, not
                  applicable to CSDs);

              ▪  Automation  of  CSDs´  settlement  processes  and  reporting  of  ‘manual
                   interventions’;

              ▪  Settlement instructions mandatory matching fields;

              ▪  CSDs´ settlement functionalities aiming at preventing settlement fails (e.g.
                    bilateral cancellation, hold & release, partial settlement) and possible derogation
               from the requirements to  offer  partial settlement and hold &  release
                   functionalities by CSDs under certain conditions.

          Pillar II.   Requirements to monitor and report settlement fails:

              ▪  CSDs are required to monitor and analyse settlement fails and CSD participants´
                 settlement efficiency, including setting up working groups to define measures
                 to improve efficiency;

              ▪  Settlement efficiency/ fails reporting to authorities, CCPs/ Trading Venues, and
                the public.

         Pillar III.   Requirements for CSDs to charge cash penalties to users that cause settlement
                       fails (the sole subject of this ECSDA Penalties Framework):

              ▪  For matched settlement instructions failing to settle on the Intended Settlement
               Date (ISD), daily calculation, (at least) monthly collection, distribution, and
                 reporting of penalties to CSD participants are required to be applied by CSDs
                  subject to CSDR or alike regulation.

         Pillar IV.   Rules requiring a mandatory buy-in5:

              ▪  Receiving trading parties and CCPs are required to initiate a mandatory buy-in
                   after a specific period after the ISD (the CSD role is limited to information
                 gathering and regulatory reporting).

      (ii.)  In May 2020, the EU Commission Delegated regulation 2020/12126 amended the date of
         entry into force of the CSDR SDR RTS to 01st February 20217. However, a further delay until
           01st February 2022 was adopted by another EU Commission delegated regulation issued
       on 23.10.20208.

      (iii.) Any  relevant  additional  clarification (once  officially  published) by the European
         Authorities will be taken into account in the Framework.





5 The entry into force of these rules has been delayed beyond 01st February 2022 to a date that is yet to be defined.
6 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32020R1212&from=EN
7 https://www.esma.europa.eu/press-news/esma-news/esma-proposes-amend-technical-standards-in-view-postponing-entry-force-csdr
8 https://ec.europa.eu/transparency/regdoc/rep/3/2020/EN/C-2020-7186-F1-EN-MAIN-PART-1.PDF



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                              11 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 13
     (iv.) Settlement penalties are applicable to CSD participants, including CSDs when these have
         established a CSD-link with a CSD applying CSDR SDR penalties.

     (v.)  The parameters and penalty rates for the calculation of cash penalties for settlement fails
        have been adopted and officially published in March 2017 (‘Cash Penalties Calculation
        Delegated Act’).

     (vi.) T2S CSDs and the Eurosystem (via the ‘T2S CDR Task Force’) jointly identified the
        necessary changes to the T2S platform and to facilitate T2S CSDs’ compliance with CSDR.

       As a result, the following documents were created (see Annexes I and II for details):

                  ▪  T2S penalty mechanism document and subsequent specifications in the
                    T2S Change Request 654;

                  ▪   Penalty lists – Messages overview (ISO20022 format, only; transposition
                       into ISO15022 messages is ongoing by SWIFT); and

                  ▪   List of clarifications sent to ESMA (note that an additional list of items
                       requiring clarifications has been submitted by ECSDA to ESMA).

         Please note that several penalties-related elements mentioned in this Framework have
       been explicitly excluded from the T2S CSDR Task Force discussions and the documents
         resulting from it, such as:

                                i.   Agreement on the list of financial instruments subject to penalties and
                     sourcing of a ‘golden data feed’ for the cash penalties calculation;
                                ii.    Collection and redistribution of cash penalties (i.e. the actual payment of
                    cash penalties); and
                               iii.   Reporting and messaging from CSDs to their participants and between
                    CSDs.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                                     12 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 14
1  ECSDA CSDR PENALTIES FRAMEWORK - KEY CONSIDERATIONS


1.  The ECSDA Framework (market practice) applies to all CSDs subject to the EU CSDR (text with
   EEA relevance) or alike regulation9. In case a CSD does not comply with the Framework in a
    specific aspect (due to e.g. legislative or operational boundaries), it should provide the relevant
    information to its participants accordingly.
2.  The Framework aims at ensuring that all CSDs implement the provisions in a harmonised way,
    neutral of whether settlement takes place in or outside of T2S, and neutral to the systems that
    are used by CSDs to process settlement fails penalties.
3.  The CSDR penalties mechanism will be set up by all CSDs subject to CSDR. If a CSD already
    applies a penalties regime, this was adapted to or replaced by the CSDR Settlement Discipline
   Regime requirements. Beyond CSDR, CSDs may additionally introduce or use supplementary
    tools (e.g. if required by a regulator or deemed reasonable by the CSD for its local market) in
    order to ensure high settlement efficiency.
4. ESMA and T2S documents served as the basis for creating this Framework. Large parts of the
   Framework are fully aligned and have been sourced from the discussions at the T2S CSDR Task
    Force as mentioned in the ‘T2S Penalty Mechanism’ document (version October 2017) and the
   subsequent T2S Change Request CR65410. For CSDs using the T2S settlement platform, in case
    of inconsistency between the ECSDA Framework and the relevant T2S documentation, the
    latter shall prevail. The Framework also covers penalties related aspects that are not subject to
    the T2S CSDR Task Force documents (when they are not covered by the T2S scope as noted in
    the Framework introduction11).
5.  This document may be subject to changes, e.g. due to various working assumptions taken due
    to pending ESMA feedback or ongoing discussions within ECSDA or the market community.
    Material changes compared to the previous  latest published Framework version are
    highlighted in light grey colour.
6.  The Framework is shared with other relevant stakeholders (i.e. CSD participants, ECB, Central
    Counterparties, ESMA, and other European Union and national authorities) with the aim of
    alignment and information sharing.
7.  According to CSDR and final ESMA RTS, the following principles must be applied by all EU CSDs:
       ▪  A CSD shall provide for a cash penalty mechanism for participants that caused
           settlement fails.
       ▪  Cash penalties are to be calculated on a daily basis for each business day that a matched
            (free of, with or against) payment settlement instruction fails to settle on or after its





9 A CSD may decide to subscribe to the Framework also in cases when it is based in an EU third-country jurisdiction and is subject to a
legislation declared equivalent to the CSDR or even ahead of the recognition of non-EU legislation equivalent to the CSDR by the
European Commission.
10 See ECB website for the latest version of the CR:
https://www.ecb.europa.eu/paym/target/t2s/governance/html/changerequests.en.html
11 In context of SDR RTS Art. 20, T2S CSDs signed a specific document, separate from the T2S Framework Agreement and ECSDA
Penalties Framework, to comply with the respective CSDR requirements described in this Article and the subsequent ESMA Q&A.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                                  13 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 15
          Intended Settlement Date (ISD), including those instructions that are ‘on hold’ or failing
         due to a lack of cash.
       ▪   Penalties shall also apply to instructions that matched in the securities settlement
          system after their ISD (‘late matching’, e.g. due to instruction entry after ISD).
       ▪  Cash penalties are calculated as from the ISD until the actual settlement or (bilateral)
            cancellation date of the instruction, considering12:
          −  Settlement Fail Penalty (SEFP): once the instruction is matched, penalties apply
                 earliest from the ISD or the matching date (when matching took place after ISD and
            no settlement occurred on the matching date) to the date of actual settlement or
               cancellation of the instruction, in addition to Late Matching Fail penalties, when
                applicable;
          −  Late Matching Fail Penalty (LMFP): penalties apply retroactively from the ISD until
              the actual matching date.
       ▪  As a general rule, penalty amounts shall be rounded up to maximum of two decimals.
       ▪   For settlement fails involving multiple CSDs (cross-CSD settlements), SDR penalties, if
            applicable, shall be calculated only by one CSD (the ‘Calculating-CSD’, i.e. the CSD where
           settlement is actually taking place based on the ‘actual place of settlement’ concept).
            This also means that an Investor-CSD being a participant in another CSD (e.g. Issuer
          CSD) shall comply with the Terms & Conditions of the latter CSD.
       ▪   Daily reports shall be provided to the CSD participants in order to allow them to
           reconcile and calculate the recharge of the penalty to their underlying clients where
            applicable.
       ▪  CSDs must redistribute the penalties only once they have been collected from their
            participants.
       ▪  The full amount collected as a penalty shall be redistributed to the participant that
           suffered from the fail at least on a monthly basis and latest until the end of the month
           following the fail date (fail month + 1).
       ▪   Instructions with a CCP as counterparty (see CSDR SDR RTS Article 19 amended on 11
          August 2023): for penalties calculated after 01st September 2024, CSDs shall apply
            Articles 16, 17 and 18, hence, CSDs must calculate, report and collect/ distribute any
           penalties for participants that are CCPs
       ▪  The cash penalties shall not be configured as a revenue source for the CSD13.





12 Note: Both, a late matching fail penalty (LMFP) and a settlement fail penalty (SEFP), can apply on a single instruction; they may be
charged to the delivering, receiving or both participants, depending on which of the two participants caused a) the late matching and
b) the settlement fail. However, LMFP and SEFP cannot both apply for the same business day: either LMFP or SEFP can occur, depending
on the matching timestamp (being before or after the CSD´s settlement cut-off time).
13 However, CSDs have the possibility to charge for the cost of development and maintenance of their penalty system as a fee separate
from the actual penalties amounts calculations and processing.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                14 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 16
2  PENALTIES LIFECYCLE AND BUSINESS DAYS CALENDAR


This section covers the penalties lifecycle for both, intra-CSD and cross-CSD settlement fails
scenarios:

A.  Daily events:
            i.    Daily Calculations
           ii.    Daily Reporting
B.  Monthly events:
            i.   Monthly Appeal Period
           ii.   Monthly Aggregated Amounts Provision
           iii.   Monthly Payment (Collection and Redistribution)

For the ‘Monthly Appeal Period’, ‘appeals’ refer to the exceptional correction or update of
previously calculated and reported penalties upon CSD or participant request (e.g. due to the
application of incorrect or updated reference data) and limited to the cases provided in the ESMA
CSDR Q&A.

Messaging and reporting aspects are covered in Chapter 11 of this document.


2.1  INTRA-CSD SETTLEMENT FAILS

Daily and monthly events apply for the business days defined below.

2.1.1   Business Days calendars

Applicable business days calendars:

    ▪  the CSD´s own settlement calendar14;

    ▪  the payment system calendar of the relevant currency.

Business days are those days on which an instruction can settle in the CSD (and in the relevant
payment system in case of settlement versus payment); such ‘‘opening days’’ are excluding, for
instance, week-ends.

Based on the above, a penalty shall not be applied:

    ▪   for ‘free of payment’ instructions: for the days when the CSD settlement system is closed.

    ▪   for ‘against payment’ instructions: for the days when the CSD settlement system and/ or
       the payment system of the relevant currency is closed (if the cash leg is to be settled in the
      payment system of the relevant currency).





14 Note: the calendars of the CSDs and the payment systems should be retained for at least three months for penalties calculation
purposes.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                   15 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 17
2.1.2   Penalties Business Days (PBD)

ECSDA Member CSDs agreed on common principles for a harmonised process in the definition and
counting of ‘‘business days’’ for the CSDR penalties management. For clarity, such specific
‘‘business days’’ are called ‘‘Penalties Business Days’’ (PBD). The PBDs may differ from the actual
‘‘business days’’ of a CSD’s settlement system or of a relevant payment system’s calendar (see
2.1.1).



2.1.3   Daily calculations

A CSD shall calculate daily penalties for each instruction that:

            i.    failed to settle on its intended settlement date (SEFP); or
           ii.   matched after its intended settlement date (LMFP15).

For the daily calculation (and reporting), the CSD’s own calendar is to be applied; if the CSD is closed
on a specific day, it will not calculate any penalties.

For the computation of the Settlement Fail Penalties (SEFP) as well as the Late Matching Fail
Penalties (LMFP), the (possibly different for FOP and DVP) CSD settlement cut-off times must be
considered.

Daily penalties calculations for every single failed settlement instruction shall be completed by the
CSD as soon as possible to make the daily reports available to its participants (including other
directly linked CSDs) in a timely manner, i.e. the penalties Calculating-CSDs shall report until midday
(12:00 p.m. Central European Time (CET)) while CSD´s depending on the reporting of a settlement
platform (like T2S) or Calculating-CSD shall provide their reports ideally until latest 14:00 p.m. CET
on the business day following the settlement fail. No ‘‘intraday’’ penalties calculation or reporting
applies.

Daily penalties can only be calculated by CSDs when all relevant reference data is known to them.
For instance, the daily reference price of the security will likely only be available to CSDs during the
following business day. As such, the penalties will be calculated and reported for instructions that
failed to settle on the previous business day (please also refer to the assumptions in Chapter 5.2).

For every failing settlement instruction, the CSD will calculate, for each party, the net penalties (i.e.
the single credit or debit net amount) per CSD, currency and counterparty on a daily basis.

Under exceptional circumstances (see ESMA CSDR Q&A ‘‘Settlement Discipline Questions 4 – Cash
penalties: scope’’), daily penalties previously calculated by the CSD or penalty engine (e.g. T2S) for
the current calendar month, could be amended (i.e. re-calculated due to changes in applicable





15 For the specific case of ‘partially successful buy-in’ related settlement instructions, please refer to Chapter 7.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                              16 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 18
reference data) or removed (i.e. cancelled) on any business day prior to the monthly report
generation(see Chapters 22.1.6/ 2.2.4 for details).

The penalties calculation methods are described in Chapter 7.



2.1.4   Daily Reporting

CSDs will send a daily penalty report to their participants when there are new, amended, removed
or re-included penalties during the day.

The penalty calculation period shall be one calendar month. For each business day, CSDs may
generate:

     i.    either a single report; or
    ii.   two separate reports: one for the new penalties and one for the amended, removed or re-
       included ones,  if applicable (e.g. such as described in the T2S penalty mechanism´s
       approach).

The ‘‘business days’’ used for penalties management may differ from the ‘‘actual business day’’ of
a CSD or payment system calendar. Hence, the term ‘‘Penalties Business Day’’ (PBD) was
introduced that applies to the below diagram.





CSDs shall report penalties for each ‘‘party’’ and aggregated per counterparty (i.e. a participant in
this same CSD).

In case when no penalty is to be applied (i.e. no failed transaction resulted in new penalties,
amendments, removals or re-inclusions) for one reporting day for a party, a ‘no activity’ report may
be sent16.

CSDs shall deliver the daily reports to their participants after the closing of the settlement day on
which (new or previous) penalties were calculated, amended, removed or re-included on the
following business day. Daily reports will be provided in line with the CSD´s settlement system





16 CSDs may offer such ‘no activity’ reports upon subscription, so that its participants are able to choose to receive these reports.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                    17 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 19
business days calendar and reporting schedule but shall be provided by Calculating-CSDs until 12:00
p.m. CET, latest (general note: penalties for fails on a Friday will be calculated and reported either
on Saturday, Sunday or Monday; in all cases, the business day date shall be the one of Monday).



2.1.5   Monthly Events

All CSDs shall follow the same principles to ensure that the appeal period and monthly penalty
reporting are finished prior to the 16th PBD.

The ‘business days’ used for penalties management may differ from the ‘actual business days’ of a
CSD or payment system calendar. Hence, the term ‘Penalties Business Day’ (PBD) was introduced
that applies to the below diagram, illustrating the timeline for the monthly reporting, assessment
and payment process:

Following MONTH (provision of aggregated amounts and payment)





 Daily reporting          End of appeal             th                                                   12 BD COB
 of penalties               period: 11 th BD     = Last day to 14th BD = Monthly         16th BD OPTIONAL          th
 computed for           = Last day to       input       aggregated amounts    =                     18 BD =
 last business             ask for          amendment for penalties of                          Payment
 day of previous           corrections on      s           previous month - -       Net amount to be
 month (i.e.                penalties from                     Bilateral net per         received OR paid
 First month)             previous                       CSD/currency / cpty      including cross-
                                                                 CSD penalties
                       month.                                            - Global net per CSD /                                                                              (Cash pre-advice)
                                                         currency (net amount
                                                         to be received OR paid
                                                       per CSD link)
                                              OPTIONAL





‘Payment pre-advices’ are usually not provided by CSDs as the monthly reports and/ or PFOD
instructions provide the necessary penalty amounts information. Therefore, ‘pre-advices’ are only
generically mentioned or described in this Framework.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                              18 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 20
2.1.6   Monthly Appeal Period

CSDs shall apply a dedicated appeal period for CSD participants to assess single settlement fails
penalty calculations, on an exceptional basis, within and maximum up to a defined point in time
post the end of a calendar month.

The appeal period shall generally end on the 10th PBD (included) of the following month. If a CSD is
closed on this date, the appeal period may close prior to the 10th PBD, so no appeal can be
processed after.

Reasons for appeals may be the situations listed in the ESMA CSDR Q&As ‘Settlement Discipline
Questions 4 – Cash penalties: scope’:

    ▪   ISIN suspension from trading17 or settlement (e.g. due to ‘undue creation or deletion of
        securities’ reconciliation issues);
    ▪  Settlement instructions involving cash settlement outside the securities settlement system
       operated by the CSD if, on the respective day, the relevant payment system is closed for
       settlement;
    ▪   Technical impossibilities at the CSD level that prevent settlement, such as a failure of the
        infrastructure components, a cyber-attack, and network problems.

In the absence of a single central source, the reference prices applied by CSDs may slightly deviate
for a single instrument that can be settled in multiple CSDs; such deviations do not represent a valid
reason for lodging ‘appeals’ towards the CSDs (see also Chapter 5.2).

Appeals can be lodged by CSD participants at any time during the calendar month, as from the
moment of computation and reporting of the penalty, and maximum until (and including) the 10th
PBD of the following month.

Each time that an appeal is accepted by a CSD, and a change is applied to a penalty, a “penalty
update” report will be provided. Updates made by the CSD or penalty engine (e.g. T2S) after the
10th PBD of the following month will be reported at the latest one day before the monthly report
generation. Penalties updates shall be provided by the Calculating-CSDs until midday (12:00 p.m.
CET), while CSD depending on the reporting of a settlement platform (like T2S) or a Calculating-CSD
shall provide their reports ideally until 14:00 p.m. CET.

In order to apply for an appeal, sufficient information needs to be provided by the CSD participant
to the CSD, covering at least:

    ▪  Reference of the penalty as well as the failed transaction details,
    ▪  Reason for the appeal; and
    ▪  Expected penalty amount and calculation details to be applied.





17 While this is stated in the ESMA Q&As, ESMA advised ECSDA this is not meant to be mandatory but a non-exhaustive example for
cases when CSD may not need to apply penalties. In this specific case, CSDs are usually not aware of the suspension taking place at
trading level, hence, will not waive any penalties that were calculated.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                               19 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 21
Appeals represent an exception handling by CSDs; until further notice, each CSD will design its
own processes considering e.g. its GTCs, communication requirements to submit an appeal and
providing the outcome of the appeal assessment to the appealing participant18.

2.1.7   Monthly aggregated amounts

At the latest on the 14th PBD of the following month, the CSD will report the monthly aggregated
amounts for the penalties of the previous month (i.e. the aggregated amounts of the penalties
computed for the business days of the previous month).

The 14th PBD is the last day when the monthly reporting shall be sent. If the CSD is closed on this
day, the monthly reporting may be sent prior to the 14th PBD.

For each party, per currency and counterparty, the CSD will sum up all the cash penalties that this
party can be expecting to be credited or debited with.

If the net result is a credit, the party can expect a cash payment from this counterparty. If the result
is a debit, the party will have to pay this counterparty.

Thus, the monthly reporting shall include, per currency and per party, all the net amounts against
each of its counterparties for the penalties computed for the business days of the previous month.

It is recommended that one ‘global net amount’ (the amount to be received minus the amount to
be paid) will be provided by the CSDs in the monthly report on the 14th PBD. Otherwise, PFODs shall
be generated by CSDs on the 16th PBD, but latest before the start of the 18th PBD, serving to timely
notify the ‘global net amount’ to be debited from/ credited to the CSD participants.

The monthly reports will include only a subset of the details of each gross penalty that are provided
in the daily reports.

For additional information, please refer to Chapter 7.4 ‘Monthly cash penalties aggregation and
global net amounts’.



2.1.8   Monthly payment (collection & redistribution)

On the 18th PBD of the following month, the CSD (and its participants) shall perform the payment
process, i.e. the CSD shall collect and redistribute the penalties amounts to/ from its participants.

If the CSD and/ or the payment system of the currency is closed on the 18th PBD, the payment shall
be done on the next possible business day.

For each party, the net amount (to be paid or to be received by a CSD participant) shall be reported
by the CSD at the latest on the 16th PBD thereby providing time to perform FX transactions (if
required) before the payment date (18th PBD).





18 Appeals can only be raised from parties/ participants that maintain a contractual relationship with the CSD.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                       20 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 22
Each CSD participant will have to pay (for each currency, if applicable) the exact amount as reported
by the CSD.

Depending on their set-up (having/ not having a banking license) and national specificities, CSDs
will use different models for the actual penalties’ payments processing; intra-CSD payment
processes may also differ from the cross-CSD payments.

The following possible payment models were identified:

    ▪  CSD triggers direct debits and/ or cash transfers;
    ▪  CSD generates PFOD instructions;
    ▪  Cash is transferred using a payment bank.

CSDs may define appropriate measures (to be described in the relevant contractual documents
with the CSD participants) to ensure CSD participants comply with their payment obligations to
the CSD on time on the 18th PBD to avoid delays and processing issues due to a lacking or
incomplete penalties collection by the CSD.

For detailed information about the monthly payment process, please refer to Chapter 10.


2.2  CROSS-CSD SETTLEMENT FAILS (FOR CSD DIRECT LINKS TO OTHER CSDS)

Daily and monthly events apply for the business days defined below.

2.2.1   Business Days calendars

Applicable business days calendars used for the penalties purposes can be the following:

    ▪   Calculating-CSD´s settlement penalties calendar19;

    ▪  Payment system’s calendar of the relevant currency.

Business days are those days on which an instruction can settle in the Calculating-CSD (and in the
relevant payment system in case of settlement versus payment); such ‘opening days’ exclude, for
instance, weekends.

Based on the above, a penalty shall not be applied:

    ▪   For the ‘free of payment’ instructions: for the days when the Calculating-CSD settlement
       system is closed;
    ▪   For the ‘against payment’’ instructions: for the days when the Calculating-CSD´s settlement
       system and/ or the payment system of the relevant currency is closed (if the cash leg is to
      be settled in the payment system of the relevant currency).





19 Note: The calendars of the CSDs and the payment systems should be retained for at least three months for penalties calculation
purposes.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                     21 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 23
2.2.2   Penalties Business Days (PBD)

The concept of ‘Penalties Business Days’, as described in Chapter 2.1.2, is used to achieve a
harmonised process across CSDs. This is of paramount importance in the management of the cross-
CSD settlement fails penalties processing.



2.2.3   Daily calculations

For the daily calculation (and reporting), the Calculating-CSD´s calendar is to be applied. If the
Calculating-CSD is closed on a specific day, it will not calculate any penalty.

The same process as the one mentioned in Chapter 2.1.1 shall apply when the CSD is acting as an
Issuer-CSD (for an Investor-CSD).

In line with the ‘actual place of settlement’ concept, if the CSD is acting as an Investor-CSD, it shall
wait for the daily amounts to be provided by the Calculating-CSD where settlement is actually
taking place and report them afterwards to its own participants.

To avoid procedural complexity and reconciliation issues, the Investor-CSD shall not make its own
penalty calculations but rely on the Calculating-CSD20.

The daily calculation performed by the Calculating-CSD considers the Investor-CSD as a standard
participant (in the other CSD´s books). It means that the Calculating-CSD cannot provide the daily
penalties at the level of the Investor-CSD´s participants.

The Calculating-CSD shall report the daily penalties to the Investor-CSD, as soon as possible and, at
the latest, until 12:00 p.m. CET on the business day following the settlement fail. This is done in
order for the Investor-CSD to report these cross-CSD penalties in a timely manner to its own
participants.



2.2.4   Daily Reporting

The same process as the one mentioned in Chapter 2.1.4 shall apply when the CSD is acting as
penalties Calculating-CSD (for an Investor-CSD).

CSDs shall send a daily penalty report to their CSD participants when there are new, amended,
removed, or re-included penalties.





20 If all involved CSDs are subject to CSDR, only the CSD where settlement is actually taking place shall calculate the penalties; all CSDs
involved will have to report and collect/ redistribute. Note for T2S external settlement, T2S will (until further notice) calculate in any
case. T2S CSDs will replace these penalties by the ones reported by the Calculating-CSD. Please refer to Chapter 9 ‘Cross-CSD
settlement fails‘ and Annex III for a description of all settlement scenarios.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                              22 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 24
The sending of the daily reporting will depend on the CSDs´ settlement system business days
calendars.

The daily reporting shall segregate the penalties resulting from the intra-CSD activity, and the ones
resulting from the cross-CSD activity. In such a case, the CSD participant might receive up to four
reports, for the same business day:

           1.  Report including all-new intra-CSD penalties;
         2.  Report including the penalties intra-CSD which were amended, removed or re-included
           (unless included in the ‘new penalties’ report);
         3.  Report including all-new cross-CSD penalties;
        4.  Report including the penalties cross-CSD which were amended, removed or re-included
           (unless included in the ‘new penalties’ report).

The Calculating-CSDs shall provide the daily reports until midday (12:00 p.m. CET), while the CSD
depending on the reporting of a settlement platform (like T2S) or of other Calculating-CSDs shall
provide their reports ideally until 14:00 p.m. CET. The receiving CSD will in turn report these
penalties to its participants. Thus, CSD participants should consider that cross-CSD penalties may
be reported later than intra-CSD penalties (depending on the time of receipt from the Calculating-
CSD).

The penalty information shall be passed on to the part of the failing settlement instruction, as it
appears in the Investor-CSD´s records.

In the case of a CSD link, the failing party may be a participant or an underlying client of a participant
of the relevant linked CSD. In the case of indirect and operated direct21 links, the information flow
is longer compared to a direct link, i.e. it could go from the CSD reporting the penalties to the
intermediary acting on behalf of the CSD to the customer of the intermediary (i.e. the CSD), and
then to the underlying CSD participant. How this information flow is technically ensured is subject
to specification by the involved CSDs.



2.2.5   Monthly Events

The monthly events, in a cross-CSD scenario, are identical to the ones in an Intra-CSD scenario for
the ‘First month’ (see Chapter 2.1.3).

A difference applies related to the end of the appeal period (as highlighted in red).

The ‘business days’ used for penalties management may differ from the ‘actual business days’ of a
CSD or payment system calendar. Hence, the term ‘Penalties Business Day’ (PBD) is introduced that
applies to the below diagram, illustrating the timeline for the monthly reporting, assessment and
payment process:





21 ‘Operated’ means the CSD has a direct link/ account with the other CSD that is operated by an agent.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                            23 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 25
                                                                               14th BD = Monthly
                                                         aggregated              16th BD
                                                     amounts for         OPTIONAL =
                                                                   penalties of
                                                              previous month - -     Net amount to
                                                                         Bilateral net per      be received OR
                                                            CSD/currency /         paid including
                                                              cpty                  cross-CSD
                                                                                          penalties (Cash
                                                               Global net per CSD     pre-advice)
                                                                                                          / currency (net
                                                   amount to be
                                                               received OR paid
                                                            per CSD link)
                                                  OPTIONAL

Note that ‘payment pre-advices’ are usually not provided by CSDs as the monthly reports and/ or
PFOD instructions provide the necessary penalty amounts information; therefore, ‘pre-advices’ are
only generically mentioned or described in this Framework.



2.2.6  Monthly Appeal Period

While the general process as described in Chapter 2.1.6 applies, in a cross-CSD context, the appeal
period ends at the close of business on the 11th PBD of the following month. It allows CSDs to still
pass on to other CSDs the appeals requested by CSD participants on the 10th PBD. At the close of
business on the 11th Penalties Business Day, CSDs shall no longer request appeals to other CSDs. In
case the 11th PBD is a CSD closing date, the appeal end date may be advanced to an earlier date. It
means that the end of the appeal period for participants (planned on the 10th PBD) may also be
moved to an earlier date.

An appeal requested, at the latest, until the 10th PBD by a CSD participant (in line with Chapter 2.1.5)
and accepted by a CSD, must be sent to the other CSD on the 11th PBD so that it can be considered
in the “penalty update” report and monthly report generation.

By close of business on the 12th PBD of the following month, any adjustment resulting from
appeals shall be completed by the CSD or penalty engine (e.g. T2S), to be reported on the 13th PBD
ideally, at the latest, until 14:00h p.m. CET.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                          24 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 26
Any Investor-CSD may request an appeal to the Issuer-CSD to remove penalties caused by
technical impossibilities at the CSD, as referred to in Chapters 2.1.6, and for any reason deemed
justified by the Investor-CSD. The Investor-CSD will lodge an appeal including its reasoning at the
Issuer-CSD during the applicable appeal period. The Issuer-CSD will process the appeal as received
from the Investor-CSD and remove the penalty applied by the Issuer-CSD.



2.2.7   Monthly aggregated amounts

The general process will be identical to the one described for Intra-CSD settlement fails (see
Chapter 2.1.7). The 14th PBD is the last day when the monthly reporting shall be sent. If the
Calculating-CSD or the calculating settlement platform is closed on this day, the monthly reporting
may be sent prior to the 14th PBD.

It is recommended that one ‘global net amount’ be provided by the Calculating-CSD in the monthly
report on the 14th PBD. Alternatively or in addition, PFODs shall be generated by CSDs on the 16th
PBD but, at the latest, before the start of the 18th PBD, serving to timely notify the ‘global net
amount’ to be debited from/ credited to the parties/ CSD participants.

For additional information, please refer to Chapter 7.4 ‘Monthly cash penalties aggregation and
global net amounts’.

2.2.8  Monthly payment (collection and redistribution)

In a cross-CSD scenario, the process will slightly differ compared to 2.1.8, as CSDs are not
themselves responsible for supplying the funds to proceed with the penalties payment.

On the 18th PBD of the month, all involved CSDs shall have collected the amounts due by their
participants (including those that are CSDs themselves), in order to be able to start the payment
process across CSDs.

If the CSD and/ or the payment system of the currency is closed on the 18th PBD the payment will
have to be done on the next possible business day.

Each CSD participant and CSD will have to pay (for each currency, if applicable) the exact amount
as reported by the other CSD.

CSDs may define appropriate measures (to be described in the relevant contractual documents
with the CSD participants) to ensure CSD participants comply with their payment obligations (in
each currency reported) to the CSD on time on the 18th PBD to avoid delays and processing issues
due to a lacking or incomplete penalties collection.

For detailed information about the monthly payment process, please refer to Chapter 10.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                            25 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 27
3  PENALTIES SCOPE


Several aspects (mainly content and technical) related to the usage of the ESMA databases
mentioned in this section are currently discussed amongst CSDs and are subject to ESMA
clarification. Hence, the Framework may be adapted at a later stage.

3.1  INSTRUCTIONS SUBJECT TO CASH PENALTIES – GENERAL SCOPE

Settlement fails penalties shall be calculated for all settlement instructions, free of, against or with
payment, that are:

    ▪  matched (prior, on or after their Intended Settlement Date (ISD)), and
    ▪   failing to settle on and after their ISD.

WORKING ASSUMPTION (ESMA/EC to confirm): The only exemptions are:

                   i.   Settlement transactions that do not represent ‘transfer orders22 according to the
             second indent of point (i) of Article 2 of Directive 98/26/EC [Settlement Finality
                 Directive];
                   ii.   Corporate actions on stock (ISO transaction code equals ‘CORP’);
                  iii.    Technical instructions, e.g. T2S automatic realignments;
             iv.   T2S Settlement restrictions23.

Note:

    ▪   (T2S) Auto-collateralisation operations, though automatically generated, are considered in
       scope.
    ▪  OPEN ITEM (ESMA/EC to clarify): Primary issuance settlements are in scope (except the
       process of the initial creation of securities which cannot be regarded as a ‘transfer order’
      from a legal standpoint24).
    ▪  OPEN ITEM (ESMA/EC  to  clarify):  treatment  of  Investment  Funds  redemptions/
        subscriptions order routing instructions (CSD model vs. TA model/ transfer order vs.
       settlement instructions model).





22 Definition: ‘Any instruction by a participant to place at the disposal of a recipient an amount of money by means of a book entry on the
accounts of a credit institution, a central bank, a central counterparty or a settlement agent, or any instruction which results in the
assumption or discharge of a payment obligation as defined by the rules of the system, or an instruction by a participant to transfer the
title to, or interest in, a security or securities by means of a book entry on a register, or otherwise.’
23 A T2S Settlement restriction is an Intra-position movement. It is used to manage restriction on a securities position which can be: a
securities blocking; a securities reservation; or a securities earmarking.
24 T2S CSDR TF wording; note re. Investment funds issuance (creation/ redemption), based on ECB feedback: unlike for corporate
actions where the Issuers are paying CSD participants, there is generally no obligation on the side of participants, for Issuance and
Fund Investment the counterparties are CSD participants who are buyers, so these shall be considered as normal transactions, subject
to penalties.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                        26 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 28
3.2  INSTRUCTIONS SUBJECT TO CASH PENALTIES - CROSS-CSD SETTLEMENT SCOPE

In the context of settlement transactions beyond the CSD´s own system, various scenarios were
elaborated by T2S CSDR Task Force and ECSDA and shared with ESMA. These must be considered
by CSDs to define if a failing instruction is actually subject to penalties; please refer to Chapter 9 for
details.

In summary, an ‘actual place of settlement’ concept applies:

    ▪  when the actual settlement is taking place in a CSD subject to CSDR, penalties shall be
        calculated and applied by this CSD (‘Calculating-CSD’); the (Investor-) CSD being a
        participant of the other CSD is obliged to report the penalties further to its own participants
      and also perform the cash collection and redistribution process;
    ▪  when the actual settlement is taking place in a third country CSD (not subject to CSDR), no
       (CSDR) penalties shall apply.

Notes regarding T2S:

             a.  T2S always calculates and reports the penalties, even if T2S is not the actual place
               of settlement; hence, it is up to the T2S CSDs to remove these penalties and replace
            them by the ones reported by the Calculating-CSD (i.e. the ‘external CSD’ in T2S
               terms);
            b. when settlement takes place between two Investor-CSDs, the subsequent
              realignment transactions on Issuer-CSD level shall not be subject to settlement fails
                penalties, independent  if the Issuer-CSD  is inside or outside T2S (see ‘T2S
               realignment’ exemption stated in Chapter 3.1).


3.3  INSTRUMENTS SUBJECT TO PENALTIES

Settlement fails penalties must be calculated in case a matched settlement instruction in scope of
SDR is failing to settle and the instruments to be transferred are25:

   ▪    CSD-eligible MiFID II/ MiFIR financial instruments:
       ▪  admitted to trading or traded on an EU trading venue (see ESMA FIRDS databases26);
           or
       ▪   cleared (or eligible for clearing) by an EU CCP.





25 See also ESMA Q&A 4 on Settlement Discipline (https://www.esma.europa.eu/sites/default/files/library/esma70-708036281-
2_csdr_qas.pdf)
26 https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_firds Note: ‘’‘‘As the FIRDS database also
contains instruments that are not CSD-eligible (like derivatives), CSDs should limit the query to instruments being eligible in their CSD
settlement system.
Please consider the ECSDA Penalties Reference Data Rules & Recommendations in Annex V.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                             27 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 29
   ▪   excluding shares when their principal trading venue is located in a third country27.

Note: the relevant MiFID II/ MiFIR financial instruments types are:

   ▪   transferable securities [i.e. equity- and bond- (like) instruments (including ETFs) and giving
       a right to buy or sell any of those],

   ▪  money-market instruments,

   ▪   UCITS, and

   ▪   emission allowances.

I.e. to derive the concrete list of ISINs subject to SDR, a CSD shall:

    a)  use the ESMA FIRDS database for MIFID II/ MiFIR instruments;
    b)  identify the ISINs eligible for settlement in the CSD; and
    c)  eliminate those shares that are exempted from the Short Selling Regulation.

Please also refer to Chapter 5 for the reference data required to calculate penalties and consider
the ECSDA Reference Data Rules & Recommendations in Annex V.





27 CSDR Art. 7.13 states: ‘This [CSDR] Article [7] shall not apply where the principal venue for the trading of shares is located in a third
country. The location of the principal venue for the trading of shares shall be determined in accordance with Article 16 of Regulation (EU)
No 236/2012.’. See ‘Short Selling Regulation (SSR)’ exempted instrument list:
https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_mifid_shsexs




DRAFT V7.0 – Publicly available to relevant stakeholders                                                        28 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 30
4  IDENTIFICATION OF THE PARTY TO BE PENALISED


4.1  LATE MATCHING FAIL PENALTY (LMFP)

Any settlement instruction being in scope of the penalties calculation that is matched after the
relevant CSD settlement cut-off time of its ISD will be subject to computation of Late Matching
Fail Penalties (LMFP) retroactively for each past business day that it failed to settle.

The penalty is charged to the participant who was last to enter or modify the relevant settlement
instruction (e.g. ‘accepted timestamp’ is later than the one of the counterparty´s instruction) for
the periods between the ISD and the day of matching of the instruction; when both parties send
their instructions ‘late’ after the ISD, only one of the two counterparts of a transaction will be
imposed with a LMFP.

Please also refer to Chapter 7 regarding the special handling in case of only partially successful buy-
ins.

4.1.1   LMFP special case: ‘already matched’ instructions

If a CSD is offering the possibility to send settlement instructions as ‘already matched’ (i.e. both
instructions are sent at the same time as matched; often used for CCP instructions), these
settlement instructions will be subject to the computation of LMFPs in case they are sent after the
ISD.

In such cases, it is not always possible for the CSD (and never possible for the T2S settlement
platform) to determine the real failing party by comparing the accepted timestamps (as both legs
have the same timestamp).

In such cases, the penalty will be applied to the instructing party of the two settlement instructions
(i.e. the party who sent the instructions to the CSD).

When the instructing party is one of the counterparties of the failed settlement transaction, it will
be up to the instructing party (e.g. CCP) to inform the CSD to whom to allocate the penalty (i.e. the
delivering or the receiving participant) and enable the CSD to adjust the penalty assignment
accordingly28.

When the instructing party is a third party, the penalty might not be applicable to the instructing
party of the two settlement instructions as this instructing party does not have an account in the
CSD´s books (e.g. electronic trading platforms/ Trading Venues). In such a case, if there is no
request to re-allocate the penalty to one of the counterparties during the appeal period, the
delivering party might be the one to be penalised by default. It will be up to the delivering party,





28 Such a case will likely be very rare, as CCPs are normally sending their settlement instructions prior to the ISD.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                         29 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 31
in agreement with the receiving party, to request the CSD to perform a re-allocation of the
penalty to the receiving party if the receiving party was the real defaulting party.

Note: the penalised party may claim its dues outside the CSD penalty mechanism if the real failing
party does not have a securities account in the CSD´s books or is no party in the settlement
transaction (when, for instance, a Trading Venue is the real failing party, the penalty will be charged
to the delivering party by default; the delivering party may pass on its penalty bilaterally to the
Trading Venue).


4.2  SETTLEMENT FAIL PENALTY (SEFP)

Any settlement instruction being in scope of the penalties’ calculation that

     i.          is matched before the relevant cut-off of a given business day; and
    ii.       has reached its ISD; and
   iii.         fails to settle on that ISD or the day it is matched (late, i.e. after ISD) and after the ISD,

shall be subject to the computation of Settlement Fail Penalties (SEFP) for each business day the
instruction is failing to settle. A settlement instruction that  ‘fails to settle on ISD’ must be
understood as a settlement instruction that is not cancelled and remaining to be settled, fully or
partially, by the time of the end of settlement processing of the relevant CSD (settlement cut-off
time).

The relevant cut-off is the key point in time to take a ‘snapshot’ of the status and fail reason of a
settlement instruction and determine its eligibility for penalty application. A penalty shall be
imposed to a CSD participant if its settlement instruction fulfills, at the time of the end of processing
of the relevant settlement cut-off, any of the below conditions:

    ▪  the instruction is ‘on hold’ (note: when ‘on hold’ is identified for one instruction, no
        additional check for a ‘lack of cash’ or ‘lack of securities’ of the counterparty instruction
         shall be made by the CSD); or
    ▪  the instruction failed the settlement eligibility or provision check, i.e. the fail reason
       associated with this instruction is ‘lack of securities’ or ‘lack of cash’ (note: when ‘lack of
        securities’ is identified no additional fail check for a ‘lack of cash’ of the counterparty
        instruction shall be made by the CSD).

Note: Settlement Fails Penalties (SEFP) apply in addition to LMFP as described in Chapter 4.1.
when the ‘matched-late’ instruction is not actually settled before the CSD settlement cut-off time
of the matching business day.

It is possible that the two counterparts of a transaction are imposed with a SEFP, for example, when
both legs of a matched instruction are ‘on hold’ until the CSD settlement processing cut-off time.
In such a scenario, both parties will be imposed with a SEFP (i.e. the delivering party will be charged
with ‘lack of securities’ penalties and the receiving party with ‘lack of cash’ penalties).





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      30 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 32
5  REFERENCE DATA REQUIRED FOR PENALTY CALCULATIONS


In order to calculate the daily settlement fails penalties, the information described in this section
needs to be available to or sourced by CSDs.

When reference data (e.g. CFI code, security reference price) required to calculate penalties is
missing by the calculation date, penalty amounts shall be set to ‘zero’ until the data becomes
available unless the latest available reference data can be applied by the CSD until it is updated.

The latest point in time for consideration of new (or updated) reference data by the CSD is prior to
the monthly reporting. That means if new or updated data for calculating penalties are available
to the CSD or penalty engine (e.g. T2S) only after the monthly report is generated, no retroactive
penalties calculations or adaptations can be made by CSDs or the penalty engine.

Please refer to Chapter 8 related to updated reference data leading to changes in previously
calculated penalties.

In addition, the information contained in Annex V ‘ECSDA Penalties Reference Data Rules &
Recommendations’ of this Framework should be considered.


5.1   LIST OF INSTRUMENTS SUBJECT TO PENALTIES
For the identification of instruments in scope, please refer to Chapter 3.3.

In short, using ESMA publicly available information, the CSD-eligible ISINs listed in the MiFID II/
MiFIR ‘FIRDS’ databases to be diminished by those shares exempted from the EU Short Selling
Regulation (SSR) will be considered for the penalties application.


5.2  DAILY REFERENCE PRICE

CSDs need to source (or derive) and apply a reference price for each day when the settlement
instructions fail to settle. The prices applied shall be in line with CSDR price determination rules29
for the securities in the scope of the CSDR penalty regime and eligible for settlement in the CSD
and considering information in the ESMA FIRDS and FITRS databases:

                   i.    for shares and similar instruments: apply the closing price of the ‘most relevant
              market’ (MRM) in terms of liquidity (the MRM information – but no price data - is
                available in the ESMA FITRS database);

                   ii.    for other instruments: apply the closing price of the ‘most relevant market’ (MRM)
                 in terms of ‘highest turnover’ (trading venue to be derived from the ESMA FIRDS





29 See Article 7 of the Delegated Regulation: http://eur-lex.europa.eu/eli/reg_del/2017/389/oj



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                   31 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 33
              database) whereby the MRM is assessed according to rule RE17- Rule for the
                definition of the ‘Most relevant market’ (MRM) by liquidity and highest turnover’ in
            Annex V30 (;

                  iii.   For instruments for which no updated daily MiFID II/ MiFIR price is available, use the
                 latest available price from a MiFID II/ MiFIR or other trading venue or - when no
               trading venue price is available at all - a price as determined by the CSD (see below).

                In case of lacking MiFID II/ MiFIR or trading venue price data, two situations should
            be considered as follows:

                  ▪  Where a market value can be derived, the CSD will apply a market price
                    determined by the CSD, according to the price determination method
                   approved by the CSD´s National Competent Authority31;

                  ▪  Where no market value is available at all, CSDs will use:

                            ▪   for debt instruments: nominal value (in the ISIN denomination
                                  currency);

                            ▪   for non-debt instruments: default price (e.g. issue price).

Considering the above, CSDs must source (usually via their data vendors) the applicable prices from
the individual MIFID II/ MiFIR trading venue relevant for a single instrument, identifying the relevant
trading venue by using the ESMA FITRS and FIRDS databases32:

    ▪   For shares and similar (covered in the ESMA FITRS database):

          –  the       relevant      information      can     be      found       here:
               https://www.esma.europa.eu/databases-library/registers-and-data

          –  use   file  ‘Financial  Instruments  Transparency  System  (FITRS)’  to  open:
               https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers
                  _fitrs_files





30 The new ESMA file published every three months for fixed income securities is under ECSDA review.
31 In such case, the reference prices applied by CSDs may deviate for a single (EU or non-EU) instrument that can be settled in multiple
CSDs. However, the impact would be limited to intra-CSD settlement fails (as for cross-CSD settlement fails, the ‘actual place of
settlement’ concept applies, see Chapter 9).

32 Please note that ESMA does not publish the trading prices.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                            32 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 34
    ▪   For other instruments than shares (covered in the ESMA FIRDS database):

          –  the       relevant      information      can     be      found       here:
               https://www.esma.europa.eu/databases-library/registers-and-data

          –  use file ‘Financial Instruments Reference Database (FIRDS)‘ to open:

        https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_firds





DRAFT V7.0 – Publicly available to relevant stakeholders                                                          33 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 35
Due to the huge size of the database (containing more than twelve million entries, including
derivatives), the data must be extracted and electronically checked for relevant updates on a daily
basis.

In the absence of a single central source, the reference prices applied by CSDs may slightly deviate
for a single instrument that can be settled in multiple CSDs. Such deviations do not represent a valid
reason for lodging ‘appeals’ towards the CSDs (see also Chapters 2.1.6, 2.2.6).

For all technical issues related to the ESMA databases, the ESMA Support Team can be reached at
support@esma.europa.eu.

The daily reference price used for calculating the fails penalties is the price of each business day
when the settlement instruction is subject to penalty calculation (i.e. using a maximum of three
months of historical prices when relevant, e.g. for late matching fails), independently from when
the calculation is performed.

That means that the reference price for the penalty calculation of each fail day shall be the one of
the relevant fail dates.



Example

An FOP instruction with Intended Settlement Date 05.10.18 only matches (but does not settle) on
07.10.18 – reference prices for 05.10., 06.10. (for LMFP calculation) and 07.10.18 (for SEFP




DRAFT V7.0 – Publicly available to relevant stakeholders                                                        34 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 36
calculation) are to be applied (assuming that these are business days and the CSD system was open
for settlement).

Therefore, CSDs are required to source and store market price data for all instruments in the scope
of the penalty regime on a daily basis33. In the absence of a single European price feed or source for
all CSDs, this has to be managed individually by CSDs via their data vendors, unless CSDs can source
price data themselves.

Reference price data shall not be reported or otherwise made available to parties other than the
responsible CSD or its penalties mechanism provider (i.e. the penalty messages as described in
Chapter 11 shall contain ‘NONREF’ or remain blank in the respective price fields).

The application of identical reference prices for the same ISIN by CSDs in a cross-CSD settlement
context is ensured by the process design as CSDs shall always use the penalties calculation as
provided to them from the Calculating-CSD where settlement is actually taking place (‘actual place
of settlement’ concept; see detailed scenarios in Chapter 9), i.e. the penalties as calculated and
reported by this CSD to its participants (that may as well be CSDs) shall always be applied as such
by the CSDs involved in the settlement chain.

The amount imposed by the penalty should be calculated:

    ▪   For against payment settlement fails, in the currency of the cash leg.

      Note that the ICSDs Euroclear Bank SA/ NV and Clearstream Banking Luxembourg S.A., in
        their role of the penalties Calculating-CSDs for their internal and Bridge settlement fails,
       use a single currency (EUR) for all their penalties calculations (related to both, free of and
       against payment settlement fails). The default currency does not apply to penalties
        calculated by other CSDs and reported to the ICSDs for settlement instructions that
        actually failed to settle outside the two ICSDs´ settlement systems and the Bridge.

    ▪   For free of payment settlement fails:

       –   either in the currency of the underlying security if the instrument is quoted in nominal
           or per cent (usually fixed income instruments); or

       –   in the currency of the daily reference price, if the underlying security is quoted in units
            (usually shares); or

       –   in a default currency, as defined by and eligible for settlement in the Calculating-CSD or
           settlement platform.

This may lead to the need to calculate penalties in another currency (see Chapter 6).





33 For instruments with specific features like pool factors, CSDs shall apply the price as sourced from the Trading Venue or determined
by the CSD, without any special modifications for penalties calculation purposes.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                          35 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 37
5.3  INSTRUMENT TYPE

The instrument type classification will be derived from a CFI code mapping table included in
Annex II (Document 2).

The ‘Financial Instrument Type’ is a classification of securities according to which CSDs shall report
settlement fails to regulators, as laid out in the CSDR SDR RTS Annex 1, table 134.

This  classification  is  also  relevant, together with the  Liquidity and SME Growth Market
classifications for the identification of the applicable penalty rate for any given failed settlement
instruction.

Therefore, CSDs shall, for each security, derive the Financial Instrument Type classification from the
CFI Code of the same security, according to the following mapping table (source: T2S CR654 dd.
04.10.2018):

CFI Code Structure                                              Type of Financial
                                                                   Instrument

Position 1 of the code is ‘E’                                     SHRS

Position 1 of the code is ‘D’ and position 4 is ‘T’ or ‘C’, or position 2 is ‘N’    SOVR

Position 1 of the code is ‘D’, position 2 is neither ‘Y’ or ‘N’ and Position 4 is  DEBT
neither ‘T’ nor ‘C’

Position 1 of the code is ‘R’                                     SECU

Position 1 of the code is ‘C’ and position 2 is ‘E’                         ETFS

Position 1 of the code is ‘C’ and position 2 is not ‘E’                      UCIT

Position 1 of the code is ‘D’, position 2 is ‘Y’ and position 4 is neither ‘T’ nor MMKT
‘C’

Position 1 is ‘T’, position 2 is ‘T’ and position 3 is ‘N’                  EMAL

Residual category                                        OTHR

5.4  INSTRUMENT LIQUIDITY/ ILLIQUIDITY CLASSIFICATION

The liquidity indicator is a binary classification of securities that, for the penalties calculation, only
applies to shares, i.e. when the Financial Instrument Type of the security is ‘SHRS’ and specifies if
the security is ‘Liquid’ or ‘Illiquid’35.





34 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.230.01.0001.01.ENG&toc=OJ:L:2018:230:TOC
35 See Rules RE15 and RE20 of the ‘ECSDA Rules & Recommendations’ document in Annex V for details.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                       36 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 38
For instruments not listed in the FITRS Equity Transparency Calculation Results at all and for
instruments for which the CFI code starts with ‘E’ but that are not listed in the relevant FITRS ‘Equity
Instruments’ file, the applicable value shall be ‘illiquid’.

This classification of securities is an attribute of the securities subject to penalties and must be
derived  by  the CSDs  from  the ESMA  database:  https://www.esma.europa.eu/databases-
library/registers-and-data

    ▪  Use the file ‘Financial Instruments Transparency System (FITRS)’ to open and filter on
       ‘Instrument Type’ equals ‘Equity Instruments’.





    ▪   ‘Please refer to the detailed ESMA information:
        https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_fitrs_fi
        les
    ▪  Then use the link to ‘ Instructions on how to download and use transparency results files’
      and use the document stored under:
        https://www.esma.europa.eu/sites/default/files/library/esma65-8-
       5240_firds_download_and_use_of_full_and_delta_transparency_results_files.pdf ’





DRAFT V7.0 – Publicly available to relevant stakeholders                                                           37 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 39
In summary, FULECR/ DLTECR records occur in one of the following cases and are to be assessed
according to Rule RE19 ‘Rule for usage of FITRS reporting markers’ of the ‘ECSDA Penalties
Reference Data Rules & Recommendations’ document in Annex V:

Reporting period    Type of calculation   Type of instrument   Period of application
Empty               Estimates             Equity/ Equity-like     Liquidity and LIS/ SMS
                                                               thresholds apply from first
                                                               trading date for six weeks
                                                                   Calculation results may be
                                                        updated e.g. when refined
                                                              estimates are provided NCAs
                                                              or ESMA.
Four calendar         Calculations based    Equity/ Equity-like     Liquidity and LIS/ SMS
weeks            on first four weeks                        thresholds apply from six
                     of trading                                calendar weeks after the
                                                                               first trading date, until the
                                                          next yearly calculation as per
                                                                 table 24
1/Jan/Y – 31/Dec/Y     Yearly calculations    Equity/ Equity-like     Liquidity and LIS/ SMS
                                                               thresholds apply from 1 April
                                                              of year (Y+1) until 31 March
                                                              of year (Y+2)

For all technical issues related to the ESMA databases, the ESMA Support Team can be reached at
‘support@esma.europa.eu’, copying also ‘FITRS-Secondary-Markets@esma.europa.eu’.


5.5  INSTRUMENT TRADING SEGMENT ‘SME GROWTH MARKET’  - PLACE OF TRADING

     INFORMATION

The SME Growth Market indicator is a binary classification of securities that applies to any type of
securities and that specifies whether the security is listed in an SME Growth Market.

For the sake of identifying the applicable penalty rate, CSDs need to identify whether the
instrument to be settled was actually traded on an EU SME Growth Market by verifying both, the
receiving and delivering instruction of the settlement transaction.

Only when both instructions show the same ‘Place of trading’ four-digit MIC (Market Identifier
Code) the reduced penalty rate applicable to SME instruments shall be applied.

The list of SME Growth Market Trading Venues can be found on the ESMA website:

https://www.esma.europa.eu/databases-library/registers-and-data

Use file: ‘MiFID II/MiFIR TV/SI/DRSP’ to open:

https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_upreg





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      38 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 40
Considering the attached screenshot:

    ▪   set filter in selection field ‘SME’ to ‘YES’;
    ▪   in order to see the MIC36, the detailed view ‘More Info’ must be opened.





36 As of 23.07.2021, the following venues´ MICs represent EU SME Growth Markets: XAIM, GBUL, XZAP, DSME, SSME, FSME, ALXP, XESM,
ALXL, ALXB, XETW, XETS, FRAS, NSME, XNCO, WMTF, GROW, XSAT.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                       39 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 41
5.6  INSTRUMENT CATEGORY PENALTY RATE

Considering all the previously mentioned decision criteria, CSDs shall apply the ESMA penalty rates
as quoted below and published as such in the Delegated Regulation 2017/38937:

 Type of fail                                             Rate

   1. Settlement fail due to a lack of shares that have a liquid  1,0 basis point
    market within the meaning of point (b) of Article 2(1)(17) of
    Regulation (EU) No 600/2014, excluding shares referred to
     in point 3

  2. Settlement fail due to a lack of shares that do not have a  0,5 basis point
     liquid market within the meaning of point (b) of Article
     2(1)(17) of Regulation (EU) No 600/2014, excluding shares
    referred to in point 3

  3. Settlement  fail due to a lack of financial instruments  0,25 basis point
    traded  on SME  growth  markets,  excluding  debt
    instruments referred to in point 6

  4. Settlement fail due to a lack of debt instruments issued or  0,10 basis point
    guaranteed by:

      (a)    a sovereign issuer as defined in Article 4(1)(60) of
             Directive 2014/65/EU;

      (b)   a third country sovereign issuer;

      (c)    a local government authority;

      (d)    a central bank;

      (e)    any multilateral development bank referred to in
           the second subparagraph of Article 117(1) and in
              Article 117(2) of Regulation (EU) No 575/2013 of
           the European Parliament and of the Council (1);





37 European Commission Delegated Regulation (EU) 2017/389, of 11 November 2016, supplementing Regulation (EU) No 909/2014 of the
European Parliament and of the Council as regards the parameters for the calculation of cash penalties for settlement fails and the
operations of CSDs in host Member States. Published at: http://eur-lex.europa.eu/eli/reg_del/2017/389/oj When applicable, updates will
be proposed and published by ESMA.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                    40 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 42
       (f)    the European Financial Stability Facility or the
           European Stability Mechanism.

  5. Settlement fail due to a lack of debt instruments other  0,20 basis point
    than those referred to in points 4 and 6

  6. Settlement fail due to a lack of debt instruments traded  0,15 basis point
    on SME growth markets

  7. Settlement  fail due to a  lack of  all other  financial  0,5 basis point
    instruments not covered in points 1 to 6

  8.   Settlement fail due to a lack of cash                         Official    interest    rate    for
                                                           overnight credit charged by the
                                                                 central   bank    issuing   the
                                                           settlement currency with a floor
                                                             of 0 (zero)38




5.7  CENTRAL BANK DISCOUNT RATE (PENALTIES DUE TO LACK OF CASH)

CSDs must source the relevant interest rate for the currency of the failing settlement instruction in
case the fail reason is ‘lack of cash’.

The cash discount rate is the official interest rate of the central bank issuing the settlement
currency that should evidence the borrowing costs for that currency.

For EUR, this is the ‘marginal lending facility rate’ which is published on the ECB website39.

For penalties calculations, the annual cash discount rate shall be divided by 360 days in order to
generate the applicable daily penalty rate.

Discount rates in percentages shall be reported up to ten digits after the comma; the rounding rule
RE11 ‘Rule for cash discount penalty rates’ as defined in the ‘ECSDA Penalties Reference Data Rules
& Recommendations’ (see Annex V of the Framework) applies, i.e. rounding to the next higher digit
when the 11th digit´s value is five or higher.





38 As this is an annual rate, a conversion to a ‘daily rate’ (by dividing the rate by 360 days) shall be applied for penalties the calculations
(see Chapter 5.7).
39 Discount rates would be updated by the corresponding to the currency EU Central Banks. For the ECB rates, please see
http://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.htmll




DRAFT V7.0 – Publicly available to relevant stakeholders                                                                41 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 43
Example: annual rate for currency XYZ is 0.05% - daily rate in % is 0.05/360= 0.000138888889% à
daily penalty rate is: 0.0001388889%.

In the absence of a common definition of the CSDR legal text term ‘discount rate’, ECSDA defined
a table describing for each currency which Central Bank rate concretely shall be used by CSDs for
penalties calculation purposes (note: the attached file serves as illustration, the interest rates and
website links displayed therein are not updated through this ECSDA Framework document. For
DKK, the ‘proxy’ rate calculation rule of the Danish National Bank from July 2021 is displayed).



      Currencies Discount
     Rates_Update_260820



5.8  FOREIGN EXCHANGE RATES (FX)

For non-EUR currencies, the relevant Central Banks’ Foreign exchange (FX) rates shall be consulted.

As explained in Chapter 6, for FOP instructions related penalties, a penalty calculation in another
currency may be required.

CSDs must then source the relevant FX rate for the relevant currency of the failing settlement
instruction (for EUR, various FX rates are published by ECB on their website40; in case FX rates are
missing or other cross-rates (e.g. SEK/ DKK) are needed, these must be sourced by CSDs preferably
from the respective National Central Bank issuing the currency).

Foreign exchange rates applied will not be reported in the daily and monthly reporting.





40 http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html




DRAFT V7.0 – Publicly available to relevant stakeholders                                                          42 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 44
6  PENALTIES CURRENCIES CONVERSIONS NEEDS


This section suggests an approach for scenarios involving multiple CSDs when the currency of the
reference price or cash penalty is calculated in a currency that is not eligible at the Calculating-CSD
or Investor-CSD.

As it is the responsibility of the CSD being a participant in the Calculating-CSD to ensure the
payment is executed towards the Calculating-CSD in the currency as reported, the handling of a
potential cash conversion is ultimately left to the discretion of the Investor-CSD.

An issue related to the penalties collection/ redistribution due to divergent currencies can
materialise only in a free of payment41 settlement fails scenario where the penalty currency applied
by the Calculating-CSD is not eligible in the Investor-CSD(s) or settlement platform (e.g. the T2S
settlement platform). CSDs may in such cases require payments to be arranged by their participants
to/ via payment banks.

Generally, the instrument reference price currency shall be applied by the Calculating-CSD, i.e. the
amount imposed by the penalty shall be calculated in one of the following ways:

       ▪   either in the currency of:

                          i.   the underlying security  if the instrument is quoted in nominal or percent
                    (usually fixed income instruments); or

                          ii.   the daily reference price if the underlying security is quoted in units (usually
                    shares);

              or

       ▪   in a default currency as defined by and eligible for settlement in the Calculating-CSD.

If a currency is not eligible at the Calculating-CSD (i.e. settlement or cash accounts in the reported
currency are not available for participants), unless CSDs require payments to be arranged by their
participants to/ via payment banks, a currency conversion process shall apply by the Calculating-
CSD (using a default currency to be defined by the CSD) as follows:

      1.   It calculates the penalty in the currency of the reference price;
     2.   It converts the daily penalty amount into the CSD´s default currency and rounds the amount
      up at least to the first two decimals;
    3.   It reports the (converted) penalty amount in the currency actually to be credited/ debited
         in the daily penalty reporting, per CSD, currency, and counterparty.





41 For against payment transactions, by definition, the settlement currency must be eligible in all CSDs involved in the settlement; this
applies for intra- and cross-CSD settlements. In case the reference price is deviating from the currency of the cash leg, conversion into
the settlement currency must be applied by the penalties Calculating-CSD. In case of fails due to lack of cash, the penalty amount shall
always be calculated in the currency of the cash leg.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                        43 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 45
The Calculating-CSD subsequently only reflects the converted currency amount in its monthly
reports (and payment pre-advices, if applicable).

No cash is actually to be exchanged on a daily basis, but payments are only made once a month.

Cross-CSD settlement fails

In case the Investor-CSD does not offer cash accounts/ settlement in the currency applied by the
Calculating-CSD, the Calculating-CSD may be paid by the Investor-CSD (or the Investor-CSD by its
underlying participants) via a payment bank.

As described before, the penalty currency(ies) to be processed is defined by the Calculating-CSD.
Subsequently, Investor-CSDs should, if possible, collect from/ pay to their underlying clients in the
currency as reported by the Calculating-CSD in order to avoid that FX exposures or cash imbalances
occur on the level of the Investor-CSDs.

After receipt from the Calculating-CSD, the Investor-CSD reports the penalties further to its
underlying participants and secures the collection/ redistribution of the penalty amounts on a
monthly basis, if possible, in each currency as reported by the Calculating-CSD. Hence, the Investor-
CSD(s) being participants of the Calculating-CSD, shall provide the following reporting in the
currency(ies) as applied by the Calculating-CSD:

     1.   Daily reporting of penalties;
     2.  Monthly aggregated reporting of penalties over the calculation period per currency and
        party;
    3.  Aggregated amounts to be collected/ redistributed per currency and party.

Intra-CSD settlement fails

In an intra-CSD context, no FX issues should occur. The currency to be used for the penalties is at
the discretion of the Calculating-CSD. For DVP instructions, the currency of the cash leg should be
applied (see Chapter 5.2).





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      44 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 46
7  CALCULATION METHODS OF THE CASH PENALTIES


As also described in Chapter 9, the (obligation for the) calculation of penalties depends on the
settlement platform:

    ▪   For T2S, as the T2S penalty mechanism knows both, the receipt and delivery leg of the
        transaction, the involved CSDs can rely on T2S to calculate the penalties.

    ▪   For intra-CSD settlements outside T2S, the CSD on whose platform settlement takes place
          is calculating the penalties.

    ▪   For non-T2S cross-CSD settlements, the (Issuer-)CSD where the ultimate settlement takes
       place calculates the penalties for both legs of the transaction.

For Bridge settlement, the delivering (I)CSD performs the calculation. Note: in relation to Chapters
7.3 and 7.4, the term ‘party’ refers to ‘T2S party BIC’ (where the T2S settlement platform is
calculating the penalties. The term ‘CSD-link’ refers to settlement fails outside T2S (i.e. the Issuer-
CSD is the Calculating-CSD).

As a general rule, all penalty amounts shall be rounded up by CSDs at least to the first two decimals.

      Note regarding partially successful buy-ins42 and LMFP:

      CSDR RTS Article 16.343 (referring to Art. 27.10 (c), 29.11 (b) and 31.11 (b)) stipulates that cash
        penalties shall apply to new settlement instructions that are representing the remaining
          (i.e. not bought-in) part of the failing transaction only as of the date of entry into the CSD
       system but not from the ISD of that instruction.

For CSDs to be able to comply with this requirement, the relevant CSD participants (including CCPs)
should apply a market practice in such instances, requesting them to provide a specific qualifier in
their settlement instructions; otherwise, CSDs cannot ensure the avoidance of LMFP calculations
on an automated basis:

    ▪  MT54x/ ISO15022: sequence E ‘Settlement Details’ must contain field 22F:: STCO/REGL/BSSP.
    ▪   sese/ ISO20022 (e.g. T2S): code ‘BSSP’ to be used, see T2S CR717 and 728 for details.

Note: SWIFT implemented a new code “BPSS” in November 2021. CSDs using the MT537 or sese/
20022 messaging should communicate to their participants whether they support the new
“BPSS” coding (and by which date) or not.





42 The entry Into force of these rules has been delayed beyond 01st February 2022 to a date that is yet to be defined.

43 The Article states “(…) Where new settlement instructions are entered into the securities settlement system for any non-delivered
financial instruments in accordance with Article 27(10), Article 29(11) or Article 31(11) [these Articles refer to partial buy-ins], cash penalties
shall apply to the new settlement instructions from the day those instructions are entered into the securities settlement system.”




DRAFT V7.0 – Publicly available to relevant stakeholders                                                        45 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 47
Important note: only when these values are present on both, the receipt and delivery instruction,
LMFP would not be applied under this exemption rule.

Alternatively, CSD participants may adapt the ISD for such new instructions to a later date to
avoid LMFP.

Example

    ▪   Party A has a delivery to Party B for 300 shares that fails for 4 days (SEFP and LMFP, if
        instructed after ISD, is applied)

    ▪  On ISD+4, a buy-in is initiated by Party B with Buy-in Agent C. The buy-in is only successful
        for 200 shares, the subsequent delivery from Party C to Party B settles on ISD. (If the buy-
         in settlement instruction was instructed or settled after ISD, SEFP and LMFP will be
       applied as normal).

    ▪  Upon settlement of the 200 shares, the initially failing instruction of 300 shares between
       Party A and Party B should be cancelled by both parties.

    ▪   Additionally, unless cash compensation is applied, the remaining 100 shares need to be
        instructed by both parties A and B for matching and settlement, normally using the ISD of
       the original instruction and containing the respective ‘BSSP’ coding for the CSDs to be
       able to apply the ‘exceptional instruction entry date’ rule not to apply LFMP.


7.1  SETTLEMENT FAIL PENALTY (SEFP)

Once a failing settlement instruction has been identified as subject to the computation of SEFP
according to the detection rules described in Chapter 3 and it was determined that a penalty is
imposed (refer to Chapter 4), the CSD can calculate the penalty to be applied.

The amount imposed by the penalty must be calculated depending on:

            i.       the type of transaction formed by the two matched settlement instructions using
              reference data,

           ii.       penalty rate of the ISIN or discount rate (Central Bank interest rate on cash) for the
                 financial instrument exchanged by the transaction and

          iii.      whether the instruments need to be delivered or received by the counterparty.

It is to be noted that:

       ▪  When a settlement fail reason ‘lack of securities’ has been identified by the CSD, no
            additional fail check for a ‘lack of cash’ shall be made by the CSD.
       ▪   or currencies aspects, please refer to Chapters 7.3 and 7.4 for various calculation
          examples.

The following table summarises the basis for calculating the penalty amount for each type of
transaction:




DRAFT V7.0 – Publicly available to relevant stakeholders                                                     46 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 48
Type of transaction                      SEFP
- Delivering versus Payment (DVP)            Penalty based on the quantity of securities failed to
- Delivering Free of Payment (DFP)          be delivered and Security penalty rate of the
- Receiving Free of Payment (RFP)             relevant asset type44.


- Receiving versus Payment (RVP)             Penalty based on the quantity of securities failed to
                                     be delivered and the discount rate of the relevant
                                             currency.
- Debiting Payment Free of Delivery (DPFOD)  Penalty based on the amount of cash failed to be
- Crediting Payment Free of Delivery (CPFOD)  delivered and the discount rate of the relevant
                                             currency.
- Delivering with Payment (DWP)             Penalty will be the sum of:
- Receiving with Payment (RWP)                         - Penalty based on the quantity of securities failed
                                           to be delivered and Security penalty rate of the
                                             relevant asset type; and
                                                                              - Penalty based on the amount of cash failed to be
                                             delivered and the discount rate of the currency.

If a fail is due to an instruction that is put ‘on hold’, such instruction is to be considered as the failing
one, and the above-mentioned formulas have to be applied.

The formulas to calculate the penalty imposed by a Settlement Fail Penalty (SEFP) are the following:

    ▪     i. For a failing DVP, DFP or RFP Settlement Instruction (including when ‘on hold’):

         SEFP = Security Penalty Rate*Reference Price*Quantity

         −  Security Penalty Rate is the penalty rate stored in Static Data for the relevant asset
              type (derived from the ISIN and Place of trade) and the business day for which the
              penalty is calculated;

         −  Reference Price is the price stored in static data for the ISIN of the instruction and
              the business day for which the penalty is calculated;

         −  Quantity is the quantity of securities failed to be delivered, which is the quantity of
              the instruction remaining to be settled at the time of the end of processing of the
               relevant cut-off.

    ▪     ii. For a failing RVP Settlement Instruction (including when ‘on hold’):

         SEFP = Cash Discount Penalty Rate*Reference Price*Quantity





44 Penalty rate as determined in the relevant ESMA Delegated Act.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                         47 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 49
         −  Cash Discount Penalty Rate is the discount rate of the relevant currency stored in
                Static Data divided by 360 and the business day for which the penalty is calculated.

         −  Reference Price is the price stored in Static Data for the ISIN of the instruction and
              the business day for which the penalty is calculated.

         −  Quantity is the quantity of securities failed to be delivered, which is the quantity of
              the instruction remaining to be settled at the time of end of processing of the
               relevant cut-off.

    ▪     iii. For a failing DPFOD or CPFOD Settlement Instruction (including when ‘on hold’):

         SEFP = Cash Discount Penalty Rate*Amount

         −  Cash Discount Penalty Rate is the discount rate of the relevant currency stored in
                Static Data divided by 360 and the business day for which the penalty is calculated.

         −  Amount is the cash amount failed to be delivered, which is the amount of the
                instruction remaining to be settled at the time of end of processing of the relevant
                 cut-off45.

    ▪    iv. For a failing DWP or RWP Settlement Instruction (including when ‘on hold’):

         SEFP = Security Penalty Rate* Reference Price* Quantity + Cash Discount Penalty Rate*
         Amount

         −   Security Penalty Rate*Reference Price*Quantity as described in (i);

         −  Cash Discount Penalty Rate* Amount as described in (iii).

The penalties amounts might be reported with various decimals, but the monthly payment
amounts shall be rounded up at least to the first two decimals.

The penalties calculated should be retained for 3 months.

7.1.1    Illustrative penalties calculation examples

     1.   Failing DVP or DFP settlement instruction (SEFP) – lack of securities

Delivery of 5,000 (liquid or illiquid) shares (“SHRS”), traded on an SME Growth Market Trading
Venue, failing due to “lack of securities” for 2 days after the ISD, penalty reference price day 1 =
25.—EUR/ day 2 = 27.—EUR. Please also refer to Chapter 5 for reference data information.

    ▪   Formula: Security Penalty Rate*Reference Price*Quantity





45 Rationale: Although the CSDR prescribes to use the security quantity and reference price for the calculation of all settlement fail
penalties, for DPFOD and CPFOD settlement instructions where the ISIN quantity is zero, the cash amount is used to compute the
penalty (approach as confirmed by ESMA in their Q&A as updated on 03rd August 2022). Please note the special handling in case of
partially successful buy-ins as described in the Framework Chapter 7.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                     48 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 50
Fail day 1:

0.25 basis points * 25 *5,000

= 0.0025% * 125,000 EUR

= 3.13 EUR



Fail day 2:

0.25 basis points * 27 *5,000

= 0.0025% * 135,000 EUR

= 3.38 EUR



Total SEFP amount = 3,13 EUR + 3,38 EUR = 6.51 EUR (due to be paid by the securities delivering
participant).



2.  Failing RVP settlement instruction (SEFP) – lack of cash

Delivery of 5,000 (liquid or illiquid) shares (“SHRS”), failing due to “lack of cash” for 2 days after
the ISD, penalty reference price day 1 = 25.—EUR/ day 2 = 27.—EUR, for EUR, the ECB “marginal
lending facility rate” applies. Please also refer to Chapter 5 for reference data information.

    ▪   Formula: Cash Discount Penalty Rate*Reference Price*Quantity

Fail day 1:

(0.25%/ 360) * 25 *5,000

= 0.0006944444 * 125,000 EUR

= 0.87 EUR



Fail day 2:

(0.25%/ 360) * 25 *5,000

= 0.0006944444 * 135,000 EUR

= 0.94 EUR



Total SEFP amount = 0.87 EUR + 0.94 EUR = 1.81 EUR (due to be paid by the cash-delivering
participant).



DRAFT V7.0 – Publicly available to relevant stakeholders                                                     49 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 51
Note that the examples also apply in the case of “Late Matching Fail Penalties” (LMFP; see also
Framework Chapters 4.1 and 7.2). The only difference is that the failing participant is identified by
who was “last to enter or modify” the relevant settlement instruction after the ISD.


7.2  LATE MATCHING FAIL PENALTY (LMFP)

For settlement instructions that are matched in the CSD system only after the relevant cut-off of
their Intended Settlement Date (ISD), penalties shall be calculated only once (i.e. on the business
day when they are matched) but considering all the previous business days where the instruction
failed to settle due to the late matching46.

Settlement Fail Penalties (SEFP) and Late Matching Fail Penalties (LMFP) shall follow the same
principles for their computation.

7.2.1   Number of days considered in the computation of LMFP

The number of days to consider in the formula to calculate the amount imposed by a Late Matching
Fail Penalty (LMFP) will differ depending on whether the instruction subject to LMFP can either still
settle, or no longer settle, on the business day when the instruction is matched (i.e. depending on
whether it is matched before or after the relevant cut-off for the Matching Business Day).

     1.  When the instruction can still settle on the business day when it is matched:

           ▪   This scenario relates to those instructions matched after their ISD (late matching)
              but matched at a point in time when it is still possible to settle them on the business
             day when they are matched (i.e. matched before the relevant cut-off for Matching
              Business day).

           ▪  The LMFP shall be calculated for each business day as from the ISD until and
               excluding, the business day when the instruction is matched.

           ▪   In case the instruction does not settle on the business day when it is matched (even
                       if it was possible because it arrived before the cut-off) then, a separate calculation
                  will have to be performed for an additional SEFP.





46 Amendments could still be performed on these LMFP, in case of reference data updates for instance.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                      50 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 52
The matching date is excluded from the LMFP and included in the SEFP.

     2. When the instruction can no longer settle on the business day when it is matched:

           ▪   This scenario relates to those instructions matched, on or after the ISD, at a point
                 in time when it is not possible to settle them on the business day when they are
            matched because it is after the relevant cut-off.

           ▪  The LMFP shall be calculated for each business day as from the ISD until, and
                including, the business day when the instruction is matched.





The matching date is included in the LMFP and excluded from the SEFP.



7.2.2   Formulas to be used

Note: Everything will be the same as for instructions that can still settle but, additionally, the
business day when the instructions are matched must be included.

i. For a DVP, DFP or RFP received late:

        LMFP = Security Penalty Rate*Reference Price*Quantity

          −   Security Penalty Rate is the penalty rate stored in Static Data for the relevant asset
              type (derived from the ISIN and Place of trade) and for the relevant business day.

          −  Reference Price is the price stored in Static Data for the ISIN of the instruction and
                for the relevant business day.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                                   51 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 53
            −   Quantity is the quantity of securities failed to be delivered, which is the matched
               quantity of the Settlement Instruction.

ii. For an RVP received late:

        LMFP = Cash Discount Penalty Rate* Reference Price* Quantity, where;

          −  Cash Discount Penalty Rate is the discount rate of the relevant currency stored in
                Static Data divided by 360 and the business day for which the penalty is calculated;

          −  Reference Price is the price stored in Static Data for the ISIN of the instruction and
              the relevant business day.

          −  Quantity is the quantity of securities failed to be delivered, which is the matched
               quantity of the instruction.

iii. For an RVP received late and as an already matched instruction:

        LMFP = Security Penalty Rate * Reference Price* Quantity, where:

          −   Security Penalty Rate is the penalty rate stored in Static Data for the relevant asset
              type (derived from the ISIN and Place of trade) and for the relevant business day;

          −  Reference Price is the price stored in Static Data for the ISIN of the instruction and
              the relevant business day;

          −  Quantity is the quantity of securities failed to be delivered, which is the matched
               quantity of the instruction.

iv. For a DPFOD or CPFOD received late (ISIN quantity is 0):

          −  LMFP = Cash Discount Penalty Rate* Amount;
          −  Cash Discount Penalty Rate is the discount rate of the relevant currency stored in
                Static Data divided by 360 for the relevant business day;
          −  Amount is the cash amount failed to be delivered, which is the matched cash
            amount of the Settlement Instruction.

v. For a DWP or RWP received late:

          −  LMFP = Security Penalty Rate * Reference Price * Quantity + Cash Discount Penalty
             Rate * Amount;

          −   Security Penalty Rate*Reference Price*Quantity as described in (i);

         −  Cash Discount Penalty Rate* Amount as described in (iv).

Note: the penalties calculated should be retained for 3 months.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                            52 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 54
7.3  DAILY BILATERAL NET PER COUNTERPARTY

In addition to the gross penalties calculated on a daily basis, a bilateral net amount per CSD link,
(only relevant for cross-CSD fails with non T2S CSDs), per currency and counterparty must be
provided.

For each relevant business day, a net amount is calculated for the party against each of its
counterparties.

Thus, for a given party, the bilateral net amount (due or entitled) against a given counterparty is:

       ▪  The sum of all the penalties (SEFP + LMFP) calculated at the failed instruction level that
             this party is entitled to receive (reported as credit) from a given counterparty (i.e. to be
           paid by this counterpart) in a CSD;

minus

       ▪  The sum of all the penalties (SEFP + LMFP) calculated at the failed instruction level that
           are imposed to the party (reported as debit) and to be paid to the same counterparty
             in the same CSD.

Three scenarios apply:

     1.   Intra CSD scenario47: daily bilateral net with each counterparty in this CSD (at party level).
     2.  Cross-CSD scenario (‘T2S in CSDs’): daily bilateral net with each T2S CSD (at party level).
    3.  Cross-CSD scenario (non-‘T2S in CSDs’): daily bilateral net per CSD-link (CSD level).

If the result of the calculation is a positive amount, the bilateral net amount will be a credit for the
party (i.e. an amount entitled from the counterparty); if the result is a negative amount, the
bilateral net amount will be a debit (i.e. an amount due to the counterparty).

Note: No netting is to be performed across CSDs and currencies, i.e. a net by CSD-link, currency and
counterparty must be applied.


7.4  MONTHLY CASH PENALTIES AGGREGATION AND GLOBAL NET AMOUNTS

7.4.1   Monthly bilateral net per counterparty

On the 14th PBD of the month, bilateral net amounts of the penalties computed for all the business
days of the previous month are calculated per CSD, currency, and party against each of its
counterparties.

When calculating the monthly aggregated amounts, the CSD will consider the last available value
of the amount of each penalty aggregated (i.e. the CSD will take into account all updates performed





47 This scenario covers as well parties/ participants at the Issuer-CSD that are CSDs.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                          53 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 55
until the end of the penalties appeal period for CSDs, i.e. changes until and including the 11th PBD of
the following month).

This aggregation of the monthly penalties per CSD-link, currency and counterparty (i.e. bilateral net
amounts) allows to:

    ▪   Isolate non-payments from CSD participants (i.e. participants affected by a non-payment of
          its counterpart as well as the amount that cannot be distributed by the CSD since it was not
        collected could be easily identified);
    ▪   Provide a netting as required by the CSDR;
    ▪  Reduce the required liquidity.

Accordingly, for each party/ CSD-link, currency and counterparty, the monthly bilateral net amount
equals to:

   ▪  The sum of all the cash penalties of the previous month in the relevant currency, that the
       party is entitled to receive (reported as credit) from a given counterparty (i.e. to be paid by
        this counterparty);

Minus

   ▪  The sum of all the cash penalties of the previous month in the relevant currency and that
      were imposed to the party (reported as debit), and to be paid to the same counterparty.

Subsequently, for each party/ CSD-link, a bilateral ‘net amount per counterparty’ is calculated.

Three scenarios apply:

     1.   Intra CSD scenario48: monthly bilateral net with each counterparty in this CSD (at party
         level).
     2.  Cross-CSD scenario (‘T2S in CSDs’): monthly bilateral net with each counterparty T2S CSD
        (at party level).
    3.  Cross-CSD scenario (non-‘T2S in CSDs’): monthly bilateral net per CSD-link (CSD participant
         level).

If the result is a positive amount, the bilateral net amount will be a credit for the party (i.e. an
amount entitled to be received from the counterparty);  if the result is a negative amount, the
bilateral net amount will be a debit (i.e. an amount due to the counterparty).



7.4.2   Global Net (monthly amount to be paid or to be received)

For each CSD, currency and party, the monthly net amount equals to:





48 This scenario covers as well participants at the Issuer-CSD that are also CSDs (i.e. Investor-CSDs).



DRAFT V7.0 – Publicly available to relevant stakeholders                                                        54 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 56
   ▪  The sum of all the net bilateral amounts in the relevant currency, that the party is entitled
       to receive (reported as credit and for all counterparties);

Minus

   ▪  The sum of all the net bilateral amounts in the relevant currency and that were imposed to
       the party (reported as debit and for all counterparties).

The total of the bilateral nets will result in:

    ▪  a global net per CSD (for intra-CSD), and/ or
    ▪  a global net for per counterparty-CSD for cross CSD with T2S-in CSDs scenarios. For
        instance, a global net between CSD A and CSD B (note: there is no “place of settlement”
       concept applied by the T2S penalty mechanism), and/ or a global net per CSD-link (for cross-
      CSD with non-‘T2S in CSDs’ scenario). For instance, a global net between a) CSD B and CSD
     A where CSD B is the actual place of settlement, and b) between CSD B and CSD A where
      CSD A is the actual place of settlement. The ‘global net’ amount resulting from this
        calculation and will either be an amount due by the party (i.e. to be paid by the party), or
      an amount to be received by the party.

This amount will either be reported via the monthly report, a payment pre-advice or through PFOD
instructions (the process depends on the CSD payment process and the CSD settlement platform)
to the CSD participants. Please refer to Chapter 11.3.3 for details.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                          55 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 57
8 CHANGES TO PREVIOUSLY CALCULATED PENALTIES


Updates of previous penalty calculations shall be done by the CSD as soon as the reference data
becomes available to the CSD and considering the appeal period.

T The latest point in time for consideration of new (or updated) reference data by the CSD is prior
the monthly reporting. That means if new or updated data for calculating penalties are available to
the CSD or penalty engine (e.g. T2S) only after the monthly report was generated, no retroactive
penalties calculations or adaptations can be made by the CSDs or penalty engine.



Note that, in addition to the following penalties changes activities steps, T2S foresees a ‘switch’
mechanism49; as this is not considered relevant for non-T2S settlements it is not covered in this
Framework.


8.1  REMOVAL OF EXISTING PENALTIES

In the circumstances described in Chapters 2.1.4 and 2.2.4 (‘Monthly Appeal Period’), CSDs may
remove an already computed and reported penalty (i.e. set the penalty amount to ‘zero’) latest
until (and including) the 11th PBD of the following month.

When the removal of a penalty is performed, the CSD shall use a standard to specify the reason for
the removal (see Framework Annex II, item 4 ‘Penalties adjustments reason codes’ for details).
Such removals would need to be communicated to the National Competent Authorities.

The CSD shall also report the removal of a penalty in the relevant Daily Report:

    ▪  On the business day following the removal of the penalty, the CSD shall report the removal,
        either in the Daily Report (with the penalties computed for the previous day) or in the
       report of updated/ modified penalties.

    ▪   Within this report, the penalties that have been set to zero will be reported with:

          −  New amount equal to zero;





49 Switch between the failing and non-failing party of a cash penalty: this functionality caters inter alia for cases where a transaction is
settled on multiple platforms, i.e. where settlement on T2S depends on the fulfilment of a condition outside T2S. For example, when
cash settlement takes place outside T2S while the settlement of securities takes place in T2S, conditional securities deliveries (CoSD)
may be used by T2S Actors to block the securities in T2S until cash settlement takes place on the relevant platform. Depending on the
CoSD configuration and the business scenario, T2S could compute and assign the penalty to the incorrect party (i.e. to the delivering
instead of to the receiving participant or vice versa), e.g. because the free-of-payment delivery in T2S is failing, while as it is due to the
lack of cash of the counterparty on the external cash settlement platform. Hence, in order to allow the CSD to make the required ex-
post correction, the CSD shall be able to swap the failing party and the non-failing party of the cash penalty.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                       56 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 58
          −   Status ‘Removed’;

          −  The standard removal reason code (see SWIFT SMPG Market Practice in Annex II,
              item 4); and

          −   Optionally, a further description (free text) of the reason for the removal (provided
             by the CSD).



8.2  RE-INCLUSION OF A PREVIOUSLY REMOVED PENALTY

CSDs may re-include already removed penalties as from when e.g. updated information becomes
known to the CSD and latest until (and including) the 11th PBD of the following month.

When a penalty is re-included, CSDs shall calculate the penalty amount again as it may have changed
due to updates in the reference data since it was removed. This recalculation shall be performed
by the CSD in its next daily recalculation process50.

CSDs shall report the re-inclusion (penalty with status ‘active’) to both, the failing and the non-
failing parties.

On the following business day after the re-inclusion of the penalty, the CSD shall report the re-
inclusion, either in the Daily Report (with the penalties computed for the previous day), or in the
report of updated/ modified penalties:

          −   Status ‘Active’; and

          −  The standard reintroduction reason code (see SWIFT SMPG Market Practice in
            Annex II, item 4).



8.3  RE-ALLOCATION OF AN EXISTING PENALTY

CSDs may re-allocate penalties, e.g. for an LMFP (Late Matching Fail Penalty), when the penalised
party is not the real defaulting one (i.e. need to re-allocate the penalty from the instructing party
to the delivering or receiving party, or from the delivering party to the receiving one).

The CSD shall re-calculate the amount of the penalty (because a different formula for calculating
the penalty may apply, or due to changes in the reference data).





50 For T2S-in CSDs, the amount of the cash penalty, as it was when the penalty was removed, is reported by T2S; this amount may
change afterwards due to a subsequent recalculation by T2S (penalty is considered as ‘to be recalculated after being modified’).




DRAFT V7.0 – Publicly available to relevant stakeholders                                                           57 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 59
On the following business day after the re-allocation of the penalty, the CSD shall provide either
the Daily Report (with the penalties computed for the previous day) or the report of updated
penalties, including the following information:

    ▪   For the initially penalised party and its counterparty:

          −   Status ‘Removed’;

          −  A reason code to reflect the re-allocation (see SWIFT SMPG Market Practice in
            Annex II, item 4); and

          −   Optionally, a description (free text) of the reason for the re-allocation (provided by
              the CSD).

    ▪   For the ‘newly’ penalised party and its counterparty:

          −   Status ‘Active’;

          −  A reason code to reflect the re-allocation (see SWIFT SMPG Market Practice in
            Annex II, item 4);

          −   Optionally a description (free text) of the reason for the re-allocation (provided by
              the CSD); and

          −  A reference of the original penalty that has been re-allocated.



8.4 UPDATE OF EXISTING PENALTIES

Upon changes of values of the attributes of the securities subject to penalties (e.g. the reference
price of the financial instrument), CSDs shall recalculate affected penalties (i.e. those that used the
modified reference data in their calculation) and update the penalty in case their details have
changed, for example, if there is a new amount due/ entitled to receive.

The latest point in time for consideration of new (or updated) reference data by the CSD is prior to
the monthly reporting. That means if new or updated data for calculating penalties are available to
the CSD or penalty engine (e.g. T2S) only after the monthly report was generated, no retroactive
penalties calculations or adaptations can be made by CSDs or penalty engine.

After the recalculation of a penalty, CSDs shall provide either the Daily Report (with the penalties
computed for the previous day), or the report of updated penalties, including:

       ▪  New updated amount and values; and

       ▪  Reason code ‘Updated’.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      58 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 60
9 CROSS-CSD SETTLEMENT FAILS


9.1  BACKGROUND

The settlement fails scenarios listed in this section have been discussed with ESMA and informally
approved.

The following scenarios consider whether or not a CSD in the settlement chain is actually subject
to CSDR and also illustrate which CSD is responsible for the calculation, reporting and/ or collection/
redistribution of penalty amounts, including when CSDs settle via the T2S platform.

Generally, the scenarios apply an ‘actual place of settlement’ concept, i.e. only the CSD where
matching and settlement is ultimately taking place (i.e. where settlement finality is reached) is
responsible for calculating the penalties (the ‘Calculating-CSD’) and report them to its underlying
participants (that may as well be CSDs) for processing.

Note for T2S: there is no Calculating-CSD as the T2S settlement platform is the relevant penalties
calculating system. ‘T2S CSDs’ send the daily and monthly penalties reports to their participants
based on the information received from the T2S penalties system.

Relying on the Calculating-CSD avoids that CSDs calculate penalties in parallel (which anyway is not
always feasible, as e.g. late matching information is only available to the settling CSD), possibly
leading to deviating results (e.g. due to different reference prices) and reconciliation needs51.

Based on the Calculating-CSD´s input, all its participants need to ensure the actual timely collection
and redistribution of the monthly penalty amounts52 is triggered. Investor CSD(s) is/ are responsible
for the full collection and timely payment of the penalty amounts to the Calculating-CSD.

In essence, the CSDR penalties must be applied by all involved CSDs whenever the ultimate
matching and settlement is taking place in a CSD that is subject to CSDR (and if the underlying
instrument and transaction are actually subject to the penalties regime), and in compliance with
the CSD´s Terms and Conditions that bind all participants of that CSD, including when they are
themselves CSDs (in or outside CSDR reach), as it is the case for CSD-direct links.

In the case of a purely intra-CSD (i.e. CSD-internal settlement), the actual penalties application
depends on whether or not the CSD itself is subject to CSDR or equivalent legislation.





51 This approach is the same as today for those markets where penalties already apply.
52 Note for T2S external settlement, T2S will (until further notice) calculate penalties in any case. T2S CSDs will replace these penalties
by the ones reported by the Calculating-CSD (see as well Chapter 2.2.1).




DRAFT V7.0 – Publicly available to relevant stakeholders                                                       59 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 61
9.2  SCENARIO 1A





Due to its single settlement platform, T2S is able to calculate penalties for both legs of the T2S
transaction.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                   60 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 62
9.3  SCENARIO 1B





Only the Issuer-CSD (being the Calculating-CSD) receives both legs of the transaction, allowing it to
calculate the ultimate penalties.

Note regarding T2S: Due to the current T2S design, even for the single T2S leg, penalties will be
calculated by T2S. T2S CSDs will replace these penalties with the ones reported by the Calculating-
CSD (see as well Chapter 2.2).





DRAFT V7.0 – Publicly available to relevant stakeholders                                                              61 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 63
9.4  SCENARIO 1C





Due to its single settlement platform, T2S is able to calculate penalties for both legs of the T2S
transaction.


9.5  SCENARIO 2A





DRAFT V7.0 – Publicly available to relevant stakeholders                                                        62 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 64
Due to its single settlement platform, T2S is able to calculate penalties for both legs of the T2S
transaction.


9.6  SCENARIO 2B





Only the Issuer-CSD (being the Calculating-CSD) receives both legs of the transaction.

For the ‘T2S-in CSDs’, due to the current T2S design, even for the single T2S leg, penalties will be
calculated by T2S. ‘T2S-in CSDs’ will replace these penalties with the ones reported by the
Calculating-CSD (see as well as Chapter 2.2).





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      63 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 65
9.7  SCENARIO 2C





Due to its single settlement platform, T2S is able to calculate penalties for both legs of the T2S
transaction.


9.8  SCENARIO 2D





DRAFT V7.0 – Publicly available to relevant stakeholders                                                     64 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 66
Only the Issuer-CSD (being the Calculating-CSD) receives both legs of the transaction, allowing it to
calculate the ultimate penalties.

For the ‘T2S-in CSDs’, due to the current T2S design, even for the T2S legs, penalties will be
calculated by T2S. T2S CSDs will replace these penalties with the ones reported by the Calculating-
CSD (see as well as Chapter 2.2).


9.9  SCENARIO 2E





Due to its single settlement platform, T2S is able to calculate penalties for both legs of the T2S
transaction.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       65 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 67
9.10 SCENARIO 2F





Only the Issuer-CSD (being the Calculating-CSD) receives both legs of the transaction, allowing it to
calculate the ultimate penalties.


9.11 SCENARIO 2X





DRAFT V7.0 – Publicly available to relevant stakeholders                                                    66 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 68
CSD 2 (e.g. CBF, Euroclear France) is Investor CSD for the Issuer CSD (e.g. CBL, Euroclear Bank) and
at the same time technical Issuer for CSD 1 in the same ISIN. Investor CSD 1 participant is delivering
to the Issuer CSD Participant.

Only the Issuer-CSD (being the Calculating-CSD) receives both legs of the transaction, allowing it to
calculate the ultimate penalties.

Assumptions:
   Step 1: Issuer CSD reports penalties to the Investor CSD 2 (as the Issuer CSD has no relationship
   with Investor CSD 1)
   Step 2: Investor CSD 2 reports penalties to the Investor CSD1
Collection and Redistribution follow the same steps.


9.12 SCENARIO BRIDGE





Note that the ICSDs´ realignment transactions on the Issuer-CSD level are separately handled
outside the Bridge settlement flow.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       67 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 69
10 COLLECTION & REDISTRIBUTION OF PENALTIES (PAYMENT)


10.1 GENERAL OVERVIEW

‘Collection and redistribution of penalties’ refers to the actual exchange of penalties cash-amounts
(i.e. the penalties payments; separate for every single currency in which penalties were calculated
and reported by a CSD) resulting from the calculation process as described in Chapter 7.

CSDs applying this Framework shall perform the actual ‘collection and redistribution’ of the applied
penalties via the relevant payment process only once, in the following month on the 18th PBD (if
the CSD and/ or the payment system of the currency is closed on the 18th PBD, the payment shall be
done on the next possible business day).

CSDs, via their participants, shall collect/ redistribute the full amount of penalties on the 18th PBD
of the month as described in Chapter 2.

Regarding T2S, Chapter 10.1.1 must be considered.

CSDs shall not take any financial or counterparty risks; in case participants fail to pay, the CSD itself
will fail to pay further to its participants and potentially other CSDs that are expecting the cash. The
CSD should inform its participants about payment delays but cannot be held liable for such delays
caused by CSD participants.

The full penalty amounts shall be collected and redistributed to the participant that suffered from
the fail latest until the end of the month following the fail date (fail month + 1). To mitigate market
impacts in case of delays in the payments collection, a CSD may redistribute the cash it has received
on the 18th PBD to receiving participants, as well as other CSDs for cross-CSD penalties, already even
when not all dues have been fully collected and apply a ‘partial redistribution’. In such case, the
relevant receiving participants and CSDs must be paid the full amount expected by them and not
only a portion (i.e. no ‘partial payments’ apply by the CSD).

CSDs shall segregate penalties cash flows in their own books from any other activities, hence, CSDs
shall use a single (or may use several, e.g. in case of multiple links) dedicated penalties cash
account(s).

In relation to their participants, CSDs will use by default the participants´ cash account linked to the
settlement account (only if allowed by a CSD, a participant may assign a dedicated penalties cash
account as long as this complies with the CSD´s payment process). Participants not having a cash
account communicated to/ held at a CSD will be required to define one.

CSDs may use different models for the actual penalties payments processing:





DRAFT V7.0 – Publicly available to relevant stakeholders                                                   68 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 70
     1.  CSD triggers direct debits53 and/ or cash transfers;
     2.  CSD generates PFOD instructions (T2S model, see Chapter 10.1.1);
    3.  Cash transfer using a payment bank54.

CSDs shall inform their participants of the applicable payment method(s).

CSDs may define appropriate measures (to be described in the relevant contractual documents
with the CSD participants) to ensure penalty amounts due are available to the CSD and CSD
participants comply with their payment obligations to the CSD on time to avoid delays and
processing issues due to a lacking or incomplete penalties collection by the 18th PBD.

The process of collection and redistribution has to be managed in a phased approach to make sure
CSDs do not pre-finance any payment. The overall payment process consists of the following
phases:

          1.  Collection from the CSD participants (as well as receiving the subsequent payments from
          other CSDs) that are due to pay penalties;
        2.  Redistribution from a ‘penalties-receiving’ CSD to its participants.

All steps shall be performed completely on the 18th PBD for every currency involved (note: if the
CSD and/ or the payment system of the currency is closed on the 18th PBD, the payment shall be
done on the next possible business day).

As a result, penalties cash-related information must be transferred by all involved parties at least in
a near-time mode as the use of end of day cash statements would not allow for the timely payment
process completion by the involved parties including (I)CSDs and their agents (if applicable) in case
of settlement chains.

Participants that are CSDs will be treated the same way as any other CSD-participant.



10.1.1   T2S-In CSDs payments processing55
In the context of ESMA RTS on Settlement Discipline Article 20 (‘CSDs that use a common
settlement infrastructure’), T2S-In CSDs agreed to commonly apply a PFOD payment process.

Participants shall fund their relevant T2S DCAs in time to ensure PFOD penalties can settle in the
T2S night-time settlement cycle (NTS) for value 18th PBD to avoid payment delays.

T2S-In CSDs, via their participants, shall collect/ redistribute the full amount of penalties on the 18th
PBD of the month as described in Chapter 2 before cash redistributions are executed. Pre-condition





53 Note that ESMA was asked to acknowledge the risks related to CSDs not being allowed to perform direct debits in some EU countries
and to consider appropriate mechanisms to enforce the timely payment of due amounts.

54 Option 3 is least preferred by CSDs due to extended payment chains (via CCBs), increasing risk of delayed payments. However, for
foreign currency transactions it may be the only feasible option.
55 Note that non-T2S CSDs may apply a similar process and the rules described in this Chapter whenever possible and applicable.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                    69 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 71
is that the full amount expected to be received by a single CSD or CSD participant can be paid (i.e.
no ‘partial payments’ apply).



Cross-CSD payments

For cross-CSDs payments, CSDs using the T2S settlement platform will commonly apply the PFOD
method for settlement fail penalties payments reported by T2S resulting from T2S transactions
and in T2S eligible currencies.

All (delivery and receipt) PFODs should be generated at the same time.

All T2S-In CSDs shall use a single dummy ISIN LU2128008567 (debt instrument, CFI code TRFMXX,
i.e. qualified as Financial Instrument Type ‘OTHR’ as per Framework Chapter 5.356).

No ‘already matched’ process applies, i.e. each CSD needs to instruct its own settlement leg on
the 16th PBD to ensure timely matching.

 PFOD criteria
 Transaction Type          PAIR
 Trade Date                 16th PBD of the following month
 Intended Settlement Date   18th PBD of the following month57
 Dummy ISIN code         LU2128008567
 Partial Indicator         No partial allowed (NPAR in T2S platform)
 Priority Indicator           Highest possible for the CSDs (for instance, 001 in T2S platform)
 Modification Allowed     No for CSD participants that are not CSDs
                          Yes for CSD participants that are CSDs58
 Hold and Released         Released
 Common reference        Not to be used
 2nd level matching          Dedicated or standard59 CSD penalty BIC
 Matching status          To be matched
 Delivery/ Receipt          The CSD creating its leg of the PFOD is to be considered as the
                                  ‘party’:
                                                  - a CPFOD (PFOD-CRDT, crediting cash) will be used to collect cash
                       on the CSD penalties cash account, thus being a debit for the
                            counterparty CSD => collection
                                                  - a DPFOD (PFOD-DBIT, debiting cash) will be used to distribute
                           cash from the CSD penalties cash account, thus being a credit for
                           the counterparty CSD => re-distribution





56CSDs may apply blocking rules for their customers to avoid usage of the dummy ISIN.
57 Or, if not corresponding to a T2S BD, the subsequent next T2S BD.
58 Investor-CSDs in an Issuer-CSD must be able to use the hold/ release functionality.
59 Some CSDs may decide to use their ‘standard’’ BIC code and link it to a dedicated penalty cash account (DCA), while others may
decide to create a dedicated BIC code for penalties management.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                       70 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 72
                                          If the ‘party’ CSD has to receive a penalty amount è CPFOD for
                             delivery (to credit the ‘party’ CSD DCA)
                                          If the ‘party’ CSD has to pay a penalty amount è DPFOD for
                             receipt (to debit the ‘party’ CSD DCA)


Intra-CSD payments

For intra-CSD payments, unless communicated otherwise by a CSD, PFOD will be applied like for
cross-CSD payments. However, the instructions will be generated by the CSD on behalf of its
participants, as ‘already matched’, non-modifiable and should be ‘released’.

 PFOD criteria
 Transaction Type          PAIR
 Trade Date                 16th PBD of the following month
 Intended Settlement Date   18th PBD of the following month60
 Dummy ISIN code         LU2128008567
 Partial Indicator         No partial allowed (NPAR in T2S platform)
 Priority Indicator           Highest possible for the CSDs (for instance, 001 in T2S platform)
 Modification Allowed     No for CSD participants that are not CSDs
                          Yes for CSD participants that are CSDs61
 Hold and Released         Released
 Common reference        Not to be used
 2nd level matching           Participant BIC code (linked to the default settlement cash
                           account)
 Matching status            Already matched
 Delivery/ Receipt          As the transaction is already matched, both legs are created and
                        matched by the CSD:
                                                  - a CPFOD (PFOD-CRDT, crediting cash) will be used to collect cash
                       on the CSD penalties cash account, thus being a debit for the CSD
                         customer => collection
                                                  - a DPFOD (PFOD-DBIT, debiting cash) will be used to distribute
                           cash from the CSD penalties cash account, thus being a credit for
                           the CSD customer => re-distribution



10.2 STEP 1: PENALTIES COLLECTION FROM CSD PARTICIPANTS
Participants must ensure their cash accounts are funded or dues paid to the dedicated CSD
penalties cash account by the start of the CSD´s first settlement processing cycle on the 18th PBD





60 Or, i if not corresponding to a T2S BD, the subsequent next T2S BD
61 Investor-CSDs in an Issuer-CSD must be able to use the ‘hold/ release’ functionality.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                                    71 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 73
but at latest 2 hours prior to the cut-off time of the relevant currency payment system; see as well
Chapter 2 for details.

CSDs due to pay penalties to another CSD shall do so upon ) collection of the penalties from their
participants.

Note that only one ‘global net’ amount for each ‘actual place of settlement CSD’ will be exchanged
across CSDs, i.e. a CSD shall either pay to or receive penalties from another CSD as otherwise the
payment process cannot be executed (‘lock’ situation where both CSDs would be waiting for the
other to pay as otherwise they cannot redistribute the penalties to the other CSD). See Chapter 11
for details.

Regarding T2S, Chapter 10.1.1 must also be considered.

No tolerance between the amount to be paid as reported by the CSD and the amount actually
collected by the CSD is allowed, i.e. CSD participants must pay exactly the amount as calculated and
reported by the CSD. Should the amount received by a CSD not represent the one expected, the
CSD may not be able to perform the penalties redistribution to its participants (including other CSDs
in a cross-CSD penalties scenario).

There are different mechanisms available to the CSDs on how to collect the penalties; depending
on the payment model, the relevant cash account number information may need to be provided to
participants and relevant other CSDs.



10.2.1  Payment via direct debits and/ or cash transfers

10.2.1.1   Direct debit
Whenever legally and/ or contractually allowed, the CSD may collect the penalties by directly
debiting the relevant cash accounts of its participants. Such a process will avoid delays and
differences in the amounts expected and collected by the CSD and subsequent blocking of the cash
distribution process.

CSD participants must have adequately funded their cash account on time on the 18th PBD. In case
the participant cash account is not sufficiently funded; the direct debit may lead to the
consumption of granted credit lines or an account overdraft62.

10.2.1.2  Cash transfer

In the case when a direct debit is not feasible, the CSD participants will have to actively transfer the
amounts due to the dedicated cash account of the CSD by the start of the relevant currency





62 If the cash account is owned by a (Investor-) CSD, it shall not go into negative, considering that CSDs have to first collect the cash
from their own participants.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                             72 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 74
payment system´s processing cycle on the 18th PBD but at latest 2 hours prior the cut-off time of
the payment system; see as well Chapter 2 for details.



10.2.2  Payment via PFOD transactions
This process will be applied by T2S-In CSDs intra- and cross-CSD payments.

On the 16th PBD, but at the latest before the start of the 18th PBD, the CSD will create PFOD
instructions to receive the cash amounts from its participants that have to pay penalties.

CSD participants must have adequately funded their relevant cash account in order for the PFOD
to timely settle on the 18th PBD.

In the CSD´s penalties collection process, the PFOD settlement will lead to a debit of the CSD
participant´s cash account (e.g. T2S DCA) and a credit of the CSD´s penalties cash account.

Note: With the use of the PFOD instructions, the rules of the settlement platform will be applied
(i.e. recycling, reporting or other relevant rules).



10.2.3  Payment via a payment bank
In some cases (and currencies), the penalties payment process may involve a third party acting as
a payment bank for a CSD participant.

CSD participants, via their payment bank, must ensure the CSD´s penalty account is credited latest
on the 18th PBD of the month by 09:00 a.m. CET but latest 2 hours prior to the cut-off time of the
relevant currency payment system.



10.3 STEP 2: PENALTIES REDISTRIBUTION FROM PENALTIES RECEIVING CSD TO ITS
     PARTICIPANTS
When the (full or partial) collection from the CSD participants (incl. other CSDs) was processed, the
CSD shall initiate to redistribute the cash collected to its participants to clean the CSD´s dedicated
penalties cash account.

Three mechanisms are available for payments from the cash receiving CSD to its participants. Their
choice is depending on the payment model, the relevant cash account number information may
need to be provided to participants and relevant other CSDs.

10.3.1  Cash transfers
The CSD transfers the amounts due to the relevant cash accounts of its participants. Such credit
shall take place only once the payments due have been (fully or partially) collected on the 18th PBD.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                           73 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 75
10.3.2  Payment via PFOD transactions
This process will be applied at least by T2S-In CSDs for their intra- and cross-CSD payments.

On the 16th PBD, but at the latest before the start of the 18th PBD, the CSD will create PFOD
instructions to deliver the cash amounts to its participants that shall be credited with penalties.

The intra-CSD PFOD instructions will be created as ‘already matched’ (if this functionality does exist
in the CSD). Upon settlement, these PFODs will debit the CSD´s dedicated penalties cash account
and credit the CSD participants´ relevant cash accounts.

Note: With the use of the PFOD instructions, the rules of the Settlement platform will be applied
(i.e. recycling, reporting or other relevant rules).



10.3.3  Payment via a payment bank
CSDs may outsource the penalties payment process to a third party acting as a payment bank.
Credits to the CSD participants will take place only if the payments due have been ) collected on
the 18th PBD.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                         74 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 76
11 REPORTING


For the purpose of exchanging penalties information between CSDs and their participants
(including those that are CSDs) in a Straight Through Processing fashion, penalties reports content
and formats used by CSDs shall be harmonised. Such an approach will enable all involved parties to
apply a common messaging and communication process, by using ISO reports for Application-to-
Application (A2A) message exchanges.

This is especially relevant in the context of cross-CSD settlement and customers being participants
of multiple CSDs.

Proprietary solutions to report penalties may be used by CSDs as additional (User-to-Application;
U2A) communication means63, for example to support participants´ demand or address market-
specific aspects.

This Framework section focuses on providing a high-level overview of the information to be
provided in the respective messages and reports.

However,  the  specifications  agreed  with and made  available  by  the  standards-setting
organisations, like SWIFT, apply.

It is recommended that the CSDs provide a ‘global net amount’ per counterparty CSD in their
monthly reports on the 14th PBD. Otherwise, PFODs shall be generated by CSDs prior to the 18th PBD
serving to timely notify the ‘global net’ amount to be debited from/ credited to the CSD
participants.

As PFOD instructions and/ or the monthly penalties reports will contain the ‘net amount’ due to be
paid or received by a participant, no dedicated payment pre-advices per currency will be issued by
the CSDs.

In case of penalties removal, re-integration and/ or  re-calculation, the net penalties per
counterparty and currency provided in the previous daily reports will not be updated (recalculated)
but reflected in the ‘amended’ penalties report; however, the penalty updates will be considered
for the calculation of the monthly penalty amounts.

Please also refer to Annex IV for illustrative examples in relation to the daily and monthly reporting.


11.1  REPORTING FORMATS

CSDs should use either the ISO20022 and/ or ISO15022 messages, when available.





63 For the exceptional cases where a CSD may use other standards, please refer to the ESMA Questions and Answers to the CSDR on
article 35, CSD Question 4 (a) under the conduct of business rules. The document can be found here:
https://www.esma.europa.eu/press-news/esma-news/esma-updates-csdr-qas-0



DRAFT V7.0 – Publicly available to relevant stakeholders                                                           75 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 77
This section describes penalty reports, as well as subsequent cash payment-related messages.

11.1.1   ISO20022 messages

T2S/ 4CB is created dedicated daily and monthly penalties ISO20022 customized T2S semt.044
messages.

For the ISO20022 format, a Pillar III semt.044 message dedicated to penalty messaging are used.
The features of this message are as follows:

    ▪    It is a message dedicated to penalty reporting and its peculiarities (new information fields);

    ▪    It uses the most recent ISO standard in XML format;

    ▪    It has hierarchical blocks, repetitive for every party. These repetitive party blocks will
       contain repetitive blocks for counterparties, with the specific penalties’ information
        (report->party->counterparty->penalty). These repetitive blocks might ease the processing
       of reports further down the line as they will already contain the needed block of
       information; and

    ▪  The proposed message contains fields going beyond the potential group of mandatory
         fields and can possibly accommodate also optional and additional fields if needed.

The penalties amounts contain a ‘credit’ (for amounts to be received by the CSD participant) or
‘debit’ (for amounts to be paid by the CSD participant) indicator.



11.1.2   ISO15022 messages

11.1.2.1   Penalties calculation reporting:

Based on the T2S ISO20022 messages content and structure, the existing ISO15022 messages
MT537 and MT548 64 were adapted by SWIFT in November 2019 to cover penalties-related
information by introducing a ‘PENA’ sequence. However, the MT548 is only usable for the reporting
of daily penalties but not the monthly aggregated reporting.

The SWIFT SMPG provided a detailed market practice for the use of ISO 15022 MT537 and ISO 20022
semt.044 penalties messages (see Annex II, item 4 of this Framework document), i.e. no additional
mapping (in case messages received in ISO20022 need to be processed in ISO15022 or vice versa)
on message fields level is provided by SWIFT.

The following development of the standard was agreed by the SWIFT SMPG:





64 The adapted MT message were made available in November 2019. Please refer to the SMPG, Standards MT Release November 2019,
Settlement and Reconciliation; the following Change Requests relevant to the CSDR Settlement Discipline were implemented: CR
001449, CR 001446, CR 001463, CR 001447.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                        76 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 78
    ▪  MT537 (Statement of transactions) and MT548 (Securities Settlement Status Advice)
       adaptations to contain a dedicated new ‘PENA’ sequence specific to the penalties
        reporting, in order to avoid any rejection of a ‘standard’ MT537 or MT548 received after the
       settlement of the transaction.

    ▪  The MT537/ 548 ‘PENA’ messages will include new fields and repetitive blocks containing
       information such as:

             -   late matching/ settlement fail;

             -   reporting of underlying transaction;

             -   penalty ID;

             -   credit/debit indicators;

             -   calculation parameter references.

      The new fields correspond to the new ISO20222 message in their content and level,
       although there might be alternative approaches to the content of some fields if the nature
       of the field requires it.

    ▪  The penalties amounts contain an ‘N’ (debit) indicator for amounts to be paid by the CSD
        participant.

11.1.2.2   Penalties collection and redistribution (payments) reporting:

Unless a PFOD payment process is applied (see Chapter 10) or the ‘monthly report’ already displays
the ‘global net’ amount to be paid or received by a CSD participant, CSDs shall inform their
participants of the actual amounts (debit or credit) of the penalties via a dedicated ‘payment pre-
advice’ (using cash or settlement messages or proprietary communication means, whichever the
CSD deems more appropriate).

Payment pre-advices for amounts to be paid or received shall be issued on the 16th PBD and latest
prior to the 18th PBD; no payment confirmations are required to be issued once the payment has
been executed.

For further details, see Chapter 11.3.3.



11.1.3   Alternative reporting solutions
In addition to the above-mentioned messages, CSDs may develop User to Application (U2A)
interfaces or alternative forms of penalties related to reporting for the benefit of their
participants.

For U2A, formats other than XML (i.e. csv, xls, xlsx) might be used.

Baseline reporting solutions are however ISO15022 or ISO20022 messages, which represent the
minimum and mandatory reporting to be offered by all CSDs to their participants.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                            77 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 79
11.2 GENERIC REPORTING CONTENT

11.2.1   Information blocks for penalty reporting

The corresponding SWIFT ISO messages described in Chapter 11.1 refer to the content of relevant
information fields.

However, in order to harmonise the interpretation of the relevant fields on a pan-European level,
the intended hierarchy and content of those fields are described below.

The penalty reports have a hierarchical structure wherein the level within the hierarchy indicate:

    ▪   Level of aggregation;
    ▪  Reporting element.

These levels, in technical terms, correspond to repetitive blocks within the reports, regardless of
which ISO format is used.

This way, the high-level report consists of repetitive blocks, each one representing an individual
reporting segment/ level:

T - Technical level

This type of data is of a technical nature stating the specifics of a report. This sort of information -
being metadata and being, therefore, mandatory for every produced report - falls not strictly within
the hierarchical division of provided information.

A - Report issuer level (If the non-T2S CSD itself manages the calculation process, then this level
becomes obsolete).

This level of information provided refers to high-level reports or master reports which are available
to CSDs (either produced by themselves or by third parties as in the case of the T2s Penalty
Mechanism).

B - Participant level

This level of reporting states information relating to a specific participant (be it a participant, CCP,
Investor-CSD or other).

C - Counterparty/ Penalty level

At this level, a specific participant is informed within the positions against specific counterparties
about the actual penalties. This applies to daily reports, as well as monthly reports with the details
at penalty and transaction level.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       78 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 80
11.2.2  Mandatory fields

Mandatory fields ensure that the recipient of a penalty report will always be able to identify a failing
settlement instruction subject to a penalty, i.e. even though he would have to use information from
his internal sources. Mandatory fields have to comply with the mapping standards of the penalty
reporting.

For example, a penalty report recipient would be informed about the amount of a penalty. In order
to identify the settlement instruction, the recipient would need to know:

    ▪   Instruction/ transaction ID;
    ▪  Day for which the penalty was computed.

In order to understand the penalty, the recipient would need65:

    ▪   Security penalty rate and/ or the penalty Central Bank cash discount rate for the currency;
    ▪  SME Growth Market indicator (only for those settlement fails where the transaction was
        actually concluded on an SME Growth Market trading venue and the same SME Trading
      venue MIC code is used in the receiving and delivering settlement instruction);
    ▪   Liquidity indicator (for shares); and
    ▪  Number of securities to which the penalty applies (in case of partial settlements).

Thereby it is made sure that in a cross-CSD context, the receiving CSD will always be able to allocate
the penalty correctly to its underlying participants.

Penalties and penalty aggregates in penalty reports will be always reported in the currency in which
the penalty amounts were calculated, i.e. no conversion will take place except for the possible
conversion during the calculation process (see Chapters 6 and 7.4).



11.3 MESSAGE TYPES
There are several types of reporting on penalties throughout the month (see Chapter 2):

     1.   Daily reporting of new and/ or updated/ modified penalties;

     2.  Monthly aggregated reporting of the penalties over the period;

    3.  Payment pre-advices via cash or settlement messages or proprietary communication
      means (pre-advices may not be issued when the CSD applies the PFOD payment process or
       the ‘monthly report’ already displays the ‘global net’ amount to be paid or received by a
      CSD participant).





65 Note that the ‘reference price’ as well as the price source used by the CSD for the penalty calculation for the failing instrument will
not be displayed; the respective message field, if part of the report, may be blank or contain ‘NONREF’ or similar information.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                        79 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 81
11.3.1   Daily penalties report

Daily penalties are computed for and reported to the relevant failing and non-failing party. The
CSD will hence report twice each penalty computed:

     1.  The one applicable to the failing party (i.e. party imposed with the penalty), and

     2.  The one applicable to the non-failing party (i.e. party entitled to receive the penalty).

The failing party and the non-failing party are the two counterparts instructing the settlement
transaction and consequently the respective owner of the involved securities account.

It shall be noted that in case of a ‘cross-CSD scenario’ (see Chapter 9), the CSD will consider the
other involved CSD as the owner of the relevant securities account of the underlying settlement
instruction.

Within the messages:

       ▪  The party is a repetitive block in order to be able to include all the information in a single
          message. The CSD shall report cash penalties for a given party sorted by CSD (for cross-
         CSD fails), currency, and counterparty of the penalty (i.e. non-failing or failing party,
            respectively).
       ▪  Each penalty computed for a given business day and reported to the failing/ non-failing
           party and/ or its CSD shall include the information described in Chapter 11.2.
       ▪    It  is understood that an individual penalty contained in the report of a specific
            participant will have a mirror entry (debit vs. credit) in the penalty report of the relevant
           counterparty, i.e. will be on the participant level reported in two penalty reports.
       ▪  The daily reports contain only the amounts and information for a specific business day,
                i.e. they do not reflect exposures accrued in the course of several fail days.

Note that T2S and SWIFT confirmed on 26.03.2019 the availability of the information listed in these
bullets in the foreseen ISO20022 semt.044 and ISO15022 MT537/ 548 messages.



11.3.2  Monthly aggregated report
On the 14th PBD of the following month, CSDs shall provide the monthly aggregated penalties
report (see Chapter 7 ).

This report shall include, per CSD, currency and party, the bilateral and ‘global’ (when applied by
the CSD, see Chapter 7.4.2) net amounts of the penalties against each of its counterparties,
computed for all the business days of the previous month.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                   80 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 82
11.3.3  Payment pre-advices

In regard to the timeline of the collection and redistribution process, the payment pre-advice (if
applicable) is to be issued by the CSD on the 16th PBD of the following month66.

Besides proprietary communication tools that a CSD may use to report the net amount to be paid/
redistributed, the following reporting options apply:

11.3.3.1  Cash messages

For the cash messages, the mandatory fields are:

    ▪  Cash Account number of the participant (including CSDs) to be debited or credited;
    ▪  Cash Account number of the CSD dedicated to the penalties management (if applicable);
    ▪  Amount to be paid (= debit amount)/ Amount to be received (= credit amount);
    ▪   Currency;
    ▪   Value date of relevant payment; and
    ▪   Free text (payment reference, reference to the penalty process, or other).

As indicated, a payment pre-advice message will contain only one amount. That means that the
CSD will send out to every participant payment pre-advices only in case there are payments to be
processed and, for any of the two possible payment directions (debit and credit), there will be a
dedicated pre-advice (i.e. a payment pre-advice message can contain only a credit or a debit
amount, but not both).

11.3.3.2  Settlement messages
Various settlement messages can be used to report the net amount to be received/ paid, such as
the following:

    ▪  Settlement instructions;
    ▪  Statement of transactions;
    ▪   Status advice etc.

Settlement messages will be sent for both, the debit and credit amounts.

The Settlement message may contain one or several amounts depending on the type of message
to be used (i.e. a statement may contain several amounts).





66 Note that payment pre-advice messages are not (e-)invoices. Therefore, they shall not contain the elements listed in Article 6 of EC
Directive 2014/55/EU as not to be perceived as such.




DRAFT V7.0 – Publicly available to relevant stakeholders                                                              81 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 83
12 MISCELLANEOUS


12.1  PENALTIES ACTIVATION PROCESS
This section was removed as the penalty mechanisms of all EU/ EEA CSDs were activated since 01
February 2022.



12.2 EXCEPTIONS HANDLING

12.2.1  Delayed delivery of CSD penalties reports

In case a CSD cannot deliver a scheduled report on time (see Chapter 2), it shall inform its
participants as soon as possible about this temporary operational disruption via the standard CSD
customer communication means (the same applies in case of delayed payment processing).



12.2.2  Exceptional situations where the cash penalties should not be applied
In addition to situations where insolvency proceedings are opened against the failing participant,
cash penalties should not be applied in the following situations where settlement cannot be
performed for reasons that are independent from the involved participants:

            i.    ISIN suspension from settlement due to an ‘undue creation/ deletion of securities’
            reconciliation break;
           ii.    ISIN suspension from trading67;
           iii.   Settlement instructions involving cash settlement outside the securities settlement
          system operated by the CSD if, on the respective day, the relevant payment system is
           closed for settlement;
       iv.    Technical impossibilities at the CSD level that prevent settlement, such as: a failure of
          the infrastructure components, a cyber-attack, network problems.

Note: in all or some occasions, penalties may continue to be calculated and reported by the CSD
but removed afterwards. Also note that suspension of an ISIN from settlement does not impact
the principle eligibility of the ISIN for SDR penalties application, hence, penalties will continue to
be calculated and reported by the CSD(s) and removed afterwards.





67 While this is stated in the ESMA Q&As, ESMA advised ECSDA this is not meant to be mandatory but a non-exhaustive example for
cases when CSD may not need to apply penalties. In this specific case, CSDs are usually not aware of the suspension taking place at
trading level, hence, will not waive any penalties that were calculated.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                        82 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 84
According to the ESMA Q&As, CSDs should report the concrete cases falling in the above-
mentioned categories to their competent authorities who may ask the CSDs to apply cash penalties
in the future in similar cases if they consider the non-application of penalties unjustified.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      83 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 85
12.3 CCP Related Aspects

This section was removed as the CCP-penalties are processed in the same way as any other
penalties, since September 2024.





DRAFT V7.0 – Publicly available to relevant stakeholders                                                     84 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 86
  ANNEXES


ANNEX I- T2S DOCUMENTS

     1.  T2S CR654:

https://www.ecb.europa.eu/paym/target/t2s/governance/html/changerequests.en.html



     2.  Penalty lists – Draft message (ISO 20022) overview (updated version 04 March 2020)



T2S_0654_URD_Ann
ex 5a_semt_044_001_



    3.  Latest list of T2S CSDR TF items for clarification sent to ESMA:



2017-06-28 - List of
CSDR Items for clarif




ANNEX II - OTHER DOCUMENTS AND REFERENCES


     1.  Link to ESMA website re. CSDR:

https://www.esma.europa.eu/regulation/post-trading/settlement



     2.  CFI code mapping table (ECSDA version dd. October 2020 as shared with ESMA):



    2020_10_21
-CSDR_CFI_code_map





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       85 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 87
    3.  SWIFT SMPG Market Practice for penalties reporting and penalties adjustments reason
       codes (status codes ‘ACTV’ or ‘REMO’ to be used with the reason code to be provided as
        ‘additional information’):
       https://www.smpg.info/fileadmin/documents/3_Settlement%20and%20Reconciliation%20
       WG/A_Final%20Global%20Market%20Practices/SMPG_MP_SR_CSDR_Penalties_reporting.p
       df


             a.  Reason codes for penalty removal (as proposed by T2S, 08.04.2019, based on
          ESMA CSDR Q&A section ‘Settlement Discipline Questions 4 – Cash penalties:
                scope’):
                                    i.  INSO – Insolvency
                                    ii. SESU – Settlement Suspended
                                    iii. SUSP – Trading status suspended
                         iv. SEMP - Settlement on multiple platforms (applies in case the cash
                     settlement is outside the CSD settlement system and the payment system
                               is closed)
                       v.  TEIM (ISO 15022)/ TECH (ISO 20022) – Technical impossibilities
                         vi. OTHR – any other case (requires a narrative text to be added)
            b.  Reason code for penalty recalculation or re-inclusion:
                                    i. UPDT – update of a penalty due to change in the relevant reference data
                      or penalty re-inclusion.
              c.  Reason code for penalty re-allocation:
                                    i. RALO - re-allocation of a penalty from the instructing party to the
                        delivering/ receiving party or from the failing party to the non-failing party
                      or vice versa.


ANNEX III - SETTLEMENT PENALTIES SCENARIOS (EXCLUDING SCENARIO 2X)




  Doc1 - Non-T2S    Doc2 -T2S CSDR
CSDR SD penalties s SDR scenarios- upda





DRAFT V7.0 – Publicly available to relevant stakeholders                                                    86 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 88
ANNEX IV – PENALTIES AMOUNTS REPORTING – ILLUSTRATIVE EXAMPLES68


      1.  Daily reporting

- Gross penalties calculated on a daily basis

        CSD   Party  CSD  Counterparty  Currency   Penalties  Comment

 Inx 1       I     A         I    B          EUR       -100       Intra-CSD

 Inx 1       I     B          I    A          EUR      +100      Intra-CSD

 Inx 2       I     A         I    B          EUR      +50       Intra-CSD

 Inx 2       I     B          I    A          EUR       -50        Intra-CSD

 Inx 3       I     A         I    C          EUR       -20        Intra-CSD

 Inx 3       I     C          I    A          EUR      +20       Intra-CSD

 Inx 4      I     A         I    C          DKK      +10        Intra-CSD

 Inx 4      I     C          I    A          DKK        -10        Intra-CSD

 Inx 5       I     A         II    Unknown    DKK        -10        Cross-CSD (PSET CSD I)

 Inx 5       II     B          I    A          DKK      +10       Cross-CSD (PSET CSD I)

 Inx 6      I     A         II    Unknown    DKK      +20       Cross-CSD (PSET CSD I)

 Inx 6      II     B          I    A          DKK       -20       Cross-CSD (PSET CSD I)

 Inx 7       I     B          I    A          EUR      +150       Intra-CSD

 Inx 7       I     A         I    B          EUR       -150       Intra-CSD

 Inx 8      I     B          I    C          EUR        -25        Intra-CSD

 Inx 8      I     C          I    B          EUR      +25        Intra-CSD

 Inx 9      I     C          II    B          EUR      +250      Cross-CSD (PSET CSD II)

 Inx 9      II     B          I    Unknown    EUR       -250      Cross-CSD (PSET CSD II)

 Inx 10     I     C          II   D          EUR       -300      Cross-CSD (PSET CSD II)

 Inx 10     II    D         I    Unknown    EUR      +300      Cross-CSD (PSET CSD II)

 Inx 11      I     A         I    A          DKK      +625      Intra-CSD

 Inx 11      I     A         I    A          DKK       -625       Intra-CSD

 Inx 12     I     B          III   Unknown    EUR      +28       Cross-CSD (PSET CSD I)

 Inx 12     III    C          I    B          EUR       -28       Cross-CSD (PSET CSD I)

 Inx 13     I     B          III   B          EUR       -49       Cross-CSD (PSET CSD III)

 Inx 13     III    B          I    Unknown    EUR      +49       Cross-CSD (PSET CSD III)





68 The scenarios were enriched to cover as well the T2S platform as PSET.



DRAFT V7.0 – Publicly available to relevant stakeholders                                                       87 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 89
 Inx 14     I     A         II    C          DKK      +23       Cross-CSD (PSET II)

 Inx 14     II     C          I    Unknown    DKK        -23        Cross-CSD (PSET II)

 Inx 15    IV     E     V    Unknown    EUR        -10        Cross-CSD (PSET T2S)

 Inx15   V     F       IV   Unknown    EUR       +10       Cross-CSD (PSET T2S)

 Inx16    IV    G     V    Unknown    EUR      +25       Cross-CSD (PSET T2S)

 Inx16   V     F       IV   Unknown    EUR        -25        Cross-CSD (PSET T2S)

 Inx17   V    H      VI   Unknown    EUR      +7        Cross-CSD (PSET T2S)

 Inx17    VI         I     V    Unknown    EUR        -7         Cross-CSD (PSET T2S)

 Inx18    IV     E     V    Unknown    EUR      +50       Cross-CSD (PSET T2S)

 Inx18   V     F       IV   Unknown    EUR       -50       Cross-CSD (PSET T2S)



- Daily bilateral net amount per CSD, per currency & per counterparty (view per CSD participant)

   For party A in CSD I

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  I      A         I     B           EUR       -200        Intra-CSD

  I      A         I     C           EUR        -20         Intra-CSD

  I      A         I     C           DKK       +10        Intra-CSD

  I      A         II     Unknown     DKK       +10        Cross-CSD (PSET CSD I)

  I      A         I     A           DKK      0          Intra-CSD

  I      A         II     C           DKK       +23        Cross-CSD (PSET II)

       For party B in CSD I

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  I      B          I     A           EUR      +200       Intra-CSD

  I      B          I     C           EUR        -25         Intra-CSD

  I      B          III    Unknown     EUR       +28        Cross-CSD (PSET CSD I)

  I      B          III    B           EUR       -49        Cross-CSD (PSET CSD III)

       For party B in CSD II

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  II      B          I     A           DKK         -10        Cross-CSD (PSET CSD I)

  II      B          I     Unknown     EUR        -250       Cross-CSD (PSET CSD II)

       For party B in CSD III

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  III     B          I     Unknown     EUR      +49        Cross-CSD (PSET CSD III)





DRAFT V7.0 – Publicly available to relevant stakeholders                                                   88 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 90
       For party C in CSD I

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  I      C          I     A           EUR       +20        Intra-CSD

  I      C          I     A           DKK         -10         Intra-CSD

  I      C          I     B           EUR       +25        Intra-CSD

  I      C          II     B           EUR       +250       Cross-CSD (PSET CSD II)

  I      C          II    D           EUR       -300       Cross-CSD (PSET CSD II)

       For party C in CSD II

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  II      C          I     Unknown     DKK        -23        Cross-CSD (PSET II)

       For party C in CSD III

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  III     C          I     B           EUR        -28        Cross-CSD (PSET CSD I)

       For party D in CSD II

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

  II     D         I     Unknown     EUR      +300      Cross-CSD (PSET CSD II)

       For party E in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV      E     V     Unknown     EUR      +40        Cross-CSD (PSET T2S)

       For party F in CSD V

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 V       F       IV    Unknown     EUR        -65        Cross-CSD (PSET T2S)

       For party G in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV     G     V     Unknown     EUR       +25        Cross-CSD (PSET T2S)

       For party H in CSD V

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 V     H      VI    Unknown     EUR       +7         Cross-CSD (PSET T2S)

       For party I in CSD VI

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 VI           I     V     Unknown     EUR         -7         Cross-CSD (PSET T2S)




DRAFT V7.0 – Publicly available to relevant stakeholders                                                    89 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 91
- Daily bilateral net amount per CSD, per currency & per counterparty (view per CSD):

      CSD I

 CSD    CSD   Currency   Penalties  Comment

  I             I     EUR      0          Intra-CSD

  I             I     DKK      0          Intra-CSD

  I             II    EUR        -50        Cross-CSD (PSET CSD II)

  I             II    DKK       +10        Cross-CSD (PSET CSD I)

  I             II    DKK       +23        Cross-CSD (PSET II)

  I             III    EUR       +28        Cross-CSD (PSET CSD I)

  I             III    EUR        -49        Cross-CSD (PSET CSD III)

      CSD II

 CSD    CSD   Currency   Penalties  Comment

  II            I     DKK         -10        Cross-CSD (PSET CSD I)

  II            I     DKK        -23        Cross-CSD (PSET II)

  II            I     EUR      +50        Cross-CSD (PSET CSD II)

      CSD III

 CSD    CSD   Currency   Penalties  Comment

  III           I     EUR      +49        Cross-CSD (PSET CSD III)

  III           I     EUR        -28        Cross-CSD (PSET CSD I)

   CSD IV

 CSD    CSD   Currency   Penalties  Comment

 IV     V    EUR      +65        Cross-CSD (PSET T2S)

   CSD V

 CSD    CSD   Currency   Penalties  Comment

 V        IV    EUR        -65        Cross-CSD (PSET T2S)

 V        VI    EUR       +7         Cross-CSD (PSET T2S)

   CSD VI

 CSD    CSD   Currency   Penalties  Comment

 VI     V    EUR         -7         Cross-CSD (PSET T2S)



    2.  Monthly reporting




DRAFT V7.0 – Publicly available to relevant stakeholders                                                   90 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 92
- Daily bilateral amounts of the business days of the month (view per CSD participant)

 BD     CSD   Party  CSD   Cpty         Curr.    Penalties  Comment

 Day 1      I     A         I     B         EUR     -200        Intra-CSD

 Day 1      I     B          I     A         EUR    +200       Intra-CSD

 Day 1      I     A         I     C         EUR     -20         Intra-CSD

 Day 1      I     C          I     A         EUR    +20        Intra-CSD

 Day 1      I     A         I     C         DKK    +10        Intra-CSD

 Day 1      I     C          I     A         DKK     -10         Intra-CSD

 Day 1      I     A         II     Unknown   DKK    +10        Cross-CSD (PSET CSD I)

 Day 1      II     B          I     A         DKK     -10        Cross-CSD (PSET CSD I)

 Day 1      I     A         I     A         DKK    0          Intra-CSD

 Day 1      I     A         II     C         DKK    +23        Cross-CSD (PSET II)

 Day 1      II     C          I     Unknown   DKK     -23        Cross-CSD (PSET II)

 Day 1      I     B          I     C         EUR     -25         Intra-CSD

 Day 1      I     C          I     B         EUR    +25        Intra-CSD

 Day 1      I     B          III    Unknown   EUR    +28        Cross-CSD (PSET CSD I)

 Day 1      III    C          I     B         EUR     -28        Cross-CSD (PSET CSD I)

 Day 1      I     B          III    B         EUR     -49        Cross-CSD (PSET CSD III)

 Day 1      III    B          I     Unknown   EUR    +49        Cross-CSD (PSET CSD III)

 Day 1      II     B          I     Unknown   EUR     -250       Cross-CSD (PSET CSD II)

 Day 1      I     C          II     B         EUR    +250       Cross-CSD (PSET CSD II)

 Day 1      I     C          II    D         EUR    -300       Cross-CSD (PSET CSD II)

 Day 1      II    D         I     Unknown   EUR    +300      Cross-CSD (PSET CSD II)

 Day 3      I     A         I     D         EUR     -200        Intra-CSD

 Day 3      I     D         I     A         EUR    +200       Intra-CSD

 Day 3      I     A         II     Unknown   DKK     -23        Cross-CSD (PSET CSD I)

 Day 3      II     B          I     A         DKK    +23        Cross-CSD (PSET CSD I)

 Day 3      I     B          I     C         EUR    +18        Intra-CSD

 Day 3      I     C          I     B         EUR     -18         Intra-CSD

 Day 3      I     B          III    Unknown   EUR     -62        Cross-CSD (PSET CSD I)

 Day 3      III    B          I     B         EUR    +62        Cross-CSD (PSET CSD I)

 Day 3      I     C          II    D         EUR    -300       Cross-CSD (PSET CSD II)

 Day 3      II    D         I     Unknown   EUR    +300      Cross-CSD (PSET CSD II)

 Day 5      I     A         I     C         DKK    +10        Intra-CSD

 Day 5      I     C          I     A         DKK     -10         Intra-CSD

 Day 5      I     B          I     A         EUR     -47         Intra-CSD





DRAFT V7.0 – Publicly available to relevant stakeholders                                                              91 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 93
 Day 5      I     A         I     B         EUR    +47        Intra-CSD

 Day 10    I     A         I     B         EUR    +2500      Intra-CSD

 Day 10    I     B          I     A         EUR    -2500      Intra-CSD

 Day 10    I     A         I     C         EUR    -480       Intra-CSD

 Day 10    I     C          I     A         EUR    +480       Intra-CSD

 Day 10    I     A         I     C         DKK    +67        Intra-CSD

 Day 10    I     C          I     A         DKK     -67         Intra-CSD

 Day 10    I     A         II     Unknown   DKK     -19        Cross-CSD (PSET CSD I)

 Day 10    II     B          I     A         DKK    +52        Cross-CSD (PSET CSD I)

 Day 10    II    D         I     A         DKK     -33        Cross-CSD (PSET CSD I)

 Day 10    I     A         I     A         DKK    0          Intra-CSD

 Day 10    I     A         II     C         DKK     -857       Cross-CSD (PSET CSD II)

 Day 10    II     C          I     Unknown   DKK    +857       Cross-CSD (PSET CSD II)

 Day 10    I     B          III    Unknown   EUR    +2368     Cross-CSD (PSET CSD I)

 Day 10    III    B          I     B         EUR    -2368      Cross-CSD (PSET CSD I)

 Day 10    I     B          III    B         EUR     -56        Cross-CSD (PSET CSD III)

 Day 10    III    B          I     Unknown   EUR    +56        Cross-CSD (PSET CSD III)

 Day 10    I     C          II    A         EUR     -475       Cross-CSD (PSET CSD II)

 Day 10    II    A         I     Unknown   EUR    +475       Cross-CSD (PSET CSD II)

 Day 10    I     C          II     B         EUR     -587       Cross-CSD (PSET CSD II)

 Day 10    II     B          I     Unknown   EUR    +587       Cross-CSD (PSET CSD II)

 Day 15    I     A         II    D        DKK    +70        Cross-CSD (PSET CSD II)

 Day 15    I     B          II    D        DKK     -45        Cross-CSD (PSET CSD II)

 Day 15    II    D         I     Unknown   DKK     -25        Cross-CSD (PSET CSD II)

 Day 15    I     A         I     D         EUR     -65         Intra-CSD

 Day 15    I     D         I     A         EUR    +65        Intra-CSD

 Day 15    I     A         I     B         EUR    +100       Intra-CSD

 Day 15    I     B          I     A         EUR     -100        Intra-CSD

 Day 22    I     A         I     C         EUR    +20        Intra-CSD

 Day 22    I     C          I     A         EUR     -20         Intra-CSD

 Day 22    I     A         II     B         DKK     -50        Cross-CSD (PSET CSD II)

 Day 22    II     B          I     Unknown   DKK    +50        Cross-CSD (PSET CSD II)

 Day 22    I     A         II     Unknown   EUR     -356       Cross-CSD (PSET CSD I)

 Day 22    II    D         I     A         EUR    +356       Cross-CSD (PSET CSD I)

 Day 1    IV     E     V     Unknown   EUR    +40        Cross-CSD (PSET T2S)

 Day 1   V     F       IV    Unknown   EUR     -65        Cross-CSD (PSET T2S)

 Day 1    IV    G     V     Unknown   EUR    +25        Cross-CSD (PSET T2S)




DRAFT V7.0 – Publicly available to relevant stakeholders                                                        92 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 94
 Day 1   V    H      VI    Unknown   EUR    +7         Cross-CSD (PSET T2S)

 Day 1    VI         I     V     Unknown   EUR      -7         Cross-CSD (PSET T2S)

 Day 15  V     F       IV    Unknown   EUR     -100       Cross-CSD (PSET T2S)

 Day 15   IV    G     V     Unknown   EUR    +100       Cross-CSD (PSET T2S)

 Day 22   VI         I     V     Unknown   EUR    +30        Cross-CSD (PSET T2S)

 Day 22  V     F       VI    Unknown   EUR     -30        Cross-CSD (PSET T2S)



- Monthly bilateral net amount per CSD, per currency & per counterparty (view per CSD)

      CSD I

 CSD   CSD    Curr    Penalties        Comment

  I            I      EUR   0                  Intra-CSD

  I            I      DKK   0                  Intra-CSD

  I            II     EUR    -356              Cross-CSD (PSET CSD I)

  I            II     DKK     -32                Cross-CSD (PSET CSD I)

  I            II     EUR     -1412              Cross-CSD (PSET CSD II)

  I            II     DKK    -859              Cross-CSD (PSET CSD II)

  I            III     EUR    +2334             Cross-CSD (PSET CSD I)

  I            III     EUR    -105               Cross-CSD (PSET CSD III)

      CSD II

  II           I     EUR     +356            Cross-CSD (PSET CSD I)

  II           I     EUR      +1412            Cross-CSD (PSET CSD II)

  II           I     DKK     +32              Cross-CSD (PSET CSD I)

  II           I     DKK     +859            Cross-CSD (PSET CSD II)

      CSD III

 CSD    CSD     Curr     Penalties     Comment

  III           I      EUR    +105           Cross-CSD (PSET CSD III)

  III           I      EUR    -2334          Cross-CSD (PSET CSD I)

      CSD IV

 CSD   CSD    Curr    Penalties        Comment

 IV     V     EUR    +165              Cross-CSD (PSET T2S)

      CSD V

 CSD   CSD    Curr    Penalties        Comment

 V       IV     EUR    -165               Cross-CSD (PSET T2S)





DRAFT V7.0 – Publicly available to relevant stakeholders                                                      93 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 95
 V       VI     EUR     -23                Cross-CSD (PSET T2S)

      CSD VI

 CSD   CSD    Curr    Penalties        Comment

 VI     V     EUR    +23               Cross-CSD (PSET T2S)



- Monthly bilateral net amount per CSD, per currency & per counterparty (view per CSD
participant)

       For party A in CSD I

 CSD    Party  CSD    Cpty       Curr    Penalties        Comment

  I     A         I      B       EUR    +2447              Intra-CSD

  I     A         I      C        EUR    -480               Intra-CSD

  I     A         I      C       DKK    +87                Intra-CSD

  I     A         II     Unknown  DKK     -32                Cross-CSD (PSET CSD I)

  I     A         I     A       DKK   0                  Intra-CSD

  I     A         II      C       DKK    -834              Cross-CSD (PSET CSD II)

  I     A         I     D       EUR    -265               Intra-CSD

  I     A         II     D       DKK    +70               Cross-CSD (PSET CSD II)

  I     A         II     B       DKK    -50               Cross-CSD (PSET CSD II)

  I     A         II     Unknown  EUR    -356              Cross-CSD (PSET CSD I)

       For party A in CSD II

  II     A           I      Unknown    EUR     +475        Cross-CSD (PSET CSD II)

       For party B in CSD I

 CSD     Party  CSD    Cpty       Curr     Penalties     Comment

  I      B         I      A       EUR    -2447           Intra-CSD

  I      B         I      C        EUR     -7              Intra-CSD

  I      B          III     Unknown  EUR    +2334         Cross-CSD (PSET CSD I)

  I      B          III     B       EUR     -105           Cross-CSD (PSET CSD III)

  I      B          II     D       DKK     -45            Cross-CSD (PSET CSD II)

       For party B in CSD II

 CSD     Party  CSD    Cpty       Curr     Penalties     Comment

  II     B          I      A       DKK    +65           Cross-CSD (PSET CSD I)

  II     B          I      Unknown  EUR    +337          Cross-CSD (PSET CSD II)

  II     B          I      Unknown  DKK    +50           Cross-CSD (PSET CSD II)





DRAFT V7.0 – Publicly available to relevant stakeholders                                                     94 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 96
       For party B in CSD III

 CSD     Party  CSD    Cpty       Curr     Penalties     Comment

  III     B         I      Unknown  EUR    +105           Cross-CSD (PSET CSD III)

  III     B         I      B       EUR    -2306          Cross-CSD (PSET CSD I)

       For party C in CSD I

 CSD     Party  CSD    Cpty    Curr     Penalties     Comment

  I      C          I      A     EUR    +480           Intra-CSD

  I      C          I      A     DKK     -87             Intra-CSD

  I      C          I      B     EUR    +7              Intra-CSD

  I      C          II      B     EUR     -337           Cross-CSD (PSET CSD II)

  I      C          II     D     EUR    -600           Cross-CSD (PSET CSD II)

  I      C          II     A     EUR     -475           Cross-CSD (PSET CSD II)

       For party C in CSD II

 CSD     Party  CSD    Cpty       Curr     Penalties     Comment

  II      C          I      Unknown  DKK    +834          Cross-CSD (PSET CSD II)

       For party C in CSD III

 CSD     Party  CSD    Cpty    Curr     Penalties     Comment

  III     C          I      B     EUR     -28            Cross-CSD (PSET CSD I)

       For party D in CSD I

 CSD     Party  CSD    Cpty    Curr     Penalties     Comment

  I      D         I      A     EUR    +265           Intra-CSD

       For party D in CSD II

 CSD     Party  CSD    Cpty       Curr     Penalties     Comment

  II     D         I      Unknown  EUR    +600          Cross-CSD (PSET CSD II)

  II     D         I      A       DKK     -33            Cross-CSD (PSET CSD I)

  II     D         I      Unknown  DKK     -25            Cross-CSD (PSET CSD II)

  II     D         I      A       EUR    +356          Cross-CSD (PSET CSD I)

       For party E in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV      E     V     Unknown     EUR      +40        Cross-CSD (PSET T2S)

       For party F in CSD V





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       95 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 97
 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 V       F       IV    Unknown     EUR        -165       Cross-CSD (PSET T2S)

 V       F       VI    Unknown     EUR        -30        Cross-CSD (PSET T2S)

       For party G in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV     G     V     Unknown     EUR       +125       Cross-CSD (PSET T2S)

       For party H in CSD V

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 V     H      VI    Unknown     EUR       +7         Cross-CSD (PSET T2S)

For party I in CSD VI

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 VI           I     V     Unknown     EUR       +23        Cross-CSD (PSET T2S)



- Monthly amount to be paid or to be received (view per CSD)

      CSD I

 CSD    CSD     Curr     Penalties     Comment

  I             I      EUR    0               Intra-CSD

  I             I      DKK    0               Intra-CSD

  I             II     EUR     -356           Cross-CSD (PSET CSD I)

  I             II     EUR     -1412           Cross-CSD (PSET CSD II)

  I             II     DKK     -32            Cross-CSD (PSET CSD I)

  I             II     DKK    -859           Cross-CSD (PSET CSD II)

  I             III     EUR    +2334          Cross-CSD (PSET CSD I)

  I             III     EUR     -105           Cross-CSD (PSET CSD III)

      CSD II

  II            I      EUR    +356           Cross-CSD (PSET CSD I)

  II            I      EUR     +1412          Cross-CSD (PSET CSD II)

  II            I      DKK    +32            Cross-CSD (PSET CSD I)

  II            I      DKK    +859           Cross-CSD (PSET CSD II)

      CSD III

 CSD    CSD     Curr     Penalties     Comment

  III           I      EUR     -2334          Cross-CSD (PSET CSD I)





DRAFT V7.0 – Publicly available to relevant stakeholders                                                    96 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 98
  III           I      EUR    +105           Cross-CSD (PSET CSD III)

      CSD IV

 CSD    CSD     Curr     Penalties     Comment

 IV     V     EUR    +165           Cross-CSD (PSET T2S)

      CSD V

 CSD    CSD     Curr     Penalties     Comment

 V        IV     EUR     -165           Cross-CSD (PSET T2S)

 V        VI     EUR     -23            Cross-CSD (PSET T2S)

      CSD VI

 CSD    CSD     Curr     Penalties     Comment

 VI     V     EUR    +23            Cross-CSD (PSET T2S)



- Monthly amount to be paid or to be received

       For party A in CSD I

 CSD     Party  CSD     Curr     Penalties     Comment

  I      A         I      EUR    +1702           Intra-CSD

  I      A         I      DKK    +87             Intra-CSD

  I      A         II     EUR     -356           Cross-CSD (PSET CSD I)

  I      A         II     DKK     -32            Cross-CSD (PSET CSD I)

  I      A         II     DKK     -814           Cross-CSD (PSET CSD II)

       For party A in CSD II

  II     A           I      EUR    +475           Cross-CSD (PSET CSD II)

       For party B in CSD I

 CSD     Party  CSD     Curr     Penalties     Comment

  I      B          I      EUR    -2454           Intra-CSD

  I      B          III     EUR    +2334          Cross-CSD (PSET CSD I)

  I      B          II     DKK     -45            Cross-CSD (PSET CSD II)

  I      B          III     EUR     -105           Cross-CSD (PSET CSD III)

       For party B in CSD II

 CSD     Party  CSD     Curr     Penalties     Comment

  II      B          I      DKK    +65            Cross-CSD (PSET CSD I)





DRAFT V7.0 – Publicly available to relevant stakeholders                                                       97 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 99
  II      B          I      EUR    +337           Cross-CSD (PSET CSD II)

  II      B          I      DKK    +50            Cross-CSD (PSET CSD II)

       For party B in CSD III

 CSD     Party  CSD     Curr     Penalties     Comment

  III     B          I      EUR    -2306          Cross-CSD (PSET CSD I)

  III     B          I      EUR    +105           Cross-CSD (PSET CSD III)

       For party C in CSD I

 CSD     Party  CSD     Curr     Penalties     Comment

  I      C          I      EUR    +487           Intra-CSD

  I      C          I      DKK     -87             Intra-CSD

  I      C          II     EUR     -1412           Cross-CSD (PSET CSD II)

       For party C in CSD II

 CSD     Party  CSD     Curr     Penalties     Comment

  II      C          I      DKK    +834           Cross-CSD (PSET CSD II)

       For party C in CSD III

 CSD     Party  CSD     Curr     Penalties     Comment

  III     C          I      EUR     -28            Cross-CSD (PSET CSD I)

       For party D in CSD I

 CSD     Party  CSD     Curr     Penalties     Comment

  I      D         I      EUR    +265           Intra-CSD

       For party D in CSD II

 CSD     Party  CSD     Curr     Penalties     Comment

  II     D         I      EUR    +356           Cross-CSD (PSET CSD I)

  II     D         I      DKK     -33            Cross-CSD (PSET CSD I)

  II     D         I      EUR    +600          Cross-CSD (PSET CSD II)

  II     D         I      DKK     -25            Cross-CSD (PSET CSD II)

       For party E in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV      E     V     Unknown     EUR      +40        Cross-CSD (PSET T2S)

       For party F in CSD V

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment




DRAFT V7.0 – Publicly available to relevant stakeholders                                                   98 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 100
 V       F       IV    Unknown     EUR        -165       Cross-CSD (PSET T2S)

 V       F       VI    Unknown     EUR        -30        Cross-CSD (PSET T2S)

       For party G in CSD IV

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 IV     G     V     Unknown     EUR       +125       Cross-CSD (PSET T2S)

       For party H in CSD V

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 V     H      VI    Unknown     EUR       +7         Cross-CSD (PSET T2S)

For party I in CSD VI

 CSD     Party  CSD   Counterparty   Currency   Penalties  Comment

 VI           I     V     Unknown     EUR       +23        Cross-CSD (PSET T2S)



- As a summary, the amounts to be paid / received are:

 Party    Pay / Receive  Curr.      Penalties      To / From       PSET

 A        Receive     EUR       +1702        CSD I            Intra-CSD

 A        Receive     DKK      +87          CSD I            Intra-CSD

 B        Pay        EUR       -2454        CSD I            Intra-CSD

 C        Receive     EUR      +487         CSD I            Intra-CSD

 C        Pay        DKK       -87          CSD I            Intra-CSD

 D        Receive     EUR      +265         CSD I            Intra-CSD

 CSD I     Pay        EUR       -356         CSD II          PSET CSD I

 CSD I     Pay        EUR        -1412         CSD II          PSET CSD II

 CSD I     Receive     EUR      +2334        CSD III         PSET CSD I

 CSD I     Pay        EUR       -105          CSD III         PSET CSD III

 CSD I     Pay        DKK        -32          CSD II          PSET CSD I

 CSD I     Pay        DKK       -859         CSD II          PSET CSD II

 CSD II    Receive     EUR      +356         CSD I          PSET CSD I

 CSD II    Receive     EUR       +1412         CSD I          PSET CSD II

 CSD II    Receive     DKK      +32          CSD I          PSET CSD I

 CSD II    Receive     DKK      +859         CSD I          PSET CSD II

 CSD III   Pay        EUR       -2334         CSD I          PSET CSD I

 CSD III    Receive     EUR      +105         CSD I          PSET CSD III

 CSD IV    Receive     EUR      +165         CSD V          PSET T2S

 CSD V    Pay        EUR       -165          CSD IV         PSET T2S




DRAFT V7.0 – Publicly available to relevant stakeholders                                                    99 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 101
 CSD V    Pay        EUR        -23          CSD VI         PSET T2S

 CSD VI    Receive     EUR      +23          CSD v          PSET T2S



ANNEX V – ECSDA PENALTIES REFERENCE DATA RULES & RECOMMENDATIONS


ECSDA Penalties Reference Data Rules and Recommendations





DRAFT V7.0 – Publicly available to relevant stakeholders                                                         100 | P a g e
Key changes of the version are highlighted in a light grey colour.

## PDF page 102
European Central Securities Depositories Association, aisbl
Rue du Congrès 1, 1000 Brussels, Belgium
ecsda.eu – info@ecsda.eu  - +32 2 230 99 01
RPM/VAT : BE0464619112 – Tribunal de l’entreprise francophone de Bruxelles
ING – BE30 3630 9647 3311 – Transparency Register : 278118292203-75