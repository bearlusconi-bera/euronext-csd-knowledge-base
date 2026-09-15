
## PDF page 1
                                                 SDD ACCOUNT STRUCTURE


Euronext
Securities Milan
Account structure
Service Description Document

V. 03, MAY 2026





1 | V.03 May 2026

                                        PRIVATE

## PDF page 2
                                                 SDD ACCOUNT STRUCTURE





  1. Introduction .............................................................................................. 3

  1.1 Document purpose .................................................................................. 3

  1.2 Target audience ....................................................................................... 3

  1.3 Reference Service Description Document ................................................ 3

  2. Securities account creation ....................................................................... 4

  2.1 Client onboarding .................................................................................... 4

    2.1.1 Opening a client security account ............................................................ 4

    2.1.2 Securities account management .............................................................. 5

  3. Securities account structure ...................................................................... 5

  3.1 Type of operations and activities ............................................................. 5

  3.2 Type of issuer securities account ............................................................. 7

  3.3 Type of intermediary securities account .................................................. 7

    3.3.1 Account type combinations ..................................................................... 8

  3.4 Types of holding ...................................................................................... 9

  3.5 Mandatory securities accounts to manage the specificities of French
  securities ..................................................................................................... 10

    3.5.1 Securities account numbering convention ................................................ 10

    3.5.2 Securities account detailed information ................................................... 11

    3.5.3 Account structure optimisation with T2S restrictions ................................. 12

  3.6 Securities account mapping ................................................................... 15

  3.7 Link between securities account and cash account ................................ 16

  4. Glossary .................................................................................................. 17





2 | V.03 May 2026

                                        PRIVATE

## PDF page 3
                                                 SDD ACCOUNT STRUCTURE


1. Introduction


1.1 Document purpose


This document is intended for current and prospective clients of Euronext Securities
Milan. It provides a comprehensive overview of the security account structure, aligned
with applicable onboarding procedures, and outlines the key elements relevant to
account configuration.

Additionally, it offers a complementary explanation of our account framework,
particularly in relation to French-registered securities and corporate event services
provided by Euronext Securities Milan.

In addition, it presents the various types of securities accounts available, along with their
structural attributes and operational purposes. The document also details the mapping of
these accounts to the TARGET2-Securities (T2S) platform, ensuring clarity on how local
account configurations correspond to T2S settlement architecture.


1.2 Target audience


The target audience for this document are:

    •   Financial intermediaries, and
    •  Other users1 of Euronext Securities Milan services, particularly those seeking
      guidance on setting up their account structures.


1.3 Reference Service Description Document


To support a clear understanding of Euronext Securities Milan’s service offering, the
following Service Description Documents (SDDs) are provided:


 Service Description Document        Key provided information

                                               • French registered securities background and main
 French Registered Shares Service
                                                   activities
 Description Document
                                               •  Specificities of the security account structure for
                                        French registered securities




1 Users refers broadly to any party interacting with Euronext Securities Milan services and systems,
including CSD participants clients, and related operation or technical teams.


3 | V.03 May 2026

                                        PRIVATE

## PDF page 4
                                                 SDD ACCOUNT STRUCTURE





 Service Description Document        Key provided information

                                               • Information on Registered Investors (IRI)
                                           processing



 Corporate Events Service               • Corporate event management
 Description Document                   • Transaction management


These documents are available in here CSD Expansion Documentation.

2. Securities account creation


2.1 Client onboarding


To open an account with Euronext Securities Milan, an entity must first complete the
onboarding process. This process involves several key steps, which are detailed in the
following Euronext Securities Milan client onboarding documentation.

After successful onboarding, clients will be granted access to the Client Membership
Platform (CLIMP). It is important to note that the Client Membership Platform is only
available to clients of Euronext Securities Milan who possess the appropriate credentials
for Euronext Securities Milan platform.

Once access to the Client Membership Platform has been established, clients who are
already familiar with the platform can submit their account opening requests directly
through the Client Membership Platform.

2.1.1 Opening a client security account


Clients seeking to open a securities account with Euronext Securities Milan must follow a
structured onboarding process.

This includes submitting legal and operational documentation, and configuring the
securities account appropriately to manage the required securities and financial asset
types, either:

     •   Proprietary account
     •   Third-party account
     •  Segregated account.

