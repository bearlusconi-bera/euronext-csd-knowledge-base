# Amending a settlement instruction in T2S after matching, and when it is partially settled

## Direct answer

**After matching you can amend only three process indicators — Partial Settlement Indicator (and its threshold type), Priority, and the Linkages Block — one per Amendment Instruction, and only on your own leg; any other field change requires cancelling the instruction and instructing it again.** **Once the instruction is partially settled, "Priority" is the only process indicator you may still amend**; an Amendment Instruction referring to anything else on a partially settled instruction is denied.

All three retrievals in this bundle returned `evidence_only`, so there is no blocked, needs_context or needs_refresh status to disclose. Everything below is T2S-native functional description for platform release **R2026.JUN** from the T2S UDFS; the sections were reviewed on **13 and 14 September 2026** (source document reviewed 13 September 2026) and each carries the limitation that this is **not a local participant interface specification, production XSD or message usage guideline**, and that no independent whole-edition supervisory approval certification exists for the source.

*Term explanations (background, not documented requirements): a "process indicator" is a control flag on an instruction that steers how T2S processes it, as opposed to the business content of the trade; an "Amendment Instruction" is a maintenance instruction referencing an existing instruction; "partially settled" means part of the quantity has already been transferred and a pending part remains.*

---

## 1. What may be amended after matching

**Documented requirement — the permitted process indicators.** T2S Actors can only amend the following process indicators of a **Settlement Instruction**: Partial Settlement Indicator and threshold type; Priority; Linkages Block. For a **Settlement Restriction** only Priority and the Linkages Block may be amended. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3, PDF page 279; reviewed 14 September 2026; English, no separate authoritative language established; T2S-native functional description only.

Table 59 states the same matrix by instruction state:

| Instruction state | "Partial Settlement Indicator" | "Linkages Block" | "Priority" |
|---|---|---|---|
| Settlement Instruction | YES | YES | YES |
| Settlement Restriction | NO | YES | YES |
| Partially Settled Instruction | NO | NO | YES |

[[t2s-amendment]] T2S UDFS R2026.JUN, Table 59 in §1.6.1.4, PDF page 280; reviewed 14 September 2026.

**Documented requirement — one indicator per instruction, and everything else means cancel and re-instruct.** "T2S Actors are only allowed to modify one process indicator per Amendment Instruction. If the T2S Actor wants to modify a second process indicator, a new Amendment Instruction is required. If the T2S Actor wants to modify other fields of the instruction, it has to cancel the referenced instruction and instruct it again." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 279; reviewed 14 September 2026.

**Documented requirement — who may amend.** T2S Actors send an Amendment Instruction to modify a process indicator "depending on its instruction type and its settlement status"; the T2S Party, the relevant CSD and the authorized parties can amend instructions of a given T2S Actor. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.1, PDF page 277; reviewed 14 September 2026.

**Documented requirement — when the amendment is denied.** T2S accepts and processes an Amendment Instruction that passes Business Validation **unless** any of the following is fulfilled, in which case it is denied:

1. the Settlement Status of the referenced Settlement Instruction or Settlement Restriction is "Settled" or "Cancelled";
2. the referenced Settlement Instruction is identified as CoSD and the Amendment Instruction does not aim to remove a linkage having the CSD as the Instructing Party;
3. the referenced Settlement Instruction or Settlement Restriction is partially settled and the Amendment Instruction refers to a process indicator other than "Priority".

