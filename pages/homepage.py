from playwright.sync_api import Page

JUMIA_URL = "https://www.jumia.com.ng/"

class Homepage:
    """A class implementing the page object model of Jumia e-commerce"""
    
    def __init__(self, page: Page):
        self.page = page
        self.url = JUMIA_URL
    
    def load(self):
        self.page.goto(self.url)
        
    def click_december_sales(self):
        self.page.get_by_role("link", name="COOK SMARTER").click()