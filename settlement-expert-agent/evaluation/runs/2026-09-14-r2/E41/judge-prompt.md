You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
From 21 September 2026, where do Euronext Paris equity trades settle and what is the first intended settlement date under the new model?

# Case category: future-programme (positive — evidence should support a useful answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "MN_07/2026: Euronext Securities Milan becomes designated place of settlement for Paris (XPAR/MLXI/ALXP) equity trades from 21 September 2026; first ISD 23 September; alternative CSD choice remains; announced go-live as of 8 September, not proof of live operation; future mode."
]
Fail conditions (must NOT appear):
[
  "Present as already live on 14 September."
]
Expected sections (if any): ['milan-european-offering-golive']
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
# Euronext Paris equity trades from 21 September 2026: place of settlement and first ISD

## Direct answer

**Documented requirement.** On the announced model, **Euronext Securities Milan** becomes the designated place of settlement for equity trades executed on the Euronext Paris market (together with Amsterdam and Brussels) as of **21 September 2026**, and **transactions executed on or after 21 September 2026 under the new model have 23 September 2026 as their first intended settlement date (ISD)**. Two qualifications are material and must travel with that answer: the notice announces a **go-live, which is not proof of live operation** (as of the 14 September 2026 review date the date was still in the future), and **Trading Members may designate an alternative settlement system in place of Euronext Securities Milan**, so "where a given Paris equity trade settles" is a per-member (and, for individual instruments, per-instrument) question that this evidence does not close.

Source for both statements: [[milan-european-offering-golive]] MN_07/2026 "Euronext European Offering: Go-Live confirmation" (8 September 2026), MN_07/2026 PDF 1–2; reviewed 14 September 2026; body language English but **authoritative language Italian** — the admitted text is a **translation and the authoritative language differs**, so the English wording is not the governing wording; no version identifier; approval: source identity checked, no independent whole-edition supervisory approval certification.

## 1. Scope of the migration, as documented

**Documented requirement** — from the same notice and citation as above ([[milan-european-offering-golive]] MN_07/2026, PDF 1–2; reviewed 14 September 2026; English translation, authoritative language Italian; no version; source identity checked, no independent whole-edition supervisory approval certification):

1. Euronext Securities Milan confirms the go-live of the Euronext European Offering "will take place as planned on **21 September 2026**".
2. As of that date Euronext Securities Milan **will become the designated place of settlement** for:
   - equity trades executed on **Euronext Amsterdam, Brussels and Paris** markets; and
   - **ETP trades denominated in euro** executed on **Euronext Amsterdam and Paris** markets.
3. The migration applies to Equity and ETP transactions executed on the following MICs: **XAMS, XBRU, XPAR, MLXB, XMLI, ALXB, ALXP**. For ETPs, the scope is limited to instruments traded in euro.
4. **Trading Members may designate an alternative settlement system** in place of Euronext Securities Milan, "as further described by Euronext Markets".
5. **Transactions executed on or after 21 September 2026 under the new model will have 23 September 2026 as their first intended settlement date (ISD).**
6. Settlement agents should ensure that all required operational and settlement arrangements are in place ahead of the migration date.
7. For **physically settled equity derivatives**, the place of settlement "will remain aligned with the underlying instrument and, where applicable, the resulting settlement will be processed through Euronext Securities Milan".
8. The settlement arrangements applicable to **other Euronext markets and other asset classes, including bonds, certificates and warrants, remain unchanged**.

**Reasoned inference** (derived from items 2 and 3): the Paris part of the question is covered twice over — once by the named market ("Euronext Paris") and once by the MIC list, which includes **XPAR** and **ALXP**. The notice does not, however, map each MIC to a market name, so any statement that a *particular* MIC is the Paris regulated market or the Paris growth market would go beyond the evidence. Which of the seven MICs corresponds to Paris venues is not in reviewed evidence.

## 2. What the first-ISD statement does and does not establish

**Documented requirement.** The first ISD under the new model is 23 September 2026, for transactions executed on or after 21 September 2026 [[milan-european-offering-golive]] MN_07/2026, PDF 1–2; reviewed 14 September 2026; English translation, authoritative language Italian; approval: source identity checked, no independent whole-edition supervisory approval certification.

