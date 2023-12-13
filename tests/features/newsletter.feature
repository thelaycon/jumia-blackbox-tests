Feature: Subscription to newsletter

	Scenario: User subscribe to newsletter
		Given user visits Jumia site
		When the newsletter form is filled
		And it is submitted
		Then a success message is displayed
