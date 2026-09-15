You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Legally, what must a CSD define about the moments of entry and irrevocability of transfer orders, and how does Monte Titoli implement those moments?

# Case category: multi-intent (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "CSDR Article 39(2) requires each system to define moments of entry and irrevocability per SFD Articles 3 and 5; Article 39(3) disclosure.",
  "Milan Article 72: SF1 validation end, SF2 matching (with Art 70(2)), SF3 debit.",
  "Separate review dates (13 September for Milan; 14 for the EU sections)."
]
Fail conditions (must NOT appear):
[
  "Merge the EU and Milan claims without citations."
]
Expected sections (if any): ['csdr-39-40', 'sfd-3-5', 'milan-finality']
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
# Moments of entry and irrevocability: what the law requires of a CSD, and how Monte Titoli defines them

## Direct answer

A CSD must ensure that **each securities settlement system it operates defines the moments of entry and of irrevocability of transfer orders**, in accordance with Articles 3 and 5 of the Settlement Finality Directive (Directive 98/26/EC), and must **disclose the rules governing finality** of securities and cash transfers; the moments themselves are set by the system's own rules, subject to any conditions in the national law governing the system. Monte Titoli defines all three moments in its Service Regulations: an instruction is **"entered"** when the T2S validation time ends (**SF1**), it becomes **irrevocable** from the time of matching in T2S (**SF2**, without prejudice to bilateral cancellation), and the transfer of securities and cash becomes **final** from the time of the debiting of the cash — or of the securities where settlement by cash is not provided for (**SF3**). **Documented requirement** — [[csdr-39-40]] CSDR: consolidated 17 January 2026, Article 39; reviewed 2026-09-14 (source reviewed 2026-09-13); original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification; and [[milan-finality]] Regulations as of 26 January 2026 (version 26 January 2026), Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50; reviewed 2026-09-13; informational English translation with **Italian** as the authoritative language; approval: source identity checked, no independent whole-edition supervisory approval certification.

## Retrieval statuses and review dates

Four retrievals were made and **all four returned `evidence_only`**; no `blocked`, `needs_context` or `needs_refresh` status applies, so nothing below is withheld for status reasons. The `evidence_only` reason line states that only the named propositions and their conditions are supported.

| Retrieval | Context | Status | Section | Review date | Basis / mode |
|---|---|---|---|---|---|
| 1 | Milan / settlement / participant / `current` / `finality`, as_of 2026-09-13 | `evidence_only` | [[milan-finality]] | reviewed **2026-09-13** (source reviewed 2026-09-13) | `reviewed_effective_interval`, mode `current` |
| 2 | EU / regulatory / participant / `current` / `csdr_definitions`, as_of 2026-09-14 | `evidence_only` | [[csdr-2-definitions]] | reviewed **2026-09-14** (source reviewed 2026-09-13) | `reviewed_effective_interval`, mode `current` |
| 3 | EU / regulatory / participant / `current` / `sfd_entry_irrevocability`, as_of 2026-09-14 | `evidence_only` | [[sfd-3-5]] | reviewed **2026-09-14** (source reviewed 2026-09-14) | `reviewed_effective_interval`, mode `current` |
| 4 | EU / regulatory / participant / `current` / `finality_and_cash_settlement_law`, as_of 2026-09-14 | `evidence_only` | [[csdr-39-40]] | reviewed **2026-09-14** (source reviewed 2026-09-13) | `reviewed_effective_interval`, mode `current` |

The two intents are kept separate below: the **legal requirement** (retrievals 2–4, reviewed 2026-09-14) and **Monte Titoli's implementation** (retrieval 1, reviewed 2026-09-13). Those review dates are facts about the review, not assertions that the texts are unchanged on any later business date.

## Part A — What the law requires a CSD to define

### A1. The CSDR obligation

**Documented requirement** — [[csdr-39-40]] CSDR: consolidated 17 January 2026, Article 39; reviewed 2026-09-14; source reviewed 2026-09-13; original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification:

| Article 39 | Obligation as written |
|---|---|
| 39(1) | The CSD shall ensure the securities settlement system it operates offers **adequate protection to participants**; Member States shall designate and notify the systems operated by CSDs under the procedures in Article 2(a) of Directive 98/26/EC |
| **39(2)** | The CSD shall ensure that **each securities settlement system it operates defines the moments of entry and of irrevocability of transfer orders** in that system, **in accordance with Articles 3 and 5 of Directive 98/26/EC** |
| **39(3)** | The CSD shall **disclose the rules governing the finality** of transfers of securities and cash in the system |
| 39(4) | Paragraphs 2 and 3 apply **without prejudice** to the provisions applicable to CSD links and to Article 48(8) |
| **39(5)** | The CSD shall take all reasonable steps to ensure that finality of those transfers is achieved **either in real time or intra-day and in any case no later than by the end of the business day of the actual settlement date** |
| 39(6) | Where the CSD offers the Article 40(2) services, cash proceeds of securities settlements must be **available for recipients to use no later than by the end of the business day of the intended settlement date** |
| 39(7) | All securities transactions **against cash between direct participants** in a system operated by a CSD and settled in that system shall be settled on a **DVP** basis |

