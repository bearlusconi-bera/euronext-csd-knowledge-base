# See VPs CSDR Q&A

Source: https://www.euronext.com/en/media/9131/download

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

CSDR Q&A


Implementation of the Regulation (EU) No 909/2014 on improving securities settlement in the EU and on
central securities depositories.

November 2019

## PDF page 2

CSRD – Q&A

Contents
  Background & Purpose ................................................................................................................................................... 3
  General Questions .......................................................................................................................................................... 3
    Q1: What are the changes to the VP-system in order to be CSDR compliant? .......................................................... 3
    Q2: How and when will the VP Rulebook be updated in accordance with CSDR? ..................................................... 3
   LEI ................................................................................................................................................................................... 4
    Q3: What is a LEI? ....................................................................................................................................................... 4
    Q4: Where do I get a LEI? ........................................................................................................................................... 4
    Q5: At which level are LEIs mandatory and who has to report them? ....................................................................... 4
    Q6: Regarding the account type “Customer On behalf of customers (Global Custodian)” – whose LEI should be
     registered on these types of Securities Accounts – is it the CSD Participant´s LEI i.e. the Securities Account
     Controller (KI) or is it the actual customer´s LEI e.g. the Global Custodian? .............................................................. 4
    Q7: Is it mandatory to report a LEI on collective investment funds? ......................................................................... 5
    Q8: Should remote participants report a LEI? ............................................................................................................ 5
    Q9: Does VP check if the correct data has been registered? ...................................................................................... 5
    Q10: What if issuers or Participants refuse to submit a LEI? ...................................................................................... 5
    Q11: Is there any other legislation mandating the registration of LEI? ...................................................................... 5
   Static Data on Securities Accounts ................................................................................................................................. 6
    Q13: Is it possible to determine which account markings used (PR/FH/ST) will be the equivalent of IS/OM/OW? .. 6
  Protection of securities ................................................................................................................................................... 7
    Q14: What are the obligations for Participants regarding information related to the protection of customers
     securities, i.e. levels of segregation? .......................................................................................................................... 7
  IBAN-number .................................................................................................................................................................. 7
    Q15: IBAN-numbers – what has to be reported? ....................................................................................................... 7
  Data on Transaction Type, Place of Trading and Place of Clearing ................................................................................. 8
    Q16: Which new fields will enter into force with the CSDR settlement discipline regime? ....................................... 8
  Reporting – Technical Issues ........................................................................................................................................... 8
    Q17: How do I report Ownership type on Securities Accounts? ................................................................................ 8
    Q18: How do I report information on issuers and Participants? ................................................................................ 8
  Suspension of securities for Settlement ......................................................................................................................... 9
    Q19: What is the procedure for suspension of securities for settlement? ................................................................ 9
  Settlement Internalisers ................................................................................................................................................. 9
    Q20: What should be reported regarding internalised settlement? .......................................................................... 9
   Partial Settlement ......................................................................................................................................................... 10
    Q21: Will partial settlement be implemented in the VP Clearing and Settlement system? .................................... 10





                                                                                        Page 2 of 10

## PDF page 3

CSRD – Q&A

Background & Purpose

Regulation (EU) No 909/2014 of the European Parliament and of the Council on improving securities
settlement in the European Union and on central securities depositories and amending Directives 98/26/EC
and 2014/65/EC and Regulation (EU) No 236/2012 (“CSDR”) entered into force on 17 September 2014.
Most of the obligations under the CSDR have been specified further via regulatory technical standards.

The CSDR framework consists of the following EU legislation:
    •  CSDR
    •   Delegated Act (parameters for the calculation of cash penalties for settlement fails)
    •  RTS on CSD Prudential Requirements
    •  RTS on Internalised Settlement
    •  RTS on CSD Requirements
    •   ITS on Internalised Settlement
    •   ITS on CSD Requirements
    •  RTS on settlement discipline

The intent of the legislation is the harmonisation of the regulatory environment of securities settlement
and Central Securities Depositories in the European Union.

