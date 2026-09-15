You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Explain market claims at Monte Titoli: when are CLAI instructions generated, and can they be partially settled?

# Case category: explanation (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "CLAI generated for matched-not-settled at record date, unmatched matched within RD+20, CUM trades after RD; reverse market claims; opt-out; CLAI cash cannot be partially settled, securities can; no links/pools; cross-CSD CLAI forwarded to T2S for matching."
]
Fail conditions (must NOT appear):
[
  "Invert the partial-settlement rule."
]
Expected sections (if any): ['milan-caof']
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

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.499922+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_partial_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-partial-settlement]] — Partial settlement conditions, thresholds and procedure (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Cash-value thresholds are configured per currency by the T2S Operator; actual values are not in this excerpt.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.9.3 with Table 68 and footnotes 224–229; PDF 343–345):
1.6.1.9.3 Partial Settlement

 2   Concept

 3   T2S provides partial settlement process, i.e. settles only a fraction of the original quantity or amount when
 4     full settlement is not possible due to lack of securities or cash, in order to increase the volume and value of
 5    settlement.

 6   Overview

 7     Partial settlement applies under conditions and procedures that differ whether they apply to:

 8         l  Settlement Instructions;

 9         l  Settlement Restrictions;

10         l  Liquidity transfers.

11    Partialsettlementprocess

12     Partial settlement process for Settlement Instructions

13   A Settlement Instruction is partially settled 224, in case there are insufficient securities to settle the full quan-
14     tity and provided the following conditions are met:

15         l  The partial settlement window is currently running; 225

16         l  The Settlement Instructions are eligible to settle partially;

17         l  The partial settlement threshold criteria are fulfilled.

18    Partial settlement window

19     Partial settlement is active in T2S within the dedicated partial settlement windows 226.

20    Partial settlement eligibility

21   The settlement eligibility depends notably on conditions set by the T2S parties on their matched Settlement
22    Instructions.

23   A matched pair of Settlement Instructions is eligible to partial settlement, when these Settlement Instruc-
24    tions are entered by the T2S parties with the following characteristics:

25         l  They are related to Free Of Payment or to Delivery Versus Payment or Delivery With Payment; 227

26         l  The partial settlement indicator is not set to "No" in any of the Settlement Instructions;

27         l  They are not linked to any other Settlement Instruction or Settlement Restriction by the T2S parties by a
28         link type “Before”, “After” “With” or by a pool reference.

     _________________________


        224    Partial settlement is triggered only in case of lack of securities (i.e. lack of securities only or lack of securities and cash) but not in case of lack of
               cash only.

        225    Partially released Settlement Instructions can be submitted for settlement attempts for the total partially released quantity also when the partial
                settlement window is not running. Partially released Settlement Instructions can be submitted for settlement attempts for a part of the partially
                released quantity only when the partial settlement window is running.

        226   For details about the schedule of partial settlement window, see section Settlement Day [ 155]

        227    Including such Settlement Instructions which are on Party Hold and have been partially released.


                                                                                            Page 343 of 2017



[PDF page 344]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1     Partial settlement of Partially Released Settlement Instructions

 2   A Settlement Instruction on Party Hold may be partially released to allow the partial settlement of a specified
 3    quantity. This Partially Released Settlement Instruction must conform to all the conditions of partial settle-
 4   ment as for any other Settlement Instruction. During the real-time period the partial settlement of Partially
 5    Released Settlement Instructions can occur outside a partial settlement window for the total partially re-
 6    leased quantity, as well as during a partial settlement window for the total or part of the partially released
 7    quantity and until the relevant cut-off time (partial release is only valid for the current business day) at
 8    which point the partial release will be cancelled and the underlying Settlement Instruction set back on Party
 9    Hold for the full unsettled quantity. For partial release to be considered during sequence C2SX of the night
10    time settlement the partial release must occur as of the start of day.

11    Partial settlement threshold

12     Partial settlement is conditioned by thresholds, below which it cannot apply, and that are determined in T2S
13   when the settlement occurs, on the basis of the following content of the Settlement Instructions:

14         l  The instruction type (FOP or DVP or DWP);

15         l  The instruction threshold type (see table below);

16         l  The underlying ISIN;

17         l  The currency of the cash amount of the Settlement Instruction.

18   These contents of the Settlement Instructions allow T2S to determine the type of partial settlement thresh-
19    old applicable on the Settlement Instructions being processed. The following types of partial settlement
20    thresholds are possible:

21         l A threshold in “quantity”: meaning the partial settlement cannot take place for a quantity lower than an
22        applicable value;

