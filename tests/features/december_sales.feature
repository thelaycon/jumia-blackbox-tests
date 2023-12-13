Feature: User can access december sales on the homepage

	Scenario: User gets december offer
		Given the user visits Jumia hompage
		When the december offer is clicked
		Then the december offer products are displayed
