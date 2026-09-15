# Technical specification (bounded) — ICP interface to Monte Titoli's X-TRM for OTC DvP instructions settled in T2S

**Question.** Write a technical specification for an indirectly connected participant (ICP) that sends OTC delivery-versus-payment (DvP) settlement instructions to Monte Titoli through X-TRM for settlement in T2S: connectivity and static data, the fields to send and their T2S mapping, lifecycle messages and statuses, maintenance functions, and everything that is not published.

**Direct answer.** The reviewed evidence supports a functional specification: the connectivity models and static-data prerequisites, the published X-TRM-to-T2S field correspondence (13 mandatory, 2 additional and 4 optional matching fields plus nine additional indicators), the X-TRM lifecycle (validation, enrichment, real-time routing of OTC instructions to T2S, allegement disclosure, modification, cancellation, hold/release, reporting) and the legal finality points. It does **not** support a production message specification: the X-TRM message layouts (RNI G-messages, SWIFT MT layouts, MT-X standards VER.01.09) are client-only material and are **blocked** (gap G03), and the T2S-native ISO 20022 usage rules and XSDs are **blocked** (gap G14). Three retrievals in this bundle returned `blocked`; they are disclosed in §8. Nothing below is a production field layout, XML fragment or cardinality.

## 0. Scope block

| Item | Value | Label |
|---|---|---|
| CSD and platform | Monte Titoli (Euronext Securities Milan) Settlement Service, settled on T2S | Stated assumption |
| Access model | Indirectly connected participant (ICP) using Monte Titoli's X-TRM connection system | Documented option [[milan-connectivity-static-data]] |
| Instruction scope | OTC sale/purchase (CVT) instructions, DvP/RvP, matched in T2S | Documented category [[milan-xtrm-service]]; DvP-in-EUR and single-ISIN are stated assumptions |
| Roles | Participant (its own account or as settlement agent for Indirect Participants); Monte Titoli as CSD and X-TRM operator; T2S | Documented [[milan-connectivity-static-data]] |
| Governing documents in evidence | Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025); Service Regulations of 26 January 2026; Client Configurations T2S, September 2026 edition (dated 7 September 2026); T2S UDFS R2026.JUN | Documented; Italian text prevails for the Milan documents |
| Review dates | 14 September 2026 for the Instructions, Articles 68 and 73–76, the client-configuration note and T2S status management; 13 September 2026 for Articles 69–72 and the T2S matching section | Documented |
| Release | T2S R2026.JUN for T2S-native content; X-TRM standards version is not established here (the notice naming VER.01.09 is not in this bundle) | Unresolved requirement |
| Not in scope | Market and CCP flows, repos (PCT/PCR), FOP transfers, external (non-T2S) settlement, DCP connectivity | Stated exclusion |
| Blocked retrievals | `milan_xtrm_message_layout` (G03), `production_matching_fields` (G14), `mystandards_usage_rules` (G14) | Disclosed; see §8 |

## 1. Preconditions, permissions, eligibility and static data

