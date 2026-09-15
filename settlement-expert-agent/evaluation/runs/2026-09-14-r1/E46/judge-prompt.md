You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Does Monte Titoli's Article 72 SF2 rule (irrevocability at matching) apply to participants of Euronext Securities Copenhagen?

# Case category: wrong-market (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "No: Milan Article 72 governs Monte Titoli's system; Copenhagen defines its own moments (Part 4 §11.6.7, 11.7.1, 11.8.2.1 for T2S settlement; §§4-6 for VP settlement).",
  "CSDR Article 39(2) requires each system to define its own moments."
]
Fail conditions (must NOT appear):
[
  "Apply Milan rules to Copenhagen."
]
Expected sections (if any): ['copenhagen-t2s-settlement', 'milan-finality']
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
# Does Monte Titoli's Article 72 SF2 (irrevocability at matching) apply to Euronext Securities Copenhagen participants?

## Direct answer

**No.** Article 72 is a provision of **Monte Titoli's own Service Regulations**, it binds participants of **Monte Titoli's** settlement system, and its entry concept is anchored in Italian law (Article 2(2) of Legislative Decree 210/2001) [[milan-finality]] Regulations as of 26 January 2026, Articles 69–71 and 72(1)–(3) retaining 70(2), PDF 50–51 (printed 49–50); version 26 January 2026; reviewed 2026-09-13 (source reviewed 2026-09-13); **English translation, Italian is the authoritative language and the translation's authoritative language differs**; source identity checked, no independent whole-edition supervisory approval certification. Participants of Euronext Securities Copenhagen are instead governed by the **VP Rule Book Part 4 – Settlement Rules**, which fixes its own Moment of Entry, Moment of Irrevocability and Moment of Settlement Finality separately for the **VP settlement route** and the **T2S settlement route** [[copenhagen-vp-matching-finality]] Part 4 §§4–6.2.1, PDF 7–9 and [[copenhagen-t2s-settlement]] Part 4 §11, PDF 14–17; both version "Part 4 Settlement Rules: 1 May 2025" (document footer "Settlement Rules – Version 13"); reviewed 2026-09-14 (source reviewed 2026-09-13); **English rulebook text, Danish law governs the VP system and no authoritative-language statement was reviewed**.

**Substance converges, authority does not.** On Copenhagen's **T2S route**, clause 11.7.1 produces a materially similar outcome to SF2 — irrevocability on "Matched" status on the T2S platform, with bilateral cancellation still available — but it does so **under Copenhagen's own rulebook**, not because Article 72 reaches Copenhagen participants. On Copenhagen's **VP route** the moments are defined around batches, not around T2S at all.

## Retrieval statuses and routing disclosure

All **six** retrievals in the bundle returned **`evidence_only`**. There is no `blocked`, `needs_context` or `needs_refresh` status to disclose.

| # | Context | Status | Sections |
|---|---|---|---|
| 1 | Milan / settlement / participant / current / `matching_concept`, as of 2026-09-13 | evidence_only | milan-finality, t2s-matching, t2s-posting |
| 2 | Copenhagen / settlement / participant / current / `matching_concept`, as of 2026-09-13 | evidence_only | t2s-matching, t2s-posting |
| 3 | Milan / settlement / participant / current / `finality`, as of 2026-09-13 | evidence_only | milan-finality |
| 4 | Copenhagen / settlement / participant / current / `copenhagen_vp_settlement_finality`, as of 2026-09-14 | evidence_only | copenhagen-vp-matching-finality |
| 5 | Copenhagen / settlement / participant / current / `copenhagen_t2s_settlement`, as of 2026-09-14 | evidence_only | copenhagen-t2s-settlement |
| 6 | Copenhagen / settlement / participant / current / `copenhagen_settlement_routing`, as of 2026-09-14 | evidence_only | copenhagen-routing |

**Routing correction applied (once).** As first delivered, the bundle carried only retrievals 1–4. The Copenhagen evidence was therefore limited to the **VP (non-T2S)** route, and that section carries the LIMITATION "Applies to the VP (non-T2S) settlement route; the T2S route is the section copenhagen-t2s-settlement." Since the question asks about a rule whose trigger is **matching in T2S**, the T2S route for Copenhagen participants, and the rule that decides which route a transfer order takes, were the obviously relevant missing routes. Retrievals 5 (`copenhagen_t2s_settlement`) and 6 (`copenhagen_settlement_routing`) were added from the topic index; both returned `evidence_only`. No question type, entity, date or release outside the index was used.

## 1. Why Article 72 does not extend to Copenhagen participants

**Documented requirement** — Monte Titoli's Article 72 reads, in the reviewed text: (1) settlement instructions are deemed "entered" into **the Settlement System**, **pursuant to Article 2(2) of Legislative Decree 210/2001**, from the moment the validation time in T2S ends (**SF1**); (2) settlement instructions **cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2)**, **without prejudice to the bilateral cancellation of settlement instructions provided for under Article 70(2)**; (3) the transfer of securities and cash become final from the time of the **debiting of the cash, or of the securities when settlement by cash is not provided for (SF3)** [[milan-finality]] Regulations as of 26 January 2026, Article 72(1)–(3), PDF 51 (printed 50); version 26 January 2026; reviewed 2026-09-13 (source reviewed 2026-09-13); English translation, Italian authoritative. Article 70(2) — which SF2 preserves — provides that **matched settlement instructions may be cancelled bilaterally, with the consent of both participants, or upon request of an entity acting on their behalf subject to prior submission to Monte Titoli of the relevant mandate** [[milan-finality]] Article 70(2), PDF 50 (printed 49); same version and qualifications. LIMITATION carried with these claims: "**SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP.**"

**Reasoned inference** — derived from the text and scope of the section itself: Article 72 speaks of "**the Settlement System**" and of instructions cancellable only "upon... prior submission **to Monte Titoli** of the relevant mandate"; the designation is made under an **Italian** statute; and the reviewed section is scoped in the library to **entity Milan only** (`entities ['Milan']`), unlike the platform sections, which are scoped to T2S, Milan, Copenhagen and Porto. The rule therefore operates by virtue of participation in Monte Titoli's system, not by subject matter. Nothing in the reviewed evidence extends it to another CSD's participants.

**Unresolved requirement** — the reviewed excerpt covers Articles 69–71 and **only paragraphs (1)–(3) of Article 72**. LIMITATION on this section: "**No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted.**" Any scope, applicability or conflict-of-laws paragraph that might sit in the remainder of Article 72 is **not in reviewed evidence**, and no legal opinion on the reach of the Italian designation is admitted here.

**Unresolved requirement** — the bundle contains **no** evidence on cross-CSD settlement between Milan and Copenhagen, on realignment, or on which system's designation governs each leg where a Copenhagen participant faces a Monte Titoli participant. That question cannot be answered from this bundle.

## 2. What governs a Copenhagen participant instead — and which route applies

**Documented requirement — two settlement routes.** Settlement in the VP Clearing and Settlement system may take place as **VP Settlement or T2S Settlement**; the terms governing VP Settlement are in clauses 3 to 10 and the terms governing T2S Settlement are in **clause 11** [[copenhagen-routing]] Part 4 §2.3.1, PDF 4; version "Part 4 Settlement Rules: 1 May 2025"; reviewed 2026-09-14 (source reviewed 2026-09-13); English rulebook text, Danish law governs the VP system, no authoritative-language statement reviewed. Both routes include DvP transactions in central bank money and FoP transactions; VP also offers handling of **DwP and PFoD** transfer orders in T2S [[copenhagen-routing]] §2.3.2, PDF 4. The **same form of transfer order** is used for both routes [[copenhagen-routing]] §2.2.5, PDF 3.

