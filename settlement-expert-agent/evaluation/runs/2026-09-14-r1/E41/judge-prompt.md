You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
From 21 September 2026, where do Euronext Paris equity trades settle and what is the first intended settlement date under the new model?

# Case category: future-programme (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "MN_07/2026: Euronext Securities Milan becomes designated place of settlement for Paris (XPAR/MLXI/ALXP) equity trades from 21 September 2026; first ISD 23 September; alternative CSD choice remains; announced go-live as of 8 September, not proof of live operation; future mode."
]
Fail conditions (must NOT appear):
[
  "Present as already live on 14 September."
]
Expected sections (if any): ['milan-european-offering-golive']
Expected retrieval statuses: ['evidence_only']

# Rubric
# Evaluation rubric — Settlement Expert Agent

Each end-to-end case is scored on the dimensions below. Three sources of judgement are kept apart and reported separately:

| Source | What it produces | Limits |
|---|---|---|
| Deterministic checks (`settlement_agent.py check`) | Citation ids exist in the retrieved bundle; non-`evidence_only` statuses disclosed; governing-language and publication-description qualifications present; review date stated; no clock times, message versions, EUR amounts or XML absent from the bundle | Pattern-based; cannot judge meaning |
| Independent judge (separate model instance, sees the question, the answer, the actual retrieved passages, the hidden expected points and fail conditions) | Scores 0–2 per dimension with a quoted reason | Same model family as the responder; not a human review |
| Maintainer inspection | For a sample of cases the maintainer reads the source passages against the answer and records agreement or disagreement with the judge | Same assistant that built the library; not independent |

## Dimensions (judge scores 0 = fail, 1 = partial, 2 = met)

1. **Routing / scope** — Did the answer address the entity, service, date and mode the question implies, split multiple intents, and resolve or explicitly assume ambiguous scope?
2. **Evidence selection** — Were the right sections used (compared with the expected sections), including dependency/qualification sections (for example Oslo edition reservation, Milan bilateral cancellation)?
3. **Citation entailment and locator accuracy** — Does each cited passage actually say what the answer attributes to it, with a correct locator (article/section/PDF page) and review date?
4. **Preserved qualifications** — Authoritative language, translation status, approval reservations, publication-description basis, release identity, currency/date scope, LIMITATION lines.
5. **Completeness** — Are the expected key points present, and are the unanswerable parts identified with the missing source named?
6. **No unsupported operational claims** — No invented fields, cardinalities, versions, times, fees, eligibility, deployment or legal effects. Illustrative content labelled.
7. **Justified abstention** — For negative cases: did it decline/limit correctly without refusing the supportable part? For positive cases: did it avoid blanket refusal when evidence was sufficient?
8. **Label discipline** — Documented requirement / reasoned inference / proposed design choice / unresolved requirement used where they matter.

A case **passes** when: no dimension scores 0; dimensions 3, 4 and 6 score 2; and every hidden `must_not` condition is absent. A case is **partial** when it has no 0 but at least one of dimensions 3, 4 or 6 scores 1. Otherwise it **fails**.

Judges must quote the passage that supports or contradicts each key point and must not rely on their own knowledge of CSD rules; if the bundle does not contain a fact, the correct behaviour of the answer is to say so.


# The answer under review
<<<ANSWER
# Euronext Paris equity trades from 21 September 2026: place of settlement and first ISD

## Direct answer

**Documented requirement (announced, not yet observed).** Euronext Securities Milan has published a go-live confirmation stating that, from **21 September 2026**, it *"will become the designated place of settlement for … Equity trades executed on Euronext Amsterdam, Brussels and Paris markets"*, and that **transactions executed on or after 21 September 2026 under the new model will have 23 September 2026 as their first intended settlement date (ISD)**. Trading Members may, however, **designate an alternative settlement system in place of Euronext Securities Milan**, "as further described by Euronext Markets" — so Euronext Securities Milan is the designated default, not an unconditional destination. [[milan-european-offering-golive]] MN_07/2026 "Euronext European Offering: Go-Live confirmation", 8 September 2026, PDF 1–2; reviewed **14 September 2026 (2026-09-14)**; English body, **authoritative language Italian — translation, authoritative language differs**; source identity checked, no independent whole-edition supervisory approval certification; section mode **future**, basis *reference_description*.

