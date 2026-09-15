# UK Stamp Duty _ v.4 Track changes

Source: https://www.euronext.com/sites/default/files/2026-03/Euronext%20Securities%20-%20Stamp%20Duty%20Reserve%20Tax%20SDD%20-%20v.4%20Track%20changes.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED




UK Stamp Duty
Reserve Tax
Description Document

V.43 JANUARY MARCH 2026





1 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 2

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





2 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 3

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED


Summary

  1. Executive summary ................................................................................. 43

  2. Standards ................................................................................................ 43

  3. SDRT applicability in ES-MIL 1.5% regime .............................................. 43

  4. SDRT processing - External receipts of chargeable UK registered equities54

  4.1 Instruction flags and format .................................................................. 54

  4.2 Processing of the receipt instruction at Euronext Securities Milan ........ 75

  4.3 Collection and payment of the stamp duty to HMRC .............................. 86

  4.4 Reporting to HMRC ................................................................................ 86

  4.5 Retention and disclosure of documentary evidence ............................... 87

  5. Glossary .................................................................................................. 87





3 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 4

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED


1. Executive summary

As place of settlement for UK registered securities listed across Euronext Trading venues,
Euronext Securities Milan provides EUR settlement of on and off-exchange transactions
between our Participants, as well as custody of these securities.

UK registered equities  typically attract stamp duty obligations. However, settlement
transactions between Euronext Securities Milan Participant accounts will not be subject to
SDRT obligations.

Transfers of chargeable UK equities from other Clearance Service accounts (accounts
operated at 1.5% regime), will also be exempt from any stamp duty obligations.

The stamp duty obligation will arise where the Participant receives chargeable equities
from a 0.5% EUI/CREST account. This document describes the stamp duty requirements
on these transactions and Euronext Securities Milan service to facilitate the fulfilment of
our Participants’ obligations towards the UK Tax Authority (HMRC).

2. Standards

Stamp duty reserve tax (SDRT) is typically due and applied on electronic receipts of UK registered
shares including receipts of shares derived from dividend reinvestment plans where the broker
transfers the shares through CRESTand their rights, independently of where they are traded.

The standard regime rate is 0.5% and applies to all equity transactions settled between 0.5%
accounts in the CREST system. The higher 1.5% rate applies to the entry of chargeable shares into
a Clearing Service Account (as it is the case of Euronext Securities Milan) or into accounts of
depositary receipts providers.

The obligation to pay the SDRT typically lies with the transferee or buyer.

3. SDRT applicability in ES-MIL 1.5% regime

Euronext Securities Milan accesses the UK market as a Clearance Service.

For our Participants, this 1.5% SDRT regime means that the following transactions will be exempt
from SDRT

 -   All on and off-exchange transactions in chargeable UK shares, where Euronext Securities
    Milan  acts as PSETT  (all settlements  between accounts of Euronext  Securities Milan
     Participants), are exempt from stamp duty payment and reporting;
 -   External transfers (of chargeable UK shares) from and to other Clearance Service accounts
     (other 1.5% Clearance Service accounts) are also exempt of stamp duty (note these will
    however require the provision of certain stamp duty fields in the instruction, as explained
    below);
 -   Transfers of newly issued shares from a EUI /CREST system account into Euronext Securities
     Milan, receipts which equally remain exempt from SDRT.


4 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 5

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





Please note that dividends and rights distribution are also exempt from SDRT.

The regime also means that 1.5% SDRT ad valorem will apply on external receipts of chargeable UK
securities from a standard 0.5% CREST account into Euronext Securities Milan. The below
service description illustrates how the SDRT obligations are fulfilled in this particular case,
where a tax liability generated.




        Type of transaction                 Applicability for Particpants      SDRT fields required?


  External receipt transfers from another                                                 Exempt
       1.5% EUI/CREST account                                           Yes


 Transactions between Euronext Securities           Exempt                    No
            Milan participants

          Newly issued shares                     Exempt                    No


   External receipt transfers from other       Yes, 1.5% ad valorem             Yes
       EUI/CREST 0.5% accounts


4. SDRT processing  - External receipts of
chargeable UK registered equities

Euronext Securities Milan Participants are expected to adequately flag any external transfer
instruction of chargeable UK equities as to allow for

✓  identification of a chargeable transaction
✓  determine applicability of the stamp duty obligation
✓  calculation of the stamp duty payment obligation
✓  collection and subsequent payment to HMRC
✓  reporting of the transaction to HMRC


   4.1 Instruction flags and format


SDRT flagging is required for all external transfer receipts (which must be free of payment),
where -as transferee, - the Participant will be responsible for the SDRT obligations.

Euronext Securities Participants are expected to include the SDRT relevant fields as part
of the settlement instruction. Failure to adequately populate the stamp duty fields will
result in the instruction being rejected.





5 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 6

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED




Request for exemptions through the flagging of the instruction will need to be adequately
certified with the applicable supporting documentation, as per HMRC prescription.

For detail on the SSIs, please refer to the T2S gateway under Issuer CSD:UNITED
KINGDOM (MT23: 85667).




 4.2.1.   Mandatory UK stamp duty fields



        Transaction type

                                MT540                        1.5% SDRT ad valorem to be
Receipt from a 0.5% CREST account  :19A::DEAL//GBP15d                paid by the receiving party
                                  :22F::STAM/CRST/GBRX             (Euronext Securities Milan
                                                                                    Participant )
                                MT542 – SDRT indicators not required
                                                          0-5% SDRT to be paid by theDelivery to a 0.5% CREST account    :19A: not used
                                                                                 receiving CREST                                       :22F: not used
                                                                            counterparty