Connectivity set-up via SWIFT and access to Euronext Securities Milan platforms (CLIMP,
MT-X, X-TRM) are also required.



4 | V.03 May 2026

                                        PRIVATE

## PDF page 5
                                                 SDD ACCOUNT STRUCTURE




Please note that your account activation may follow either a standard or expedited
procedure depending on urgency. For full details, please refer to the Euronext Securities
Milan Client Onboarding Handbook.

2.1.2 Securities account management


Euronext Securities Milan security account management rules are detailed in the client
onboarding handbook.

These cover the following actions:

    1. Account creation and opening
    2. Account modification
    3. Account closure
    4. Account transfer.

3. Securities account structure


Euronext Securities Milan account structure is built around the following elements:

    •  Type of operations or activities
    •  Type of security account
    •  Type of holding.


3.1 Type of operations and activities


In Euronext Securities Milan, two categories of operations and activities are recognised:

    1. Issuer activities – coded as “22”

    2. Intermediary activities, coded as:

            •  “00” – French bearer and other dematerialised securities

            •  “04” – French administered registered securities

            •  “06” – Broker trading activities on French registered securities

            •  “07” – French pure registered securities

The activity type is indicated by the final two digits of your securities account number,
which will be either “22”, “00”, “04”, “06”, “07”.





5 | V.03 May 2026

                                        PRIVATE

## PDF page 6
                                                 SDD ACCOUNT STRUCTURE




Summary table:

                                                                              Example of
 Activity type    Type of assets        Code  Description                                security
                                                                                     account

                                               Operations carried out in the capacity of
                                           a securities issuer.

 Issuer            All type of assets       22     This is a debit account, opened for the    12345-22
                                                      issuer. This type of account is used to
                                                   issue new securities within the CSD,
                                       when acting as issuer CSD.


                                               Operations carried out in the capacity of
                                           a financial intermediary.
                French bearer and
                  dematerialised         00     Holds dematerialised securities and also   12345-00
                   securities                     French regulated bearer securities.

                                                   This is a credit account.


                                                     Securities account opened to hold
                                              French regulated administered
                French administered
                                   04     registered securities.                  12345-04
                  registered securities

                                                   This is a credit account.

 Intermediary
                                                     Securities account opened for brokers in
                                                order to receive and deliver registered
                French registered
                                                      securities within on-exchange
                   securities for trading    06                                       12345-06
                                                    transactions.
                     activities

                                                   This is a credit account.


                                                     Securities account opened to hold
                                                      securities in pure registered form,
                French pure registered          recorded in the issuer’s register. The
                                   07                                       12345-07
                   securities                     account is opened in the name of the
                                                    issuer or its appointed representative
                                                   acting as registrar.




This Service Description Document is intended primarily for financial intermediary
services. Refer to section 3.4.1 for further details on account numbering conventions.





6 | V.03 May 2026

                                        PRIVATE

## PDF page 7
                                                 SDD ACCOUNT STRUCTURE


3.2 Type of issuer securities account


In accordance with the Euronext Securities Milan instructions for CSD services, the Issuer
Account within the CSD platform serves as the dedicated account for registering,
managing, and updating the financial instruments issued by the Issuer. It also supports
the execution of all related corporate and administrative operations throughout the
lifecycle of those instruments.

For more information on key functions and operational use, please refer to the instruction
for CSD services.


3.3 Type of intermediary securities account


CSD participants of Euronext Securities Milan may open three types of accounts with
Euronext Securities Milan:

    •  Proprietary account (P): a securities account opened in the name of the CSD
        participant, used to hold and manage the participant’s own assets directly.

    •  Omnibus account (T): a securities account opened by CSD participant to pool
       the positions of multiple underlying clients, providing a consolidated view of
       holdings.

    •  Segregated account (L): a flexible account type that can be tailored to specific
      needs and configured with different segregation:

         o  Individual segregation (IS): segregated securities account to hold the
              assets of a single client.

         o  Omnibus segregated (OM): segregated securities account to hold the
              assets of multiple clients within a single account. This account is intended
                for participants holding instruments on behalf of their client.

         o Own segregated (OW): segregated securities account opened in the
          name of the CSD participant, used to hold and manage the participant’s
           own assets.

Note: Only Type L accounts, when enabled with the appropriate flag in the Client
Membership Platform (CLIMP), and the relevant activity code (e.g., 04), are permitted to
hold French Registered Securities2.