The purpose of this document is to provide clarity on the implementation of CSDR requirements. It provides
responses to questions posed by VPs customers and participants in relation to the practical application of
CSDR. This Q&A will be reviewed and updated as and when appropriate.

A separate Q&A on CSDR Settlement Discipline will be published in due course.

Terms with capital letters have the meaning as defined in Part 1 of the VP Rule Book, (Definitions).
General Questions

Q1: What are the changes to the VP-system in order to be CSDR compliant?
A: VP systems have been updated in order to be CSDR compliant. Hence, all existing Securities Accounts
have been marked with ownership type (OW, OM, IS), which is also applicable when opening new Securities
Accounts. Furthermore, Issuers and Participants in VP have been obliged to forward their LEI (Legal Entity
Identifier) to us for registration. For details, please refer to sections

LEI and


Static Data on Securities Accounts below.


Q2: How and when will the VP Rulebook be updated in accordance with CSDR?
A: VP received the CSDR authorisation from the Danish FSA as of 3 January 2018 and as a consequence, the
VP Rule Book was updated accordingly. All parts of the VP Rule Book, i.e. Definitions, Terms and Conditions,
Book-entry Rules and Settlement Rules, have been changed. CSDR-related updates are:



                                                                                        Page 3 of 10

## PDF page 4

CSRD – Q&A


    •   Suspension of an ISIN if the reconciliation reveals an undue creation or deletion of securities
    •   Termination of the requirement for Securities Account Controllers to provide a guarantee to VP
    •  Requirements on LEI and asset segregation
    •   VP's right to refuse access to our systems



LEI

Q3: What is a LEI?
A: The Legal Entity Identifier (LEI) is a unique 20 character code, based on the ISO 17442 standard, for a
legal entity that participates in financial transactions worldwide, throughout all markets and legal systems.
LEI contains key reference information and resembles a business registration number. The establishment of
a Global LEI system is critical to improving measurement and monitoring of systemic risks. Global,
standardised LEIs will enable regulators and organisations to more effectively measure and manage
counterparty exposure while also resolving long standing issues on entity identification across the globe.

Q4: Where do I get a LEI?
A: For information regarding LEIs and how to obtain them, please visit the Danish FSA homepage. Further
information can be found at the Global Legal Entity Identifier Foundation (GLEIF) website.

Q5: At which level are LEIs mandatory and who has to report them?
A: CSDR imposes mandatory updates to issuer identification. VP shall report LEIs on our customers and we
are therefore obliged to register LEIs on all issuers and Participants in VP.

According to CSDR, LEIs on Securities Account level is optional.

A customer can be an issuer in VP and must have a LEI registered, even though the issuer does not have a
Securities Account in VP or is listed on a regulated market. The Issuing Agent representing the issuer is
responsible for reporting LEI on the issuer.

Q6: Regarding the account type “Customer On behalf of customers (Global Custodian)” – whose LEI
should be registered on these types of Securities Accounts – is it the CSD Participant´s LEI i.e. the
Securities Account Controller (KI) or is it the actual customer´s LEI e.g. the Global Custodian?
A: First of all, LEIs on Securities Accounts are not mandatory according to CSDR. For the Securities Account
type IS where the customer is a Global Custodian, it is the LEI of the Global Custodian that may be reported,
i.e. it is the LEI of the Participant’s clients that may be reported.





                                                                                        Page 4 of 10

## PDF page 5

CSRD – Q&A

Q7: Is it mandatory to report a LEI on collective investment funds?
A: Yes, LEIs are mandatory on collective investment funds issuing securities. Sub-funds (”afdelinger”) and
unit classes (”andelsklasser”) of collective investment funds are not required to have their own and
independent LEI when acting as issuers, although it is possible to register a LEI for the various entities
within a collective investment fund. Thus, in the context of CSDR, a LEI per collective investment fund is
sufficient. Please note that a LEI on sub-funds and unit classes may be required in order to be compliant
with other legislation, c.f. below.

