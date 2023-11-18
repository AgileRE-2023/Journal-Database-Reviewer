Feature: Add Account
    Scenario: Add New Account
        Given i am on Add Account Page
        When i fill in Add Account Form with name, email, and password
        And i press Save button
        Then the response should contain Add Account Success

    Scenario: Database issues
        Given i am on Add Account Page
        When i fill in Add Account Form with name, email, and password
        And i press Save button
        Then the response should contain Add Account Success
        And i should be on Add Account Page
