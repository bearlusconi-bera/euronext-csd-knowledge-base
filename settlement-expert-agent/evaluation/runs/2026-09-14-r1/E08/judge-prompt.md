You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Quote the exact legal moment of irrevocability for Monte Titoli's settlement system and any exception to it.

# Case category: adversarial-italian-prevails (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Article 72(2): instructions cannot be revoked from matching in T2S (SF2), without prejudice to bilateral cancellation under Article 70(2).",
  "SF1 at end of T2S validation; SF3 at debit.",
  "English translation; Italian text prevails; review date 13 September 2026."
]
Fail conditions (must NOT appear):
[
  "Omit the Italian-prevails qualification.",
  "Omit the bilateral-cancellation exception."
]
Expected sections (if any): ['milan-finality']
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
# Irrevocability in Monte Titoli's settlement system (Euronext Securities Milan)

## Direct answer

The legal moment of irrevocability is **matching in T2S (SF2)**, and the exception is the **bilateral cancellation of matched settlement instructions under Article 70(2)**. The provision reads, verbatim:

> "2. Settlement Instructions cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70 (2)."

**Documented requirement** [[milan-finality]] — *Regulations as of 26 January 2026, Article 72(2); Articles 69–71 and 72(1)–(3) retaining 70(2), PDF 50–51 (printed pages 49–50); version 26 January 2026; reviewed 13 September 2026; English body text but **the authoritative language is Italian — this is a translation and the Italian text prevails**; approval: source identity checked, no independent whole-edition supervisory approval certification.*

---

## The three moments, as the Regulations separate them

Article 72 is titled "Input into the Settlement System and irrevocability of settlement Instructions" and defines three distinct moments, labelled SF1, SF2 and SF3. All three are **documented requirements** from [[milan-finality]], same locator and qualifications as above:

| Moment | Verbatim provision | What it establishes |
|---|---|---|
| **SF1 — entry** | "1. Settlement Instructions are deemed 'entered' into the Settlement System, pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the validation time in T2S ends (SF1)." | The instruction is *entered into the system* for the purposes of Article 2(2) of Legislative Decree 210/2001. Entry, not irrevocability. |
| **SF2 — irrevocability** | "2. Settlement Instructions cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70 (2)." | Unilateral revocation by a participant **or a third party** stops at matching — subject to the Article 70(2) exception. |
| **SF3 — finality of transfer** | "3. The transfer of securities and cash become final from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for. (SF3)" | The transfer itself becomes final at the cash debit, or at the securities debit where there is no cash leg (free-of-payment). |

**Reasoned inference** (derived from reading Article 72(2) against Article 72(3), not from a single sentence): SF2 is not settlement. Matching makes the instruction irrevocable in the sense of Article 72(2); the securities and cash transfer becomes final only at SF3. An instruction can therefore be irrevocable and still unsettled. Any specification that treats "matched" as "settled" misreads the article.

*Explanation of terms, not a documented requirement:* **matching** is the comparison of the two sides' settlement details to confirm both parties agree on the terms; **allegement** (printed "alledgement" in the source) is the notice to a counterparty that an instruction is waiting to be matched against it; **free-of-payment (FoP)** is a securities transfer with no cash leg in the system.

---

## The exception, and the other cancellation routes in the same chapter

### The exception named in Article 72(2)

**Documented requirement** [[milan-finality]], *Article 70(2), PDF 50 (printed 49); version 26 January 2026; reviewed 13 September 2026; English translation, Italian text prevails*:

> "2. Matched settlement Instructions may be cancelled bilaterally, with the consent of both Participants, or upon request of an entity acting on their behalf, subject to the prior submission to Monte Titoli of the relevant mandate."

So the exception has three conditions on its face: it is **bilateral**; it needs **the consent of both participants**; and where an entity acts on their behalf, the **relevant mandate must have been submitted to Monte Titoli beforehand**. The section carries an explicit limitation on this point: **SF2 retains Article 70(2) bilateral cancellation** [[milan-finality]].

**Documented requirement** [[milan-finality]], *Article 70(3), same locator and qualifications*: a bilateral cancellation is not a instant unwind — "Cancellations are sent by the Participants with the methods and the time frames provided for in the Instructions. They then go through the acquisition phase and, if referring to matched settlement Instructions, the matching phase. When the cancellations are matched, the original settlement Instructions are cancelled." The cancellation instructions must themselves match before the original instruction is cancelled.

### Other cancellation provisions in Article 70 that bear on revocability

These are **documented requirements** from the same excerpt [[milan-finality]], and they qualify the picture without being the Article 72(2) exception itself:

- **Article 70(1)** — unilateral cancellation is available to the entering participant **only up to the time of matching**, and only if the instruction was not entered as non-changeable. This is the mirror image of SF2.
- **Article 70(4)** — market management companies and central counterparties may ask Monte Titoli to **block** these cancellation functionalities for their settlement instructions, under those systems' operating rules and in accordance with the provisions for T2S.
- **Article 70(5)** — cancellations may also be entered by Monte Titoli at the request of participants and in the other cases established by the Rules, in accordance with the provisions above.
- **Article 70(6)** — "CoSD Settlement Instructions may only be cancelled by Monte Titoli."
- **Article 70(7)** — automatic cancellation from the T2S platform is disposed when instructions "a) have not passed the daily validation phase; b) are not matched or are not settled within the time limits provided in the Instructions".
- **Article 70(8)** — participants are informed of the progress and outcome of the cancellation process and of any automatic cancellation.

**Reasoned inference** (derived from Article 70(6)–(7) read against Article 72(2)): automatic cancellation under 70(7)(b) and CSD-only cancellation of CoSD instructions under 70(6) are removals of the instruction effected by the system or by Monte Titoli, not revocations by "a participant or a third party". Article 72(2) names only Article 70(2) as the reservation to irrevocability, so I do not treat 70(6) or 70(7) as further exceptions to SF2 — but the Regulations do not say so expressly, and this reading is mine, not the text's.

---

## Limitations that travel with this answer

Both limitations recorded on the section apply directly to this question [[milan-finality]]:

1. **"SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP."** — the exception is part of the rule, not a footnote to it, and SF3's trigger differs for FoP.
2. **"No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted."** — only Article 72(1)–(3) are in reviewed evidence. **Unresolved requirement:** whether Article 72 continues beyond paragraph 3, and whether any further paragraph adds an exception, a deferral or an insolvency-specific rule, is **not in reviewed evidence**. So I can state that Article 70(2) is the exception *named in Article 72(2)*, but I cannot certify that it is the only exception anywhere in the Regulations.
3. **Governing language.** The excerpt is the English edition of the Service Regulations in force as of 26 January 2026; the authoritative language is **Italian** and the Italian text prevails. For a legal opinion or a contractual citation, the Italian wording of Articles 70 and 72 must be used, not this translation [[milan-finality]].
4. **Approval status.** Source identity was checked, but there is no independent whole-edition supervisory approval certification [[milan-finality]].
5. **Review date.** This position was **reviewed on 13 September 2026**. That is a review date, not a statement that the text is unchanged at any later moment.
6. **Retrieval status.** The single retrieval in this bundle returned `evidence_only`; no retrieval returned `blocked`, `needs_context` or `needs_refresh`.

**Unresolved requirement — the wider legal frame.** Article 72(1) points outward to **Article 2(2) of Legislative Decree 210/2001**. That decree is not in this bundle, so the statutory definition of "entry into a system", its insolvency-protection effects and the moment from which those effects run under Italian law are **not in reviewed evidence** here. Nothing in this answer should be read as a legal opinion on the effect of SF1, SF2 or SF3 against an insolvency of a participant.

---

## Open items

1. **The remainder of Article 72 of the Service Regulations in force as of 26 January 2026** (any paragraph after 72(3)), to confirm whether further exceptions or insolvency provisions attach to SF1/SF2/SF3. Only 72(1)–(3) are admitted [[milan-finality]]. Route: the published Service Regulations on the Euronext Securities Milan documentation hub.
2. **The Italian original of Articles 70 and 72** of the same edition, since Italian is the authoritative language and this excerpt is an English translation [[milan-finality]]. Route: the Italian edition of the Regolamento dei Servizi on the same hub.
3. **Legislative Decree 210/2001, Article 2(2)** — referenced by Article 72(1) but not in reviewed evidence. Route: the Italian official gazette / consolidated statute text.
4. **The Instructions ("Istruzioni")** — Article 70(3) and 70(7)(b) both defer to the Instructions for the methods and time frames of cancellation and for the time limits that trigger automatic cancellation. Those methods, time frames and time limits are **not in reviewed evidence**, and no cut-off time may be inferred here. Route: the Instructions accompanying the Service Regulations on the Euronext Securities Milan hub, with client-only material via MT-X.
5. **An insolvency runbook or legal opinion**, expressly excluded from this section [[milan-finality]], if the question behind this one is the effect of irrevocability in a default scenario.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:13.504347+00:00). Review dates available: 2026-09-13, 2026-09-14.

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

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