Two things this answer is careful not to claim: the go-live is **announced, not proven live** (as at the 14 September 2026 review date, 21 September 2026 was still in the future and nothing in the bundle observes the migration actually happening), and the notice does **not** name the settlement location that applies before that date, so I cannot tell you what these trades move *from*.

## Retrieval statuses

All four retrievals in this bundle returned **evidence_only**. Review dates differ by intent and are named with each claim:

| Retrieval | Context | Status | Review date |
|---|---|---|---|
| 1 | Milan / settlement / participant / **future** — `european_offering_go_live` | evidence_only | 2026-09-14 |
| 2 | Milan / settlement / participant / **future** — `milan_securities_migration_event` | evidence_only | 2026-09-14 |
| 3 | EU / regulatory / participant / current — `settlement_cycle` | evidence_only | 2026-09-13 |
| 4 | EU / regulatory / participant / **future** — `future_t1` | evidence_only | 2026-09-13 |

Routing note: the prepared bundle for this case contained **no retrieval at all** (empty context list), so I used my one permitted routing correction and selected the four contexts above from the topic index. The library's entity vocabulary has no "Paris"/"France" entity; the only reviewed evidence that speaks to Euronext Paris trades is the Euronext Securities **Milan** notice above.

## 1. Scope of the new model — what actually migrates

**Documented requirement.** As of 21 September 2026, Euronext Securities Milan becomes the designated place of settlement for:

- **equity trades** executed on Euronext **Amsterdam, Brussels and Paris** markets; and
- **ETP trades denominated in euro** executed on Euronext **Amsterdam and Paris** markets.

The migration applies to Equity and ETP transactions executed on the MICs **XAMS, XBRU, XPAR, MLXB, XMLI, ALXB, ALXP**; for ETPs the scope is limited to instruments traded in euro. For **physically settled equity derivatives**, the place of settlement "will remain aligned with the underlying instrument and, where applicable, the resulting settlement will be processed through Euronext Securities Milan". Settlement arrangements for **other Euronext markets and other asset classes, including bonds, certificates and warrants, remain unchanged**. Settlement agents are told to ensure operational and settlement arrangements are in place ahead of the migration date. [[milan-european-offering-golive]] MN_07/2026, 8 September 2026, PDF 2; reviewed 14 September 2026; English communication, Italian authoritative; basis *reference_description*.

**Reasoned inference** (from the MIC list plus the equity scope sentence): a Euronext Paris equity trade falls in scope when it is executed on one of the listed Paris MICs — XPAR and ALXP are the Paris-market identifiers in that list — and the trade is an equity (or a euro-denominated ETP). The notice itself does not say which MIC belongs to which market, so treat the MIC-to-market attribution as my inference from the printed list, not as a published mapping.

Qualifications that travel with every sentence above:

- LIMITATION: *"Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication."* This is a market notice, not rulebook text, and its legal effect is not established by the bundle.
- LIMITATION: *"Announced go-live, not proof of live operation; place-of-settlement details for individual instruments require the programme documents."* **Unresolved requirement:** where any specific ISIN will settle cannot be confirmed from this evidence.
- The notice refers back to an earlier market notice ("Euronext Securities to be designated as settlement organisation for Euronext equities and ETFs") and to "subsequent market communications issued throughout the implementation programme". Those documents are **not in the bundle**.
- **Unresolved requirement:** the notice says nothing about account structures, CSD links, issuer-CSD versus investor-CSD roles for the migrated instruments, ICP/DCP access, or instrument eligibility. Roles are relational and defined per securities issue, so "designated place of settlement" must not be read as "Euronext Securities Milan is the issuer CSD" for these securities — the bundle does not establish that.

## 2. The first intended settlement date

**Documented requirement.** *"Transactions executed on or after 21 September 2026 under the new model will have 23 September 2026 as their first intended settlement date (ISD)."* [[milan-european-offering-golive]] MN_07/2026, 8 September 2026, PDF 2; reviewed 14 September 2026; Italian authoritative, English communication.

**Reasoned inference** (derived from that sentence plus the civil calendar): 21 September 2026 is a Monday and 23 September 2026 is a Wednesday, so for a trade executed on the go-live day itself the stated ISD sits two calendar days — and, absent any published holiday for those dates, two business days — after execution. That is consistent with, but not derived from, the CSDR ceiling below.

