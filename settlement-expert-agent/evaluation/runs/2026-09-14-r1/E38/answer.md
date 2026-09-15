# Market claims at Monte Titoli: generation of CLAI instructions and their partial settlement

## Direct answer

A **market claim** is the process by which the buyer in a transaction that has not settled (a "fail") is credited with the income distributed under a corporate action on the securities it should have received. At Monte Titoli it runs **only through X-TRM**, and the resulting settlement instructions are **coded "CLAI"** [[milan-caof]].

- **When are CLAI instructions generated?** Monte Titoli identifies "pending transactions" at the **close of the Settlement Service Operating Day and before the night-time settlement (NTS) stage**, and **CLAI instructions are generated before the beginning of the night-time settlement cycle**. For transactions already matched but unsettled at the **record date**, that generation follows the record-date extraction. For transactions **unmatched at the record date**, the CLAI is generated **at the end of the day on which they become matched**, provided that happens **within the detection period, which runs from the record date to RD+20 Settlement Service Operating Days** [[milan-caof]].
- **Can they be partially settled?** **It depends on what the claim pays.** A **market claim for a cash amount cannot be partially settled**; a **market claim on financial instruments can** [[milan-caof]]. Where it can, the underlying T2S conditions still have to be met — a running partial settlement window, partial-settlement eligibility, and the applicable threshold [[t2s-partial-settlement]].

Both retrievals in this bundle returned **evidence_only**; there is no blocked, needs_context or needs_refresh status to disclose. The limitations attached to each source (below) do apply and are carried through the answer.

## 1. Evidence basis and qualifications

- `[[milan-caof]]` — **Instructions to the Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025)**, §1.4 including footnotes 4–5, PDF 17–25 (printed 13–21); **section reviewed 14 September 2026**, source reviewed 14 September 2026. Body language English; **authoritative language Italian — the Italian text prevails** (cover, PDF 1); translation excerpt with uneven wording, so quoted terms follow the source spelling. Approval: source identity checked, no independent whole-edition supervisory approval certification. LIMITATION: **buyer-protection references point to market practice and to market/CCP rules, which are not admitted evidence.**
- `[[t2s-partial-settlement]]` — **T2S User Detailed Functional Specifications, release R2026.JUN**, §1.6.1.9.3 with Table 68 and footnotes 224–229, PDF 343–345; **section reviewed 14 September 2026**, source reviewed 13 September 2026. Body language English; authoritative language not independently established. LIMITATION: **cash-value thresholds are configured per currency by the T2S Operator and the actual values are not in the excerpt.** LIMITATION: this is the **T2S-native functional description for R2026.JUN — not a local participant interface specification, production XSD or message usage guideline**, so it does not tell you how your own interface to Monte Titoli represents any of it.

A review date records when the evidence was checked; it is not a statement that nothing has changed since. The Milan Instructions edition reviewed here is the one in force as of 30 June 2025.

## 2. Scope: when the Monte Titoli market-claim process applies at all — **Documented requirement**

[[milan-caof]]

- Corporate actions on flow ("CA on flow") at Monte Titoli comprise **market claims** and **transformations**; the question here concerns market claims (CLAI). Transformations produce **TRAN** instructions and work differently — in particular a transformation **cancels the original instruction and enters a new one**, whereas the **market-claim process does not erase the original operation in fail**.
- The management of both processes is **available only through X-TRM**.
- The processes are **not available** where the settlement of the underlying transaction involves a **CSD outside T2S** (so-called external settlement), or where the **corporate action is not managed within the Monte Titoli systems**. In that case participants must handle the claim themselves, by **deleting the failing settlement instructions and entering the corresponding instructions**.
- The Settlement Service operates market claims and transformations **only in currencies allowed in T2S and cleared on the same cash account** on which the pending transaction's settlement is provided. Where necessary, the countervalue of the CLAI instruction is calculated on the **ECB exchange-rate fixing recorded at the record date** (footnote 4).
- The processes apply to **all types of transaction processed by the Settlement Service except realignment instructions generated automatically by T2S**. ("Realignment" instructions are the movements T2S generates across CSD links to keep issuance positions consistent; they are excluded from claim generation.)
- Participants, markets and central counterparties may **exclude** transactions by setting the **OPT-OUT** indicator; transactions bearing **"OPT-OUT = Y" are excluded** from market-claim and reverse-market-claim management. Exclusion can be set by the markets for all transactions traded there that are not CCP-guaranteed, by the **CCP** for all guaranteed transactions, and by **participants for each OTC contract**.

## 3. When CLAI instructions are generated — **Documented requirement**

### 3.1 Which corporate events trigger a market claim

