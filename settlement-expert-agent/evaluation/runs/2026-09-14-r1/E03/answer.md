# (a) Unilateral cancellation of a matched instruction; (b) how long an unmatched instruction survives in T2S

## Direct answer

**(a) No.** Once your instruction is matched you cannot cancel it unilaterally. Milan's rules allow unilateral cancellation only up to the moment of matching (and only if the instruction was not entered as non-changeable); a matched instruction requires **bilateral** cancellation, and T2S enforces the same thing technically — both counterparties must send cancellation instructions for their own leg, unless the instruction entered T2S as already matched and an authorised T2S party sends one cancellation carrying both legs. CoSD instructions are narrower still: in Milan they may only be cancelled by Monte Titoli.

**(b) 20 working days for an unmatched instruction**, as the current value: T2S recycles pending instructions for a "recycling period" — the number of working days a pending instruction may remain in T2S before the system cancels it — configured by the T2S Operator, and the UDFS footnote records the current unmatched period as 20 working days. The count runs from the intended settlement date **or the date of the last status change, whichever is later**, and any status change restarts it. Matched instructions have a separate, longer period (currently 60 working days). Note two qualifications: the value is operator-configured, not a fixed rule, and Milan's own automatic-cancellation article refers to "the time limits provided in the Instructions", a document not in this bundle.

**Routing note.** I corrected the routing for this case once: the prepared bundle covered matching and cancellation but carried no retrieval for recycling periods, which is the whole of part (b). I re-ran the retriever with `cancellation_rules` (Milan), `t2s_cancellation_process` (Milan), `t2s_recycling_periods` (Milan) and `matching_concept` (Milan). All four retrievals returned `evidence_only`; nothing was blocked, and no retrieval reported missing context or an unreviewed knowledge date.

---

## (a) Cancelling a matched instruction

### What Milan's Regulations say

**Documented requirement.** All from [[milan-finality]] Regulations as of 26 January 2026, Articles 69–71 and 72(1)–(3), PDF 50–51 (printed 49–50); version 26 January 2026; reviewed 13 September 2026; English translation and the **Italian text prevails**; source identity checked, no independent whole-edition supervisory approval certification:

1. **Unilateral cancellation, and its cut-off.** "Settlement Instructions may be unilaterally cancelled by the Participant which entered them **up to the time of the matching**, on condition that such Settlement Instructions were not entered as non-changeable" (Article 70(1)).
2. **After matching it is bilateral.** "Matched settlement Instructions may be cancelled bilaterally, with the consent of both Participants, or upon request of an entity acting on their behalf, subject to the prior submission to Monte Titoli of the relevant mandate" (Article 70(2)).
3. **The cancellation itself must match.** Cancellations are sent with the methods and time frames provided for in the Instructions, go through the acquisition phase and, if they refer to matched instructions, the matching phase; "When the cancellations are matched, the original settlement Instructions are cancelled" (Article 70(3)).
4. **CoSD.** "CoSD Settlement Instructions may only be cancelled by Monte Titoli" (Article 70(6)).
5. **Blocking by CCPs and market management companies.** Market management companies and central counterparties may ask Monte Titoli to block the cancellation functionality for their instructions (Article 70(4)); Monte Titoli may also enter cancellations at participants' request and in the other cases established by the Rules (Article 70(5)).
6. **Why matching is the boundary.** Instructions "cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70(2)" (Article 72(2)); the transfer becomes final only at the debiting of cash, or of securities where settlement by cash is not provided for (SF3, Article 72(3)).

LIMITATIONS carried with the above: SF2 retains the Article 70(2) bilateral cancellation, and SF3 is the relevant cash debit or the securities debit for free-of-payment instructions; no insolvency runbook, legal opinion, or the unreviewed remainder of Article 72 is admitted here.

*Explanation of the term (background wording, not a documented requirement):* "non-changeable" is the status under which an instruction is entered such that the participant may not later modify or unilaterally cancel it; "CoSD" is conditional settlement, where settlement depends on a condition administered by a designated party.

### How T2S enforces it

