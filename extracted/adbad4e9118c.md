# Client test approach - addendum for clients of Euronext Securities

Source: https://www.euronext.com/sites/default/files/2026-03/euronext_securities_-_client_test_approach_-_addendum_for_clients_of_euronext_securities.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

Client Test
Approach

CSD European Offering –
Addendum for clients of Euronext Securities

VERSION 1.0





1

## PDF page 2

Table of contents

   1. Purpose of this document ...................................................................................................................... 3

   2. Target audience ..................................................................................................................................... 3

   3. Test preparation phase .......................................................................................................................... 3

     3.1 Euronext preparation ............................................................................................................................. 3

     3.2 Client preparation .................................................................................................................................. 3

   4. Test execution phase.............................................................................................................................. 5

     4.1 Testing timeline ...................................................................................................................................... 5

     4.2 Test scenario prioritization ..................................................................................................................... 6

     4.3 Guided test execution ............................................................................................................................ 6

     4.4 Entry & Exit criteria ................................................................................................................................ 7

   5. Roles & responsibilities .......................................................................................................................... 8

     5.1 Responsibilities of Euronext Securities................................................................................................... 8

     5.2 Responsibilities of clients of Euronext Securities ................................................................................... 9

   6. Defect management process ................................................................................................................ 10

     6.1 Defect identification and reporting ...................................................................................................... 10

     6.2 Defect handling and coordination ........................................................................................................ 10

     6.3 Defect resolution and retesting............................................................................................................ 11

   7. Environments & technical set-up ......................................................................................................... 11

   8. Reporting & KPIs .................................................................................................................................. 11

     8.1 Focus of reporting ................................................................................................................................ 11

     8.2 Key Performance Indicators (KPIs) ....................................................................................................... 12

   9. Readiness sign-off ................................................................................................................................ 12





2

## PDF page 3

1. Purpose of this document


This document is an addendum to the “Client Test Approach – CSD European Offering – General approach for
market participants” document, focused on specificities applicable only to clients of Euronext Securities which
are not mentioned in the “…General approach for market participants”. As for the target audience of this
document, the two documents must be read together for completeness of information in the following order:

    •   Client Test Approach – CSD European Offering – General approach for market participants
    •   Client Test Approach – CSD European Offering – Addendum for clients of Euronext Securities


2. Target audience


This document is intended for clients of Euronext Securities, in particular settlement agents, custodians, and
other CSD participants, involved in or impacted by the European Offering. While not all clients of Euronext
Securities are required to test the same services or scenarios, this document applies to all participants testing
Euronext Securities services. Variations in scope and obligations are described where applicable and detailed
further in the relevant test scenarios.


Note for Issuing Agents and Issuers
Due to the diversity of service configurations, timelines, and onboarding models applicable to these
stakeholders, testing with Issuing Agens and Issuers is handled on a case-by-case basis. Issuing Agents and
Issuers wishing to test services offered by Euronext Securities Milan are requested to contact Euronext
Securities (CSD.onboarding@euronext.com) to initiate tailored onboarding and testing activities aligned with
the specific needs of each Issuing Agent or Issuer.


3. Test preparation phase


3.1 Euronext preparation


Please refer to “Client Test Approach – CSD European Offering – General approach for market participants”
document, as the first document to read, for information about preparatory steps to expect from Euronext
Securities ahead of test execution, including information about detailed test documentation. Detailed test
documentation from Euronext Securities can be accessed following this link.


3.2 Client preparation


Clients are expected to complete the necessary preparation activities ahead of test execution. Timely
completion of these actions is critical to ensure that testing can start as planned. All clients must ensure they:

    •   Complete onboarding processes, if acting as a new participant
    •   Complete account set-up activities towards Euronext Securities

3 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 4

    •   Ensure access to the test environment (EUA, connected to T2S UTEST)
    •   Ensure access to relevant services introduced as part of the European Offering
    •   Verify connectivity is set-up to all relevant systems and networks (see more information below)
    •   Validate the accessibility and accuracy of test data provided by Euronext Securities
    •   Establish internal test governance and escalation procedures
    •   Establish clear internal processes for progress tracking and defect reporting
    •   Allocate appropriate resources and plan internal capacity for testing
    •   Nominate and share primary and backup points of contact with Euronext Securities
    •   Review and confirm understanding of the client test documentation
    •   Raise any difficulties, findings, or questions, related to the preparation to Euronext Securities