The market-claim process is executed for the following corporate transactions, described as **distributions**: payment of dividends (including mixed dividends); payment of income units of closed-end funds; coupon payment; free share allocation; option-rights assignment (related to a free or paid capital increase); and reimbursement with pool factor [[milan-caof]].

### 3.2 Which transactions are picked up

| Instrument type | Rule as printed [[milan-caof]] |
|---|---|
| **Unit-denominated** (shares and similar) | Relevance is fixed by the **EX-date** set by the markets' trading calendar: contracts negotiated **up to the accounting day before the EX-date (ED-1) relate to securities CUM**; contracts negotiated **from the EX-date relate to securities EX**. For **OTC** transactions the **CUM/EX indicator entered by the counterparties** governs, and the trading date is **not** taken into account for identifying pending transactions. On that basis, the transactions that give rise to market claims are those **(a) matched and not settled by the record date; (b) not matched at the record date but matched within the identification period; (c) submitted to T2S after the record date, referring to securities CUM, and matched within the identification period**. |
| **Nominal** (bonds and similar) | Market claims are generated **only for transactions whose Intended Settlement Date precedes or coincides with the record date and that are not settled by that date**. |
| **Reverse market claim** | Also generated **by transactions traded EX and settled before the record date**, unless those operations bear a **CUM** indicator; in that case the gain is **recognised to the delivering party**. |

Terms used above, explained on first use: the **record date** is the date whose end-of-day position determines entitlement to the corporate action; **CUM** means the trade carries the entitlement, **EX** that it does not; **matched** means the two sides of the instruction have been paired — it is not settlement, and an instruction can be matched and still fail.

### 3.3 Identification timing and the detection period

[[milan-caof]]

- Both processes require Monte Titoli to **identify the pending transactions** according to rules specific to each process. The **identification process is carried out at the close of the Operating Day of the Settlement Service and before the night-time settlement (NTS) stage.**
- Monte Titoli identifies the settlement instructions potentially subject to a market claim **from the record date of the corporate action for the twenty following Settlement Service Operating Days (RD+20)**.
- The identification process is **repeated daily in batch mode at the same time** for the whole detection period, so as to catch (i) a change of state from *unmatched* to *matched* for CUM contracts that were unmatched at the record date, and (ii) transactions entered after the record date but with a trade date before the ex-date (or CUM = Yes).

### 3.4 The moment of generation

[[milan-caof]]

1. **At the record date**, Monte Titoli **downloads the data of matched transactions not settled at that date**.
2. **CLAI settlement instructions are generated before the beginning of the night-time settlement cycle.**
3. **Pending transactions that were unmatched at the record date generate market claims at the end of the day on which they are matched**, provided this occurs **before the end of the detection period**.
4. The generation of a market claim **does not erase the original operation in fail** — the original instruction and the CLAI coexist.

**Antedated record dates.** If, during the identification period, the system detects **(a)** a new corporate event whose record date is earlier than the current date, or **(b)** a change bringing forward the record date of an event already known, Monte Titoli manages the claim automatically according to the state of the underlying at the close of the accounting day coinciding with the new record date. In case (a), for transactions **unmatched at the (past) record date** a market claim is generated **only if matching occurs after that record date and until the accounting date on which the corporate action is detected**; and for **operations settled at the (past) record date but traded from the ex-date**, Monte Titoli generates a **reverse market claim**. In case (b), the general rules apply provided the backdating falls within the detection period. **All other record-date modifications are managed manually**, according to what is communicated via the messaging service or equivalent, and **it is up to participants to act on market claims already generated** [[milan-caof]].

### 3.5 What the CLAI instruction carries, and its lifecycle

For reconciliation purposes, a CLAI instruction contains **at least**: the counterparty participant's ID in the transaction generating the claim; the identification of that transaction; the **corporate-action identifier as assigned by the issuer CSD**; the **trade date, coinciding with the trade date of the original transaction**; the **Intended Settlement Date, coinciding with the scheduled payment date of the corporate action**; the value or amount of financial instruments covered; the **same partial-settlement indicator as the original transaction** (applicable only for market claims on financial instruments, because a cash market claim cannot be partially settled); and the **same on-hold/released status as the original transaction**, whatever its origin (market, CCP, OTC) — participants are expected to mirror any change of status of the original transaction onto the CLAI [[milan-caof]].

Footnote 5 sets out the amount: for a **cash distribution**, the countervalue equals the quantity of shares / nominal value of the original transaction multiplied by the unit value of the corporate action (gross dividend per unit; interest rate); for a **securities distribution**, the quantity of the CLAI equals the original quantity multiplied by the number of instruments distributed, per the ratio established by the issuer [[milan-caof]].

Lifecycle points [[milan-caof]]:

