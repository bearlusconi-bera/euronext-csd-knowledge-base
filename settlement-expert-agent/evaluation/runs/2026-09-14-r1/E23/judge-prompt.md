You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
I want to swap an asset with my counterparty in Milan. What is the flow?

# Case category: ambiguity (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "Ask what 'swap' means: sale against cash (DvP), free-of-payment transfer, or exchange of two securities.",
  "Conditional outline for each; two-security atomicity unsupported.",
  "Milan-specific flow via X-TRM for ICPs."
]
Fail conditions (must NOT appear):
[
  "Assume one meaning silently.",
  "Confirm atomicity of a two-security exchange."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked', 'evidence_only']

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
# "Swapping an asset with a counterparty in Milan" — which flow applies

## Direct answer

"Swap" is ambiguous and the answer differs completely by reading, so I cannot give you one flow until you tell me which of these you mean: **(a) a sale against cash** (delivery versus payment, DVP), **(b) a free-of-payment transfer** (FOP — securities move, no cash leg in the system), or **(c) a two-security exchange** (your security against the counterparty's security, sometimes called a security-for-security swap). For readings (a) and (b) the reviewed evidence documents the Monte Titoli / T2S flow end to end: acquisition and validation (entry, SF1) → matching (irrevocability, SF2) → posting (transfer and finality, SF3), plus automatically generated realignment if the two of you are participants of different CSDs. For reading (c) **the retrieval was blocked** and there is no reviewed evidence that an arbitrary two-security exchange settles atomically — do not assume it does.

## Retrieval statuses (disclosure)

| # | Context | Status |
|---|---|---|
| 1 | T2S / settlement / current — securities swap atomicity | **blocked** — "Two-security structure, actual eligible links and supported instruction linkage require separate evidence." GAP IDS `['G04']` |
| 2 | Milan / settlement / current — realignment mechanism | evidence_only |
| 3 | Milan / settlement / current — linked instructions | evidence_only |
| 4 | Milan / settlement / current — finality | evidence_only |
| 5 | Milan / settlement / current — instruction processing rules | evidence_only |

Because of retrieval 1, **reading (c) is an unresolved requirement**: the two-security structure, the actual eligible links and the supported instruction linkage are not established by reviewed evidence (gap G04). Nothing below fills that gap.

## Step 0 — Resolve the ambiguity first

**Documented requirement.** Monte Titoli's Settlement Service acquires settlement instructions for "individual transactions (DVP or FOP)", for bilateral netting of securities and cash balances, and for securities and cash balances netted via interposition of a central counterparty. [[milan-instruction-processing]] Monte Titoli Regulations as of 26 January 2026, Article 68(1), PDF 49–50 (printed 48–49); reviewed 14 September 2026 (2026-09-14); **English translation, the Italian text prevails** (cover, PDF 1); source identity checked, no independent whole-edition supervisory approval certification.

**Documented requirement.** At T2S level the reviewed matching matrix carries exactly two transaction headers, verbatim "DVP/DWP" and "FOP"; the accompanying paragraph separately mentions DVP/PFOD. [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2 and visually checked Diagrams 55–57, PDF 267–271; reviewed 13 September 2026; platform release R2026.JUN; English, authoritative language not independently established. LIMITATION carried with this: "Functional matrix only; no production XML/XSD validation or local interface certification" and "Retain diagram DVP/DWP labels" — the labels must not be silently normalised into a certified schema mapping.

**Reasoned inference**, derived from the two points above: the reviewed evidence recognises a cash-against-securities leg (DVP) and a securities-only leg (FOP). It contains **no** transaction type for "one security against another security". That is why reading (c) has to be constructed out of two separate instruction pairs, and why its atomicity is not documented.

## The documented flow for reading (a) sale against cash, or (b) FOP transfer

Assumption stated openly (not evidence): both of you are Monte Titoli participants instructing for settlement in T2S. If the counterparty is in another CSD, add step 5.

1. **Acquisition and validation.** During acquisition the Settlement Service checks the completeness and formal correctness of the instruction, and the consistency of the instruction data with personal data found in T2S (common static data) as well as with any restrictions, including the match of the financial instruments involved with Article 86. Validated instructions are forwarded to the subsequent phases; non-validated instructions are rejected; participants are informed of the validation result. Participants may also specify linked settlement, conditional settlement outside T2S (CoSD), partial settlement within T2S limits, and instruction priority within T2S limits — noting that Monte Titoli assigns priority first to instructions with the Italian Ministry of Finance as counterparty, monetary-policy transactions and Bank of Italy collateral transfers, then those from Market Management Companies. *Documented requirement.* [[milan-instruction-processing]] Article 68(2)–(6), PDF 49–50 (printed 48–49); reviewed 14 September 2026; English translation, Italian text prevails.
2. **Entry into the system (SF1).** Settlement instructions are deemed "entered" into the Settlement System pursuant to Article 2(2) of Legislative Decree 210/2001 from the moment the validation time in T2S ends. *Documented requirement.* [[milan-finality]] Monte Titoli Regulations as of 26 January 2026, Article 72(1), PDF 50–51 (printed 49–50); reviewed 13 September 2026 (2026-09-13); English translation, **Italian text prevails**; no insolvency runbook or legal opinion admitted, and the remainder of Article 72 was not reviewed.
3. **Matching (SF2).** Matching checks that the information corresponds to the instructions entered; it covers mandatory matching fields and may also cover non-mandatory ones. T2S gives participants complete disclosure of instruction status and of the counterparty's instruction awaiting matching (*allegement* — a notice to a counterparty that an instruction is waiting to be matched against it). Unmatched instructions may be changed by participants only as regards status indicators. *Documented requirement.* [[milan-finality]] Article 69, PDF 50–51; reviewed 13 September 2026; English translation, Italian text prevails.
   At T2S level, mandatory matching-field values must be the same on both sides **except** Settlement Amount for DVP/PFOD (where a tolerance may apply) and Credit/Debit and Securities Movement Type (Deliver/Receive), which match opposite. The mandatory fields in the reviewed matrix are Payment Type, Securities Movement Type, ISIN Code, Trade Date, Settlement Quantity, Intended Settlement Date, Delivering Party BIC, Receiving Party BIC, CSD of the Delivering Party and CSD of the Receiving Party for both DVP/DWP and FOP, plus Currency, Settlement Amount and Credit/Debit for DVP/DWP only (for FOP those three are *additional* fields). Additional fields must match when either side fills them; optional fields may match filled against blank. The EUR tolerance is EUR 2 for a cash countervalue up to EUR 100,000 and EUR 25 above it; upper- and lower-case letters count as different when values are compared. *Documented requirement.* [[t2s-matching]] T2S UDFS R2026.JUN, §1.6.1.2.3 with footnote 194 and Diagrams 55–57, PDF 267–271; reviewed 13 September 2026; platform release R2026.JUN; functional matrix only, not a production schema or local interface mapping.
   **Matched is not settled.** From the time of matching in T2S the instruction cannot be revoked by a participant or a third party (SF2) — but this is expressly "without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70(2)", i.e. matched instructions can still be cancelled bilaterally with both participants' consent (or by a mandated agent). Before matching, a participant may cancel unilaterally unless the instruction was entered as non-changeable; a participant may also hold and later release its instructions on the same condition. *Documented requirement.* [[milan-finality]] Articles 70(1)–(3), 71 and 72(2), PDF 50–51; reviewed 13 September 2026; English translation, Italian text prevails.
4. **Posting (SF3) — the actual transfer.** The posting application process checks whether settlement can be achieved considering eligibility and available resources; instructions are submitted to posting at the Intended Settlement Date; when the check is satisfactory, posting updates the cash balance, securities position and limit headroom, "resulting in the irrevocability of the settlement". *Documented requirement.* [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1 and first overview paragraph of §1.6.1.8.2, PDF 303–304; reviewed 13 September 2026; platform release R2026.JUN.
   In Milan's own legal terms, the transfer of securities and cash becomes final from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for (SF3) — so for your FOP reading (b), the securities debit is the finality moment. *Documented requirement.* [[milan-finality]] Article 72(3), PDF 50–51, with the section LIMITATION "SF3 is the relevant cash debit or securities debit for FoP"; reviewed 13 September 2026; English translation, Italian text prevails.
   Around posting, Monte Titoli's Regulations add: the settlement process has a night-time phase and a day-time phase, both gross; each phase settles newly entered eligible instructions (in real time during the day-time phase) plus those unsettled from the previous phase; capacity checks may be made on a net balance where instructions are handled jointly for optimisation, with collateralisation checked for a cash shortfall and partial settlement for a securities shortfall; instructions unsettled for lack of securities or cash are re-proposed in the subsequent phase of the same settlement day or on the following day until settled or cancelled under Article 70, and re-proposed instructions may be changed only as to status indicators unless entered as non-changeable. *Documented requirement.* [[milan-instruction-processing]] Articles 74–75, PDF 52–53 (printed 51–52); reviewed 14 September 2026; English translation, Italian text prevails.
5. **Realignment — only if you and the counterparty are in different CSDs.** Once instructions are matched (or validated, for already-matched incoming instructions), the realignment process automatically creates the required instructions between the involved CSDs, based on the cross-CSD links set by CSDs in reference data, with no further action from the actors; the generated instructions are linked to the underlying business instructions by two INFO links for information purposes, and **T2S ensures that the generated realignment instructions and their business instructions settle on an all-or-none basis**. Whether a CSD is issuer CSD or investor CSD is defined per security and relationship, and a CSD can be both. *Documented requirement.* [[t2s-realignment]] T2S UDFS R2026.JUN, §1.6.1.10.1–1.6.1.10.3, PDF 373–376; reviewed 13 September 2026; platform release R2026.JUN. Its LIMITATION lines travel with this: "Actual links/accounts and ISIN eligibility require verification" and "Does not establish atomicity of an arbitrary two-security swap or describe every action outside T2S". Note also that generated realignment instructions are instructions, not completed ledger movements — the movement is the posting in step 4.

## Reading (c), the two-security exchange: what can and cannot be said

- **Unresolved requirement.** There is no reviewed evidence that an arbitrary exchange of one security against another settles atomically in Milan/T2S. The dedicated retrieval is blocked under gap **G04**, and the realignment section explicitly does not establish such atomicity. The all-or-none property documented above attaches to a business instruction together with its own T2S-generated realignment chain — it is not a statement about two independent business instructions in two different ISINs.
- **Documented requirement, as far as it goes.** T2S does provide actor-specified links: a T2S Actor links instructions using a processing position code — INFO (information only, no processing), BEFO (settle before or at least at the same time), AFTE (settle after or at least at the same time), **WITH (all-or-none: settled at the same time as the linked instruction)** — and/or a Pool Reference. Instructions may be linked whatever the type (delivery/receipt), the ISIN code or the Intended Settlement Date, provided the links do not contradict each other. To create a link the actor sends the instruction with the processing position code and the reference of the linked instruction (T2S Instruction Reference or T2S Actor Instruction Reference); if the actor reference is used, the Reference Owner BIC of the linked instruction is also required, and without it T2S does not create the link and rejects the instruction. Changing a link requires first an amendment with linkage type UNLK and the same processing position code, then a second amendment with linkage type LINK and the new code. A liquidity transfer cannot be linked to an instruction or restriction, and a T2S internally generated instruction cannot be linked by an actor. [[t2s-linked-instructions]] T2S UDFS R2026.JUN, §1.6.1.11.1–1.6.1.11.3 with footnote 243, PDF 442–444; reviewed 14 September 2026; platform release R2026.JUN. LIMITATIONs carried with it: "Table 71 validation rules for links (PDF 448) are not admitted" and "T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline".
- **Proposed design choice (yours to make and to verify, not an infrastructure rule):** construct the exchange as two DVP or FOP instruction pairs — one per ISIN, in opposite directions — linked with WITH so that they are submitted for settlement at the same time. This is the closest supported construct in the reviewed evidence, but it is a design choice, not a documented guarantee: the link validation rules that would tell you when such a link is accepted (Table 71) are **not** in reviewed evidence, the blocked retrieval G04 covers exactly this structure, and nothing reviewed states the legal consequence in Milan if one leg of such a pair fails.
- **Proposed design choice / alternative to consider:** Monte Titoli's Regulations allow a settlement instruction to be connected to the settlement of linked instructions, or made conditional on events outside T2S (CoSD — conditional securities delivery, where final posting depends on an action or event external to T2S confirmed by an administering party). [[milan-instruction-processing]] Article 68(4), PDF 49–50; reviewed 14 September 2026; English translation, Italian text prevails. The reviewed text establishes that these possibilities exist; it does not specify how to configure them for a two-security exchange.

## What I am not telling you, deliberately

- **No cut-off times, no submission deadlines, no calendar.** None are in this bundle, so none is stated here.
- **No message identifiers, field cardinalities or Milan local-interface (X-TRM) mapping.** The T2S sections are T2S-native functional descriptions and are explicitly not a local participant interface specification; Milan's own client-facing standards were not retrieved for this question.
- **No ISIN, account or link eligibility.** Whether your two instruments and accounts are actually eligible, and which CSD links exist, requires verification per the realignment LIMITATION; until then any cross-CSD flow above is conditional.
- Review dates: 13 September 2026 for [[t2s-matching]], [[t2s-posting]], [[t2s-realignment]] and [[milan-finality]]; 14 September 2026 for [[t2s-linked-instructions]] and [[milan-instruction-processing]]. These are review dates, not a statement that the position is unchanged today.

## Open items

1. **Which swap do you mean?** Sale against cash (DVP), free-of-payment transfer (FOP), or two-security exchange. Everything downstream depends on this; I have given you (a) and (b) as documented and (c) as unresolved.
2. **Two-security exchange atomicity — blocked, gap G04** ("Two-security structure, actual eligible links and supported instruction linkage require separate evidence"). Required sources: the T2S UDFS Table 71 rules applying to linked settlement instructions (PDF 448), currently not admitted in reviewed evidence, plus a Monte Titoli statement on linked-instruction usage. Official route: the ECB T2S documentation pages for the UDFS of the deployed release, and the Euronext Securities Milan documentation hub / MT-X client platform for the Milan side.
3. **Counterparty location and link model.** Tell me whether the counterparty is a Monte Titoli participant (intra-CSD) or a participant of another CSD, whether both CSDs are in T2S, and whether the link is direct — otherwise step 5 stays conditional.
4. **Access model.** ICP (instructing through Monte Titoli) versus DCP (instructing T2S directly) changes which interface and which message set applies. No Milan local interface specification is in this bundle.
5. **Instrument and account eligibility.** ISINs, securities accounts, the intended settlement date and the currency for the cash leg, so that eligibility and the applicable realignment chain can be verified rather than assumed.
6. **Milan legal effect of a failed leg.** No reviewed evidence states what happens under Milan's Regulations if one leg of a linked two-security pair settles and the other does not; Article 72 was reviewed only for paragraphs (1)–(3), and no insolvency runbook or legal opinion is admitted.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T11:54:40.929253+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "current", "question_type": "securities_swap_atomicity"}
STATUS: blocked — Two-security structure, actual eligible links and supported instruction linkage require separate evidence.
GAP IDS: ['G04']

=== RETRIEVAL 2: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "realignment_mechanism"}
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

--- SECTION [[t2s-realignment]] — Realignment generation, CSD roles and all-or-none relationship (reviewed 2026-09-13; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.10; concepts and reference-data requirements; PDF 373–376 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Actual links/accounts and ISIN eligibility require verification.
LIMITATION: Does not establish atomicity of an arbitrary two-security swap or describe every action outside T2S.
EXCERPT (§1.6.1.10; concepts and reference-data requirements; PDF 373–376):
1.6.1.10 Realignment


 2    1.6.1.10.1 Concept

 3   The realignment application process handles the cases of:

 4         l  Cross-CSD settlements, i.e. settlements between T2S Actors of different CSDs, the latter being in T2S;

 5         l  External-CSD settlements, i.e. settlements between T2S Actors of different CSDs, with some of the CSDs
 6        involved in the settlement being external to T2S.

 7    Cross-CSD settlement is achieved in T2S with the simultaneous booking of cash and securities for Settlement
 8    Instructions between participants of different CSDs. Once incoming Settlement Instructions are matched (or
 9    validated for already matched incoming Settlement Instructions), the realignment application process creates
10    automatically all the requested Settlement Instructions between the involved CSDs, referred hereafter as
11   T2S generated realignment Settlement Instructions. This automatic generation relies on links set in the ref-


                                                                                            Page 373 of 2017



[PDF page 374]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1    erence data between the relevant CSDs and does not request from the T2S Actors any other action. It takes
 2    place immediately following either the validation of already matched Settlement Instructions, or the match-
 3    ing of Settlement Instructions matching in T2S.

 4    Realignment application process is also applied for external-CSD settlement.

 5    This section details the parameters required from T2S Actors to manage the realignment in T2S for cross-
 6   CSD and external-CSD settlement. It also details the resulting realignment chain with the description of the
 7   T2S generated realignment Settlement Instructions reported to the involved T2S Actors.

 8    For external-CSD settlement, only the process applying to the Settlement Instructions actually submitted to
 9   T2S is described. All actions required by the realignment but without interaction with T2S are not described.

10                               DIAGRAM 85 - REALIGNMENT APPLICATION PROCESS





11

12    1.6.1.10.2 Overview

13   Upon the matching of Settlement Instructions, or upon the validation of already matched Settlement Instruc-
14    tions, the realignment application process verifies if the incoming business Settlement Instructions are re-
15    quiring realignment Settlement Instructions on securities accounts other than those of the submitting T2S
16    Actors (e.g. on the accounts of the issuer CSD).





                                                                                            Page 374 of 2017



[PDF page 375]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   When the need to realign is identified, the realignment application process creates automatically the T2S
 2    generated realignment Settlement Instructions, based on the cross-CSD links set by CSDs in the reference
 3    data.

 4   The T2S generated realignment Settlement Instructions are then validated, and linked to the initial underly-
 5    ing Settlement Instructions through two links INFO providing the references of both business Settlement
 6    Instructions for information purposes. T2S ensures that the T2S generated realignment Settlement Instruc-
 7    tions and their business Settlement Instructions settle on an all-or-none basis.


 8    1.6.1.10.3 Realignment process

 9   Parametersnecessaryforrealignment

10    Role and links between CSDs for cross-CSD and external-CSD settlement

11    Irrespective of whether it is a cross-CSD or an external-CSD settlement, a CSD is defined for the realignment
12    process as:

13         l  The issuer CSD, when it is the CSD in which the security has been issued and distributed on behalf of
14       the Issuer;

15         l  The investor CSD, when it is the CSD of at least one party of the Settlement Instruction;

16         l  Or both, when it is the CSD in which the security has been issued and the CSD of at least one party of
17       the Settlement Instruction.

18   To manage the cross-CSD and external-CSD settlements, each investor CSD has the choice between:

19         l  Opening an omnibus account (see section below) in the books of the issuer CSD to reflect the holdings
20        of its participants for the securities, or;

21         l  Opening an omnibus account in the books of any other CSD being already an investor CSD for the same
22         financial instrument.

23    In both cases, the CSD where the omnibus account is opened is defined as the technical issuer of the inves-
24    tor CSD for the given securities. For a given ISIN, an investor CSD can define several such investor-type CSD
25     links, meaning that it can define several technical issuer CSDs for a given ISIN. However, one of those links
26    (and only one) should be given the preference for settlement under simple configurations (all CSDs in T2S,
27   no multi-issuance), this is the “default” link. Under more complex configurations (external CSD configuration,
28    multi-issuance), the preference should go first to one of the other “alternative” links, more specifically the
29   one pointing to the counterpart CSD, in case it is set up in the reference data. If T2S cannot find an alterna-
30     tive link to the counterparty CSD or if such an alternative link is found, but unusable due to a missing static
31    data (i.e. invalid or incomplete configuration of CSD Account Links), T2S reverts back to the valid default
32     links should be used also under those complex configurations.

33    Only one link, whether default or alternative, can be set up towards a given technical issuer CSD for a given
34    investor CSD and a given ISIN at the same point in time.

35   The issuer-type CSD link cannot be an alternative link, it has always to be defined as a “default” link. Only
36    investor-type links can be flagged “alternative”. Those links cannot be defined for an investor CSD outside
37   T2S and they cannot point to a technical issuer CSD outside T2S.



                                                                                            Page 375 of 2017



[PDF page 376]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1   To that purpose, CSDs are required to configure the following set-up in the reference data:
 2

               PARAMETERS                                      DEFINITION

        Security CSD links                   Each investor CSD has to define at least one technical issuer CSD per securities
                                                                            it intends to set as eligible for settlement (See section Securities reference data
                                              [ 71]). This results in the creation of one or several links between the investor
                                   CSD and its technical issuer CSD(s) for a given financial instrument.

                                  Among those links, one (and only one) should be flagged “default”, the other
                                         ones being considered “alternative”.

                                      The alternative links can only be set up for T2S-in investor CSDs, pointing to a
                                             T2S-in technical issuer CSD.

                                             For a given investor CSD and a given ISIN, only one link (either default or al-
                                                  ternative) should point to a given technical issuer CSD.

                                             For a given investor CSD, the technical issuer CSD may be different for each
                                                    security. It is in most cases the issuer CSD of the security.

                                      The issuer CSD sets a CSD link with itself as issuer. This link cannot be an al-
                                                 ternative one, it is always a default one.

                                           (See section Configuration of securities accounts for cross-CSD settlement and
                                                external CSD settlement [ 97])

 3    This set-up is used by T2S to derive the realignment chain applicable to matched Settlement Instructions
 4    starting either from both investor CSDs (delivering and receiving) up to the issuer CSD(s) of the traded secu-
 5     rities when default links are used, or from the delivering investor CSD up to the receiving investor CSD (or
 6    vice versa) when alternative links are used.

 7

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "t2s_linked_instructions"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[t2s-linked-instructions]] — Linked instructions: BEFO/AFTE/WITH links, pools and T2S-generated links (reviewed 2026-09-14; modes ['current']; entities ['T2S', 'Milan', 'Copenhagen', 'Porto']; basis reviewed_effective_interval; platform release R2026.JUN)
CITATION: T2S User Detailed Functional Specifications R2026.JUN (UDFS) | §1.6.1.11.1–1.6.1.11.3 with footnote 243; PDF 442–444 | version R2026.JUN | body language en | authoritative language None | not independently established | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.JUN_clean_20260122.en.pdf
LIMITATION: Table 71 validation rules for links (PDF 448) are not admitted.
LIMITATION: T2S-native functional description for R2026.JUN; not a local participant interface specification, production XSD or message usage guideline.
EXCERPT (§1.6.1.11.1–1.6.1.11.3 with footnote 243; PDF 442–444):
1.6.1.11 Linked Instructions


 2    1.6.1.11.1 Concept

 3   T2S provides the functionality to link Settlement Instruction(s) and/or Settlement Restriction(s) together.
 4   The aim is to submit such linked instructions to specific rules during business validation, eligibility or settle-
 5   ment application processes.

 6    Settlement Instructions and Settlement Restrictions can be linked together either via a link specified by a
 7   T2S Actor or via a link generated automatically by T2S.


 8    1.6.1.11.2 Overview

 9    Settlement Instructions linked via an indicator, a Pool Reference specified by a T2S Actor aim to cover the
10    settlement of specific operations such as coupon stripping/reattachment, baskets of collateral etc.

11   They are linked by the means of a before (BEFO), an after (AFTE) or a with (WITH) link, leading to specifici-
12    ty at their business validation, eligibility or settlement application processes.

13    Settlement Instructions linked automatically by T2S aim to cover the settlement of operations such as rea-
14    lignment, auto-collateralisation, corporate rebalancing liquidity, etc.

15   T2S ensures in those cases the settlement on an all-or-none basis of the initial Settlement Instruction to-
16    gether with the T2S generated Settlement Instruction for realignment, for auto-collateralisation or the T2S
17    generated liquidity transfer for corporate rebalancing liquidity etc.


18    1.6.1.11.3 Link specified by T2S Actor

19   MeanstolinkinstructionsbyT2SActor

20   A T2S Actor links Settlement Instruction(s) and/or Settlement Restriction(s) together by making the use of:

21         l A processing position code corresponding to:

22      – [INFO] Information, for information purpose. There is no processing in T2S behind this code;

23      – [BEFO] Before, which means that a Settlement Instruction or Settlement Restriction is to be settled
24          before or at least at the same time as the linked Settlement Instruction or Settlement Restriction;

25      – [AFTE] After, which means that a Settlement Instruction or Settlement Restriction is to be settled af-
26           ter or at least at the same time as the linked Settlement Instruction or Settlement Restriction;

27      – [WITH] All-or-none, which means that a Settlement Instruction, or Settlement Restriction is to be set-
28           tled at the same time as the linked Settlement Instruction or Settlement Restriction;

29         l A Pool Reference;

30    With the use of a processing position code, a T2S Actor:

31         l  Can link together:

32      – Two Settlement Instructions;

33      – Two Settlement Restrictions;

34      – One Settlement Instruction with one Settlement Restriction;


                                                                                            Page 442 of 2017



[PDF page 443]

                                                                   T2S User Detailed Functional Specifications
                                                                                               General Features of T2S
                                                                                                 Application Processes Description

 1      – One Settlement Instruction or Settlement Restriction can be executed before, after or at the same
 2          time as an existing pool, by linking the instruction to any instruction that belongs to that pool, through
 3         a processing position code WITH, AFTE or BEFO and the reference of the linked instruction. In this
 4          case, no Pool Reference is needed.

 5      – Settlement Instruction(s) and/or Settlement Restriction(s) can be linked whatever the type (deliv-
 6           ery/receipt), the ISIN code or the Intended Settlement Date, provided that the links do not contradict
 7         each other (See Table 79 - Set-up or increase of blocking, reservation or earmarking on securities
 8          [ 534]).

 9         l  Cannot link together:

10      – A Liquidity Transfer with a Settlement Instruction or a Settlement Restriction;

11      – A T2S internally generated Settlement Instruction.

12   ProcesstolinkinstructionsbyT2SActor

13         l A T2S Actor can create, update or cancel the link of a Settlement Instruction or Settlement Restriction if
14         this Settlement Instruction or Settlement Restriction is compliant with the validation checks (See Table
15      71 - Rules applying to linked Settlement Instructions/Settlement Restrictions [ 448]).

16         l  To create a link, the T2S Actor sends a Settlement Instruction/Settlement Restriction including:

17      – A processing position code (e.g. WITH as example below)

18      – The reference of the linked instruction with the T2S Instruction Reference or the T2S Actor Instruction
19          Reference.

20         l   If the T2S Actor Instruction Reference is provided, T2S also requires the Reference Owner BIC of the
21       Linked Instruction (Instructing Party BIC). In case the instruction does not include this field, T2S does
22       not create the link and the instruction is rejected (i.e. no processing position code is taken by default).
23      To identify univocally a Party in T2S, two BICs are needed (Party BIC+Parent BIC), and there is no field
24         in the message for informing the Parent BIC of the Reference Owner: in order to identify the relevant
25        Party in T2S for the Reference Owner BIC, T2S considers by default the Reference Owner BIC and the
26      CSD (or NCB) of the Instructing Party of the instruction stating the link 243.

27         l   If a T2S actor wants to make use of linkages across several instructions send to T2S via different CSDs
28       he holds accounts with (or NCBs in case of Settlement Restrictions on cash), the T2S actor has to make
29       use of the T2S reference.





     _________________________


        243   In case the Reference Owner BIC relates to a CSD that is also defined as CSD Participant of itself, T2S will consider the CSD as the relevant Party
                    in T2S for the Reference Owner BIC.


                                                                                            Page 443 of 2017



[PDF page 444]

                                                                  T2S User Detailed Functional Specifications
                                                                                              General Features of T2S
                                                                                               Application Processes Description

1                                       EXAMPLE 108 - CREATION OF A LINK





2

3   To update a link (e.g. changing the link from WITH to BEFO as example below), it is necessary first to unlink
4    the Settlement Instruction/Settlement Restriction through an Amendment Instruction, which linkage type
5   must contain the value UNLK and which processing position code must be the same as the one specified in
6    the referenced instruction. In a second step, the T2S Actor has to send another Amendment Instruction
7    which linkage type must contain the value LINK with the new processing position code (e.g. BEFO).





                                                                                          Page 444 of 2017

=== RETRIEVAL 4: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
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

=== RETRIEVAL 5: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_instruction_processing_rules"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-instruction-processing]] — Acquisition, validation, linked/CoSD instructions, partial settlement, priority, collateral, processing phases and CAoF (Articles 68, 73–76) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Article 68; PDF 49–50, printed 48–49 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
CITATION: Regulations as of 26 January 2026 | Articles 73–76; PDF 52–53, printed 51–52 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Articles 69–72 (matching, cancellation, hold, finality) are the 13 September section milan-finality.
EXCERPT (Article 68; PDF 49–50, printed 48–49):
Article 68 – Acquisition of settlement Instructions

1. Settlement instructions are acquired by the Settlement Service regarding:
      a) individual transactions (DVP or FOP);
      b) bilateral netting of securities and cash balances;
       c) securities and cash balances, netted via interposition of a Central
         Counterparty.