**Unresolved requirement — do not generalise this into a cycle.** The notice publishes the *first* ISD of the new model; it does **not** publish a settlement-cycle rule for trades executed on 22 September 2026 or later, and it does not state which calendar governs the business-day count. Anything of the form "therefore every Paris equity trade settles on T+2 from now on" is not supported by this evidence.

**Documented requirement (legal ceiling, separate intent, reviewed 13 September 2026).** CSDR Article 5(1) requires participants to settle on the intended settlement date, and Article 5(2) provides that for transactions in transferable securities **executed on trading venues the ISD "shall be no later than on the second business day after the trading takes place"**, with carve-outs for privately negotiated transactions executed on a venue, bilaterally executed transactions reported to a venue, and the first transaction where securities are subject to initial recording in book-entry form under Article 3(2). [[csdr-5]] CSDR consolidated text of 17 January 2026, Article 5; reviewed **13 September 2026 (2026-09-13)**; EU official languages, original/official-language text; source identity checked, no independent whole-edition supervisory approval certification. LIMITATION: legal context only, not local procedures and not Norwegian incorporation; future amendments are separate.

**Reasoned inference:** Article 5(2) sets a maximum, not a mandatory cycle — a "no later than" ceiling. The ISD of 23 September 2026 for a 21 September 2026 execution sits at that ceiling, but the ceiling neither produces that date nor fixes the ISD of any other trade date.

**Documented requirement (future law, not applicable on 21 September 2026).** Regulation (EU) 2025/2075 Article 1 replaces CSDR Article 5(2) so that the ISD for venue-executed transactions "shall be no later than on the first business day after the trading takes place", with exclusions including privately negotiated transactions executed on a venue, bilaterally executed transactions reported to a venue, initial book-entry recording, and certain securities financing transactions (securities lending/borrowing, buy-sell back and sell-buy back, repurchase transactions) documented as single transactions composed of two linked operations. Article 2 states that the Regulation **applies from 11 October 2027**. [[t1-law]] Regulation 2025/2075, Articles 1 and 2; reviewed **13 September 2026**; body language English, **authoritative language not independently established**; basis *reference_description*. LIMITATION: adopted law with future application on 11 October 2027 — never auto-promote by date.

**Reasoned inference:** because the T+1 amendment applies only from 11 October 2027, it has no bearing on the 21 September 2026 go-live or on the 23 September 2026 first ISD. Adoption is not application.

## 3. Adjacent dated event on the same day — ETPs only, not equities

**Documented requirement.** A separate Milan notice states that **on 23 September 2026, from the opening of business on Wednesday 23 September 2026**, listed **ETP** instruments will migrate issuer CSD as follows: Issuer CSD **Euroclear Sweden** — from Euroclear Bank to **Euroclear France**; **SIX-SIS** — from Euroclear Bank to **SIX-SIS**; **Euroclear UK&I** — from Euroclear Bank to **Euroclear UK&I**; **DTCC** — from Euroclear Bank to **DTCC**. For settlement instructions on the migrated securities: **in T2S**, only cross-CSD instructions sent to T2S by the migration date and pending on 22 September 2026 will be deleted from T2S without any action by the client; **external**, for transactions sent for settlement by the migration date and pending on 22 September 2026, and for transactions not sent for settlement by the migration date, a cancellation request will be sent by Euronext Securities Milan. **It is the customer's responsibility to re-enter the instruction, from 23 September 2026 onward, to allow proper routing to the settlement system (T2S/ICSD) based on the related SSI.** [[milan-securities-migration-sep23]] ON_31/2026 "Securities migration", 31 July 2026, PDF 1–2; reviewed **14 September 2026**; English communication, **authoritative language Italian — translation, authoritative language differs**; PRIVATE footer despite public publication; basis *reference_description*, mode future. LIMITATION: operational/market notices are not the Service Regulations or Instructions. LIMITATION: **the ISIN list referenced by the notice is not admitted**, so which instruments are affected cannot be checked here.

**Reasoned inference and scope warning:** this migration is expressly about **ETP ISINs** and their issuer CSD; it is *not* the equity migration asked about, and the two notices do not cross-reference each other in the reviewed text. What they share is the calendar: 23 September 2026 is both the first ISD of the European Offering model and the effective date of this ETP issuer-CSD migration. A participant trading Paris equities and euro ETPs should read the second notice only for its instruction-handling consequences on ETPs, not as evidence about equities.

