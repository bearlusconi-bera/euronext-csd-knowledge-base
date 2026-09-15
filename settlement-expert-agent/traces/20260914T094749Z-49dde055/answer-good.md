**Direct answer.** No. "Matched" means T2S has compared the two instructions and found them consistent; it does not mean securities or cash have moved.

**Documented requirements**
- Matching compares the settlement details provided by deliverer and receiver so both agree on the terms [[t2s-matching]] T2S UDFS R2026.JUN §1.6.1.2, PDF 267–271; reviewed 13 September 2026.
- Settlement happens in the posting process, which checks eligibility and resources and then books the movement, "resulting in the irrevocability of the settlement" [[t2s-posting]] UDFS §1.6.1.8.1, PDF 303–304; reviewed 13 September 2026.
- For Monte Titoli, matching is the point of irrevocability (SF2) "without prejudice to the bilateral cancellation" under Article 70(2); the transfer becomes final only at the debit of the cash, or of the securities for FoP (SF3) [[milan-finality]] Milan Service Regulations 26 January 2026, Articles 69–72, PDF 50–51; reviewed 13 September 2026; English translation, the Italian text prevails.

**Reasoned inference.** A matched status is therefore an intermediate status; your client "has the shares" only when the securities posting is confirmed.

**Open items.** Confirmation semantics on your local interface (X-TRM relays) are not in this bundle.
