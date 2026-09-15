# Client test pack for Tax Services - Relief at source Belgium (Issuer CSD)_v2(Track changes)

Source: https://www.euronext.com/sites/default/files/2026-05/euronext_securities_client_test_pack_for_tax_services_relief_at_source_Belgium_%28Issuer-CSD%29_v2_track%20changes.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

Guidelines to Euronext European Offering Client Test Pack
for Tax Services – Relief at Source Belgium (issuer CSD)TAX
BELGIAN - ISSUER


1.   Tax Services – Relief at Source Belgium (issuer CSD) TAX BELGIAN -
    ISSUER testing is important, and a client win in the European Expansion
     context

Testing the Tax Services – Relief at Source Belgium (issuer CSD)Tax Belgian Issuer
service is critical for clients as Euronext expands its integrated European offering. This
service ensures that Belgian tax procedures are handled accurately and efficiently,
supporting regulatory compliance and operational excellence. By participating in these
tests, clients can validate the correct processing of tax profiles, breakdowns and
reporting, minimising risk and ensuring readiness for cross-border activity. This is not
only vital for regression assurance but also for adapting to evolving tax and reporting
requirements in a harmonised European environment.


Important: If you have opted for this service, you must participate in these tests to
ensure your systems are fully compatible and compliant.

This document provides guidance for new and existing clients engaging with the
Euronext European Offering. It covers how to access the test pack, interpret test cases
and scenarios, seek assistance and many more.

Basically, this document is written as a run book and guiding the reader through a
logical flow of questions, we believe any reader will have. It helps to put the test pack
material into best practice.

Clients can find detailed Services description documents at the following page:

European Offering Documentation | Euronext Securities





  © 2026, Euronext                                                             | 1 of 9



                                           PRIVATE

## PDF page 2

2.    Getting to the test pack documentation

The test pack is available via the Euronext client portal at the next location:
https://www.euronext.com/en/post-trade/euronext-securities/milan/membership/csd-
expansion-documentation


Detailed technical information, service descriptions, and connectivity requirements are
available on our webpage. Further details on connectivity options can specifically be
found in the Connectivity Service Description Document.

You will receive login credentials from your Euronext account manager.
Once logged in, navigate to the “Testing” section and select “European Offering Test
Pack”.
If you have not received your credentials, please contact your account manager or the
Euronext support team.


3.   What does the Euronext European Offering Test Pack contain?

The Client Test Pack is a comprehensive resource designed to support your testing
activities.
With the Client Test Pack, your testers will have everything required to efficiently
start, carry out and document the results of your testing activities.
First, it includes a range of test cases and scenarios. These comprehensive set of test
cases and test scenarios are covering all core functionalities of the Euronext European
Offering. Then main characteristics of the tests are:


■  They are prioritised as high, medium or low, to ensure that the most important tests
   are completed first.
■ Some tests are straightforward single-step cases, while others are multi-step
   scenarios, providing thorough coverage of your requirements.
■  Each test is tailored to a specific service, user role and set of test conditions.
■  All tests have a similar structure like description, preconditions, steps to execute,
   expected results, and references to related documentation.
■  The tests are delivered in a simple tabular structure in Excel. Doing so makes our
   test case and scenarios accessible, tool independent and should allow you to upload
  them in most test management tools. To upload the tests, you may need to apply
  some mapping rules (please refer to the instructions of your test management tool
   in this case)




  © 2026, Euronext                                                             | 2 of 9



                                           PRIVATE

## PDF page 3

In the tabular list of test cases/scenarios for Tax Services – Relief at Source Belgium
(issuer CSD)TAX BELGIAN - ISSUER, the reader can find the tests required to validate
the next elements:


          Area tested                          Description
 BO profile creation and upload         Tests the creation and upload of beneficial
                                 owner (BO) profiles via Excel files.
 Tax document verification              Validates the setup and verification of tax
                                 documents and account segregation.
 Tax breakdown processing           Checks the processing  of tax breakdowns
                                    through SWIFT messages (MT565, MT567,
                                 MT564, etc.).
 Tax reversals and cancellations        Assesses the handling of tax reversals and
                                          cancellations.
 Tax report generation                   Verifies the generation and accuracy of tax
                                         reports.
 Event creation (DVCA, DVOP, DVSE)   Tests the creation of different tax event types
                                 and their correct processing.
 Manual and offline processing          Includes steps  for manual adjustments or
                                              offline processing when required.