**Documented requirement — when the T2S route is mandatory.** DvP, DwP and PFoD transactions **must** be submitted for T2S Settlement if (i) the securities are eligible for settlement via T2S according to the User Guidelines and are made available to T2S (cf. clause 11.3), (ii) the settlement currency is a **T2S Currency**, and (iii) the **Cash Settlement Agent of the Participant is not the same on both transfer orders**. A FoP transaction, **excluding one-sided transfer orders (stock dumps)**, must be submitted for T2S Settlement if (i) the securities are T2S-eligible and made available to T2S and (ii) **the Participant is not the same on both transfer orders**. Transactions concerning **Single Priced Mutual Funds** must instead be submitted for FundHub Order Routing Settlement under Part 6 of the VP Rule Book [[copenhagen-routing]] §§2.3.3–2.3.5, PDF 4; same version and qualifications. LIMITATION on this section: "**T2S-eligibility of a security is defined by the User Guidelines, which are not in the library.**"

**Documented requirement — settlement-day frames.** VP will execute **VP Settlement** on all VP Business Days such that VP's settlement day commences at **18:00** on a VP Business Day and concludes immediately prior to **18:00** on the following VP Business Day, and **T2S Settlement** on all T2S Business Days such that the T2S settlement day commences at **18:45** on a T2S Business Day and concludes at **18:00** on the following T2S Business Day — in both cases "subject however, to any technical delay or similar". Settlement participants may submit transfer orders from **05:00** on all VP Business Days until **01:45** on the following day, subject to special conditions for transfers between VP Accounts and T2S Accounts described in the User Guidelines. VP will only execute settlement in a currency on days when the central bank(s) responsible for that currency is open for settlement [[copenhagen-routing]] §§2.2.2–2.2.4, PDF 3; same version and qualifications.

*These are the rulebook's own stated day-frames, not appointments or participant deadlines for any particular business date; no dated event overlay is in this bundle.*

**Documented requirement — how T2S platform rules reach a Copenhagen participant.** The T2S settlement services available to settlement participants are described in the T2S UDFS and the T2S User Handbook (together the **T2S User Guidelines**), and "**The T2S User Guidelines also apply to the Settlement Participant unless the VP Rule Book provides otherwise**" [[copenhagen-t2s-settlement]] Part 4 §11.1.1, PDF 14; version "Part 4 Settlement Rules: 1 May 2025"; reviewed 2026-09-14 (source reviewed 2026-09-13); English rulebook text, Danish law governs, no authoritative-language statement reviewed. LIMITATION on this section: "**The clause links an outdated T2S UHB URL (v2.1, 2015); use the current UDFS sections for platform mechanics.**"

**Reasoned inference** — derived from clause 11.1.1 together with the Milan section: the route by which T2S platform rules bind a Copenhagen participant is **Copenhagen's own rulebook incorporating the T2S User Guidelines**, subordinated to the VP Rule Book where the two differ. Monte Titoli's Service Regulations are not part of that chain in any reviewed evidence.

**Documented requirement — access model.** A settlement participant may instruct a transfer order to T2S **either via VP if it is an ICP of T2S, or directly via the T2S platform if it is a DCP of T2S**; to become a DCP the settlement participant must enter into a **separate agreement with VP** [[copenhagen-t2s-settlement]] §11.2.1, PDF 14; same version and qualifications. *Explanation (not a documented requirement): ICP — indirectly connected participant, instructing through its CSD; DCP — directly connected participant, instructing the platform itself.*

## 3. The three moments, side by side

All rows below are **Documented requirements** from the cited sections. Qualifications travel with every row: the Milan column is an **English translation of an Italian-authoritative text**, version 26 January 2026, **reviewed 2026-09-13**; the two Copenhagen columns are **English rulebook text with Danish law governing the VP system and no authoritative-language statement reviewed**, version "Part 4 Settlement Rules: 1 May 2025", **reviewed 2026-09-14**; all three sources carry source review date **2026-09-13**, source identity checked, **no independent whole-edition supervisory approval certification**.

| Moment | Monte Titoli (Milan) — Article 72 | Euronext Securities Copenhagen — **T2S route** | Euronext Securities Copenhagen — **VP route** |
|---|---|---|---|
| **Entry** | Instructions deemed "entered" into the Settlement System pursuant to Art. 2(2) of Legislative Decree 210/2001 **from the moment the validation time in T2S ends** (**SF1**) [[milan-finality]] Art. 72(1), PDF 51 | **Two different moments**: a transfer order successfully validated **and Pre-Matched** is deemed entered **at the moment VP declared it compliant with the technical rules of T2S**; a transfer order **not** Pre-Matched but passed to T2S is deemed entered **at the moment the T2S platform declared it compliant** [[copenhagen-t2s-settlement]] §11.6.7, PDF 16 | Upon receipt of the transfer order VP makes an acknowledgement available to the instructing party and other participants; **as from that moment the transfer order is deemed "entered"** (**the Moment of Entry**) [[copenhagen-vp-matching-finality]] §4.3, PDF 7 |
| **Irrevocability** | Instructions **cannot be revoked by a participant or a third party from the time of their matching in T2S** (**SF2**), **without prejudice to bilateral cancellation under Art. 70(2)** [[milan-finality]] Art. 72(2) with Art. 70(2), PDF 50–51 | When a transfer order has been given the status **"Matched" on the T2S platform, irrespective of whether it has been Pre-Matched or not**, it **cannot unilaterally be cancelled or revoked** (**the Moment of Irrevocability**); from that moment until settlement, **"Hold & Release" may be applied by each party** and the parties **may bilaterally agree to cancel** their transfer orders **until settlement** [[copenhagen-t2s-settlement]] §11.7.1, PDF 16 | When **Match** has occurred the transfer order **cannot be cancelled or revoked unilaterally** by either participant or a third party (**the Moment of Irrevocability**); the transaction "is thus ready for settlement"; if the parties agree, a binding transfer order **can be cancelled by both parties** submitting a cancellation transaction **received by VP prior to the time of legal effect of the Batch** in which the cancellation is to have effect [[copenhagen-vp-matching-finality]] §5.3.1, PDF 8 |
| **Finality of transfer** | Transfer of securities and cash become final **from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for** (**SF3**) [[milan-finality]] Art. 72(3), PDF 51 | A transfer order is finally settled (**unconditional, irrevocable and enforceable**) as from the **account entry (credit) of the securities on the receiving settlement participant's securities account on the T2S platform** (**the Moment of Settlement Finality**); the corresponding entry is **hereafter mirrored** in the VP Clearing and Settlement System [[copenhagen-t2s-settlement]] §11.8.2.1, PDF 17 | **Net settlement**: finally settled (unconditional, irrevocable and enforceable) **as from the moment the Batch in which the transfer order is settled is completed**; a batch is completed as of the posting on a net basis of the trade amount and the crediting or debiting of the affected securities accounts by book-entry; the transfer order **attains legal effect at the time of legal effect specified for that batch** [[copenhagen-vp-matching-finality]] §6.2.1.1, PDF 9 |

