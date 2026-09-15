# Coverage and gap register — Settlement Expert Agent (14 September 2026)

This register reuses the library's authorities: admissions live in `retrieval/section-decisions.json` and `retrieval/source-register.json`; the section index is `retrieval/README.md`; audit dependencies are `audits/2026-09-13/MISSING-SOURCES.md` (G01–G17). "Supported" means a bounded, cited answer is possible; "Partial" means the concept is supported but production detail is not; "Blocked" means the retriever returns a controlled block.

## 1. Question-to-source matrix

| Topic (agent scope) | Milan | T2S | Copenhagen | Porto | Athens | Oslo | EU law |
|---|---|---|---|---|---|---|---|
| Participants, categories, access | Supported (Regs 58–61; Instructions §1.1–1.2; ON_12) | — | Supported (Part 2 §2.1–2.2, publication description; Part 5 DCP) | Supported for DCP relationship (Reg 1/2016 Art 2) | Reference (Res 2 staffing) | Reference (VPO NOK §§9–10 liquidity, edition reservation) | Supported (CSDR Arts 33, 35) |
| Accounts, cash, static data | Supported (Regs 58(4)–(5), 60, 62; Instructions §1.2; Party 2 rule) | — | Partial (Part 4 §11.4–11.5) | Partial (manual §12 channels; DCA link chapter not admitted) | Reference (Res 5 Part 1 cash agents) | Reference (§22 settlement banks) | Supported (CSDR Art 40) |
| Issuer / investor CSD roles | Supported (Regs Art 77) | Supported (realignment concept) | — | Supported (manual Ch. 15) | — | — | Supported (RTS 2017/392 Art 1(e)-(f), reference) |
| Domestic and cross-CSD settlement | Supported (Instructions §1.3, Title 2; Gateway index) | Supported (realignment, posting, messages for the ICP/EUR/direct assumption) | Supported (Part 4 §2.3, §11) | Supported (Ch. 15, 16) | Reference (Res 5 Part 3) | Reference (VPO NOK outside T2S) | — |
| Validation and matching | Supported (Regs 68–69; X-TRM Table 2) | Supported (§1.6.1.1–1.6.1.3, diagrams 55–57) | Supported (§11.6–11.7) | Supported (field table, tolerance) | Reference (Res 5 §4.3) | Reference (§23.1) | Supported (RTS 2018/1229 Arts 5–6) |
| Settlement, realignment, partial, links, CoSD | Supported (Regs 73–76) | Supported (§1.6.1.8–1.6.1.12) | Supported (§11.8) | Supported (§12.5, 16.2) | — | Reference (§23.4–23.8) | Supported (RTS Arts 10) |
| Messages and statuses | Partial (X-TRM channels/codes; layouts client-only) | Partial (native families; sese.023 blocks; sese.024 usages; no XSD) | Partial (User Guidelines client-only) | Supported at reference level (STD/MT/ISO message references) | Blocked (DSS announcements) | Blocked (User Documentation) | Supported (RTS Art 11 information) |
| Deadlines and calendars | Partial (T2S baseline; ON_13 1 May; penalties calendar); participant cut-offs blocked (G01) | Supported (baseline; five windows; dated overlays for 17 dates and routine-only list from 14 June 2026) | Partial (day boundaries 18:00/18:45) | Reference (working-days page; Notice 394/2024; calendar 2026) | Blocked (cycles) | Blocked (calendar) | Supported (CSDR Art 5 ceiling; T+1 future) |
| Exceptions, cancellation, finality | Supported (Regs 69–72; Instructions §1.6, Title 4) | Supported (§1.6.1.4–1.6.1.7) | Supported (§§4–6.2, 11.7–11.8) | Supported (§12.2–12.4) | Reference (Res 5 §4.3 acceptance) | Reference (§§23.1–23.3) | Supported (CSDR 39; SFD 3, 5; RTS 7–8) |
| Participation / legal requirements | Supported (Regs 59–61, 64) | — | Supported (Part 2) | Partial | Reference | Reference | Supported (CSDR 33, 39, 40; DORA scope) |
| Release status and future changes | Supported (ON_20 deployment; ON_28/10 Aug plan; ON_30 SWIFT SR2026; MN_07 go-live) | Supported (final publication; June-vs-November comparison) | — | — | — | — | Supported (T+1 law; RTS stages) |

## 2. Status of the audit dependencies after this snapshot

