from playwright.sync_api import Playwright, sync_playwright, expect
from pages.login_page import login_page
import pytest

@pytest.mark.regression
def test_Success_Login(setup):
    page = setup
    loginP = login_page(page)

    page.goto("https://www.saucedemo.com/v1/index.html")
    loginP.login("standard_user", "secret_sauce")
    expect(page.locator("text=Products")).to_be_visible()


@pytest.mark.regression
def test_Fail_Login(setup):
    page = setup
    loginP = login_page(page)

    page.goto("https://www.saucedemo.com/v1/index.html")
    loginP.login("locked_out_user", " ")
    expect(page.locator("text=Epic sadface: Username and password do not match any user in this service")).to_be_visible()
