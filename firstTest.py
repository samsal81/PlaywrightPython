from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    driver = browser.new_page()
    driver.goto("https://www.google.com/")
    driver.get_by_label("Search", exact=True).click()
    driver.get_by_label("Search", exact=True).fill("test automation")
    driver.get_by_label("Clear").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