Roles involved:

■  Issuer: Initiates and approves tax-related operations.
■  Custodian: Manages client accounts and ensures correct tax processing.
■  System administrator: Oversees technical setup, uploads and manual interventions.
■  Tax authority (indirect): Receives and reviews tax reports and breakdowns.

Activities tested:

■  Creation and upload of BO profiles
■  Verification and setup of tax documents
■  Processing and validation of tax breakdowns and reversals
■  Generation and review of tax reports
■  Manual and offline processing steps

Typical results checked:

■  Accurate creation and upload of BO profiles
■  Correct processing of tax breakdowns and reversals
■  Timely and compliant generation of tax reports

  © 2026, Euronext                                                             | 3 of 9



                                           PRIVATE

## PDF page 4

■  Proper handling of manual and offline processes
■  Full traceability and auditability of all tax-related actions

These tests are prioritised as high and ensure that the Tax Services – Relief at Source
Belgium (issuer CSD) Tax Belgian Issuer service delivers robust, compliant and efficient
solutions for clients operating in an expanding and harmonised European market.


Clients can find detailed Services description documents at the following page:
European Offering Documentation | Euronext Securities


Next, the exhaustive overview of the template items and a short explanation can be
found here:
                                                                                Used for
                                                                                     Euronext test
 Ref_Key                 Status of test case
                                                                                            praparation
                                                                                                only



                                                                                     High Priority

                               Test relevance gives the tester a clear indication of the
 Priority                  importance of the test. High Priority test cases and scenarios
                              are to be executed first. The different indications can be:
                                                                        Medium Priority

                                                                         Low Priority

                                                                                    Not to be
                                                                                                tested


                                                                               Under
                                                                                          Construction
                             This field is not relevant for test execution but is used only to
 Test Design Status*
                                             track the test design activities.
                                                                                Review ongoing

                                                                                Approved by PO

 TEST Case               Numerical ID of the test case

 ETA                     Planned date for completion

 Main Topic              General topic object of the test case

 Functionality              Specific functionality of the test case

 Application               Application or module being tested

 Role / User Profile      Type of client targeted by the test case



  © 2026, Euronext                                                             | 4 of 9



                                           PRIVATE

## PDF page 5

 Pre-requisites           Conditions or setup needed before testing

 Dependencies            Tests or systems that must be completed first

 References              Related documents or requirements

 Description               Detailed description of the test case

 Expected Result          Anticipated outcome of the test





                                                                     To Do




 Testing status                                Specify test outcome

                                                                        Passed

                                                                                     Failed

                                                             On Hold

                                                             N/A

                                                                           Blocked

 Testing Comments      Report notes / comments if needed

 Last Day Execution      Specify test execution date

 BUG Ref                    Identifier for any bugs found


Second, the pack also contains clear references to the test data to be used, as well
as all the documentation you will need to begin, execute and report on your tests. In
our test pack we have the particular ISIN-codes included for your testing.

Third, there are guidelines for conducting the tests (covered by this document)
ensuring you have step-by-step support throughout the process.





  © 2026, Euronext                                                             | 5 of 9



                                           PRIVATE

## PDF page 6

