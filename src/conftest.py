import pytest
from src.pages.login_page import LoginPage
import os

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    from src import utils

    PASSWORD = src.utils.credentials.PASSWORD


@pytest.fixture(scope="session")
def setup_browser(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    yield page
    page.close()


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    username = 'standard_user'
    passwd = PASSWORD
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()

    yield context


@pytest.fixture()
def logging_in(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    page.wait_for_load_state("networkidle")

    yield page