23         l A threshold in “cash value”: meaning the partial settlement cannot take place for an amount lower than
24      an applicable value.25





                                                                                            Page 344 of 2017



[PDF page 345]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                            TABLE 68 - APPLICABLE THRESHOLD TYPES FOR PARTIAL SETTLEMENT
 2

               CONTENT OF SETTLEMENT INSTRUCTION            RESULTING     RESULTING APPLICABLE
                                                                 APPLICABLE      THRESHOLD VALUE
       INSTRUCTION     INSTRUCTION         ISIN     CURRENCY
                                                         THRESHOLD
           TYPE       THRESHOLD TYPE
                                                                 TYPE

      FOP 228          n/a                     applicable    n/a          Quantity    Minimum settlement unit (only for
                                                                                                                         first partial settlement) and set-
     DVP/DWP        Set to “Quantity” for
                                                                                      tlement unit multiple are used.
                       both matched Settle-
                     ment Instructions

     DVP/DWP        Not set to “Quantity”   Unit-quoted  applicable    Cash value   Amount configured in the currency
                             for both matched Set-                                              specified (for quantity, minimum
                        tlement Instructions                                            settlement unit and settlement
                                                                                                  unit multiple are used).

                                             Nominal-                          Amount configured in the currency
                                            quoted                                     specified (for quantity, minimum
                                                                                        settlement unit and settlement
                                                                                                  unit multiple are used).

 3   The parameters determining the threshold applicable above are set:

 4         l  By T2S Actors from the content of their Settlement Instructions for the instruction type and instruction
 5        threshold type mentioned in the table above;

 6         l  By the T2S Operator inside the Static Data for the applicable threshold in cash value. This parameter is
 7      common to all T2S Parties, and set per T2S settlement currency, and separate for unit-quoted or nomi-
 8        nal quoted ISIN;

 9         l  By the T2S Actors in charge of the administration of the relevant ISIN in the Static Data for the applica-
10        ble threshold in quantity (See section Concept of securities in T2S [ 71]).

11    Partial settlement procedure

12    Settlement Instructions are submitted to a full settlement attempt before being submitted to a partial set-
13    tlement attempt. 229

14    In case the Settlement Instruction does not settle, the Settlement Instruction is submitted to Optimising
15    application process. The Optimising application process tries to settle the failed Settlement Instruction with
16    other Settlement Instructions in T2S based on different technical optimisations. In case the Optimising appli-
17    cation process is not able to find a solution for a full settlement, T2S tries to submit the Settlement Instruc-
18    tion for partial settlement provided the above conditions are met.

     _________________________


        228   Cash value thresholds are not considered for FOP regardless of the partial settlement threshold type (partial settlement indicator PARC, PART)
                defined within the settlement instruction. This also applies for FOP instructions related to a foreign currency transaction (non-EUR amount).

        229    Partially Released Settlement Instructions are only submitted to partial settlement attempts for the released quantity.


                                                                                            Page 345 of 2017

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_market_claims_transformations"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-caof]] — Corporate actions on flow: market claims and transformations (§1.4) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §1.4 including footnotes 4–5; PDF 17–25, printed 13–21 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Buyer protection references market practice and market/CCP rules, which are not admitted.
EXCERPT (§1.4 including footnotes 4–5; PDF 17–25, printed 13–21):
1.4 MANAGEMENT OF OPERATIONS IN CASE OF CORPORATE
EVENTS (CD CORPORATE ACTION ON FLOW)

The management of unsettled transactions in financial instruments of corporate
actions includes the following processes based on the corporate event on the
financial instrument:

    a) Management of Market Claim

    b) Management of Transformation

The management of these processes is available only through X-TRM.

The management process of Market Claim allows to recognize to the receiving
counterparty in an unregulated transaction (fail) the income distributed as part
of a corporate action relating to the securities subject to the transaction in fail.

The management process of Transformation allows to recognize to the receiving
counterparty in an unregulated transaction (fail), the securities or the proceed
resulting as part of a corporate action relating to the securities subject to the
transaction in fail.

The management processes of Market Claim & Transformation are not available if
the regulation underlying transaction involving a CSD outside T2S (cd external
settlement) and in cases where the corporate operation is not managed within
the Monte Titoli systems. In this latter case, participants must provide for the
management of Market Claims and Transformation by deleting the fail settlement
instructions and entering the corresponding settlement instructions, in line with
the procedures described below.

The Settlement  Service  operates  solely Market Claim & Transformation  in
currencies allowed in T2S and cleared on the same cash account on which the
settlement of the pending transaction is provided4.