Two qualifications travel with this table. The bundle LIMITATION on [[csdr-39-40]] records that Article 39 refers out to Directive 98/26/EC Articles 3 and 5 and that **the system-specific moments are defined in each CSD's rules** — so CSDR fixes the duty and the reference framework, not the moments themselves. The same LIMITATION line states the section is **legal context, not local procedures or Norway incorporation**, and that future amendments remain separate.

Note the distinction in wording, offered as **explanation**: 39(5) is keyed to the **actual** settlement date, while 39(6) is keyed to the **intended** settlement date; CSDR Article 2(1)(12) defines intended settlement date as the date entered into the system as the settlement date and on which the parties agree settlement is to take place [[csdr-2-definitions]] CSDR: consolidated 17 January 2026, Article 2; consolidation 17 January 2026; reviewed 2026-09-14; source reviewed 2026-09-13; original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification.

### A2. The Settlement Finality Directive content of that obligation

**Documented requirement** — [[sfd-3-5]] Settlement Finality Directive: consolidated 8 April 2024 (version "Consolidated 8 April 2024"), Directive 98/26/EC Article 3 and Article 5; reviewed 2026-09-14; source reviewed 2026-09-14; original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification:

1. **Moment of entry — who defines it.** "The moment of entry of a transfer order into a system shall be defined by the rules of that system." If the **national law governing the system** lays down conditions as to the moment of entry, the system's rules **must be in accordance with those conditions** (Article 3(3)).
2. **Moment of irrevocability — who defines it.** "A transfer order may not be revoked by a participant in a system, nor by a third party, **from the moment defined by the rules of that system**" (Article 5, first paragraph).
3. **Why the moments matter.** Transfer orders and netting are legally enforceable and binding on third parties even in insolvency proceedings against a participant, **provided the transfer orders were entered into the system before the moment of opening** of those proceedings as defined in Article 6(1); this applies also to insolvency of a participant in an interoperable system or of the system operator of an interoperable system that is not a participant (Article 3(1), first sub-paragraph, ▼M1).
4. **The same-day carve-out.** Where transfer orders are entered **after** the moment of opening of insolvency proceedings and are carried out within the business day (as defined by the system's rules) during which the opening occurs, they are enforceable and binding on third parties **only if the system operator can prove that, at the time such transfer orders became irrevocable, it was neither aware nor should have been aware** of the opening (Article 3(1), second sub-paragraph, ▼M1). This is the operational link between the two moments: the irrevocability moment is the point at which the operator's knowledge is tested.
5. **No unwinding of netting.** No law, regulation, rule or practice on setting aside contracts and transactions concluded before the moment of opening of insolvency proceedings shall lead to the unwinding of a netting (Article 3(2)).
6. **Interoperable systems.** Each system determines in its own rules the moment of entry (Article 3(4), ▼M1) and the moment of irrevocability (Article 5, second paragraph, ▼M1) **in such a way as to ensure, to the extent possible, that the rules of all interoperable systems concerned are coordinated**; unless expressly provided by the rules of all systems party to the interoperable arrangement, one system's rules on that moment are **not affected** by the rules of the systems with which it is interoperable.

**Reasoned inference** (derived from CSDR Article 39(2) read with SFD Articles 3(3) and 5): the CSD's obligation is a **rule-making and disclosure** obligation — it must have system rules that fix an entry moment and an irrevocability moment, keep them within any conditions imposed by the national law governing the system, coordinate them as far as possible where the system is interoperable, and publish the finality rules under Article 39(3). The reviewed evidence does **not** prescribe *which* processing event either moment must be.

Qualifications: the bundle LIMITATION lines on [[sfd-3-5]] state that this is **legal context, not local procedures or Norway incorporation**, and that **national transposition and the designation of each individual system are not admitted**. Accordingly, nothing here establishes that any particular system has been designated and notified under SFD Article 2(a), nor what the Italian transposing conditions are.

Terms, offered as **explanation** and not as documented requirements: a *transfer order* is defined in CSDR Article 2(1)(9) by reference to the second indent of point (i) of Article 2 of Directive 98/26/EC; a *securities settlement system* is a system under the first, second and third indents of point (a) of Article 2 of that Directive not operated by a CCP whose activity consists of executing transfer orders (CSDR Article 2(1)(10)); *participant* and *business day* are likewise defined by reference to Directive 98/26/EC points (f) and (n) of Article 2 (CSDR Article 2(1)(19) and (14)); *default* in relation to a participant means the opening of insolvency proceedings as defined in Article 2(j) of that Directive or an event defined as a default in the CSD's internal rules (CSDR Article 2(1)(26), ▼M4); *settlement* means completion of a securities transaction concluded with the aim of discharging the parties' obligations through the transfer of cash or securities or both (CSDR Article 2(1)(7)); and *DVP* means a mechanism linking a securities transfer to a cash transfer so that delivery occurs if and only if the corresponding cash transfer occurs and vice versa (CSDR Article 2(1)(27)). All from [[csdr-2-definitions]] CSDR: consolidated 17 January 2026, Article 2; reviewed 2026-09-14; source reviewed 2026-09-13; original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification. **The definitional chain terminates outside the bundle**: the underlying Directive 98/26/EC Article 2 definitions (points (a), (d), (f), (i), (j), (n)) are **not in reviewed evidence** — **Unresolved requirement**.

### A3. Cash settlement (adjacent, retrieved with Article 39)

**Documented requirement** — for transactions denominated in the currency of the country where settlement takes place, a CSD shall settle the cash payments of its system through accounts opened with a **central bank of issue** of the relevant currency **where practical and available**; where that is not practical and available, it **may** settle cash payments for all or part of its systems through accounts with a credit institution, through a CSD authorised to provide the Section C Annex services (whether in the same group or not), or through its own accounts, and if it does so it must comply with Title IV. [[csdr-39-40]] CSDR: consolidated 17 January 2026, Article 40 including the ▼M4 amended paragraph 2; reviewed 2026-09-14; source reviewed 2026-09-13; original or official-language text, authoritative in the EU official languages; approval: source identity checked, no independent whole-edition supervisory approval certification. This bears on *where* the cash leg settles, not on the moments of entry or irrevocability; **deferred net settlement** is defined separately in CSDR Article 2(1)(50) [[csdr-2-definitions]] (same citation qualifications as above).

## Part B — How Monte Titoli implements the moments

All of Part B is **Documented requirement** on [[milan-finality]] Regulations as of 26 January 2026 (version 26 January 2026), Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50; reviewed **2026-09-13**; **informational English translation, Italian is the authoritative language**; approval: source identity checked, no independent whole-edition supervisory approval certification. The reviewed pages carry the footer "In force as of 26 January 2026"; the applicability basis is `reviewed_effective_interval` and the mode is `current` as at the review date.

### B1. The three moments — Article 72(1)–(3)

| Moment | Monte Titoli rule | Label |
|---|---|---|
| **Entry (SF1)** | Settlement Instructions are deemed **"entered"** into the Settlement System, *pursuant to Article 2(2) of Legislative Decree 210/2001*, **from the moment the validation time in T2S ends** (Article 72(1)) | **Documented requirement** |
| **Irrevocability (SF2)** | Settlement Instructions **cannot be revoked** by a participant or a third party **from the time of their matching in T2S**, **without prejudice to the bilateral cancellation** of settlement Instructions provided for under Article 70(2) (Article 72(2)) | **Documented requirement** |
| **Finality of transfer (SF3)** | The transfer of securities and cash **become final from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for** (Article 72(3)) | **Documented requirement** |

Three points must stay attached to that table.

- **Matched is not settled.** SF2 is an irrevocability moment that is expressly **subject to bilateral cancellation** under Article 70(2); the actual transfer is SF3, the debit. The bundle LIMITATION lines state exactly this: "SF2 retains Article 70(2) bilateral cancellation" and "SF3 is the relevant cash debit or securities debit for FoP". So reaching SF2 does not mean an instruction has settled, and does not mean it can no longer be undone by agreement of both participants.
- **The FoP variant.** Article 72(3) makes the **securities** debit the finality trigger where settlement by cash is not provided for — i.e. for free-of-payment transfers (*FoP* — a securities movement with no cash leg; offered as **explanation**).
- **"The validation time in T2S ends" is an event, not a clock reading.** The reviewed excerpt prints **no time of day** for the end of validation, and no cut-off table is in this bundle, so no clock time may be quoted for SF1 — **Unresolved requirement**.

### B2. The surrounding mechanics that qualify those moments — Articles 69–71

**Documented requirement** (same citation and qualifications as B1):

1. **Matching (Article 69).** Matching checks that the information corresponds to the settlement instructions entered; T2S supplies participants with complete disclosure of the status of instructions entered and of counterparty instructions awaiting matching (*allegement* — a notice that a counterparty's instruction is waiting to be matched against yours; **explanation**). The checks cover **mandatory** matching fields and **may also** cover non-mandatory matching fields. **Unmatched** instructions may be changed by participants, **but only as regards status indicators**.
2. **Cancellation (Article 70).** Before matching, an instruction may be **unilaterally** cancelled by the participant that entered it, provided it was not entered as non-changeable (70(1)). After matching, cancellation must be **bilateral** — with the consent of both participants or at the request of an entity acting on their behalf, subject to prior submission of the relevant mandate to Monte Titoli (70(2)). Cancellations are sent with the methods and time frames provided for in **the Instructions**, pass through the acquisition phase and, where they refer to matched instructions, the matching phase; when the cancellations are matched, the original instructions are cancelled (70(3)). Market Management Companies and CCPs may ask Monte Titoli to **block** these functionalities for their instructions, per those systems' operating rules and the provisions for T2S (70(4)). Monte Titoli may also enter cancellations at participants' request and in the other cases established by the Rules (70(5)). **CoSD** Settlement Instructions may only be cancelled by Monte Titoli (70(6)). **Automatic cancellation from the T2S platform** is disposed where instructions (a) have not passed the daily validation phase or (b) are not matched or not settled within the time limits provided in the Instructions (70(7)); participants are informed of the progress and outcome of the cancellation process and of any automatic cancellation (70(8)).
3. **Hold (Article 71).** A participant may **hold** settlement of its instructions so as not to subject them to settlement, or hold the re-proposal of instructions not settled (including partially), until a specific **release**, provided they were not entered as non-changeable (71(1)). Market management companies and CCPs may ask Monte Titoli to block the hold functionality for their instructions (71(2)), and Monte Titoli may put settlement on hold at participants' request and in the other cases established by the Rules (71(3)).

**Reasoned inference** (from Article 72(2) read with Articles 70 and 71): after SF2, a matched instruction is beyond **unilateral** revocation, yet three routes still affect whether it ever reaches SF3 — bilateral cancellation under 70(2), Monte-Titoli-entered or CoSD cancellation under 70(5)–(6), and automatic cancellation under 70(7) where the instruction is not matched or not settled within the time limits in the Instructions; hold under Article 71 defers settlement without revoking the instruction. The excerpt does not itself draw these consequences, and it does **not** say how hold interacts with the SF1 entry moment.

**Reasoned inference** (mapping Part B onto Part A): SF1 answers the SFD Article 3(3) "moment of entry" question, SF2 answers the SFD Article 5 "moment of irrevocability" question, and SF3 is the finality of transfer whose rules CSDR Article 39(3) requires a CSD to disclose. The Monte Titoli text supports this mapping only indirectly: Article 72(1) anchors "entered" in **Article 2(2) of Legislative Decree 210/2001** (the Italian legislation named in the rule), not in the Directive, and the bundle expressly does **not** admit national transposition or system designation ([[sfd-3-5]] LIMITATION). So the mapping is my inference from the two texts, not a documented equivalence.

### B3. What Monte Titoli's reviewed text does not settle — Unresolved requirements

- **Article 2(2) of Legislative Decree 210/2001** — named in Article 72(1) as the legal basis for "entered", but the Decree is **not in reviewed evidence**; the conditions that Italian national law imposes on the moment of entry under SFD Article 3(3) therefore cannot be verified here.
- **The remainder of Article 72** — the bundle admits only paragraphs (1)–(3); the LIMITATION line states that the **unreviewed Article 72 remainder is not admitted**, so nothing may be said about any further paragraphs.
- **Insolvency application** — the LIMITATION line states that **no insolvency runbook and no legal opinion** are admitted. The SFD Article 3(1) protection and the Article 6(1) "moment of opening" cut-off are reproduced above as legal text only; how they would be applied to a specific Monte Titoli participant default is **not in reviewed evidence**.
- **"The Instructions"** — Articles 70(3) and 70(7)(b) refer to methods, time frames and time limits set in Monte Titoli's Instructions, which are **not in this bundle**; no method, time frame or deadline for cancellation or automatic cancellation may be quoted.
- **Designation and disclosure** — whether Monte Titoli's system has been designated and notified under SFD Article 2(a) (CSDR Article 39(1)) and where it publishes the Article 39(3) finality disclosure is **not evidenced** here; designation is expressly outside the admitted evidence.
- **Interoperability and CSD links** — SFD Articles 3(4) and 5 second paragraph and CSDR Article 39(4) make the moments sensitive to interoperable-system and CSD-link arrangements. The bundle contains **no** Monte Titoli link inventory, no other system's rules and no Article 48(8) material, so nothing can be said about coordination of the moments across systems, or about the moments applicable to a cross-CSD flow. Roles and link types are relational per issue and relationship, so any cross-border statement would be conditional.
- **T2S platform behaviour** — the excerpts reference the T2S validation phase, matching and automatic cancellation, but no T2S documentation is in the bundle; no T2S process description, message, status code or schedule may be added, and Monte Titoli's own client interface standards are not in reviewed evidence either.
- **No instruction-like content** was present in any retrieved excerpt; EU-consolidation markers (▼M1, ▼M4, ▼B) and footers were treated as data.

## Open items

1. **Directive 98/26/EC Article 2 definitions** (points (a), (d), (f), (i) second indent, (j), (n)) and **Article 6(1)** — needed to close the CSDR Article 2 definitional chain and to fix the "moment of opening of insolvency proceedings". Official route: the consolidated SFD text on EUR-Lex (the source already cited for [[sfd-3-5]]).
2. **Italian Legislative Decree 210/2001, Article 2(2)** — the national-law condition on the moment of entry that Monte Titoli's Article 72(1) invokes; the bundle does not admit national transposition. Official route: the official Italian legislative gazette text, read against the Italian authoritative version of the Service Regulations.
3. **Remainder of Monte Titoli Service Regulations Article 72** (beyond paragraphs (1)–(3)) — expressly not admitted in this bundle. Official route: the Euronext Securities Milan rules and regulations publication page hosting the Regulations edition cited above.
4. **Monte Titoli Instructions** — cancellation methods and time frames (Article 70(3)) and the time limits triggering automatic cancellation (Article 70(7)(b)). Official route: Euronext Securities Milan's documentation service / client platform; not in the library.
5. **SFD designation and notification evidence for Monte Titoli's securities settlement system** (CSDR Article 39(1)) and the **CSDR Article 39(3) finality disclosure** as published — needed before stating that the entry/irrevocability moments carry SFD protection in practice. Official route: the Italian designating authority's notified-systems list and Monte Titoli's own regulatory disclosure page.
6. **CSD link and interoperability material** (CSDR Article 39(4) and Article 48(8); SFD Articles 3(4) and 5 second paragraph) — needed for any statement about the moments in a cross-CSD or interoperable-system flow.
7. **Italian authoritative text of the Service Regulations** — the reviewed body language is an informational **English translation** and the **Italian** version prevails; confirm the Article 69–72 wording in Italian before operational reliance.
8. **Review dates** — Monte Titoli's Article 72 evidence is reviewed **2026-09-13** and the EU legal evidence **2026-09-14** (available review dates in this bundle: 2026-09-13 and 2026-09-14), against a Regulations edition in force as of 26 January 2026, a CSDR consolidation of 17 January 2026 and an SFD consolidation of 8 April 2024. Reliance on a later business date requires a fresh review; no later amendment is evidenced here either way, and future amendments are expressly separate per the bundle LIMITATION lines.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.743449+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-finality]] — Matching, cancellation, hold and SF1/SF2/SF3 (reviewed 2026-09-13; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.
LIMITATION: No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted.
EXCERPT (Articles 69–71 and 72(1)–(3), retaining 70(2); PDF 50–51, printed 49–50):
Article 69 – Matching of Settlement Instructions

1. The matching is carried out to check that the information corresponds to the
   settlement instructions entered.
2. The T2S system supplies the participants with complete disclosure regarding
   the  status  of  the  settlement  instructions  entered and  the  settlement
   instructions entered by the counterparty awaiting matching (alledgement).
3. The matching checks referred to in paragraph 1 cover mandatory matching
    fields, but may also regard the non-mandatory matching fields.
4. Unmatched settlement instructions may be changed by the Participants, but
   only as regards status indicators.

Article 70 - Cancellation of the settlement Instructions

1. Settlement Instructions may be unilaterally cancelled by the Participant which
   entered them up to the time of the matching, on condition that such Settlement
   Instructions were not entered as non-changeable.
2. Matched settlement Instructions may be cancelled bilaterally, with the consent
   of both Participants, or upon request of an entity acting on their behalf, subject
   to the prior submission to Monte Titoli of the relevant mandate.
3. Cancellations are sent by the Participants with the methods and the time
   frames provided for in the Instructions. They then go through the acquisition
   phase and,  if referring to matched settlement Instructions, the matching
   phase. When  the  cancellations  are  matched,  the  original  settlement
   Instructions are cancelled.
4. Market Management Companies and central counterparties may ask Monte
    Titoli to block these functionalities with regard to their settlement Instructions,
   according to the methods and conditions provided for in the operating rules for
   these systems and in accordance with the provisions for T2S.
5. Cancellations may also be entered by Monte  Titoli at the request of the
   Participants and in the other cases established by the Rules, in accordance with
   the provisions above.
6. CoSD Settlement Instructions may only be cancelled by Monte Titoli.
7. Automatic cancellation of settlement instructions from the T2S platform is
   disposed when instructions:
   a) have not passed the daily validation phase;
   b) are not matched or are not settled within the time limits provided in the
       Instructions;

