# Cross-CSD settlement of ISIN FR0000120271 between Monte Titoli and the French CSD

## Direct answer

**I cannot confirm that this specific ISIN is eligible, and I cannot tell you the link that applies to it "today".** Per-ISIN eligibility is a controlled block in this library (GAP **G04**): current ISIN, CSD-link, account, currency and MT23 static-data evidence would be required, and none of it is in the reviewed evidence. What the reviewed evidence *does* give you is (i) the rule that makes cross-CSD settlement possible at Euronext Securities Milan, (ii) the published inventory of issuer-CSD / counterparty-CSD combinations that Milan's T2S Gateway guide covered as of 1 May 2026 — which includes both a **France issuer CSD (MT23 81346) ↔ counterparty in Italy** chapter and an **Italy issuer CSD ↔ counterparty in France (ESES FR – SICVFRPPXXX)** chapter — and (iii) the exact documented lookup you must perform yourself to resolve your ISIN: **MTX → Lists → MT23 List of Financial Instruments → Search ISIN**, then read the Issuer/Investor and Issuer Code columns.

## Retrieval statuses that are not `evidence_only` (disclosure)

| Retrieval | Context | Status |
|---|---|---|
| 1 | `question_type: instrument_eligibility`, entity Milan, mode current, `as_of` 2026-09-14 | **blocked** — "Current ISIN, CSD-link, account, currency and MT23/static-data evidence required." **GAP ID G04** |

Retrievals 2–7 (`milan_cross_csd_rule`, `milan_cross_csd_link_guide`, `milan_settlement_service_scope`, `milan_external_settlement`, `investor_csd_definition`, `issuer_investor_csd_definitions`) returned `evidence_only`.

**Routing note:** the case as prepared had been routed to `t2s_linked_instructions` — the T2S BEFO/AFTE/WITH instruction-linkage feature — which answers a different sense of the word "link". I rerouted once to the CSD-link and instrument-eligibility routes listed in the topic index, which is why `instrument_eligibility` now appears as an explicit block rather than as silence.

Review dates used: **14 September 2026** for `[[milan-cross-csd-disclosure]]`, `[[milan-gateway-links-guide]]`, `[[milan-service-scope]]`, `[[milan-external-settlement]]` and `[[rts392-issuer-investor-csd]]`; **13 September 2026** for `[[t2s-realignment]]` and `[[t2s-posting]]`.

## On the word "today"

*Reasoned inference, from the review dates and the source version dates themselves.* Nothing in this bundle is a live static-data feed. The link guide is titled "valid from 1st May 2026" and its LIMITATION states that the index "proves which issuer-CSD/counterparty combinations the guide covers on 1 May 2026, not per-ISIN eligibility". The library's most recent review of it is 14 September 2026. Neither of those is a statement about the configuration in force on the day you read this, and a review date does not become "current" because time has passed. Any answer about a named ISIN on a named business date needs the MT23 record for that ISIN on that date.

## On "Euroclear France"

*Unresolved requirement.* The admitted evidence never uses the name "Euroclear France". Milan's T2S Gateway guide names the French counterparty CSD as **"ESES FR – SICVFRPPXXX"** (`[[milan-gateway-links-guide]]`, table of contents, chapters 7 and 10). I am not entitled to assert from memory that "ESES FR / SICVFRPPXXX" is the entity you call Euroclear France; that identity mapping is not established in reviewed evidence. Everything below therefore speaks of "ESES FR" as the guide does, and you should confirm the entity identity against the counterparty's own SSI before instructing.

## What is documented

### 1. Cross-CSD settlement between a Milan participant and a participant in another T2S CSD is provided for

*Documented requirement.* `[[milan-cross-csd-disclosure]]` Regulations as of 26 January 2026, Articles 77–78 with footnote 8, PDF 54 (printed 53), version 26 January 2026; reviewed 14 September 2026 (source reviewed 13 September 2026); **English translation — the Italian text prevails** (cover, PDF 1); source identity checked, no independent whole-edition supervisory approval certification.

- Article 77(1): where instructions are to be settled between a Monte Titoli participant and "a participant in another CSD in T2S (cross CSD), T2S shall automatically carry out the movements between the securities accounts of the participants involved, of the Investor CSDs and of the Issuer CSD."
- Article 77(2): "Monte Titoli does not envisage the possibility of carrying out a cross CSD settlement on securities if the Issuer CSD is outside of T2S, unless both investor CSDs have in place a link with another CSD in T2S so that the realignment with the Issuer CSD outside T2S is not necessary."
- Article 78: on request, Monte Titoli makes settlement status and balance-changing events available in real time "through the direct link channel to T2S, or through the X-TRM Service".