Connectivity to Euronext Securities’ services

To test and use services provided by Euronext Securities, clients must ensure that the appropriate connectivity
is in place before the start of testing. At a high level, the following connectivity options are available, with
indicative set-up timelines:


 Connectivity type                               Current connectivity clients1   Clients with no connectivity


 Euronext Managed Connectivity (EMC Solution)            2 weeks                   3 months


 Client Managed Connectivity (CMC Solution)               2 weeks                   3 weeks


 Indirect Connection (via Service Provider2)                2 weeks                   2 weeks


 VPN (for test only)                                   2 weeks                   2 weeks


Clients are responsible for initiating the connectivity process in due time based on their selected option. Please
note that VPN connectivity may be leveraged as back-up alternative for the above-mentioned connectivity
methods during the testing period, until permanent connectivity is established.


Detailed technical information, service descriptions, and connectivity requirements are available on our
webpage. Further details on connectivity options can specifically be found in the Connectivity Service
Description Document.





1 Upon contract signing. Please note that this is Euronext effort and is not including activities that client needs to execute
internally or with the Service Provider.
2 Currently supported Service Providers are BT Radianz, Colt, ICE, FNN, OptionsIT, Pico, TNS, NEXI, DXC, Bloomberg, Fidessa,
CQG, TradingTechnologies, iRess and others

4 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 5

4. Test execution phase


4.1 Testing timeline


As also shown in document “Client Test Approach – CSD European Offering – General approach for market
participants”, testing is planned and executed according to defined timelines per service according to the
overview below. For more information about testing timeline and milestones, please refer to the general
approach document referenced above.


 Services                  Feb    Mar     Apr      May          Jun             Jul      Aug


 Front-to-back testing                            Test execution: March 5th – July 31st


 ISO20022 Settlement                                                        Test execution:
 Messages via MQ channel                                             June 1st – July 31st


 Portfolio Migration and                          Test execution: March 5th – July 31st
 Position Transfer


 Corporate Events                                                   Test execution:
                                                May 4th – July 31st


 General Meetings and                                               Test execution:
 Proxy Voting                                      May 4th – July 31st


  Fiscal Services (Tax)                                                 Test execution
                                                May 4th – July 31s


 Post Trade Confirmation                         Test execution: March 5th – July 31st
 System (PTCS)


 Registered Shares and                                               Test execution:
 Information on Registered                             May 4th – July 31st
 Investors (IRI) – Euronext
 Securities as Investor CSD


 Registered Shares and                                                      Test execution:
 Information on Registered                                            June 1st – July 31st
 Investors (IRI) – Euronext
 Securities as Issuer CSD





5 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 6

 Services                  Feb    Mar     Apr      May          Jun             Jul      Aug


 Stamp Duty                                                         Test execution:
                                                May 4th – July 31st




4.2 Test scenario prioritization


Test scenarios provided in the test documentation from Euronext Securities are prioritized using a risk-based
approach, reflecting business criticality, regulatory impact, and operational risk. Scenarios are classified into
three categories: High Priority, Medium Priority, and Low Priority. The categories are defined below.


High Priority
These are critical test scenarios that must be executed. Failure to successfully complete these tests would
materially impact the usability, compliance, or stability of the service. For High Priority test scenarios, Euronext
will apply a guided test execution approach. These scenarios will be executed following a defined sequence
when explicitly indicated for the test. This approach is intended to focus the attention of all participants on the
same parts of the end-to-end process at the same time, enabling aligned execution, shared learning, and more
effective joint discussions on specific scenarios. By progressing through high-priority scenarios in a coordinated
manner, testing can flow more smoothly, dependencies can be identified earlier, and issues impacting multiple
participants can be addressed collectively. Further details on the sequencing and execution of high-priority
scenarios are described in the Test Execution section of this document.