The following table provides a summary of the account types available at Euronext
Securities Milan:




2 This applies for French registered securities which may be of the VON or VEN type. For further
details on our French Registered Securities offering, please refer to our SDD section of the website.


7 | V.03 May 2026

                                        PRIVATE

## PDF page 8
                                                 SDD ACCOUNT STRUCTURE





 Account type   Code  Purpose                                Legal form of underlying securities

                                                                Dematerialised securities held
                                                           under bearer form in the
                       Records financial instruments owned by   participant’s own name.
 Property
               P      the participant in its own name and for
 account
                                 its own benefit.                          This type of account cannot be
                                                          used to hold French registered
                                                                          securities.


                                                                Dematerialised securities held in
                                                                          collective form without individual
                       Records financial instruments held by
                                                                             client registration.
 Omnibus              the participant on behalf of multiple
               T
 account                  clients, pooled together without
                                                                   This type of account cannot be
                            individual segregation.
                                                          used to hold French registered
                                                                          securities.


                                                                Dematerialised securities held
                                                                       either for own assets, individual
                                                                           clients or multiple clients
                       Subaccount format identifier used for
                                                              (omnibus).
 Segregated             specific operational or client-level
                 L
 account               segregation purposes within the main    This type of account can be used
                         account.                                  to segregate registered securities
                                                                       either for investor or broker
                                                                             activity, as per the configuration in
                                                           CLIMP.


3.3.1 Account type combinations


Depending on their business profile and the nature of their clients’ activities, CSD
participants may choose to first open either a Proprietary Account (P) or an Omnibus
Account (T).

If only one account is opened, whether P or T, it will automatically be designated as the
participant’s default account, for French regulated bearer securities and other
dematerialised securities issued in other jurisdictions. Euronext Securities Milan
participants may also decide to segregate their clients’ assets by opening additional
accounts with the relevant type.

Where both a Proprietary Account (P) and an Omnibus Account (T) are opened, the
Proprietary Account will be set as the default.

Once one or both of these main account types have been established, CSD participants
may request the creation of additional segregated accounts (Type L) to meet specific
operational or regulatory requirements.

In that case, these accounts will be linked together.

These accounts can be tailored to individual needs and may take several forms (e.g., IS,
OM, OW). Type L accounts may also be used for:



8 | V.03 May 2026

                                        PRIVATE

## PDF page 9
                                                     SDD ACCOUNT STRUCTURE




          •  Holding registered securities – when enabled with the dedicated CLIMP flag
          •  Supporting broker activities on registered securities.

     Existing participants also have the option to reuse their current accounts and supplement
    them with Type L accounts, which are specifically designed to segregate French regulated
     securities and their nature of activity (e.g., “04”). These may include administered
     registered shares.

    3.3.1.1 Application of account types and activity codes

    Euronext Securities Milan account framework accommodates the combination of different
    type of accounts and activity codes. to serve the various combinations of accounts for
     proprietary

Account     Form of           Participant      Account                                                                    Activities  Type  Securities Account
purpose       assets/activities  BIC (PARTY1)   number
             Bearer –
                                                00       P     MOTI-BANKFRPPXXX-12345-00
              dematerialised
Proprietary   Administered
                                        12345   04        L     MOTI-BANKFRPPXXX-12345-04activities      registered
             Broker trading
                                                06        L     MOTI-BANKFRPPXXX-12345-06                activities

             Bearer         BANKFRPPXXX          00       T     MOTI-BANKFRPPXXX-23456-00
Principal
                                        23456
omnibus     Administered
                                                04        L     MOTI-BANKFRPPXXX-23456-04
              registered

             Bearer                               00        L     MOTI-BANKFRPPXXX-34567-00
Secondary                                        34567
omnibus     Administered
                                                04        L     MOTI-BANKFRPPXXX-34567-04              registered

    Notes: for simplification, the account number is shown here with a ‘–’ character. In
    operational documents and business messages, account numbers are displayed as
    continuous digits without separators (e.g., 1234501).


  3.4 Types of holding


    Euronext Securities Milan security accounts allow CSD participants and their clients to
    hold securities issued in the form referred to in CSD-R as complemented by relevant
     national securities law where applicable and according to the provisions of ES-MIL
    Rulebook.

    Notably in relation to French securities the following categories of securities could be
    managed:

         •  French dematerialised securities, also referred to as bearer on the French
          market, eligible in T2S and in the Euronext Securities Milan book-entry system.

         •  French registered securities, under the French legal form, either purely
            registered or administered registered, included in the Euronext Securities Milan
           book-entry system.




    9 | V.03 May 2026

                                            PRIVATE

