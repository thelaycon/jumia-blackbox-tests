import time
from playwright.sync_api import Page, expect
from pytest_bdd import parsers, scenario, when, given, then
from pages.category import Category


@scenario("features/categories.feature",
          "User views products under a category")
def test_categories():
    pass


@given("user visits Jumia site", target_fixture="homepage")
def homepage(page: Page):
    category = Category(page)
    category.load()
    assert page.url == "https://www.jumia.com.ng/"


@when(parsers.cfparse('a {goodscategory} is selected'))
def select_category(page: Page, goodscategory):
    category = Category(page)
    category.select_category(goodscategory).click()
    goodscategory = goodscategory.lower()
    # Assert that the url change successfully
    assert page.url == f"https://www.jumia.com.ng/{goodscategory}/"


@then(parsers.cfparse('user in {goodscategory} page'))
def list_products(page: Page, goodscategory):
    category = Category(page)

    # Expect the header to contain the category text
    expect(page.locator("#ctlg").get_by_text(goodscategory)).to_be_visible()
    time.sleep(10)
    page.screenshot(path=f"screenshots/{goodscategory}-page.png")


@then(parsers.cfparse('{exampleproduct} are listed'))
def example_products(page: Page, exampleproduct):
    category = Category(page)

    # Expect products under the category to be listed
    expect(
        page.get_by_role(
            "link",
            name=exampleproduct,
            exact=True)).to_be_visible()
