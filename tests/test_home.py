
from playwright.sync_api import Page, expect
from pages.home import homePage
import pytest


@pytest.mark.smoke
def test_homeScreen(page: Page, navigation):
    homeObj = homePage(page)
    # page.goto("https://www.amazon.in/")
    # expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    homeObj.validateAmazonLogo()
    # expect(page.get_by_role("button", name="Go", exact=True)).to_be_visible()
    homeObj.validateSearchButtonVisiblity()

    # page.get_by_role("searchbox", name="Search Amazon.in").click()
    # page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone 18 pro")
    # page.get_by_role("searchbox", name="Search Amazon.in").press("Tab")
    homeObj.fillSearchProduct()

    # page.get_by_role("button", name="Go", exact=True).click()
    homeObj.clickSearchButton()
    page.wait_for_timeout(3000)


# @pytest.mark.smoke
# def test_searchProduct(page: Page):
#     # page.wait_for_timeout(3000)
#     expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
#     expect(page.get_by_text("Sort by:Featured")).to_be_visible()
#     page.locator("#a-autoid-3").get_by_role("button", name="Add to cart").click()
#     expect(page.locator("#nav-cart-count")).to_contain_text("1")
#     page.get_by_role("link", name="item in cart").click()
#     page.wait_for_timeout(3000)


# @pytest.mark.smoke
# def test_Cart(page: Page) -> None:
#     expect(page.get_by_role("heading", name="Shopping Cart")).to_be_visible()
#     expect(page.get_by_role("button", name="Proceed to Buy Buy Amazon")).to_be_visible()
#     page.wait_for_timeout(3000)









   