## 4. What a participant should take from this (labelled)

| # | Statement | Label |
|---|---|---|
| 1 | From 21 September 2026 Euronext Securities Milan is the designated place of settlement for equity trades on Euronext Amsterdam, Brussels and Paris (MICs XAMS, XBRU, XPAR, MLXB, XMLI, ALXB, ALXP) | Documented requirement (market notice, announced) |
| 2 | Trading Members may designate an alternative settlement system instead | Documented requirement; the description of how is in Euronext Markets material not in the bundle |
| 3 | First ISD under the new model is 23 September 2026 | Documented requirement |
| 4 | 21 September 2026 → 23 September 2026 is a two-business-day interval on the civil calendar | Reasoned inference (calendar arithmetic) |
| 5 | The settlement cycle applying to trades executed after 21 September 2026 | Unresolved requirement — not published in this notice |
| 6 | The place of settlement before 21 September 2026 (e.g. which CSD these trades leave) | Unresolved requirement — not named in reviewed evidence |
| 7 | Where a specific ISIN will settle; account, link and eligibility arrangements | Unresolved requirement — programme documents required (LIMITATION on [[milan-european-offering-golive]]) |
| 8 | That the migration has actually gone live | Unresolved requirement — announcement only, as at review date 14 September 2026 |
| 9 | Confirm in advance with your settlement agent whether you will use Euronext Securities Milan or an alternative settlement system, and re-point SSIs accordingly before 21 September 2026 | Proposed design choice — an implementation decision for you, prompted by the notice's instruction to settlement agents; not an infrastructure rule |
| 10 | Plan to re-enter ETP instructions deleted or cancelled around the 23 September 2026 ETP migration | Proposed design choice, resting on the documented customer responsibility in [[milan-securities-migration-sep23]] |

## Open items

1. **Programme documents for the European Offering**: the referenced market notice "Euronext Securities to be designated as settlement organisation for Euronext equities and ETFs" and the subsequent implementation-programme communications, plus the Euronext Markets description of how a Trading Member designates an alternative settlement system. Needed to establish per-instrument place of settlement, account and link arrangements. Official route: Euronext Securities Milan's published notices and the Euronext Markets notice service; for client-specific arrangements, the Relationship Manager / Client Onboarding contacts printed in MN_07/2026. I have not contacted anyone.
2. **Settlement-cycle rule after the first ISD** and the **calendar** used to count business days for these markets: not in reviewed evidence; a Milan timetable/notice chain would establish it (the library records the Milan timetable notice chain as unresolved, gap **G01**).
3. **The ISIN list behind ON_31/2026** is not admitted, so no instrument-level confirmation of the 23 September 2026 ETP migration is possible here.
4. **Confirmation that go-live occurred**: as at the review date this is an announcement about a future date. A post-go-live notice or an updated review would be needed; nothing in this bundle observes live operation.
5. **Review dates and freshness**: the Milan notices were reviewed **14 September 2026 (2026-09-14)**; CSDR Article 5 and Regulation 2025/2075 were reviewed **13 September 2026 (2026-09-13)**. Available review dates in this library are 2026-09-13 and 2026-09-14; nothing here is asserted as verified after those dates.
6. **Legal status of the notices**: they are English communications by Euronext Securities Milan with the **Italian text authoritative** where a translation exists, they are not the Service Regulations or the Instructions, and no independent whole-edition supervisory approval certification exists for them. If the answer must stand on rulebook authority, the Service Regulations/Instructions text implementing the European Offering is still required and is not in reviewed evidence.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:56:42.134374+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "future", "question_type": "european_offering_go_live"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-european-offering-golive]] — European Offering go-live confirmed for 21 September 2026: scope, MICs, alternative CSD choice and first ISD 23 September (reviewed 2026-09-14; modes ['future']; entities ['Milan']; basis reference_description)
CITATION: MN_07/2026 Euronext European Offering: go-live confirmation (8 September 2026) | MN_07/2026 PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/20260903%20Euronext%20Securities%20Milan%20Market%20Notice%20-%20EE_0.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Announced go-live, not proof of live operation; place-of-settlement details for individual instruments require the programme documents.
EXCERPT (MN_07/2026 PDF 1–2):
[PDF page 1]