[[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 278; reviewed 14 September 2026.

**Documented requirement — amendment does not reach other instruction types.** "T2S Actors are not able to amend other instruction types than Settlement Instructions or Settlement Restrictions … (i.e. Realignment instructions cannot be amended by T2S Actors)." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2, PDF page 278; reviewed 14 September 2026.

**Reasoned inference — matching itself is not what limits you.** None of the three denial conditions is keyed to match status; they are keyed to settlement status, CoSD identification and partial settlement. Derived from the denial list in [[t2s-amendment]] §1.6.1.4.2. What matching changes is *whose* leg an Amendment Instruction can reach and which reference identifies it, per Table 58 below. The set of amendable indicators is the same before and after matching; the reviewed excerpt does not state a separate pre-matching regime, so do not read one into it.

### Whose leg you can amend (Table 58)

**Documented requirement.** An Amendment Instruction can amend a process indicator of both legs at the same time, or only one leg, of a Settlement Instruction **that entered T2S as already matched**, depending on the reference used:

| Amendment Instruction of … | Instruction sent to T2S **already matched** | Instruction **matched in T2S** |
|---|---|---|
| one leg of the Settlement Instruction | T2S Reference | T2S Actor Reference **or** T2S Reference |
| both legs of the Settlement Instruction | T2S Actor Reference | X (not available) |

[[t2s-amendment]] T2S UDFS R2026.JUN, Table 58 in §1.6.1.4.2, PDF pages 278–279; reviewed 14 September 2026.

For a both-legs Amendment Instruction on an already-matched Settlement Instruction, T2S splits the amendment into two separate maintenance instructions, one per leg, so two different Amendment Instructions are created in T2S; status reporting derived from each lifecycle is handled separately, and the T2S Actor may subscribe to notifications of only one of the two legs. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.2 and §1.6.1.4.3, PDF pages 279–280; reviewed 14 September 2026.

**Reasoned inference — for an instruction matched *in* T2S you reach only your own leg.** Table 58 marks the both-legs cell "X" for instructions matched in T2S, so a party that matched in T2S amends one leg only. Derived from Table 58 in [[t2s-amendment]]. This matters for the Partial Settlement Indicator: partial settlement eligibility requires that the indicator "is not set to 'No' in any of the Settlement Instructions" [[t2s-partial-settlement]] T2S UDFS R2026.JUN, §1.6.1.9.3, PDF page 343; reviewed 14 September 2026 — that is, on both sides. Amending your own leg alone therefore does not by itself make a matched pair partially settleable if the counterparty's instruction says "No". The reviewed evidence does not say whether the counterparty is notified of your amendment beyond the general subscription mechanism.

**Documented requirement — how you learn the outcome.** T2S informs the T2S Actor of the result of the amendment process through a Status Advice message; interested parties can also be informed depending on their message subscription preferences. No specific T2S Reference Data configuration by the T2S Actor is needed for amendment. [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3–§1.6.1.4.4, PDF page 280; reviewed 14 September 2026.

### What you cannot amend, and therefore must cancel and re-instruct

**Reasoned inference — derived from §1.6.1.4.3 read with the matching-field tables.** Because only the three process indicators are amendable, the business content that T2S matches on cannot be changed by amendment. The reviewed matching evidence lists these as **mandatory** matching fields for both DVP/DWP and FOP: Payment Type, Securities Movement Type, ISIN Code, Trade Date, Settlement Quantity, Intended Settlement Date, Delivering Party BIC, Receiving Party BIC, CSD of the Delivering Party and CSD of the Receiving Party — plus Currency, Settlement Amount and Credit/Debit for DVP/DWP; **additional** fields include the Opt-out ISO transaction condition indicator and the CUM/EX Indicator (and Currency, Settlement Amount and Credit/Debit for FOP); **optional** fields include Common Trade Reference, the client of the delivering and of the receiving CSD participant, and the securities accounts of the delivering and receiving parties. [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2, PDF pages 267–271, Diagrams 55–57 and footnote 194; reviewed 13 September 2026. Two limitations travel with this list: it is a **functional matrix only, with no production XML/XSD validation or local interface certification**, and the diagram headers read **DVP/DWP** while the surrounding paragraph mentions DVP/PFOD — these labels must not be silently normalised into a certified schema mapping. Changing any such field means a cancel-and-reinstruct, not an amendment.

**Unresolved requirement — the cancellation half of that route.** The UDFS section "Instruction Cancellation" is referenced from the excerpts but is **not in this bundle**, so the conditions for cancelling an instruction that has already matched — in particular whether both counterparties must instruct the cancellation, and the effect on the pending part of a partially settled instruction — are **not in reviewed evidence**. Do not assume the cancellation is unilateral. The reviewed matching excerpt establishes only that T2S automatically cancels Settlement Instructions that **remain unmatched** after a certain period of time. [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3, PDF page 271; reviewed 13 September 2026.

---

## 2. The partially settled instruction

**Documented requirement — Priority only.** "Additionally, for partially settled instructions, T2S Actors are only allowed to amend the 'Priority' of the unsettled part of the partially settled Settlement Instruction or Settlement Restriction." [[t2s-amendment]] T2S UDFS R2026.JUN, §1.6.1.4.3, PDF page 279; reviewed 14 September 2026. Table 59 confirms it: for a Partially Settled Instruction, Partial Settlement Indicator = NO, Linkages Block = NO, Priority = YES [[t2s-amendment]] Table 59, PDF page 280. And the third denial condition makes the consequence explicit: an Amendment Instruction against a partially settled instruction referring to any process indicator other than "Priority" is **denied** [[t2s-amendment]] §1.6.1.4.2, PDF page 278.

**Reasoned inference on a textual tension in the source, so you can read it correctly.** The overview sentence on PDF 278 says T2S Actors "are not able to amend other instruction types than Settlement Instructions or Settlement Restrictions, including the pending part of a partially settled Settlement Instruction or Settlement Restriction (i.e. Realignment instructions cannot be amended by T2S Actors)". Read in isolation that sentence sounds like a total bar on the pending part; read with §1.6.1.4.3, Table 59 and the third denial condition — all three of which expressly permit "Priority" on the unsettled part — the operative rule is the narrow one: Priority yes, everything else no. I state this as my reading of the excerpt, not as a separate documented rule, and a production specification should have it confirmed against the full §1.6.1.4 text.

**Practical consequence — Reasoned inference.** The Partial Settlement Indicator and threshold type must therefore be right **before** the instruction partially settles; once a partial settlement has occurred you can no longer switch partial settlement on or off, change the threshold type, or change linkages for the remaining quantity. Only re-prioritising the unsettled part remains. Derived from §1.6.1.4.3 and Table 59 in [[t2s-amendment]].

### When partial settlement happens at all (so you know what you are amending into)

**Documented requirement.** A Settlement Instruction is partially settled where there are insufficient securities to settle the full quantity, provided that the partial settlement window is currently running, the instructions are eligible to settle partially, and the partial settlement threshold criteria are fulfilled. Footnote 224: partial settlement is triggered **only in case of lack of securities** (lack of securities alone, or lack of securities and cash) — **not in case of lack of cash only**. [[t2s-partial-settlement]] T2S UDFS R2026.JUN, §1.6.1.9.3, PDF page 343 with footnote 224; reviewed 14 September 2026.

**Documented requirement — eligibility.** A matched pair is eligible when the instructions are related to Free Of Payment, Delivery Versus Payment or Delivery With Payment; the partial settlement indicator is not set to "No" in any of the Settlement Instructions; and they are **not linked** to any other Settlement Instruction or Settlement Restriction by the T2S parties by a link type "Before", "After", "With" or by a pool reference. Footnote 227 includes instructions on Party Hold that have been partially released. [[t2s-partial-settlement]] §1.6.1.9.3, PDF page 343; reviewed 14 September 2026.

**Documented requirement — thresholds.** Partial settlement is conditioned by thresholds determined in T2S when the settlement occurs, on the basis of the instruction type (FOP, DVP or DWP), the instruction threshold type, the underlying ISIN and the currency of the cash amount. Thresholds are either in "quantity" or in "cash value". Per Table 68: for FOP the applicable threshold type is quantity (minimum settlement unit is used only for the first partial settlement, together with the settlement unit multiple); for DVP/DWP with threshold type set to "Quantity" on both matched instructions the resulting type is quantity; for DVP/DWP not set to "Quantity" on both, the resulting type is cash value, for unit-quoted and for nominal-quoted ISINs alike. Footnote 228: cash-value thresholds are not considered for FOP regardless of the partial settlement threshold type defined in the instruction, including FOP instructions related to a foreign-currency transaction. [[t2s-partial-settlement]] §1.6.1.9.3 with Table 68 and footnote 228, PDF pages 344–345; reviewed 14 September 2026. **LIMITATION carried with this claim: the cash-value thresholds are configured per currency by the T2S Operator and the actual values are not in this excerpt** — I do not state any threshold value.

**Documented requirement — order of attempts.** Settlement Instructions are submitted to a full settlement attempt before a partial settlement attempt; if the instruction does not settle it goes to the Optimising application process, and only if optimisation finds no full-settlement solution does T2S try partial settlement, provided the conditions are met. Footnote 229: Partially Released Settlement Instructions are only submitted to partial settlement attempts for the released quantity. [[t2s-partial-settlement]] §1.6.1.9.3, PDF page 345 with footnote 229; reviewed 14 September 2026.

**Documented requirement — partial release, a different lever from amendment.** A Settlement Instruction on Party Hold may be **partially released** to allow partial settlement of a specified quantity, and must meet all the ordinary partial settlement conditions. During the real-time period, partial settlement of a Partially Released Settlement Instruction can occur outside a partial settlement window for the **total** partially released quantity, and during a window for the total or part of it, until the relevant cut-off time — partial release is valid only for the current business day, at which point the partial release is cancelled and the underlying Settlement Instruction is set back on Party Hold for the full unsettled quantity. For partial release to be considered during sequence C2SX of night-time settlement, the partial release must occur as of the start of day. [[t2s-partial-settlement]] §1.6.1.9.3, PDF pages 343–344 with footnotes 225–227; reviewed 14 September 2026.

**Unresolved requirement — the partial settlement window schedule.** Footnote 226 of the same section refers the schedule of the partial settlement window to the UDFS "Settlement Day" section, which is **not in this bundle**. The window times and the relevant cut-off time referred to above are therefore **not in reviewed evidence** and I state none. Nominal T2S times would in any case be baseline values, not a participant deadline, and a specific business date would need its own dated overlay.

---

## 3. Why "Settled" is an absolute bar

**Documented requirement.** The posting application process checks whether settlement can be achieved considering eligibility and available resources, and "when the check is satisfactory, the posting application process updates the cash balance, securities position and limit headroom, **resulting in the irrevocability of the settlement**". [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1, PDF pages 303–304; reviewed 13 September 2026. **Reasoned inference:** this is the substance behind the first denial condition — there is nothing left to amend on the settled quantity, only on a pending part, and only its Priority. Matching is not that moment: matching is agreement on the settlement terms between deliverer and receiver [[t2s-matching]] §1.6.1.2.1, PDF page 267; reviewed 13 September 2026, whereas posting is the transfer.

---

## 4. Summary table

| Question | Answer | Label |
|---|---|---|
| Amendable after matching | Partial Settlement Indicator + threshold type; Priority; Linkages Block | Documented requirement [[t2s-amendment]] §1.6.1.4.3, PDF 279 |
| Amendable on a Settlement Restriction | Priority; Linkages Block | Documented requirement [[t2s-amendment]] Table 59, PDF 280 |
| Amendable once partially settled | Priority of the unsettled part only | Documented requirement [[t2s-amendment]] §1.6.1.4.3 and Table 59, PDF 279–280 |
| Number of indicators per Amendment Instruction | One; a second needs a new Amendment Instruction | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 279 |
| Any other field | Cancel the referenced instruction and instruct it again | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 279 |
| Both legs at once | Only for instructions that entered T2S already matched, using the T2S Actor Reference; marked X for instructions matched in T2S | Documented requirement [[t2s-amendment]] Table 58, PDF 278–279 |
| Amending a Realignment instruction | Not possible for T2S Actors | Documented requirement [[t2s-amendment]] §1.6.1.4.2, PDF 278 |
| Conditions to cancel a matched instruction | Not in reviewed evidence (UDFS "Instruction Cancellation" not retrieved) | Unresolved requirement |
| Partial settlement window times and cut-off | Not in reviewed evidence (UDFS "Settlement Day" not retrieved) | Unresolved requirement |
| Threshold values | Not in reviewed evidence; configured per currency by the T2S Operator | Unresolved requirement |
| Local interface message, field and version to carry the amendment | Not in reviewed evidence | Unresolved requirement |

No claim above is a validated, certified or production-ready mapping; all of it is the T2S-native functional layer for R2026.JUN.

---

## Open items

1. **UDFS "Instruction Cancellation" section** — needed to state the conditions for cancelling a matched instruction (including whether both parties must instruct it) and the treatment of the pending part of a partially settled instruction. Route: retrieve the cancellation topic from the library; the underlying document is the public T2S UDFS R2026.JUN on the ECB's T2S professional-use documents pages.
2. **UDFS "Settlement Day" section** — needed for the partial settlement window schedule and the relevant cut-off referred to in footnote 226, and for anything time-related. Any dated answer would additionally need a reviewed overlay for the specific business date and currency.
3. **Partial settlement threshold values** — configured per T2S settlement currency by the T2S Operator in Static Data (and per ISIN for the quantity threshold by the actor administering that ISIN). Route: T2S Static Data for the currency and ISIN concerned; not derivable from this excerpt.
4. **Your local CSD interface specification** — this answer is T2S-native. The message, version and field by which your CSD accepts an Amendment Instruction, the references it expects, and any local entitlement are not in reviewed evidence; route is your CSD's client documentation service (for example the client platform of Euronext Securities Milan, Copenhagen or Porto) and, for T2S-native usage rules, an account-based MyStandards access, which the library does not admit field by field.
5. **Business Validation rules** — the amendment acceptance path depends on the UDFS Business Validation section, which is referenced in the excerpt but not retrieved here.
