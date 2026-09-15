# Porto "17:00" vs T2S "18:00" FOP cut-off — which is right?

## Direct answer

Both figures are right, and they are almost certainly **the same moment on two different clocks**: T2S publishes **18:00 CET** as the FOP (free-of-payment) cut-off, while Interbolsa's Portuguese timetable notice prints **17h00m**, i.e. Portuguese local time, which the Porto operating-hours page states is "-1 hour than CET". There is no substantive conflict in the reviewed evidence.

Two corrections to the premise, both material:

1. **The reviewed Operational Manual does not state a FOP cut-off at all.** The retrieved Operational Manual excerpt (Chapter 12 / §12.1) contains no cut-off times; it expressly defers the schedule to "Chapter 4 – 'Schedule and Timetables'", which is **not in the reviewed evidence**. In this bundle, 17h00m comes from Interbolsa Notice 394/2024, not from the Manual.
2. **17h00m is not labelled "FOP cut-off" in the Porto source.** Notice 394/2024 calls it "Closing: 17h00m (end of day)". On the CET clock, 18:00 is simultaneously the FOP cut-off and the start of the T2S End of Day period — so the labels coincide in effect but are not identical wordings.

*Terms used below:* **FOP (free of payment)** — a securities delivery with no cash leg; **DVP (delivery versus payment)** — securities against cash; **cut-off** — the platform deadline after which instructions are no longer processed for same-day settlement in that category.

## Retrieval statuses

All five retrievals in the bundle returned **`evidence_only`**. No retrieval returned `blocked`, `needs_context` or `needs_refresh`, so nothing in this answer is suppressed by a status. Every claim below is nevertheless bounded by the LIMITATION lines carried by its section.

## What the evidence says

### 1. The T2S side: 18:00 CET

**Documented requirement.** T2S's real-time settlement closure runs from "start of cut-off phase with DVP cut-off at 16:00 hrs CET and end of cut-off phase at 18:00 hrs CET with FOP cut-off" [[t2s-schedule-r2]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.4.2 and exception conditions, PDF 156–158, version R2026.JUN; reviewed 14 September 2026 (source reviewed 13 September 2026); body language English, no authoritative language designated; source identity checked, no independent whole-edition supervisory approval certification. The same section's Table 37 shows End of day (EOD) as the period **18:00 – 18:45**, with Start of day 18:45 – 20:00 and night-time settlement 20:00 – 3:00 [[t2s-schedule-r2]] UDFS R2026.JUN, Table 37, PDF 160–163; same version, review dates and qualifications.

**Documented requirement.** The UDFS distinguishes cut-offs the T2S Operator may move for a settlement currency (DVP cut-off "remains harmonised for all currencies at 16h00", cash settlement restriction cut-off, BATM, CBO, cash sweeps, inbound liquidity transfer cut-off) from the case where, if T2S extends the EOD cut-off because of a general issue across all currencies, "T2S ensures the sequence of currency independent cut-offs (securities Settlement Restriction cut-off and FOP cut-off) is not changed" [[t2s-schedule-r2]] UDFS R2026.JUN, §1.4.2, PDF 157–158; same qualifications. Note this protects the **sequence**, not a guarantee of the clock time.

**LIMITATIONs that travel with these claims** [[t2s-schedule-r2]]: CET is the source convention and no UTC conversion was made; the nominal schedule "is not guaranteed execution or a local participant cut-off"; a dated query requires a reviewed event overlay for the same review date; the section is the 14 September re-verification of the same pages as the 13 September section, with source bytes re-fetched and hash-identical.

**Documented requirement (context).** The real-time settlement period contains five partial settlement windows: 08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15, and a fifth "between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first)" [[t2s-rts-phase]] UDFS R2026.JUN, §1.4.4.4, PDF 193–194, version R2026.JUN; reviewed 14 September 2026 (source reviewed 13 September 2026); English, no authoritative language designated; LIMITATION: these are the R2026.JUN baseline values, some cut-offs are currency dependent, and a supplied business date requires a reviewed event overlay.

### 2. The Porto side: 18:00 on the CET table, 17h00m on the local-clock notice

**Documented requirement.** Euronext Securities Porto's published operating-hours table, expressed in **CET**, lists: DVP cut-off 16:00, collateral reimbursement 16:30, BATM / CBO cut-off 17:40, inbound LTO cut-off / automatic cash sweep 17:45, **FOP (Free of Payment) cut-off 18:00**, End of Day – EoD 18:00, real-time settlement 05:00 – 18:00, partial settlement cycles 08:00–08:30, 10:00–10:15, 12:00–12:15, 14:00–14:15 and 15:30–16:00. The page carries the note: "Portugal uses WET (Western European Time), which is -1 hour than CET" [[porto-operating-hours-web]] Euronext Securities Porto — Working Days & Operating hours, operating-hours section, web page capture of 14 September 2026; reviewed 14 September 2026; basis: reference description; English, no authoritative language designated; source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONs: this is a web-page reproduction of the T2S schedule, **the binding source is Notice 0394/2024** and dated exceptions need event evidence; the page's 2025 closing-day list was visible at capture, while the 2026 calendar is Notice 25/1162 (section porto-calendar, **not in this bundle**).

