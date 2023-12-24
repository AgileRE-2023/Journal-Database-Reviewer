Feature: Journal Scrapping
    Scenario: Scrapping Journal
    Given i am on Dashboard
    And i see Journal Scrapping
    When i press Go
    Then the response should contain Scrapping Success

