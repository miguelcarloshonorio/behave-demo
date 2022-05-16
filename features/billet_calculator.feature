@create
Feature: Calculate Operations

@late_billet_calculator
Scenario: Addition Operations
    Given billet with value 500 dollars
    And the date due is 2022-05-05
    And the payment date is 2022-05-10
    And the late fee is 2 percent
    And the late payment interest is 0.33 cents per day
    When I calculate the total value to pay
    Then the system informs the total value is 513.33
    And the total late payment days is 10
    And the total of late payment interest 3.33
    And the total of late fee is 10 dollars