2. During acquisition, the Settlement Services checks:
    ▪ the completeness of the settlement instruction and its formal correctness to
     ensure the ensuing processing by the Service; and
    ▪ the matching of the settlement instruction data with personal data found in
     T2S (common static data), as well as with any restrictions, including the
     matching of the financial instruments involved with the provisions of Article
      86.
3. The validated settlement Instructions are forwarded to the subsequent phases
   of the service. Non-validated Settlement Instructions are rejected.
4. Settlement Instructions can establish that the settlement:
    ▪  is connected to the settlement of linked instructions; or
    ▪  is  conditional on  the  occurrence  of  specific  conditions  outside T2S
      (Conditional Securities Delivery CoSD7).
5. Participants may also specify:
    ▪ the possibility of a partial settlement, within the limits allowed by the T2S
      system’s functionalities; and
    ▪ the rule priority of the settlement instruction entered, within the limits
      allowed by the functionalities of T2S and taking into account that Monte
       Titoli  assigns  priority  to  the  settlement  Instructions  in  which  the
      counterparty is the Italian Ministry of Finance, those involving monetary


7 Conditional securities delivery in T2S refers to a procedure in which the final posting of securities and/or cash is dependent on
the successful completion of an additional action or event external to T2S and confirmed by an administering party.

48    In force as of 26 January 2026