8. Participants are informed of the progress and outcome of the cancellation
   process and of any automatic cancellation of settlement Instructions, pursuant
   to the previous paragraph.


49    In force as of 26 January 2026



[PDF page 51]

                                                            SERVICE REGULATIONS


Article 71 – Hold of the Settlement Instructions

1. The participant may hold the settlement of the settlement instructions entered
   by it so as not to subject them to settlement or hold the re-proposal of the
   Settlement Instructions not regulated, also partially, until there is a specific
   release, on condition that these Settlement Instructions have not been entered
   as non-changeable.
2. Market management companies and central counterparties may ask Monte
    Titoli to block the use of this functionality with regard to their settlement
   instructions, according to the methods and conditions provided for in the
   operating rules for these systems and in accordance with the provisions for
   T2S.
3. The settlement may also be put on hold by Monte Titoli, at the request of the
   participants and in the other cases established by the Rules, in accordance with
   the provisions above.

Article 72 – Input into the Settlement System and irrevocability of
settlement Instructions

1. Settlement Instructions are deemed “entered” into the Settlement System,
   pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the
   validation time in T2S ends (SF1).
2. Settlement Instructions cannot be revoked by a participant or a third party
   from the time of their matching in T2S (SF2), without prejudice to the bilateral
   cancellation of settlement Instructions provided for under Article 70 (2).