Medium Priority
These are important scenarios that are strongly recommended. While not strictly required for go-live, they
significantly reduce operational risk and improve user confidence.


Low Priority
These are optional scenarios that add incremental value but are not required for the current release.


This prioritization ensures that testing efforts are focused on the most critical risks first, while allowing
flexibility based on participant readiness and available resources.


4.3 Guided test execution


High Priority cases: Guided execution of test scenarios
For high-priority test scenarios, Euronext Securities will apply a guided test execution approach. These
scenarios will be executed following a defined sequencing, which will be used as a reference during the regular
coordination meetings. Euronext Securities will actively guide participants through these scenarios to ensure
aligned execution and effective use of testing time.


As part of this guided approach:

    •   Required test data and references (ISINs or others) will be prepared and shared by Euronext Securities
          in the detailed test documentation, where applicable


6 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 7

    •   Dedicated test experts and subject matter experts will be available to support execution
    •   Daily support will be provided to address questions, clarify expected outcomes, and assist with issue
         analysis
    •   Outcomes of executed scenarios, identified issues, and next steps will be debriefed regularly to ensure
      common understanding across participants


This coordinated execution model is intended to focus all participants on the same critical scenarios at the
same time, facilitate collective discussion of findings and dependencies, accelerate issue identification and
resolution, and improve overall testing efficiency and readiness.


Medium- and Low Priority cases: Independent execution of test scenarios
For lower-priority test scenarios, guided execution will not be applied. Hence, for these test scenarios, clients
should execute testing independently and in line with the published test scenarios and guidance. Also, for
these test scenarios, Euronext Securities will provide functional and operational support throughout the
execution phase in line with the defined client support model.


4.4 Entry & Exit criteria


Entry, hold, resume, and exit criteria define the formal conditions under which testing activities can start, be
paused, resumed, or completed. They provide a controlled framework to ensure that testing is executed only
when the required prerequisites are met and that progression between phases is based on objective readiness.
These criteria are designed to protect testing quality, ensure efficient use of resources, and minimize
operational and delivery risk.


The principles and categories of criteria described in this section apply across all testing activities with Euronext
Securities for the European Offering services. The exact and detailed criteria are defined in the test plan for
each service, considering service-specific risks, dependencies, and participant roles.


4.4.1 Entry criteria

Entry criteria define the conditions that must be met before a testing phase can start. To support this, Euronext
Securities will organize preparatory meetings ahead of the client testing window to confirm readiness and
comfort to begin testing. These sessions are intended to identify and address any practical questions or
constraints related to test execution, such as resource availability, understanding of test scenarios and
supporting documentation, and client support arrangements. See document “Client Test Approach – CSD
European Offering – General approach for market participants” for more information. This approach ensures
that all parties are aligned and adequately prepared before testing starts.


4.4.2 Hold criteria

Hold criteria define situations where testing must be temporarily paused, in cases such as:

    •   Occurrence of unexpected blocking issues
    •   Introduction of unplanned or planned new deliveries or system versions
    •   Repeated or prolonged unavailability of required resources
    •   Interrupting scope changes impacting the validity of ongoing tests
    •   Change requests requiring additional risk assessment before continuation





7 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 8

When hold criteria are triggered, the testing phase is paused until the situation is assessed and resolved. Due to
the unpredictability of such event, the client test support panel will inform the relevant parties immediately
after detection. As soon as a timing for resume is known a communication will be shared by Euronext
Securities. This way clients can ensure the availability of resources and start testing again.


During the Hold-Resume time window, the frequency of the status meetings and reporting may increase to
keep all parties close in the loop and aligned when and as long as needed.


4.4.3 Resume criteria

Resume criteria define the conditions under which testing can safely restart after a hold. When testing can
resume relevant parties will be informed immediately. Testing may resume once:

    •   Required resources are available again or suitable replacements have been secured
    •   Blocking issues or interruptions have been resolved and validated
    •   The intake process has been successfully re-completed where applicable
    •  A clear resume signal has been communicated and acknowledged by all testing participants


