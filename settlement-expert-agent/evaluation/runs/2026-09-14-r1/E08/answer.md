# Irrevocability in Monte Titoli's settlement system (Euronext Securities Milan)

## Direct answer

The legal moment of irrevocability is **matching in T2S (SF2)**, and the exception is the **bilateral cancellation of matched settlement instructions under Article 70(2)**. The provision reads, verbatim:

> "2. Settlement Instructions cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70 (2)."

**Documented requirement** [[milan-finality]] — *Regulations as of 26 January 2026, Article 72(2); Articles 69–71 and 72(1)–(3) retaining 70(2), PDF 50–51 (printed pages 49–50); version 26 January 2026; reviewed 13 September 2026; English body text but **the authoritative language is Italian — this is a translation and the Italian text prevails**; approval: source identity checked, no independent whole-edition supervisory approval certification.*

---

## The three moments, as the Regulations separate them

Article 72 is titled "Input into the Settlement System and irrevocability of settlement Instructions" and defines three distinct moments, labelled SF1, SF2 and SF3. All three are **documented requirements** from [[milan-finality]], same locator and qualifications as above:

| Moment | Verbatim provision | What it establishes |
|---|---|---|
| **SF1 — entry** | "1. Settlement Instructions are deemed 'entered' into the Settlement System, pursuant to Article 2(2) of Legislative Decree 210/2001, from the moment the validation time in T2S ends (SF1)." | The instruction is *entered into the system* for the purposes of Article 2(2) of Legislative Decree 210/2001. Entry, not irrevocability. |
| **SF2 — irrevocability** | "2. Settlement Instructions cannot be revoked by a participant or a third party from the time of their matching in T2S (SF2), without prejudice to the bilateral cancellation of settlement Instructions provided for under Article 70 (2)." | Unilateral revocation by a participant **or a third party** stops at matching — subject to the Article 70(2) exception. |
| **SF3 — finality of transfer** | "3. The transfer of securities and cash become final from the time of the debiting of the cash, or of the securities when settlement by cash is not provided for. (SF3)" | The transfer itself becomes final at the cash debit, or at the securities debit where there is no cash leg (free-of-payment). |

**Reasoned inference** (derived from reading Article 72(2) against Article 72(3), not from a single sentence): SF2 is not settlement. Matching makes the instruction irrevocable in the sense of Article 72(2); the securities and cash transfer becomes final only at SF3. An instruction can therefore be irrevocable and still unsettled. Any specification that treats "matched" as "settled" misreads the article.

*Explanation of terms, not a documented requirement:* **matching** is the comparison of the two sides' settlement details to confirm both parties agree on the terms; **allegement** (printed "alledgement" in the source) is the notice to a counterparty that an instruction is waiting to be matched against it; **free-of-payment (FoP)** is a securities transfer with no cash leg in the system.

---

## The exception, and the other cancellation routes in the same chapter

### The exception named in Article 72(2)

**Documented requirement** [[milan-finality]], *Article 70(2), PDF 50 (printed 49); version 26 January 2026; reviewed 13 September 2026; English translation, Italian text prevails*:

> "2. Matched settlement Instructions may be cancelled bilaterally, with the consent of both Participants, or upon request of an entity acting on their behalf, subject to the prior submission to Monte Titoli of the relevant mandate."

So the exception has three conditions on its face: it is **bilateral**; it needs **the consent of both participants**; and where an entity acts on their behalf, the **relevant mandate must have been submitted to Monte Titoli beforehand**. The section carries an explicit limitation on this point: **SF2 retains Article 70(2) bilateral cancellation** [[milan-finality]].

**Documented requirement** [[milan-finality]], *Article 70(3), same locator and qualifications*: a bilateral cancellation is not a instant unwind — "Cancellations are sent by the Participants with the methods and the time frames provided for in the Instructions. They then go through the acquisition phase and, if referring to matched settlement Instructions, the matching phase. When the cancellations are matched, the original settlement Instructions are cancelled." The cancellation instructions must themselves match before the original instruction is cancelled.

### Other cancellation provisions in Article 70 that bear on revocability

These are **documented requirements** from the same excerpt [[milan-finality]], and they qualify the picture without being the Article 72(2) exception itself:

