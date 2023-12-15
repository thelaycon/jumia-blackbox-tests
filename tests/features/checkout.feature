Feature: Checkout Product
	User should be able to add to cart,
	Use the checkout button

	Scenario: Checkout product
		Given that user visits Jumia website
		When login into the site
		And they add <product> to cart
		Then they can checkout

	