| Gap | Status on 14 September 2026 | What was found | Still missing (exact) | Route |
|---|---|---|---|---|
| G01 Milan participant timetable | Narrowed, open | Regs Art 66(1)(f) delegates calendar/hours to notices and Art 67(2) to the T2S URD; ON_20/2026 confirms R2026.JUN production; hub keyword searches show no post-June timetable notice | A Milan notice or Instructions amendment restating participant cut-offs after 15 June 2026 | Operational notices hub; MT-X |
| G02 Dated ECB events | Extended | 17 non-routine business dates and 158 routine-only dates admitted from the 14 September capture (currency-neutral); since revision v1.1 reachable on their own through `t2s_status_history` for any reviewed date, including dates before 14 June 2026 | The nominal timetable for dates before 14 June 2026 (R2025.NOV baseline not reviewed); dates after 14 September 2026 | ECB status history |
| G03 X-TRM standards | Identified, client-only | Titles/versions: ES-MIL-A2A/RNI X-TRM Standard VER.01.09 (final June 2026, MT-X); ON_36 update planned 30 November | The standards' content | MT-X Docs > Live services > Technical documentation |
| G04 ISIN/link eligibility | Open (transaction-dependent) | Gateway link index (1 May 2026); Regs Art 65, 77 | MT23 list per ISIN; account/link static data | MT-X Lists > MT23 |
| G05 Matching diagrams | Closed (functional) | — | Production schema (G14) | — |
| G06 DORA chain | Unchanged | — | RTS/ITS and national reporting chain | ESMA/EBA/NCA |
| G07 Oslo edition approval | Open | Finanstilsynet page confirms system approval only | Edition approval or unconditional successor | Finanstilsynet |
| G08 Athens approval chain | Open | HCMC route unreachable (TLS error) | HCMC decision 1/1074, Gazette B 6784 | HCMC / et.gr |
| G09 Porto calendar/timetable | Extended | Working-days page table with WET note admitted | Portuguese originals; day-specific exceptions | MyInterbolsa notices |
| G10 Copenhagen DCP guide | Open | Hub links only Parts 1–6 | DCP User Guidelines, test acceptance | VP documentation service |
| G11 Oslo user documentation | Open | VPO NOK §§21–23 admitted | User Documentation, calendar | MyVPS |
| G12 Athens DSS technical set | Open | Res 5 §2.2 delegation admitted | DSS technical announcements | DSS |
| G13 Porto layouts | Extended | Manual field table and notes admitted | STD Manual Appendix A1; ISO 15022 conditional blocks | Porto documentation |
| G14 MyStandards usage/XSD | Open | Links redirect to authentication | R2026.JUN/NOV usage guidelines and XSDs | MyStandards account |
| G15 R2026.NOV deployment | Partially closed | Final publication (14 Sept); Milan plan 14/16 November; text comparison | Deployment confirmation (November); change-request review | ECB status history |
| G16 CMVM 5/2018 | Open | cmvm.pt route 404 | Consolidated regulation text | CMVM |
| G17 CLIMP/fees/tax | Open | ON_04 payment fields; penalties calendar | Fee rows; CLIMP guide; tax procedures | MT-X / pricing documents |
| New: RTS 2017/392 capture language | Recorded | Consolidated EN page serves German; English Article 1 excerpt captured | Full English consolidated text | EUR-Lex (browser) |

## 3. Prioritised missing-source list (for the user)

1. Milan participant timetable authority after R2026.JUN (G01) — highest impact on "when must I send" questions.
2. Standard for X-TRM Users A2A/RNI VER.01.09 (G03) — needed for any technical specification of the ICP interface.
3. MyStandards R2026.JUN usage guidelines and XSDs (G14) — needed for field-level T2S message specifications.
4. MT23/static-data extract for the relevant ISINs and links (G04) — needed for any real cross-CSD flow.
5. R2026.NOV deployment confirmation and change-request review (G15) — before any November-effective specification.
6. Copenhagen DCP User Guidelines (G10); Porto STD Appendix A1 (G13); Athens DSS technical announcements (G12); Oslo User Documentation (G11).
7. Oslo edition approval (G07) and Athens HCMC/Gazette chain (G08) for unconditional legal statements.
8. CMVM Regulation 5/2018 as amended (G16); DORA reporting chain (G06); fee rows and tax procedures (G17).

Client-specific documents (account structures, entitlements, test acceptance, SSIs) are required whenever a question concerns a particular firm's configuration; the agent states this instead of inferring.