4.4.4 Exit criteria

Exit criteria define the conditions that must be met for a testing phase to be considered successfully
completed. The recommended criteria to guide readiness and completion of the test execution are:

    •    All test cases market “High Priority” have been executed in line with the test plan
    •   In case of defects, they have been re-tested and closed
    •   Risks have been either mitigated or accepted
    •   Only mutually accepted issues remain (if any)
    •   Agreement to close the testing phase between Euronext and stakeholders


5. Roles & responsibilities


Executing test activities for the European Offering is a collaborative effort between Euronext Securities and its
clients, with specific responsibilities to be fulfilled by each. Responsibilities described in this section apply to
testing activities only, and the exact scope of testing and required actions are further detailed in the applicable
test plans and test scenarios.


5.1 Responsibilities of Euronext Securities


Euronext Securities is responsible for:

    •   Provide relevant test scenarios to execute for the relevant market participant segments interacting
        with Euronext Securities
    •   Providing and maintaining test environments and test data
    •   Supporting test execution involving settlement transactions and other relevant services offered by
        Euronext Securities to the market participants
    •   Supporting defect analysis, resolution, and retesting



8 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 9

    •   Confirming readiness for services in scope of the European Offering from Euronext Securities’
        perspective


5.2 Responsibilities of clients of Euronext Securities


Clients have a general responsibility to ensure that testing is executed in line with the agreed test plans and
timelines, that defects are reported following the defined defect management process, to ensure timely
communication and escalation of issues, and that formal readiness confirmations are provided where relevant.
Specific responsibilities are defined further below.


Settlement Agents
Settlement Agents are responsible for validating settlement processing and communication with CSDs. Their
key responsibilities include the following:

    •   Executing settlement-related test scenarios
    •   Validating connectivity, messaging, and operational processes
    •   Validating settlement instruction processing and confirmations
    •   Determining, at their own discretion, the number of Trading Members with whom testing is required
        to achieve sufficient confidence for sign-off on end-to-end market flow testing
    •  Where settlement involves other market infrastructures or alternative CSDs, assessing the need to
        perform testing with those infrastructures and coordinating such testing directly with the relevant
         parties; testing with Euronext Securities will be supported as part of the European Offering testing
    •   Reporting defects
    •   Confirming operational readiness via dedicated form


Custodians
Custodians are responsible for validating safekeeping, settlement, and asset servicing flows relevant to their
role. Their key responsibilities include:

    •   Executing relevant test scenarios
    •   Validating connectivity, messaging, and operational processes
    •   Reporting defects
    •   Confirming readiness for services in scope

Issuing Agents3
Issuing Agents are responsible for validating issuance-related and issuer-facing services. Their key
responsibilities include:

    •   Executing test scenarios related to issuance and issuer services
    •   Validating new tools, interfaces, and reporting
    •   Coordinating with issuers and Euronext Securities on issue resolution
    •   Involve registrars as needed in testing





3 Issuing Agents and Issuers should contact Euronext Securities directly for tailored onboarding and testing.

9 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 10

Issuing Agents typically act on behalf of Issuers for operational matters, including testing and onboarding,
unless otherwise defined between the parties.


6. Defect management process


Defect management is a key component of the European Offering testing activities for Euronext Securities. The
objective is to ensure that defects identified during testing are captured, assessed, communicated, and
addressed in a transparent and coordinated manner, while avoiding duplication of effort across participants.


6.1 Defect identification and reporting


Defects may be identified by any market participant during test execution. Participants are encouraged to
report defects as soon as they are discovered to allow timely analysis and mitigation.


Defects can be reported through:

    •   Bilateral communication4, where a participant identifies and reports a defect directly, and
    •   Regular testing coordination meetings, where defects can be raised, discussed, and tracked
          collectively.


6.2 Defect handling and coordination


Once a defect is reported, Euronext Securities will analyse and assess the reported issue, including its impact
and priority. Where relevant, the defect and its status will be shared with the wider testing community to
increase transparency, prevent multiple participants from testing the same failing scenario, and align
expectations on known limitations or fixes in progress. Follow-up actions, including resolution, workaround, or
retesting, will be coordinated with impacted participants.


