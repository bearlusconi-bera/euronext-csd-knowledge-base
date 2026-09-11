# How Euronext’s CSDs work

Research synthesis, **11 September 2026**. Read this with the linked local rules. It explains the architecture and the practical questions a knowledge base should answer; it is not a determination of a particular firm’s permissions.

## Five CSDs, with separate local operating rules

Euronext’s current CSD group includes Athens, Copenhagen, Milan, Oslo and Porto. A shared brand and planned common platform do not remove the need to identify the legal entity, market and service before answering an operational question. [Euronext Securities overview](https://www.euronext.com/en/csd).

| Market | Legal entity named in local materials | Main current sources | Cash/settlement distinction established in the reviewed sources |
|---|---|---|---|
| Athens | Hellenic Central Securities Depository S.A. / ATHEXCSD | Master rulebook and 22 resolutions | DSS settlement and euro cash via TARGET-GR arrangements; specific non-euro routes |
| Copenhagen | VP Securities A/S | Six-part rulebook | Both VP and T2S arrangements; EUR and DKK T2S settlement |
| Milan | Monte Titoli S.p.A. | Service Regulations, CSD Instructions, Settlement Instructions | T2S settlement; gateway links add route-specific procedures |
| Oslo | Verdipapirsentralen ASA | Registration Rules and VPO NOK Rules | VPS securities records and NOK cash settlement at Norges Bank/NBO |
| Porto | Interbolsa – Sociedade Gestora de Sistemas de Liquidação e de Sistemas Centralizados de Valores Mobiliários, S.A. | Local regulations, Operational Manual and technical layouts | T2S arrangements and separately specified foreign-currency services |

Sources: [Athens Resolution 5, PDF pp. 3–4](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/410859953fce-ATHEXCSD-Resolution-5.pdf>); [Copenhagen Part 4, PDF pp. 3–6](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/3d76a327339b-Part-4-Settlement-Rules-PDF.pdf>); [Milan Service Regulations](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/8719262f5e8b-Regulations-as-of-26-January-2026.pdf>); [Oslo VPO NOK, PDF pp. 13–19](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/14dc34b8e54e-ES-OSL-VPS-NOK-Rules-pdf.pdf>); [Porto Operational Manual, PDF pp. 15–17](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/089b7aaef991-Operational-Manual-of-INTERBOLSA.pdf>). Oslo’s linked English VPO copy retains an approval qualification; see the currentness register.

For authorisation questions, consult the **ESMA register dated 2 September 2026**, especially the authorisations, links and passports tabs. Some CSDs have several decision rows. Do not collapse those rows to a single initial authorisation. The workbook identifies recent Milan extensions, including a July 2026 decision. [Saved ESMA register](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/535f6a23062a-CSD-Register.xlsx>) and [official register landing page](https://www.esma.europa.eu/document/csd-register).

## The three core functions

**Initial recording** establishes an issue in book-entry form. **Central maintenance** maintains securities accounts at the top tier. **Settlement** completes transfers in a securities settlement system. Under CSDR, a CSD operates a settlement system and provides at least one of the other two core services. These functions are distinct from executing a trade, clearing it through a CCP, or providing a retail brokerage account. [CSDR, consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117), Article 2 and Annex Section A.

An issuance workflow therefore needs the issuer, issue terms, identifiers, eligible security type, appointed agents and initial account postings. The ongoing ledger must remain consistent with the issued quantity. CSDR requires at least daily reconciliation and prohibits securities overdrafts or unauthorised securities creation within the settlement system. [CSDR, consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117), Article 37; [Porto general operating rules](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/4e7eec1c51e0-INTERBOLSA-Regulation-2-2016.pdf>).

## A typical settlement workflow

This is an explanatory sequence. Its exact messages, cut-offs and finality points depend on the local system and instruction type.

1. The trading/clearing chain determines what securities and cash are due, by whom, and on which settlement date.
2. Parties or their agents submit instructions using the required instrument, account, counterparty, place-of-settlement and cash details.
3. The system validates instructions and matches the required fields. Acceptance or matching alone does not establish final settlement.
4. Securities and cash availability, instruction controls, priorities and system timing determine whether settlement can complete. Some services support partial settlement, hold/release or collateralisation, with local conditions.
5. Delivery-versus-payment links the securities and cash obligations. Finality depends on the system’s legal rules, including entry and irrevocability points.
6. Participants reconcile confirmations and balances. Unsettled instructions require investigation, funding/securities remediation and, where applicable, penalty processing.

Operational source trail: [Milan Settlement Instructions](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/dd1cf7cb930b-Instructions-to-Settlement-Service-and-related-instrumental-activities-in-force-as-of-30-J.pdf>), [Copenhagen Part 4](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/3d76a327339b-Part-4-Settlement-Rules-PDF.pdf>), [Porto Operational Manual](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/089b7aaef991-Operational-Manual-of-INTERBOLSA.pdf>), [Athens Resolution 5](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/410859953fce-ATHEXCSD-Resolution-5.pdf>) and [Oslo VPO NOK rules](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/14dc34b8e54e-ES-OSL-VPS-NOK-Rules-pdf.pdf>). The legal foundations for finality and cash settlement are CSDR Articles 39–40 and the [Settlement Finality Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408).

## The cash leg matters as much as the securities leg

CSDR favours the relevant central-bank accounts where practical and available, while providing a framework for other cash arrangements. A technical connection does not itself provide cash, credit or a settlement-bank relationship. Treat currency, cash account, provider and funding responsibility as separate data fields. [CSDR, consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117), Articles 40 and 54.

In Oslo, the reviewed rules describe settlement participants, liquidity banks and substitute arrangements. A substitute-liquidity-bank declaration is expressly not a funding guarantee. In Porto, affiliation procedures include appropriate cash-settlement account arrangements. These are concrete reasons to model liquidity dependencies in a participant knowledge base. [Oslo VPO NOK, PDF pp. 16–19](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/14dc34b8e54e-ES-OSL-VPS-NOK-Rules-pdf.pdf>); [Porto Manual, PDF pp. 15–17](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/089b7aaef991-Operational-Manual-of-INTERBOLSA.pdf>).

## Accounts, segregation and ownership

An account’s technical identifier, its segregation category and the legal identity of an owner are different facts. CSDR Article 38 addresses participant/client segregation and the choice between omnibus and individual client segregation, including disclosure of costs and protection. Local registration law and account-operator rules add further meaning. [CSDR, consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117), Article 38; [Oslo Registration Rules](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/838261c7c0d4-ES-OSL-Registration-rules-in-force-4-February-2025-pdf.pdf>); [Copenhagen Book-entry Rules](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/16ded02d7a65-Part-3-Book-entry-Rules-PDF.pdf>).

The European Offering’s account guide shows how market conventions affect account structures, including French registered-share arrangements. Its rules are tied to the Milan-based offering. They cannot be applied automatically to every account elsewhere in the group. [European Offering Account Structure V03, PDF pp. 3–5](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/00a3e1aeba1c-Account-Structure-v03.pdf>).

## Asset servicing continues after settlement

Corporate events include cash or securities distributions, reorganisations and elective events. Their workflows involve eligibility dates, entitlements, elections, payments and sometimes adjustments to pending transactions. The corporate-events handbook distinguishes issuer, issuer-agent, paying-agent and investor-CSD responsibilities. When a CSD holds through another CSD, upstream information and local market practice affect processing. [Corporate Events Processes Handbook V05, PDF pp. 16–17](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/e1354fb2d76a-Corporate-Events-Services-User-Guide-20260507-clean-pdf.pdf>).

The July 2026 T+1 corporate-events guide is particularly useful for understanding how a shorter cycle changes key dates, market claims, transformations and buyer protection. Its purpose is future implementation. [AMI-SeCo T+1 Corporate Events Guide, PDF pp. 1–5](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/a46c6c66a0e4-T-1-Corporate-Events-Harmonised-Implementation-Guide.pdf>).

## T2S and cross-border links

T2S provides common settlement infrastructure. The local CSD relationship, account responsibilities and applicable rules still matter. Porto’s manual distinguishes directly connected participants (DCPs) from indirectly connected participants (ICPs). Direct technical access does not remove the CSD’s oversight. [Porto Manual, PDF pp. 15–17](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/089b7aaef991-Operational-Manual-of-INTERBOLSA.pdf>).

Keep three routes separate: settlement within one CSD, settlement across CSDs on T2S, and settlement through an external/non-T2S link. The Convergence settlement specification explains these distinctions, but describes a future platform. For a transaction today, use the local manual, current link/eligibility data and current T2S release. [Convergence Settlement SDD, PDF pp. 8–13](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/71233aed41e7-Settlement-Services-Service-Description-Document-v1-6-pdf.pdf>); [Milan T2S Gateway settlement links](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/1bd67deaace2-T2S-GATEWAY-Euronext-Securities-Milan-Settlement-Links-Valid-from-1st-May-2026.pdf>); [T2S UDFS R2026.JUN](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/aa3d5a3b94c9-T2S-User-Detailed-Functional-Specifications-R2026-JUN-UDFS.pdf>).

## Three changes that must remain separate

| Change | State at 11 September 2026 | Knowledge-base treatment |
|---|---|---|
| European Offering / new Euronext settlement model | Announced start 21 September 2026, using Milan for the expanded offering. The announcement covers Amsterdam, Brussels and Paris equity/ETP euro transactions and preserves choice of alternative CSDs. | Future rollout with specific markets, instruments and service scope |
| Convergence | Planned common platform over a longer horizon. Programme page gives Copenhagen first in August 2028, Porto in 2028, Milan/Athens in 2029; Oslo timing depends on a Norges Bank T2S decision. July Athens newsletter specifies indicative H2 2029. | Future architecture; keep local migration targets provisional |
| EU T+1 | Shorter cycle applies from 11 October 2027. ESMA’s July 2026 statement identifies an earlier 7 December 2026 allocation/confirmation milestone in the regulatory transition. | Separate the legislated cycle date from detailed RTS adoption/application status |

Sources: [new settlement model announcement](https://www.euronext.com/en/news/confirmation-go-live-euronexts-new-settlement-model-september-2026); [Convergence programme](https://www.euronext.com/en/csd/strategic-projects/convergence-programme); [Athens July newsletter](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/9a9900fa74db-Euronext-Securities-ATH-Convergence-Newsletter-July2026.pdf>); [T+1 amendment](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2075); [ESMA July statement](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/f488a7016d8c-statement.pdf>). The programme webpage retains an old “dates to be confirmed” qualifier, so its schedule should not be represented as a binding commitment.
