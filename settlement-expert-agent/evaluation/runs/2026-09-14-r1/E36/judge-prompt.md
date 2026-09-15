You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Could a Monte Titoli participant settle a FOP instruction on 1 May 2026, and a DvP in EUR on that day?

# Case category: dated-calendar (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "ON_13/2026: T2S open for FOP but not DVP/PFOD in EUR on 1 May 2026; T2 closed; X-TRM limited; EUR payments deferred.",
  "Notice-based evidence, not the Regulations."
]
Fail conditions (must NOT appear):
[
  "Say EUR DvP settled on 1 May."
]
Expected sections (if any): ['milan-may1-2026']
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
# 1 May 2026 at Euronext Securities Milan: FOP yes (with conditions), EUR DvP no

## Direct answer

**FOP: yes, but only for some instruction populations.** 1 May 2026 was announced as a business day on which T2S was **open for FOP** ("free of payment" — a securities transfer with no cash leg) and all CSD participants in T2S, including ES-MIL, were open; free instructions already in T2S were to attempt settlement and free instructions could be entered, matched and settled with any intended settlement date. **EUR DvP: no.** T2S was announced as **not open for DVP and PFOD operations in EURO**, T2 was closed, no EUR payments could be made, and "APMT" (against-payment) instructions were to be blocked or rejected by the T2S platform; an against-payment instruction with an intended settlement date of 1 May 2026 would be rejected outright [[milan-may1-2026]] ON_13/2026 "May 1st as a business day: impact on ES-MIL systems", 24 April 2026, PDF 1 and PDF 4–5; reviewed 14 September 2026; English notice, **Italian is the authoritative language**.

## Retrieval status and what the evidence is

One retrieval was made — Milan, settlement service, participant role, current mode, question type `milan_calendar_exception`, with the two required scope elements supplied (business date 2026-05-01, payment type FOP) — and it returned **evidence_only**. No `blocked`, `needs_context` or `needs_refresh` status applies. The whole answer rests on one section, reviewed **14 September 2026**.

Qualifications that stay attached to every claim below:
- The source is **ON_13/2026, an operational/market notice** issued by Euronext Securities Milan on 24 April 2026, in English, with **Italian as the authoritative language** (translation; authoritative language differs). It is **not the Service Regulations and not the Instructions**, and it carries a **PRIVATE** footer on every page despite being published. Source identity was checked; there is no independent whole-edition supervisory approval certification.
- The notice **applies to 1 May 2026 only**. Nothing in it describes any other calendar exception.
- The impact tables are reproduced from a **layout-heavy PDF**; row alignment should be verified against the original before relying on any single cell.
- **It is a notice published in advance (24 April 2026), i.e. an announced arrangement, not a record of the day.** The reviewed evidence does not confirm what actually happened on 1 May 2026 and contains no post-event or incident report. "Could a participant settle" is answered here as "what the published arrangement provided for".

## FOP on 1 May 2026 — Documented requirement, by population

The notice sets out the headline platform position and then splits settlement by instruction population [[milan-may1-2026]] ON_13/2026, PDF 1, 4–6; reviewed 14 September 2026; English notice, Italian authoritative:

**Platform level (PDF 1):** "T2S: open for FOP, but not for DVP and PFOD operations in EURO"; "T2: closed"; "All CSD participants in T2S (including ES-MIL): open".

**Settlement impact, T2S–X-TRM (PDF 4):** the T2S platform was available and therefore the X-TRM service was operational "with some limitations due to the impossibility of settling the cash part"; "only and exclusively Intra and Cross-CSD instructions can be settled, while 'APMT' instructions will be blocked/rejected by the T2S platform". Reports concerning penalties were still to be sent (PDF 1).

| Population | FOP on 1 May 2026 (as announced) | Locator |
|---|---|---|
| **OTC, intra-CSD and cross-CSD** | Yes. "FREE" instructions already in T2S attempt settlement; "FREE" instructions can be entered/reset/settled **with any ISD**. | PDF 5 |
| **Non-guaranteed market operations** | No new flow and no settlement attempt: any transaction with a Trade Date of 1/5/2026 is **rejected by X-TRM**, and unsettled transactions from previous days **will not attempt settlement on 1/5/2026**. | PDF 5 |
| **Guaranteed market operations** | Same as above: Trade Date 1/5/2026 rejected by X-TRM; unsettled transactions from previous days do not attempt settlement on 1/5/2026. | PDF 5 |
| **External CSD — markets** | All markets connected to X-TRM closed; trades with a Trade Date of 1/5/2026 rejected by X-TRM. Trades (EuroTLX and EuroMOT) received on previous days with the stated ISD were to be sent to the relevant ICSDs on the trade day. | PDF 6 |
| **External CSD — OTC** | Pending "FREE" instructions with an ISD before 1/5/2026 attempt settlement; "FREE" instructions can be entered/matched/settled **with any ISD**. | PDF 6 |