## PDF page 10
                                                 SDD ACCOUNT STRUCTURE




Securities, registered under the French legal form and included in the Euronext Securities
Milan book-entry system, may be either administered (managed via an intermediary) or
pure (held directly with the issuer).


3.5 Mandatory securities accounts to manage the
specificities of French securities


To manage French securities, and particularly trading activities in French registered
securities, and to hold these types of assets, it is mandatory to open three distinct
accounts, as outlined below:

                                              Account     Activity     Flag in
 Holding type                                                types      type      CLIMP

 Bearer and dematerialised securities         L         00       No


 Administered Registered securities           L         04         Yes


 Registered for trading activity                L         06         Yes


 Pure registered securities                    L         07         Yes



During the securities account configuration process, the accounts required to hold bearer,
dematerialised, and registered securities will be linked in CLIMP according to the relevant
activity type.

3.5.1 Securities account numbering convention


Euronext Securities Milan uses a defined account structure, with each account created
according to the following numbering convention to ensure consistency and clear
segregation between participants.

Numbering convention


 Components                       Description

 Parent BIC                  MOTI

 Party BIC                   SWIFT BIC 11 of the party


 Account                           Five (5) digits


 Activity type number         Two (2) digits





10 | V.03 May 2026

                                        PRIVATE

## PDF page 11
                                                 SDD ACCOUNT STRUCTURE




The five-digit account number included in both account types is assigned directly by
Euronext Securities Milan.

Participants cannot select or customise these numbers, as they are system generated to
ensure the integrity and uniqueness of each account. This standardisation supports
consistent account identification and facilitates efficient processing and reconciliation
across the platform.

3.5.2 Securities account detailed information


Euronext Securities Milan provides the following intermediary securities accounts,
determined by the CLIMP configuration of the underlying legal form of the security
(bearer – B, or registered – R).

It is assumed that the CSD participant has also opened an additional T or P default
account.

Account type L – 00 - Bearer

                                                       Corporate
 Type of    Account    Segregation   Activity   Flag in                                                      event         Earmarking  Direction
 holding    types      type          type     CLIMP                                                            services
                        IS3
 Bearer    L       OM         00      B        Yes           Yes          Credit
              OW

This account type represents securities maintained in book-entry and dematerialised
form.

Account type L – 04 – Administered registered

                                                       Corporate
 Type of     Account   Segregation   Activity   Flag in                                                      event         Earmarking  Direction
 holding     types      type         type     CLIMP                                                            services
                       IS
 Registered  L      OM         04      R       Yes           Yes          Credit
               OW

The account is used exclusively for securities in administered registered form. It records
the balances of parties whose underlying clients are registered in the issuer’s register as
per applicable market practice.

This account can be linked with a bearer and a broker trading account.

Account type L – 06 – Broker trading – Registered





3 Refer to the section 3.2 for more details on the segregation levels.


11 | V.03 May 2026

                                        PRIVATE

## PDF page 12
                                                 SDD ACCOUNT STRUCTURE




                                                       Corporate Type of     Account   Segregation   Activity   Flag in
                                                      event         Earmarking  Direction holding     types      type         type     CLIMP
                                                            services
                OM Registered  L                    06      R       Yes          N/A          Credit
               OW

This account is available to brokers and is used exclusively for securities in fully
registered legal form. It acts as an interim account used prior to the transfer into a
registered securities account and vis à vis the central counterparty.

This account can be linked with a bearer and an administered registered securities
account.

Account type L – 07 – Pure registered

                                                       Corporate
 Type of     Account   Segregation   Activity   Flag in
                                                      event         Earmarking  Direction holding     types      type         type     CLIMP
                                                            services

 Registered  L      OM         07      R       Yes           Yes          Credit

Used exclusively for pure registered securities, this account records the balances of
parties whose underlying clients are registered in the issuer’s books and official register,
in accordance with applicable market practice. This account is opened by the registrar
responsible for managing the investor register.