[PDF page 50]

                                                            SERVICE REGULATIONS


      policy transactions and those concerning transfer of collateral by the Bank
      of  Italy  and,  subsequently,  those coming from Market Management
     Companies.
6. Participants are informed of the result of the validation process.
EXCERPT (Articles 73–76; PDF 52–53, printed 51–52):
Article 73– Automatic mechanisms for posting Collateral

1.   The participants to the Settlement Service and/or their Agent Banks that
    have previously communicated their intention to avail themselves of the
     automatic mechanisms for posting Collateral must, with the methods and
     time frames provided for in the Instructions, indicate the securities accounts
     and/or the positions that can be used for collateralisation and the exposure
      limits to be considered in the settlement process.
2.   The activation of the collateralisation mechanisms causes the automatic
     generation  of  settlement  instructions by  the Settlement  Service. The
     settlement instructions arising from collateralisation are settled jointly with
     the original Settlement Instructions, relative to which the mechanism for
     posting Collateral was activated.

Article 74 – Processing of the settlement Instructions

1. The settlement process includes a night-time phase and a day-time phase. In
   each phase the Settlement Instructions are processed on a gross basis.
2. In  each  phase,  according  to  the  eligibility  criteria  of  the  settlement
   Instructions, Monte Titoli settles:
      a) the new settlement Instructions entered before each phase during the
         night-time settlement phase and in real-time during the daytime phase,
          including the instructions for realignment and those resulting from any
         corporate actions; and
      b) the Settlement Instructions that remained unsettled in the previous
         phase.

