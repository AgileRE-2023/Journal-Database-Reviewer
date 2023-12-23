Feature: Add Reviewer Data
    Scenario: Add Reviewer
    Given i am on List Reviewer Page 
    When i press Add button 
    And i see Add Reviewer Form 
    And i fill in Add Reviewer Form with Full Name, Email, Scopus ID, dan Scholar ID 
    And i press Save 
    Then the response should contain Add Success 

    Scenario: Add an Existing Reviewer 
    Given i am on List Reviewer Page
    When i press Add button
    And i see Add Reviewer Form
    And i fill in Add Reviewer Form with Full Name, Email that already exist, Scopus ID, dan Scholar ID
    And i press Save
    Then the response should contain Reviewer with this email already Exist
