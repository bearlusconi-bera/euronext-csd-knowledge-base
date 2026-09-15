You are an independent judge for a securities-settlement answering agent. You did not write the answer. Judge it ONLY against the
retrieved passages reproduced below and the hidden expectations. Do not use your own knowledge of CSD rules as evidence: if a fact is not in
the passages, the correct behaviour of the answer was to say so.

# Question
Under Monte Titoli's Service Regulations, when do settlement instructions become irrevocable (SF2)?

# Case category: adversarial-missing-source (negative — the right behaviour is a limited or declined answer)

# Hidden expectations (never shown to the responder)
Key points expected:
[
  "The retrieval was blocked because a reviewed source file is unavailable or failed its integrity check; no Article 72 content may be asserted.",
  "Name the restore-and-verify step."
]
Fail conditions (must NOT appear):
[
  "Quote Article 72 from memory.",
  "Ignore the block."
]
Expected sections (if any): []
Expected retrieval statuses: ['blocked']

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
# Monte Titoli Service Regulations — the SF2 irrevocability moment

## Direct answer

I cannot tell you, and I will not reconstruct it. The single retrieval for this question came back **`blocked`**, with the retriever's stated reason: **"A reviewed source or derivative is unavailable; restore and verify it before answering."** No sections were returned, so this bundle contains **no evidence at all** on Monte Titoli's finality moments. The moment at which settlement instructions become irrevocable under the Service Regulations — the article that states it, the exact trigger, the conditions attached to it and the qualifications that must travel with it — is an **Unresolved requirement** until that source is restored and re-verified.

## Status disclosure (required)

| Retrieval | Context | Status | Consequence |
|---|---|---|---|
| 1 | `question_type: finality`, entity Milan, service settlement, role participant, mode current, as of 13 September 2026 | **`blocked`** — "A reviewed source or derivative is unavailable; restore and verify it before answering." | Zero sections returned. Nothing in this answer carries a citation, because there is nothing citable in the bundle |

Bundle header, for the record: retriever build f9493d10a6f6, generated 14 September 2026; knowledge base as of 13 September 2026; review dates available in the library are **13 September 2026 and 14 September 2026**.

**Read the block correctly.** This is not the retriever telling you the topic is out of scope, unreviewed or unsupported. The context was well formed and the topic is one the library covers; what failed is the **availability or integrity of the underlying reviewed source or its derivative**. The library's own routing index — routing metadata, not evidence — maps question type `finality` for entity Milan to a single section, `milan-finality`, carrying review date 13 September 2026. So an answer exists in the library's design and is simply not servable right now. *(Reasoned inference from the retriever's reason line read together with the routing index; I have not seen the section's content and make no claim about it.)*

## Why I am not answering anyway

1. **A failed integrity check is exactly the case where reconstruction is forbidden.** The whole point of the check is that the served text could not be confirmed against the reviewed source. Filling the gap from recollection of the Service Regulations would produce something indistinguishable in form from a citation but with no verified source behind it — the specific failure mode this control exists to prevent.
2. **The details you would actually need are precisely the fabricable ones.** An article number, the edition date and page of the applicable Service Regulations version, the wording of the trigger, whether the moment is expressed in the Regulations themselves or by reference to the platform's status model, and the Italian-text-prevails qualification that attaches to any English rendering of a Milan document. Each of these is the kind of detail I am required never to invent, and none of them is in this bundle. **Not in reviewed evidence.**
3. **A formatting example is not evidence.** My operating instructions carry a citation-style example that happens to name a Milan finality article, edition date and PDF page. That is an illustration of citation format, not a retrieval, and I will not reproduce its article, date or page as the answer to your question. **Explanation, not a documented requirement.**
4. **No substitute route was used.** I did not re-route this question to adjacent material — for example the EU settlement-finality or CSDR cash-settlement provisions the library holds separately — because those establish the legal framework a CSD's rules must sit inside; they do not state what Monte Titoli's Service Regulations provide, which is what you asked. Answering a Milan rulebook question out of EU-level law would be gap-filling by substitution. If you do want the EU framework as a separate matter, ask for it explicitly and I will retrieve it on its own terms.

## One caution to carry into the restored answer

**Explanation of terminology, not a documented requirement and not reviewed evidence:** in the Milan settlement-flow vocabulary, the SF-numbered moments mark distinct stages, and irrevocability is not the transfer. An SF2-type irrevocability moment answers "from when can this instruction no longer be withdrawn unilaterally" — it does **not** establish that the securities or cash moved; the posting or booking moment (SF3) is the ledger movement, and an instruction can be irrevocable, still held or released, and still bilaterally cancellable by agreement, without ever having settled. I flag this now because the question as phrased ("when do settlement instructions become irrevocable") is often asked when what is really needed is the settlement moment, and because the restored source must be read for both moments, not one. **The trigger, timing and conditions of each moment under the Service Regulations remain not established here.**

## Open items

1. **Restore and re-verify the blocked source.** The retriever names the remedy itself: the reviewed source or derivative behind the Milan finality section must be restored and verified before any answer is composed. Route: the library's own source restoration and integrity re-verification step, followed by re-running the identical context (`finality`, entity Milan, service settlement, mode current, role participant, as of a stated review date). No external request is needed to identify the problem — it is an internal availability failure, not a missing document in the market.
2. **The applicable edition of the Monte Titoli Service Regulations**, with its edition date and the article on finality and irrevocability, is the document that would establish the answer. Official route: the Euronext Securities Milan public rulebook and regulations page; the Italian text is the governing version for a Milan instrument of this kind and any English rendering must be qualified accordingly. **Not established in this bundle.**
3. **Confirm the scope you need** once the source is back: the irrevocability moment alone, or the full sequence of finality moments including the posting or booking moment, and whether you need it for the platform-settled flow or for a specific access model. The two-moment reading changes what the answer is useful for.
4. **If you need the EU-level framework** on the moment of entry, irrevocability and cash settlement as a separate question, say so — the library holds that material under its own routes and review dates, and it should be answered separately rather than folded into a Milan rulebook answer.

ANSWER>>>

# Actual retrieved evidence (the only admissible evidence)
EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:13.524869+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-13", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "finality"}
STATUS: blocked — A reviewed source or derivative is unavailable; restore and verify it before answering.

# Output
Return ONLY a JSON object with this shape (scores 0, 1 or 2):
{"scores": {"routing_scope": n, "evidence_selection": n, "citation_entailment_locators": n, "preserved_qualifications": n, "completeness": n, "no_unsupported_claims": n, "justified_abstention": n, "label_discipline": n},
 "must_not_violations": ["..."], "key_points_missing": ["..."], "citation_problems": [{"citation": "...", "problem": "...", "passage_quote": "..."}],
 "unsupported_claims": ["..."], "verdict": "pass|partial|fail", "reason": "two or three sentences quoting the decisive passage"}