**LIMITATION carried with this claim:** "Article 77(2) excludes cross-CSD settlement when the issuer CSD is outside T2S unless both investor CSDs hold a link avoiding realignment with it; **actual links per ISIN are not certified**."

### 2. The Settlement Service scope confirms the intra-CSD / cross-CSD split

*Documented requirement.* `[[milan-service-scope]]` Instructions to Settlement Service and related instrumental activities, in force as of 30 June 2025 (MN_10/2025), §1.3 opening, PDF 12 (printed 8); reviewed 14 September 2026; **English translation, Italian text prevails**; source identity checked, no independent whole-edition approval certification. The Settlement Service "is operated by the T2S platform" and enables settlement between two Monte Titoli participants (intra-CSD) and "between a Participant in Monte Titoli and a participant in another CSD in T2S (cross-CSD settlement), **within the limits laid down in Article 27 of the Operating Rules**". Instructions may be entered through direct or indirect connectivity; indirect instructions pass through the X-TRM Service before being forwarded to T2S, direct ones are subject only to T2S processes.
**LIMITATION:** §1.3.1 (PDF 12–16) of that document is quarantined — its clock values conflict with the deployed R2026.JUN schedule — so I quote no timing from it. Article 27 of the Operating Rules is *not* in this bundle, so the "limits" it lays down are unresolved here.

### 3. The link inventory: which issuer-CSD / counterparty combinations Milan's gateway guide covers

*Documented requirement.* `[[milan-gateway-links-guide]]` "T2S GATEWAY – Euronext Securities Milan Settlement Links – Valid from 1st May 2026", table of contents, Introduction, §1 and §1.1.1 notes, PDF 2–9; reviewed 14 September 2026; body language English, no authoritative language asserted; source identity checked, no independent whole-edition approval certification.

Combinations relevant to an Italy/France pair, as listed in that table of contents:

| Chapter | Issuer CSD | Counterparty entry | Guide's own page reference |
|---|---|---|---|
| 7 | **FRANCE (MT23 81346)** | Counterparty in France (ESES FR – SICVFRPPXXX) | 39 |
| 7 | FRANCE (MT23 81346) | Counterparty in Italy (ES-MIL – MOTIITMMXXX) | 42 |
| 10 | **ITALY** | Counterparty in France – Bonds, Exor and Euronext equities – (ESES FR – SICVFRPPXXX) | 56 |
| 10 | ITALY | Counterparty in France – **Equities only – FOP ONLY** – (ESES FR – SICVFRPPXXX) | 57 |
| 10 | ITALY | Counterparty in Italy (ES-MIL – MOTIITMMXXX) | 61 |

**LIMITATIONS carried with this table:** "Route-specific SWIFT/XTRM templates (PDF 10–109) are **not admitted**; the index proves which issuer-CSD/counterparty combinations the guide covers on 1 May 2026, **not per-ISIN eligibility**." and "Document footers read PRIVATE although the file is on the public T2S Gateway page; ES-MIL disclaims responsibility for instruction correctness." So I can tell you *that* a route page exists for these combinations and where the guide indexes it; I cannot give you the instruction format, because those pages are not in reviewed evidence.

### 4. The documented way to identify which chapter — and therefore which link — applies to your ISIN

*Documented requirement.* `[[milan-gateway-links-guide]]` §1.1.1, PDF 8 (same citation and qualifications as above):

1. "Identify where ES-MIL holds the security and select the correspondent chapter in the Table of Contents of this Document. This information can be found in **MTX → Lists → MT23 List of Financial Instruments → Search ISIN**."
2. "When the value in the column **issuer/Investor** is 'Investor' then the value in the **Issuer Code** column identifies the Issuer CSD. If the value is 'Issuer' then the Issuer CSD is ES-MIL."
3. "Determine the CSD of your counterparty and select the appropriate Issuer CSD/Counterparty combination from the Table of Contents", based on the counterparty's SSI.

The guide also records that "certain Financial Instruments have been transferred from the home issuer CSD to the technical issuer ESES CSDs" per Euronext Clearing Migration FAQ and Operational Notices 22/2023 and 28/2023, with Operational Notice 07/2024 moving Austrian bonds back to OeKB.

