Feature: User can view product by category

	Scenario Outline: User views products under a category
		Given user visits Jumia site
		When a <goodscategory> is selected
		Then user in <goodscategory> page
		And <exampleproduct> are listed
		
		Examples:
		| goodscategory | exampleproduct |
		| Computing | MacBooks |
		| Electronics | Smart TVs |