So the correct FOP answer is population-dependent: an **OTC free-of-payment instruction** (intra-CSD, cross-CSD or towards an external CSD) could be entered, matched and settled; a **market-sourced instruction routed through X-TRM**, guaranteed or not, could not — it was either rejected at entry (Trade Date 1/5/2026) or simply not presented for settlement that day.

**Validity-date counting.** For transactions received on previous days with an ISD up to 26/04/2026, the determination of the end-of-validity date (ISD + n days) was **not** to take 1/5/2026 into account — for both non-guaranteed and guaranteed market operations (PDF 5). *Reasoned inference:* although the day was "treated as a business day" for system opening, it was excluded from that recycling count, so the day was not neutral for instruction lifecycle arithmetic. Derived from the two PDF 5 bullets read against the "business day" framing on PDF 1.

## DvP in EUR on 1 May 2026 — Documented requirement

No. The notice is explicit on three independent grounds [[milan-may1-2026]] ON_13/2026, PDF 1, 4, 5–6; reviewed 14 September 2026; English notice, Italian authoritative:

1. **T2S was not open for DVP and PFOD operations in EURO** (PDF 1); **T2 was closed** (PDF 1). PFOD — payment free of delivery — is a cash-only movement in the securities settlement system.
2. **"APMT" (against-payment) instructions were to be blocked/rejected by the T2S platform**, and only intra-CSD and cross-CSD instructions could be settled (PDF 4). X-TRM was operational only with limitations "due to the impossibility of settling the cash part" (PDF 4).
3. **Entry was barred for that ISD**: for OTC intra/cross-CSD, "It will NOT be possible to enter 'AMPT' instructions with an ISD of 1/5. Any instructions will be rejected by T2S"; against-payment instructions with an ISD **other than** 1/5 could be entered and matched, "but they will not attempt settlement" on the day (PDF 5). The same entry bar is repeated for external-CSD OTC, where any delivery or withdrawal instruction with an ISD of 1/5 would be rejected by T2S (PDF 6). ("AMPT" is printed that way in the source at these two points and "APMT" elsewhere; quoted as printed.)

**Cash consequences already pending (PDF 1–3, custody).** No payments in EUR could be made on 1 May; payments were to be postponed to the first subsequent working day (with deferred cash settlement shown against 04/05/2026 in the impact tables). Securities disposal or Pool Factor adjustment for REDM, PCAL and MCAL was to be performed at SOD in the scheduled NTS cycle following 1 May. Issuers were to be prevented from entering transactions with a payment date of 1 May (dividends/fund units, DVPIssaunce [printed as such], ACPG); RIFPA, REVPA and RIAPA paying-agent instructions on 1 May were to be prevented, with RIAPA instructions received the day before postponed to the next working day; reversals were not to be executed on 1 May. Securities-only reorganisations, issuance, mark-up and mark-down were to run regularly.

**Cross-border against-payment already pending (PDF 6).** For pending "APMT" instructions towards an external CSD, a delivery from the ES-MIL account could be settled with the foreign CSD but the securities would be released and debited on 2/5 together with the corresponding cash credit, and a receive to the ES-MIL account would be settled at the ICSD with securities credited on 2/5. *Reasoned inference:* this is the only against-payment outcome the notice allows around that date, and it is an external-CSD leg with a next-day ES-MIL booking, not settlement of a EUR DvP inside ES-MIL on 1 May. Derived from the PDF 6 OTC rows read against the PDF 4 statement that APMT instructions are blocked/rejected by T2S.

## Not in the reviewed evidence — Unresolved requirement