**Reasoned inference** (derived from that single sentence, and from the absence of any settlement-cycle provision in the bundle): the notice prints one date for one cohort of transactions. It does **not** state a settlement cycle rule, so it cannot be read as evidence that Paris equity trades settle on T+2, T+1 or any other fixed cycle, either before or after the migration. The interval between 21 and 23 September 2026 is a fact about those two dates only. No calendar, no CSDR Article 5 text and no Euronext or Euronext Securities Milan settlement-cycle provision is in this bundle, so:

**Unresolved requirement.** The applicable settlement cycle and the business-day counting rule for Paris equity trades after 21 September 2026 are **not in reviewed evidence**. So is the ISD for any transaction executed *before* 21 September 2026, and the treatment of a trade executed on 21 September under the *old* arrangements — the notice conditions its ISD statement on "under the new model" and does not define the transition boundary any further.

**Unresolved requirement.** Whether 23 September 2026 is a settlement day on the applicable operating-day calendar is not independently in the bundle; the date is admitted because the notice prints it, not because a calendar was reviewed.

## 3. Qualifications that stay attached to every statement above

From the LIMITATION lines on [[milan-european-offering-golive]] (reviewed 14 September 2026):

- **Announced go-live is not proof of live operation.** The notice is dated 8 September 2026 and the bundle was reviewed on 14 September 2026, both before 21 September 2026. Nothing in the bundle evidences that the migration has actually happened, nor any post-go-live confirmation, deferral or contingency notice.
- **Place-of-settlement details for individual instruments require the programme documents**, which are not in this bundle. The notice establishes the designation at market/MIC level, not ISIN-by-ISIN eligibility.
- The evidence is an **operational/market notice**: an English communication by Euronext Securities Milan. It is **not the Service Regulations or the Service Instructions**, and such notices "carry a PRIVATE or INTERNAL USE ONLY footer despite public publication" in several cases. The admitted pages also carry Euronext's own disclaimer that the publication is for information purposes only, is provided "as is", forms the basis of no contract, and that rights and obligations in respect of traded financial products depend solely on the applicable rules of the market operator.
- The section's applicability basis is **reference_description** and its mode is **future** — it describes an announced arrangement, not a currently evidenced operating rule.
- **Governing language: Italian.** The admitted text is an English translation whose authoritative language differs, so no argument should be built on the precise English phrasing (for example on "designated place of settlement" as a term of art) without the Italian authoritative text.

*Explanation, not a documented requirement:* "intended settlement date (ISD)" is the date on which the parties intend the transfer of securities and cash to take place, as stated in the settlement instruction; it is a date attribute of the instruction, not a guarantee that settlement occurs then. "Place of settlement" identifies the securities settlement system where the transfer is to be booked. "MIC" is a market identifier code used to identify the execution venue.

## 4. The second retrieval is not evidence for this question

**Retrieval 2 status: evidence_only**, but on a different subject: the final publication of the **T2S R2026.NOV** documentation set. For completeness and because the bundle admits it: the T2S UDFS R2026.NOV and UHB R2026.NOV (with GFS, DMT, URD, BFD and the BDM/BILL/CRDM/ESMIG UDFS and User Handbooks) were finally published per a cover note dated 14 September 2026, the UDFS R2026.NOV itself carrying the date 11 September 2026; drafts were published on 31 July 2026 and reviewed 3–21 August 2026; the final versions incorporate Change Requests in the scope of T2S Release 2026.NOV, including editorial Change Requests approved by the CSD Steering Group until 23 July 2026 [[november-final-release]] Cover Note, PDF page 1 (final-publication statement, dated 14 September 2026); reviewed 14 September 2026; version "R2026.NOV final publication; no production-deployment certification"; body language English, authoritative language English, original or official-language text; approval: final document delivery confirmed, production deployment not verified. [[november-final-release]] T2S User Detailed Functional Specifications R2026.NOV (UDFS), PDF page 1 (document identity/date, 11 September 2026); reviewed 14 September 2026; same version, language and approval qualifications.

