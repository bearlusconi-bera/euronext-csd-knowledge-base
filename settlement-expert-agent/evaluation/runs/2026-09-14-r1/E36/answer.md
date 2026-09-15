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