### Reading the table

**Reasoned inference** — derived from row 2: on the **T2S route** the operative trigger is the same observable event (status "Matched" on the T2S platform), and both texts preserve bilateral cancellation, so a Copenhagen participant on the T2S route faces a **substantively comparable** irrevocability moment. The comparison is between **two independent rulebooks that happen to key off the same platform status**; it is not Article 72 applying. Copenhagen's clause also adds something Article 72(2) does not state in the reviewed text — that **Hold & Release remains available after irrevocability** — and expresses the bilateral-cancellation window as running **until settlement**, whereas Milan's Article 70(2) states the consent and mandate conditions without stating a closing point in the reviewed excerpt.

**Reasoned inference** — derived from row 1: the moments of **entry** genuinely differ. Milan fixes SF1 at the end of the validation time in T2S; Copenhagen's T2S route fixes entry **earlier** for pre-matched orders (VP's own compliance declaration) than for non-pre-matched orders (the platform's declaration). LIMITATION carried with that claim: "**Pre-match by VP creates a consolidated already-matched instruction: moments of entry differ for pre-matched and non-pre-matched orders.**"

**Reasoned inference** — derived from row 3: the finality triggers are **not the same event**. Milan's SF3 keys off a **debit** (cash, or securities for FoP); Copenhagen's T2S route keys off the **credit** of securities to the receiving participant's account on the T2S platform, with the VP-side entry described as a subsequent **mirror**; Copenhagen's VP net route keys off **completion of a batch**. Anyone reasoning about a precise cut-off between the two CSDs must use each CSD's own designation.

**Reasoned inference** — derived from [[copenhagen-t2s-settlement]] §11.6.4 read with [[t2s-matching]]: VP attempts a **Pre-Match outside the T2S platform** after successful validation but before upload to the T2S match module; where the pre-match succeeds, **VP creates a new consolidated transfer order** for entry in the T2S match module, and where there is no pre-match the order is passed immediately to T2S for matching in the T2S matching module — the right to pre-match following from a **Collective Agreement with the ECB** [[copenhagen-t2s-settlement]] §§11.6.4–11.6.5, PDF 16. This lines up with the platform rule that **T2S allows CSDs and CSD participants to send already matched instructions cross-CSD and intra-CSD**, such instructions being created with the matching fields as if they had matched in T2S [[t2s-matching]] T2S UDFS §1.6.1.2.2, PDF 268; version R2026.JUN; reviewed 2026-09-13 (source reviewed 2026-09-13); body language English, no authoritative language established. This is a structural feature with no counterpart in the reviewed Milan text, which describes matching as performed in T2S [[milan-finality]] Articles 69 and 72(2), PDF 50–51.

**Documented requirement — the platform layer both CSDs sit on.** T2S matching compares the settlement details provided by the deliverer and the receiver to ensure both parties agree on the settlement terms in a standardised way, according to T2S rules compliant with the ECSDA and ESF matching proposals [[t2s-matching]] UDFS §1.6.1.2.1, PDF 267; R2026.JUN; reviewed 2026-09-13. LIMITATIONs on that section: "**Functional matrix only; no production XML/XSD validation or local interface certification**" and "**Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD**". Separately, the **posting** application process checks whether settlement can be achieved considering eligibility and available resources and, when the check is satisfactory, updates cash balance, securities position and limit headroom, "resulting in the irrevocability of the settlement"; instructions sent by T2S Actors or generated by T2S are submitted to posting at the Intended Settlement Date [[t2s-posting]] UDFS §1.6.1.8.1–1.6.1.8.2, PDF 303–304; R2026.JUN; reviewed 2026-09-13.

**Reasoned inference** — derived from [[t2s-posting]] read against the two rulebooks: the UDFS's "irrevocability of the settlement" at posting is the **platform's** processing concept. The legally designated moments for a participant are those in its **own CSD's** rules — SF1/SF2/SF3 for Monte Titoli, and the Moment of Entry / Moment of Irrevocability / Moment of Settlement Finality of Part 4 for Copenhagen. Matching is agreement on terms; it is not a completed book movement.

## 4. Insolvency treatment is also CSD-specific (context, not part of the SF2 answer)

**Documented requirement** — Copenhagen's T2S route: settlement takes place until VP has received an **authoritative notice on Insolvency Proceedings** of a settlement participant from the **Danish FSA** or other public authority and has initiated its T2S insolvency procedures; transfer orders that reached Moment of Entry, with the corresponding counterparty orders also at Moment of Entry, **prior to the moment of opening** of the proceedings will be attempted settled; orders reaching Moment of Entry **after** opening but matched on the T2S platform before VP became aware (or should have been aware) and due for settlement on the same T2S Business Day will be attempted settled but **cancelled if unsettled at end of day**; all other orders are **immediately cancelled** once VP becomes aware [[copenhagen-t2s-settlement]] §§11.8.3.1–11.8.3.4, PDF 17. On the VP route, if the insolvency procedure is initiated **during a Batch** its effects do not occur until the current batch has concluded, and "**Securities transactions concluded in a Batch are final, irrespective of the Insolvency Proceedings**"; client transactions are not settled from initiation of the procedure, and participant transactions follow the **18:00** notification rules stated in clause 6.1.6.1 [[copenhagen-vp-matching-finality]] §§6.1.4.1–6.1.6.1, PDF 8–9.

**Unresolved requirement** — the corresponding Monte Titoli insolvency treatment is **not in reviewed evidence**: LIMITATION on [[milan-finality]] — "No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted." No comparison of the two insolvency regimes is made here.

## 5. Dates, versions and what is not asserted

- **Review dates.** [[milan-finality]], [[t2s-matching]] and [[t2s-posting]] were **reviewed 2026-09-13**; [[copenhagen-vp-matching-finality]], [[copenhagen-t2s-settlement]] and [[copenhagen-routing]] were **reviewed 2026-09-14**. Every underlying source carries **source review date 2026-09-13**. These are review dates, not assertions that the texts are current at any later moment.
- **Versions.** Milan: "Regulations as of 26 January 2026", version 26 January 2026 (the excerpt's page footer reads "In force as of 26 January 2026"). Copenhagen: "Part 4 Settlement Rules: 1 May 2025", document footer "Settlement Rules – Version 13". T2S sections: release **R2026.JUN**. No other release or edition is described in this bundle and no deployment claim is made.
- **Governing language.** Milan text is an **English translation; Italian is authoritative and the authoritative language differs from the body language**. Copenhagen texts are **English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed**. The T2S UDFS sections are English with **no authoritative language established**. All sources: identity checked, **no independent whole-edition supervisory approval certification**.
- **Not asserted.** No message names or versions, field cardinalities, account numbers, participant-level cut-offs for a given business date, tolerance figures for Copenhagen, ISIN or T2S-eligibility determinations, fees or penalty amounts are stated, because the bundle establishes none of them for this question. Copenhagen's **User Guidelines** — which the rulebook repeatedly designates as the source of matching tolerances, eligibility, formats, account-transfer rules and supported T2S functionalities — are **not in the library**.
- **Instruction-like content.** None of the retrieved excerpts contained text purporting to instruct the responder; all retrieved text was treated as data.

## Open items

1. **Remainder of Monte Titoli's Article 72** — only paragraphs (1)–(3) are admitted (LIMITATION on [[milan-finality]]: "No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted."). Any paragraph defining the article's personal or territorial scope would have to come from the full Italian Service Regulations. Official route: Euronext Securities Milan's published rulebook (Italian authoritative edition).
2. **Italian authoritative text** — the reviewed Milan source is an English translation whose authoritative language differs; a finality determination should rest on the Italian text.
3. **Danish-law authoritative statement for the VP Rule Book** — LIMITATION on all three Copenhagen sections: "English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed." Needed before relying on the English wording of the Moment of Irrevocability.
4. **Copenhagen User Guidelines** — LIMITATION on [[copenhagen-routing]]: "T2S-eligibility of a security is defined by the User Guidelines, which are not in the library." They also define matching tolerances, pre-match detail, Hold & Release mechanics, formats and VP/T2S account transfer rules. Official route: Euronext Securities Copenhagen's client documentation (the User Guidelines are not part of the reviewed public rulebook set).
5. **Outdated reference inside Copenhagen clause 11.1.1** — LIMITATION on [[copenhagen-t2s-settlement]]: the clause links a **T2S UHB URL of v2.1 (2015)**; platform mechanics must be taken from the current UDFS (release R2026.JUN here), and the mismatch between the rulebook's cited handbook edition and the current release is unresolved in reviewed evidence.
6. **Cross-CSD interaction between Milan and Copenhagen** — no section in this bundle addresses cross-CSD or external-CSD settlement, realignment, or which designation governs each leg when a Copenhagen participant faces a Monte Titoli participant. That requires a separate retrieval on cross-CSD settlement and the applicable CSD links.
7. **Legal opinions on finality designations** — none is admitted for either CSD; no conclusion about enforceability against third parties or in insolvency across jurisdictions is drawn here.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:54:57.041840+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
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

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "matching_concept"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-matching]] — Matching rules and repaired functional field diagrams (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | Visually checked Diagrams 55–57; original PDF 269–271 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Functional matrix only; no production XML/XSD validation or local interface certification.
LIMITATION: Retain diagram DVP/DWP labels; paragraph separately mentions DVP/PFOD.
EXCERPT (§1.6.1.2; PDF 267–271; Diagrams 55–57 and footnote 194):
1.6.1.2 Matching


10    1.6.1.2.1 Concept

11   T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer
12   and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in
13   a standardised way, according to the T2S rules, which are compliant with the European Central Securities
14    Depositories Association (ECSDA) and the European Securities Forum (ESF) matching proposals.





     _________________________


        193   The under insolvency situation will be activated upon request of a CSD or CB as explained in the Manual of Operational Procedures (MOP).


                                                                                            Page 267 of 2017



[PDF page 268]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                 DIAGRAM 54 - MATCHING APPLICATION POCESS





 2

 3    1.6.1.2.2 Overview

 4   T2S provides T2S Actors matching services for Settlement Instructions that require to be matched in T2S
 5     (i.e. all Settlement Instructions except the Settlement Instructions with Match status “Matched” regardless
 6    their ISO indicator, ISO transaction code (e.g. CORP) or hold status(es)).

 7    Settlement Restrictions, Maintenance instructions, Realignment instructions, Auto-collaterisation instructions,
 8   Reimbursement auto-collaterisation instructions and Liquidity transfers do not go through the T2S matching
 9    process. The matching of Cancellation Instructions does not follow the rules presented in this section and is
10    presented in section Instruction Cancellation [ 280]).

