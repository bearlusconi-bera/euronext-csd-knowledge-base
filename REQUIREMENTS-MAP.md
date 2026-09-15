# Requirements map

Research map as of **11 September 2026**, corrected after the 13 September audit. This remains a navigation map, not a retrieval allowlist. Use [reviewed sections](retrieval/README.md) and the [implementation/gap report](IMPLEMENTATION-REPORT.md). “CSD requirements” has three meanings: requirements for the infrastructure operator, requirements to participate, and requirements for an issuer/service user. Store these as separate roles. The tables below are research navigation and evidence checklists; they are not a complete application dossier for an unspecified business.

## 1. Operating a CSD

| Requirement area | Evidence to collect in the knowledge base | Primary legal anchor |
|---|---|---|
| Authorisation and permitted services | Legal entity, home jurisdiction, authority, decision, approved core/ancillary services, instruments and subsequent changes | CSDR Articles 16–19; ESMA register; RTS 2017/392 and ITS 2017/394 |
| Governance and compliance | Governance structure, conflicts management, controls, management suitability and public rules | CSDR Articles 26–29 |
| Record keeping and outsourcing | Record-retention controls, service providers, contractual responsibilities and oversight | CSDR Articles 29–30; relevant technical standards |
| Fair participation and transparent charges | Admission criteria, response/refusal procedures, user rights and service-level fees | CSDR Articles 33–35 |
| Integrity and safeguarding | Reconciliation processes, issue balances, participant/client segregation, disclosures and consent controls | CSDR Articles 37–38 |
| Settlement and finality | Entry/irrevocability/finality rules, DvP, cash provider and currency arrangements | CSDR Articles 39–40; Settlement Finality Directive and national implementation |
| Participant default | Default triggers, responsibilities, public procedures and periodic testing | CSDR Article 41 |
| Risk, resilience and capital | Legal/operational/business risk, recovery, accessible financial resources, risk-based capital and orderly wind-down | CSDR Articles 42–47; RTS 2017/390; DORA |
| Net settlement and links | Netting design, credit/liquidity risk, linked-CSD legal arrangements, reconciliations and additional intermediary risk | CSDR Articles 47a–48 |
| Cross-border service | Passport/recognition permissions and the securities’ applicable law | CSDR Articles 23, 25, 49; ESMA passports/links data |
| Banking-type ancillary services | Additional permissions, authorised designated provider, applicable prudential requirements | CSDR Title IV, including Article 54 |

Read the actual articles and referenced instruments in [CSDR, consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117). Saved complete texts and links are in the [reading guide](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/READING-GUIDE.md>). The selected CSDR provisions were reviewed, but the complete capital calculation, national transpositions and every implementing requirement were not assessed.

**DORA is part of the operating framework.** CSDR Article 45 now explicitly references it for ICT risk and recovery. A knowledge base focused only on connectivity specifications would omit incident handling, resilience testing and ICT third-party dependencies. [DORA English OJ text](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng), reviewed Articles 2 and 64. The archived English-labelled consolidated capture has French operative text and is excluded from English quotations. The full incident-reporting RTS/ITS and national procedure chain remains unreviewed.

Use the PFMI as a cross-cutting control taxonomy, then map it to binding rules and local evidence. Porto’s WFC questionnaire and Athens’ PFMI self-assessment provide examples of disclosed controls; their dates matter, and disclosure is not independent proof that a control remains effective. [PFMI](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/1ae6d477d17b-PFMI-April-2012.pdf>); [Porto WFC 2025](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/2a1af673b358-WFC-Single-Disclosure-Report-2025.pdf>); [Athens December 2023 PFMI assessment](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/3cfbaea6fa93-PFMI-Self-Assessment-Report-IOSCO.pdf>).

## 2. Becoming and remaining a participant

