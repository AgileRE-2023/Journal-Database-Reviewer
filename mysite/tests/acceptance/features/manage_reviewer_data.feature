Feature: Manage Reviewer Data
    Scenario: Update Reviewer Data
    Given i am on List Reviewer Page
    # And i should see List Reviewer
    When i press Edit button on one reviewer from List Reviewer
    And i see Edit Reviewer Form
    And i fill in Edit Reviewer Form with the latest data
    And i press save edit
    Then the response should contain Success
    
    Scenario: Cancel Update
    Given i am on List Reviewer Page
    # And I see List Reviewer
    When i press Edit button on one reviewer from List Reviewer
    And i see Edit Reviewer Form
    And i fill in Edit Reviewer Form with the latest data
    And i press Cancel
    Then i should be on List Reviewer Page