- **What actually happened on 1 May 2026.** The bundle contains the advance notice only. No dated event overlay, incident report or post-day confirmation was retrieved, so nothing here should be stated as an observed outcome; the day may also have carried deviations that this notice could not anticipate.
- **Non-EUR against-payment settlement.** The PDF 1 headline is currency-qualified ("DVP and PFOD operations in EURO"), while the PDF 4 settlement-impact row blocks "APMT" instructions without naming a currency. The reviewed evidence therefore does **not** resolve whether an against-payment instruction in a non-EUR T2S settlement currency could have settled on 1 May 2026. The question as asked (DvP **in EUR**) is not affected by this ambiguity.
- **Times of day.** The notice gives no cut-off, cycle time or deadline for 1 May 2026; only SOD/NTS/RTS phase labels appear. No clock time may be inferred, and Milan participant cut-offs are an unresolved gap in this library (gap id G01; `milan_participant_cutoff` is a blocked question type).
- **Instrument, link and account eligibility.** Whether a specific ISIN, CSD link or account could actually have been used for the FOP settlement described above is not established here (instrument eligibility is a blocked question type, gap id G04).
- **Message-level behaviour.** No message type, version, status code or rejection reason code for the X-TRM or T2S rejections above is in the reviewed evidence; "blocked/rejected" is the notice's own wording.
- **An internal source inconsistency.** The external-CSD markets row reads "Trades (EuroTLX and EuroMOT) received on previous days with ISD 1/5/2025 will be sent to the relevant ICSDs on the trade day" (PDF 6). The year printed there is inconsistent with the rest of the notice; it is reproduced, not corrected, and the Italian authoritative text would be needed to settle it.
- **Normative status.** This is a notice, not the Service Regulations or the Instructions; if a rule-level obligation is needed rather than an operational arrangement, the rulebook would have to be retrieved separately.

## Open items

1. **Italian authoritative text of ON_13/2026** — to confirm the settlement tables, the "APMT"/"AMPT" spellings, the ISD 1/5/2025 year and the row alignment of the layout-heavy impact tables; route: Euronext Securities Milan public notices page.
2. **Any follow-up or corrective notice for 1 May 2026**, and any post-event communication confirming that the day ran as announced; route: the same notices page / ES-MIL client communications.
3. **Milan Service Regulations and Instructions** if a normative (rule-level) rather than operational answer is required for calendar exceptions; route: Euronext Securities Milan public documentation hub.
4. **Non-EUR against-payment position** for the same date — evidence that reconciles the currency-qualified headline with the unqualified APMT block; not retrieved for this question.
5. **Client-specific confirmation** of which of your instructions were market-sourced (X-TRM, guaranteed or non-guaranteed) versus OTC, since the FOP answer differs between them; route: your own instruction records and ES-MIL client support through the official client channel.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.457266+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_calendar_exception", "payment_type": "FOP", "business_date": "2026-05-01"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-may1-2026]] — 1 May 2026 treated as a business day: T2S open for FOP only in EUR, T2 closed, X-TRM limitations and custody impacts (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: ON_13/2026 May 1st as a business day: impact on ES-MIL systems (24 April 2026) | ON_13/2026 PDF 1–6 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/ON_primo_maggio_eng_2026_0.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Applies to 1 May 2026 only; impact tables are reproduced from a layout-heavy PDF and should be read against the original for row alignment.
EXCERPT (ON_13/2026 PDF 1–6):
[PDF page 1]

24 April 2026
ON_13/2026


May 1st as a business day:
impact on ES-MIL systems
   To the attention of:                           All Clients and Account Operators


   Topic:                                         May 1st 2026 treated as a business day:
                                                  impact on ES-MIL systems


Dear Client,


Please take note that May 1st, 2026 will be treated                                   as a business day and will have
the following specific characteristics:

     •    T2S: open for FOP, but not for DVP and PFOD operations in EURO
     •    T2: closed
     •    All CSD participants in T2S (including ES-MIL): open

In particular, for Custody activities:
   • no payments in EURO may be made on May 1st; payments will be postponed
       and made on the first subsequent working day
   • securities disposal or Pool Factor adjustment for REDM, PCAL and MCAL will be
       performed at SOD in the scheduled NTS cycle following May 1st.

For Settlement activities:
   • the X-TRM service will be operational with some limitations due to the
      impossibility of settling the cash part.
   • Reports concerning penalties will be sent




This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprie tary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 6

                                                             PRIVATE



[PDF page 2]

          Impact on Custody
          The custody processes concerned are typically those that involve cash-related
          activities, including:
               •       Cash Distribution
               •       Payment of Government Bonds
               •       Payments management by the Paying Agent
               •       Late dividend collection
               •       RCC
               •       Reorganisation


          The following chart describes the expected impact on individual processes




                                              CASH              1/5/2026      1/5/2026