3.5.3 Account structure optimisation with T2S restrictions


Euronext Securities Milan has established an account structure aligned with T2S
requirements, enabling clients to achieve the necessary segregation of their activities
while maintaining a limited number of accounts.

This structure relies on the T2S blocking and earmarking capabilities, which allows
dedicated quantities to be reserved for specific purposes (e.g., an instructed quantity
during an elective corporate event).

The platform leverages this functionality to create blocked sub‑balances within a single
account, enabling clients to separate and manage multiple activities efficiently.

3.5.3.1 Restrictions definition

In T2S, earmarking/blocking refers to designating a position on a financial instrument
for a specific purpose, ensuring it cannot be used for anything else until the
earmarking/reservation is lifted.

This helps manage financial obligations and ensures that assets are available for their
intended use.

Earmarking/reservation works in both ways: it can be either requested or lifted.





12 | V.03 May 2026

                                        PRIVATE

## PDF page 13
                                                 SDD ACCOUNT STRUCTURE





 Code              Reason

                         Blocking of an instructed quantity of dematerialised/bearer securities, is
                      based on a valid corporate action instruction. Once the instruction is
                           validated, the specified quantity is transferred to the reserved balance by
                        the corporate action system.
 CUS1
                     The blocking process remains consistent whether Euronext Securities Milan
                          functions as the Investor CSD or the Issuer CSD.

                     Any cancellation of a corporate action instruction triggers the lifting of the
                          reservation.


                         Blocking of an instructed quantity of registered securities, either Pure or
                         Administered, is based on a valid corporate action instruction. Once the
                           instruction is validated, the specified quantity is transferred to the reserved
                        balance by our corporate action system.
 RECA
                     The blocking process remains consistent whether Euronext Securities Milan
                          functions as the Investor CSD or the Issuer CSD.

                     Any cancellation of a corporate action instruction triggers the lifting of the
                          reservation.


                         Blocking of a certain quantity of security proceeds, to be distributed by
                       Euronext Securities Milan on a registered securities account, upon the
                        acceptance of an IRI or BRN. E045

                    Upon the acceptance of the related IRI or BRN, the quantity will be moved to
                        the available balance (AWAS).



                  CSD participants' clients have the option to decline receiving a cash
                            distribution on an eligible security (either under bearer/dematerialised form
                         or registered). If a client makes this choice, participants must instruct this
                             specific earmarking to reflect it.

                         In such cases, cash proceeds, despite being eligible, will not apply to the
 EREF                        reserved quantity. There will be no cash paid on that earmarked quantity.

                     The earmarking should be lifted after the event payment date.

                         In this scenario, earmarking must be instructed manually by the participant.
                                It will not be instructed by Euronext Securities Milan automatically.





13 | V.03 May 2026

                                        PRIVATE

## PDF page 14
                                                 SDD ACCOUNT STRUCTURE





 Code              Reason

                           Clients of CSD participants who hold an eligible security (either under
                         bearer/dematerialised form or registered) can choose to decline commission
                     payments alongside a cash distribution. If a client opts for this, participants
                     must make this specific earmarking to reflect the choice.

                         In these instances, commission payments will not apply on the proceeds
                         regarding the earmarked quantity, and no commission proceeds will be paid
 ECOM                     on it.

                     The earmarking could be lifted after the event payment date, or whenever
                          required.

                         In this scenario, earmarking must be instructed manually by the participant.
                                It will not be instructed by Euronext Securities Milan automatically.



3.5.3.2 Restriction processing

Earmarking and blocking are a key process that ensures the correct segregation and
management of securities positions, particularly in relation to entitlement calculations
and compliance with market practice requirements.

In relation to corporate events processing, restrictions may be triggered in two ways:

    1. By our corporate event management platform – The system automatically
       applies blocking codes in response to specific triggering events, such as:

         o  Client instruction or cancellation request validation – After verifying
             the accuracy of the instruction, an earmarking request is sent to T2S via
             the standard sequence of messages (semt.013, semt.014, and semt.015).
                   If accepted by T2S, the instructed quantity is earmarked on the relevant
             sub-balance.

         o  Confirmation of corporate event proceeds from a newly issued
           French registered security – When these are awaiting registration by
             the issuer, and it is known they will be delivered to a registered securities
              account, a dedicated earmarking is triggered. As above, the instructed
              quantity is earmarked on the relevant sub-balance.

    2. By user action – Users may manually apply earmarking codes in T2S to reserve
       or exclude securities from entitlement calculations in two cases:

         o  Declining to receive a cash distribution payment.

         o  Declining to receive a commission payment from a cash distribution, in line
              with current French market practice.

         o  Users can either request earmarking by sending ISO20022 semt.013 or
             sese.023 messages.





