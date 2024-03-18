from playwright.sync_api import Playwright
import pytest

@pytest.fixture
def setup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    yield page