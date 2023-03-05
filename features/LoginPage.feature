# Created by Indrani at 27-02-2023
@Functionaltests
Feature: Payback Login page

  Background:
    Given Launch Chrome Browser and Payback Application
    When User clicks on Login Page icon

  Scenario:To Validate user navigation to Login page
    Then User is navigated to Login Page

  Scenario: To Validate that Clicking anywhere on #Payback Chalao picture redirects to Sign up page
    When User clicks on Sign Up #Payback Chalao Picture
    Then User is navigated to Join Now page

  Scenario: To Validate that Login Button is clickable
    When User enters 9999999999 in PAYBACK card number or Mobile Number field
    And User enters 9999 in Pin field
    And User selects Check Box on reCAPTCHA
    Then Login Button is Clickable


  Scenario Outline: To Validate that user is successfully Logged into to payback account
    When User enters <validnumber> in PAYBACK card number or Mobile Number field
    And User enters <validpin> in Pin field
    And User selects Check Box on reCAPTCHA
    And User clicks on login button
    Then User Logins Successfully into Payback Account
    Examples:
      |  validnumber    | validpin |
      |  9381385233     |   7686   |
      |9401179105033003 |   7686   |

  Scenario Outline: To validate that error message is displayed for Invalid Payback card/ Mobile number
    When User enters <invalidnumber> in PAYBACK card number or Mobile Number field
    And User enters <invalidpin> in Pin field
    And User selects Check Box on reCAPTCHA
    And User clicks on login button
    Then It shows Error window

    Examples:
     |  invalidnumber    |  invalidpin|
     |   9381385234      |    7678    |
     |9401179105033009   |    7658    |

  Scenario Outline:  To Validate that PAYBACK CARD Number/Mobile Number field AND PIN field does not accept any Characters and Special Characters .
    When User clicks on Login Page icon
    When User enters "<characters1>" in PAYBACK card number or Mobile Number field
    And User enters "<characters2>" in Pin field
    Then Payback Card Number field and Pin fields are Empty
    Examples:
      | characters1 | characters2 |
      | ABC         |    ABC      |
      | !@#         |    !@#      |