No.      PROCESS          SERVICE    CAEV   SECURITIES            NTS           RTS         04/05/2026               ACTION

1     payments made       Custody   INTR,   Cash/securities    securities   no payment     Deferred      Payments will be deferred until
      in central bank     ITA       REDM,                      accounting                  cash          the next business day
      money                         PCAL,                      or PF                       settlement    The deferral will also apply to
                                    PRED,                      amendment                                 securities with a “PREVIOUS
                                    MCAL                       download                                  GOOD BUSINESS DAY”
                                                                                                         convention.
                                                                                                         No impact is expected for
                                                                                                         securities with a MODIFIED
                                                                                                         FOLLOWING BUSINESS DAY
                                                                                                         convention.

2     payments made       Custody   INTR,   Cash/securities    securities   suspension     Deferred      After suspension, payments will
      in commercial       ITA       REDM,                      accounting   of payment     cash          be postponed until the next
      bank money          Custody   PCAL,                      or PF                       settlement    working day
                          EST       PRED,                      amendment
                                    MCAL                       download

3     Payment of          Custody   INTR,   Cash/securities    securities   no payment     Deferred      Payments will be postponed until
      Government          ITA       REDM                       accounting                  cash          the next working date.
      Bonds                                                    download                    settlement    in the event of partial or total
                                                                                                         redemption the securities
                                                                                                         accounting download will be
                                                                                                         performed on 1 May.

4     Payment of          Custody   DVCA,   Cash/securities    N.A.         no payment     N.A.          Issuers will be prevented from
      dividends/fund      ITA       CAPD,                                                                entering transactions with a
      units               Custody   etc.                                                                 payment date of 1 May
                          EST

5     Payments            Custody   DVCA    Cash               N.A.         No             Deferred      the sending of RIFPA, REVPA,
      management by       ITA                                               instructions   cash          RIAPA instructions on 1 May will
      the Paying                                                                           settlement    be prevented.
      Agent.                                                                                             For RIAPA instructions received
      RIFPA, REVPA,                                                                                      the day before 1 May, payments
      RIAPA                                                                                              will be postponed to the next
      (MSG7B4)                                                                                           working day.
      instructions




          | 2 of 6


                                                              PRIVATE



[PDF page 3]

                                                       CASH                 1/5/2026        1/5/2026
    No.        PROCESS          SERVICE     CAEV     SECURITIES               NTS             RTS            04/05/2026                  ACTION

    6       Late dividend      Custody     DVCA     Cash                N.A.              No payment        Deferred         Payments will be deferred until
            collection         ITA                                                                          cash             the first subsequent working date
                                                                                                            settlement       for collection instructions
                                                                                                                             received on the day before 1
                                                                                                                             May

    7       Reversal           Custody     INTR,    Cash                N.A.              No payment        N.A.             transactions will not be executed
                               ITA         REDM,                                                                             on 1 May
                               Custody     etc.
                               EST



                 Cash distribution: currency <> Eur:
                                                     CASH               1/5/2026          1/5/2026
N.           PROCESS           SERVICE     CAEV    SECURITIES             NTS               RTS            4/5/2026                   ACTION

8         payments            Custody     INTR,    cash/securities      securities        sending of         N.A.         No Action. Payment made outside
          executed in         ITA         REDM,                        accounting       final payment                                  ES-MIL
          commercial bank                 PCAL,                           or PF           messages
          money directly by               PRED,                        amendment
          the Paying Agent                MCAL                          download
          or its
          correspondent
          bank

9         payments            Custody     INTR,    cash/securities      securities           cash             N.A.         No Action. Regularly executed
          executed in         EST         REDM,                        accounting         settlement                                operations
          commercial bank                 PCAL,                           or PF
          money                           PRED,                        amendment
                                          MCAL,                         download
                                          DVCA,
                                          etc.




                 Reorganization: currency Eur:
                                                     CASH             1/5/2026          1/5/2026
N.           PROCESS          SERVICE      CAEV    SECURITIES           NTS               RTS             4/5/2026                    ACTION

10        ACPG                Custody     EXRI,    Cash              N.A.              No payment       Cash post        Issuers will be prevented from
          (accounting and     ITA         EXWA,                                                         settlement       entering transactions with a
          rolling)            Custody     DVOP,                                                                          payment date of 1 May In the case
          Warrant exercise    EST         etc,                                                                           of rolling transactions, unexecuted
          and dividend with                                                                                              instructions received on the
          option                                                                                                         business day before 1 May and
                                                                                                                         those received on 1 May will all be
                                                                                                                         settled on the next business day




                 | 3 of 6


                                                                      PRIVATE