**Documented requirement.** Interbolsa Notice 394/2024 states that the systems' operating timetable "is based on the operation hours adopted by the TARGET2-Securities (T2S) platform and also defined in the T2S rules", and gives: "a) Opening: 17h45m the previous working day (start of day); b) Closing: 17h00m (end of day) being 15h00m for instructions with financial component"; the night-time settlement period "starts at 19h00m", followed by a daytime period running "until 17h00m"; partial settlement occurs in the last night-time cycle and between 07h00m–07h30m, 09h00m–09h15m, 11h00m–11h15m, 13h00m–13h15m and 14h30m–15h00m; mandatory maintenance runs 01h30m Saturday to 01h30m Monday and optional maintenance 2h00m–4h00m [[porto-timetable]] porto-timetable-notice, Interbolsa Notice 394/2024 §§1–15, effective 17 April 2024; reviewed 13 September 2026; body language English, **authoritative language Portuguese**. LIMITATIONs: the English translation is expressly **not legally binding** ("In case of legal matters the original documents written in Portuguese ... should be consulted"); source clock values must be preserved, and conversion and dated exceptions are **not certified**.

### 3. What the Operational Manual actually contains

**Documented requirement.** The retrieved Operational Manual text on the real-time settlement system states only that "The operating schedule of the systems and respective timetables are available in Chapter 4 – 'Schedule and Timetables'", and otherwise describes instruction types (DVP, FOP, DWP, PFoD; DFP/RFP for FOP), channels (STD SLRTfile/SLRTmsg, ISO 15022 MT530/540/541/542/543, ISO 20022 for DCPs), references (IB Reference, T2S Reference, Matching Reference), SF1 acceptance and SF2 matching. It records that "FOP (Free of Payment) operations are allowed by entering a zero cash amount in the 'Financial Amount to be settled' field and ' ' (blank) in the 'Currency' field" [[porto-rts-registration]] Operational Manual of INTERBOLSA, Chapter 12 opening and §12.1, PDF 116–120 (printed 115–119), version "Operational Manual V43, internal date 26 January 2026; filename 16 February 2026; posted April 2026"; reviewed 14 September 2026 (source reviewed 13 September 2026); body language English, **authoritative language Portuguese**. LIMITATIONs: this is the English version, the **Portuguese text governs**, the manual's operative effective date is unresolved, and matching-tolerance values are on the website rather than in the excerpt.

**Unresolved requirement.** Chapter 4 of the Operational Manual — the chapter the premise attributes the 17:00 figure to — was **not retrieved**, and the topic index offers no route to it. Whether Chapter 4 prints 17:00, on which clock, and with which label, is not in reviewed evidence.

## Why the two numbers are the same moment (reasoned inference)

**Reasoned inference**, derived from (a) the WET note on the Porto operating-hours page [[porto-operating-hours-web]] and (b) a value-by-value comparison of Notice 394/2024 [[porto-timetable]] against the CET table [[porto-operating-hours-web]] and the UDFS baseline [[t2s-schedule-r2]], [[t2s-rts-phase]]: every timetable value in the Notice sits exactly one hour behind the corresponding CET value, which is what a WET-clock rendering of the same T2S schedule produces.

| Interbolsa Notice 394/2024 (source clock) | Porto CET table / T2S UDFS baseline |
|---|---|
| Opening 17h45m previous working day (start of day) | SOD, change of business date 18:45 |
| Night-time settlement starts 19h00m | Start of NTS 20:00 |
| Daytime settlement runs until 17h00m; "Closing: 17h00m (end of day)" | Real-time settlement 05:00 – 18:00; **FOP cut-off 18:00**; EoD 18:00 |
| "being 15h00m for instructions with financial component" | DVP cut-off 16:00 |
| Partial settlement 07h00m–07h30m | Cycle 1, 08:00–08:30 |
| 09h00m–09h15m | Cycle 2, 10:00–10:15 |
| 11h00m–11h15m | Cycle 3, 12:00–12:15 |
| 13h00m–13h15m | Cycle 4, 14:00–14:15 |
| 14h30m–15h00m | Cycle 5, 15:30–16:00 (page) / 15:30–16:05 or closure of both DVP cut-offs, whichever is first (UDFS) |
| Mandatory maintenance 01h30m Sat – 01h30m Mon | 02:30 – 02:30 |
| Optional maintenance 2h00m–4h00m | 03:00 – 05:00 |

