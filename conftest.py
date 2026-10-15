from playwright.sync_api import Page, expect
import pytest

@pytest.fixture()
def navigation(page):
    page.goto("https://www.amazon.in/")