**Documented requirement.** All from [[t2s-cancellation]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.5 with Table 60 and footnote 195, PDF 280–284; version R2026.JUN; reviewed 14 September 2026 (underlying source reviewed 13 September 2026); body language English, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification:

| Situation | T2S behaviour |
|---|---|
| Referenced instruction **unmatched** | The cancellation instruction "is executed or denied immediately after its validation". |
| Referenced instruction **matched** | "T2S requires bilateral cancellation and the cancellation is only possible if both Counterparties send their Cancellation Instructions to cancel each leg separately **or** if the Cancellation Instruction is sent with the information of both legs by an authorised T2S Party." |
| Instruction that entered T2S **as already matched** | One cancellation instruction may address both legs or a single leg, depending on the reference used (Table 60: T2S Reference vs T2S Actor Reference). Where it addresses both legs, T2S splits it internally into two maintenance instructions, one per leg, creating two cancellation instructions. |
| **CoSD** instruction | Only Administering Parties or the relevant CSD may cancel; cancellation occurs on receipt of one valid cancellation instruction for each of the two matched instructions; T2S **rejects** cancellation requests from other T2S actors (i.e. CSD participants) for a CoSD instruction, and does not allow Administering Parties to request cancellation if at least one CoSD rule applies to an underlying realignment instruction. |
| **Denial conditions** | A cancellation instruction is denied if the referenced instruction's settlement status is "Settled" or "Cancelled"; if a cancellation instruction for it is already pending; if the referenced instruction is CoSD and the instructing party is not the relevant CSD or administering party; or if a realignment instruction related to it fulfils a CoSD rule and the instructing party is not the relevant CSD. T2S communicates the denial with the relevant reason code, subject to message subscription preferences. |
| **Timing of execution** | Cancellation instructions are immediately executed or denied during the Daytime Window, except those needing to be matched in T2S (bilateral cancellation); during night-time sequences, instructions received are not taken into account until the end of the sequence. |
| **What cannot be cancelled by actors** | T2S actors cannot cancel instruction types other than settlement instructions and settlement restrictions — for example they cannot cancel realignment instructions. They can cancel the unsettled remaining part of a partially settled instruction. |
| **Competing cancellations** | Footnote 195: where the CSD and the party each send a cancellation instruction for the same leg and both remain pending awaiting the counterparty, the T2S matching process prioritises the CSD cancellation instruction over the party cancellation instruction. |

LIMITATIONS carried with this table: the local legal effects of cancellation (for example Milan's Article 70) sit in separate sections at their own review dates; and this is a T2S-native functional description for R2026.JUN — **not** a local participant interface specification, a production XSD or a message usage guideline. I therefore state no field, message version or reason-code value.

**Reasoned inference** (derived from Article 70(2) read with §1.6.1.5.3): the only route that looks like a single-message cancellation of a matched instruction is not a unilateral right. It is either an authorised T2S party instructing both legs of an instruction that entered T2S as already matched, or, in Milan's wording, an entity acting on behalf of both participants under a mandate previously submitted to Monte Titoli. In both cases the other side's consent is presupposed; nothing in the reviewed evidence lets one counterparty cancel against the other's will.

**Documented requirement — the background reason this matters operationally.** Matching only establishes that both parties agree on the settlement terms [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2, PDF 267–271, Diagrams 55–57 and footnote 194; reviewed 13 September 2026 (LIMITATIONS: functional matrix only, no production XML/XSD validation or local interface certification; diagram DVP/DWP labels retained while the paragraph mentions DVP/PFOD). The securities move only when posting succeeds against eligibility and available resources, which is what produces irrevocability of the settlement [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1 and first overview paragraph, PDF 303–304; reviewed 13 September 2026.

---

## (b) How long T2S keeps an unmatched instruction

**Documented requirement.** All from [[t2s-recycling]] T2S UDFS R2026.JUN, §1.6.1.7 "Instructions Recycling" with footnotes 199–200, PDF 296–299; version R2026.JUN; reviewed 14 September 2026 (underlying source reviewed 13 September 2026); body language English, no authoritative language independently established:

1. **The concept.** "At each end of a Settlement Day, T2S recycles pending instructions for a period of time known as recycling period, which is defined as the number of working days a pending instruction can remain in T2S, before being cancelled by the system." Recycling triggers the revalidation process at Start of Day, and the recycling process manages the automatic cancellation of all pending instructions that have exceeded their recycling period.
2. **Two periods.** T2S manages one recycling period for pending **unmatched** instructions and another for pending **matched** instructions and settlement restrictions.
3. **Unmatched — the number.** Unmatched settlement instructions are recycled "for a period of working days **configured by the T2S Operator**", and footnote 199 states: "Current recycling period for unmatched instructions of **20 working days**." The same unmatched period applies to cancellation instructions that need to be matched, counted from their reception in T2S until matching occurs.
4. **When the clock starts — and restarts.** The count starts "from the Intended Settlement Date or the date of the last status change of the instruction… depending on which date is the latest", and "any status value change is considered for restarting the count of the number of days for the recycling period". The UDFS gives a change of Party Hold status from "Yes" to "No" as an example of a status change.
5. **Matched — for contrast.** Pending matched instructions and settlement restrictions are recycled for a period of working days configured by the T2S Operator until settlement or cancellation occurs; footnote 200 states the current matched period as **60 working days**.
6. **The exception that removes the deadline.** In an external-CSD scenario, instructions are **not** automatically cancelled but remain pending and are recycled "for an indefinite period of time" while all three conditions hold: any of the relevant CSDs is external to T2S; the external CSD is the issuer of the security; and the external CSD is configured as not compliant with T2S automatic cancellation of instructions. This lasts until one of those conditions ceases to hold or the T2S actors cancel the instruction.

LIMITATIONS carried with these six points: the external-CSD exception is stated but **individual configurations are not certified** — whether a given external CSD is flagged non-compliant is not established here; and this is a T2S-native functional description for R2026.JUN, not a local participant interface specification, production XSD or message usage guideline.

**Documented requirement — the same outcome in Milan's own rules, without a number.** "Automatic cancellation of settlement instructions from the T2S platform is disposed when instructions: a) have not passed the daily validation phase; b) are not matched or are not settled **within the time limits provided in the Instructions**"; participants are informed of the progress and outcome of the cancellation process and of any automatic cancellation. [[milan-finality]] Articles 70(7)–(8), Regulations as of 26 January 2026, PDF 50 (printed 49); version 26 January 2026; reviewed 13 September 2026; English translation, Italian text prevails. **Documented requirement** also from the same source: T2S automatically cancels pending instructions once they exceed their recycling period, where the realignment chain cannot be built, where instructions fail revalidation (triggered at Start of Day and by reference-data changes affecting the instruction), and in the Start-of-Day realignment-chain scenario described for partially settled transactions [[t2s-cancellation]] §1.6.1.5.3 "Cancellation by the system process", PDF 283–284; reviewed 14 September 2026.

**Unresolved requirement — the two caveats you should carry into any operational rule.**
- The 20-working-day figure is a **footnoted current operator configuration**, not a fixed provision: the body text says the period is "configured by the T2S Operator". It is accurate as of the reviewed edition (R2026.JUN, reviewed 14 September 2026) and could be reconfigured without the body text changing. Nothing in the bundle establishes a notification route for such a change.
- Milan's Article 70(7)(b) points to "the time limits provided in the Instructions". **Monte Titoli's Instructions are not in this bundle**, so I cannot confirm that Milan applies no shorter or additional local limit, nor state what those limits are.

**Reasoned inference** (derived from points 3 and 4 above): because a status change restarts the count, an unmatched instruction that is repeatedly amended or put on and off hold can remain in T2S considerably longer than 20 working days from its original intended settlement date. The restart rule is documented; the practical consequence is my inference.

---

## Open items

- **Unresolved requirement — Monte Titoli's own time limits.** The Instructions referenced by Article 70(3) (methods and time frames for sending cancellations) and Article 70(7)(b) (time limits before automatic cancellation) are not in reviewed evidence. Establishing source: Monte Titoli's Instructions / Services Manuals, via the Euronext Securities Milan public documentation hub or the client documentation service.
- **Unresolved requirement — the current operator configuration.** Whether the recycling periods remain at the footnoted 20 and 60 working days after the review date of 14 September 2026 is not established by this bundle; only the R2026.JUN UDFS footnotes are. Establishing source: the T2S operational configuration as published by the Eurosystem / a later UDFS edition.
- **Unresolved requirement — external-CSD configuration.** Whether any CSD relevant to your instruction is external to T2S, is the issuer CSD, and is configured as not compliant with automatic cancellation is not certified by the evidence; this is what decides whether the deadline applies at all.
- **Unresolved requirement — the client interface.** No message name, version, field, reason code or status value for sending or receiving a cancellation is claimed above: the T2S sections are functional descriptions only, and the Milan local interface (X-TRM) specification was not retrieved for this question.
- **Not asserted:** no cut-off time, deadline hour, fee, ISIN or account eligibility appears above; none is in the reviewed evidence for this question.
- No gap id was named by the bundle, and after the routing correction every retrieval returned `evidence_only`.