Eleven independent pairs align on a one-hour offset, so the reading "Porto closes an hour earlier than T2S" is not supported: the Notice is describing the same T2S day on the Portuguese clock. The Notice itself says its timetable is based on the T2S operating hours [[porto-timetable]].

**Qualifications on that inference.** The Notice does **not** state its own clock convention; the WET statement is on the web page, whose LIMITATION says the page is a reproduction and the binding source is the Notice [[porto-operating-hours-web]]. The Notice's own LIMITATION requires source clock values to be preserved and says conversion is not certified [[porto-timetable]]. So: treat 17h00m and 18:00 CET as the same event on the evidence available, but quote each source in its own clock rather than rewriting the Notice's figures, and take the governing Portuguese text of the Notice for any legal purpose.

**Reasoned inference (label mismatch).** In the Notice the value is "end of day"/closing; in the CET table 18:00 is both the FOP cut-off and the EoD marker, and in the UDFS 18:00 CET is the end of the cut-off phase with the FOP cut-off, with the EOD **period** running 18:00 – 18:45 [[t2s-schedule-r2]]. A Porto participant reading "closing 17h00m" is reading the local rendering of that same boundary, not a separate Portuguese deadline. The Notice does not print a line labelled "FOP cut-off".

**Documented divergence worth noting.** For the fifth partial window the Porto page shows 15:30 – 16:00 [[porto-operating-hours-web]] while the UDFS shows "between 15:30 and 16:05 or the closure of both DVP cut-offs (whichever comes first)" [[t2s-rts-phase]]. The page is a reproduction; the UDFS is the platform specification for R2026.JUN. This does not affect the FOP answer.

## Scope limits you should not skip

- **Nominal, not an appointment.** Both 18:00 CET and 17h00m are nominal schedule values. The UDFS LIMITATION states that the nominal schedule is not guaranteed execution and not a local participant cut-off [[t2s-schedule-r2]]; the T2S Operator manages planned, revised and effective times per event, and may move certain currency-dependent cut-offs for a settlement day [[t2s-schedule-r2]] §1.4.2, PDF 156–157. For any **actual business date** a reviewed event overlay for the same review date is required, and none was retrieved here.
- **Review dates are facts.** The T2S sections and the Porto operating-hours capture were reviewed 14 September 2026 (T2S source bytes reviewed 13 September 2026); the Interbolsa Notice section and the Operational Manual source were reviewed 13 September 2026. Nothing here becomes "current today" by the passage of time.
- **Governing language.** For both Porto sources the **Portuguese text governs**; the Notice's English translation is expressly not legally binding [[porto-timetable]], and the English Operational Manual V43 is a translation whose operative effective date is unresolved [[porto-rts-registration]]. The UDFS body language is English with no authoritative language designated and no independent whole-edition supervisory approval certification [[t2s-schedule-r2]], [[t2s-rts-phase]].
- **Release identity.** The T2S values are the **R2026.JUN** platform baseline [[t2s-schedule-r2]], [[t2s-rts-phase]]. No other release is evidenced in this bundle.
- **Not a local participant deadline.** Whether Porto imposes an earlier local deadline for ICPs (indirectly connected participants) sending instructions through its own systems ahead of the T2S FOP cut-off is **not in reviewed evidence**; the retrieved Manual section points to Chapter 4 for schedules [[porto-rts-registration]].

## Open items

1. **Operational Manual Chapter 4, "Schedule and Timetables"** (Operational Manual of INTERBOLSA V43, Portuguese governing version) — needed to verify the premise that the Manual prints a 17:00 FOP cut-off, and in which clock. Not retrieved; the topic index lists no route to this chapter for Porto. Route: Euronext Securities Porto public documentation service (Documentation / Operational Documentation).
2. **Portuguese original of Interbolsa Notice 394/2024** — the English text in evidence is expressly non-binding; the governing figures and any clock statement must be read in Portuguese. Route: Interbolsa/Euronext Securities Porto public notices.
3. **Explicit clock convention for the Notice** — no reviewed source states that Notice 394/2024 is written in WET; the WET statement sits on the web page, whose own LIMITATION makes the Notice the binding source. Needed before converting the Notice's values in any specification.
4. **Dated event overlay** for any specific business date, for both T2S (revised/effective times, currency-dependent cut-off extensions) and Porto (published exceptions). Not retrieved for any date here; the 2026 Porto closing-day calendar is Notice 25/1162 (section porto-calendar), which is not in this bundle.
5. **Porto local (ICP) submission deadlines** ahead of the T2S FOP cut-off, if any — not in reviewed evidence. Route: Porto Operational Manual Chapter 4 and the STD/technical manuals available on the client platform.

No section in the bundle contained instruction-like content directed at the answering system.
