
from playwright.sync_api import Page, expect
import pytest 

class homePage:

    def __init__(self,page):
        self.imgAmazonLogo = page.get_by_role("link", name="Amazon.in")
        self.btnSearch = page.get_by_role("button", name="Go", exact=True)
        self.editSearchBox = page.get_by_role("searchbox", name="Search Amazon.in")
        

    def validateAmazonLogo(self):
        expect(self.imgAmazonLogo).to_be_visible()

    def validateSearchButtonVisiblity(self):
        expect(self.btnSearch).to_be_visible()

    def validateSearchBoxVisivility(self):
        expect(self.editSearchBox).to_be_visible()

    def fillSearchProduct(self):
        self.editSearchBox.fill('iphone 18 pro')

    def clickSearchButton(self):
        self.btnSearch.click()