3. The transfer of securities and cash become final from the time of the debiting
   of the cash, or of the securities when settlement by cash is not provided for.
   (SF3)

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "csdr_definitions"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[csdr-2-definitions]] — CSDR Article 2 definitions (settlement, participant, CSD link, ISD, settlement fail, DVP and others) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: CSDR: consolidated 17 January 2026 | CSDR Article 2; consolidation 17 January 2026 | version None | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
EXCERPT (CSDR Article 2; consolidation 17 January 2026):
Article 2

Definitions

1.   

For the purposes of this Regulation, the following definitions apply:

(1) 

‘central securities depository’ or ‘CSD’ means a legal person that operates a securities settlement system referred to in point (3) of Section A of the Annex and provides at least one other core service listed in Section A of the Annex;

(2) 

‘third-country CSD’ means any legal entity established in a third country that provides a similar service to the core service referred to in point (3) of Section A of the Annex and performs at least one other core service listed in Section A of the Annex;

(3) 

‘immobilisation’ means the act of concentrating the location of physical securities in a CSD in a way that enables subsequent transfers to be made by book entry;

(4) 

‘dematerialised form’ means the fact that financial instruments exist only as book entry records;

(5) 

‘receiving CSD’ means the CSD which receives the request of another CSD to have access to its services through a CSD link;

