# Format specifications

Source: https://www.euronext.com/sites/default/files/2024-07/Format%20Specifications%20v%200.1_0.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

Semantic versioning

This document overall use the concept of semantic versioning, a common and easily
understandable   industry  standard   in   large-scale  software  management.  See
https://semver.org/ for further information. Most importantly:

    -  The version always consists of three numbers: MAJOR.MINOR.PATCH.

    -   If the MAJOR version is increased (e.g. from 2.1.0 to 3.0.0), this marks changes
       that are incompatible to the previous version, meaning that an updated data
       input format must be used. All users of the KaFE interface should adjust the
      data they provide to the latest version.

    -   If the MINOR version is increased (e.g. from 2.0.0 to 2.1.0), this marks functionality
       that has been added in a backwards-compatible manner. Existing inputs can
       continue to be used, but new features, new information or new explanations might
      be available.

    -   If the PATCH version  is increased (e.g. from 2.0.0 to 2.0.1), this marks
      backwards-compatible bug fixes. No change in input data is needed.

Changelog

Since version 3.0.0, the changes listed in the changelog below are classified according
to whether they relate to a MAJOR, a MINOR or a PATCH change.


 Version  Date         Changes





                                1

                                                 Confidential

## PDF page 2

3.0.0     2024-05-22   MAJOR changes (action required):
                               -  Use version 3 in the “meta” sheet. Make sure to
                              use the updated templates. Find updated
                                templates with demo data here.
                               -  Removed the field
                                   “CreditorNat/General_Data/Nationality” from the
                                     “creditorsNatural” sheet and this documentation,
                            because it is not needed by the BOP anymore.

                  MAJOR changes (incompatibilities with version 2):
                                -  Added section 5.4 (Character set limitations).
                               -  Added BOP-defined length restrictions to most
                                      fields with type “String” in section 6.
                               -  Marked “generalData/LegalForm” in
                                     “creditorsJuridical” as required.
                               -  Marked “Bank/Account/BIC” and
                              “Bank/Account/IBAN” in both sheets
                                   “creditorsNatural” and “creditorsJuridical” as
                                   required.
                               -  Marked the fields relating to a beneficiary’s TIN as
                                  required, i.e. “CreditorNat/General_Data/
                             IDNumber_CountryOfResidence” (in
                                   “creditorsNatural”) and “CreditorJur/General_Data/
                             IDNumber_CountryOfResidence” (in
                                      “creditorsJuridical”).

                   MINOR changes:
                               -  Added section on “Semantic versioning” above.
                               -  Added section 2.3 (Terminology and roles),
                                  explaining the terms “Creditor”, “Authorized
                                  representative” and “Authorized recipient”.
                               -  Added note to section 5.2 (Required files) that
                          XLSX must be provided, not CSV.
                               -  Added link to demo data to section 5.5 (Further
                                 resources).
                               -  Added section 5.3 (Data types), explaining the





                               2

                                               Confidential

## PDF page 3

                                types “String”, “Number” and “Boolean”.
                                -  Added section 6.4.2 (Tax certificates), explaining
                              the format and legal basis for tax certificates.

                   PATCH changes:
                               -  Various formatting improvements.

3.1.0     2024-07-01   MINOR changes:
                               -  Marked “CreditorNat/German_TaxOffice/
                                Inquiry_TaxReturn” in “creditorsNatural” as
                                   required.
                               -  Marked “CreditorJur/German_TaxOffice/
                                Inquiry_TaxReturn” in “creditorsJuridical” as
                                   required.
                               -  Marked “AuthorizedRep/General_Data/LegalForm”
                                      in “creditorsNatural” and “creditorsJuridical” as
                                   required.
                               -  Market “Economic_Ownership/Ownership_and_
                              Right_To_Use” in “income” as required.
                               -  Added section 5.4 (Required, optional and
                                  semi-required fields), including input data cluster
                                 constraint details.
                               -  Made the contents of the “Required” columns in
                                 section 6 more precise.

3.2.0     2024-07-03   MINOR changes:
                               -  Marked “TaxTreatment/Taxation_Treatment” in
                                     “creditorsJuridical” as required.
                               -  Marked “Business_Establishment/Business_
                               Establishment_DE” in “income” as required.
                               -   Clarified “Required” column contents for
                                  “InvTaxAct/StatusCertificateDetails/…” fields in
                                      “creditorsJuridical”.
                               -   Clarified “Description” and “Required” column
                                contents for “Depositary_Receipts/…” fields in
                                 “income”.





                               3

                                               Confidential

## PDF page 4

1  Excel format specification

1.1 Sheet “creditorsNatural”

    -   clusters
           -  CREDITOR_ADDRESS
           -  CREDITOR_POSTBOX
           -  REP_ADDRESS
           -  REP_POSTBOX
           -  DIFF_PAYEE
    -   cluster constraints
           -   either CREDITOR_ADDRESS or CREDITOR_POSTBOX or both
           -   either REP_ADDRESS or REP_POSTBOX or both
           -  DIFF_PAYEE is optional


 Name              Description                  Data Type       Required

 id                      Arbitrary, but unique creditor      String           Yes
                       ID, e.g. a customer number

 generalData/Count   Country/                           String           Yes
 ry                   Organisation (Land/                  (two lower case
                                                                                            letters, ISO 3166-1
                       Organisation)1                            alpha-2)

 CreditorNat/Gener    Withholding tax number           String         No
 al_Data/Withholdin   (Entlastungs-Steuernummer)2
 gTaxNumber

 CreditorNat/Gener    Form of address (Anrede)         String         No
 al_Data/FormOfAd                                                         (either “Frau” or
                                                                                 “Herr”)
 dress

 CreditorNat/Gener   Form of address/title (Titel /        String         No
 al_Data/FormOfTitl   akademischer Grad)              (maximum length: 100
                                                                                characters)
 e

 CreditorNat/Gener   Name/Family name (Name)        String           Yes
 al_Data/Name                                            (maximum length: 256
                                                                                characters)

 CreditorNat/Gener    Given name (Vorname)            String           Yes
 al_Data/GivenNam                                       (maximum length: 256
                                                                                characters)
 e



1 This refers to the beneficiary’s country of tax residency.
2 Note that this is a tax number which might have been assigned to the beneficiary previously if
the beneficiary ever had contact with the BZSt before. This field does not refer to the
beneficiary’s tax identification number (TIN). The TIN shall instead be given in the field
“CreditorNat/General_Data/IDNumber_CountryOfResidence”.


                                4

                                                 Confidential

## PDF page 5

CreditorNat/Gener    Date of birth (Geburtsdatum)       String           Yes
al_Data/Birthday                                                     (date as
                                                         YYYY-MM-DD)

CreditorNat/Gener   ID number country of             String           Yes
al_Data/IDNumber_   residence/territory (ID-Nummer   (maximum length: 100
                                                                              characters)
CountryOfResiden   Ansässigkeitsstaat/Gebiet)
ce

CreditorNat/Addre   Street (Straße)                     String         No
ss/Street                                                  (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
                                                                                 ADDRESS)

CreditorNat/Addre   Street number (Hausnummer)     String         No
ss/StreetNumber                                         (maximum length: 10      (cluster:
                                                                              characters)            CREDITOR_
                                                                                 ADDRESS)

CreditorNat/Addre   Additional address details         String         No
ss/AdditionalAddre   (Adresszusatz)                     (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
ssDetails                                                                       ADDRESS)

CreditorNat/Addre    District (Ortsteil)                   String         No
ss/District                                                 (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
                                                                                 ADDRESS)

CreditorNat/Addre   Postcode (Postleitzahl)            String           yes
ss/Postcode                                               (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
                                                                                 ADDRESS)

CreditorNat/Addre   City (Ort)                          String           yes
ss/City                                                    (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
                                                                                 ADDRESS)

CreditorNat/Addre   Region/Federal state (Region /    String         No
ss/Region_Federal    Bundesstaat)                       (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
State                                                                           ADDRESS)

