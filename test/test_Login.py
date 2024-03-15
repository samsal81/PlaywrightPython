from playwright.sync_api import Playwright, sync_playwright, expect
from pages.login_page import login_page

def test_Success_Login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = browser.new_page()
    loginP = login_page(page)

    page.goto("https://parabank.parasoft.com/")
    loginP.login("samsal81", "samsal81")
    expect(page.locator("text=Account Services")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