1. **Connectivity model (documented requirement).** Participants connect to T2S either as DCP, "using technological systems that interact directly with the T2S platform … certified by the ECB and authorized by Monte Titoli", or as ICP, "using the system for connection to the T2S platform of Monte Titoli whose features are regulated under the X-TRM Service Rules". Issuers admitted under Article 57(1) may enter FOP instructions only through X-TRM. [[milan-connectivity-static-data]] Settlement Service Instructions 30 June 2025, §1.1.1, PDF 7 (printed 3); reviewed 14 September 2026; English translation, Italian text prevails. **Unresolved requirement:** the X-TRM Service Rules themselves are not in this bundle.
2. **LEI (documented requirement).** Participants and Agent Banks "must have a unique LEI code. Failing that, it is not possible to proceed to the configuration of the Participant on the T2S platform and therefore Monte Titoli will not allow the start of operations". §1.2.1, PDF 7.
3. **Static data and Indirect Participants (documented requirement).** Set-up is done by Monte Titoli from information the Participant communicates through the web application CLIMP. To qualify clients as Indirect Participants the Participant must communicate name and LEI of each and associate "one or more securities accounts to be used exclusively" for that Indirect Participant's instructions; the same entity may be an Indirect Participant through more than one Participant. Monte Titoli keeps the domestic codes in use (ABI code, MT code, CED code, LEI) and manages the correspondence between them. §1.2.1, PDF 8. The CLIMP procedures and forms are not admitted (section limitation).
4. **Accounts (documented requirement).** Monte Titoli opens securities accounts in the name of its Participants "regardless of connectivity model"; each must be "connected to a dedicated account (DCA) for cash settlement in central bank money at the T2S platform and also for the purpose of the processes of self-collateralization", with DCA-to-account links configured on the Participant's guidance. §1.2.2, PDF 9.
5. **Changing operating conditions (documented requirement).** Requests go through CLIMP (e-mail fallback address as printed in the 30 June 2025 edition); Monte Titoli updates "normally within 5 days" from a complete request and may take longer for complex or mass updates; an "urgent request" path exists with confirmed timing and fees per the Pricelist; urgent requests must be received "by 4 p.m.", later ones count as received the following day. §1.2.3, PDF 9–10.
6. **Auto-collateralisation opt-in (documented requirement).** Participants or Agent Banks that intend to use the automatic collateral mechanisms must indicate, per the Instructions, the securities accounts or positions usable as collateral and the exposure limits. [[milan-instruction-processing]] Service Regulations 26 January 2026, Article 73(1), PDF 52 (printed 51); reviewed 14 September 2026; Italian text prevails.
7. **Party 2 BIC population (documented requirement, publication-description basis).** In the September 2026 client-configuration list Monte Titoli states: if the CED code in column 2 differs from the CED code in column 6, the BIC in column 1 is the T2S Party 2 in the instruction; if they are equal, "DO NOT use BIC code in column 1 as Party 2" (leave blank or use a different BIC); for an allegement from T2S, a populated Party 2 matching a column-1 BIC assigns the instruction to that trading member, otherwise to the settlement agent in column 6. [[milan-party2-rule]] Client Configurations T2S – September 2026, bilingual header note, PDF 1; published list dated 7 September 2026 that "substitute[s] the previous one"; reviewed 14 September 2026. The per-participant rows are not admitted, so the concrete BIC/CED values must be taken from the published list itself.

## 2. Business sequence and observable states

