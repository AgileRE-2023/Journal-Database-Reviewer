Feature: Reviewer Scrapping
    Scenario: Scrapping Reviewer
    Given I am on Dashboard
    And I see Reviewer Scrapping
    When I press Go
    Then the response should contain Scrapping Success