08 September 2026
MN_07/2026

Euronext European Offering: Go-Live
confirmation
   To the attention of:                           All Participants


   Priority:                                      High


   Topic:                                         Euronext European Offering: Go-Live
                                                   confirmation




Dear Client

Further to the Market Notice "Euronext Securities to be designated as settlement
organisation for Euronext equities and ETFs" and the subsequent market
communications issued throughout the implementation programme, Euronext
Securities Milan confirms that the go-live of the Euronext European Offering will
take place as planned on 21 September 2026.

This milestone represents a significant step in Euronext's strategy to further
harmonise post-trade services across its markets, reduce settlement fragmentation
and enhance the efficiency of the European post-trade infrastructure.

Scope:

As of this date, Euronext Securities Milan will become the designated place of
settlement for:

     •    Equity trades executed on Euronext Amsterdam, Brussels and Paris markets;
          and
     •    ETP trades denominated in euro executed on Euronext Amsterdam and Paris
          markets.
This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 2



[PDF page 2]

The migration applies to Equity and ETP transactions executed on the following
MICs:
   •   XAMS
   •   XBRU
   •   XPAR
   •   MLXB
   •   XMLI
   •   ALXB
   •   ALXP
For ETPs, the scope is limited to instruments traded in euro.

Trading Members may designate an alternative settlement system in place of
Euronext Securities Milan, as further described by Euronext Markets.

Transactions executed on or after 21 September 2026 under the new model will
have 23 September 2026 as their first intended settlement date (ISD).

Settlement agents should ensure that all required operational and settlement
arrangements are in place ahead of the migration date.

For physically settled equity derivatives, the place of settlement will remain aligned
with the underlying instrument and, where applicable, the resulting settlement will
be processed through Euronext Securities Milan.

The settlement arrangements applicable to other Euronext markets and to other
asset classes, including bonds, certificates and warrants, remain unchanged.

Further information:

For further information, please contact your Relationship Manager or the Client
Onboarding team.


Client Onboarding Team
E: CSD.Onboarding@euronext.com


Sales & Relationship Management
E: MTsalesteam@euronext.com




| 2 of 2

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "future", "question_type": "milan_securities_migration_event"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-securities-migration-sep23]] — ETP issuer-CSD migration on 23 September 2026 and handling of pending cross-CSD/external instructions (reviewed 2026-09-14; modes ['future']; entities ['Milan']; basis reference_description)
CITATION: ON_31/2026 Securities migration on 23 September 2026 (31 July 2026) | ON_31/2026 PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/EE_ON%20pubblicazione_31.07%20v.%200.1%20ENG_1.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: The ISIN list referenced by the notice is not admitted.
EXCERPT (ON_31/2026 PDF 1–2):
[PDF page 1]

31 July 2026
ON_31/2026



Securities migration


   To the attention of:                           Intermediaries


   Priority:                                      High


   Topic:                                         Securities migration



Dear client,

We would like to inform you that on 23rd September 2026, the ETPs instruments listed in the
following ISINs list will be migrated as described below. The migration will take effect from the
opening of business on Wednesday 23rd September 2026.

Specifically, the following migrations will apply only to the ETPs ISINs for which the Issuer CSD
indicated in Column H of the above linked document corresponds to the values below:

     •    Issuer CSD Euroclear Sweden: from Euroclear Bank to Euroclear France
     •    Issuer CSD SIX-SIS: from Euroclear Bank to SIX-SIS
     •    Issuer CSD Euroclear UK&I: from Euroclear Bank to Euroclear UK&I
     •    Issuer CSD DTCC: from Euroclear Bank to DTCC

The following are the guidelines for managing settlement instructions relating to the migrated
securities.

     •    In T2S: Only Cross-CSD instructions sent to T2S by the migration date and which are
          pending on 22nd September 2026, will be deleted from the T2S system without any action
          by the client.
     •    External: For transactions sent for settlement by the migration date and which are
          pending on 22nd September 2026, and for transactions not sent for settlement by the
          migration date, a cancellation request will be sent by Euronext Securities Milan.
This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 2

                                                             PRIVATE



[PDF page 2]

