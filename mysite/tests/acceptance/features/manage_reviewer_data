Feature: Manage Reviewer Data
Scenario: Update Reviewer Data
Given i am on “List Reviewer Page”
And i should see “List Reviewer”
When i press “Edit button” on one reviewer from “List Reviewer”
And i see “Edit Reviewer Form”
And i fill in “Edit Reviewer Form” with the latest data.
And i press “Save”
Then the response should contain “Update Success”
And i should be on “Dashboard”

Scenario: Cancel Update
Given i am on “List Reviewer Page”
And I see “List Reviewer”
When i press “Edit button” on one reviewer from “List Reviewer”
And I see “Edit Reviewer Form”
And I fill in “Edit Reviewer Form” with the latest data.
And i press “Cancel”
Then i should be on “List Reviewer Page”