Its LIMITATION lines: final publication is established but **November production deployment is not verified**; the 14 September cover/listing, the 11 September UDFS date and the earlier target are separate facts; and **only cover-page statements are admitted** — no November operational provisions, payloads or changed message versions.

**Reasoned inference** (derived from comparing the question with this section's content): this retrieval contributes nothing to the Paris place-of-settlement or first-ISD question. It was pulled by the router's "future business date: release status retrieved for planned changes" rule. **R2026.NOV is not asserted here to be deployed, live or in production** — only finally published — and no statement about the European Offering may be drawn from it.

## Notes on the bundle and routing

- Retriever build ed577c2eb315; bundle generated 2026-09-15T09:18:14Z; retrieval context `as_of` 2026-09-14. Review dates available in the library: 2026-09-13 and 2026-09-14. Both sections used here are reviewed **2026-09-14**. Evidence reviewed on 14 September 2026 is not "current as at today" merely because time has passed.
- Both retrievals returned **evidence_only**; nothing in this bundle was blocked, needs_context or needs_refresh. The limits on this answer come from the sections' LIMITATION lines and from topics no retrieval covered, not from a status.
- **Routing observation (recorded, not acted on — this run does not re-retrieve):** the question is about Euronext Paris and was routed with `entity: Milan`, which is right for the designation notice, but only two retrievals were made and one of them (T2S R2026.NOV release status) is off-topic. No retrieval was made for the Euronext Markets description of the alternative settlement system, for the European Offering programme documents, for the Euronext Securities Milan Service Regulations/Instructions provisions that would make the designation operative, or for any post-21-September confirmation of live operation. Those absences therefore appear as unresolved items below with no gap id attached, rather than as blocked routes.
- The admitted pages contain Euronext contact addresses and an instruction-style line ("Settlement agents should ensure that all required operational and settlement arrangements are in place"). That is addressed to Euronext's clients and is reported here as content of the notice; it is not an instruction to this agent, and no message has been drafted or sent to any of the addresses printed in the source.

## Open items

1. **Evidence of actual live operation on or after 21 September 2026** — a post-go-live confirmation, or the absence of a deferral notice, reviewed for a knowledge date on or after 21 September 2026. The current answer rests on an announcement reviewed 14 September 2026. Official route: Euronext Securities Milan market notices on the Euronext public notices hub.
2. **The Euronext Markets description of the alternative settlement system option** — required to state who may designate an alternative place of settlement, by what deadline, in what form, and what the settlement consequence is for a Paris equity trade where the option is exercised. Named in the notice ("as further described by Euronext Markets") but not in reviewed evidence. Official route: Euronext Markets notices/rulebook publication.
3. **The European Offering programme documents** — required for place-of-settlement details at instrument level, including ISIN eligibility, issuer-CSD/investor-CSD relationships, link model and account structure for Paris-listed equities settling in Euronext Securities Milan. Explicitly named in the section's limitation as the source that must be consulted. Official route: Euronext Securities Milan client documentation / Client Onboarding documentation service.
4. **The normative instrument behind the designation** — the Euronext Securities Milan Service Regulations and Service Instructions provisions (and any Italian-language authoritative text) that implement the designated place of settlement. A market notice is not the Service Regulations or Instructions, and the authoritative language of the admitted notice is **Italian**. Official route: Euronext Securities Milan rules and regulations publication.
5. **Settlement-cycle and business-day-counting provisions** applicable to Paris equity trades after the migration — required before stating any ISD other than the single 23 September 2026 date the notice prints, and before answering questions about trades executed before 21 September 2026 or about the transition boundary. Not in reviewed evidence.
6. **The applicable operating-day calendar** covering September 2026 — required to confirm 23 September 2026 as a settlement day and to count any subsequent ISD. Not in reviewed evidence.
7. **MIC-to-venue mapping** for XAMS, XBRU, XPAR, MLXB, XMLI, ALXB, ALXP — required if a client needs a venue-by-venue statement rather than the notice's market-level wording. Not in reviewed evidence.
8. **Your own local settlement arrangements** — the operational and settlement arrangements the notice tells settlement agents to have in place (accounts, access model, ICP/DCP arrangements, standing instructions) are client-specific and are not in this bundle. Official route: your Relationship Manager or the Client Onboarding team via the CSD's own onboarding channel; no contact has been made here.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build ed577c2eb315, generated 2026-09-15T09:18:14.916605+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "future", "question_type": "european_offering_go_live"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-european-offering-golive]] — European Offering go-live confirmed for 21 September 2026: scope, MICs, alternative CSD choice and first ISD 23 September (reviewed 2026-09-14; modes ['future']; entities ['Milan']; basis reference_description)
CITATION: MN_07/2026 Euronext European Offering: go-live confirmation (8 September 2026) | MN_07/2026 PDF 1–2 | version None | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/notices/monte-titoli/20260903%20Euronext%20Securities%20Milan%20Market%20Notice%20-%20EE_0.pdf
LIMITATION: Operational/market notices are English communications by Euronext Securities Milan; they are not the Service Regulations or Instructions, and several carry a PRIVATE or INTERNAL USE ONLY footer despite public publication.
LIMITATION: Announced go-live, not proof of live operation; place-of-settlement details for individual instruments require the programme documents.
EXCERPT (MN_07/2026 PDF 1–2):
[PDF page 1]

08 September 2026
MN_07/2026

Euronext European Offering: Go-Live
confirmation
   To the attention of:                           All Participants


   Priority:                                      High


   Topic:                                         Euronext European Offering: Go-Live
                                                   confirmation




Dear Client

Further to the Market Notice "Euronext Securities to be designated as settlement
organisation for Euronext equities and ETFs" and the subsequent market
communications issued throughout the implementation programme, Euronext
Securities Milan confirms that the go-live of the Euronext European Offering will
take place as planned on 21 September 2026.

This milestone represents a significant step in Euronext's strategy to further
harmonise post-trade services across its markets, reduce settlement fragmentation
and enhance the efficiency of the European post-trade infrastructure.

Scope:

As of this date, Euronext Securities Milan will become the designated place of
settlement for:

     •    Equity trades executed on Euronext Amsterdam, Brussels and Paris markets;
          and
     •    ETP trades denominated in euro executed on Euronext Amsterdam and Paris
          markets.
This publication is for information purposes only and is not a recommendation to engage in investment activities. This publication is
provided “as is” without representation or warranty of any kind. Whilst all reasonable care has been taken to ensure the accuracy of
the content, Euronext does not guarantee its accuracy or completeness. Euronext will not be held liable for any loss or damag es of
any nature ensuing from using, trusting or acting on information provided. No information set out or referred to in this publication
shall form the basis of any contract. The creation of rights and obligations in respect of financial products that are traded on the
exchanges operated by Euronext’s subsidiaries shall depend solely on the applicable rules of the market operator. All proprietary
rights and interest in or connected with this publication shall vest in Euronext. No part of it may be redistributed or reproduced in any
form without the prior written permission of Euronext.
Euronext refers to Euronext N.V. and its affiliates. Information regarding trademarks and intellectual property rights of Euronext is
located at https://www.euronext.com/terms-use.
© 2022, Euronext N.V. - All rights reserved.



| 1 of 2



[PDF page 2]

The migration applies to Equity and ETP transactions executed on the following
MICs:
   •   XAMS
   •   XBRU
   •   XPAR
   •   MLXB
   •   XMLI
   •   ALXB
   •   ALXP
For ETPs, the scope is limited to instruments traded in euro.

Trading Members may designate an alternative settlement system in place of
Euronext Securities Milan, as further described by Euronext Markets.

Transactions executed on or after 21 September 2026 under the new model will
have 23 September 2026 as their first intended settlement date (ISD).

Settlement agents should ensure that all required operational and settlement
arrangements are in place ahead of the migration date.

For physically settled equity derivatives, the place of settlement will remain aligned
with the underlying instrument and, where applicable, the resulting settlement will
be processed through Euronext Securities Milan.

The settlement arrangements applicable to other Euronext markets and to other
asset classes, including bonds, certificates and warrants, remain unchanged.

Further information:

For further information, please contact your Relationship Manager or the Client
Onboarding team.


Client Onboarding Team
E: CSD.Onboarding@euronext.com


Sales & Relationship Management
E: MTsalesteam@euronext.com




| 2 of 2

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "T2S", "service": "settlement", "role": "participant", "mode": "future", "question_type": "release_status"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.
ROUTER NOTES: {"_note": "future business date: release status retrieved for planned changes"}

--- SECTION [[november-final-release]] — November final publication confirmed on 14 September; deployment unverified (reviewed 2026-09-14; modes ['reference', 'future']; entities ['T2S']; basis reference_description; subject release R2026.NOV)
CITATION: Cover Note | PDF page 1: final-publication statement, dated 14 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/pub/pdf/annex/Cover_Note_Final_Delivery_T2S_UDFS_R2026.NOV_UHB_R2026.NOV.en.pdf?1d8ee68f0593cb88571835efb7cd5ed8
CITATION: T2S User Detailed Functional Specifications R2026.NOV (UDFS) | PDF page 1: document identity/date, 11 September 2026 | version R2026.NOV final publication; no production-deployment certification | body language en | authoritative language en | original or official-language text | approval: Final document delivery confirmed; production deployment not verified | source reviewed 2026-09-14 | url https://www.ecb.europa.eu/paym/target/target-professional-use-documents-links/t2s/sdd/shared/pdf/T2S_UDFS_R2026.NOV_clean_20260911.en.pdf?8a61e1a06ea669f708ba50ac84a842a0
LIMITATION: Final publication is established; November production deployment is not verified.
LIMITATION: The 14 September cover/listing, 11 September UDFS date and earlier target are separate facts.
LIMITATION: Only cover-page statements are admitted. No November operational provisions, payloads or changed message versions are admitted.
EXCERPT (PDF page 1: final-publication statement, dated 14 September 2026):
[PDF page 1]
              
                 
 
 
 
 
ECB-PUBLIC 
 
14 September 2026 
 
Delivery of the T2S UDFS R2026.NOV and UHB R2026.NOV 
As envisaged in the T2S Plan, we have published final versions of the: 
• 
T2S User Detailed Functional Specifications R2026.NOV (UDFS R2026.NOV) 
• 
T2S User Handbook R2026.NOV (UHB R2026.NOV) 
• 
T2S General Functional Specifications R2026.NOV (GFS R2026.NOV) 
• 
T2S Data Migration Tool R2026.NOV (DMT R2026.NOV) 
• 
T2S User Requirements Document R2026.NOV (URD R2026.NOV) 
• 
T2S Business Functionality for T2S Graphical User Interface R2026.NOV (BFD R2026.NOV) 
• 
BDM User Detailed Functional Specifications R2026.NOV 
• 
BILL User Detailed Functional Specifications R2026.NOV 
• 
CRDM User Detailed Functional Specifications R2026.NOV 
• 
ESMIG User Detailed Functional Specifications R2026.NOV 
• 
BDM User Handbook R2026.NOV 
• 
BILL User Handbook R2026.NOV 
• 
CRDM User Handbook Book 1 R2026.NOV 
• 
CRDM User Handbook Book 2 R2026.NOV 
 
For the convenience of the readers, all changes in the documents were highlighted in revision marks. 
Additionally, we added the appropriate CR references. 
The draft intermediate versions of these documents were published on 31 July and were reviewed from 03 
August 2026 to 21 August 2026. The comments from the market participants have been taken into account for 
the final versions to be published on 11 September 2026. 
Scope of the delivery 
These new versions incorporate Change Requests in the scope of the T2S Release 2026.NOV, including the 
editorial Change Requests approved by the CSD Steering Group (CSG) until 23 July 2026.  
The exhaustive list of all Change Requests is provided as Annex A to this cover note.  
Complementing the information provided in the Service Transition Plans, the Release Notes and the UDFS 
itself, a list containing all the T2S messages with their respective links to MyStandards is provided as Annex 
B to the Cover Note.
EXCERPT (PDF page 1: document identity/date, 11 September 2026):
[PDF page 1]
Author
Version
Identifier
Date
4CB
R2026.NOV
T2S UDFS
11 September 2026
User Detailed Functional Specifications

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
