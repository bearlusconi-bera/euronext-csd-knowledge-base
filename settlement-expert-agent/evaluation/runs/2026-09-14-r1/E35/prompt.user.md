QUESTION FROM THE USER:
What happens to my pending instructions if my counterparty at Monte Titoli becomes insolvent?

Answer only from the EVIDENCE BUNDLE below. Cite each supporting section as [[section-id]] with its locator, review date and qualifications. Disclose every retrieval status that is not evidence_only. Do not use any other knowledge as evidence.

EVIDENCE BUNDLE (retriever build f9493d10a6f6, generated 2026-09-14T09:53:15.454728+00:00). Review dates available: 2026-09-13, 2026-09-14.

=== RETRIEVAL 1: context {"as_of": "2026-09-14", "entity": "Milan", "service": "settlement", "role": "participant", "mode": "current", "question_type": "milan_default_procedure"}
STATUS: evidence_only — Only the named propositions and their conditions are supported. Classifying the question and composing a faithful answer remain separate tasks.

--- SECTION [[milan-default-procedure]] — Default management procedure: notification, blocks, cancellation table and cross-CSD hold (Title 4) (reviewed 2026-09-14; modes ['current']; entities ['Milan']; basis reviewed_effective_interval)
CITATION: Instructions to Settlement Service and related instrumental activities - in force as of 30 June 2025 | Title 4 §§4–4.4; PDF 71–75, printed 67–71 | version Settlement Service Instructions in force as of 30 June 2025 (MN_10/2025) | body language en | authoritative language it | translation; authoritative language differs | approval: Source identity checked; no independent whole-edition supervisory approval certification | source reviewed 2026-09-14 | url https://www.euronext.com/sites/default/files/2025-07/03%20Settlement%20Service%20Instructions_30062025_WITHOUT%20EVIDENCE.pdf
LIMITATION: Italian text prevails (cover, PDF 1). English translation excerpt with uneven wording; quoted terms follow the source.
LIMITATION: Cross-references to Article 57/59 numbering reflect the 2025 Instructions; the 2026 Regulations renumbered articles (e.g. Article 59 categories).
EXCERPT (Title 4 §§4–4.4; PDF 71–75, printed 67–71):
4 DEFAULT MANAGEMENT PROCEDURE


The procedure applies to  all the settlement instructions (related to trades),
repurchase agreements and compensation securities and / or cash and resulting
from guaranteed market transactions, non guaranteed market transactions and
OTC) entered for settlement on Monte Titoli Settlement System and related to
the  Participants and  /  or  indirect  participants, pursuant the  to  Article 59,
paragraph 5 of the Service Regulations.

If a Participant or Indirect Participant defaults, the procedure activated by Monte
Titoli is divided into the following phases:
      1.  Receipt of the declaration of default;
      2.  Interventions on the  settlement system  in  order  to manage  the
      transactions of the insolvent entity.
 The following definitions apply for managing insolvencies:
 -   “time of insolvency” or “TOI”, the moment an insolvency proceeding is
    opened pursuant to article 3 of Legislative Decree 210/2001;
 -   “time of awareness” or “TOA”, the moment Monte Titoli becomes aware of
     the insolvency status of one of its Participants or Indirect Participants.

4.1 RECEIPT OF THE DECLARATION OF DEFAULT

This procedure applies when Monte Titoli is notified of a default, declared in Italy
or another EU country or extra-EU, pursuant to Article 3(6) of Legislative Decree
210/2001.

The procedure is activated by Monte Titoli:

    •  upon receipt of the notification from the Bank of Italy, or

    •  when Monte Titoli is aware of insolvency in the manner required by the
      operational procedures for crisis management, defined in agreement with
      the T2S System Operator; or by written note by a Participant or of a
       central counterparty provided that the notice specifies that the sender "
      under its own responsibility gives notice of the opening of an insolvency
      procedure under Legislative Decree 210/2001 against [name, LEI code,
     CED code, ABI code of the insolvent participant]. This communication must
     be made by the legal and/or contract representative of the Participant or
       central counterparty.





67



[PDF page 72]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





To this end Monte Titoli has a procedure in place with the Bank of Italy that
provides for  it to receive notifications ex art. 3 comma 6 e 9 del D. Lgs. N.
210/2001 at the following dedicated address:

BINnotifyMT@lseg.com

so as to ensure the prompt receipt and appropriate handling of notifications and
the timely communication of the moment and the way in which Monte Titoli has
been informed of the opening of default proceedings and the operations that
follow:

 Immediately upon receiving notification, Monte Titoli:
 a)  in the case of the insolvency of a Participant, actives the Settlement System
    technical  procedures  to  block:   i)  the  acquisition  of new  settlement
    instructions in the Settlement System that are attributable to the insolvent
    Participant; and  ii) amendments to settlement instructions already in the
    Settlement System that are attributable to the same entity;
   To this end, Monte Titoli: (i) blocks the acquisition of settlement instructions
     in the Settlement System that are attributable to the insolvent Participant;
      (ii) for direct connections, prevents the insolvent Participant from sending
   new settlement instructions to the Settlement System, or from amending
    Instructions already in the System;
 b)  in the case of insolvency of an Indirect Participant, blocks the acquisition of
    settlement instructions in the Settlement System that are attributable to
    the  insolvent  Indirect  Participant;  allows  the  Participant  that  settles
    transactions on behalf of the Indirect  Participant to issue, on  its own
    responsibility and  within 2  business  days  (not  including  the day  of
     notification), new settlement  instructions on the accounts pursuant  to
     article 57, paragraph 5, letter b) of the Regulation, for the sole purpose of
    exercising retention rights and guarantee rights, within the limits permitted
   by law;
 c)  cancels the intra-CSD settlement instructions already in the Settlement
   System  that  are  attributable  to  the  insolvent  Participant  or  Indirect
    Participant that have already been acquired by the Settlement System,
    according to methods and timing set out in Chapter 4.2;
 d) puts a hold on the cross-CSD settlement instructions attributable to the
    insolvent  Participant  or  Indirect  Participant  already  in  the  Settlement
    System, according to methods and timing set out in Chapter 4.3;
 e) cancels  the  settlement  instructions from  the X-TRM  Service  that  are
    attributable to the insolvent Participant or Indirect Participant that have not
    yet been input in the Settlement System;
 f)  informs the Participants in the Settlement Service of the activation of the
    default management procedure, specifying the TOI and the TOA.