Q8: Should remote participants report a LEI?
A: Customers who have signed an agreement with VP as a Settlement Participant and appointed another
Securities Account Controller (remote participant) are considered participants under CSDR, as VP’s General
Terms and Conditions apply. Furthermore, they are participating directly in the settlement of securities.
Remote participants are therefore obliged to comply with CSDR, and report a LEI.

Q9: Does VP check if the correct data has been registered?
A: All issuers and Participants are responsible for delivering the correct information. The LEI must be valid
and have a status of ‘Issued’, ‘Pending Transfer’ or ‘Pending Archival’. If the LEI is not provided for the
correct legal entity or does not have the correct status, the LEI will be considered invalid. Furthermore, the
LEI must be renewed yearly to maintain validity. Thus, VP has to ensure that accurate and up-to-date
details have been provided for reporting purposes to the Danish FSA.

Q10: What if issuers or Participants refuse to submit a LEI?
A: According to CSDR, VP has to report a LEI on all issuers and Participants to the competent authorities,
which is also incorporated in the VP Rulebook upon receipt of the CSDR authorisation (cf. VP Rulebook, Part
2 General Terms and Conditions, section 2.1.4.). All our customers are obliged to observe and comply with
the terms and conditions as stipulated in the VP Rulebook and must act in accordance with applicable
legislation for VP, including CSDR. Thus, VP has a responsibility to require the presence of an issuer LEI
before we can accept to act as an issuer CSD for securities of that issuer.

If an issuer or Participant does not provide a LEI, they do not fulfill the requirements for participation with
VP and VP may suspend the service or terminate the agreement (cf. VP Rule Book, Part 2 General Terms
and Conditions, section 6.7)

Q11: Is there any other legislation mandating the registration of LEI?
As mentioned above, VP shall report LEIs on our customers in accordance with CSDR, i.e. VP have to
register LEIs on all issuers and Participants in VP. However, other European legislation mandates both EU
and non-EU market participants to obtain an LEI in a variety of circumstances in order to trade or clear:

EMIR: EU trade repositories are obligated to reject trade reports that do not contain an LEI. Under certain
circumstances, the underlying fund/sub-fund must get its own LEI.





                                                                                        Page 5 of 10

## PDF page 6

CSRD – Q&A

MIFID II/MIFIR: Investment firms are required to obtain an LEI from their customers prior to providing a
service that would result in a transaction reporting obligation. Customers of investment firms, including
sub-funds, intermediaries and wealth clients, will be required to have an LEI, even if they are not an EU
entity, not operating or domiciled in the EEA and not directly subject to EU regulations.

Please consult the corresponding regulation for further details:
MIFIDII/MIFIR
EMIR

A LEI is therefore necessary to buy or sell securities – no LEI, no trade. You can still hold existing securities
and not have a LEI, but once you buy or sell, including subscriptions and emissions, a LEI will be required.

Once again, it must be stressed that VP is subject to CSDR and must require LEI from you in accordance
with these rules, but that you might be subject to other legislation as well, which will require a LEI in order
for you to be fully compliant with all European Legislation.


Static Data on Securities Accounts

Q12: What information is added at Securities Account level?
A: CSDR imposes mandatory markings of Securities Accounts depending on the type of owner:
    •  OW – Own account (Participant’s own account)
    •  OM – Omnibus account (Account held by participant on behalf of customers)
    •   IS – Client individual account (Individual client segregation)

Clients who wish to change the marking of a Securities Account may report this to VP. Please also note that
an ownership type is mandatory for all new Securities Accounts.

Q13: Is it possible to determine which account markings used (PR/FH/ST) will be the equivalent of
IS/OM/OW?
A: No, the markings PR/FH/ST refers to settlement groups in the system with different rights/obligations.
They are not related to CSDR and are part of the system management tools necessary to ensure the
operation of the system.





                                                                                        Page 6 of 10

## PDF page 7

CSRD – Q&A

Protection of securities

Q14: What are the obligations for Participants regarding information related to the protection of
customers securities, i.e. levels of segregation?
A: According to CSDR art. 38(6) VP shall publicly disclose the levels of protection and the costs associated
with the different levels of segregation that we provide. The description shall include the main legal
implications of the respective levels of segregation. VP has published a brief regarding the levels of
segregation offered by VP, which has also been distributed to the members of Finance Denmark.

