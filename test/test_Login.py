from playwright.sync_api import Playwright, sync_playwright, expect
from pages.login_page import login_page
import pytest

@pytest.mark.regression
def test_Success_Login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = browser.new_page()
    loginP = login_page(page)

    page.goto("https://www.saucedemo.com/v1/index.html")
    loginP.login("standard_user", "secret_sauce")
    expect(page.locator("text=Products")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.regression
def test_Fail_Login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = browser.new_page()
    loginP = login_page(page)

    page.goto("https://www.saucedemo.com/v1/index.html")
    loginP.login("locked_out_user", " ")
    expect(page.locator("text=Epic sadface: Username and password do not match any user in this service")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
