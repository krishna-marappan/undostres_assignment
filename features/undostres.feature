Feature: Use Python-selenium to automate the Undostres web application.

  Scenario: validating recarga celular and ensuring successful recharge
      Given user,he or she is to launch an undostres website
      When user fills in the Recarga Celular details, click on the siguiente
      Then the user is able to reach the next screen (Payment screen)
      When the user is able to enter payment information
      And the user is able to fill Access with mail fields
      Then the user gets a success message and the recharge is successful
      And users close all open browsers