14 | V.03 May 2026

                                        PRIVATE

## PDF page 15
                                                                                    SDD ACCOUNT STRUCTURE



3.6 Securities account mapping


The Euronext Securities Milan account structure and related functionalities are designed to align with the framework used by Belgian,
Dutch and French issuer CSDs.

This approach ensures operational compatibility for participants, allowing them to manage securities in a consistent manner among the
issuer CSDs account types and associated processes.


     Issuer CSD market practices in terms of accounts                       Euronext Securities Milan structure

     Account                                                                    Euronext Securities Milan sample of                        Restriction                     Definition                                                                                                         Restrictions
     Nature (AN)                                                                          security account number                               type

    009       Permanent holding of pure registered securities                                          none (AWAS)  na
                                                              MOTI-BABCITMMXXX-12345-07
               Temporary holding of registered securities in issuer register    112                                                                                RECA          Blocking
                reserved upon a corporate action instruction

    000       Permanent holding of bearer securities                                                 none (AWAS)  na

               Temporary holding of bearer securities reserved upon a    110                                                                               CUS1          Blocking
                 corporate action instruction
                                                              MOTI-BABCITMMXXX-23456-00
               Temporary holding - direct payment on bearer securities
    014                                                                          ECOM         Earmarking                 without commission

               Temporary holding – bearer securities account excluded    015                                                                                      EREF         Earmarking
               from direct payment

    001       Permanent holding of administered registered Securities                                   none (AWAS)  na

                                                              MOTI-BABCITMMXXX-34567-04
               Temporary holding of administered registered securities
    111                                                                                RECA          Blocking                reserved upon a corporate action instruction





15 | V.03 May 2026

                                                                PRIVATE

## PDF page 16
                                                                                    SDD ACCOUNT STRUCTURE



     Issuer CSD market practices in terms of accounts                       Euronext Securities Milan structure

     Account                                                                    Euronext Securities Milan sample of                        Restriction                     Definition                                                                                                         Restrictions
     Nature (AN)                                                                          security account number                               type

               Temporary holding of administered registered outturn
    045                                                                                     E045          Blocking                   securities awaiting registration by IRI/BRN

               Temporary holding - direct payment on administered
    016                                                                          ECOM         Earmarking                  registered securities without commission

               Temporary holding - administered registered securities
    017                                                                                      EREF         Earmarking                account excluded from direct payment

               Permanent holding of broker – transit account for brokerage
    010                                                       MOTI-BABCITMMXXX-45678-06   none (AWAS)  na                    activity


3.7 Link between securities account and cash account


To ensure proper settlement of Delivery-versus-Payment (DVP) operations and corporate actions in T2S, each participant’s security
account must be linked to a Dedicated Cash Account (DCA). Under T2S regulations, these links are immutable—modifications require
the link to be closed and re-established with updated parameters.

The security account is connected to the DCA through the Credit Memorandum Balance (CMB). Once the Payment Bank authorizes the
use of a DCA, Euronext Securities Milan can establish the security account - DCA link using data provided by the client. This link can
only be created if the client's Party BIC is listed among those authorized via CMB to access the specified DCA. Additionally, a single
security account may be linked to multiple DCAs to support both settlement and self-collateralization activities.





16 | V.03 May 2026

                                                                PRIVATE

## PDF page 17
                                                 SDD ACCOUNT STRUCTURE



4. Glossary


