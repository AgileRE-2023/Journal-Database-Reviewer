Feature: Editor Login
    Scenario: Success login
    Given i am on Login Page
    When i fill in Login Form with correct email and password
    And i press Login button
    Then i should be on Dashboard

    Scenario: Incorrect Email or Password
    Given i am on Login Page
    When i fill in Login Form with incorrect email and password
    And i press Login button
    Then the response should not contain Login Success
    And i should be on Login Page
    