Internal Euronext Securities Milan   No formatting requirements whether
                                                                    Exempt from SDRTtrades                            PSETT is Euronext Securities Milan
Delivery to/from a Clearance Service MT540/MT542
account or a Depositary receipt      :19A: not used                       Exempt from SDRT
system account                    :22F::STAM/CRST/GBTX
Exemption claimed on receipt of new MT540
issued shares                        :19A: not used                       Exempt from SDRT
                                 :22F::STAM/CRST/GBWX



For these chargeable free receipts, it is important to note that Euronext Securities Milan
will not support settlement instructions where the delivering counterparty in EUI/CREST
is accountable for the payment of the stamp duty.




 4.2.2.    Input of the stampable consideration amount

Clients are expected to provide the stampable consideration amount as part of the free
receipt instructions to provide the basis for EUI/CREST calculation of the in-principle SDRT
amount due. This is to ensure the Participant determines the price at which the transaction
must be taxed at. The stampable consideration amount must be provided in GBP in the
relevant message field.

Euronext Securities Milan will not accept for processing any external transfer receipt from
standard 0.5% EUI/CREST accounts where the consideration is not included.

 4.2.3.    Calculation of SDRT

EUI/CREST system calculates the SDRT to be collected is performed by EUI/CREST, 1.5%
on the stampable cash consideration amount provided by the Participant in the receipt
instruction.




6 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 7

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED




Participants need to calculate the tax due (1.5% x share price x no. of shares) in order to
fund Euronext Securities Milan GBP account ahead of settlement. Please note the provision
of the stampable amount in the MT540 is required and its absence will prevent the release
of the instruction.


   4.2 Processing of the receipt instruction at Euronext Securities
   Milan


Euronext Securities Milan will identify the chargeable external receipt instructions and
validate their format and fields.

 4.2.4.   Funding of the SDRT

Participants receiving chargeable UK registered shares from a standard 0.5% SDRT
EUI/CREST account, need to fund the GBP stamp duty amount ahead of the settlement of
the receipt.

Participants need to calculate the stamp duty tax due The tax is due is calculated as 1.5%
of the stampable cash consideration.

Participants must provide the stampable cash consideration in the securities settlement
receipt instruction, and its absence will prevent the release of the instruction to market.

Participants are expected to pay the stamp duty tax amount due ahead of the securities
instruction  settlement  date,    into  the  following  Euronext  Securities  Milan GBP
account:(which must have been provided in the settlement receipt instruction), and must
be paid into the Euronext Securities Milan GBP account :

Citibank London: CITIGB2LCB2

Account number: 12724154

Participants are expectedneed to include the settlement transaction reference in the
payment instruction, to allow the linkage of the SDRT payment to the securities receipt
instruction.

To this effect, Participants are expected to include field <RmtInf> in the payment message
Pacs.009, as per quick market guide details. Please note that failure to comply with these
instructions, will entail the application an administrative fee, as listed in the fee schedule..

Once the confirmation of receipt of funds is received, Euronext Securities Milan releases
the chargeable free receipt to the market for settlement.

Important: in order to avoid any delays in the processing, Participants are advised to
arrange for the stamp duty payment as soon as possible.





7 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 8

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED



   4.3 Collection and payment of the stamp duty to HMRC

EUI/CREST System collects the duty from Euronext Securities Milan on Settlement Date
and deposits the amounts in a SDRT collections account.


Upon collection of the in principle amounts EUI/CREST pools all SDRT collections in an
account and pays HMRC regularly, but not immediately.

Where the amount collected by CREST is greater than the amount funded by the Participant
(tax underfunded), ES-MIL Client Service will contact the Participant to level the GBP
difference within 3BD. ES-MIL will debit the Participant in EUR and pass on any charges
incurred as a result as an administrative fee (please refer to fee schedule).

Where the Participant has overfunded the stamp duty obligation, ES_MIL will refund the
GBP excess in 3BD to the same account that instructed the prefund. Where the excess
funding amount for the day is below GBP 100, the refund will be effected on a monthly
basis.


   4.4 Reporting to HMRC


Whilst there are no reporting requirements for internal Euronext Securities Milan trades
(inside the 1.5% regime), transfers in and out Euronext Securities Milan Clearance Service
account are reported by EUI/CREST to HMRC.

EUI  reports on  behalf  of  its members  all both chargeable and exempted CREST
transactions, as well as the collected SDRT. EUI also provides HMRC with exceptions
reporting, informing where SDRT may have been underpaid.


   4.5 Retention and disclosure of documentary evidence


HMRC expects the maintenance of documentary evidence of details of all transactions and,
where applicable, proof of relief from SDRT, for at least six years from the settlement date
of the transaction and will need to be disclosed upon request from HMRC.

By holding UK securities in an account with Euronext Securities Milan, customers will be
deemed to have authorised the disclosure to HMRC upon request  of  all  details  of
transactions relating to UK securities.


5. Glossary


 Terms                       Definitions





8 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY

## PDF page 9

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





 SDRT                   UK Stamp Duty Reserve Tax


 CSA                          Clearance Service Account


 CSP                          Clearance Service Provider (owner of a CSA)


 HMRC                HM Revenue & Customs, the UK Tax Authority


 DRS                          Depositary Receipts System


 PSETT                    Acronym for Place of Settlement


                                Euroclear UK& Ireland (EUI/CREST) is the UK domestic
 EUI/CREST
                        CSD





                  euronext.com/post-trade


9 | Subtitle text, Verdana 9pt, Left aligned V.4 March 2026

                                     INTERNALPRIVATEPRIVATEPRIVATEPRIVATEPRIVATEUSE ONLY