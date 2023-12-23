Feature: Add Reviewer Data
    Scenario: Add Reviewer
    Given i am on List Reviewer Page 
    # And i see List Reviewer 
    When i press Add button 
    And i see Add Reviewer Form 
    And i fill in Add Reviewer Form with Full Name, Email, Scopus ID, dan Scholar ID 
    And i press Save 
    Then the response should contain Add Success 

    Scenario: Add an Existing Reviewer 
    Given i am on List Reviewer Page
    # And i see List Reviewer
    When i press Add button
    And i see Add Reviewer Form
    And i fill in Add Reviewer Form with Full Name, Email, Institution, Scopus ID, dan Scholar ID
    And i press Save
    Then the response should not contain Add Success
    And the response should contain Reviewer Already Exist