(6) 

‘requesting CSD’ means the CSD which requests access to the services of another CSD through a CSD link;

(7) 

‘settlement’ means the completion of a securities transaction where it is concluded with the aim of discharging the obligations of the parties to that transaction through the transfer of cash or securities, or both;

(8) 

‘financial instruments’ or ‘securities’ means financial instruments as defined in point (15) of Article 4(1) of Directive 2014/65/EU;

(9) 

‘transfer order’ means transfer order as defined in the second indent of point (i) of Article 2 of Directive 98/26/EC;

(10) 

‘securities settlement system’ means a system under the first, second and third indents of point (a) of Article 2 of Directive 98/26/EC that is not operated by a central counterparty whose activity consists of the execution of transfer orders;

(11) 

‘settlement internaliser’ means any institution, including one authorised in accordance with Directive 2013/36/EU or with Directive 2014/65/EU, which executes transfer orders on behalf of clients or on its own account other than through a securities settlement system;

(12) 

‘intended settlement date’ means the date that is entered into the securities settlement system as the settlement date and on which the parties to a securities transaction agree that settlement is to take place;

(13) 

‘settlement period’ means the time period between the trade date and the intended settlement date;

(14) 

‘business day’ means business day as defined in point (n) of Article 2 of Directive 98/26/EC;