CreditorNat/Addre   Country (Staat)                    String           yes
ss/Country                                                       (two lower case            (cluster:
                                                                                          letters, ISO 3166-1      CREDITOR_
                                                                             alpha-2)              ADDRESS)

CreditorNat/Addre    P.O. box (Postfach)                String           yes
ss/PO_Box                                                  (maximum length: 30      (cluster:
                                                                           characters)            CREDITOR_
                                                                                 POSTBOX)

CreditorNat/Addre   P.O. box: Postcode                String           yes
ss/Postcode           (Postleitzahl)                       (maximum length: 100     (cluster:
                                                                              characters)            CREDITOR_
                                                                                 POSTBOX)

CreditorNat/Addre   P.O. box: City (Ort)                 String           yes
ss/City                                                    (maximum length: 100
                                                                              characters)



                               5

                                               Confidential

## PDF page 6

                                                                                                                     (cluster:
                                                                                   CREDITOR_
                                                                                 POSTBOX)

CreditorNat/Conta   Phone (Telefon)                   String         No
ct/Phone

CreditorNat/Conta   Fax                                String         No
ct/Fax

CreditorNat/Conta   Own reference (reason for          String         No
ct/Own_Reference   payment in the case of a         (maximum length: 140
                                                                              characters)
                    refund) (Eigene Referenz
                 (Verwendungszweck bei
                     Erstattung))

CreditorNat/Germa   Has a tax return already been   Boolean         Yes
n_TaxOffice/Inquiry   filed with a German tax office in
_TaxDeclaration     which a request was made for
                    the capital income tax due in
                Germany to be credited?
                 (Wurde bereits eine
                    Steuererklärung bei einem
                  deutschen Finanzamt
                      eingereicht, in der die
                 Anrechnung der hier geltend
                 gemachten Kapitalertragsteuer
                   beantragt wurde?)

CreditorNat/Germa   State (Land)                        String, one of       Only when
                                                                                                                “./Inquiry_Tax
n_TaxOffice/TaxNu                                   the following:       Return” is
mber/State                                                                                             true
                                                             de-bw (Baden-Württe
                                                          mberg /
                                                                Baden-Württemberg)

                                                                     de-by (Bavaria /
                                                                        Bayern)

                                                                    de-be (Berlin / Berlin)

                                                                    de-bb (Brandenburg /
                                                                     Brandenburg)

                                                                   de-hb (Bremen /
                                                                 Bremen)

                                                                   de-hh (Hamburg /
                                                               Hamburg)

                                                                  de-he (Hesse /
                                                                  Hessen)

                                                            de-mv (Mecklenburg-
                                                               Western Pomerania /
                                                                Mecklenburg-Vorpom
                                                                mern)

                                                                           de-ni (Lower Saxony /
                                                                     Niedersachsen)



                               6

                                               Confidential

## PDF page 7

                                                               de-nw (North
                                                                        Rhine-Westphalia /
                                                                        Nordrhein-Westfalen)

                                                                         de-rp (Rhineland-Palat
                                                                               inate /
                                                                            Rheinland-Pfalz)

                                                                                  de-sl (Saarland /
                                                                           Saarland)

                                                                      de-sn (Saxony /
                                                                      Sachsen)

                                                                             de-st (Saxony-Anhalt /
                                                                          Sachsen-Anhalt)

                                                                   de-sh (Schleswig-Hols
                                                                               tein /
                                                                         Schleswig-Holstein)

                                                                          de-th (Thuringia /
                                                                        Thüringen)

CreditorNat/Germa   Tax number (Steuernummer)      String                Only when
                                                                                                                “./Inquiry_Tax
n_TaxOffice/TaxNu                                                                        Return” is
mber/Number                                                                                         true

CreditorNat/Germa  Was a request made to a       Boolean         Yes
n_TaxOffice/Inquiry  German tax office for the
_Unlimited_TaxLiabi  person specified as the creditor
lity                   of the capital income to be
                    treated as a taxpayer with
                       unlimited tax liability, or is there
                 an intention to make such a
                    request? (Wurde für die unter
                    Gläubiger der Kapitalerträge
                 angegebene Person bei einem
                  deutschen Finanzamt ein
                   Antrag auf Behandlung als
                   unbeschränkt steuerpflichtig
                       gestellt oder besteht die
                    Absicht einen solchen Antrag
                  zu stellen?)

AuthorizedRep/Ge    Authorisation as                   String, one of    Yes
neral_Data/TypeOf   (Bevollmächtigung als)            the following:
Representative
                                                         BEVOLLMAECHTIGTE
                                                        R (Authorised
                                                                            representative /
                                                                              Bevollmächtigter)

                                                             GESETZLICHER_VERT
                                                       RETER (Legal
                                                                         representative /
                                                                           Gesetzlicher Vertreter)

                                                           INSOLVENZVERWALTE
                                                        R (Insolvency
                                                                             administrator /
                                                                             Insolvenzverwalter)


                               7

                                               Confidential

## PDF page 8

                                                              LIQUIDATOR (Liquidat
                                                                                or / Liquidator)

                                                       VERFUEGUNGSBERAE
                                                           CHTIGTER (Person
                                                                          with power of
                                                                              disposal / Verfügungs
                                                                                 berechtigter)

                                                    VERMOEGENSVERWA
                                                             LTER (Asset manager /
                                                                       Vermögensverwalter)

                                                             VERTRETER_§81AO (R
                                                                         epresentative
                                                                          pursuant to section 81
                                                                            of the Fiscal
                                                              Code / Vertreter
                                                                  §81AO)

                                                     ZWANGSVERWALTER
                                                                                (Administrative
                                                                               receiver /
                                                                        Zwangsverwalter)

                                                            SONSTIGER_VERTRET
                                                           ER (Other
                                                                            representative /
                                                                            Sonstiger Vertreter)

                                                               FINANZINSTITUT (Fin
                                                                                  ancial institution /
                                                                                     Finanzinstitut)

AuthorizedRep/Ge    Name/Company/Corporation       String           Yes
neral_Data/Name   (Name / Firma / Gesellschaft)     (maximum length: 256
                                                                              characters)

AuthorizedRep/Ge    Legal form (Rechtsform)           String           Yes
neral_Data/LegalFo                                                       (either "N" for a
                                                                              natural representative
rm                                                                                   entity, "J" for a legal
                                                                                    entity or "T" for a
                                                                           transparent entity)

AuthorizedRep/Ge  Form of address (Anrede)         String         No
neral_Data/FormOf                                                         (either “Frau” or
                                                                               “Herr”)
Address

AuthorizedRep/Ge   Contact person                    String         No
neral_Data/Contact    (Ansprechpartner)                  (maximum length: 256
                                                                              characters)
Person