Layer A is participant ↔ X-TRM (Monte Titoli's interface). Layer B is X-TRM/Monte Titoli ↔ T2S. Layer A message layouts are blocked (§8).

1. **Entry (documented requirement).** The instruction is entered through one of the access methods in the Instructions' §3.3 table: RNI message switching (G52, G53), RNI file transfer (G50, G51), SWIFT FIN or InterAct (MT540, MT541, MT542, MT543, MT548), SWIFT FileAct (G50, G51) or MT-X/X-TRM on-line. [[milan-xtrm-service]] §3.3, PDF 37 (printed 33), transcribed from the rendered page image because text extraction was column-garbled; reviewed 14 September 2026; Italian text prevails. Codes are as printed; layouts are not admitted.
2. **X-TRM validation (documented requirement).** "Formal, logical and congruency checks on the elementary data of each individual settlement instruction"; if not validated, X-TRM "sends a rejection message to the subject that entered it"; if validated, the instruction moves to the next phases. [[milan-xtrm-lifecycle]] §3.4.2, PDF 41 (printed 37); reviewed 14 September 2026; Italian text prevails.
3. **Valorisation / enrichment (documented requirement).** X-TRM adds data from its database ("relations between the parties, securities account and other default information") and calculated data; for a CVT it can "calculate the cash amount"; enrichment fields are expenses amount (OTC only), exchange rate (default 1), price, total commission (OTC only, amount or percentage), unit accrual (interest from the last coupon) and type of operation. Valorisation runs "only if no errors have been detected during the validation phase". §3.4.3, PDF 42–43. Chapter 5 formulas are not in this bundle.
4. **Doubling (documented requirement; reasoned inference for OTC).** Trades from markets, central banks and CCPs, "which by definition are already matched", are doubled into two matched operations. §3.4.4, PDF 43. **Reasoned inference:** OTC instructions are not doubled, because §3.4.5 states they "must be subjected to matching".
5. **Routing to T2S (documented requirement).** Two methods exist: batch "before the starting of the night-time settlement phase" and real-time "at the moment when the instructions are entered, during the opening hours of the X-TRM Service". "Settlement Instructions relating to OTC transactions are sent in real time to the Settlement Service as they must be subjected to matching." T2S then runs its own validation; if T2S rejects, X-TRM relays a rejection; only after T2S validation does X-TRM assign "a univocal reference code (reference ID)" and send an acceptance message. §3.4.5, PDF 44.
6. **Entry into the system, SF1 (documented requirement).** Instructions are "entered" into the Settlement System "from the moment the validation time in T2S ends (SF1)". [[milan-finality]] Service Regulations 26 January 2026, Article 72(1), PDF 51 (printed 50); reviewed 13 September 2026; Italian text prevails.
7. **Matching and allegement (documented requirement).** T2S compares mandatory and non-mandatory matching fields with unmatched instructions; after matching both actors receive a status advice carrying the T2S Matching Reference and the counterparty's references; unmatched instructions trigger an allegement to the counterparty after a waiting period and are cancelled automatically after a period. [[t2s-matching]] UDFS R2026.JUN §1.6.1.2, PDF 267–271; reviewed 13 September 2026. Through X-TRM the participant receives "allegement notification", "allegement remove", "allegement cancellation" and "allegement reporting". [[milan-xtrm-lifecycle]] §3.4.6, PDF 44–45. Monte Titoli's Article 69 adds that unmatched instructions may be changed "only as regards status indicators". [[milan-finality]] Article 69(4), PDF 50.
8. **SF2 (documented requirement).** From matching the instruction "cannot be revoked by a participant or a third party", without prejudice to bilateral cancellation under Article 70(2). [[milan-finality]] Article 72(2), PDF 51.
9. **Settlement processing (documented requirement).** Night-time and day-time phases, gross processing; steps: settlement-status check, securities and cash capacity check (including collateralisation resources and exposure limits), then debit of the seller and credit of the purchaser; in optimisation T2S checks the net balance and, on failure, tries collateralisation for a cash deficit or partial settlement for a securities deficit; unsettled instructions are re-proposed in the next phase or day "until they are settled or cancelled in accordance with the Article 70"; re-proposed instructions may be changed only in their status indicators. [[milan-instruction-processing]] Article 74(1)–(6), PDF 52–53. Priority: Monte Titoli assigns priority to instructions with the Italian Ministry of Finance as counterparty, monetary-policy and Bank of Italy collateral transfers, then Market Management Companies; equal priority settles the earlier settlement date first. Article 68(5) PDF 49–50 and Article 75, PDF 53.
10. **SF3 (documented requirement).** Transfers "become final from the time of the debiting of the cash". [[milan-finality]] Article 72(3), PDF 51.
11. **Status reporting from T2S (documented requirement).** A settlement instruction carries Settlement, Match, Cancellation, CSD Hold, Party Hold, CSD Validation Hold and CoSD Hold statuses; T2S sends status advices on every value change (and on a reason-code change), possibly several values in one advice; the counterparty of a matched instruction is informed of updates except hold changes, which reach it on the intended settlement day; statuses are "intermediate" or "end" statuses; messages are real-time unless optional file bundling is used, bundling being deactivated in the maintenance window and near the DVP cut-off, while in night-time only settlement-related messages are sent bundled (files up to 32 MB). [[t2s-status-management]] UDFS §1.6.3.1, PDF 653–656; reviewed 14 September 2026. **Unresolved requirement:** how X-TRM relays each T2S status to an ICP (the "Results of operations transmission" G56 and the alignment messages G57/G58, MT598/MT548 are listed as channel features only).
12. **Reporting (documented requirement).** Report on request (selection criteria: counterparty code, object code, operation type, settlement date, execution date, date entered, valid/cancelled status, matching status "matched, outbound, acknowledged", origin, settlement system, hold/release indicator status, bilateral cancellation indicator status), online report, and original-entry on-screen report allowing update or cancellation. [[milan-xtrm-lifecycle]] §3.4.8, PDF 47–48.

## 3. Message and field table

### 3a. Fields the ICP must or may send (Table 2 of the Instructions, transcribed from the rendered pages)

Semantics as printed: mandatory fields "if not specified can assume default values"; additional fields, once specified by one counterparty, "must also be specified by the other party"; optional fields are matched "only if specified by both counterparties". [[milan-xtrm-field-mapping]] §3.4.1 Table 2, PDF 39–41 (printed 35–37); reviewed 14 September 2026; Italian text prevails; functional correspondence only.

| # | X-TRM field (as printed) | T2S field (as printed) | Type | Default | T2S matching class for DVP (UDFS Diagram 55–57) |
|---|---|---|---|---|---|
| 1 | Issuer | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO | mandatory |
| 2 | Counterparty | Delivering / Receiving Party BIC (based on Securities Movement Type) | Mandatory | NO | mandatory |
| 3 | Code of System Custody Issuer | CSD of Delivering / Receiving Party | Mandatory | NO | mandatory |
| 4 | Code of System Custody Counterparty (footnote marker 1) | CSD of Delivering / Receiving Party | Mandatory | NO | mandatory |
| 5 | Settlement Date | Intended Settlement Date | Mandatory | blank as printed | mandatory |
| 6 | Data Executed | Trade Date | Mandatory | "Date of release of the contract in X-TRM" | mandatory |
| 7 | Object Code Negotiated | ISIN | Mandatory | NO | mandatory |
| 8 | Quantity | Settlement Quantity | Mandatory | NO | mandatory |
| 9 | Countervalue | Settlement Amount | Mandatory | NO | mandatory (tolerance applies) |
| 10 | Settlement Currency | Currency | Mandatory | NO | mandatory |
| 11 | Mark | Securities Movement Type | Mandatory | NO | mandatory (opposite values match) |
| 12 | Countervalue Verse | Credit / Debit Indicator | Mandatory | NO | mandatory (opposite values match) |
| 13 | n.a. | Payment Type (cell truncated in the original: "this fields will be fill…") | Mandatory | NO | mandatory |
| 14 | Settlement Transaction Condition (footnote marker 1) | Settlement Transaction Condition (Opt Out) | Additional | NO | additional |
| 15 | Trade Transaction Condition | Trade Transaction Condition (cell truncated: "CUM / Ex…") | Additional | NO | additional |
| 16 | Beneficiary Issuer Code BIC | Client of Delivering / Receiving Party | Optional | NO | optional |
| 17 | Beneficiary Counterpart Code BIC | Client of Delivering / Receiving Party | Optional | NO | optional |
| 18 | Common Trade Reference | Common Trade Reference | Optional | NO | optional |
| 19 | Counterpart Settlement Securities Account | Securities Account of Delivering / Receiving Party | Optional | NO | optional |

The last column comes from [[t2s-matching]] UDFS R2026.JUN Diagrams 55–57, PDF 269–270 (visually checked), reviewed 13 September 2026: thirteen mandatory DVP/DWP fields (Payment Type, Securities Movement Type, ISIN, Trade Date, Settlement Quantity, Intended Settlement Date, Delivering and Receiving Party BIC, CSD of each party, Currency, Settlement Amount, Credit/Debit), additional fields (opt-out indicator, CUM/EX indicator) and optional fields (Common Trade Reference, client of each participant, securities account of each party). **Reasoned inference:** the two tables are consistent for DVP; row 13 shows Payment Type is supplied by Monte Titoli's side, not by the ICP ("n.a." as X-TRM field).

Additional information the ICP may specify in X-TRM (documented requirement, same section, PDF 41): ISO code of the operation; partial settlement indicator; priority settlement indicator; indicator for the connection (linking) of settlement instructions; indicator of the changeability of settlement instructions; pool reference ID; reference ID for linked settlement instructions; reference ID for settlement restrictions; identification code for suspension, cancellation or modification of a settlement instruction.

Recorded anomalies (unresolved requirements): footnote marker (1) appears on two rows but its text was not located on PDF 39–41; two T2S-field cells are truncated in the original layout and were not completed.

### 3b. Messages

| Layer | Direction | What is documented | Source | Label |
|---|---|---|---|---|
| A | ICP → X-TRM | Acquisition/changing transactions on RNI M.S. (G52, G53), RNI F.T. (G50, G51), SWIFT FIN/InterAct (MT540–MT543, MT548), SWIFT FileAct (G50, G51), MT-X on-line | [[milan-xtrm-service]] §3.3 table, PDF 37 | Documented channel list; layouts **blocked** (G03) |
| A | X-TRM → ICP | Rejection message (X-TRM validation), rejection relayed from T2S validation, acceptance message with X-TRM reference ID, allegement notification/remove/cancellation/reporting, acceptance or error message per modification request, counterparty hold information on ISD | [[milan-xtrm-lifecycle]] §§3.4.2, 3.4.5–3.4.7 | Documented events; message codes/layouts not established |
| A | X-TRM → ICP | "Results of operations transmission (ROM/ACB)" on RNI F.T. and FileAct (G56) and MT-X; "Alignment on-line system user" on RNI M.S. (G57, G58) and SWIFT FIN (MT598, MT548) | [[milan-xtrm-service]] §3.3 table | Documented channel features; semantics not in evidence |
| B | Monte Titoli ↔ T2S | Settlement instruction, status advices (statuses listed in §2 item 11), allegements, confirmations | [[t2s-status-management]] §1.6.3.1; [[t2s-matching]] §1.6.1.2.3 | Documented at functional level; ISO 20022 identifiers and versions are not in this bundle; usage rules and XSDs **blocked** (G14) |

No XML, element names, cardinalities or reason-code lists are given: none are in reviewed evidence.

## 4. Timing

- **Documented requirement.** X-TRM "is available on working days as indicated in the TARGET operational calendar"; dates in acquired operations may follow other calendars (for example the Borsa calendar) but "must in any case be compatible with the TARGET calendar"; operating timetables depend on the availability of the settlement systems X-TRM interacts with. [[milan-xtrm-service]] §3.1, PDF 36.
- **Documented requirement.** OTC instructions are routed to T2S in real time during X-TRM opening hours; batch routing occurs before the start of night-time settlement; market and CCP timings are set in the Service Notice. [[milan-xtrm-lifecycle]] §3.4.5, PDF 44. The hold/release indicator "may occur during the opening of the X-TRM Service". §3.4.7 C, PDF 47.
- **Documented requirement.** Static-data urgent requests are accepted until 4 p.m. [[milan-connectivity-static-data]] §1.2.3, PDF 10.
- **Unresolved requirement.** X-TRM opening hours, participant cut-off times and the T2S settlement-day schedule are not in this bundle; the T2S nominal schedule is available in the library on the schedule route and the Milan participant timetable after R2026.JUN is a recorded gap (G01). The Instructions' own clock table is quarantined and must not be used.

## 5. Exceptions and controls

1. **Modification (documented requirement).** Only the partialisation indicator, settlement priority and linkage blocks can be edited; a modification instruction is accepted only if the target instruction is not already settled or cancelled and is not CoSD; a partially settled instruction can be changed only in its priority; any other change requires deletion and re-entry; the X-TRM reference code assigned at entry must be supplied; modifications pass X-TRM validation and valorisation; an acceptance or error message is returned for each request. Central-bank instructions cannot be modified by X-TRM participants; market and CCP instructions only if the operator has enabled it. [[milan-xtrm-lifecycle]] §3.4.7 A, PDF 45–46.
2. **Cancellation (documented requirement).** Unilateral cancellation by the entering Participant "up to the time of the matching" unless entered as non-changeable; bilateral cancellation of matched instructions with both Participants' consent (or by a mandated entity); cancellations pass acquisition and, for matched instructions, matching; CoSD instructions may be cancelled only by Monte Titoli; automatic T2S cancellation for instructions that fail daily validation or remain unmatched or unsettled beyond the limits in the Instructions; Participants are informed of the outcome. [[milan-finality]] Article 70(1)–(8), PDF 50; X-TRM cancellation scope in [[milan-xtrm-lifecycle]] §3.4.7 B, PDF 46–47.
3. **Hold and release (documented requirement).** Instructions are in "release" state unless one of the four T2S hold indicators (Party Hold, CSD Hold, CSD Validation Hold, CoSD Hold) is active; enablement is configured by Participant role (Party) or at securities-account level (default); not available for CoSD instructions; X-TRM informs the counterparty of a hold on the ISD and only if the counterparty's instruction is in release state; for repos the indicator can be set separately for spot and forward legs. [[milan-xtrm-lifecycle]] §3.4.7 C, PDF 47. Legal basis: [[milan-finality]] Article 71, PDF 51.
4. **Matching tolerance and comparison rules (documented requirement).** For EUR the tolerance is EUR 2 for a cash countervalue up to EUR 100.000 and EUR 25 above it; if amounts differ within tolerance the deliverer's amount is the matched settlement amount; among several candidates T2S picks the smallest amount difference, then the closest entry time; upper and lower case are different when comparing values (footnote 194). [[t2s-matching]] UDFS §1.6.1.2.3, PDF 269–271. Do not generalise the EUR bands to other currencies (section condition).
5. **Party 2 handling (documented requirement).** Apply the column-2 versus column-6 rule of the published client-configuration list when populating Party 2 and when attributing inbound allegements. [[milan-party2-rule]] PDF 1.
6. **Corporate actions on flow (documented requirement).** Monte Titoli may change or cancel unsettled instructions on instruments in corporate actions or enter rectifying instructions; procedures are in the Instructions (not in this bundle). [[milan-instruction-processing]] Article 76, PDF 53.
7. **Proposed design choice.** Persist the X-TRM reference ID together with the trade reference and, once matched, the T2S Matching Reference; key all maintenance requests on the X-TRM reference ID, since the Instructions require it for modifications.

## 6. Finality and cancellation boundaries

SF1 at the end of T2S validation; SF2 at matching, with bilateral cancellation still possible under Article 70(2); SF3 at the debit of the cash (or of the securities for FOP). [[milan-finality]] Article 72(1)–(3), PDF 51; reviewed 13 September 2026; Italian text prevails. The insolvency procedure and the remainder of Article 72 are not admitted (section limitation).

## 7. Acceptance criteria (evidence-tied)

1. Every outbound OTC instruction carries the thirteen Table 2 mandatory fields with the T2S mapping of §3a; Payment Type is not sent by the ICP. [[milan-xtrm-field-mapping]]
2. An additional field (opt-out or CUM/EX condition) sent by the counterparty is mirrored in the ICP's instruction; optional fields are populated only when agreed. [[milan-xtrm-field-mapping]] [[t2s-matching]]
3. No downstream process treats the X-TRM acceptance with reference ID as settlement, nor "matched" as settled; settlement is recognised only on the settlement-status end value. [[milan-xtrm-lifecycle]] [[t2s-status-management]]
4. Modification requests change only partialisation, priority or linkage blocks and always carry the X-TRM reference code; other changes are implemented as cancel-and-re-enter. [[milan-xtrm-lifecycle]]
5. Cancellation logic distinguishes unilateral (pre-matching) from bilateral (post-matching) cancellation. [[milan-finality]]
6. Party 2 BIC is populated per the published configuration rule. [[milan-party2-rule]]
7. Amount comparisons in reconciliation allow the EUR tolerance bands and treat identifiers case-sensitively. [[t2s-matching]]

## 8. Open dependencies blocking a production specification

| Missing item | Status / gap | Route |
|---|---|---|
| Standard for X-TRM Users (A2A MT / RNI layouts, MT-X standards, VER.01.09) | **Blocked** — client-only in MT-X (G03) | MT-X → Docs → Live Services → Technical Documentation (client account) |
| T2S ISO 20022 usage guidelines and XSDs (sese.023 family and status advices) | **Blocked** — MyStandards requires an account (G14); production matching-field usage not validated | SWIFT MyStandards, T2S community (account) |
| X-TRM Service Rules (document referenced by the Instructions) | Not admitted | Euronext Securities Milan rules hub |
| Service Notices with market/CCP maintenance permissions and routing timings | Not admitted | Euronext Securities Milan notices hub |
| X-TRM opening hours and participant cut-offs after R2026.JUN | Gap G01; Instructions' clock table quarantined | Milan operational notices / MT-X |
| Table 2 footnote (1) text; two truncated T2S-field cells | Anomalies recorded in the transcription | Original PDF layout; Italian edition |
| Per-participant rows of the client-configuration list (BIC, CED/ABI, SAC accounts) | Not admitted | Published list (September 2026 edition) |
| CLIMP procedures and forms; Pricelist for urgent requests | Not admitted | MT-X / Monte Titoli price list |
| T2S message identifiers and versions for the instruction dialogue | Not in this bundle (available in the library on the message route) | `settlement_agent.py retrieve` with the message-flow route |
| Chapter 5 calculation formulas (countervalue, interest) | Not in this bundle | Settlement Service Instructions, Chapter 5 |

## Open items

1. Obtain the Standard for X-TRM Users VER.01.09 through the firm's MT-X account and admit it as a new dated section before writing field layouts (G03).
2. Obtain the R2026.JUN usage guidelines from MyStandards through an authorised account (G14).
3. Confirm the X-TRM cut-off times from a post-June 2026 Milan notice (G01).
4. Resolve Table 2's footnote (1) and truncated cells against the Italian edition of the Instructions.

*Authored by the library maintainer on 14 September 2026 from `bundle.json` in this folder and checked with `settlement_agent.py check` (`checks.json`). Worked example of a bounded technical specification that exposes what is not published; not a production specification and not a model output.*
