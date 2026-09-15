# Moments of entry and irrevocability: what EU law requires, and how Monte Titoli defines them

**Direct answer.** EU law does not fix the clock: it requires that the **moment of entry** of a transfer order into a system, and the **moment from which a transfer order can no longer be revoked**, are each defined **by the rules of that system** (and, where the national law governing the system lays down conditions on the moment of entry, the system's rules must conform to those conditions) [[sfd-3-5]]. Monte Titoli discharges that duty in Article 72 of its Service Regulations, which names three moments: **entry = end of the T2S validation time (SF1)**, **irrevocability = matching in T2S (SF2)**, and **finality of the transfer = the debiting of cash, or of the securities where settlement by cash is not provided for (SF3)** [[milan-finality]].

All three retrievals in this bundle returned `evidence_only`. No status disclosure for blocked, needs_context or needs_refresh is required.

Terms used below: *transfer order* — under CSDR it takes its meaning from the Settlement Finality Directive (see the definitions section); *allegement* — a notice to a counterparty that an instruction is waiting to be matched against it; *matching* — the check that the two sides' instruction data correspond.

---

## 1. What the law requires a system (and therefore a CSD operating it) to define

**Documented requirement.** The Settlement Finality Directive places the definition of both moments in the system's own rulebook.

| Requirement | Text relied on | Citation |
|---|---|---|
| The moment of entry of a transfer order into a system **shall be defined by the rules of that system**; if the national law governing the system lays down conditions as to the moment of entry, the system's rules **must be in accordance with those conditions** | Article 3(3) | [[sfd-3-5]] Settlement Finality Directive 98/26/EC, Article 3, consolidated 8 April 2024; reviewed 14 September 2026; EU official languages, original or official-language text |
| A transfer order **may not be revoked** by a participant in a system, nor by a third party, **from the moment defined by the rules of that system** | Article 5, first paragraph | [[sfd-3-5]] Settlement Finality Directive 98/26/EC, Article 5, consolidated 8 April 2024; reviewed 14 September 2026 |
| In **interoperable systems**, each system determines in its own rules the moment of entry (Article 3(4)) and the moment of irrevocability (Article 5, second paragraph), "in such a way as to ensure, to the extent possible," that the rules of all interoperable systems concerned are coordinated; unless expressly provided for by the rules of all the systems concerned, one system's rules on those moments are **not affected** by the rules of the systems with which it is interoperable | Article 3(4); Article 5, second paragraph | [[sfd-3-5]] as above; reviewed 14 September 2026 |

**Documented requirement — why the two moments carry the legal weight.** Article 3(1) makes transfer orders and netting legally enforceable and binding on third parties even in insolvency proceedings against a participant, **provided the transfer orders were entered into the system before the moment of opening of such proceedings as defined in Article 6(1)**. Where transfer orders are entered **after** that moment and are carried out within the business day (as defined by the rules of the system) during which the opening occurs, they are enforceable against third parties **only if the system operator can prove that, at the time those transfer orders became irrevocable, it was neither aware nor should have been aware of the opening** [[sfd-3-5]] Article 3(1), consolidated 8 April 2024; reviewed 14 September 2026. So the defined moment of entry sets the insolvency cut-off, and the defined moment of irrevocability sets the point at which the operator's state of knowledge is tested.

**Documented requirement — the vocabulary CSDR imports.** CSDR does not redefine these moments; it borrows the Directive's concepts: "transfer order" means a transfer order as defined in the second indent of point (i) of Article 2 of Directive 98/26/EC (Article 2(1)(9)); "securities settlement system" is a system under the first, second and third indents of point (a) of Article 2 of that Directive, not operated by a CCP, whose activity consists of the execution of transfer orders (Article 2(1)(10)); "participant" takes point (f) of Article 2 of that Directive (Article 2(1)(19)); "business day" takes point (n) (Article 2(1)(14)); and "default", as amended, means a situation where insolvency proceedings as defined in Article 2, point (j), of Directive 98/26/EC are opened against a participant, or an event defined in the CSD's internal rules as constituting a default (Article 2(1)(26)) [[csdr-2-definitions]] CSDR, Article 2, consolidated text of 17 January 2026; reviewed 14 September 2026; EU official languages, original or official-language text.

**Qualifications that travel with the two EU sections.** Both are legal context only, not local procedures and not Norwegian incorporation of the acts; future amendments are separate evidence [[csdr-2-definitions]], [[sfd-3-5]]. In addition, **national transposition and the designation of any individual system are not admitted** in this bundle [[sfd-3-5]] — so nothing here establishes *which* Italian instrument transposes the Directive or that a particular system has been designated and notified under it. Source identity was checked for both; no independent whole-edition supervisory approval certification exists for either.

**Reasoned inference** (derived from the two EU sections read together, not stated in either): because Article 3(3) and Article 5 delegate the definition to the system's rules, the CSD's obligation is one of *definition and publication in the rulebook*, not of adopting any particular moment; EU law constrains the content only indirectly, through the national-law conditions clause in Article 3(3) and the coordination duty for interoperable systems.

---

## 2. How Monte Titoli implements the two moments

**Documented requirement.** Article 72 of the Service Regulations ("Input into the Settlement System and irrevocability of settlement Instructions") defines three successive moments, labelled SF1, SF2 and SF3 in the text:

| Moment | Rule text | Label in the source |
|---|---|---|
| **Entry** | Settlement Instructions are deemed "entered" into the Settlement System, pursuant to Article 2(2) of Legislative Decree 210/2001, **from the moment the validation time in T2S ends** | SF1 |
| **Irrevocability** | Settlement Instructions **cannot be revoked by a participant or a third party from the time of their matching in T2S**, without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70(2) | SF2 |
| **Finality of transfer** | The transfer of securities and cash **become final from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for** | SF3 |

[[milan-finality]] Monte Titoli Service Regulations as of 26 January 2026, Articles 69–71 and 72(1)–(3) (retaining Article 70(2)); PDF 50–51, printed 49–50; version 26 January 2026; reviewed 13 September 2026; **English translation — the Italian text is the authoritative language and prevails**; source identity checked, with no independent whole-edition supervisory approval certification.

**Documented requirement — the mechanics around the two moments** (same section, same citation and qualifications):

1. **Matching (Article 69).** Matching checks that the information corresponds to the settlement instructions entered; T2S gives participants complete disclosure of the status of their own instructions and of the counterparty's instructions awaiting matching (allegement); the checks cover mandatory matching fields and may also cover non-mandatory matching fields; unmatched instructions may be changed by participants **only as regards status indicators**.
2. **Cancellation before and after matching (Article 70).** Unilateral cancellation by the entering participant is possible **up to the time of matching**, on condition that the instruction was not entered as non-changeable (70(1)). **Matched** instructions may be cancelled **bilaterally**, with the consent of both participants or on request of an entity acting on their behalf subject to a mandate previously filed with Monte Titoli (70(2)). Cancellations go through the acquisition phase and, if they refer to matched instructions, the matching phase; when the cancellations are matched, the original instructions are cancelled (70(3)). Market management companies and CCPs may ask Monte Titoli to block these functionalities for their instructions (70(4)); Monte Titoli may enter cancellations at participants' request and in the other cases established by the Rules (70(5)); **CoSD settlement instructions may only be cancelled by Monte Titoli** (70(6)); T2S automatically cancels instructions that have not passed the daily validation phase, or that are not matched or not settled within the time limits provided in the Instructions (70(7)); participants are informed of the progress and outcome of cancellation, including automatic cancellation (70(8)).
3. **Hold (Article 71).** A participant may hold settlement of its instructions, or hold the re-proposal of instructions not settled (including partially), until a specific release, provided the instruction was not entered as non-changeable; market management companies and CCPs may ask for the functionality to be blocked for their instructions; Monte Titoli may also apply a hold at participants' request and in the other cases established by the Rules.

**Qualifications attached to this claim (LIMITATION lines of the section).** SF2 **retains Article 70(2) bilateral cancellation** — irrevocability at matching therefore bars *unilateral* revocation by a participant or a third party, and does not bar a bilaterally matched cancellation. SF3 is the **relevant cash debit, or the securities debit for free-of-payment transfers**. **No insolvency runbook, legal opinion, or the unreviewed remainder of Article 72 is admitted** in this bundle [[milan-finality]].

---

## 3. Reading the two together

**Reasoned inference** (derived from Article 3(3) and Article 5 of [[sfd-3-5]] set against Article 72(1)–(2) of [[milan-finality]]; not stated in either source): Article 72(1) is the rulebook definition that Article 3(3) requires, and Article 72(2) is the rulebook definition that Article 5 requires; Monte Titoli locates both moments inside the T2S processing chain — end of validation, then matching. Article 72(3) (SF3) is a **third**, later moment about when the transfer itself becomes final; the excerpts of Articles 3 and 5 in this bundle do not require a system to define that moment, so SF3 is a rulebook addition rather than a transposition of those two articles.

**Reasoned inference — matched is not settled.** SF2 makes a matched instruction irrevocable by unilateral act, but it is not the transfer: the debit at SF3 is. An instruction can therefore be irrevocable and still unsettled — for example while on hold under Article 71, or pending the time limits after which T2S cancels automatically under Article 70(7) [[milan-finality]].

**Unresolved requirement.** Article 72(1) asserts that entry is "pursuant to Article 2(2) of Legislative Decree 210/2001", but that Decree is not in the reviewed evidence, and the section on the Directive expressly does not admit national transposition or the designation of any system [[sfd-3-5]]. This bundle therefore supports *what Monte Titoli's rules say*, not that those rules satisfy the Italian conditions referred to in Article 3(3), and not that the Monte Titoli system is a designated system for the purposes of the Directive.

**Unresolved requirement.** Whether Monte Titoli's system is interoperable with another system for the purposes of Article 3(4) and the second paragraph of Article 5, and how the coordination duty has been exercised, is not in reviewed evidence. Nothing in the bundle addresses the moments of entry or irrevocability of Copenhagen (VP), Porto (Interbolsa), Athens (ATHEXCSD) or Oslo (VPS).

**Note on scope of the dates.** The Milan retrieval was made as of the **13 September 2026** review date; the two EU retrievals as of **14 September 2026**. Those are review dates, not statements that the texts are unchanged today.

---

## Open items

1. **Remainder of Article 72 and the related Regulations text** — only Article 72(1)–(3) (with Articles 69–71) is admitted; any further paragraphs are outside reviewed evidence. Route: Euronext Securities Milan public documentation for the Service Regulations in force (the reviewed edition is the one of 26 January 2026, English translation with the Italian text prevailing).
2. **Legislative Decree 210/2001, Articles 2(2) and the insolvency provisions** — referenced by Article 72(1) but not reviewed. Route: the Italian official source of the Decree; the section on Directive 98/26/EC expressly does not admit national transposition.
3. **Designation and notification of the Monte Titoli settlement system under the Directive** — "national transposition and designation of each system are not admitted" [[sfd-3-5]]. Route: the competent national authority's designation record.
4. **Insolvency runbook / legal opinion on how SF1–SF3 operate on a participant default** — expressly not admitted by the LIMITATION on [[milan-finality]]. Route: Monte Titoli's Instructions to the Settlement Service and any default-management documentation, obtained through the CSD's documentation service or client platform (MT-X).
5. **The "time limits provided in the Instructions"** that trigger automatic cancellation under Article 70(7) — the Instructions are not in this bundle. Route: as item 4.
6. **Italian authoritative text** — every Milan proposition above is taken from an English translation; where the wording is legally decisive, the Italian original governs and should be checked.
