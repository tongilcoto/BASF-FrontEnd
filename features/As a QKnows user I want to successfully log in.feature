Feature: As a QKnows user I want to successfully log in
Scenario: As a QKnows user I want to successfully log in
    Given I open QKnows log in page
    When I set my user credentials
    And I select Log In option
    Then I access QKnows main page
    And "search field" is visible
    And "search magnifier" is visible
    And "Upcoming Events section" is visible
    And "News section" is visible
    And "access to Support chat" is visible