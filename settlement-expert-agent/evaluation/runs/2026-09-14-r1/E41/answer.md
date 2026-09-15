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