- **Intra-CSD** CLAI instructions relating to unsettled transactions are **matched from the time of generation**.
- **Cross-CSD** CLAI instructions are **forwarded by Monte Titoli to T2S to be matched with the instruction generated by the counterparty's CSD**.
- **Deletion**: CLAI instructions on **OTC** transactions can be deleted by participants under the rules and general conditions applicable to OTC settlement instructions; those on **guaranteed or market transactions are cancelled by Monte Titoli at the request of the markets or the CCPs**. Central counterparties can be the counterparty in withdrawal or delivery of a market claim.
- **Reporting**: available via **X-TRM for ICP participants**; **DCP participants receive the information produced by the T2S platform**, as for all other transactions settled by the Settlement Service; for participants using **RNI messaging, Monte Titoli sends notification message 7B2** on generation of the CLAI instruction (described as a message type forecast). The **layout of that message is not in the reviewed evidence.**

## 4. Partial settlement of CLAI instructions

### 4.1 The Monte Titoli rule — **Documented requirement**

[[milan-caof]], §1.4.1 "Market Claim Settlement":

- **"The Market Claim for payment of amounts in cash can not be partially settled."**
- **"The Market Claim on financial instruments can be partially settled."**
- **CLAI instructions cannot be linked to other CLAI instructions**, and **cannot be included in a pool**.
- The CLAI inherits the **partial-settlement indicator of the original transaction**, and this is expressly stated to be applicable **only** for claims on financial instruments.

### 4.2 The T2S conditions that apply underneath — **Documented requirement**

Partial settlement means T2S settles only a fraction of the original quantity or amount when full settlement is not possible for lack of securities or cash, in order to increase settlement volume and value. For settlement instructions, T2S partially settles **only if all of the following hold** [[t2s-partial-settlement]]:

1. **The partial settlement window is currently running.** (The schedule of those windows is cross-referenced to the UDFS "Settlement Day" section and is **not in this excerpt** — see Open items. No window times may be quoted from this bundle.)
2. **The instructions are eligible to settle partially.** A matched pair is eligible where: they are **FOP, DVP or DWP**; the **partial settlement indicator is not set to "No" in any of the instructions**; and they are **not linked to any other settlement instruction or restriction by a "Before", "After" or "With" link type or by a pool reference**.
3. **The partial settlement threshold criteria are fulfilled.** Thresholds are determined at settlement time from the instruction type (FOP/DVP/DWP), the instruction threshold type, the underlying ISIN and the currency of the cash amount. A **quantity** threshold means partial settlement cannot take place below an applicable quantity; a **cash-value** threshold means it cannot take place below an applicable amount. Per Table 68: **FOP** always resolves to a **quantity** threshold, using the minimum settlement unit (only for the first partial settlement) and the settlement unit multiple; **DVP/DWP with "Quantity" set on both matched instructions** also resolves to a quantity threshold; **DVP/DWP not set to "Quantity" on both** resolves to a **cash-value** threshold, for both unit-quoted and nominal-quoted ISINs. Footnote 228: **cash-value thresholds are not considered for FOP**, regardless of the partial settlement indicator (PARC, PART) in the instruction, including FOP instructions related to a foreign-currency transaction.
4. Threshold parameters are set **by T2S actors through their instruction content** (instruction type and threshold type), **by the T2S Operator in static data for the cash-value threshold** (common to all T2S parties, per settlement currency, separate for unit-quoted and nominal-quoted ISINs), and **by the T2S actors administering the relevant ISIN for the quantity threshold**. **The actual threshold values are not in the reviewed excerpt.**

Two further T2S mechanics that bear on a claim [[t2s-partial-settlement]]:

- **Footnote 224: partial settlement is triggered only in case of lack of securities** (lack of securities alone, or lack of securities and cash) — **not in case of lack of cash only**.
- **Order of attempts:** an instruction is first submitted to a **full settlement attempt**; if it does not settle it goes to the **optimising application process**; only if that finds no full-settlement solution does T2S attempt **partial settlement**, and only where the conditions above are met.
- **Partial release** (a party-hold instruction released for a specified quantity) has its own regime: during the real-time period a partially released instruction can settle for the **total** released quantity outside a window, and for the total **or part** of it during a window, until the relevant cut-off, at which point the partial release is cancelled and the instruction is set back on party hold for the full unsettled quantity; for partial release to count in night-time sequence C2SX it must occur as of the start of day. **The cut-off time itself is not in this excerpt.**

### 4.3 Putting the two layers together — **Reasoned inference**

Derived from [[milan-caof]] read with [[t2s-partial-settlement]]; these are inferences, not quoted rules:

1. **The "not linked / not pooled" T2S eligibility condition is structurally satisfied for CLAI.** Milan states CLAI instructions cannot be linked to other CLAI instructions and cannot be included in a pool; T2S disqualifies instructions linked by "Before"/"After"/"With" or by a pool reference. *Caveat:* Milan's prohibition is expressed as a prohibition on linking CLAI **to other CLAI instructions**, and the reviewed evidence does not state whether a CLAI can be linked to any non-CLAI instruction — so this is a probable, not a certain, alignment.
2. **An original instruction flagged as non-partial propagates.** Because the CLAI carries the **same partial-settlement indicator as the original transaction**, and T2S requires that the indicator is **not set to "No" in any** instruction of the matched pair, a securities market claim derived from a transaction whose indicator was "No" will not settle partially. The reviewed evidence does not give the local X-TRM field or value names for that indicator.
3. **The cash-claim prohibition is consistent with the T2S trigger.** T2S triggers partial settlement only for a **lack of securities**, never for a lack of cash alone; a claim that pays only a cash amount can only fail for want of cash, so there would be nothing for T2S's partial mechanism to act on. This explains, but does not replace, Monte Titoli's explicit rule that a cash market claim cannot be partially settled.
4. **Eligibility still depends on the instruction type actually used.** T2S restricts partial settlement to **FOP, DVP or DWP**. The reviewed evidence **does not state which T2S instruction type Monte Titoli uses for a CLAI** — "PFOD" (payment free of delivery) appears in §1.4.2 only in the transformation context, for option rights from capital increases, and cannot be carried over to market claims. This is an **Unresolved requirement**, and it is the point to confirm before designing anything that depends on partial behaviour of a securities claim.

## 5. What the reviewed evidence does **not** establish — **Unresolved requirement**

- **Any time of day.** The excerpt states that identification happens at the close of the Operating Day and before NTS, and that CLAI instructions are generated before the start of the night-time settlement cycle, but **no clock time, window schedule or participant deadline is in this bundle** — neither the Milan operating timetable nor the T2S partial settlement window schedule (cross-referenced to a UDFS section not retrieved). Do not import a nominal T2S time as a Monte Titoli deadline.
- **Threshold values**: the applicable quantity and cash-value thresholds, and the per-currency values set by the T2S Operator, are expressly outside the excerpt.
- **Field-level layouts**: the content of RNI message **7B2**, the X-TRM representation of the OPT-OUT and partial-settlement indicators, and any ISO 20022 message/version mapping are not in reviewed evidence; the T2S source is a functional description and is expressly not an interface specification, XSD or usage guideline.
- **Buyer protection**: §1.4.2 refers to market practice and to market/CCP rules; those are **not admitted** evidence. (Buyer protection concerns transformations rather than market claims, but it is the adjacent process a reader is likely to ask about next.)
- **Instrument, link and account eligibility** for any particular ISIN or counterparty, and the behaviour of a specific cross-CSD case, are not established here; the cross-CSD path is stated only as "forwarded to T2S for matching with the counterparty CSD's instruction".
- **Release identity**: the T2S content is the **R2026.JUN** functional description. The bundle contains no evidence about any later release's treatment of partial settlement, and nothing here should be read as describing a release that is published but not deployed.

## Open items

1. **T2S partial settlement window schedule** — the UDFS cross-reference to the "Settlement Day" section was not retrieved; obtain that UDFS section (same R2026.JUN edition) before stating when a securities market claim could actually settle partially. Official route: the ECB TARGET/T2S professional-use documents page for the T2S UDFS.
2. **The T2S instruction type used for CLAI instructions** (and therefore whether the FOP/DVP/DWP eligibility gate is met for a securities claim, and how a cash claim is represented) — not in reviewed evidence; confirm with Euronext Securities Milan through the client documentation service.
3. **Applicable partial settlement thresholds** — quantity thresholds set by the ISIN administrator and cash-value thresholds set by the T2S Operator per settlement currency; values are outside the reviewed excerpt.
4. **RNI message 7B2 layout and the X-TRM field mapping** for OPT-OUT, partial settlement and hold/release indicators — the client-only X-TRM standards, available through the Monte Titoli client platform (MT-X), not from the public Instructions.
5. **Whether a CLAI may be linked to a non-CLAI instruction** — the Instructions prohibit linking CLAI instructions to each other and pooling them, but are silent on the general case; needed to confirm inference 1 above.
6. **The Italian authoritative text of Instructions §1.4**, given that the reviewed English version is a translation with uneven wording and the Italian prevails — required before any wording of §1.4 is relied on contractually.
7. **Any Instructions edition or Service Notice later than 30 June 2025** amending §1.4, and any Monte Titoli confirmation that the detection period and generation sequence still stand as printed.