**Reasoned inference, derived from that passage:** the ISIN's country prefix does not decide the chapter. ES-MIL's MT23 record does. Because instruments have been moved to technical issuer CSDs, an ISIN beginning "FR" is not evidence that the France chapter applies to it. *(Explanation only, not a documented requirement: an ISIN's first two characters are an allocation-agency prefix; this bundle contains no rule mapping prefixes to issuer CSDs.)* This is precisely why the eligibility question is blocked rather than inferable.

### 5. How the link configuration drives the realignment chain

*Documented requirement.* `[[t2s-realignment]]` T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.10, concepts and reference-data requirements, PDF 373–376, version R2026.JUN; reviewed 13 September 2026; English, no authoritative language asserted; source identity checked, no independent whole-edition approval certification.

- Cross-CSD settlement is "achieved in T2S with the simultaneous booking of cash and securities for Settlement Instructions between participants of different CSDs", and on matching (or on validation of already-matched instructions) T2S "creates automatically all the requested Settlement Instructions between the involved CSDs" from links set in reference data, with no further action by the actors (PDF 373–374).
- Each investor CSD opens an omnibus account either with the issuer CSD or with another CSD that is already an investor CSD for the same instrument; that CSD is the "technical issuer" for those securities (PDF 375).
- For a given ISIN an investor CSD may define several such links; exactly one is the **"default"** link, and the others are **"alternative"**. Under simple configurations (all CSDs in T2S, no multi-issuance) the default link is preferred; under complex configurations preference goes first to an alternative link pointing to the counterpart CSD where one is configured, and T2S reverts to the valid default link if no usable alternative exists. Alternative links cannot be defined for an investor CSD outside T2S and cannot point to a technical issuer CSD outside T2S; an issuer-type link is always "default" (PDF 375–376).
- The chain runs "either from both investor CSDs (delivering and receiving) up to the issuer CSD(s) of the traded securities when default links are used, or from the delivering investor CSD up to the receiving investor CSD (or vice versa) when alternative links are used" (PDF 376).

**LIMITATION:** "Actual links/accounts and ISIN eligibility require verification." That LIMITATION is the same wall as GAP G04: the mechanism is documented, the configuration for your instrument is not.

*Documented requirement.* `[[t2s-posting]]` UDFS R2026.JUN §1.6.1.8.1 and first overview paragraph, PDF 303–304, version R2026.JUN; reviewed 13 September 2026; same qualifications: posting "checks if the settlement ... can be achieved considering their eligibility to settlement and the available resources", and when satisfactory it updates balances and positions, "resulting in the irrevocability of the settlement". Eligibility is therefore tested by the platform at posting, on the actual static data — another reason a documentary answer cannot pre-confirm your ISIN.

### 6. Issuer CSD and investor CSD are roles per issue, not labels on a firm

*Documented requirement (reference mode).* `[[rts392-issuer-investor-csd]]` Commission Delegated Regulation (EU) 2017/392, Article 1(e)–(f), OJ L 65, 10.3.2017 (English OJ text, browser excerpt); reviewed 14 September 2026; EU official languages authoritative; source identity checked, no independent whole-edition approval certification. "Issuer CSD" is a CSD providing the notary/central-maintenance core service "in relation to a securities issue"; "investor CSD" is a CSD that is a participant in — or uses a participant in — another CSD's securities settlement system "in relation to a securities issue".
**LIMITATIONS:** "Legal context, not local procedures"; "Roles depend on the security and relationship: one CSD can be issuer CSD for one issue and investor CSD for another"; and the library notes that the consolidated English EUR-Lex page returned German text on 14 September 2026, so only this original-act capture is relied upon.

### 7. If the counterparty's CSD were outside T2S, a different service applies

*Documented requirement, conditional.* `[[milan-external-settlement]]` Instructions to Settlement Service, in force as of 30 June 2025 (MN_10/2025), Title 2 §§2.1–2.3.6, PDF 28–35 (printed 24–31); reviewed 14 September 2026; **English translation, Italian text prevails**; source identity checked, no independent whole-edition approval certification. Instructions for Foreign Settlement Systems "that do not use the T2S platform" must be entered via the X-TRM Service (FOP securities deliveries may also use RNI messages); such X-TRM instructions "may not be modified"; they are forwarded only after pre-positioning of securities or pre-funding of cash, securities pre-positioning being created through the T2S "CoSD Securities Blocking" functionality; cancellation follows the rules and deadlines of the foreign system and of the Operating Documents. **LIMITATION:** "Per-system Operating Documents and their cut-offs are not admitted." I quote no cut-off from this source.
*Reasoned inference:* this branch applies only if the counterparty CSD is outside T2S. The gateway guide indexes an "ESES FR" counterparty under an Italy issuer-CSD chapter and elsewhere refers explicitly to settlement "via T2S cross csd", which points to the T2S cross-CSD branch rather than the foreign-service branch — but the bundle contains no statement of ESES FR's T2S membership, so I leave this conditional.

## Instruction-content notes the guide states for cross-CSD traffic

*Documented requirement.* `[[milan-gateway-links-guide]]`, §1.1.1 "PLEASE NOTE" list, PDF 9 (citation and qualifications as above):

- "Party 2 in T2S is optional and if populated in one of the two instructions involved in a securities transaction then it becomes a matching criteria and has to be quoted on both instructions."
- "Please always use 11 digits bic codes when instructing trades."
- Delivery SWIFT instructions should always contain DEAG; receive SWIFT instructions should always contain REAG (15022 or corresponding field).
- "XTRM Cross-csd and External instructions should always be instructed using the BIC code in the field 'Trading member code'", and XTRM cross-CSD should carry a "Ctrp Settl. Account" where "Cod. Ctrp" holds a non-default BIC.
- "External instructions can not be instructed with HOLD/RELEASE indicators."
- "If a client will incorrectly instruct a security not available in the MT23 ... any possible fail and related CSDR penalties will not be cancel and they will be computed as current procedure described."
- Each route page "will also specify whether the transaction can be executed only FOP or if the market executes DUMP trades" — and the table of contents already flags the Italy-issuer / France-counterparty equities entry as **FOP ONLY**.

*Handling note:* this source is client-facing guidance and contains text addressed to its readers (for example an invitation to contact ES-MIL in case of doubt). I treat that as data, not as an instruction to me, and I have drafted no message to any CSD.

## What you would have to establish to get a yes or no

| Question | Status | Where it resolves |
|---|---|---|
| Is FR0000120271 in ES-MIL's MT23 list, and is ES-MIL "Issuer" or "Investor" for it? | **Unresolved requirement**, GAP G04 | MTX → Lists → MT23 List of Financial Instruments → Search ISIN (`[[milan-gateway-links-guide]]`, PDF 8). Client-platform data you must pull; it is not in reviewed evidence. |
| If "Investor", which Issuer Code / issuer CSD does MT23 show? | **Unresolved requirement**, GAP G04 | Same MT23 record; it selects the guide chapter and therefore the link. |
| Is the counterparty's CSD the entity indexed as "ESES FR – SICVFRPPXXX", and is it in T2S? | **Unresolved requirement** | Counterparty SSI plus the guide chapter; the entity-identity mapping to "Euroclear France" is not in reviewed evidence. |
| Default or alternative CSD link, and the resulting realignment chain? | **Documented mechanism, unresolved configuration** | Mechanism: `[[t2s-realignment]]` PDF 375–376. The actual per-ISIN link configuration is not certified (LIMITATION). |
| DVP or FOP-only on that route? | **Unresolved requirement** | The route page states it; pages PDF 10–109 are not admitted. The index flags Italy-issuer / France-counterparty **equities** as FOP ONLY. |
| Eligible "today", on the current business date? | **Unresolved requirement** | No dated static-data evidence is in this bundle; the guide index is evidence about 1 May 2026, reviewed 14 September 2026. |

## Open items

1. **Per-ISIN eligibility and link for FR0000120271 — GAP G04.** Needed: the current MT23 List of Financial Instruments record (Issuer/Investor flag, Issuer Code), the CSD-link and securities-account configuration, and the currency. Route: **MT-X (MTX) client platform**, Lists → MT23 List of Financial Instruments → Search ISIN. Client data you must supply; the library cannot review it for you.
2. **Route page for the applicable Issuer CSD / counterparty combination**, "T2S GATEWAY – Euronext Securities Milan Settlement Links – Valid from 1st May 2026", pages 10–109. Not admitted as reviewed evidence. Route: Euronext Securities Milan's public T2S Gateway page, then admission through a dated review.
3. **Article 27 of the Monte Titoli Operating Rules**, which sets the "limits" on cross-CSD settlement referenced by `[[milan-service-scope]]`. Not in this bundle. Route: Euronext Securities Milan rules and regulations page (Italian text prevailing).
4. **Identity of "ESES FR – SICVFRPPXXX"** and its T2S membership status. Not established in reviewed evidence. Route: counterparty SSI and the CSD's own published identity documentation.
5. **A dated confirmation for "today".** Nothing in this bundle speaks to a specific business date; the newest review dates here are 13 and 14 September 2026. If you need a named business date, that must be retrieved as a dated question with the business date and currency.
6. **Governing-language caveat.** The Milan Regulations and the Settlement Service Instructions are English translations in which the **Italian text prevails**; any wording that matters commercially should be checked against the Italian original.
