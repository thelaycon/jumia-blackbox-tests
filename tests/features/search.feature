Feature: Product search
	A user should be able to search for products,
	And also filter them

	Scenario: Search for a product
		Given that user visit Jumia website
		When they search for a product
		Then list of products related to product is returned
		And user can filter


