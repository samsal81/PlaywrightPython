from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = browser.new_page()

    page.goto("https://parabank.parasoft.com/")
    page.locator("xpath=//input[@name='username']").click()
    page.locator("xpath=//input[@name='username']").fill("samsal81")
    page.locator("xpath=//input[@name='password']").click()
    page.locator("xpath=//input[@name='password']").fill("samsal81")
    page.locator("xpath=//input[@value='Log In']").click()
    expect(page.locator("text=Account Services")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
