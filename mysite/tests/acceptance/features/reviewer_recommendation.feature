Feature: Search Recommendation Reviewer
    Scenario: Search Recommendation Reviewer
    Given i am on Search Recommendation Reviewer Page
    And i should see Journal Submission Form
    When i fill in Journal Submission Form with Title and Abstract
    And i press Save and Continue
    Then i should see Recommendation Reviewer Page
    And i should see list of recommended reviewer
