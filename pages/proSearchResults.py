from playwright.sync_api import Page,expect
import pytest

class prodSearchResutsPage:

    def __init__(self,page):
        self.txtResults = page.get_by_role("heading", name="Results", exact=True)
        self.lnkAddtoCart = page.locator("#a-autoid-3").get_by_role("button", name="Add to cart")
        self.imgCart = page.get_by_role("link", name="item in cart")



# expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
#     expect(page.get_by_text("Sort by:Featured")).to_be_visible()
#     page.locator("#a-autoid-3").get_by_role("button", name="Add to cart").click()
#     expect(page.locator("#nav-cart-count")).to_contain_text("1")
#     page.get_by_role("link", name="item in cart").click()