To support structured coordination, Euronext Securities will maintain a central defect tracking file, covering all
defects, statuses, priorities, and next steps. This file will be shared with relevant stakeholders ahead of each
recurring test coordination meeting and will serve as the single reference point for discussion, alignment, and
progress tracking during testing.


This collaborative approach supports efficient testing execution, maximizes reuse of test outcomes, and
reduces unnecessary duplication of testing efforts. Any client-specific or confidential information will not be
shared.





4 See document “Client Test Approach – CSD European Offering – General approach for market participants” for detailed
point of contact.

10 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 11

6.3 Defect resolution and retesting


Defects are addressed based on their severity, business impact, and relevance to go-live readiness. Once a fix
or mitigation is implemented impacted participants will be informed, retesting will be organized as required,
and outcomes will be communicated through the established testing communication channels.


7. Environments & technical set-up


Testing with Euronext Securities for the European Offering is conducted using a dedicated test environment
that mirror, as closely as possible, the target production set-up. The environment is EUA (connected to T2S
UTEST) and is made available to support consistent and reliable test execution across all services in scope.


As a general principle, the test environment required for the European Offering is available and operational
during normal working hours throughout the testing period. This availability applies across the different
services and infrastructures from Euronext Securities and is intended to provide participants with stable access
for test execution, analysis, and retesting activities.


The test environment will remain open also after the testing period is completed, however please note that (1)
sign-off must be completed as part of the testing period, and (2) support from Euronext Securities can only be
granted on an exceptional basis after the testing period.


Any deviations from the standard availability described above, including exceptional incidents or planned
maintenance, will be communicated to clients in due time.


8. Reporting & KPIs


Reporting during the European Offering testing is designed to support transparency, coordination, and issue
resolution, while avoiding unnecessary administrative overhead for clients.


A key principle of the testing approach is that Euronext Securities will monitor that its applications and services
are delivered as planned, while clients are expected to perform the testing relevant to their role and services in
line with the published test documentation and to raise any concern in timely manner. The primary focus of
reporting is therefore on issues, risks, and overall readiness, rather than on detailed test execution metrics.


Reporting is organized to facilitate efficient coordination and timely resolution of issues identified during
testing. It is supported through regular coordination meetings, targeted written updates where relevant, and
ongoing bilateral exchanges to address specific issues or clarifications. Reporting activities are centred on
shared understanding of the testing situation, known limitations, and actions required to ensure overall
readiness.


8.1 Focus of reporting


Reporting during the testing period focuses on the following areas:



11 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 12

Defects and issues

    •   Identification of new defects and/or issues raised during testing
    •   Status of open, resolved, and blocking defects
    •    Visibility on known defects and/or issues impacting multiple participants


Risk and impact assessment

    •   Identification of risks that could impact service readiness or timelines
    •   Assessment of the operational or functional impact of identified defects


Resolution and mitigation

    •   Progress on issue resolution and planned fixes
    •   Agreed workarounds or mitigations where applicable
    •   Coordination of re-testing where required


Key dependencies and constraints

    •   Dependencies between services or participants
    •   Constraints that may impact testing efficiency or readiness


8.2 Key Performance Indicators (KPIs)


KPIs used during testing are limited and targeted and are intended to support issue management and readiness
assessment rather than to measure client testing performance. Indicative KPIs include:

    •  Number of open defects by severity per service
    •  Number of unresolved blocking issues per service


These indicators are reviewed regularly as part of the testing governance to identify areas requiring additional
focus or support.


9. Readiness sign-off


Please refer to document “Client Test Approach – CSD European Offering – General approach for market
participants” for information regarding readiness sign-off. Relevant sign-off documentation can be found on
the European Offering Documentation website.





12 | European Offering – Client Test Approach – Addendum for clients of
Euronext Securities – V1.0

## PDF page 13

                                       CHAPTER TITLE, VERDANA 9PT, RIGHT ALIGNED





                      euronext.com


13 | Subtitle text, Verdana 9pt, Left aligned

                                           PRIVATE