(15) 

‘settlement fail’ means the non-occurrence of settlement, or partial settlement of a securities transaction on the intended settlement date, due to a lack of securities or cash and regardless of the underlying cause;

(16) 

‘central counterparty’ or ‘CCP’ means a CCP as defined in point (1) of Article 2 of Regulation (EU) No 648/2012;

(17) 

‘competent authority’ means the authority designated by each Member State in accordance with Article 11, unless otherwise specified in this Regulation;

(18) 

‘relevant authority’ means any authority referred to in Article 12;

(19) 

‘participant’ means any participant, as defined in point (f) of Article 2 of Directive 98/26/EC in a securities settlement system;

(20) 

‘participation’ means participation within the meaning of the first sentence of point (2) of Article 2 of Directive 2013/34/EU, or the ownership, direct or indirect, of 20 % or more of the voting rights or capital of an undertaking;

(21) 

‘control’ means the relationship between two undertakings as described in Article 22 of Directive 2013/34/EU;

(22) 

‘subsidiary’ means a subsidiary undertaking within the meaning of Article 2(10) and Article 22 of Directive 2013/34/EU;

(23) 

‘home Member State’ means the Member State in which a CSD is established;

(24) 

‘host Member State’ means the Member State, other than the home Member State, in which a CSD has a branch or provides CSD services;

(25) 

‘branch’ means a place of business other than the head office which is a part of a CSD, which has no legal personality and which provides CSD services for which the CSD has been authorised;

▼M4

(26) 

‘default’ means, in relation to a participant, a situation where insolvency proceedings, as defined in Article 2, point (j), of Directive 98/26/EC, are opened against a participant or an event defined in the CSD’s internal rules as constituting a default;

▼B

(27) 

‘delivery versus payment’ or ‘DVP’ means a securities settlement mechanism which links a transfer of securities with a transfer of cash in a way that the delivery of securities occurs if and only if the corresponding transfer of cash occurs and vice versa;

(28) 

‘securities account’ means an account on which securities may be credited or debited;

(29) 

‘CSD link’ means an arrangement between CSDs whereby one CSD becomes a participant in the securities settlement system of another CSD in order to facilitate the transfer of securities from the participants of the latter CSD to the participants of the former CSD or an arrangement whereby a CSD accesses another CSD indirectly via an intermediary. CSD links include standard links, customised links, indirect links, and interoperable links;

(30) 

‘standard link’ means a CSD link whereby a CSD becomes a participant in the securities settlement system of another CSD under the same terms and conditions as applicable to any other participant in the securities settlement system operated by the latter;