Both processes require identification by Monte Titoli - according to specific rules
for each process - of transactions in financial instruments which may result in a
Market Claim or a Transformation (cd pending transactions).

The  identification process  is  carried out  at the  close  of Operating Day  of
Settlement Service and before the stage night-time settlement (NTS).





4 Where necessary, the countervalue of the CLAI instruction is calculated on the basis of the exchange rate fixing of the ECB
recorded at the record date.





13



[PDF page 18]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The management processes of Claim Market and Transformation apply to  all
types of transactions processed by the Settlement Service except instructions
realignment generated automatically by T2S.

The  Participants, markets and  central  counterparties may  exclude  certain
transactions from the management process of Market Claim or Transformation,
valuing the appropriate indicator OPT-OUT.


1.4.1 Market Claim

    •  Operations that originate a Market Claim

The process of managing the Market Claim  is executed when the following
corporate transactions (cd. Distributions) occurs:

    •  Payment of dividends (including mixed dividends);
    •  payment income units of closed-end funds;
    •  coupon payment ;
    •  free share allocation;
    •  option rights assignment (related to capital increase free or paid)
    •  reimbursement with pool factor.

The transaction giving rise to the Market Claim are identified according to the
following rules.

For  transactions  involving  financial instruments denominated  in  units  (e.g.
Shares and similar securities)

   Monte Titoli identifies relevant transactions:

    •   for  transactions coming from guaranteed  or non-guaranteed market,
      according to the EX-date established according to the trading calendar of
      the markets. All contracts negotiated by the end of the accounting day
      previous  of  the  EX-date (ED-1)  relate  to  securities CUM.  Contracts
      negotiated from the EX-date relate to securities EX,
    •   for transactions concluded OTC according to the CUM or EX indicator
      entered by the counterparties, for the management of Market Claim. In
      that case is not taken into account the trading date for the identification of
      pending transactions.

   In this context, the transaction giving rise to Market Claims are:

    a) matched and not settled by the Record Date;





14



[PDF page 19]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





    b) not matched  at the Record Date, but matched  within the period  of
       identification;
    c) submitted to the T2S system after the Record Date, referred to securities
     CUM, and matched within the period of identification.

For transactions involving bonds and similar securities ("nominal")


   The Market Claim are only generated for transactions with the Intended
   Settlement Date preceding or coinciding with the Record Date and not settled
   by that date.

The  Market  Claim  are  also  generated  by  transactions  involving  financial
instruments traded EX and settled before the Record Date (cd. Reverse Market
Claim), unless such operations bear an indicator CUM. In this case the gain is
recognized to the deliverying party.

The process of managing the Market Claim can be excluded according to the
rules specified:

    •  by the markets, for all transactions therein negotiated if not guaranteed by
       central counterparties;
    •  by the CCP for all guaranteed transactions;
    •  by the Participants for each OTC contract.

The operations that bear the indicator "OPT-OUT = Y" are excluded from the
management of Market Claim or Claim Reverse Market.

    •  Timing of identification process

Monte Titoli identifies the Settlement Instructions potentially subject to Market
Claim, cd. pending operations, from the Record Date of the corporate action for
the twenty following Settlement Service Operating Days(RD+20).

The identification process is repeated daily with batch mode at the same time,
for the duration of the period of the identification (detection period), in order to
verify the  possible change  of  state (from "unmatched  "  to "matched")  of
contracts involving securities CUM unmatched on Record Date (as evidence
produced to the same Record Date), or to identify any transactions entered after
the Record Date but with Trade Date before Ex Date (or indicator CUM = Yes) .

    •  Generation of the settlement Instructions  for the management of the
      Market Claim





15



[PDF page 20]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Settlement Instructions generated for the management of Market Claim are
coded as ‘’CLAI’’.

The process of generating Market Claim will not erase the original operation in
fail.
At the Record Date Monte  Titoli download data of matched transactions not
settled at that date. CLAI Settlement instructions are generated before the
beginning of the night time settlement cycle.

Pending transactions unmatched at Record Date generate Market Claims at the
end of the day in which they are matched (before the end of the detection
period).