Below are the definitions of terms used in this document. Unless otherwise specified, these
definitions apply throughout

 Terms                  Definitions

                       The account nature is part of the French Issuer CSD accounting
 Account nature          structure. Account natures are used to segregate different balances
                              of securities (ISIN).

                               Classification assigned to an account to distinguish usage of the
 Account type
                          account within Euronext Securities Milan systems.

                           Registered securities managed by a Custodian. The Custodian is in
 Administered           charge of the accounting of the shares and has the responsibility of
 registered securities    updating the register with any changes that may occur regarding its
                                 client, a shareholder of the company.


                          Balance of financial instruments that are freely available with no AWAS
                               specific additional status.


                             Restriction applied to a securities position or account that prevents
 Blocking                the affected securities from being used or settled until the block is
                                   lifted.

                         Bordereau de Reference Nominative – refers to Euroclear France’s BRN
                             detailed service description.

                      An entity that has direct contractual and operational relationship
                           with Euronext Securities Milan generally holding accounts and
 Client
                           accessing services such as safekeeping, settlement and corporate
                             actions.

 CLIMP                  Euronext Securities Milan Client Membership Platform.

 CSD                      Central Securities Depository.

                             Securities held as electronic book entries in securities accounts at a
 Dematerialised
                            Central Securities Depository, where individual end-investor details
 security
                          are not recorded.


                          Dedicated Cash account used to settle the cash leg of a securities
 DCA                      transactions and to process cash movements related to corporate
                            actions within systems like TARGET2-Securities (T2S).





17 | V.03 May 2026

                                        PRIVATE

## PDF page 18
                                                 SDD ACCOUNT STRUCTURE




 Terms                  Definitions

                       The process of specifying that a quantity of a security in a securities
                          account is only eligible for specific types of transactions or
                           processes. For example, a bank can earmark a securities position in
                        a securities account for use as eligible collateral. Earmarking

                         Earmarking can be requested or lifted by sending an intra-position
                     movement (semt.013) message or a settlement instruction (e.g.,
                           sese.023).


                       The Information on Registered Investors (IRI) is a set of information
                        used to manage the accurate identification of shareholders by the
                             Issuer, and to facilitate the exchange of shareholder information
 IRI                   between Custodians and Issuers/Registrars in a set format. IRI
                       messages (IRIs) play a central role in enabling seamless
                        communication and ensuring that shareholder data is transmitted
                       and recorded accurately.


                             Individual Segregation account designed to hold and isolate the
 IS
                           assets of a single client.

                     A company or legal entity that creates and issues shares to raise
                               capital. The Issuer is responsible for registering the shares,
 Issuer                   maintaining shareholder records and complying with regulatory
                          requirements related to the issuance and management of those
                               securities.

                     A Central Securities Depository (CSD) where all the securities are
                                    initially recorded and from which they are created and distributed.
 Issuer CSD            The Issuer CSD is responsible for the initial registration,
                           safekeeping, and central administration of the securities on behalf of
                          the Issuer.

                     A mirror account is a securities account the investor CSD opens in
                                    its books for itself. It reflects the securities positions an investor
 Mirror account        CSD holds in an omnibus account in the book of the issuer CSD.
                        Each omnibus account is always linked to one and only one mirror
                           account.

                      Omnibus segregated account designed to separate the assets of
 OM
                            multiple clients within a single account.

                     A security account in the books of the issuer CSD for the investor
 Omnibus account      CSD which holds the security positions owned by all the participants
                              of the investor CSD for the relevant security.

                   Own segregated account used to hold and segregate the assets that
 OW
                          are owned directly by the account holder.

                         Pure Registered Securities – registered securities managed by the
                           Issuer itself if they have an account at the CSD, or by a designated
 Pure registered          registered agent. The Issuer or their representative is in charge of
 securities               the accounting of the shares and has the responsibility of updating
                          the register with any change that may occur regarding the
                           shareholder.



18 | V.03 May 2026

                                        PRIVATE

## PDF page 19
                                                 SDD ACCOUNT STRUCTURE




 Terms                  Definitions

                           For registered securities, the shareholder is registered in the Registered securities
                              register of the company for the number of securities they hold.

                             Securities Account, book-entry account used to record, hold and
 SAC                 manage securities such as stocks, bonds or other financial
                           instruments.





This document is for information purposes only. The information and materials contained in this document are provided ‘as is’
without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of the content,
Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damages of any nature
ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication shall form
the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the exchanges
operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary rights and
interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any form
without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext
is located at euronext.com/terms-use.
© 2026, Euronext N.V. - All rights reserved.


19 | V.03 May 2026

                                        PRIVATE

## PDF page 20
                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





                  euronext.com/post-trade


20 | Subtitle text, Verdana 9pt, Left aligned

                                        PRIVATE