11   T2S allows CSDs and CSD participants to send already matched instructions Cross-CSD and Intra CSD. In-
12    structions that enter into T2S as already matched are created with the matching fields as if they were
13   matched in T2S (i.e. follow the same matching rules as in T2S).





                                                                                            Page 268 of 2017



[PDF page 269]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    1.6.1.2.3 Matching process

 2   When a new instruction enters T2S, the matching process compares 194 each of the Mandatory and Non-
 3   mandatory matching fields of the Settlement Instruction with the Settlement Instructions that remain un-
 4   matched in T2S:

 5         l  Mandatory matching fields are those fields that must be present in the instruction and which values
 6       should be the same in both Settlement Instructions except Settlement Amount for DVP/PFOD for which a
 7        tolerance might be applied and for Credit/Debit Code (CRDT/DBIT) and Securities Movement Type Deliv-
 8        er/Receiver (DELI/RECE), whose values match opposite.

 9         l  Non-mandatory matching fields can be Additional or Optional:

10      – Additional matching fields are initially not mandatory but their values have to match when one of the
11          counterparties provides a value for them in its instruction. Consequently, once an Additional matching
12             field is filled in by one Counterparty, the other Counterparty should also fill it in, since a filled-in Addi-
13            tional matching field cannot match with a field with no value.

14      – In case of Optional matching fields, a filled-in field may match with a field with no value (unlike Addi-
15            tional matching fields), but when both Parties provide a value, the values have to match.

16   Depending on the Transaction Type T2S considers some fields mandatory or not, as described in the table
17    below. The following tables and illustrations provide examples of the use of the mandatory, optional and
18    additional fields in the matching process.

19   Exhaustive List of Matching Fields

20                   DIAGRAM 55 - MANDATORY MATCHING FIELDS PER TRANSACTION TYPE AND EXAMPLE





21


     _________________________


        194   Upper and lower case letters are considered as different when comparing the values of two different instructions. In case a given matching field is
                      filled in two different instructions with the same reference but a different combination of upper and lower case letters, this matching field is not
                 subject to matching.


                                                                                            Page 269 of 2017



[PDF page 270]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   Non Mandatory Matching Fields per Transaction Type

 2                            DIAGRAM 56 - ADDITIONAL MATCHING FIELDS AND EXAMPLE





 3

 4   Non Mandatory Matching Fields per Transaction Type

 5                             DIAGRAM 57 - OPTIONAL MATCHING FIELDS AND EXAMPLE





 6

 7     If all the Matching fields on both instructions match, except for the Settlement Amount, T2S checks if the
 8    difference between both Settlement Amounts is compliant with the tolerance amount configured in T2S.

 9    This tolerance amount set up in T2S has two different bands per currency, depending on the cash counter-
10    value. ECSDA proposal for Euro is the following:





                                                                                            Page 270 of 2017



[PDF page 271]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1                                TABLE 57 - TOLERANCE AMOUNT FOR MATCHING FOR EURO
 2

             COUNTERVALUE FOR THE CASH AMOUNT                         TOLERANCE

                   ≤ EUR 100.000                                    EUR 2

                   > EUR 100.000                                    EUR 25

 3    In case there is more than one potentially matching Settlement Instruction, T2S chooses the one having the
 4    smallest Settlement Amount difference. If there is more than one potentially matching Settlement Instruc-
 5    tion with the same Settlement Amount, T2S chooses the one with the closest entry time in T2S. When Set-
 6    tlement Instructions with different Settlement Amount are matched, the amount that T2S submits for set-
 7    tlement as Matched Settlement Amount is the Settlement Amount indicated by the Deliverer of the securi-
 8     ties.

 9    After successful matching of both instructions, the T2S Actors receive a Status Advice message as described
10     in section Send Settlement Instruction. This Status Advice will also contain the T2S Matching Reference as-
11    signed to both Settlement Instructions that have been matched by T2S and the T2S Reference and Account
12   Owner Reference of the counterparty´s instruction. Interested parties can also be informed depending on
13    their message subscription preferences (see Section Status Management [ 653] and section Message sub-
14    scription [ 135]).