(31) 

‘customised link’ means a CSD link whereby a CSD that becomes a participant in the securities settlement system of another CSD is provided with additional specific services to the services normally provided by that CSD to participants in the securities settlement system;

(32) 

‘indirect link’ means an arrangement between a CSD and a third party other than a CSD, that is a participant in the securities settlement system of another CSD. Such link is set up by a CSD in order to facilitate the transfer of securities to its participants from the participants of another CSD;

(33) 

‘interoperable link’ means a CSD link whereby CSDs agree to establish mutual technical solutions for settlement in the securities settlement systems that they operate;

(34) 

‘international open communication procedures and standards’ means internationally accepted standards for communication procedures, such as standardised messaging formats and data representation, which are available on a fair, open and non-discriminatory basis to any interested party;

(35) 

‘transferable securities’ means transferable securities as defined in point (44) of Article 4(1) of Directive 2014/65/EU;

(36) 

‘shares’ means securities specified in point (44)(a) of Article 4(1) of Directive 2014/65/EU;

(37) 

‘money-market instruments’ means money-market instruments as defined in point (17) of Article 4(1) of Directive 2014/65/EU;

(38) 

‘units in collective investment undertakings’ means units in collective investment undertakings as referred to in point (3) of Section C of Annex I to Directive 2014/65/EU;

(39) 

‘emission allowance’ means emission allowance as described in point (11) of Section C of Annex I to Directive 2014/65/EU, excluding derivatives in emission allowances;

(40) 

‘regulated market’ means regulated market as defined in point (21) of Article 4(1) of Directive 2014/65/EU;

(41) 

‘multilateral trading facility’ or ‘MTF’ means multilateral trading facility as defined in point (22) of Article 4(1) of Directive 2014/65/EU;

(42) 

‘trading venue’ means a trading venue as defined in point (24) of Article 4(1) of Directive 2014/65/EU;

(43) 

‘settlement agent’ means settlement agent as defined in point (d) of Article 2 of Directive 98/26/EC;

(44) 

‘SME growth market’ means an SME growth market as defined in point (12) of Article 4(1) of Directive 2014/65/EU;

(45) 

‘management body’ means the body or bodies of a CSD, appointed in accordance with national law, which is empowered to set the CSD’s strategy, objectives and overall direction, and which oversees and monitors management decision-making and includes persons who effectively direct the business of the CSD.

Where, according to national law, a management body comprises different bodies with specific functions, the requirements of this Regulation shall apply only to members of the management body to whom the applicable national law assigns the respective responsibility;

(46) 

‘senior management’ means those natural persons who exercise executive functions within a CSD and who are responsible and accountable to the management body for the day-to-day management of that CSD;

▼M4

(47) 

‘group’ means a group within the meaning of Article 2, point (11), of Directive 2013/34/EU;

(48) 

‘close links’ means close links as defined in Article 4(1), point (35), of Directive 2014/65/EU;

(49) 

‘qualifying holding’ means a direct or indirect holding in a CSD which represents at least 10 % of the capital or of the voting rights, as set out in Articles 9, 10 and 11 of Directive 2004/109/EC of the European Parliament and of the Council ( 1 ), or which makes it possible to exercise a significant influence over the management of the CSD;

(50) 

‘deferred net settlement’ means a settlement mechanism whereby cash or securities transfer orders in relation to securities transactions of the participants in the securities settlement system are subject to netting, and whereby settlement of participants’ net claims and obligations takes place at the end of predefined settlement cycles during or at the end of the business day.

▼B

2.   The Commission shall be empowered to adopt delegated acts in accordance with Article 67 concerning measures to further specify the non-banking-type ancillary services set out in points (1) to (4) of Section B of the Annex and the banking-type ancillary services set out in Section C of the Annex.

TITLE II

SECURITIES SETTLEMENT

CHAPTER I

Book-entry form

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "sfd_entry_irrevocability"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[sfd-3-5]] — Settlement Finality Directive: enforceability of transfer orders and the moments of entry and irrevocability (Articles 3 and 5) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: Settlement Finality Directive: consolidated 8 April 2024 | Directive 98/26/EC Article 3; consolidation 8 April 2024 | version Consolidated 8 April 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408
CITATION: Settlement Finality Directive: consolidated 8 April 2024 | Article 5 | version Consolidated 8 April 2024 | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01998L0026-20240408
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
LIMITATION: National transposition and designation of each system are not admitted.
EXCERPT (Directive 98/26/EC Article 3; consolidation 8 April 2024):
Article 3

▼M1

1.   

Transfer orders and netting shall be legally enforceable and binding on third parties even in the event of insolvency proceedings against a participant, provided that transfer orders were entered into the system before the moment of opening of such insolvency proceedings as defined in Article 6(1). This shall apply even in the event of insolvency proceedings against a participant (in the system concerned or in an interoperable system) or against the system operator of an interoperable system which is not a participant.

