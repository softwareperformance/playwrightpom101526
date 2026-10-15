import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone 18 pro")
    page.get_by_role("button", name="iphone 18 pro").click()


