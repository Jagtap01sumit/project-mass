Feature: Google Search

  Scenario: Search keyword on the first page
    Given I launch the browser and search for URL
    # When I search for "https://expired.badssl.com/"
    Then I should see results on the page
    Then I save the responsiveness screenshots
    Then I verify SSL certificate is available and valid