AuthorizedRep/Ad     Street (Straße)                     String         No
dress/Street                                              (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad   Street number (Hausnummer)     String         No
dress/StreetNumb                                        (maximum length: 10      (cluster: REP_
                                                                              characters)            ADDRESS)
er





                               8

                                               Confidential

## PDF page 9

AuthorizedRep/Ad   Additional address details         String         No
dress/AdditionalAd   (Adresszusatz)                     (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)
dressDetails

AuthorizedRep/Ad      District (Ortsteil)                   String         No
dress/District                                             (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad    Postcode (Postleitzahl)            String           yes
dress/Postcode                                           (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad     City (Ort)                          String           yes
dress/City                                                 (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad    Region/Federal state (Region /    String         No
dress/Region_Fede   Bundesstaat)                       (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)
ralState


AuthorizedRep/Ad     Country (Staat)                    String           yes
dress/Country                                                   (two lower case            (cluster: REP_
                                                                                          letters, ISO 3166-1      ADDRESS)
                                                                             alpha-2)

AuthorizedRep/Ad   P.O. box (Postfach)                String           yes
dress/POBox_Addr                                         (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/POBox

AuthorizedRep/Ad   P.O. box: Postcode                String           yes
dress/POBox_Addr     (Postleitzahl)                       (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/Postcode

AuthorizedRep/Ad   P.O. box: City (Ort)                 String           yes
dress/POBox_Addr                                         (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/City

AuthorizedRep/Co   Phone (Telefon)                   String         No
ntact/Phone

AuthorizedRep/Co   Fax                                String         No
ntact/Fax

AuthorizedRep/Aut   Duration of the authorisation      String (one of    No
horization/Duration   (Dauer der Bevollmächtigung)    the following:

                                                         BEGRENZT (For a
                                                                                  limited time /
                                                                          Begrenzt)

                                                        UNBEGRENZT (Indefin
                                                                                               itely / Unbegrenzt)

AuthorizedRep/Aut   Time period (Zeitraum), start      String                Only when
                                                                                                              “./Duration” is
horization/Period/fr   date                                        (date as               “BEGRENZT”                                                         YYYY-MM-DD)
om



                               9

                                               Confidential

## PDF page 10

AuthorizedRep/Aut    Time period (Zeitraum), end       String                Only when
                                                                                                              “./Duration” is
horization/Period/t   date                                        (date as               “BEGRENZT”                                                         YYYY-MM-DD)
o

AuthorizedRep/Aut     Is the authorised person an      Boolean         Yes
horization/Authoriz    authorised recipient? (Besteht
edRecipient          eine Empfangsvollmacht?)

Bank/Name        Name of the bank (Name der       String           Yes
                  Bank)                              (maximum length: 256
                                                                              characters)

Bank/City             City (Ort)                          String           Yes
                                                           (maximum length: 100
                                                                              characters)

Bank/Country         Country/territory (Staat /          String           Yes
                     Gebiet)                                 (two lower case
                                                                                          letters, ISO 3166-1
                                                                             alpha-2)

Bank/AccountHold   Name of the account holder       String           Yes
er              (Name des Kontoinhabers)       (maximum length: 256
                                                                              characters)

Bank/Account/BIC    BIC                                 String           Yes

Bank/Account/IBA    IBAN                               String           Yes
N

Bank/DifferentPaye   Deviating payment recipient:      String           yes
e/Name            Name/Family name (Name)       (maximum length: 256    (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String         No
e/FirstName         Given name (Vorname)            (maximum length: 256    (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String           yes
e/Street              Street (Straße)                     (maximum length: 100     (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String           yes
e/StreetNumber      Street (Hausnummer)             (maximum length: 20     (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye    Deviating payment recipient:      String           yes
e/Postcode         Postcode (Postleitzahl)             (maximum length: 100     (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye    Deviating payment recipient:      String           yes
e/City                 City (Ort)                          (maximum length: 100     (cluster:
                                                                              characters)             DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String           yes
e/Country           Country (Staat)                       (two lower case            (cluster:
                                                                                          letters, ISO 3166-1      DIFF_PAYEE)
                                                                             alpha-2)




                               10

                                               Confidential

## PDF page 11

Bank/DifferentPaye   Deviating payment recipient: Is   Boolean         yes
e/Assignment_or_C    it an assignment of debt or a                                      (cluster:
                                                                                          DIFF_PAYEE)
ollections            debt collection service? (Es
                     handelt sich um eine Abtretung
                    oder Inkassodienstleistung)

Residence/NonResi   At the time of receiving the     Boolean         Yes
dency_DE          income from capital, was the
                      creditor of the capital income
                     resident in the country of
                    residence specified, and did
                    the creditor have neither their
                    place of residence nor habitual
                 abode in the Federal Republic
                     of Germany at this time? (War
                   der Gläubiger der
                       Kapitalerträge im Zeitpunkt des
                    Zuflusses des Kapitalertrags im
                 angegebenen
                     Ansässigkeitsstaat ansässig
                 und hatte zu diesem Zeitpunkt
                 weder seinen Wohnsitz noch
                   einen gewöhnlichen Aufenthalt
                       in der Bundesrepublik
                   Deutschland?)

TaxTreatment/Taxa  In the year in which they          String (one of       Only when
                                                                                                  “generalData
tion_Treatment       received the capital income,      the following:       /Country” is
                how is the                                                            “ch”
                                                         TRANSPARENT (Trans
                   person/company/other legal        parent / Transparent)
                   arrangement specified as the
                       creditor treated for tax            INTRANSPARENT (Op
                                                                aque / Intransparent)
                    purposes in their country of
                     residence?

TaxTreatment/Citiz  Was the person with limited tax   Boolean              Only when
                                                                                                  “generalData
enship_not_Switzer    liability subject to unlimited tax                            /Country” is
land/In_Germany_M    liability in Germany for at least                                “ch” and the
in_5_Years_Taxable   five years? (Waren Sie in                                       beneficiary
                                                                                    does not
                    Deutschland mindestens fünf                           have Swiss
                    Jahre unbeschränkt                                                 citizenship
                     einkommensteuerpflichtig?)

TaxTreatment/Citiz   Did the unlimited tax liability in   Boolean              Only when
                                                                                                  “generalData
enship_not_Switzer  Germany end in the due year or                           /Country” is
land/In_Germany_T   in the five calendar years                                        “ch” and the
ax_Liability_Ended   preceding the oldest inflow                                    beneficiary
                                                                                    does not
                     included in the application?                             have Swiss
                    (Hat Ihre unbeschränkte                                          citizenship
                    Einkommensteuerpflicht in
                    Deutschland im Fälligkeitsjahr



                               11

                                               Confidential

## PDF page 12

                    oder in den vergangenen fünf
                    Kalenderjahren geendet?)

Questions/Explanat    Explanatory notes                 String         No
oryNotes            (Erläuterungen)

Questions/Explanat   Documents relating to the       Boolean        No
oryAttachmentsIncl   explanatory notes have been
uded               attached (Anhänge zu den
                     Erläuterungen sind dem Antrag
                     beigefügt)





                               12

                                               Confidential

## PDF page 13

1.2  Sheet “creditorsJuridical”

    -   clusters
           -  CREDITOR_ADDRESS
           -  CREDITOR_POSTBOX
           -  REP_ADDRESS
           -  REP_POSTBOX
           -  DIFF_PAYEE
    -   cluster constraints
           -   either CREDITOR_ADDRESS or CREDITOR_POSTBOX or both
           -   either REP_ADDRESS or REP_POSTBOX or both
           -  DIFF_PAYEE is optional


 Name              Description                  Data Type       Required

 id                      Arbitrary, but unique creditor     String           Yes
                       ID, e.g. a customer number

 generalData/Count   Country/Organisation              String           Yes
 ry                    (Land/Organisation)3                 (two lower case letters,
                                                                ISO 3166-1 alpha-2)

 generalData/Legal    Legal form (Rechtsform)          String           Yes
 Form                                                                           (either "N" for a natural
                                                                              representative entity,
                                                                                       "J" for a legal entity or
                                                                            "T" for a transparent
                                                                                        entity)

 generalData/JP_Sp     Specific legal form                String (one of       Only when
                                                                                                    “generalData
 ecificLegalForm     (Ausprägung)                   the following:        /LegalForm”
                                                                                                                                           is “J”
                                                           AV (Pension scheme /
                                                                                 Altervorsorgeeinrichtu
                                                                          ng)

                                                                    F (Fund / Fonds)

                                                       G (Non-profit company
                                                                                            / Gemeinnützige
                                                                                   Gesellschaft)

                                                    H (Public authority /
                                                                               Hoheitsträger)

                                                                INV (Investment fund
                                                                        pursuant to
                                                                           the Investment Tax Act
                                                                                            / Investmentfonds i. S.
                                                                                     d. InvStG)

                                                        KAPG (Corporation / K
                                                                                  apitalgesellschaft)

                                                                    PF (Pension fund/
                                                                        Pensionsfonds))



3 This refers to the beneficiary’s country of tax residency.


                                13

                                                 Confidential

## PDF page 14

 generalData/TP_Sp   Specific legal form                String (one of       Only when
                                                                                                    “generalData
 ecificLegalForm      (Ausprägung)                   the following):       /LegalForm”
                                                                                                                                           is “T”
                                                           AV (Pension scheme /
                                                                                 Altervorsorgeeinrichtu
                                                                          ng)

                                                                    F (Fund / Fonds)

                                                       G (Non-profit company
                                                                                            / Gemeinnützige
                                                                                   Gesellschaft)

                                                    H (Public authority /
                                                                               Hoheitsträger)

                                                                INV (Investment fund
                                                                        pursuant to
                                                                           the Investment Tax Act
                                                                                            / Investmentfonds i. S.
                                                                                     d. InvStG)

                                                                    PF (Pension fund/
                                                                       Pensionsfonds)

                                                       PG (Partnership /
                                                                          Personengesellschaft)

 CreditorJur/Genera    File number in the format St I B   String          No
 l_Data/FileNumber   3 MU - XXX / XXXXXX (if
                  known) (Aktenzeichen im
                   Format St I B 3 MU - XXX /
                   XXXXXX (soweit bekannt))

 CreditorJur/Genera   Withholding tax number           String          No
 l_Data/Withholding   (Entlastungs-Steuernummer)4
 TaxNumber

 CreditorJur/Genera   Name/Company/Corporation      String           Yes
 l_Data/Name         (Name/Firma/Gesellschaft)        (maximum length: 256
                                                                                characters)

 CreditorJur/Genera   Legal form of company           String           Yes
 l_Data/CompanyFo   (Gesellschaftsform)               (maximum length: 100
                                                                                characters)
 rm

 CreditorJur/Genera   Contact person                   String          No
 l_Data/ContactPers   (Ansprechperson)                  (maximum length: 256
                                                                                characters)
 on

 CreditorJur/Genera   Date of establishment            String           Yes
 l_Data/DateOfEsta   (Gründungsdatum)                   (date as
                                                          YYYY-MM-DD)
 blishment




4 Note that this is a tax number which might have been assigned to the beneficiary previously if
the beneficiary ever had contact with the BZSt before. This field does not refer to the
beneficiary’s tax identification number (TIN). The TIN shall instead be given in the field
“CreditorJur/General_Data/IDNumber_CountryOfResidence”.


                                14

                                                 Confidential

## PDF page 15

CreditorJur/Genera   Company ID country of            String           Yes
l_Data/IDNumber_C   residence / territory                (maximum length: 100
                                                                              characters)
ountryOfResidence   (Unternehmens ID
                       Ansässigkeitsstaat/Gebiet)

CreditorJur/Genera   Place of effective management   String          No
l_Data/PlaceOfEffe   (Ort der tatsächlichen            (maximum length: 100
                                                                              characters)
ctiveManagement    Geschäftsleitung)

CreditorJur/Genera   Place of establishment (Ort der   String          No
l_Data/PlaceOfEsta   Errichtung)                        (maximum length: 100
                                                                              characters)
blishment

CreditorJur/Addres   Street (Straße)                    String          No
s/Street                                                  (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres   Street Number (Hausnummer)    String          No
s/StreetNumber                                          (maximum length: 10       (cluster:
                                                                              characters)             CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres   Additional address details         String          No
s/AdditionalAddres   (Adresszusatz)                    (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
sDetails                                                                        ADDRESS)

CreditorJur/Addres   District (Ortsteil)                  String          No
s/District                                                 (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres  Postcode (Postleitzahl)           String            yes
s/Postcode                                               (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres   City (Ort)                          String            yes
s/City                                                     (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres  Region / Federal state (Region /   String          No
s/Region_FederalSt    Bundesstaat)                      (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
ate                                                                             ADDRESS)

CreditorJur/Addres  Country (Staat)                   String            yes
s/Country                                                        (two lower case letters,    (cluster:
                                                               ISO 3166-1 alpha-2)     CREDITOR_
                                                                                 ADDRESS)

CreditorJur/Addres   P.O. box (Postfach)                String            yes
s/POBox_Address/                                        (maximum length: 30       (cluster:
                                                                          characters)            CREDITOR_
POBox                                                                         POSTBOX)





                               15

                                               Confidential

## PDF page 16

CreditorJur/Addres   P.O. box: Postcode                String            yes
s/POBox_Address/   (Postleitzahl)                       (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
Postcode                                                                       POSTBOX)

CreditorJur/Addres   P.O. box: City (Ort)                String            yes
s/POBox_Address/                                       (maximum length: 100     (cluster:
                                                                              characters)             CREDITOR_
City                                                                            POSTBOX)

CreditorJur/Contac  Phone (Telefon)                   String          No
t/Phone

CreditorJur/Contac  Fax                                String          No
t/Fax

CreditorJur/Contac  Own reference (plus reason for   String          No
t/OwnReference    payment in the case of a         (maximum length: 140
                                                                              characters)
                      refund) (Eigene Referenz (auch
                 Verwendungszweck bei
                     Erstattung))

CreditorJur/Germa   Has a tax return already been   Boolean         Yes
n_TaxOffice/Inquiry   filed with a German tax office
_TaxReturn           in which a request was made
                       for the capital income tax due
                       in Germany to be credited?
                 (Wurde bereits eine
                    Steuererklärung bei einem
                  deutschen Finanzamt
                      eingereicht, in der die
                 Anrechnung der hier geltend
                   gemachten Kapitalertragsteuer
                   beantragt wurde?)

CreditorJur/Germa    State (Land)                      String (one of       Only when
                                                                                                                “./Inquiry_Tax
n_TaxOffice/TaxNu                                   the following:        Return” is
mber/State                                                                                             true
                                                            de-bw (Baden-Württe
                                                         mberg /
                                                                Baden-Württemberg)

                                                                     de-by (Bavaria /
                                                                       Bayern)

                                                                    de-be (Berlin / Berlin)

                                                                   de-bb (Brandenburg /
                                                                     Brandenburg)

                                                                   de-hb (Bremen /
                                                                Bremen)

                                                                   de-hh (Hamburg /
                                                               Hamburg)

                                                                  de-he (Hesse /
                                                                 Hessen)

                                                           de-mv (Mecklenburg-


                               16

                                               Confidential

## PDF page 17

                                                              Western Pomerania /
                                                                Mecklenburg-Vorpom
                                                               mern)

                                                                          de-ni (Lower Saxony /
                                                                     Niedersachsen)

                                                               de-nw (North
                                                                       Rhine-Westphalia /
                                                                       Nordrhein-Westfalen)

                                                                        de-rp (Rhineland-Palati
                                                                      nate / Rheinland-Pfalz)

                                                                                 de-sl (Saarland /
                                                                           Saarland)

                                                                      de-sn (Saxony /
                                                                      Sachsen)

                                                                             de-st (Saxony-Anhalt /
                                                                         Sachsen-Anhalt)

                                                                  de-sh (Schleswig-Hols
                                                                               tein /
                                                                         Schleswig-Holstein)

                                                                         de-th (Thuringia /
                                                                        Thüringen)

CreditorJur/Germa   Tax number (Steuernummer)      String                 Only when
                                                                                                                “./Inquiry_Tax
n_TaxOffice/TaxNu                                                                        Return” is
mber/Number                                                                                         true

CreditorJur/Opting    Is the creditor a company that   Boolean         Yes
UnderCorpTaxAct/I   has opted to be treated like a
nquiryCorpTaxAct    corporation for tax purposes
Option_Creditor      pursuant to section 1a of the
                    Corporation Tax Act? (Handelt
                   es sich bei der Gläubigerin um
                    eine Gesellschaft, die gemäß §
                 1a KStG zur
                    Körperschaftsbesteuerung
                      optiert hat?)

CreditorJur/Opting   When will or did the company   String                 Only when
                                                                                                         “./InquiryCorp
UnderCorpTaxAct/   begin to be treated like a          (date as                 TaxActOption                                                         YYYY-MM-DD)
TaxationStart_Cred   corporation for tax purposes?                               _Creditor” is
itor                 (Ab wann beginnt oder begann                                  true
                     die Besteuerung wie bei einer
                      Kapitalgesellschaft?)

CreditorJur/Opting   Please provide the file number    String                 Only when
                                                                                                         “./InquiryCorp
UnderCorpTaxAct/  under which the option was                               TaxActOption
FileNumber        approved (Bitte geben Sie das                               _Creditor” is
                   Aktenzeichen an, unter dem                                   true
                     die Option genehmigt wurde)

CreditorJur/Opting   Did the company opt for        Boolean              Only when
                                                                                                         “./InquiryCorp
UnderCorpTaxAct/I   corporation tax in the country                              TaxActOption


                               17

                                               Confidential

## PDF page 18

nquiry_Option_Resi  where it has its registered                                    _Creditor” is
                                                                                                            true
dence                 office? (Wurde im Sitzstaat zur
                    Körperschaftsteuer optiert?)

AuthorizedRep/Ge    Authorisation as                  String (one of     Yes
neral_Data/TypeOf   (Bevollmächtigung als)            the following:
Representative
                                                        BEVOLLMAECHTIGTER
                                                                           (Authorised
                                                                            representative /
                                                                             Bevollmächtigter)

                                                            GESETZLICHER_VERTR
                                                       ETER (Legal
                                                                        representative /
                                                                           Gesetzlicher Vertreter)

                                                          INSOLVENZVERWALTE
                                                       R (Insolvency
                                                                            administrator /
                                                                             Insolvenzverwalter)

                                                              LIQUIDATOR (Liquidato
                                                                                                   r / Liquidator)

                                                       VERFUEGUNGSBERAE
                                                           CHTIGTER (Person
                                                                          with power of
                                                                           disposal / Verfügungsb
                                                                              erechtigter)

                                                     VERMOEGENSVERWAL
                                                          TER (Asset manager /
                                                                      Vermögensverwalter)

                                                             VERTRETER_§81AO (Re
                                                                        presentative pursuant
                                                                          to section 81 of the
                                                                                Fiscal Code / Vertreter
                                                                 §81AO)

                                                      ZWANGSVERWALTER (
                                                                            Administrative receiver
                                                                                             / Zwangsverwalter)

                                                           SONSTIGER_VERTRET
                                                          ER (Other
                                                                            representative /
                                                                           Sonstiger Vertreter)

                                                               FINANZINSTITUT (Fina
                                                                                      ncial institution /
                                                                                    Finanzinstitut)

AuthorizedRep/Ge    Name/Company/Corporation      String           Yes
neral_Data/Name   (Name / Firma / Gesellschaft)     (maximum length: 256
                                                                              characters)

AuthorizedRep/Ge    Legal form (Rechtsform)          String           Yes
neral_Data/LegalFo                                                      (either "N" for a natural
                                                                            representative entity,
rm                                                                                 "J" for a legal entity or
                                                                           "T" for a transparent
                                                                                      entity)





                               18

                                               Confidential

## PDF page 19

AuthorizedRep/Ge  Form of address (Anrede)        String          No
neral_Data/FormOf                                                        (either “Frau” or “Herr”)
Address

AuthorizedRep/Ge   Contact person                   String          No
neral_Data/Contact    (Ansprechpartner)                  (maximum length: 256
                                                                              characters)
Person

AuthorizedRep/Ad     Street (Straße)                    String          No
dress/Street                                              (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad   Street number (Hausnummer)    String          No
dress/StreetNumb                                       (maximum length: 10       (cluster: REP_
                                                                              characters)            ADDRESS)
er

AuthorizedRep/Ad   Additional address details         String          No
dress/AdditionalAd   (Adresszusatz)                    (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)
dressDetails

AuthorizedRep/Ad      District (Ortsteil)                  String          No
dress/District                                             (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad    Postcode (Postleitzahl)           String            yes
dress/Postcode                                           (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad     City (Ort)                          String            yes
dress/City                                                (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)

AuthorizedRep/Ad    Region/Federal state (Region /    String          No
dress/Region_Fede   Bundesstaat)                      (maximum length: 100     (cluster: REP_
                                                                              characters)            ADDRESS)
ralState

AuthorizedRep/Ad     Country (Staat)                   String            yes
dress/Country                                                   (two lower case letters,    (cluster: REP_
                                                                 ISO 3166-1            ADDRESS)
                                                                           alpha-2)

AuthorizedRep/Ad   P.O. box (Postfach)                String            yes
dress/POBox_Addr                                         (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/POBox

AuthorizedRep/Ad   P.O. box: Postcode                String            yes
dress/POBox_Addr     (Postleitzahl)                       (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/Postcode

AuthorizedRep/Ad   P.O. box: City (Ort)                String            yes
dress/POBox_Addr                                         (maximum length: 100     (cluster: REP_
                                                                              characters)            POSTBOX)
ess/City

AuthorizedRep/Co   Phone (Telefon)                   String          No
ntact/Phone




                               19

                                               Confidential

## PDF page 20

AuthorizedRep/Co   Fax                                String          No
ntact/Fax

AuthorizedRep/Aut   Duration of the authorisation     String (one of    No
horization/Duration   (Dauer der Bevollmächtigung)    the following:

                                                         BEGRENZT (For a
                                                                                 limited time / Begrenzt)

                                                        UNBEGRENZT (Indefini
                                                                                      tely / Unbegrenzt)

AuthorizedRep/Aut   Time period (Zeitraum), start     String                 Only when
                                                                                                              “./Duration” is
horization/Period/fr   date                                       (date as               “BEGRENZT”                                                         YYYY-MM-DD)
om

AuthorizedRep/Aut    Time period (Zeitraum), end      String                 Only when
                                                                                                              “./Duration” is
horization/Period/t   date                                       (date as               “BEGRENZT”                                                         YYYY-MM-DD)
o

AuthorizedRep/Aut     Is the authorised person an      Boolean         Yes
horization/Authoriz    authorised recipient? (Besteht
edRecipient          eine Empfangsvollmacht?)

Bank/Name        Name of the bank (Name der       String           Yes
                  Bank)                             (maximum length: 256
                                                                              characters)

Bank/City             City (Ort)                          String           Yes
                                                           (maximum length: 100
                                                                              characters)

Bank/Country         Country/territory (Staat /          String           Yes
                     Gebiet)                                 (two lower case letters,
                                                                 ISO 3166-1
                                                                           alpha-2)

Bank/AccountHold   Name of the account holder      String           Yes
er              (Name des Kontoinhabers)      (maximum length: 256
                                                                              characters)

Bank/Account/BIC    BIC                                String           Yes

Bank/Account/IBA    IBAN                               String           Yes
N

Bank/DifferentPaye   Deviating payment recipient:      String            yes
e/Name            Name/Family name (Name)       (maximum length: 256     (cluster:
                                                                              characters)              DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String          No
e/FirstName         Given name (Vorname)           (maximum length: 256     (cluster:
                                                                              characters)              DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String            yes
e/Street              Street (Straße)                    (maximum length: 100     (cluster:
                                                                              characters)              DIFF_PAYEE)




                               20

                                               Confidential

## PDF page 21

Bank/DifferentPaye   Deviating payment recipient:      String            yes
e/StreetNumber      Street (Hausnummer)             (maximum length: 20      (cluster:
                                                                              characters)              DIFF_PAYEE)

Bank/DifferentPaye    Deviating payment recipient:      String            yes
e/Postcode         Postcode (Postleitzahl)            (maximum length: 100     (cluster:
                                                                              characters)              DIFF_PAYEE)

Bank/DifferentPaye    Deviating payment recipient:      String            yes
e/City                 City (Ort)                          (maximum length: 100     (cluster:
                                                                              characters)              DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient:      String            yes
e/Country           Country (Staat)                       (two lower case letters,    (cluster:
                                                               ISO 3166-1 alpha-2)     DIFF_PAYEE)

Bank/DifferentPaye   Deviating payment recipient: It   Boolean          yes
e/Assignment_or_C    is an assignment of debt or a                                      (cluster:
                                                                                          DIFF_PAYEE)
ollections            debt collection service. (Es
                     handelt sich um eine Abtretung
                    oder Inkassodienstleistung)

Residence/NonResi   At the time of receiving the     Boolean         Yes
dency_DE          income from capital, was or is
                    the creditor of the capital
                  income resident in the country
                     of residence specified, and
                  does or did the creditor have
                     neither a registered office nor
                  a place of management in the
                    Federal Republic of Germany at
                        this time? (War oder ist der
                      Gläubiger der Kapitalerträge im
                    Zeitpunkt des Zuflusses des
                       Kapitalertrags im angegebenen
                     Ansässigkeitsstaat ansässig
                 und hatte zu diesem Zeitpunkt
                 weder einen Sitz noch den Ort
                   der Geschäftsleitung in der
                   Bundesrepublik Deutschland?)

InvTaxAct/Request  Was a status certificate         Boolean         Yes
ed_StatusCertificat  pursuant to section 7 (3) of the
e                 Investment Tax Act requested
                       for the creditor? (Wurde für
                 den Gläubiger der
                     Kapitalerträge eine
                   Statusbescheinigung nach § 7
                   Abs. 3 InvStG beantragt?)

InvTaxAct/StatusC   Period for which the status      String                 Only when
                                                                                                  “./Requested
ertificateDetails/Pe    certificate is issued (Zeitraum,     (date as                     _StatusCertifi                                                         YYYY-MM-DD)
riod/from             für den die                                                      cate” is true
                    Statusbescheinigung



                               21

                                               Confidential

## PDF page 22

                        ausgestellt ist), only needed
                  when

 InvTaxAct/StatusC   Period for which the status      String                 Only when
                                                                                                    “./Requested
 ertificateDetails/Pe    certificate is issued (Zeitraum,     (date as                     _StatusCertifi                                                          YYYY-MM-DD)
 riod/to                für den die                                                      cate” is true
                     Statusbescheinigung
                       ausgestellt ist)

 InvTaxAct/StatusC   Tax number as shown on          String                 Only when
                                                                                                    “./Requested
 ertificateDetails/Ta   status certificate                                                          _StatusCertifi
 xNumber           (Steuernummer lt.                                             cate” is true
                     Statusbescheinigung)

 InvTaxAct/SpecialI    Is the person specified as the   Boolean               Only when 5
                                                                                                                                   is true
 nvestmentFunds/Tr   creditor of the capital income a
 ansparencyOption    special investment fund within
                     the meaning of section 26 of
                     the Investment Tax Act that
                   used the transparency option
                       (section 30 of the Investment
                  Tax Act)? (Ist die unter
                     Gläubiger der Kapitalerträge
                  angegebene Person ein
                     Spezial-Investmentfonds im
                    Sinne des § 26 InvStG, welcher
                      die Transparenzoption (§ 30
                    InvStG) ausgeübt hat?)

 InvTaxAct/Refund/  Was a refund claim pursuant to  Boolean         Yes
 RefundClaim         section 7 (5) sentence 1 of the
                    Investment Tax Act relating to
                     the capital income specified in
                         this application made to the
                      party that withheld the tax?
                  (Wurde für die in diesem
                    Antrag aufgeführten
                      Kapitalerträge ein
                     Erstattungsanspruch nach § 7
                     Abs. 5 Satz 1 InvStG
                   gegenüber dem
                       Entrichtungspflichtigen geltend
                   gemacht?)

 InvTaxAct/Refund/   Were applications for a refund     Boolean         Yes
 RefundRequests      of the excess amount of tax
                     withheld submitted to the tax
                         office with jurisdiction for the


5 Is the person specified as the creditor of the capital income a special investment fund within
the meaning of section 26 of the Investment Tax Act? (Ist die unter Gläubiger der
Kapitalerträge angegebene Person ein Spezial-Investmentfonds im Sinne des § 26 InvStG?)


                                22

                                                 Confidential

## PDF page 23

                     party that withheld the tax or
                      to the Federal Central Tax
                       Office pursuant to section 11
                      (1) of the Investment Tax Act?
                  (Wurden bereits Anträge auf
                     Erstattung der zu viel
                     einbehaltenen
                      Kapitalertragsteuer beim
                     Betriebstättenfinanzamt des
                      Entrichtungspflichtigen/BZSt
                 gem. § 11 Abs. 1 InvStG
                        gestellt?)

TaxTreatment/Taxa  In the year in which they        String (one of     Yes
tion_Treatment      received the capital income,    the following:
               how is the
                                                         TRANSPARENT (Trans
                  person/company/other legal      parent / Transparent)
                  arrangement specified as the
                      creditor treated for tax           INTRANSPARENT (Opa
                                                               que / Intransparent)
                   purposes in their country of
                    residence? (Wie wird die/das
                    unter Gläubigerin der
                     Kapitalerträge angegebene
                    Person/Gesellschaft/abweiche
                 nde Rechtsgebilde im Jahr des
                    Zuflusses im
                     Ansässigkeitsstaat steuerlich
                    behandelt?)

Questions/Explanat    Explanatory notes                 String          No
oryNotes            (Erläuterungen)

Questions/Explanat   Documents relating to the      Boolean        No
ionsAttachmentsIn  explanatory notes have been
cluded             attached (Anhänge zu den
                     Erläuterungen sind dem Antrag
                     beigefügt)





                               23

                                               Confidential

## PDF page 24

1.3  Sheet “income”

    -   clusters
           -  DIFF_OWNER
    -   cluster constraints
           -  DIFF_OWNER is optional


 Name              Description                 Data Type        Required

 creditorId           Reference to one of the rows   String            Yes
                           in the “creditorsNatural” or the
                        “creditorsJuridical”
                    spreadsheet using their “id”

 incomeId             Arbitrary ID to identify this      String            Yes
                   income row, especially to be
                      able to match its attachments
                      to it

 CapitalIncome        Capital income (Kapitalertrag)    String (one of the   Yes
                                                            following:

                                                            KAPITALGESELLSCHAFT
                                                                     (Income from a
                                                                                non-listed company (e.g.
                                                                  a
                                                                   GmbH)/Ausschüttungen
                                                                                 nicht börsennotierter
                                                                               Kapitalgesellschaften (z.
                                                                              B. GmbH))

                                                           DIVIDENDEN (Dividends
                                                                   from listed
                                                                        shares/Dividenden aus
                                                                          börsennotierten Aktien)

                                                         GRENZKRAFTWERK_RHE
                                                                   IN (Income from a
                                                                        border power station on
                                                                          the Rhine/Einnahmen
                                                                    aus einem
                                                                        Grenzkraftwerk am
                                                                          Rhein)

                                                                STILLER_GESELLSCHAF
                                                           TER (Income from a
                                                                          shareholding in a
                                                                          business as a silent
                                                                               partner/
                                                               Einnahmen aus einer
                                                                               typisch stillen
                                                                                 Beteiligung)

                                                             GENUSSRECHTE_MIT_LI
                                                            QUIDATIONSERLOES
                                                                  (Income from profit
                                                                                   participation rights with
                                                                                   participation in
                                                                                      liquidation
                                                                     proceeds/Einnahmen
                                                                    aus Genussrechten mit



                                24

                                                 Confidential

## PDF page 25

                                                                            Beteiligung am
                                                                                 Liquidationserlös)

                                                        GENUSSRECHTE_OHNE_
                                                            LIQUIDATIONSERLOES
                                                                (Income from profit
                                                                                 participation rights
                                                                        without participation in
                                                                                    liquidation
                                                                   proceeds/Einnahmen
                                                                   aus Genussrechten ohne
                                                                            Beteiligung am
                                                                                 Liquidationserlös)

                                                         GEWINNOBLIGATIONEN
                                                                (Income from
                                                                               convertible
                                                                bonds/Einnahmen aus
                                                                         Gewinnobligationen)

                                                        LEBENSVERSICHERUNG
                                                    EN (Income from life
                                                                           insurance (section 20 (1)
                                                          no 6 of the Income Tax
                                                               Act)/Einnahmen aus
                                                                   Lebensversicherungen
                                                                           (§ 20 Abs. 1 Nr. 6 EStG))

                                                             PARTIARISCHES_DARLE
                                                      HEN (Income from loans
                                                                         with an interest rate
                                                                               linked to the borrower’s
                                                                                         profit/
                                                              Einnahmen aus
                                                                              partiarischen Darlehen)

                                                         WANDELANLEIHEN
                                                                (Income from
                                                                                   participation
                                                                bonds/Einnahmen aus
                                                                      Wandelanleihen)

                                                          SONSTIGE (Other
                                                                       income/Sonstige
                                                                             Erträge)

Stocks_Convertible   ISIN                               String            Yes
Bonds/ISIN

Stocks_Convertible  Number of shares/bonds      Number          Yes
Bonds/NumberOfS   (Stückzahl)
hares

Debtor             Debtor (Schuldner)               String            Yes
                                                         (maximum length: 256
                                                                             characters)

DateOfReceiptOfC   Date of receipt of capital        String            Yes
apitalIncome        income (Tag des Zuflusses)       (date as YYYY-MM-DD)

GrossIncomeFrom    Gross income from capital      Number          Yes
CapitalReceived     received (Bruttozufluss)

Withheld_Taxes     Tax (Steuer)                Number          Yes



                               25

                                               Confidential

## PDF page 26

Requested_Refund   Refund (Erstattung)           Number          Yes

DocumentType     Document type (Belegart)        String (one of the   Yes
                                                          following:

                                                           STEUERBESCHEINIGUN
                                                   G (Tax certificate /
                                                                        Steuerbescheinigung)

                                                       ZAHLUNGSBESTAETIGU
                                                     NG_FA (Payment
                                                                             confirmation from tax
                                                                                 office /
                                                                    Zahlungsbestätigung
                                                                   Finanzamt)

                                                        BETRIEBSPRÜFUNGSBE
                                                           RICHT (Audit report /
                                                                            Betriebsprüfungsbericht
                                                                                            )

                                                                  STILLE_BETEILIGUNG
                                                                                    (Silent partnership /
                                                                                                 Stille Beteiligung)

                                                          SONSTIGES (Other /
                                                                            Sonstiges)

Hidden_ProfitDistri    Is the capital income derived    Boolean         No
bution             from a constructive dividend
                    or a silent partnership?
                    (Handelt es sich um einen
                     Zufluss aus einer verdeckten
                  Gewinnausschüttung oder
                     einer stillen Beteiligung?)

Depositary_Receipt   ISIN of the depositary receipt   String                 Only if
                                                                                     income
s/ISIN_DR           (ISIN des Depositary Receipts)                         comes from
                                                                                    a depositary
                                                                                                         receipt

Depositary_Receipt  What is the ratio of the        Number               Only if
                                                                                     income
s/Ratio/Ratio_DR     depositary receipts to the                             comes from
                     underlying German share? –                            a depositary
                     “Depositary receipts” part                                       receipt
                   (Wie ist das Verhältnis der
                     Depositary Receipts zum
                   deutschen Anteil (z. B. Aktie)?
                  – “Depositary Receipts”-Anteil)

Depositary_Receipt  What is the ratio of the        Number               Only if
                                                                                     income
s/Ratio/Ratio_Stock   depositary receipts to the                             comes from
                     underlying German share? –                            a depositary
                 “German share” part (Wie ist                                   receipt
                   das Verhältnis der Depositary
                     Receipts zum deutschen Anteil
                          (z. B. Aktie)? – “Deutsche
                        Aktie”-Anteil)



                               26

                                               Confidential

## PDF page 27

Depositary_Receipt  What is the total number of     Number               Only if
                                                                                     income
s/TotalNumber_DR  DRs issued under the                                  comes from
                     Depositary Receipts (DR)                                a depositary
                 programme on shares with a                                   receipt
                     dividend entitlement? (Wie
                  hoch ist die Gesamtzahl der im
                Rahmen des Depositary
                     Receipts (DRs)-Programms
                  ausgegebenen DRs auf Aktien
                     mit Dividendenberechtigung?)

Depositary_Receipt   How many of the DR holder's    Number               Only if
                                                                                     income
s/NumberOfShares  DRs have been issued a tax                          comes from
                       certificate? (Wie hoch ist die                           a depositary
                   Anzahl der DRs des                                               receipt
                     DR-Inhabers, für die eine
                   Steuerbescheinigung
                      ausgestellt wurde?)

Economic_Owners   Did the person specified as     Boolean          Yes
hip/Ownership_and   the creditor of the capital
_Right_To_Use      income own and have a right
                     to use the capital income
                      (beneficial ownership) at the
                   time when the capital income
                was received? (Hatte die unter
              dem Gläubiger der
                     Kapitalerträge angegebene
                   Person für den Kapitalertrag
               zum Zeitpunkt des Zuflusses
                  das Eigentum und das Recht
                    zur Nutzung des Ertrags
                      wirtschaftliches Eigentum)
                     inne?)

Economic_Owners    Different shareholder:            String             yes
hip/Different_Share  Name/Family name (Name)      (maximum length: 256       (cluster:
                                                                             characters)                DIFF_
holder/General_Inf                                                          OWNER)
ormation/Name

Economic_Owners    Different shareholder: Given      String             yes
hip/Different_Share  name (Vorname)                 (maximum length: 256       (cluster:
                                                                             characters)                DIFF_
holder/General_Inf                                                          OWNER)
ormation/FirstNam
e

Economic_Owners    Different shareholder: Legal      String             yes
hip/Different_Share  form (Rechtsform)                (maximum length: 100       (cluster:
                                                                             characters)                DIFF_
holder/General_Inf                                                          OWNER)
ormation/LegalFor
m



                               27

                                               Confidential

## PDF page 28

 Economic_Owners    Different shareholder: Street     String             yes
 hip/Different_Share   (Straße)                           (maximum length: 100       (cluster:
                                                                               characters)                DIFF_
 holder/Address/Str                                                          OWNER)
 eet

 Economic_Owners    Different shareholder: Street     String             yes
 hip/Different_Share  number (Hausnummer)          (maximum length: 20        (cluster:
                                                                               characters)                DIFF_
 holder/Address/Str                                                          OWNER)
 eetNumber

 Economic_Owners   Different shareholder:           String             yes
 hip/Different_Share   Postcode (Postleitzahl)           (maximum length: 100       (cluster:
                                                                               characters)                DIFF_
 holder/Address/Po                                                          OWNER)
 stcode

 Economic_Owners   Different shareholder: City       String             yes
 hip/Different_Share    (Ort)                              (maximum length: 100       (cluster:
                                                                               characters)                DIFF_
 holder/Address/Cit                                                         OWNER)
 y

 Economic_Owners    Different shareholder: Country   String             yes
 hip/Different_Share   (Staat)                                 (two lower case letters,      (cluster:
                                                                ISO 3166-1 alpha-2)       DIFF_
 holder/Address/Co                                                          OWNER)
 untry

 Questions_for_50j/   Does the capital income derive   Boolean                Only when
                                                                                                    country /
 Dividend            from shares held in collective                                     entity type
                     custody or jouissance shares?                               combination
                     (See section 43 (1) sentence 1                                           is marked in                                                                                                          section 9.1
                   no 1a of the Income Tax Act)
                  (Stammen die Kapitalerträge
                    aus sammelverwahrten Aktien
                     oder Genussscheinen? (siehe
                   § 43 Absatz 1 Satz 1 Nummer
                   1a EStG))

 Questions_for_50j/  Was the person specified as    Boolean                Only when
                                                                                                    country /
 Owner_1_Year_No/   the creditor of the capital                                         entity type
 Owner_45_Days     income the beneficial owner of                             combination
                     the shares or jouissance                                                    is marked in
                                                                                                          section 9.1
                     shares for at least 45                                    and                                                                                                                                                     6 is false
                     consecutive days in a period
                       of 45 days before and 45 days
                        after the due date of the
                        capital income? (War die unter
               dem Gläubiger der
                      Kapitalerträge angegebene



6 Was the person specified as the creditor of the capital income the beneficial owner of the
shares or "jouissance" shares for an uninterrupted period of at least one year? (War die unter
dem Gläubiger der Kapitalerträge angegebene Person seit mindestens einem Jahr
ununterbrochen wirtschaftlicher Eigentümer der aufgeführten Anteile oder Genussscheine?)


                                28

                                                 Confidential

## PDF page 29

                    Person in einem Zeitraum von
                 45 Tagen vor und 45 Tagen
                  nach der Fälligkeit des
                     Kapitalertrags mindestens 45
                 Tage ununterbrochen
                      wirtschaftlicher Eigentümer
                   der Anteile oder
                   Genussscheine?)

Questions_for_50j/   Did the person specified as     Boolean                Only when
                                                                                                  country /
Owner_1_Year_No/   the creditor of the capital                                         entity type
Owner_Risk        income continuously bear,                                  combination
                      without interruption, a risk of a                                            is marked in                                                                                                        section 9.1
                 change in value of 70 percent                          and                                                                                                                                                   6 is false
                    during the minimum holding
                    period of 45 days, in a period
                     of 45 days before and 45 days
                      after the due date of the
                       capital income. (Hat die unter
              dem Gläubiger der
                     Kapitalerträge angegebene
                   Person in einem Zeitraum von
                 45 Tagen vor und 45 Tagen
                  nach der Fälligkeit des
                     Kapitalertrags während der
                   Mindesthaltedauer von 45
                 Tagen ununterbrochen ein
                    Mindestwertänderungsrisiko
                 von mindestens 70 v. H. an
                 den Anteilen oder
                  Genussscheinen getragen?)

Questions_for_50j/  Was the person specified as     Boolean                Only when
                                                                                                  country /
Owner_1_Year_No/  the creditor of the capital                                           entity type
Owner_Compensati  income obliged to pay the                                    combination
on_Obligation       income from capital to anyone                                           is marked in
                                                                                                        section 9.1
                      else in full or in part, directly                             and                                                                                                                                                   6 is false
                     or indirectly, pursuant to
                      section 43 subsection (1), first
                     sentence, number 1a, of the
                  Income Tax Act? (War die
                     unter dem Gläubiger der
                      Kapitalerträge angegebene
                   Person verpflichtet den
                      Kapitalertrag i. S. d. § 43 Abs.
                  1 S. 1 Nr. 1a EStG ganz oder
                   überwiegend, mittelbar oder
                     unmittelbar anderen Personen
                   zu vergüten?)





                               29

                                               Confidential

## PDF page 30

 Minimum_Participa   Ownership interest           Number                Only when 7
                                                                                                                                    is true
 tion_43b/Participati   (Beteiligungshöhe) in percent
 on_Height

 Minimum_Participa   Since when has or did the       String                  Only when 7
                                                                                                                                    is true
 tion_43b/Exists_Sin   direct ownership interest in      (date as YYYY-MM-DD)
 ce                  the capital of the distributing
                   company continuously exist?:
                      Existed since (Seit welchem
                     Zeitpunkt besteht bzw.
                    bestand durchgehend die
                  oben angegebene
                     unmittelbare Beteiligung am
                       Kapital der ausschüttenden
                    deutschen Gesellschaft?:
                   Bestand seit)

 Minimum_Participa   Existed from (Bestand von)       String                  Only when 7
                                                                                                                                    is true
 tion_43b/Duration_                                             (date as YYYY-MM-DD)
 from

 Minimum_Participa   Existed to (Bestand bis)          String                  Only when 7
                                                                                                                                    is true
 tion_43b/Duration_                                             (date as YYYY-MM-DD)
 to

 Business_Establish  Was the capital income        Boolean          Yes
 ment/Business_Est   distributed to a permanent
 ablishment_DE       establishment or fixed entity
                      located within the territory of
                     the Federal Republic of
                  Germany? (Ist der
                       Kapitalertrag einer auf dem
                     Gebiet der Bundesrepublik
                    Deutschland befindlichen
                       Betriebsstätte oder festen
                      Einrichtung zugeflossen?)





7 At the time of receiving the income from capital, does or did a direct ownership interest of at
least 10 percent in the capital of the distributing German company exist? (Besteht oder bestand
im Zeitpunkt des Zuflusses des Kapitalertrags unmittelbar eine Beteiligung von mindestens 10
v. H. am Kapital der ausschüttenden deutschen Gesellschaft?)


                                30

                                                 Confidential

## PDF page 31

1.4  PDF attachments

1.4.1   Limitations
   ●  Individual attachments may not exceed 100 PDF pages in length
   ●  Maximum file size per attachment: 10.4 MB

1.4.2  Tax certificates

All income lines must be certified with a tax certificate (German: “Steuerbeschei-
nigung”), as required by § 45a EStG. Such a document must be issued by the
custodian or paying agent holding the German shares on behalf of the beneficiary. An
example for a tax certificate can be found here.

The  legal  basis  for a tax  certificate’s format can be found  in the document
“Kapitalertragsteuer; Ausstellung von Steuerbescheinigungen für Kapitalerträge nach § 45a
Absatz 2 und 3 EStG” (GZ: IV C 1 - S 2401/19/10001 :006, DOK: 2022/0538617),
published by Bundeszentralamt für Steuern on May 23nd, 2022, from page 34 onwards
(“Muster I” and “Muster II”). It can be downloaded here.

1.4.3   Natural entities
   ●  For each creditor/beneficiary
        ○  the certificate of residence for every tax year in which income was
             received
        ○  the  respective power  of  attorney/authorization  for  the  specified
             authorized representative
   ●  For each income line, attach the respective tax certificate. Make sure to prefix the
      PDF’s filename with BOTH the creditorId and the incomeId from the “income”
       spreadsheet, separated by hyphens, e.g. “0-123-taxcertificate.pdf”.

1.4.4   Legal entities and transparent structures
   ●  For each creditor/beneficiary
        ○  The certificate of residence for every tax year in which income was
             received
        ○  The respective power  of attorney/authorization  for the  specified
             authorized representative
        ○  In case the creditor is a transparent structure, submit an organizational
              chart showing the ownership structure
   ●  For each income line, attach the respective tax certificate. Make sure to prefix the
      PDF’s filename with BOTH the creditorId and the incomeId from the “income”
       spreadsheet, separated by hyphens, e.g. “0-123-taxcertificate.pdf”.
   ●  Other  possibly requested documents  (necessity needs  to be  evaluated
       individually)
        ○  A fully completed questionnaire pursuant to section 50d (3) of the
           Income Tax Act


                                31

                                                 Confidential

## PDF page 32

        ○  Creditor’s  excerpt  from  the  commercial  register  with a German
               translation
        ○  Debtor’s excerpt from the commercial register
        ○  Creditor’s certificate of residence
        ○  Proof of ownership interest between the creditor and debtor in the form
              of a sales contract
        ○  Articles of agreement or certified list of shareholders (an organizational
             chart is not sufficient)
        ○  A current balance sheet together with the creditor’s P&L

1.5  Claim grouping

By default, the platform groups together all income lines relating to the same
beneficiary in a single claim. A single claim can also contain income lines from multiple
different years. However, there are a few exceptions, where the platform performs
automatic splitting/re-grouping of the income lines into more than one claim:

    -  The BOP has the limitation that one claim cannot contain both regular income
       lines and income lines from depository receipts (DR) at the same time. This
     means that if in a single input Excel file, there are both regular and DR-related
      income lines for the same beneficiary, one claim will be created and submitted
       for the regular income lines of that beneficiary and a second claim for that
       beneficiary’s DR-related income lines.

    -  The BOP also has the limitation that the total size of all PDF attachments in one
       claim must not exceed 14 MB (14,000,000 bytes). If this limit is exceeded for a
       certain beneficiary, the income lines of that beneficiary are distributed among
       several claims. Each of these claims will contain all documents which relate to
      the beneficiary (i.e. those documents whose filename starts only with their
       “creditorId”) as well as all documents which relate to the included income lines
         (i.e. those documents whose filename starts with both the “creditorId” and one
        of the respective “incomeId”s). If the size of all attachments related to a certain
       beneficiary plus the size of all attachments related to any single income line of
       that beneficiary already exceeds 14 MB, submission fails.





                                32

                                                 Confidential

## PDF page 33

   33

Confidential