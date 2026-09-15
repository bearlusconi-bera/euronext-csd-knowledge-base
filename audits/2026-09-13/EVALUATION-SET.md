# Evaluation fixtures — NOT RUN

34 cases. No retrieval system/index was found; there are no observed retrieval results, model answers or pass-rate claims. After implementation, record retrieved source/chunk IDs and as-of filters, generated answer, citation entailment, and each failure condition. Run against both normal and deliberately contradictory/future/historical candidates. Expected answers are bounded by the audit evidence, including qualifications.

## E01 — For Milan, does “T2S matched” prove that securities and cash moved?

**Expected:** No. Matching verifies compatible instructions; settlement requires eligibility and resources. Under Milan Art 72, matching is SF2 irrevocability subject to Art 70(2) bilateral cancellation; SF3 is the cash debit or securities debit for FoP.

**Required evidence:** [Regulations as of 26 January 2026](https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf) — Articles 69,70(2),72 PDF 50–51; [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 267,303–304

**Fail if:** Equates matched and settled; Says matching has no legal effect; Omits bilateral-cancellation qualification

**Result: NOT RUN.**

## E02 — Can a Milan matched instruction always be cancelled unilaterally?

**Expected:** No. Art 70 distinguishes pre-match unilateral and post-match bilateral cancellation, with non-modifiable, market/CCP and CoSD qualifications.

**Required evidence:** [Regulations as of 26 January 2026](https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf) — Article 70 PDF 50–51

**Fail if:** Unconditional yes; Unconditional no cancellation of matched instructions; Drops CoSD/market restrictions

**Result: NOT RUN.**

## E03 — Can instructions match before ISD, and does realignment generation move securities immediately?

**Expected:** Matching and generation can precede ISD under valid setup. Automatic realignment follows matching/validation of prematched instructions. Posting waits for eligibility, resources and linked settlement conditions.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 267–268,303–304,373–375,753

**Fail if:** Generation is settlement; Forbids all pre-ISD processing; Claims early matching guarantees cash

**Result: NOT RUN.**

## E04 — Two T2S CSDs, both banks ICP, seller at issuer CSD and buyer at linked investor CSD: what messages flow?

**Expected:** Illustrate bank-to-CSD via their local interface; CSD-to-T2S sese.023; T2S-to-CSD status sese.024, realignment notification sese.032 to CSDs in chain, settlement confirmation sese.025. Local relays are not proven to use native schemas. Ask for link/configuration for a production mapping.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 753,778,373–376; [Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025](https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf) — §1.1 PDF 7

**Fail if:** Bank ICP connects directly by assumption; Reverses direction of sese.032; Presents unverified X-TRM mapping as native T2S

**Result: NOT RUN.**

## E05 — Does a valid ECB DCP certificate alone admit me to Copenhagen settlement?

**Expected:** No. The sampled Part 5 requires the local DCP service relationship/entitlements and User Guidelines/local conditions in addition to certification.

**Required evidence:** [Part 5 - DCP Service Rules (PDF)](https://www.euronext.com/sites/default/files/2023-08/Rule%20Book%20Part%205%20T2S%20DCP%20Service%20Rules.pdf) — §§2–3 PDF 2–3

**Fail if:** Certificate replaces CSD membership; Ignores local testing/service conditions

**Result: NOT RUN.**

## E06 — In Milan, is a participant with a settlement cash agent exempt from having a securities account?

**Expected:** No. Art 60 requires the securities account separately from DCA access or a cash agent; DCP adds further requirements.

**Required evidence:** [Regulations as of 26 January 2026](https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf) — Article 60 PDF 44–45

**Fail if:** Cash agent replaces securities account; Conflates securities participant and central-bank cash bank

**Result: NOT RUN.**

## E07 — For the current T2S baseline, is NTS at 19:30 and are there two partial windows?

**Expected:** No: R2026.JUN Table 37 gives 20:00 and PDF 162 five windows. Current-linked Milan instructions conflict; flag and quarantine their timetable, and check local/daily notices before operational use.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 160,162; [Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025](https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf) — PDF 13,15; [Istruzioni del Servizio di Liquidazione e dei servizi accessori - in vigore dal 30 giugno 2025](https://www.euronext.com/sites/default/files/2025-07/03%20Istruzioni%20Servizio%20di%20Liquidazione_30062025_SENZA%20evidenza.pdf) — PDF 12,15

**Fail if:** Silently chooses Milan older clock; Conceals conflict; Assumes English translation alone caused it

**Result: NOT RUN.**

## E08 — What was the announced EUR DvP cut-off on 8 September 2026?

**Expected:** The 15:30 ECB notice postponed it from 16:00 to 17:00 for that day. It is not a permanent timetable amendment; consult later updates for actual incidents.

**Required evidence:** [t2s-2026-status-events](https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html) — 8 September 2026, 15:30 update

**Fail if:** Answers 16:00 from normal schedule; Applies 17:00 to all future days

**Result: NOT RUN.**

## E09 — A Monday trade is T+2: does the Wednesday T2S business day first start Wednesday morning?

**Expected:** Not necessarily. Under the normal schedule it can open Tuesday evening at 18:45 after the previous business day ends; NTS begins at 20:00 under the current baseline. Holidays, service and incident conditions matter.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 160,163,165,168

**Fail if:** Conflates trade/calendar/business/settlement date; Guarantees exact start despite predecessor dependency; Omits assumed business-day calendar

**Result: NOT RUN.**

## E10 — Is every EU securities trade required to use T+2 on 13 September 2026?

**Expected:** No. CSDR Art 5(2) sets a latest ISD for covered venue transactions and lists exceptions; Art 5(1) requires settlement on the agreed ISD. Do not extend it to every instrument/transaction.

**Required evidence:** [CSDR: consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117) — Article 5(1)–(2)

**Fail if:** T+2 mandatory for every transaction; Applies future T+1 early

**Result: NOT RUN.**

## E11 — Is EU T+1 still a proposal, and when does it apply?

**Expected:** It is enacted in Regulation 2025/2075; application begins 11 October 2027. Distinguish entry into force from application.

**Required evidence:** [T+1 amendment 2025/2075](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2075) — Articles 1–2

**Fail if:** Calls it only a draft; Applies in September 2026; Uses enactment as application date

**Result: NOT RUN.**

## E12 — May I promote the November T2S UDFS because the final-publication target was 11 September?

**Expected:** No. Latest located live-hub note is still a draft; the target is not proof final publication or deployment. June final documents and June 14 deployment were verified.

**Required evidence:** [T2S Draft Scope Defining Documents for R2026.NOV - Market Review](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/CoverNote_Draft_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf) — PDF 1–2; [Cover note](https://www.ecb.europa.eu/pub/pdf/annex/CoverNote_Final_Delivery_T2S_UDFS_R2026.JUN_UHB_R2026.JUN.en.pdf) — PDF 1–2; [t2s-2026-status-events](https://www.ecb.europa.eu/paym/target/html/t2s_history_2026_include.en.html) — 14 June 2026 confirmation

**Fail if:** Treats planned publication as fact; Says no final can exist anywhere; Promotes draft to current

**Result: NOT RUN.**

## E13 — On 13 September, does the daily eligible ISIN sheet prove BE0003809267’s new designated CSD is already operational?

**Expected:** No. Introduction and column headers distinguish data through 10 September from designated/alternative places as of 21 September. The sample current-place cell says Euroclear Belgium and future designated cell Euronext Securities. This is not a complete operational eligibility assertion.

**Required evidence:** [ISINs eligible for settlement in Euronext Securities Milan 2026-09-11](https://www.euronext.com/sites/default/files/2026-09/ISINs%20eligible%20for%20settlement%20in%20Euronext%20Securities%20Milan%202026-09-11.xlsx?VersionId=W9q4Cxr4Dog5dqZVMCUwWuDNNnIFGBUR) — Introduction B5:B8; Equities A2/I2/K2/L2

**Fail if:** Uses K2 as current; Ignores listing/currency scope; Infers all Milan securities

**Result: NOT RUN.**

## E14 — Can the Convergence v1.6 flow establish the current Athens production interface?

**Expected:** No. It is programme design. Use current Athens rules/technical announcements for DSS; T2S documents describe native platform mechanics only where applicable.

**Required evidence:** [
              Euronext Securities CSD Convergence Programme
            ](https://www.euronext.com/en/csd/strategic-projects/convergence-programme) — Programme hub; [Settlement Services _ Service Description Document _ v1.6.pdf](https://www.euronext.com/sites/default/files/2026-06/settlement_service_description_document_v1.6.pdf) — Programme identity; [ATHEXCSD Resolution 5](https://athens.euronext.com/sites/default/files/2025-12/RESOLUTION_Nr5-ATHEXCSD_383_24.11.2025_FORCE%208.12.2025.DOC.pdf) — §2.2 PDF 4–5

**Fail if:** Uses future design as current local authority; Assumes all five CSDs share one present platform

**Result: NOT RUN.**

## E15 — Does the Athens “Amendment 8” hub label prove a conflict with the seven-amendment PDF?

**Expected:** No such operative conflict was established. The Greek hub says Edition 8; both sampled documents list seven amendments. Edition count including original is a plausible explanation, explicitly an inference. Seventh amendment effectiveness is stated as 8 December 2025.

**Required evidence:** [ATHEXCSD Rulebook - Amendment 8](https://athens.euronext.com/sites/default/files/2026-06/ATHEXCSD_RULEBOOK_7th_Ammendment_383_24.11.2025_FORCE_8.12.2025.pdf) — PDF 2,217 Section XIII Part 9; [athens-greek-master](https://athens.euronext.com/sites/default/files/2026-06/%CE%9A%CE%91%CE%9D%CE%9F%CE%9D%CE%99%CE%A3%CE%9C%CE%9F%CE%A3_%CE%9B%CE%95%CE%99%CE%A4%CE%9F%CE%A5%CE%A1%CE%93%CE%99%CE%91%CE%A3_%CE%95%CE%9B%CE%9A%CE%91%CE%A4_7%CE%B7_%CE%A4%CF%81%CE%BF%CF%80%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_383_24.11.2025_%CE%99%CE%A3%CE%A7%CE%A5%CE%A3_8.12.2025.pdf) — PDF 2,206

**Fail if:** Invents an eighth amendment; Claims independent HCMC approval was fetched; Treats inference as legal proof

**Result: NOT RUN.**

## E16 — Can we remove the Oslo subject-to-approval warning because Finanstilsynet approved VPO NOK?

**Expected:** No. System approval is distinct from approval of the September 2024 edition; English and Norwegian covers both retain the qualification.

**Required evidence:** [ES-OSL VPS NOK Rules.pdf](https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf) — PDF 1; [822d46bb9149](https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_regelverket.pdf) — PDF 1; [
				Infrastrukturforetak
			](https://www.finanstilsynet.no/tilsyn/infrastrukturforetak/) — Infrastructure page

**Fail if:** Conflates system and edition approval; Ignores governing-language reservation

**Result: NOT RUN.**

## E17 — Does an Oslo substitute liquidity bank have the primary bank’s mandatory funding duty?

**Expected:** The sampled §§9–10 distinguish primary declarations from a substitute declaration that does not itself impose a duty to provide cash. Qualify the answer by the unresolved edition approval.

**Required evidence:** [ES-OSL VPS NOK Rules.pdf](https://www.euronext.com/sites/default/files/2024-09/240902_es-osl_vpo_nok_rules.pdf) — PDF 17–18, §§9–10

**Fail if:** Says identical unconditional duties; Omits approval qualification

**Result: NOT RUN.**

## E18 — What fee applies to a Copenhagen trade on 20 September versus 20 November 2026?

**Expected:** January and November fee-book periods differ. Identify service, participant role and charging basis, then inspect the exact tariff/conditions; this audit did not validate numeric fee rows.

**Required evidence:** [Euronext Securities Copenhagen - Table of fees per January 2026](https://www.euronext.com/sites/default/files/2025-12/ES-CPH_table_of_fees_jan_2026_update.pdf) — PDF 1–2; [Euronext Securities Copenhagen - Table of fees per November 2026](https://www.euronext.com/sites/default/files/2026-08/CPH%20Table%20of%20fees_Nov%202026.pdf) — PDF 1–2

**Fail if:** Uses July publication as November effective date; Invents a numeric price; No clarification of service/date

**Result: NOT RUN.**

## E19 — Are Copenhagen VP and T2S business-day boundaries the same?

**Expected:** The reviewed §2.2 distinguishes VP at 18:00 and T2S at 18:45. Service/currency calendars still control applicability.

**Required evidence:** [Part 4 - Settlement Rules (PDF)](https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf) — §2.2 PDF 3

**Fail if:** One universal group boundary; Drops route/currency qualifier

**Result: NOT RUN.**

## E20 — Does Porto DCP replace the legal relationship with INTERBOLSA?

**Expected:** No. Regulation 1/2016 Art 2(4) keeps the relationship with INTERBOLSA; direct connectivity is technical.

**Required evidence:** [INTERBOLSA Regulation 1/2016](https://www.euronext.com/sites/default/files/2023-07/regulamentoib.2016.01.consolidado.en_.pdf) — Article 2(4) PDF 2; [Operational Manual of INTERBOLSA](https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf) — PDF 17

**Fail if:** ECB replaces local contract; Conflates technical and legal participation

**Result: NOT RUN.**

## E21 — What are Porto daily reconciliation/report families for a participant?

**Expected:** §7.1 describes daily reconciliation and positions/activity reports; examples include MT535/MT536 and subscribed T2S reports for DCP. Exact schema/version/subscription needs the local layouts.

**Required evidence:** [Operational Manual of INTERBOLSA](https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf) — §7.1 PDF 66; [Layouts of the files/messages available to Financial Intermediaries](https://www.euronext.com/sites/default/files/2026-04/20260408_STD%20Layouts%20of%20the%20files%20messages%20available%20to%20Financial%20Intermediaries_v58.pdf) — Public layout candidate

**Fail if:** Exact schema invented; Ignores report subscription/access model; Copies apparent source message typo as production instruction

**Result: NOT RUN.**

## E22 — Is Porto completely closed on 1 May 2026?

**Expected:** The official 2026 calendar page expressly says FoP settlement is open that day. It references Notice 25/1162; consult that notice for binding scope.

**Required evidence:** [
              Working Days & Operating Hours
            ](https://www.euronext.com/en/post-trade/euronext-securities/porto/about-us/working-days-operating-hours) — 2026 calendar, May 1 exception

**Fail if:** Assumes cash holiday closes all securities processing; Treats webpage as entire calendar rulebook

**Result: NOT RUN.**

## E23 — Do Athens EUR and non-EUR settlement cash arrangements use the same bank and account?

**Expected:** No general equivalence. Resolution 5 distinguishes EUR TARGET-GR arrangements from non-EUR arrangements; request currency and settlement-bank setup for a concrete answer.

**Required evidence:** [ATHEXCSD Resolution 5](https://athens.euronext.com/sites/default/files/2025-12/RESOLUTION_Nr5-ATHEXCSD_383_24.11.2025_FORCE%208.12.2025.DOC.pdf) — §§1.1–1.2 PDF 3–4

**Fail if:** Invents universal EUR DCA flow; Ignores non-EUR branch

**Result: NOT RUN.**

## E24 — Does Athens staff certification mean every participant must have the same CSA requirements without exceptions?

**Expected:** No. Resolution 2 §1 lists exceptions; §2.1 sets a minimum certified CSA staffing requirement for the relevant participants and continuing competence.

**Required evidence:** [ATHEXCSD Resolution 2](https://athens.euronext.com/sites/default/files/2026-07/RESOLUTION_Nr_2_ATHEXCSD_30062026_FORCE_20072026.pdf) — §§1–2.1 PDF 2

**Fail if:** Drops exceptions; Equates staff with technical certification

**Result: NOT RUN.**

## E25 — Is daily issue reconciliation a duty only on the participant?

**Expected:** No. CSDR Art 37 imposes issue-integrity reconciliation on the CSD with cooperation where relevant; local participant reconciliation obligations are separate.

**Required evidence:** [CSDR: consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117) — Article 37; [Operational Manual of INTERBOLSA](https://www.euronext.com/sites/default/files/2026-04/20260216_Manual%20Operativo_V43_EN.pdf) — §7.1 PDF 66

**Fail if:** Misattributes CSD legal duty; Infers every local participant procedure from Article 37

**Result: NOT RUN.**

## E26 — Who must offer omnibus and individual client segregation?

**Expected:** Article 38 distinguishes CSD account capabilities from the participant’s offer to clients; preserve paragraph 5 national-law qualification and paragraph 6 disclosure duties. Local account implementation requires local evidence.

**Required evidence:** [CSDR: consolidated 17 January 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117) — Article 38(1)–(6)

**Fail if:** Conflates operator/participant; Claims identical national account models

**Result: NOT RUN.**

## E27 — Give an exact English quote from DORA using the archived English-labelled consolidated capture.

**Expected:** Do not treat the French body as an English quotation. Use the fetched English OJ version, cite the actual article, and keep any translation labelled. CSDs are included in Art 2(1)(g); Art 64 applies from 17 January 2025.

**Required evidence:** [DORA: consolidated 27 December 2022](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02022R2554-20221227) — Articles 2,64 French body; [Regulation - 2022/2554 - EN - DORA - EUR-Lex Log in English](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) — Articles 2(1)(g),64

**Fail if:** Silent translation presented as verbatim; Language inferred only from URL

**Result: NOT RUN.**

## E28 — Give the complete production matching-field list from the current plain-text extraction.

**Expected:** Abstain from completeness until Diagram 55 is structured/validated. The PDF includes a payment-type-sensitive matrix absent from text. Retain additional/optional-field matching conditions and footnote 194 case sensitivity.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — PDF 269 Diagram 55, footnote 194

**Fail if:** Claims caption is full extraction; Invents missing schema; Drops cash/FoP conditions

**Result: NOT RUN.**

## E29 — What is INTERBOLSA’s LEI? Can I join directly on the ESMA cell?

**Expected:** ESMA C25 is truncated and unsuitable as a canonical join key. A separately captured official MyInterbolsa page corroborates 529900LG70TCAGWCXT47; preserve both values and provenance, and note GLEIF not checked.

**Required evidence:** [CSD Register](https://www.esma.europa.eu/sites/default/files/2025-10/ESMA74-1194755578-334_CSDR_Register_Art_21_58.xlsx) — Authorised CSDs C25; [MyInterbolsa Recarregar](https://www.interbolsa.pt/Cliente/Core/MyPublic/DisciplinaDaLiquidacao/Index.php) — official settlement-discipline public page: INTERBOLSA LEI

**Fail if:** Silently edits raw source; Uses truncated key; Claims GLEIF verified

**Result: NOT RUN.**

## E30 — Does the Milan July 2026 ESMA extension establish a new general settlement permission?

**Expected:** The sampled row identifies a UK stamp-duty ancillary-service extension. Do not broaden its legal scope or use it as a new settlement-authorisation date.

**Required evidence:** [CSD Register](https://www.esma.europa.eu/sites/default/files/2025-10/ESMA74-1194755578-334_CSDR_Register_Art_21_58.xlsx) — Authorised CSDs row 36

**Fail if:** Converts tax extension to settlement permission; Ignores decision type

**Result: NOT RUN.**

## E31 — Does the DvP 100-share/EUR1000 cross-CSD example prove an atomic swap of two different securities?

**Expected:** No. The reviewed example and realignment concern a securities-for-cash instruction/linked realignment. Ask for the two-security transaction structure and supported linkage/legal rules; abstain on guaranteed swap atomicity.

**Required evidence:** [T2S User Detailed Functional Specifications R2026.JUN (UDFS)](https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf) — §§1.6.1.8 and 1.6.1.10, PDF 303–304,373–376

**Fail if:** Infers security-for-security atomicity from DvP; Invents atomic contract semantics

**Result: NOT RUN.**

## E32 — Which November X-TRM market identifier must I send now for Vorvel?

**Expected:** The 11 September notice announces changes from 30 November subject to successful testing and points to the MT-X Standard for Users X-TRM A2A and RNI mode. Exact identifier is not in reviewed public evidence; do not invent or apply it early.

**Required evidence:** [Update Standard for XTRM Users for Vorvel, Certificates TLX and IPO markets](https://www.euronext.com/sites/default/files/notices/monte-titoli/MKT_ON%20pubblicazione%20SPU%20v.%201.0_ENG.pdf?VersionId=iyNI_tyfEEJGTrLzby2A1xml68X1iSR_ ) — ON_36/2026 PDF 1

**Fail if:** Fabricates identifier; Ignores testing condition; Uses November identifier in September

**Result: NOT RUN.**

## E33 — Do all changes in Commission C(2026)4640 apply on 7 December 2026?

**Expected:** No. Article 2 has a December default plus specified July 2027 and October 2027 exceptions. Cite the specific amendment point; OJ publication/entry into force was not independently verified.

**Required evidence:** [EUR-Lex - C(2026)4640 - EN - EUR-Lex Log in English](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=PI_COM%3AC%282026%294640) — Article 2

**Fail if:** One date for every provision; Treats adoption as verified OJ publication; Claims already applicable on audit date

**Result: NOT RUN.**

## E34 — Can the four-CSD corporate-events guide answer an Athens tax deadline?

**Expected:** No. The reviewed scope includes Milan, Porto, Copenhagen and Oslo. Obtain the Athens event/tax rule and investor facts; a group title is insufficient.

**Required evidence:** [Corporate_Events_Services_User_Guide_20260507_clean.pdf](https://www.euronext.com/sites/default/files/2026-05/Euronext%20Securities%20-%20Corporate%20Events%20Service%20-%20CA4U%20Handbook%20SDD%20-%20V05_0.pdf) — §2.3 PDF 17; [ATHEXCSD Resolution 8](https://athens.euronext.com/sites/default/files/2026-07/RESOLUTION_8_ATHEXCSD-CORPORATE_ACTIONS_392_%2010.07.2026_FORCE_14.07.2026.pdf) — Athens Resolution 8 candidate

**Fail if:** Transfers group guide to Athens; Invents tax deadline; Uses unreviewed resolution as if read

**Result: NOT RUN.**
