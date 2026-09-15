QUESTION FROM THE USER:
What is the fee for a cross-CSD DvP settlement instruction at Euronext Securities Milan?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:55:46.769026+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "fee_amount"}
STATUS: blocked — Exact tariff row, service, charging basis, currency and transaction date must be reviewed.
GAP IDS: ['G17']

=== RETRIEVAL 2: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_cross_csd_rule"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-cross-csd-disclosure]] — Cross-CSD settlement rule and disclosure of settlement progress (Articles 77–78) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Regulations as of 26 January 2026 | Articles 77–78 with footnote 8; PDF 54, printed 53 | version 26 January 2026 | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-13 | url https://www.euronext.com/sites/default/files/2026-02/01%20REG_UNICO_ENG_WITHOUT%20EV_26012026.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt.
LIMITATION: Article 77(2) excludes cross-CSD settlement when the issuer CSD is outside T2S unless both investor CSDs hold a link avoiding realignment with it; actual links per ISIN are not certified.
EXCERPT (Articles 77–78 with footnote 8; PDF 54, printed 53):
Article 77 – Cross CSD Settlement

1.  If the settlement Instructions are to be settled between a Participant in Monte
    Titoli, different from another CSD in T2S and a participant in another CSD in
   T2S (cross CSD), T2S shall automatically carry out the movements between
   the securities accounts of the participants involved, of the Investor CSDs and
   of the Issuer CSD.
2. Monte Titoli does not envisage the possibility of carrying out a cross CSD
   settlement on securities  if the Issuer CSD  is outside of T2S, unless both
   investor CSDs have in place a link with another CSD in T2S so that the
   realignment with the Issuer CSD outside T2S is not necessary.

Article 78 – Disclosure regarding the progress of the process

1.  If requested by the Participants, Monte Titoli makes available the events that
   change the balance in their securities account, supplying in real time the
   settlement status of each transaction being processed,  all the information
   useful for monitoring it, as well as the settlement of the whole transaction. This
   disclosure is made available through the direct link channel to T2S, or through
   the X-TRM Service.
2.  If requested by the participants, Monte Titoli also makes available to the
   participants and/or to their agent bank the cash balance disclosure. This
   disclosure is processed and made available, according to the format and with
   the channels indicated in the Services Manuals.8

=== RETRIEVAL 3: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_settlement_service_scope"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-service-scope]] — Settlement Service scope: intra-CSD and cross-CSD, ICP versus DCP processing (§1.3 excluding the operational-day clock table) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | §1.3 opening; PDF 12, printed 8 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: §1.3.1 (PDF 12–16) is quarantined: its clock values (NTS 19:30, two partial windows) conflict with the deployed R2026.JUN schedule; use the T2S schedule sections and the notice chain instead.
EXCERPT (§1.3 opening; PDF 12, printed 8):
1.3 OPERATION OF THE SETTLEMENT SERVICE

The Settlement Service is operated by the T2S platform and enables settlement
of transactions:

    •  between two Participants in Monte Titoli (cd. Intra CSD Settlement);

    •  between a Participant in Monte Titoli and a participant in another CSD in
     T2S (cross-CSD settlement), within the limits laid down in Article 27 of the
      Operating Rules;

Participants may enter settlement instructions to be settled in modality intra and
cross CSD through connectivity models directly or indirectly.

Settlement Instructions entered through indirect connection, before forwarding
to T2S shall be subject to the processes specified in the subsequent chapter
relating to the X-TRM Service.

Settlement Instructions entered through a direct connection are subject only to
the processes provided by T2S platform.

Although not expressly specified or detailed in this document, with reference to
the acquisition mode, matching and settlement of transactions, please refer to
Document Operating T2S User Requirements.