51    In force as of 26 January 2026



[PDF page 53]

                                                            SERVICE REGULATIONS


3. The settlement Instructions are processed through the following steps:
      a) check on the settlement status of the instruction;
      b) check on the counterparties’ securities and cash account capacities. This
          includes  verifying whether resources are  available as a  result  of
           collateralisation, as well as checking any exposure limits set by the
          Participant or its Agent Bank in the TARGET2 system;
       c)  if there is securities and cash capacity, T2S settles the securities by
          debiting the Seller and crediting the Purchaser with the amount of the
          transaction.
4.  If a number of settlement instructions are handled jointly in the same phase
    for reasons of optimisation, T2S makes the checks referred to in letter b) of
   the previous paragraph, based on the net balance following the relevant
   settlement Instructions.  If there  is not enough capacity to settle the net
   balance, T2S identifies the settlement Instructions that cannot be settled and
   then, taking into account their characteristics:
        -  checks the possibility of settling them through a collateralisation process,
         in the event of a cash deficit;
        -  checks the possibility of partially settling them, in the event of a
        securities deficit.
5. Settlement Instructions that have not been settled because of insufficient
   securities or cash are re-proposed in the subsequent phase of the same
   settlement day or for settlement on the subsequent day, until they are settled
   or cancelled in accordance with the Article 70.
6. Participants may change settlement Instructions that have been proposed
   again, also partially, but only with regard to the status indicators, on condition
   that such settlement Instructions have not been entered as non-changeable.

Article 75 – Sequence in Processing Settlement Instructions

1. To improve  the  efficiency  of  the  settlement  process, TS2 implements
   optimisation mechanisms aimed at maximising its outcome.
2.  If several settlement Instructions make use of the resources available on the
  same securities or cash account, the optimisation process takes into account
   the priority criteria for the management of settlement Instructions referred to
    in Article 68, paragraph 5. In the event of equal priority, the settlement
   Instructions with the  earlier settlement date are settled  first within the
   functioning limits of the T2S platform.

Article 76 – Management of non-settled Settlement Instructions
(Corporate Action of Flow - CAoF)

1. Monte Titoli may change or cancel the settlement Instructions that have not
   been  settled on  the  established  settlement date and concern  financial
   instruments involved in corporate actions or, in relation to such Instructions,
     it may  enter  additional  settlement  Instructions aimed  at  rectifying the
   distorting impacts of the event. The operating procedures for the management
   of these settlement Instructions are set out in the Instructions.



52    In force as of 26 January 2026

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
