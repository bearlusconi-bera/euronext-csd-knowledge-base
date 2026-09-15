# T2S recycling periods before automatic cancellation

## Direct answer

**Documented requirement.** Two different periods, both configured by the T2S Operator:

| Pending instruction | Recycling period | Counted from |
|---|---|---|
| **Unmatched** Settlement Instruction | **20 working days** (the current value stated in footnote 199) | the **later** of the Intended Settlement Date and the date of the **last status change** of the instruction; any status value change restarts the count |
| **Matched but unsettled** Settlement Instruction (and Settlement Restrictions) | **60 working days** (the current value stated in footnote 200) | recycled "until its settlement or cancellation occurs"; the end-of-day calculation below uses the same D1 rule |

Both are described in the UDFS as "a period of working days **configured by the T2S Operator**", with 20 and 60 given as the *current* values in footnotes — they are a parameter, not a constant of the system. There is also an external-CSD exception under which an instruction is **never** automatically cancelled.

Source for the whole table: [[t2s-recycling]] T2S User Detailed Functional Specifications R2026.JUN, §1.6.1.7 with footnotes 199–200, PDF 296–299; version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026; English body text, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification. LIMITATIONS carried with the claim: this is a **T2S-native functional description for R2026.JUN — not a local participant interface specification, production XSD or message usage guideline**; and the **external-CSD exception is stated but individual configurations are not certified**.

## Retrieval statuses (disclosure)

Three retrievals, all **evidence_only**: `t2s_recycling_periods` (as of 14 September 2026), `t2s_cancellation_process` (as of 14 September 2026) and `matching_concept` (as of 13 September 2026). No blocked, needs_context or needs_refresh status arose. Review dates are 14 September 2026 for the recycling and cancellation sections and 13 September 2026 for the matching and posting sections; all four describe platform release R2026.JUN.

## The supporting detail

**Documented requirement — what a recycling period is.** At each end of a Settlement Day, T2S recycles pending instructions for "a period of time known as recycling period, which is defined as the number of **working days** a pending instruction can remain in T2S, before being cancelled by the system". Recycling triggers the revalidation process at Start of Day, and the Instruction Recycling process manages the automatic cancellation of all pending instructions that have exceeded their recycling period — [[t2s-recycling]] §1.6.1.7.1–1.6.1.7.2, PDF 296; reviewed 14 September 2026.

**Documented requirement — the unmatched clock can be reset.** Unmatched Settlement Instructions are recycled starting from the Intended Settlement Date or the date of the last status change, whichever is later, and "**any status value change** is considered for restarting the count of the number of days for the recycling period"; the UDFS gives a change of Party Hold status from "Yes" to "No" as an example of a status change — [[t2s-recycling]] §1.6.1.7.3, PDF 297; reviewed 14 September 2026. Operationally this is the trap in "how many days do I have": touching an unmatched instruction can restart its 20-working-day window.

**Documented requirement — a third, separate period.** Unmatched **Cancellation Instructions** that need to be matched in T2S are recycled for a period of working days configured by the T2S Operator, starting from their reception in T2S until matching occurs — [[t2s-recycling]] §1.6.1.7.3, PDF 297; reviewed 14 September 2026. **Unresolved requirement:** the reviewed excerpt gives **no numeric value** for this third period (footnotes 199 and 200 cover unmatched settlement instructions and matched instructions only) — the number is **not in reviewed evidence**.

**Documented requirement — how the cut is computed.** At the End of Day process T2S cancels all instructions that have reached their recycling period. The period "is considered as reached when: The difference between 'D1' (latest date between the ISD and the business day of the last status change of the instruction) and 'D2' (current business date) equals the number of business days defined for the applicable recycling period." Once reached, T2S stops recycling and cancels automatically; "nevertheless, until the EoD the instruction is still processed as normal throughout the whole business day" — [[t2s-recycling]] §1.6.1.7.3, PDF 299; reviewed 14 September 2026. So an instruction on its final day can still settle normally that day.

**Documented requirement — you are told only at the end.** T2S does **not** send a daily message about the result of the recycling process; only when an instruction exceeds its recycling period does T2S cancel it and send a message with the corresponding reason code(s); interested parties may also be informed according to their message subscription preferences — [[t2s-recycling]] §1.6.1.7.3, PDF 299; reviewed 14 September 2026. **Unresolved requirement:** the reason codes themselves are **not in reviewed evidence** and must not be guessed.

**Documented requirement — the exception where nothing is cancelled.** In an external-CSD scenario, instructions meeting **all** of the following remain pending and are recycled for an **indefinite** period until one of the conditions ceases to hold or a T2S Actor cancels them: (i) any of the relevant CSDs is external to T2S; (ii) the external CSD is the issuer of the security; and (iii) the external CSD is configured as **not compliant** with the T2S automatic cancellation of instructions — [[t2s-recycling]] §1.6.1.7.3, PDF 298; reviewed 14 September 2026. LIMITATION carried: the exception is stated, but **individual CSD configurations are not certified** in reviewed evidence, so whether a specific external CSD is flagged non-compliant cannot be answered from this bundle.