For the purposes of the reconciliation process, the instruction "CLAI" contains at
least the following information:

    ▪  Participant's ID counterpart in the transaction that generates the Market
      Claim;
    ▪  the identification of the transaction that generates the Market Claim;
    ▪  the identifier of the corporate action , as assigned by the Issuer CSD;
    ▪  the trade date, Trade Date (TD), coinciding with the Trade Date of the
       original transaction;
    ▪  the  Intended  Settlement Date  (ISD),  coinciding  with  the  scheduled
     payment date of the corporate action;
    ▪  the value or the amount of financial instruments covered by the Market
      Claim5.
    ▪  the same  indicator  of  the  original  transaction  for  partial  settlement
       (applicable only in case of Market Claim on financial instruments because
      the Market Claim for cash amounts can not be partially settled);
    ▪  the same status on-hold / released of the original transaction whatever is
      the origin of the transaction (the market, CCP, OTC). Participants in the
      event of a change of the status of the original transaction are expected to
     change in the same way the status of the CLAI transaction.


CLAI Instructions relating to unsettled transactions intra-CSD are matched from
the time of generation.


5 For corporate action involving the payment of monetary amounts (called cash distribution), the countervalue of the Market
Claim is equal to the product of the quantity of shares / nominal value of the securities of the original transaction, multiplied by
the unitary value of the corporate action (gross dividend amount per unit; interest rate).

For transactions involving the allocation of financial instruments (called securities distribution) the amount of shares / nominal
value of financial instruments of CLAI instruction is equal to the amount of shares / nominal value of the original transaction,
multiplied by the number of financial instruments distributed, according to the ratio established by the issuer.




16



[PDF page 21]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





CLAI Instructions concerning transactions to be settled cross-CSD are forwarded
by Monte  Titoli to the T2S platform for the purposes of matching with the
settlement instruction generated by the CSD of the counterparty of the Monte
Titoli Participant.

CLAI Instructions related to OTC transactions can be deleted by Participants
according to the with the rules and the general conditions applicable to OTC
settlement  instructions,  while those  relating  to guaranteed  transactions  or
Market transactions are canceled by Monte Titoli according to the Markets or the
Central Counterparties request.

Central Counterparties can be counterpart in withdrawal or delivery of Market
Claim.

    •  Market Claim Settlement


The Market Claim for payment of amounts in cash can not be partially settled.

The Market Claim on financial instruments can be partially settled.

Settlement of CLAI instructions can not be connected to other CLAI instructions
(linkages).

CLAI instructions can not be included in a pool".


    •  Market Claim in connection with corporate events with Antedated Record
      Date


If during the period of identification of pending transactions the system detects:

   a) details of a new corporate event whose Record Date coincides with a date
       earlier than the current; or
   b) the change of the Record Date of a corporate event already known by the
      system, anticipated to the current date;

Monte Titoli automatically manages the Market Claim according to the state of
the underlying at the close of the accounting day coinciding with the new Record
Date.

Particularly in the case a), Monte Titoli detected the corporate event Record Date
in the past but within the detection period:

    ▪  For unmatched pending transactions at the Record Date (in the past)
      generates the Market Claim only  if the matching occurs subsequently to





17



[PDF page 22]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





      the Record Date and until the Accountig Date of the corporate action
      detection;
    ▪   for all operations settled at the Record Date (in the past), but traded from
      the Ex Date, Monte Titoli generates the Reverse Market Claim.

In the case b) Monte Titoli manages the Market Claim according to general rules,
provided that the backdating of the Record Date is within the detection period.

All other cases of modification of the Record Date:

    ▪   will be managed by manually according to what  is communicated via
     messaging service or equivalent;
    ▪    it is up to the Participants to act on the Market Claim already generated.

    •  Reporting to Monte Titoli Participants

Reporting related to the process of managing Market Claims, is made available
via the X-TRM for Participants ICP.

DCP Participants will receive the information produced by the T2S platform, as it
is provided  for information  relative to  all other transactions settled by the
Settlement Service.


For Participants that use RNI messaging, Monte Titoli will send the notification
message 7B2 of the generation of CLAI instruction (message type forecast).



1.4.2 Transformation

Monte  Titoli manages the process  of creating Transformations  of corporate
mandatory transactions (mandatory reorganization with or without options) or
voluntary (limited to the only or last period of the year and for which applies the
default option), such as:

    ▪  Total or partial reimbursement of the securities;
    ▪  exercise option right (as part of a capital increase for a fee, free or
      mixed);
    ▪  exercise of warrants (single or last exercise period);
    ▪  compulsory and optional conversion (last conversion period)
    ▪  groupings, splits, mergers and demergers.

Monte Titoli does not automatically manage the cancellation and Transformation
for the voluntary corporate event (voluntary reorganization).





18



[PDF page 23]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





The Transformation are generated by transactions matched but not settled
before the Record Date (cd. Operations pending).

