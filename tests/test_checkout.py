import time
from playwright.sync_api import Page, expect
from pytest_bdd import parsers, scenario, when, given, then
from pages.checkout import Homepage

@scenario("features/checkout.feature", "Checkout Product")
def test_checkout_feature():
    pass
    
@given("that user visits Jumia website", target_feature="homepage")
def homepage(page: Page):
    home = Homepage(page)
    assert page.url == "https://www.jumia.com.ng/"
    
@when("login into the site")    
def login(page: Page):
    home = Homepage(page)
    home.click_login()

@when(parsers.cfparse("they add {product} to cart"))    
def login(page: Page):
    home = Homepage(page)
    home.add_product_to_cart(product)

@then("they can checkout")
def checkout(page: Page):
    home = Homepage(page)
    home.checkout_products()