[PDF page 4]

            Other processes:
            5
                                                CASH          1/5/2026      1/5/2026
N.       PROCESS         SERVICE    CAEV      SECURITIES        NTS           RTS        4/5/2026               ACTION

11    voluntary /        Custody   RHDI,      NO           Securities    Securities    Securities    No Action. Operations
      mandatory          ITA       CONV,                   settlement    settlement    settlement    performed regularly
      Reorganization     Custody   MRGR,
      (no cash)          EST       SPLF etc
                                   .

12    Issuance, MarkUp   Custody   N.A.       NO           Securities    Securities    Securities    No Action. Operations
      and MarkDown       ITA                               settlement    settlement    settlement    performed regularly

13    DVPIssaunce        Custody   N.A.       Cash          N.A.         No payment    Cash post     Issuers will be prevented from
                         ITA                                                           settlement    entering transactions with a
                                                                                                     payment date of 1 May


14    RCC                Custody   N.A.       Cash         N.A           No payment    Cash post     Payments will be postponed to
                         ITA                                                           settlement    the next working date.




     Settlement
     impact


              System                                                      Operation
     T2S – X-TRM                    ➢     The T2S platform will be available and therefore also the X-TRM service will be
                                          operational with some limitations due to the impossibility of settling the cash part
                                    ➢     only and exclusively Intra and Cross-CSD instructions can be settled, while “APMT”
                                          instructions will be blocked/rejected by the T2S platform




            | 4 of 6


                                                           PRIVATE



[PDF page 5]

   Intra and Cross CSD:
       TYPE OF
      OPERATION                                           Operation
NON-GUARANTEED       ➢    Any transactions with a “Trade Date” of 1/5/2026 will be rejected by X-TRM.
MARKET OPERATIONS    ➢    For transactions received on previous days and with ISD up to 26/04/2026, the
                          determination of the end-of- validity date (ISD + n days) will not take into account
                          of 1/5/2026
                     ➢    Unsettled transactions from previous days will not attempt settlement on 1/5/2026
GUARANTEED           ➢    Any transactions with a “Trade Date” of 1/5/2026 will be rejected by X-TRM.
MARKET OPERATIONS    ➢    For transactions received on previous days and with ISD up to 26/04/2026, the
                          determination of the end-of- validity date (ISD + n days) will not take into account
                          of 1/5/2026. Unsettled transactions from previous days will not attempt settlement
                          on 1/5/2026.
OTC                  ➢    “FREE” instructions already in T2S will attempt settlement, while “APMT”
                          instructions will remain blocked.
                     ➢    “FREE” instructions can be entered/reset/settled with any ISD.
                     ➢    It will be possible to enter/match “APMT” instructions with ISDs other than 1/5, but
                          they will not attempt settlement.
                     ➢    It will NOT be possible to enter “AMPT” instructions with an ISD of 1/5. Any
                          instructions will be rejected by T2S.




  | 5 of 6


                                          PRIVATE



[PDF page 6]

External CSD:
           System                                           Operation
  MARKETS                  ➢     All Markets connected to X-TRM will be closed, any trades with A ‘Trade
                                 Date’ of 1/5/2026 will be rejected by X-TRM.
                           ➢     Trades (EuroTLX and EuroMOT) received on previous days with ISD
                                 1/5/2025 will be sent to the relevant ICSDs on the trade day.


  OTC                      ➢     Pending “FREE” instructions with an ISD before 1/5/2026 will attempt
                                 settlement, while for pending “APMT” instructions:
                                      o Delivery from the ES-MIL account can be settled with the foreign
                                          CSD, but the securities will be released and debited on 2/5
                                          together with the corresponding cash credit;
                                      o Receive to the ES-MIL account will be settled at the ICSD and
                                          securities will be credited on 2/5
                           ➢     “FREE” instructions can be entered/matched/settled with any ISD.
                           ➢     It will NOT be possible to enter “AMPT” instructions with an ISD of 1/5.
                                 Any delivery or withdrawal instructions will be rejected by T2S.




For further information:

E: eam@euronext.com
MIL-clientsupport@euronext.com




| 6 of 6


                                            PRIVATE

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
