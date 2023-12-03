Feature: Upload OJS Data
    Scenario: Upload OJS Data
    Given i am on Upload Data OJS Page
    And i see Upload OJS Form
    When i attach the file DataOJS.xls to Upload OJS Form
    And i press Save and Continue
    Then the response should contain Upload Success
    And i should be on Dashboard

    Scenario: Upload OJS data files that are not excel
    Given i am on Upload Data OJS Page
    And i see Upload OJS Form
    When i attach the file DataOJS.pdf to Upload OJS Form
    And i press Save and Continue
    Then the response should contain Upload Error
    And i should be on Upload Data OJS Page

    Scenario: Upload OJS data files that are excel but in wrong format
    Given i am on Upload Data OJS Page
    And i see Upload OJS Form
    When i attach the file DataOJS.xls to Upload OJS Form
    And i press Save and Continue
    Then the response should contain Upload Failed
    And i should be on Upload Data OJS Page
