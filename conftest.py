import pytest
from POM.login_page import LoginPage


@pytest.fixture
def setup_browser(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    yield page


@pytest.fixture
def logging_in(setup_browser) -> None:
    username = 'standard_user'
    passwd = 'secret_sauce'
    page = setup_browser
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)

    yield page