15    In case the Settlement Instruction does not match after the first attempt, T2S sends a Settlement Al-
16    legement message (after having waited a certain period of time) to the Counterparty informing that there is
17   a Settlement Instruction alleged against it. The Allegement process is described below (See section Al-
18    legement [ 271]), the dialogue is reflected in section Send Settlement Instruction.

19   T2S automatically cancels Settlement Instructions that remain unmatched after a certain period of time (See
20    section Instruction Cancellation [ 280] and section Instructions Recycling [ 296]).

21


22    1.6.1.2.4 Parameter Synthesis

23   No specific configuration from T2S Actor is needed. The following parameter is specified by the T2S Opera-
24     tor.
25

      CONCERNED   PARAMETER   CREATED BY  UPDATED BY  MANDATORY/   POSSIBLE    STANDARD OR DE-
        PROCESS                                         OPTIONAL     VALUES       FAULT VALUE

          Matching      Tolerance    T2S Operator  T2S Operator     M       To be defined    ≤100.000 € = 2€
                      amount                                                                                        >100.000 € = 25€


26
EXCERPT (Visually checked Diagrams 55–57; original PDF 269–271):
{
  "source_id": "aa3d5a3b94c9",
  "source_sha256": "6a0d6e18ee9efd3bba9f761a7fac42d3c3a5e8133b3dc30f51ba557a73344e99",
  "source_url": "https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf",
  "release": "R2026.JUN",
  "verified_as_of": "2026-09-13",
  "actual_content_language": "en",
  "review": "All rows, diagram notes and footnote 194 visually inspected; PDF 271 tolerance narrative read.",
  "scope": "Functional matching-field diagrams, not production XML paths, XSD validation or complete message usage rules.",
  "transaction_headers_verbatim": [
    "DVP/DWP",
    "FOP"
  ],
  "rows": [
    {
      "field": "Payment Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Securities Movement Type",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "ISIN Code",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Trade Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Settlement Quantity",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Intended Settlement Date",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Delivering Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Receiving Party BIC",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Delivering Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "CSD of the Receiving Party",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "mandatory"
    },
    {
      "field": "Currency",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Settlement Amount",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Credit/Debit",
      "diagram": 55,
      "pdf_page": 269,
      "DVP/DWP": "mandatory",
      "FOP": "n/a"
    },
    {
      "field": "Opt-out ISO transaction condition indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "CUM/EX Indicator",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "additional",
      "FOP": "additional"
    },
    {
      "field": "Currency",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Settlement Amount",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Credit/Debit",
      "diagram": 56,
      "pdf_page": 270,
      "DVP/DWP": "n/a",
      "FOP": "additional"
    },
    {
      "field": "Common Trade Reference",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of delivering CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Client of receiving CSD participant",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the delivering party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    },
    {
      "field": "Securities account of the receiving party",
      "diagram": 57,
      "pdf_page": 270,
      "DVP/DWP": "optional",
      "FOP": "optional"
    }
  ],
  "conditions": [
    "Mandatory values match, except opposing Credit/Debit and Securities Movement Type values; settlement amount may use the stated tolerance. The paragraph mentions DVP/PFOD; the diagram header itself reads DVP/DWP. Do not silently normalise these labels into a certified schema mapping.",
    "Additional: a value supplied on either side must also be supplied and match on the other side; blank/blank matches. Credit/Debit matches opposite values.",
    "Optional: one filled and one blank can match; if both are filled they must match.",
    "Footnote 194: upper- and lower-case letters are considered different when comparing values. Do not case-normalise identifiers before comparing.",
    "Diagram 56 note 1: CUM/EX matching considers only ExCoupon and CumCoupon; other values are considered blank.",
    "Diagram 56 note 2: Currency, Settlement Amount and Credit/Debit are additional FOP fields to reduce mismatching risk for non-T2S-currency cash legs submitted as FOP (Payment Flag FREE) with CoSD used to ensure DVP.",
    "Diagram 57 note: client fields match BICs or proprietary codes. Proprietary code matching uses Identification, Issuer and Scheme Name. A BIC does not match a proprietary code.",
    "PDF 270-271: EUR amount tolerance is EUR 2 for cash countervalue <= EUR 100,000 and EUR 25 above EUR 100,000. Currency-specific configuration applies; do not generalise EUR bands to other currencies.",
    "PDF 271: among candidates choose the smallest amount difference, then closest entry time if amounts are the same; the deliverer's amount becomes the matched settlement amount."
  ],
  "counts": {
    "mandatory_diagram_rows": 13,
    "additional_diagram_rows": 5,
    "optional_diagram_rows": 5
  },
  "images": [
    "audits/2026-09-13/evidence/aa3d5a3b94c9-p269.png",
    "implementation/2026-09-13/evidence/t2s-p270.png"
  ],
  "production_schema_validated": false
}

--- SECTION [[t2s-posting]] — Posting checks eligibility and resources before transfer (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.8.1 and first overview paragraph; PDF 303–304 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
EXCERPT (§1.6.1.8.1 and first overview paragraph; PDF 303–304):
1.6.1.8 Posting


 2    1.6.1.8.1 Concept

 3   The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions
 4   and Liquidity Transfers can be achieved considering their eligibility to settlement and the available resources.

 5    In case of high concentration of Settlement Instructions on the same resource (i.e. debiting the same DCA,
 6    debiting or crediting the same SAC not allowed to be negative), the Settlement Instructions could be
 7   grouped without any business links between one another.

 8     It may resort to the optimising application process if needed for the settlement (See section Optimising
 9    [ 335]).

10   When the check is satisfactory, the posting application process updates the cash balance, securities position
11   and limit headroom, resulting in the irrevocability of the settlement.

12                           DIAGRAM 81 - SETTLEMENT APPLICATION PROCESSES / POSTING





13

14    1.6.1.8.2 Overview

15    Settlement Instructions, Settlement Restrictions and Liquidity Transfers, sent by the T2S Actors or automati-
16     cally generated by T2S, are submitted to the posting application process at the Intended Settlement Date.




                                                                                            Page 303 of 2017



[PDF page 304]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1

=== RETRIEVAL 3: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
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

=== RETRIEVAL 4: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_vp_settlement_finality"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-vp-matching-finality]] — VP settlement: entry, matching, moment of irrevocability, settlement and finality (Part 4 §§4–6.2) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §§4–6.2.1; PDF 7–9 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: Applies to the VP (non-T2S) settlement route; the T2S route is the section copenhagen-t2s-settlement.
EXCERPT (Part 4 §§4–6.2.1; PDF 7–9):
4.        VP Settlement - Entering of Transfer Orders
4.1        A Settlement Participant  is entitled to instruct Transfer Orders for VP
             Settlement.
4.2         The Settlement of a transaction requires that the parties in the Transfer
             Order specify a validity period that coincide, i.e. the period during which the
               securities transaction concerned may participate in the Settlement.  If a
              Transfer Order has been received by VP prior to the commencement of the
             Settlement period, cf. clause 5.2.3, the first Batch of that Settlement period
                  will be deemed to be the commencement of the validity period.  If the
              Transfer Order is received at a later time the following Batch will be deemed
              to be the commencement of the validity period. A specified validity period
           must as a minimum comprise one Batch and cannot include more than the
             remaining part of the Settlement period.
4.3        Upon receipt of the Transfer Order for VP Settlement, VP will make an
            acknowledgement  available  to  the  instructing  party  and  any  other
               Participants in the Settlement of the transaction in question. As from that
          moment the Transfer Order is deemed "entered" into the VP Clearing and
             Settlement system (the Moment of Entry).

5.        VP Settlement - Matching

5.1         Introduction
5.1.1         For a Transfer Order to be included in a Batch, VP must have received both
              Transfer Orders concerning such transaction and Matching must be completed
              with a positive result before the time of legal effect of such Batch. If a Transfer
             Order designates a specific Batch in which the securities transaction is to be
               settled, Matching will be carried out until the time of legal effect of such Batch.
                   If no specific Batch has been designated, the Transfer Order will be included in
            matching until the time of legal effect of the last Batch, 20 settlement days
               thereafter.

5.2        Matching criteria etc.
5.2.1         After receipt in due time of the last of the two Transfer Orders VP will carry out
             Matching, i.e. a comparison of the information contained in such Transfer
             Orders, cf. the User Guidelines.
5.2.2            If the transaction amount instructed by the receiving Settlement Participant
                differs from that instructed by the delivering Settlement Participant, the



Settlement Rules - Version 13                                                                  | 7 of 17



[PDF page 8]

              transaction amount submitted  in the Transfer Order from the delivering
             Settlement Participant prevails, provided that the difference does not exceed
              VP’s tolerance thresholds for matching as described in the User Guidelines.
5.2.3            If the result of the matching is positive (Match), VP will make the output data
               available to the parties and any other Participants in the Settlement of the
               securities transaction in question.
5.2.4       Two Transfer Orders concerning net settlement which are Matched can provide
             the basis for Settlement of the securities transaction from a chosen intended
             settlement day and until Settlement takes place or the Transfer Orders are
                bilaterally cancelled by both Settlement Participants.

5.3       Moment of irrevocability
5.3.1      When Match of a Transfer Order has occurred the Transfer Order cannot be
              cancelled or revoked unilaterally by either of the Participant or a third party
              (the Moment of Irrevocability). The securities transaction is thus ready for
              settlement. However, if the parties to a transaction so agree, a binding Transfer
             Order can be cancelled by both parties submitting a cancellation transaction
             which must be received by VP prior to the time of legal effect of the Batch in
             which the cancellation is to have effect.

6.        VP Settlement - Settlement

6.1         Settlement terms
6.1.1       Net settlement

6.1.1.1      Settlement takes place when the net effect of all Transfer Orders in the relevant
             Batch is credited or debited to the affected Securities Accounts. In case of SEK
           DVP settlement, credit or debit of the affected Securities Accounts follow by
             Book-entry against the simultaneous recording  of trade amounts on the
              affected cash accounts. All updating will be carried out in the Batch in question
            and information thereon will be made available to the affected Participants.
6.1.2       Real time gross settlement
6.1.2.1       Real rime gross settlement will be carried out by crediting or debiting as the
             case may be the affected VP Accounts. The registration will be carried out
             immediately after the final verification of coverage, and information will be
          made available to the affected Participants.
6.1.3       Trade amounts
6.1.3.1     When the correct payment instructions in respect of the trade amounts have
            been provided by VP to Sveriges Riksbank for SEK Batches, or made available
              to the Cash Account Controller, VP is released of any and all liability as regards
             the further processing of the information and payments.
6.1.4       Settlement in the event of Insolvency Proceedings of a Participant
6.1.4.1      Settlement of Transfer Orders in accordance with clause 6.1 takes place until
           VP has received an  authoritative notice on Insolvency Proceedings  of a
               Participant from the Danish FSA or other public authority, and VP hereafter
              automatically has initiated its insolvency procedures. Though, VP may issue a
               default notice prior to any authoritative notice and request that the Participant
             provide VP with a statement on the Participants current status pursuant to its
              applicable corporate or company law.



Settlement Rules - Version 13                                                                  | 8 of 17



[PDF page 9]

6.1.4.2       Notwithstanding anything to the contrary in this clause,  if the insolvency
             procedure referred to in clause 6.1.4.1 is initiated during a Batch, the effects
              thereof will not occur until the current Batch has been concluded. Securities
              transactions concluded in a Batch are final, irrespective of the Insolvency
              Proceedings.
6.1.4.3       In case of Insolvency Proceedings of a Participant distinctions must be made
            between the Participant’s own transactions (″Participant Transactions″ - see
              clause 6.1.5.1) and transactions on behalf of a client of the Participant (″Client
              Transactions″ - see clause 6.1.5 ).
6.1.5         Client Transactions
6.1.5.1       Subject to clause 6.1.4.1 Client Transactions will not be settled as from the
              insolvency procedure referred to in clause 6.1.4.1 is initiated.
6.1.6        Participant Transactions
6.1.6.1       Distinctions must be made between net settlement and  real time gross
              settlement:
               A.   Net settlement:

                       Until 18:00 hours on the date that VP is notified of the Insolvency
                    Proceedings, Transfer Orders submitted by the insolvent Participant that
                  have reach Moment of Entry and where also the relevant corresponding
                     Transfer Orders submitted by counterparties have reach Moment of
                    Entry prior to the notification, will be included in VP's Batches and will
                  be submitted for settlement in accordance with the normal terms for
                    Settlement in Batches.

                            If VP is not informed of the Insolvency Proceedings until after 18:00
                   hours on the date of the Insolvency Proceedings, VP will settle the
                       Participant’s Transfer Orders  until the time VP  is notified and has
                        initiated its insolvency procedure.

               B.   Real time gross settlement:

                       Until 18:00 hours on the date that VP is notified of the Insolvency
                    Proceedings, Transfer Orders submitted by the insolvent Participant that
                  have reach Moment of Entry and where also the relevant corresponding
                     Transfer Orders submitted by counterparties have reach Moment of
                    Entry  prior to the  notification  will be submitted  for settlement  in
                   accordance with the normal terms for Settlement in RTGS.

6.2         Settlement Finality
6.2.1       Net settlement
6.2.1.1     A Transfer Order for Settlement in a Batch is finally settled (unconditional,
              irrevocable and enforceable) as from the moment when the Batch in which the
              Transfer Order is settled is completed (the Moment of Settlement Finality). A
             Batch is completed as of the posting on a net basis of the trade amount, etc.
            and the crediting or debiting of the affected Securities Accounts by Book-entry,
                  cf. clause 6.1 above. The Transfer Order in question attain legal effect as at the
             time of legal effect specified for the Batch in question.
6.2.1.2       In the event of a provisional transfer of securities between VP and a Participant
           who is a CSD, retransfer of such securities prior to the first transfer becoming
                 final is prohibited.



Settlement Rules - Version 13                                                                  | 9 of 17

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_t2s_settlement"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-t2s-settlement]] — T2S settlement at VP: access (ICP/DCP), eligibility, accounts, auto-collateral, pre-match, moments of entry, irrevocability, finality and insolvency (Part 4 §11) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §11; PDF 14–17 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: The clause links an outdated T2S UHB URL (v2.1, 2015); use the current UDFS sections for platform mechanics.
LIMITATION: Pre-match by VP creates a consolidated already-matched instruction: moments of entry differ for pre-matched and non-pre-matched orders.
EXCERPT (Part 4 §11; PDF 14–17):
11.        T2S Settlement

11.1        General
11.1.1      The T2S Settlement services available to Settlement Participants are
              described in detail in the T2S User Detailed Functional Specification and in the
           T2S User Handbook (together the T2S User Guidelines) available on the
            European Central Bank webpage
             (https://www.ecb.europa.eu/paym/t2s/pdf/t2s_uhb_v2.1_clean_20151202.p
            df?c485053816eb8ca53b82c066cc118a8d). The T2S User Guidelines also
             apply to the Settlement Participant unless the VP Rule Book provides
              otherwise.

11.2       Access rules
11.2.1      A Settlement Participant may instruct a Transfer Order to T2S, either via VP if
                      it is an ICP of T2S or directly via the T2S platform if it is a DCP of T2S. In order
              to become a DCP the Settlement Participant must enter into a separate
            agreement with VP.

11.3       T2S Settlement - Transfer Orders
11.3.1      A Settlement  Participant  is  entitled  to  instruct Transfer Orders  for T2S
             Settlement,  if the Settlement Participant complies with the terms set out in
              clause 11.4. Also MTS Denmark may submit Transfer Orders in respect of bonds
             traded in MTS Denmark.
11.3.2        Transfer Orders may settle via T2S Settlement if the following conditions are
            met:
               A.   In case of a DvP, DwP and FoP transaction:

                                   i.    The securities concerned are eligible for Settlement via T2S
                           according to the User Guidelines and are made available on T2S
                         (“T2S Eligible Securities”),

                                   ii.    The securities concerned are book-entered with VP, and



Settlement Rules - Version 13                                                                 | 14 of 17



[PDF page 15]

               B.   In case of a DvP, DwP and PFoD transaction, the settlement currency is
                  a T2S Currency, and the transaction is to be settled in central bank
                 money, unless specifically agreed otherwise with VP.

11.4       T2S Accounts
11.4.1      A Settlement Participant must have access to at least one T2S Account with VP,
              unless the Settlement Participant does not need to settle T2S Settlement
             Required Transactions.
11.4.2      A Settlement Participant may in respect of the securities registered on a T2S
             Account use the functionalities blocking, reservation and earmarking as further
              described in the User Guidelines.

11.5       T2S Auto-Collateral
11.5.1        Securities on a T2S Account can be used for T2S Auto-Collateral as agreed with
             VP. This requires that  (i) the Cash Settlement Agent has entered into an
            agreement according to which the securities registered on one or more defined
           T2S Account(s) may be used as collateral for credits granted by the relevant
               central bank in connection with T2S Settlement (referred to as the T2S Auto-
               Collateral agreement), (ii) the Cash Settlement Agent has delivered to VP a
            form stipulating that it wants to use T2S Auto-Collateral, and (iii) that the T2S
             Account has been earmarked for T2S Auto-Collateral by registration of a
                restrictive right in the VP Clearing and Settlement system. The types of
                restrictive rights that may be registered in this respect are described in the
             User Guidelines.
11.5.2      The VP Clearing and Settlement System supports the different T2S Auto-
               Collateral processes which are offered by the T2S System and described in the
           T2S User Guidelines. The T2S Auto-Collateral process depends on the T2S
              Auto-Collateral agreement entered into between the Settlement Participant and
             the relevant central bank. When a Settlement Participant enters into a T2S
              Auto-Collateral agreement the Settlement Participant must initiate the set-up
               of the right account structure with VP, and the central bank must instruct the
           T2S system. Hereafter the T2S Auto-Collateral is handled automatically by the
           T2S system in accordance with the T2S User Guidelines.

11.6        Entering of Transfer Orders, Validation and Pre-Match
11.6.1          All securities registered on a T2S Account may be used for T2S Settlement, and
             cannot be used for VP Settlement, unless the securities are transferred to a VP
             Account. The User Guidelines contain a detailed description of how and when
               securities may be transferred between VP Accounts and T2S Accounts.
11.6.2      A Transfer Order instructed for T2S Settlement is validated by VP upon receipt
                in order to declare it compliant with the technical rules of T2S as set out in the
           T2S User Guidelines. First, VP verifies that the sending party is authorised to
               instruct the Transfer Order via VP. Subsequently, VP applies the validation
                 criteria, and validates  if the mandatory data fields are correctly filled in. A
               detailed description of the information to be reported for validation is contained
                in the User Guidelines.
11.6.3      An unsuccessful validation of a Transfer Order causes a rejection of the Transfer
             Order, and information of the reason for the rejection are generated and sent
              to the submitting party.



Settlement Rules - Version 13                                                                 | 15 of 17



[PDF page 16]

11.6.4      Upon a successful validation of a Transfer Order concerning a T2S Transfer, but
               prior to upload of the Transfer Order for entry in the match module on the T2S
              platform, VP will attempt to perform Match outside the T2S platform (a Pre-
             Match), as further described in the User Guidelines. In case of no pre-match,
             the Transfer Order is immediately passed on by VP to the T2S platform for
            Match in the T2S matching module. If the result of the Pre-Match is successful,
           VP will create a new consolidated Transfer Order to T2S for entry in the T2S
            match module as described in the User Guidelines.
11.6.5      The right for VP to conduct Pre-Matches follows from an agreement (the
               Collective Agreement) with the ECB.
11.6.6          If the transaction amount instructed by the receiving Settlement Participant
                differs from that instructed by the delivering Settlement Participant, the
              transaction amount submitted  in the Transfer Order from the delivering
             Settlement Participant prevails, provided that the difference does not exceed
             the T2S tolerance match rules as set out in the T2S User Guidelines.
11.6.7      A Transfer Order, which has been successfully validated and Pre-Matched, is
           deemed "entered" into the VP Clearing and Settlement system at the moment
               at which  it was declared compliant with the technical rules of T2S by VP
              (the Moment of Entry into the System for pre-matched Transfer Orders).
            Whereas a Transfer Order for T2S Settlement, that has not been Pre-Matched,
             but passed on to the T2S System, is deemed “entered” into at the moment at
             which it has been declared compliant with the technical rules of T2S by the T2S
              platform (the Moment of Entry into the System for not pre-matched Transfer
              Orders).
11.6.8      A Transfer Order may be submitted for same day settlement, for settlement up
              to 13 months in advance of the settlement day, and for a settlement day in the
             past if all relevant static data were valid at the past settlement day.
11.6.9      VP supports various T2S  functionalities such as  linking,  partial  delivery,
                prioritization, etc. The functionalities supported by VP are described in the User
              Guidelines.

11.7       Matching on the T2S platform
11.7.1      When a Transfer Order has been given the status “Matched” on the T2S
              platform, irrespectively of whether it has been Pre-Matched or not, the Transfer
             Order  cannot  unilaterally  be  cancelled  or  revoked  (the  Moment  of
                Irrevocability). From the Moment of Irrevocability and until settlement has
             taken place, the functionality “Hold & Release” may, however, be applied by
            each party and the parties may bilaterally agree to cancel their Transfer Orders
                until settlement. This is further described in the User Guidelines.
11.7.2      A Transfer Order that has not been matched will be handled in accordance with
             the Recycling terms set out in the T2S User Guidelines.

11.8        Settlement
11.8.1      General
11.8.1.1     T2S Settlement  is  carried out by  crediting/debiting the T2S Account as
               applicable, and debiting/crediting a linked DCA as applicable. VP is not involved
                in the process of providing cash liquidity on the DCA as lines are handled in the
           payment system by the Cash Settlement Agent and the relevant central bank.
              For FoP Settlement, the DCA is not impacted.



Settlement Rules - Version 13                                                                 | 16 of 17



[PDF page 17]

11.8.1.2    A Transfer Order that has been matched but not settled because of lack of
             coverage will be handled in accordance with the recycling terms set out in the
             User Guidelines.
11.8.1.3     Information on Securities Account entries on the T2S platform will be made
               available to the affected Settlement Participants and other relevant parties as
              described in the User Guidelines.
11.8.2      Settlement Finality
11.8.2.1    A Transfer Order is finally settled (unconditional, irrevocable and enforceable)
             as from the account entry (credit) of the securities on the receiving Settlement
               Participant’s Securities Account on the T2S platform (the Moment of Settlement
                Finality). The corresponding account entry will hereafter be mirrored in the VP
              Clearing and Settlement System.
11.8.3      T2S Settlement in the event of Insolvency Proceedings of a Participant
11.8.3.1     Settlement of Transfer Orders in accordance with clause 11.8.1 takes place
                until VP has received an authoritative notice on Insolvency Proceedings of a
             Settlement Participant from the Danish FSA or other public authority, and VP
              hereafter has initiated its T2S insolvency procedures as described below. VP
          may also issue a default notice prior to any authoritative notice and request
              that the Settlement Participant provide VP with a statement on the Settlement
               Participant’s current status pursuant to its applicable corporate or company
              law.
11.8.3.2      Transfer Orders submitted by the insolvent Settlement Participant that have
             reached Moment of Entry and where also the relevant corresponding Transfer
             Orders submitted by counterparties have reached Moment of Entry prior to the
          moment of opening of the Insolvency Proceedings will be attempted settled in
             the T2S system.
11.8.3.3      Transfer Orders that have reached Moment of Entry after the moment of
             opening of the Insolvency Proceedings, but have been matched on the T2S
              platform prior to VP became aware, nor should have been aware of the opening
               of such proceedings, and are for settlement on the same T2S Business Day will
            be attempted settled in the T2S system, but will, however be cancelled  if
              unsettled at the end of the day.
11.8.3.4      Transfer  Orders  not  covered  in  clauses  11.8.3.2 and  11.8.3.3  will be
             immediately cancelled after VP becomes aware of the opening of the Insolvency
              Proceedings.
11.8.3.5      In case  of insolvency  of a Settlement Participant VP  will make relevant
              insolvency information available to relevant parties on the T2S settlement
              platform in accordance with the T2S User Guidelines and European Securities
            and Markets Authority’s “Guidelines on CSD participants default rules and
              procedures”.
11.8.3.6     Any actions taken by VP in the event of the opening of Insolvency Proceedings
              against a Settlement Participant will be executed in accordance with the T2S
             User Guidelines on a case-by-case basis.





Settlement Rules - Version 13                                                                 | 17 of 17

=== RETRIEVAL 6: context {"as_of": "2026-09-14", "entity": "Copenhagen", "service": "settlement", "role": "participant", "mode": "current", "question_type": "copenhagen_settlement_routing"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[copenhagen-routing]] — Transfer orders, VP versus T2S settlement days and routing conditions (Part 4 §§2.2–2.3) (reviewed 2026-09-14; modes ['current']; entities ['Copenhagen']; basis reviewed_effective_interval)
CITATION: Part 4 - Settlement Rules (PDF) | Part 4 §§2.2–2.3; PDF 3–4 | version Part 4 Settlement Rules: 1 May 2025. | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2025-05/es-cph_rule_book_part_4_settlement_rules.pdf
LIMITATION: English rulebook text; Danish law governs the VP system and no authoritative-language statement was reviewed.
LIMITATION: T2S-eligibility of a security is defined by the User Guidelines, which are not in the library.
EXCERPT (Part 4 §§2.2–2.3; PDF 3–4):
2.2         Transfer Orders, time periods for reporting and Settlement
2.2.1       A Transfer Order shall be submitted as soon as possible after conclusion of the
               securities transaction in order to establish agreement with respect to the details
               of the transaction (Match). This is to achieve a maximum of efficiency and to
             reduce the operational and settlement risks linked to settlement operations.
2.2.2        Settlement Participants may submit Transfer Orders from 05:00 hours on all
           VP Business Days until 01:45 hours on the following day, subject, however, to
           some special conditions that apply  for transfer of securities between VP
             Accounts and T2S Accounts, which is described in the User Guidelines.
2.2.3        Subject to clause 2.2.4 VP will execute:
               A.   VP Settlement of Transfer Orders on all VP Business Days in such a
                 manner that VP's settlement day commences at 18:00 hours on a VP
                    Business Day and is concluded immediately prior to 18:00 hours on the
                      following VP Business Day, subject however, to any technical delay or
                       similar that prevents VP from either commencing or concluding a day at
                  18:00 hours.
               B.   T2S Settlement of Transfer Orders on all T2S Business Days in such a
                 manner that T2S’ settlement day commences at 18:45 hours on a T2S
                    Business Day, and is concluded at 18:00 hours on the following T2S
                    Business Day, subject however, to any technical delay or similar that
                    prevents VP from either commencing or concluding a day.
2.2.4       VP will only execute Settlement in a currency on such days where the central
             bank(s) responsible for such currency in question is open for Settlement.
2.2.5       The same form of Transfer Order is used for both VP Settlement and T2S
             Settlement. The format requirements for Transfer Orders are described in the
             User Guidelines.
2.2.6       A Transfer Order shall contain the information necessary for the Settlement of
             the securities transaction. A detailed description of the information to be
             reported in the Transfer Order is given in the User Guidelines.




Settlement Rules – Version 13                                                                  | 3 of 17



[PDF page 4]

2.2.7        Settlement of Transfer Orders will be carried out by crediting or debiting, as
             the case may be, the affected Securities Accounts against any recording of
              trade amounts on the affected cash accounts.

2.3       VP Settlement and T2S Settlement
2.3.1        Settlement in the VP Clearing and Settlement system may take place as VP
             Settlement or T2S Settlement. The terms governing the VP Settlement are
             contained in clauses 3 to 10 and the terms governing the T2S Settlement are
             contained in clause 11.
2.3.2        Both the VP Settlement and the T2S Settlement include settlement of DvP
              transactions  in central bank money and FoP transactions. VP also offers
             handling of DwP and PFoD Transfer Orders in T2S.
2.3.3        DvP, DwP and PFoD transactions must be submitted for T2S Settlement, if (i)
             the securities concerned are eligible for Settlement via T2S according to the
             User Guidelines and are made available to T2S,  cf. clause 11.3,  (ii) the
             settlement currency is a T2S Currency, and (iii) the Cash Settlement Agent of
             the Participant is not the same on both Transfer Orders. .
2.3.4       A FoP transaction, excluding one-sided Transfer Orders (Stock dumps), must
            be submitted for T2S Settlement, if (i) the securities concerned are eligible for
             Settlement via T2S according to the User Guidelines and are made available to
             T2S, cf. clause 11.3, and (ii) the Participant is not the same on both Transfer
             Orders.
2.3.5        Notwithstanding the above, transactions concerning Single Priced Mutual Funds
           must be submitted for FundHub Order Routing Settlement in accordance with
              Part 6 of the VP Rule Book (FundHub Rules) and the User Guidelines.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
