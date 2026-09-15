# Market Practice per Additional Matching Field in T2S

Source: https://www.euronext.com/sites/default/files/2021-03/Market%20Practice%20-%20Additional%20matching%20field%20in%20T2S.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

                        ITALIAN MARKET PRACTICE
              USE OF ADDITIONAL MATCHING FIELDS IN T2S


SCOPE OF THE DOCUMENT


The aim of this document is to define a standard market practice for the use of the
additional matching fields of OTC transactions in T2S, in order to guarantee a smooth
matching process and high matching rate following the introduction of the new logic.


TECHNICAL BACKGROUND


The matching process in T2S compares mandatory and non-mandatory matching
fields of the settlement instructions.


Mandatory Matching  fields are those  fields  that must be populated  in the
instruction and whose values have to be the same in both settlement instructions for
matching.


Non-mandatory matching fields are defined as additional or optional matching fields.
     Additional matching  fields: may not be used, but  if  filled  in by one
       counterparty, the other party must also  fill  it in for matching. Additional
      matching fields cannot match against “blank”. The additional matching fields
        are:
       o  CUM/EX indicator with possible values “CCPN”  - cum coupon or
            “XCPN” - ex coupon. When specified, it will deviate from the standard
              entitlement rules taking into account the relevant dates;
       o  OPT OUT indicator with value “NOMC”. If specified, no market claims
                 will be raised on a given transaction, irrespective of the CUM/EX
               indicator and the relevant dates of the settlement instruction. When
              opt-out is not required in the transaction, the indicator should NOT be
              sent in the ISO message.
     Optional matching  fields: may not be used and   if  filled  in by one
       counterparty, the other party is not mandated to use it. Optional matching
        fields may match against “blank”.  If both parties populate the optional
      matching field, the values have to match.


Generation of market claims and reverse market claim


Market claims will be initiated by the CSD when a settlement instruction is matched
before or on record date of the mandatory event but is failing to settle over record
date, or is matched after the record date of the mandatory event till the 20th working
day after the record date.

## PDF page 2

Moreover, facing a contract executed from the ex-date and settled within the record
date, the CSD generates a reverse market claims.


Counterparties in the underlying transaction may choose to include the ex/cum
indicator only if they want to deviate from the standard market claim procedure or
to choose the “opt-out” if they want to indicate that no claim at all should be raised
on a given transaction.


OPERATIONAL GUIDELINE


Points of attention


Due to the fact that the additional matching field are not currently contemplated by
the  Italian market, CSD participants agreed to spread among their clients the
awareness of the peculiarities of these fields by underlying the below points of
attention, with the aim to avoid the increase of the fail rate caused by un-matching:
     Counterparty agreement: as additional matching fields do not allow matching
       blank, it is crucial for parties to agree the relevant value before using it;
     Proper use: these fields should be used only in exceptional cases when the
      two parties want to deviate from the standard rules applied by the CSD
       according to the analysis of the trade and intended settlement date.


Operational guidance


The Italian Community propose the below recommendations:
     CUM/EX indicator: it is strongly suggested to use this indicator only when
        clients want to deviate from the standard rules derived from the relevant
       dates of the instruction  (i.e. do not use the indicator to reconfirm the
      requirement to follow the standard Market Claim auto-generation process);
     OPT OUT indicator: by default the CSD raises the market claims as per above-
      mentioned rules. It is strongly suggested to populate this field only if the two
       parties agree to avoid the generation of the market claim or reverse market
       claim by the CSD platform.


CSD participants have agreed to reflect in the settlement instruction the same
indicators as quoted in the original clients’ instructions.


Annex
    1. ECB table - FAQ_CA_standards_Jan2014