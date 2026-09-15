# SRD II – Identification of Beneficial Holders

Source: https://www.euronext.com/en/csd/porto/legislation-and-regulation/shareholders-rights-directive/srd-ii-identification-beneficial

Retrieved: 2026-09-11

SRD II – Identification of Beneficial Holders
On September 3, 2020 Euronext Securities Porto adapted the identification of beneficial holder process in order to be able to receive information from the financial intermediaries all over the intermediation chain and to comply with one of the main objective of the Shareholders Rights Directive – allow the identification of the final investors
Identification of Beneficial Holder Process
Issuer requests
How to make a request:
The request for the identification of beneficial holders must be made by the Issuer or other entity duly mandated for this purpose – Issuer’s Agent, through the private area of Euronext Securities Porto web portal –My INTERBOLSA.
How to cancel / change a request:
Through My INTERBOLSA is also possible to cancel a request for the identification of beneficial holders until record date and update the issuer deadline of the request.
In case of requests with a reference date in the past (up to 1 year), the request can only be cancelled until its notification.
Notification of the request
The requests received and validated by Euronext Securities Porto are subsequently notified to its Participants:
On the same day the request is received;
Until 10 am on the next business day, if the request was received after 4 pm.
The notification is made through the:
STD: message NOTIDTIT – Notification of the Securities Holders Identification Request;
ISO 20022: message seev.045 – Shareholders Identification Disclosure Request, if previously subscribed.
The request for the identification of beneficial holders registered in Euronext Securities Porto systems and which are still active can be consulted in the IDE-TIT – Holders Identification file, available in the STD
Positions to be identified
At the end of the Record Date Euronext Securities Porto Participants with a position in the security subject to the identification of beneficial holders’ request receive, via STD, the PNA file – Identification of Securities Holders Request, with the positions to identify.
In case of requests with a reference date in the past (up to 1 year), the PNA file is sent at the end of the day the request is notified.
Identification of Securities Holders
Files to send:
1 – Euronext Securities Porto Participants:
For the identification of securities holders, Euronext Securities Porto Participants must send:
Via STD:
FIA file – Securities Holder Identification, with the information related to the holders
DPN file – Identification of the Securities Holders, with the detailed identification of the account positions
Via ISO 20022:
Message seev.047* – Shareholders Identification Disclosure Request
*If previously subscribed
2 – Financial Intermediaries over the intermediation chain:
Financial intermediaries that are not Euronext Securities Porto participants, or are at the next levels in the intermediation chain, must send to Euronext Securities Porto :
Via ISO 20022:
Message seev.047* – Shareholders Identification Disclosure Request
*If previously subscribed
Via My INTERBOLSA:
DPN-CLI FILE - Identification of the Securities Holders by Third Intermediaries
To register with My INTERBOLSA, financial intermediaries who are not Euronext Securities Porto participants must contact Euronext Securities Porto at centralgi@euronext.com.
Deadline for the answer:
In case the security is under the scope of Shareholders Rights Directive, the information for the identification of the beneficial holders must be sent during the business day immediately after the Record Date.
In case the security is out of the scope of the Shareholders Rights Directive, the information for the identification of the beneficial holders can be send up to the third business day immediately after the Record Date.
Requests with reference date in the past (up to 1 year):
In case of the reference date in the past, differs up until 7 days of the request date of the Issuer, the sending of the information, must be performed until the fifth day after the request date.
In case of the reference date in the past, is larger than 7 days, or until one year, of the request date of the Issuer, the sending of the information, must be performed until the tenth day after the request date.
Beneficial holder scheme
The process of beneficial holder identification is carried out according to the following scheme:
① – Issuer sends the request to Euronext Securities Porto through My INTERBOLSA
② – Euronext Securities Porto validates the request
③ – Euronext Securities Porto sends the notification of the request to its Participants, through STD (NOTIDTIT) or ISO 20022 messages (seev.045), if previously subscribed
④ – On record date after the end of day Euronext Securities Porto sends to its Participants, through STD, the positions to be identified (PNA file). For requests with a reference date in the past (up to 1 year) the PNA file is sent at the end of the day the request is notified
⑤ – Euronext Securities Porto Participants send, through STD, the information of the end investors identification (FIA file) and the detailed securities positions (DPN file) or through ISO 20022 messages (seev.047), if previously subscribed. For the financial intermediaries over the custody chain the information must be sent by ISO 20022 messages (seev.047), if previously subscribed, or through My INTERBOLSA - DPN-CLI file
⑥ – Euronext Securities Porto validates the information received
⑦ – Euronext Securities Porto sends the status advice of the information received
⑧ – Euronext Securities Porto consolidates the information received
⑨ – Euronext Securities Porto sends to Issuer, through My INTERBOLSA, the information of the end investors identification (DN file)
Support Documentation
PDF
Identification of Securities Holders (Layouts)
English
Version
/sites/default/files/2024-01/Identification%20of%20Securities%20Holders%20-%20Layouts%202023.pdf
Identification of Securities Holders (Layouts)
English
nmarsali@euron…
13/07/2023
XLSX
DPN-CLI file EN
English
Version
English
15/02/2024
DPN-CLI file EN
/sites/default/files/2024-02/202203_DPN_CLI%20excel-layouts-EN.xlsx
