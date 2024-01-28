from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("test automation")
    page.get_by_label("test automation university").get_by_text("test automation university").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_label("Clear").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