**Documented requirement — automatic cancellation is not only about recycling.** T2S automatically cancels pending instructions when they exceed their recycling period, and also: when the realignment chain cannot be built; when instructions do not pass the revalidation process (triggered at Start of Day and by a reference-data change affecting the instruction); and, where Start-of-Day revalidation finds the realignment chain invalid for the current settlement day, a new valid chain can be built but the transaction is already partially settled — [[t2s-cancellation]] T2S UDFS R2026.JUN, §1.6.1.5.3 "Cancellation by the system", PDF 284; version R2026.JUN; section reviewed 14 September 2026, source reviewed 13 September 2026. LIMITATIONS carried: **T2S-native functional description for R2026.JUN, not a local participant interface specification, production XSD or message usage guideline**; and **local legal effects of cancellation (for example Milan Article 70) are separate sections at their own review date** — none of those local sections is in this bundle. Practical consequence: a matched instruction can disappear well before day 60.

**Documented requirement — the two periods sit either side of a different rule.** Once an instruction is matched, T2S requires **bilateral cancellation**: cancellation is only possible if both counterparties send their cancellation instructions for each leg separately, or if an authorised T2S Party sends one cancellation instruction carrying the information of both legs; an unmatched instruction's cancellation is executed or denied immediately after validation — [[t2s-cancellation]] §1.6.1.5.3, PDF 282 with Table 60 (PDF 283) and footnote 195; reviewed 14 September 2026. And the matching section states plainly that T2S automatically cancels instructions that remain unmatched after a certain period, after first sending a Settlement Allegement to the counterparty — [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3, PDF 271; reviewed 13 September 2026 (LIMITATION: functional matrix only; no production XML/XSD validation or local interface certification).

**Documented requirement — why "matched but unsettled" exists at all.** The posting application process checks whether settlement can be achieved "considering their eligibility to settlement and the available resources", and instructions are submitted to posting at the Intended Settlement Date — [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1–1.6.1.8.2, PDF 303–304; reviewed 13 September 2026. A matched instruction that lacks securities or cash simply keeps being recycled until it settles, is cancelled, or hits the matched-instruction period.

## Reasoned inference and what it does not cover

**Reasoned inference (derived from §1.6.1.7.3 and footnotes 199–200).** Because both periods are T2S Operator parameters and the footnotes describe the *current* values, 20 and 60 working days should be treated as the values documented in the R2026.JUN UDFS at the 14 September 2026 review date, not as permanent constants. If a number matters contractually, confirm the operator configuration for the business date in question.

**Reasoned inference (derived from the definition of the period in working/business days).** "Working days" is counted on the applicable settlement-day calendar, which the UDFS cross-references to its Settlement Day section — that section was **not retrieved**, so the exact calendar and any market-specific closing days behind the count are **not in reviewed evidence**.

**Unresolved requirement.** Whether your CSD applies any earlier local cancellation, hold or housekeeping rule ahead of the T2S period is **not in reviewed evidence**: no CSD rulebook section was retrieved for this question, and a T2S-native description is not a local interface or local legal statement.

**Proposed design choice (yours, not a platform rule).** If you build ageing alerts, key them on D1 (the later of ISD and the last status change) rather than on instruction creation, and raise the alert several working days before the applicable period expires, since T2S sends no daily recycling message. Choose your own lead time; the evidence supports the D1 basis, not any particular alert threshold.

## Open items

1. **Numeric value of the recycling period for unmatched Cancellation Instructions** — referenced in §1.6.1.7.3 but not quantified in the reviewed excerpt.
2. **Reason codes** accompanying the automatic-cancellation message — not in reviewed evidence; the excerpt points to Status Management (page marker [653]) and Message subscription (page marker [135]), neither retrieved.
3. **Settlement Day / calendar section** (page marker [155]) — needed to convert "working days" into concrete dates for a given market.
4. **Business Validation (page marker [218]) and Realignment (page marker [373])** — needed to assess the non-recycling automatic-cancellation triggers listed in [[t2s-cancellation]].
5. **External-CSD configuration** — whether a given external issuer CSD is configured as not compliant with automatic cancellation is a per-CSD configuration that reviewed evidence does not certify.
6. **Local CSD overlay** — for Milan, Copenhagen, Porto, Athens or Oslo specifics, the relevant rulebook and instructions sections at their own review dates are needed; official route is the CSD's public documentation hub or its client platform for entitlement-restricted material. I do not contact them on your behalf.

All values above are stated as reviewed on **14 September 2026** (recycling and cancellation) and **13 September 2026** (matching and posting), for platform release **R2026.JUN**.