| Workstream | Common evidence fields | Market differences established by the review |
|---|---|---|
| Eligible entity and permitted role | Regulatory status, jurisdiction, role, LEI, scope of requested services | Copenhagen distinguishes participant roles, including issuing agents and securities-account controllers. Oslo ties settlement access to specified institution categories and account-operator arrangements. |
| Legal admission | Application, constitutional documents, representatives, signatures, contracts and foreign-law opinions where required | Athens uses application approval, preparation and activation stages. Foreign documents may require specified authentication. |
| Financial/organisational capacity | Financial statements, staffing, operational capacity, controls and ongoing change notifications | Athens Resolution 1 asks for the last two years’ financial statements; Porto’s manual refers to annual reports for the last three years. Do not merge these into one group-wide requirement. |
| Personnel and permissions | Authorised users, role lists, qualified contacts and required certification | Athens Resolution 2 requires at least one CSA-certified employee/executive, with stated exemptions. Copenhagen requires competent and appropriately authorised users. |
| Accounts and cash | Securities accounts, account operators, currencies, settlement-bank contracts, central-bank accounts or service-provider arrangements | Oslo specifies liquidity-bank and substitute arrangements; Porto specifies relevant cash account arrangements. Technical connectivity is insufficient on its own. |
| Technical readiness | Production/test access, interfaces, identifiers, message validation, reconciliation, security and contingency channels | Milan requires successful configuration/operating tests before activation. DCP and ICP requirements differ. |
| Testing and continuity | End-to-end tests, emergency arrangements, recovery roles and ongoing exercises | Copenhagen’s CSD-link admission provisions include operational testing and emergency arrangements; current local obligations must be read separately from Convergence testing plans. |
| Ongoing operations | Funding/securities availability, cut-offs, matching, fail handling, fees and notifications | Use the current local calendar, notices and tariffs; these can change faster than the rulebook. |

Evidence: [Milan Regulations, PDF pp. 13–16](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/8719262f5e8b-Regulations-as-of-26-January-2026.pdf>); [Copenhagen Part 2, PDF pp. 2–5](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/cbdf3c1f8b51-Part-2-General-Terms-and-Conditions-PDF.pdf>); [Oslo VPO NOK, PDF pp. 13–19](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/14dc34b8e54e-ES-OSL-VPS-NOK-Rules-pdf.pdf>); [Porto Manual, PDF pp. 15–17](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/089b7aaef991-Operational-Manual-of-INTERBOLSA.pdf>); [Athens Resolution 1, PDF pp. 1–4](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/dab1b35a93c5-ATHEXCSD-Resolution-1.pdf>); [Athens Resolution 2, PDF pp. 1–2](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/513a8da7c0ad-ATHEXCSD-Resolution-2.pdf>).

Keep **response to an access request**, **approval**, **testing completion** and **activation** separate. A regulatory response deadline is not a promise of operational go-live. Where you need a specific onboarding schedule, resolve the entity, requested role, complete-documentation date and service dependencies first. CSDR Article 33 and the local admission provisions above provide the source trail.

## 3. Issuing securities and using issuer services

| Requirement area | Questions the knowledge base should resolve | Where to start |
|---|---|---|
| Eligible issuer and instrument | Which legal forms, instruments, jurisdictions and recording arrangements are accepted? | Local rulebook, service instructions, current instrument eligibility lists |
| Agents and contracts | Is an issuing agent, registrar or paying agent needed, and who contracts with whom? | Local issuer rules and agreements; Copenhagen Part 2; asset-servicing handbook |
| Identifiers and initial recording | Who assigns/validates identifiers, supplies terms and reconciles issued quantities? | Local issuance instructions and numbering-agency material |
| Account/registration model | Bearer or registered security, account type, ownership records, nominee structure and disclosures? | Local registration law and account rules; market-specific European Offering documents |
| Corporate events | Who announces the event, provides funds/securities, processes elections and reconciles entitlements? | Local rules, corporate-events handbook, service cut-offs and current notices |
| Fees and tax services | Which issuer tariff and optional service terms apply? What tax documents/deadlines apply to the specific event/jurisdiction? | Separate issuer fee books and jurisdiction-specific tax manuals |

The handbook’s general actor descriptions must be reconciled with local contracts. For example, a common description of an issuer’s relationship does not override Copenhagen’s specific tri-party arrangements. The handbook also names four CSDs, so its coverage should not be assumed to include Athens. [Copenhagen Part 2](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/cbdf3c1f8b51-Part-2-General-Terms-and-Conditions-PDF.pdf>); [Corporate Events Handbook](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/sources/documents/e1354fb2d76a-Corporate-Events-Services-User-Guide-20260507-clean-pdf.pdf>).

## Scope fields to attach to every requirement

Use: **obligated role → legal entity → jurisdiction → service → instrument/currency → account/connectivity model → effective period → source clause → exceptions → evidence needed**.

Example: Athens / participant / personnel certification / Resolution 2 / effective 20 July 2026 / CSA-qualified employee or executive / retain stated exemptions. This is a researched local requirement, not a universal condition for all five CSDs.

## Questions still requiring additional evidence

Exact production message schemas and entitlements; negotiated/member-only operating documents; current national-law originals and EEA incorporation details; complete tax procedures; service-specific cut-offs; actual client test acceptance; and the firm’s own eligibility. These are tracked in [COVERAGE-AND-CAVEATS.md](</Users/mattiadalessandra/Documents/PERSONAL/outputs/euronext-csd-knowledge-base/COVERAGE-AND-CAVEATS.md>) rather than inferred from marketing pages.