4.   What is the test execution process to follow?

   1. Register for the tests

     You should complete your registration for the tests by submitting the form via
      the link below:

      European Expansion - Client Testing – Fill in form

   2. Familiarise yourself with the test pack

    We recommend that you first take some time to review the Client Test Pack
       materials. If you have any questions or need further guidance, please contact
     CSD.Onboarding@euronext.com

           a. Review all materials in the Client Test Pack to understand the scope,
             objectives and structure of the tests.
          b. Refer to the guidelines and contact points if you need clarification.
            c.  Participate to the preparation meetings that will run before the Client Test
            Execution Window opens. This is a great opportunity to raise any question
              related to the client test pack.

   3. Prepare for testing

           a. Ensure you have access to all required documentation, test data and tools.
          b. Confirm that all prerequisites or pre-conditions for each of the tests are
            met.

   4. Select tests to execute

           a. Start with high priority tests, as indicated in the test pack.
          b.  If a specific sequence is provided, follow the order prescribed in the table.

   5. Execute the test

           a. Follow the steps described in the test case or scenario.
          b. To successfully execute any of the tests we advise the next steps:
            c.  If a specific order is indicated in the table, please follow that sequence.
          d.  If specific referential data is to be used, check if this is available for your
               test.
           e. Conclusion: before running a test, ensure that all prerequisites or pre-
             conditions are met.
              f.  Carefully perform each action as outlined.

  © 2026, Euronext                                                             | 6 of 9



                                           PRIVATE

## PDF page 7

          g.  If any test scenario would require a sequence of actions to be carried out
           by a role play of different actors (roles), please inform the next tester after
            your part of the steps has been completed. That way the workflow can run
              at high pace without waiting or interruption.

Important: Testing with Euronext Securities for the European Offering is conducted
using a dedicated test environment that mirror, as closely as possible, the target
production set-up. The environment is EUA (connected to T2S UTEST) and is made
available to support consistent and reliable test execution across all services in scope.

As a general principle, the test environment required for the European Offering is
available and operational during normal working hours throughout the testing period.
This availability applies across the different services and infrastructures from Euronext
Securities and is intended to provide participants with stable access for test execution,
analysis, and retesting activities.

The test environment will remain open also after the testing period is completed,
however please note that (1) sign-off must be completed as part of the testing period,
and (2) support from Euronext Securities can only be granted on an exceptional basis
after the testing period.

Any deviations from the standard availability described above, including exceptional
incidents or planned maintenance, will be communicated to clients in due time.

   6. Validate the outcome

           a. Compare the actual result with the expected result stated in the test pack.
          b. Note any differences or unexpected outcomes.

   7. Record the test status

           a. Update the status field for each test as executed, passed or failed. This is
            not mandatory and Euronext has no means to verify it. But you can log
             the outcome/status in the Excel sheet under the status field provided.
          b.  If you do so and you share the excel once a week with the Euronext Client
             Test Support team we can consolidate the information in a more factual
            dashboard.

   8. Report defects

           a.  If a defect is identified, document it according to the instructions provided
               in the test pack.
          b. Include all relevant details to support investigation and resolution.


  © 2026, Euronext                                                             | 7 of 9



                                           PRIVATE

## PDF page 8

   9. Repeat for remaining tests

           a. Continue with the next test, following the same process until all assigned
              tests are completed.

Important:  If you encounter any defects during testing, please report them as
described later in the document. We remind the client that Euronext will only track and
report based on the fact based information shared by the client or by our internal Client
Test Support members.


5.   Do we share the progress with others?

As described in the Client Test Strategy, there will be structural meetings organized
where any issue, defect, progress or question can be shared. Of course, confidentiality
will be kept in mind.
A report will be delivered soon after each meeting and shared on the portal to keep all
participants in the test execution informed.


6.   Where can I seek help if I encounter issues?

   ■  For technical issues or questions about the test pack, contact the Euronext
      support team at CSD.Onboarding@euronext.com.
   ■  For business or account-related queries, reach out to your Euronext account
     manager.
   ■  Additional resources, including user guides and FAQs, are available on the
      Euronext client portal.


7.    Additional Resources

   ■  Glossary    of   terms:   https://www.euronext.com/en/post-trade/euronext-
      securities/milan/membership/csd-expansion-documentation

   ■  Support contact details: CSD.Onboarding@euronext.com


8.   Conclusion

We are committed to supporting you throughout your onboarding and testing process.
Please do not hesitate to reach out for assistance or clarification at any stage.



  © 2026, Euronext                                                             | 8 of 9



                                           PRIVATE

## PDF page 9

© 2026, Euronext                                                             | 9 of 9



                                       PRIVATE