68



[PDF page 73]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





As regards the notification of the default to the participants, in order to ensure
the unambiguous  identification  of  the  participant  that  has been  declared
insolvent, Monte Titoli will communicate the LEI code, the CED code and/or the
ABI code and the corresponding settlement account of the default Participant or
Indirect Participant.

Again, with the aim of ensuring the adequate dissemination of the information,
Monte  Titoli asks participants to keep the data of the subjects Monte  Titoli
must/can contact for the purposes of the default management procedure for the
same Participants or the clients of Indirect Participants updated (names, mailing
list, phone numbers, etc.).

This data is collected through the CLIMP application.

4.2 CANCELLATION OF INTRA-CSD SETTLEMENT INSTRUCTIONS
Monte Titoli will proceed with cancelling the intra-CSD settlement instructions in
the Settlement System that are attributable to the insolvent Participant or
Indirect Participant according to methods and timing set out in the following
table.


       Settlement instructions              Monte Titoli interventions


Entered  prior  to  TOI  and  with  ISD   Are cancelled at the end of ISD,  if not
subsequent to the insolvency date            settled


Entered prior to TOI and with ISD equal to   Are cancelled at the end of the day of the
or prior to the insolvency date                insolvency, if unsettled


Entered after TOI, observed prior to TOA
and   with  ISD   subsequent   to   the   Are cancelled as soon as possible
insolvency date


Entered after TOI, observed prior to TOA
                                         Are cancelled if unsettled at the end of the
and with ISD equal  to or  prior to the                                      day of insolvency
insolvency date


Entered after TOI and observed after TOA    Are cancelled as soon as possible





69



[PDF page 74]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





Notwithstanding  the  manner  and  timing  indicated  above,  for  settlement
instructions attributable to transactions guaranteed by a central counterparty
that uses the X-TRM Service to calculate balances (“CCP”), the following apply:

   a) In the case of insolvency of an Indirect Participant that is a “client broker”
      (“NCM”) tied to a CCP member entity (“GCM”), Monte Titoli cancels only
      those settlement instructions created between the NCM and GCM that are
       in the Settlement System, while instructions between GCM-CCP continue
       to be settled. If the settlement instructions were created directly between
    NCM - CCP, these settlement instructions are cancelled and together with
      the CCP are re-instructed to a securities account communicated by the
    GCM to the CCP;

   b) In the case of insolvency of a Participant or Indirect Participant that is an
       individual or general CCP member, Monte Titoli will cancel all settlement
       instructions between the Participant, or Indirect Participant, and the CCP,
      present in the Settlement System as soon as possible.


4.3 INTERVENTIONS ON THE SETTLEMENT INSTRUCTION CROSS-CSD

In the case of default from a Direct or Indirect Participant to the Settlement
Service, Monte  Titoli applies the interventions set out in paragraph 2 to the
cross-CSD  settlement  instructions,  substituting  settlement  cancellation  with
suspension (hold).

The cross-CSD settlement instructions on hold are subsequently assigned a
unilateral cancellation status by Monte Titoli so that any cancellation requests
entered by the counterparty (bilateral cancellation) may be processed by the
Settlement System.

In the case of default of a participant in another CSD in T2S, shall apply the rules
established by CSD  of the  insolvent  subject, except  for the  possibility  for
Participants of Monte Titoli to suspend liquidation of the settlement Instructions
of offsetting to the default subject.


4.4 INTERVENTIONS ON SETTLEMENT INSTRUCTIONS TO BE SETTLED
   WITHIN THE FOREIGN SETTLEMENT SERVICE

In the event of default of a participant in the Foreign Settlement Service, upon
receiving notice pursuant to Chapter 4.1, Monte Titoli:

- cancels the settlement instructions related to the participant in the X-TRM
Service, not yet forwarded to the Foreign CSD.




70



[PDF page 75]

          INSTRUCTIONS TO SETTLEMENT SERVICE, AND RELATED INSTRUMENTAL ACTIVITIES





In the case of default by an entity that a Participant had identified as an Indirect
Participant pursuant to article 57, paragraph 5 of the Serivice Regulations, upon
receiving notice pursuant to Chapter 4.1, Monte Titoli:

-  cancels  the  settlement  instructions  from  the X-TRM  Service  that  are
attributable  to  the  insolvent  Indirect  Participant  that have  not  yet been
forwarded to the Foreign CSD;





71