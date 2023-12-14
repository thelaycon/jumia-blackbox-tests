import time
from playwright.sync_api import Page, expect
from pytest_bdd import parsers, scenario, when, given, then
from pages.homepage import Homepage



@scenario("features/december_sales.feature", "User gets december offer")
def test_december_deal():
    pass


@given("the user visits Jumia hompage", target_fixture="homepage")
def homepage(page: Page):
    home = Homepage(page)
    home.load()
    assert page.url == "https://www.jumia.com.ng/"
    home.scroll_to_awoof()
    time.sleep(10)
    page.screenshot(path="screenshots/home.png")


@when("the december offer is clicked")
def december_offer_clicked(page: Page):
    home = Homepage(page)
    expect(home.christmas_products()).to_be_visible()
    home.click_december_sales()


@then(parsers.cfparse(
    'the december offer products are displayed like "{product}"'))
def december_offer_displayed(page: Page, product):
    expect(page.locator("#ctlg")).to_contain_text("Holiday Feasting")
    expect(page.locator("#ctlg")).to_contain_text("Limited Stock Deals")
    expect(page.get_by_role("link", name=product)).to_be_visible()
    time.sleep(5)
    page.screenshot(path="screenshots/december_products.png")