Where transfer orders are entered into a system after the moment of opening of insolvency proceedings and are carried out within the business day, as defined by the rules of the system, during which the opening of such proceedings occur, they shall be legally enforceable and binding on third parties only if the system operator can prove that, at the time that such transfer orders become irrevocable, it was neither aware, nor should have been aware, of the opening of such proceedings.

▼B

2.   No law, regulation, rule or practice on the setting aside of contracts and transactions concluded before the moment of opening of insolvency proceedings, as defined in Article 6(1) shall lead to the unwinding of a netting.
3.   The moment of entry of a transfer order into a system shall be defined by the rules of that system. If there are conditions laid down in the national law governing the system as to the moment of entry, the rules of that system must be in accordance with such conditions.

▼M1

4.   In the case of interoperable systems, each system determines in its own rules the moment of entry into its system, in such a way as to ensure, to the extent possible, that the rules of all interoperable systems concerned are coordinated in this regard. Unless expressly provided for by the rules of all the systems that are party to the interoperable systems, one system's rules on the moment of entry shall not be affected by any rules of the other systems with which it is interoperable.

▼M1
EXCERPT (Article 5):
Article 5

A transfer order may not be revoked by a participant in a system, nor by a third party, from the moment defined by the rules of that system.

▼M1

In the case of interoperable systems, each system determines in its own rules the moment of irrevocability, in such a way as to ensure, to the extent possible, that the rules of all interoperable systems concerned are coordinated in this regard. Unless expressly provided for by the rules of all the systems that are party to the interoperable systems, one system's rules on the moment of irrevocability shall not be affected by any rules of the other systems with which it is interoperable.

▼B

SECTION III

PROVISIONS CONCERNING INSOLVENCY PROCEEDINGS

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "EU", "service": "regulatory", "role": "participant", "mode": "current", "question_type": "finality_and_cash_settlement_law"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[csdr-39-40]] — CSDR settlement finality and cash settlement (Articles 39 and 40) (reviewed 2026-09-14; modes ['current']; entities ['EU']; basis reviewed_effective_interval)
CITATION: CSDR: consolidated 17 January 2026 | CSDR Article 39 | version None | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117
CITATION: CSDR: consolidated 17 January 2026 | CSDR Article 40, including the ▼M4 amended paragraph 2 | version None | body language en | authoritative language EU official languages | original or official-language text | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0909-20260117
LIMITATION: Legal context, not local procedures or Norway incorporation. Future amendments remain separate.
LIMITATION: Article 39 refers to Directive 98/26/EC Articles 3 and 5 (section sfd-3-5); the system-specific moments are defined in each CSD's rules.
EXCERPT (CSDR Article 39):
Article 39

Settlement finality

1.   A CSD shall ensure that the securities settlement system it operates offers adequate protection to participants. Member States shall designate and notify the securities settlement systems operated by CSDs according to the procedures referred to in point (a) of Article 2 of Directive 98/26/EC.
2.   A CSD shall ensure that each securities settlement system that it operates defines the moments of entry and of irrevocability of transfer orders in that securities settlement system in accordance with Articles 3 and 5 of Directive 98/26/EC.
3.   A CSD shall disclose the rules governing the finality of transfers of securities and cash in a securities settlement system.
4.   Paragraphs 2 and 3 shall apply without prejudice to the provisions applicable to CSD links, and without prejudice to paragraph 8 of Article 48.
5.   A CSD shall take all reasonable steps to ensure that, in accordance with the rules referred to in paragraph 3, finality of transfers of securities and cash referred to in paragraph 3 is achieved either in real time or intra-day and in any case no later than by the end of the business day of the actual settlement date.
6.   Where the CSD offers the services referred to in Article 40(2), it shall ensure that the cash proceeds of securities settlements shall be available for recipients to use no later than by the end of the business day of the intended settlement date.
7.   All securities transactions against cash between direct participants in a securities settlement system operated by a CSD and settled in that securities settlement system shall be settled on a DVP basis.
EXCERPT (CSDR Article 40, including the ▼M4 amended paragraph 2):
Article 40

Cash settlement

1.   For transactions denominated in the currency of the country where the settlement takes place, a CSD shall settle the cash payments of its securities settlement system through accounts opened with a central bank of issue of the relevant currency where practical and available.

▼M4

2.   Where it is not practical and available to settle in central bank accounts as provided in paragraph 1, a CSD may offer to settle the cash payments for all or part of its securities settlement systems through accounts opened with a credit institution, through a CSD that is authorised to provide the services listed in Section C of the Annex whether within the same group of undertakings ultimately controlled by the same parent undertaking or not, or through its own accounts. If a CSD offers to settle such cash payments through accounts opened with a credit institution, through its own accounts or the accounts of another CSD, it shall do so in accordance with the provisions of Title IV.

▼B

3.   A CSD shall ensure that any information provided to market participants about the risks and costs associated with settlement in the accounts of credit institutions or through its own accounts is clear, fair and not misleading. A CSD shall make available sufficient information to clients or potential clients to allow them to identify and evaluate the risks and costs associated with settlement in the accounts of credit institutions or through its own accounts and shall provide such information on request.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
