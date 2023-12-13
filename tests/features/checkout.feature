Feature: Checkout Product
	User should be able to add to cart,
	Use the checkout button

	Scenario: Checkout product
		Given that user visits Jumia website
		And login into the site
		When they add products to cart
		Then they can checkout

	
