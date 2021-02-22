Feature: As a QKnows user I want to check my search results
Scenario: As a QKnows user I want to check my search results
    Given I proceed to QKnows main page
    When I search for a random meaningful word
    Then the first 3 results get the searched word