# "It matched in T2S so it's done" — is that right?

## Direct answer

**No.** Matching and settlement are two different application processes in T2S. Matching only establishes that the deliverer's and the receiver's instructions **agree on the settlement terms**; the transfer itself happens in the **posting** process, which first checks eligibility and available resources and only then updates the cash balance, securities position and limit headroom — and it is that update, not the match, that the reviewed text ties to irrevocability. A matched instruction with no securities or no cash has not moved anything.

*(Matching — the comparison of the two sides' instruction details. Posting — the T2S process that actually books the movement. Allegement — a notice to a counterparty that an instruction is waiting to be matched against it.)*

## Retrieval status (disclosure)

One retrieval, context `{T2S, settlement, participant, current, matching_concept}` as of 13 September 2026, status **evidence_only**. No blocked, needs_context or needs_refresh status arose, so nothing is being withheld from you on that account. Both sections are reviewed as of **13 September 2026** and describe platform release **R2026.JUN**.

## Documented requirements

**1. What matching is.** "T2S Matching process compares the settlement details of Settlement Instructions provided by the deliverer and the receiver of securities to ensure that both parties agree on the settlement terms of the transaction in a standardised way, according to the T2S rules", which are compliant with the ECSDA and ESF matching proposals — [[t2s-matching]] T2S User Detailed Functional Specifications R2026.JUN, §1.6.1.2.1, PDF 267; version R2026.JUN; reviewed 13 September 2026; English body text, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification. **Documented requirement.** Nothing in this definition concerns securities or cash moving.

**2. What you actually receive when it matches.** After successful matching of both instructions, T2S Actors receive a **Status Advice** message containing the T2S Matching Reference assigned to both instructions, plus the T2S Reference and Account Owner Reference of the counterparty's instruction — [[t2s-matching]] §1.6.1.2.3, PDF 271; reviewed 13 September 2026. **Documented requirement.** So the artefact your ops team is reading is a status advice about agreement of terms, not a confirmation of booking.

**3. What settlement requires.** "The posting application process checks if the settlement of Settlement Instructions, Settlement Restrictions and Liquidity Transfers can be achieved considering their **eligibility to settlement and the available resources**." It may resort to the optimising process if needed. "When the check is satisfactory, the posting application process updates the cash balance, securities position and limit headroom, **resulting in the irrevocability of the settlement**" — [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1, PDF 303–304; version R2026.JUN; reviewed 13 September 2026; English body text, no authoritative language independently established; source identity checked, no independent whole-edition supervisory approval certification. **Documented requirement.** Matching is not one of the two conditions named here.

**4. Settlement is attempted on the intended settlement date, not at matching.** Settlement Instructions, Settlement Restrictions and Liquidity Transfers, whether sent by T2S Actors or generated automatically by T2S, "are submitted to the posting application process **at the Intended Settlement Date**" — [[t2s-posting]] §1.6.1.8.2, PDF 303; reviewed 13 September 2026. **Documented requirement.** An instruction matched days before its intended settlement date is simply waiting.

**5. "Matched" is not always something T2S did.** T2S allows CSDs and CSD participants to send **already matched** instructions cross-CSD and intra-CSD; these are created with the matching fields as if they had been matched in T2S — [[t2s-matching]] §1.6.1.2.2, PDF 268; reviewed 13 September 2026. **Documented requirement.** A "Matched" status can therefore be an input attribute rather than evidence that two independent parties agreed inside T2S.

**6. Several instruction types never get a match status at all.** Settlement Restrictions, Maintenance instructions, **Realignment instructions**, Auto-collateralisation instructions, Reimbursement auto-collateralisation instructions and Liquidity transfers do not go through the T2S matching process; cancellation instruction matching follows different rules — [[t2s-matching]] §1.6.1.2.2, PDF 268; reviewed 13 September 2026. **Documented requirement.** For anything in that list, "it matched" is not even a meaningful checkpoint.

**7. A match can bind you to the other side's amount.** If all matching fields agree except the Settlement Amount, T2S checks the difference against the configured tolerance; where instructions with different Settlement Amounts are matched, the amount submitted for settlement is **the amount indicated by the deliverer of the securities**. Among several candidates T2S picks the smallest amount difference, then the closest entry time. For EUR the reviewed tolerance is EUR 2 for a cash countervalue at or below EUR 100,000 and EUR 25 above it, configured by the T2S Operator — [[t2s-matching]] §1.6.1.2.3 and Table 57, PDF 270–271; reviewed 13 September 2026. **Documented requirement**, with the LIMITATIONS carried: this is a **functional matrix only, with no production XML/XSD validation and no local interface certification**; the tolerance is a **currency-specific** configuration and the EUR bands must not be generalised to other currencies; and the retained diagram labels read DVP/DWP while the narrative paragraph mentions DVP/PFOD — these labels must not be silently normalised into a certified schema mapping.

**8. Not matching has its own consequences.** If an instruction does not match at the first attempt, T2S sends a Settlement Allegement to the counterparty after waiting a certain period, and T2S automatically cancels instructions that remain unmatched after a certain period — [[t2s-matching]] §1.6.1.2.3, PDF 271; reviewed 13 September 2026. **Documented requirement.** The two "certain periods" are not quantified in the retrieved excerpt and I will not supply numbers for them.

## What your ops team is half-right about

**Reasoned inference (derived from items 1, 2 and 3 above).** "Matched" is a genuine milestone: the economic terms are no longer in dispute between the two sides, and from that point the open risks are operational (eligibility, resources, date) rather than instructional. What it does not tell you is whether the securities and cash actually moved. A defensible ops rule is therefore: *matched = agreed; posted = done*.

**Unresolved requirement.** The retrieved excerpt does **not** state what matching does to your ability to cancel unilaterally; §1.6.1.2.2 points to a separate "Instruction Cancellation" section that was not retrieved. So I cannot confirm from this bundle the common belief that a matched instruction can only be cancelled bilaterally — that is **not in reviewed evidence** here.

**Unresolved requirement.** What happens to a **matched** instruction that fails the posting check (recycling, retry, end-of-day cancellation) is **not in reviewed evidence**: the matching section references "Instructions Recycling" and the posting section references "Optimising", and neither was retrieved. The automatic cancellation documented in item 8 applies to instructions that remain **unmatched**, and must not be read as the rule for matched-but-unsettled instructions.

**Unresolved requirement.** For a cross-CSD chain, whether the business instruction settling implies the associated realignment movements are complete is **not in reviewed evidence** — realignment instructions are only mentioned here as a type that bypasses matching (item 6); the realignment mechanism itself was not retrieved.

**Proposed design choice (your decision, not a platform rule).** If your monitoring currently closes an item on the match status advice, change the completion criterion to the posting outcome on the intended settlement date, and keep matched-but-unsettled instructions in an open queue with the intended settlement date as the ageing key. That is an implementation decision for your ops tooling; the reviewed evidence supports the distinction, not any particular queue design.

## Open items

1. **Instruction Cancellation (T2S UDFS R2026.JUN, section referenced at page marker [280])** — needed to state the cancellation consequences of matching; not retrieved in this bundle.
2. **Instructions Recycling (referenced at page marker [296]) and Optimising (referenced at page marker [335])** — needed to state what happens to a matched instruction that cannot settle for lack of resources; not retrieved.
3. **Status Management (referenced at page marker [653]) and Message subscription (referenced at page marker [135])** — needed if you want the exact status values and the subscription behaviour behind what your ops screens display; not retrieved.
4. **Realignment mechanism** — needed before concluding anything about completion of a cross-CSD chain; not retrieved.
5. **Your CSD's local interface** — a T2S UDFS description is not your CSD's client interface specification. Whatever your ops team sees in a local channel (for example a CSD's own portal or message set) is governed by that CSD's client documentation, which is not in this bundle. Official route: the relevant CSD's documentation service or client platform; the T2S UDFS itself is public on the ECB website. I do not contact them on your behalf.

Evidence review date for everything above: **13 September 2026**, platform release R2026.JUN. Time passing since that review does not make these statements "current today"; it makes them reviewed as of that date.
