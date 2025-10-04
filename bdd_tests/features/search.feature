Feature: Google Search

  Scenario: Search keyword on the first page
    Given I open Google homepage
    When I search for "AWS Lambda"
    Then I should see results on the first page
