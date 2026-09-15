# Issuer CSD, investor CSD, and whether Monte Titoli can be both

## Direct answer

In plain terms: the **issuer CSD** is the CSD where a security was issued and distributed on behalf of the issuer — it is the "home" of that issue. The **investor CSD** is the CSD that holds the security for at least one party to a settlement instruction, on behalf of its own participants, by holding the position in another CSD's books. **Yes — the same CSD can be both**, and the reviewed evidence says so explicitly: a CSD is "both" when it is the CSD in which the security has been issued *and* the CSD of at least one party to the instruction. Crucially, these are **roles per security and per instruction, not permanent titles**: Monte Titoli can be issuer CSD for one ISIN and investor CSD for another at the same moment.

Both retrievals in this bundle returned `evidence_only`; no retrieval was blocked, and none reported missing context or an unreviewed knowledge date. Nothing below rests on memory of rulebooks or T2S documentation.

## The definitions, as documented

**Documented requirement.** For the purposes of the T2S realignment process, a CSD is defined as:

| Role | Definition in the evidence |
|---|---|
| Issuer CSD | "the CSD in which the security has been issued and distributed on behalf of the Issuer" |
| Investor CSD | "the CSD of at least one party of the Settlement Instruction" |
| Both | "the CSD in which the security has been issued **and** the CSD of at least one party of the Settlement Instruction" |

[[t2s-realignment]] T2S User Detailed Functional Specifications R2026.JUN (UDFS), §1.6.1.10.3 "Role and links between CSDs for cross-CSD and external-CSD settlement", PDF 373–376; version R2026.JUN; reviewed 13 September 2026; body language English, no authoritative language independently established; source identity checked but no independent whole-edition supervisory approval certification. LIMITATION carried with this claim: actual links, accounts and ISIN eligibility require verification; and this section does not establish atomicity of an arbitrary two-security swap, nor does it describe actions taken outside T2S.

**Documented requirement.** How an investor CSD actually holds the security: each investor CSD chooses between opening an omnibus account in the books of the issuer CSD, or opening an omnibus account in the books of any other CSD that is already an investor CSD for the same financial instrument. In both cases the CSD where the omnibus account is opened is the **technical issuer** for the investor CSD for those securities. For one ISIN an investor CSD may define several such investor-type links (several technical issuer CSDs); exactly one is flagged "default" and the others "alternative". Alternative links may only be set up for T2S-in investor CSDs pointing to a T2S-in technical issuer CSD, and the issuer-type link a CSD sets with itself as issuer can never be alternative — it is always default. [[t2s-realignment]] (same locator, version and review date as above).

**Documented requirement.** What this set-up is used for: T2S derives the realignment chain for matched settlement instructions either from both investor CSDs (delivering and receiving) up to the issuer CSD(s) of the traded securities when default links are used, or from the delivering investor CSD up to the receiving investor CSD (or vice versa) when alternative links are used. Realignment instructions are generated automatically from the links in reference data, without further action by T2S actors, and T2S ensures that the generated realignment instructions and their business instructions settle on an **all-or-none** basis. [[t2s-realignment]].

**Reasoned inference** (derived from the three-way definition above plus the per-ISIN link configuration in the same section): because the roles are defined by reference to a particular security and a particular settlement instruction, and because links are configured per investor CSD and per ISIN, a single CSD is necessarily issuer CSD for the issues it holds natively and investor CSD for issues it holds through another CSD — simultaneously, on the same business day. The evidence states the "both" case directly; the "same moment, different ISINs" formulation is my inference from the per-ISIN link configuration, not a sentence in the excerpt.

## What Monte Titoli's own rules add

**Documented requirement.** Where settlement instructions are to be settled between a participant in Monte Titoli (other than another CSD in T2S) and a participant in another CSD in T2S — cross-CSD settlement — T2S automatically carries out the movements between the securities accounts of the participants involved, **of the investor CSDs and of the issuer CSD**. [[milan-cross-csd-disclosure]] Regulations as of 26 January 2026, Article 77(1), PDF 54 (printed page 53); version 26 January 2026; reviewed 14 September 2026 (underlying source reviewed 13 September 2026). This is an English translation and the **Italian text prevails** (cover, PDF 1); source identity checked, with no independent whole-edition supervisory approval certification.

**Documented requirement.** Monte Titoli does not envisage carrying out a cross-CSD settlement on securities if the **issuer CSD is outside T2S**, unless both investor CSDs have a link in place with another CSD in T2S so that realignment with the issuer CSD outside T2S is not necessary. [[milan-cross-csd-disclosure]] Article 77(2), same version, translation and review dates; Italian text prevails. LIMITATION travelling with this claim: the actual links per ISIN are not certified by this evidence.

**Documented requirement.** On request, Monte Titoli makes available the events that change the balance in a participant's securities account, the settlement status of each transaction in real time and the settlement of the whole transaction, through the direct link channel to T2S or through the X-TRM Service; cash balance disclosure is also available on request, in the format and channels indicated in the Services Manuals. [[milan-cross-csd-disclosure]] Article 78, PDF 54; version 26 January 2026; reviewed 14 September 2026; English translation, Italian text prevails.

## One adjacent point, so the roles are not over-read

**Documented requirement.** Generation of realignment instructions is not the same thing as a completed transfer. The posting application process checks whether settlement can be achieved given eligibility to settlement and available resources; only when that check is satisfactory does posting update the cash balance, securities position and limit headroom, "resulting in the irrevocability of the settlement". [[t2s-posting]] T2S UDFS R2026.JUN, §1.6.1.8.1 and the first overview paragraph, PDF 303–304; version R2026.JUN; reviewed 13 September 2026; body language English, no authoritative language independently established.

**Explanation, not a documented requirement** (background wording only, to make the terms readable): "omnibus account" here means one account in the technical issuer's books in which the investor CSD's participants' holdings for that security are reflected collectively; "realignment" means the additional bookings T2S generates so that the chain of holdings between the CSDs stays consistent with the trade between the two participants.

## Open items

- **Unresolved requirement — which ISINs place Monte Titoli in which role.** This bundle defines the roles but certifies no instrument-level facts. The section's own LIMITATION states that actual links, accounts and ISIN eligibility require verification, and Article 77(2)'s carve-out is expressly not certified per ISIN. Establishing source: Monte Titoli's CSD account link / eligible-securities reference data and the Euronext Securities Milan service documentation, via the public documentation hub or the client platform (X-TRM / client documentation service); the CSD account link configuration in T2S reference data would establish the default and alternative links per ISIN.
- **Unresolved requirement — the statutory definitions.** No CSDR / RTS text defining issuer CSD and investor CSD was retrieved in this bundle; the definitions above are the T2S realignment-process definitions only. Establishing source: the regulatory text itself, not in reviewed evidence here.
- **Not asserted:** nothing in this bundle establishes atomicity of an arbitrary two-security exchange, nor any cut-off time, fee, account number or link eligibility — none is claimed above.
- No gap id was named by the bundle for this question, and no retrieval status other than `evidence_only` was returned.