Independently of VP, Participants are also obligated to publicly disclose the levels of segregation that they
offer and the commercial terms and costs related to these.

Remote participants are only participating directly in the VP Clearing and Settlement system on their own
behalf and is neither entitled nor obligated to undertake Securities Account Controller related activities
such as book-entry. Therefore Remote participants are not obligated to offer their customers several levels
of segregation according to CSDR.


IBAN-number

Q15: IBAN-numbers – what has to be reported?
A: The following has to be reported in order to be compliant with CSDR:
    •  IBAN number for issuers´ cash accounts used to provide liquidity to pay out interest, dividends,
       redemptions etc.

    •  DCA’s used for Corporate Actions have a corresponding cash account with an IBAN number

    •  Mortgage institutions may submit IBAN number for their own cash accounts in KRONOS/DN used
        for Corporate Actions

    •   For EUR cash accounts in Target 2: It will be possible to submit an internationally recognized bank
       account number specifically for accounts with no IBAN number

    •    If a Issuer issues securities in more than one currency, an IBAN number has to be provided for all
       cash accounts (DKK, SEK, EUR)





                                                                                        Page 7 of 10

## PDF page 8

CSRD – Q&A

Data on Transaction Type, Place of Trading and Place of Clearing

Q16: Which new fields will enter into force with the CSDR settlement discipline regime?
A: VP settlement instructions contain the transaction data required according to CSDR.

The changes envisaged under CSDR are the fields ‘Type of transaction’, ‘Place of Trading’ and ‘Place of
Clearing’ which will enter into force at the time as the new settlement discipline regime (not a matching
criteria).


Reporting – Technical Issues

Q17: How do I report Ownership type on Securities Accounts?
A: Static data on Securities Accounts can be reported through the proprietary format or VP user interface
(3270).

Q18: How do I report information on issuers and Participants?
A: Static data on issuers can be reported through eFORMS in vp.ONLINE. Customers with no access to
vp.ONLINE can send an email to CSD Services (csd@vp.dk) with the information in order to ensure
registration.

Participants reporting their own LEI and IBAN-no. (not reporting the information for other customers in the
capacity of Securities Account Controller/Issuing Agent) can do so by sending an email to CSD Services
(csd@vp.dk).





                                                                                        Page 8 of 10

## PDF page 9

CSRD – Q&A

Suspension of securities for Settlement


Q19: What is the procedure for suspension of securities for settlement?
A: VP performs a daily reconciliation on:
    •    Aggregated opening balance
    •    Individual movements during the day
    •    Aggregated closing balance

In case of a reconciliation break or system disturbance, there can be a suspension of settlement, and VP
issues updates through VP Info’s as per usual, until the issue has been solved.

The suspension of Settlement in case of problems related to reconciliation has been implemented in the VP
Rule Book.


Settlement Internalisers


Q20: What should be reported regarding internalised settlement?
A: Settlement internalisers shall report to the competent authorities on a quarterly basis the aggregated
volume and value of all securities transactions that they settle outside securities settlement systems.
For further information, please refer to the Guidelines on Internalised Settlement Reporting published by
ESMA.





                                                                                        Page 9 of 10

## PDF page 10

CSRD – Q&A

Partial Settlement

Q21: Will partial settlement be implemented in the VP Clearing and Settlement system?
A: According to CSDR, a CSD shall offer participants the option to settle their Transfer Orders partially. T2S
will apply partial Settlement when the delivering party does not have the full quantity of securities, or the
receiving party does not have sufficient cash on the DCA for Settlement.
Transfer Orders for Settlement on T2S are per default subject to partial Settlement, although it is possible
to exclude Transfer Orders from partial Settlement. Thus, VP will be developing a solution for partial
Settlement in the VP system in accordance with the legislation as well as aligning our systems with T2S
functionality.





                                                                                       Page 10 of 10