Monte Titoli proceeds to identify settlement instructions potentially subject to
Transformation, from the Record Date of the current corporate action until the
20th Business Day after the record date (RD+20).

▪  Timing of identification process

Monte Titoli proceeds to identify settlement instructions potentially subject to
Transformation, from the Record Date of the current corporate action until the
20th Business Day after the record date (RD+20).


The identification process is repeated daily in batch mode at the same time, for
the entire duration of the identification period (detection period), in order to
verify any change in the status (from "unmatched" to "matched") of transactions
involving that were still not matched at the Record Date.


▪  Generation  of  the  Settlement  Instructions  for  the management  of  the
   Transformation

The process  of managing Transformations  involves the  cancellation  of the
Settlement Instruction related to the original transaction and the enter of a new
Settlement Instruction (TRAN).

Unmatched pending transactions at the Record Date generate Transformation at
the close of the accounting day on which they are matched if this occurs within
the detection period.

In the case of mandatory corporate events that do not provide the exercise of
options in favor of persons entitled to participate, Monte  Titoli automatically
deletes the  original settlement instructions transaction  in  fail and enter the
Instruction TRAN.

In the case of mandatory corporate events that allow the exercise of an option to
the parties entitled to participate,  it is up to the counterparties of the original
transaction in  fail to delete  it and enter a settlement instruction which terms
must reflect the Buyer Protection. For the management of Buyer Protection it has
to make reference to the market practice for OTC transactions, and to the rules
of the Markets and of the CCPs respectively for unguaranteed and guaranteed
market transactions.

In the absence, Monte Titoli at the Market Deadline performs the process of
Transformation according to the default option provided by the Issuer.




19



[PDF page 24]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In the case of voluntary corporate actions, it is up to the original counterparties
in fail to delete and reinsert the settlement instruction. In the absence Monte
Titoli does not perform the process of Transformation.

TRAN instruction must include at least the following information:

    ▪  Reference to the counterparty of the pending transaction that generates
      the Transformation;
    ▪  The  identification  of  the  pending  transaction  that  generate  to  the
      Transformation
    ▪  The identification of the corporate action in progress
    ▪  The Trade Date, coinciding with the Trade Date of the pending transaction;
    ▪  The Settlement Date, that is the higher between the Intended Settlement
      Date of the pending transaction and the date of execution of the corporate
      event;
    ▪  the ISIN code of the new instruction is the same of the security distributed
      from the corporate event, according to the report established by the
      Issuer;
    ▪  indicator on-hold / release and partialisation equal to those of the pending
      operation.

In the event that the corporate event provides the recognition  of multiple
securities, for each security will be created an instruction TRAN. In this case  if
the original transaction was DVP, the value of the transaction will be split a
number of new DVP instructions corresponding to the number of the TRAN
operations arising from the Transformation. The value of each DVP  transaction
will be proportional to the amount / nominal value of the financial instruments
referred to each TRAN instruction.

In the event of option rights resulting from capital increases, on the Market
Deadline Monte Titoli shall cancel the original settlement instruction and shall
enter a PFOD instruction in which the participant, previously in delivery of the
right, recognizes to the counterpart an amount equal to the countervalue of the
cancelled transaction.

In the event that the corporate event provides only the recognition of a cash
amount (e.g. total reimbursement), the pending transaction it is cancelled and
replaced by two TRAN instructions, one for the countervalue of the pending
transaction and one  for the value  for the reimbursement  of the  financial
instrument  (for the possible recognition  of the coupon please  refer to the
procedure of the management of the Market Claim).

TRAN  Instructions  generated  against  unsettled  transactions  intra-CSD  are
matched from the time of generation.





20



[PDF page 25]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





TRAN Instructions generated against transactions to be settled cross-CSD are
forwarded by Monte Titoli to the T2S platform for the purposes of matching with
the settlement instruction generated by the CSD of the counterparty of the
Monte Titoli Participant.

TRAN  Instructions related to OTC transactions can be deleted by Participants
according to the  rules and the general conditions applicable to other OTC
settlement  instructions,  while those  relating  to guaranteed  transactions  or
Market transactions are canceled by Monte Titoli according to the Markets or the
Central Counterparties request.

TRAN instructions can not be connected to each other, or be part of a pool.

TRAN instructions can bear the information that the original operation was linked
to other instructions, but it does not bear the ID of the linked one.

▪  Reporting to Monte Ttitoli Participants

The reporting relating to the management of Transformation is avaible trough X-
TRM Service for the ICP Participants.

DCP Participants will receive the information produced by the T2S platform, as it
is provided for all the others transactions settled by the Settlement Service

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
