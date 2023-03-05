# Created by Indrani at 02-03-2023
@ExcelDataTests
Feature: Login with Excel Data
  Background:
    Given Launch Chrome Browser and Payback Application
    When User clicks on Login Page icon

  Scenario: To Validate that user is successfully Logged into to payback account with first data
    When User enters valid_cardnum and valid_pin for first dataset
    And User selects Check Box on reCAPTCHA
    And User clicks on login button
    Then Then It shows home page for first dataset


  Scenario: To validate that error message is displayed for Invalid Payback card/ Mobile number with first data
    When User enters cardnum and pin from invalid first dataset
    And User selects Check Box on reCAPTCHA
    And User clicks on login button
    Then It shows Error window for first data