It is the customer's responsibility to re-enter the instruction, which must be done from 23rd
September 2026 onward to allow the proper routing to the settlement system (T2S/ICSD) based
on the related SSI.



For support or clarification, please send an email to the following address:

Email: eam@euronext.com




| 2 of 2


                                            PRIVATE

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "settlement_cycle"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[csdr-5]] — Settlement-cycle ceiling and exceptions (reviewed 2026-09-13; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: CSDR: consolidated 17 January 2026 | CSDR Article 5; consolidation 17 January 2026 | version None | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
EXCERPT (CSDR Article 5; consolidation 17 January 2026):
Article 5

Intended settlement date

1.   Any participant in a securities settlement system that settles in that system on its own account or on behalf of a third party transactions in transferable securities, money-market instruments, units in collective investment undertakings and emission allowances shall settle such transactions on the intended settlement date.
2.   As regards transactions in transferable securities referred to in paragraph 1 which are executed on trading venues, the intended settlement date shall be no later than on the second business day after the trading takes place. That requirement shall not apply to transactions which are negotiated privately but executed on a trading venue, to transactions which are executed bilaterally but reported to a trading venue or to the first transaction where the transferable securities concerned are subject to initial recording in book-entry form pursuant to Article 3(2).
3.   The competent authorities shall ensure that paragraph 1 is applied.

The authorities competent for the supervision of trading venues shall ensure that paragraph 2 is applied.

CHAPTER III

Settlement discipline

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "future", "question_type": "future_t1"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t1-law]] — Adopted T+1 amendment with future application (reviewed 2026-09-13; modes ['future']; entities ['EU']; basis reference_description)
CITATION: T+1 amendment 2025/2075 | Regulation 2025/2075 Article 1 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2075
CITATION: T+1 amendment 2025/2075 | Article 2 | version None | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2075
LIMITATION: Adopted law; future application on 11 October 2027. Never auto-promote by date.
EXCERPT (Regulation 2025/2075 Article 1):
Article 1

Amendments to Regulation (EU) No 909/2014

Regulation (EU) No 909/2014 is amended as follows:

(1)

	

in Article 5, paragraph 2 is replaced by the following:

‘2.   As regards transactions in transferable securities referred to in paragraph 1 which are executed on trading venues, the intended settlement date shall be no later than on the first business day after the trading takes place.

The requirement laid down in the first subparagraph shall not apply to any of the following:

(a)

	

transactions which are negotiated privately but executed on a trading venue;

(b)

	

transactions which are executed bilaterally but reported to a trading venue;

(c)

	

the first transaction where the transferable securities concerned are subject to initial recording in book-entry form pursuant to Article 3(2);

(d)

	

the following securities financing transactions, provided that they are documented as single transactions composed of two linked operations:

(i)

	

securities lending or securities borrowing as defined in Article 3, point (7), of Regulation (EU) 2015/2365 of the European Parliament and of the Council (*1);

(ii)

	

buy-sell back transactions or sell-buy back transactions as defined in Article 3, point (8), of Regulation (EU) 2015/2365;

(iii)

	

repurchase transactions as defined in Article 3, point (9), of Regulation (EU) 2015/2365.

(*1)  Regulation (EU) 2015/2365 of the European Parliament and of the Council of 25 November 2015 on transparency of securities financing transactions and of reuse and amending Regulation (EU) No 648/2012 (OJ L 337, 23.12.2015, p. 1, ELI: http://data.europa.eu/eli/reg/2015/2365/oj).’;"

(2)

	

Article 74 is amended as follows:

(a)

	

in paragraph 1, point (a), the following point is inserted:

‘(ia)

	

the categories of transactions, the intended settlement date of the transactions and whether the transactions are executed on trading venues;’

;

(b)

	

in paragraph 2, first subparagraph, point (d) is replaced by the following:

‘(d)

	

upon request from the Commission, for the reports referred to in paragraph 1, point (a)(ia) and points (e), (h), (j) and (k).’

;

(3)

	

in Article 75, first paragraph, the following point is inserted:

‘(aa)

	

the market impact of, and the justification for, the exemption for certain types of securities financing transactions from the requirement to settle no later than on the first business day after the trading takes place as laid down in Article 5(2);’.
EXCERPT (Article 2):
Article 2

Entry into force and application

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

It shall apply from 11 October 2027.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
