from playwright.sync_api import Page

JUMIA_URL = "https://www.jumia.com.ng/"

class Homepage:
    """A class implementing the page object model of Jumia e-commerce"""
    
    def __init__(self, page: Page):
        self.page = page
        self.url = JUMIA_URL
    
    def load(self):
        self.page.goto(self.url)
    
    def christmas_products(self):
        return self.page.get_by_role("link", name="COOK SMARTER")
    
    def scroll_to_awoof(self):
        self.page.mouse.wheel(0,1500)
        
    def click_december_sales(self):
        self.page.get_by_role("link", name="COOK SMARTER").click()