- **Article 70(1)** — unilateral cancellation is available to the entering participant **only up to the time of matching**, and only if the instruction was not entered as non-changeable. This is the mirror image of SF2.
- **Article 70(4)** — market management companies and central counterparties may ask Monte Titoli to **block** these cancellation functionalities for their settlement instructions, under those systems' operating rules and in accordance with the provisions for T2S.
- **Article 70(5)** — cancellations may also be entered by Monte Titoli at the request of participants and in the other cases established by the Rules, in accordance with the provisions above.
- **Article 70(6)** — "CoSD Settlement Instructions may only be cancelled by Monte Titoli."
- **Article 70(7)** — automatic cancellation from the T2S platform is disposed when instructions "a) have not passed the daily validation phase; b) are not matched or are not settled within the time limits provided in the Instructions".
- **Article 70(8)** — participants are informed of the progress and outcome of the cancellation process and of any automatic cancellation.

**Reasoned inference** (derived from Article 70(6)–(7) read against Article 72(2)): automatic cancellation under 70(7)(b) and CSD-only cancellation of CoSD instructions under 70(6) are removals of the instruction effected by the system or by Monte Titoli, not revocations by "a participant or a third party". Article 72(2) names only Article 70(2) as the reservation to irrevocability, so I do not treat 70(6) or 70(7) as further exceptions to SF2 — but the Regulations do not say so expressly, and this reading is mine, not the text's.

---

## Limitations that travel with this answer

Both limitations recorded on the section apply directly to this question [[milan-finality]]:

1. **"SF2 retains Article 70(2) bilateral cancellation. SF3 is the relevant cash debit or securities debit for FoP."** — the exception is part of the rule, not a footnote to it, and SF3's trigger differs for FoP.
2. **"No insolvency runbook, legal opinion or unreviewed Article 72 remainder admitted."** — only Article 72(1)–(3) are in reviewed evidence. **Unresolved requirement:** whether Article 72 continues beyond paragraph 3, and whether any further paragraph adds an exception, a deferral or an insolvency-specific rule, is **not in reviewed evidence**. So I can state that Article 70(2) is the exception *named in Article 72(2)*, but I cannot certify that it is the only exception anywhere in the Regulations.
3. **Governing language.** The excerpt is the English edition of the Service Regulations in force as of 26 January 2026; the authoritative language is **Italian** and the Italian text prevails. For a legal opinion or a contractual citation, the Italian wording of Articles 70 and 72 must be used, not this translation [[milan-finality]].
4. **Approval status.** Source identity was checked, but there is no independent whole-edition supervisory approval certification [[milan-finality]].
5. **Review date.** This position was **reviewed on 13 September 2026**. That is a review date, not a statement that the text is unchanged at any later moment.
6. **Retrieval status.** The single retrieval in this bundle returned `evidence_only`; no retrieval returned `blocked`, `needs_context` or `needs_refresh`.

**Unresolved requirement — the wider legal frame.** Article 72(1) points outward to **Article 2(2) of Legislative Decree 210/2001**. That decree is not in this bundle, so the statutory definition of "entry into a system", its insolvency-protection effects and the moment from which those effects run under Italian law are **not in reviewed evidence** here. Nothing in this answer should be read as a legal opinion on the effect of SF1, SF2 or SF3 against an insolvency of a participant.

---

## Open items

1. **The remainder of Article 72 of the Service Regulations in force as of 26 January 2026** (any paragraph after 72(3)), to confirm whether further exceptions or insolvency provisions attach to SF1/SF2/SF3. Only 72(1)–(3) are admitted [[milan-finality]]. Route: the published Service Regulations on the Euronext Securities Milan documentation hub.
2. **The Italian original of Articles 70 and 72** of the same edition, since Italian is the authoritative language and this excerpt is an English translation [[milan-finality]]. Route: the Italian edition of the Regolamento dei Servizi on the same hub.
3. **Legislative Decree 210/2001, Article 2(2)** — referenced by Article 72(1) but not in reviewed evidence. Route: the Italian official gazette / consolidated statute text.
4. **The Instructions ("Istruzioni")** — Article 70(3) and 70(7)(b) both defer to the Instructions for the methods and time frames of cancellation and for the time limits that trigger automatic cancellation. Those methods, time frames and time limits are **not in reviewed evidence**, and no cut-off time may be inferred here. Route: the Instructions accompanying the Service Regulations on the Euronext Securities Milan hub, with client-only material via MT-X.
5. **An insolvency runbook or legal opinion**, expressly excluded from this section [[milan-finality]], if the question behind this one is the effect of irrevocability in a default scenario.
