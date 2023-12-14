from playwright.sync_api import Page

JUMIA_URL = "https://www.jumia.com.ng/"

class Category:
    """A class implementing the page object model of Jumia e-commerce"""
    
    def __init__(self, page: Page):
        self.page = page
        self.url = JUMIA_URL
    
    def load(self):
        self.page.goto(self.url)
    
    def select_category(self, goodscategory):
        return self.page.get_by_role("menuitem", name=goodscategory)