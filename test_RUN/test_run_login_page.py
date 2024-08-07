import os

import pytest
from playwright.sync_api import expect

# import utils.credentials
from POM.login_page import LoginPage
from POM.side_menu import SideMenu


@pytest.mark.regression
@pytest.mark.parametrize("user", ["standard_user", "fake_user", "standard_user", ""])
@pytest.mark.parametrize("passwd", [os.environ['PASSWORD'], "fake_passwd", "", os.environ['PASSWORD']])
def test_logging_in_parametrized(setup_browser, user, passwd) -> None:
    page = setup_browser
    login_page = LoginPage(page)
    side_menu = SideMenu(page)
    login_page.username_box.fill(user)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()

    if user != "standard_user" and user != "" and passwd != os.environ['PASSWORD'] and passwd != "":
        expect(login_page.username_and_passwd_error).to_be_visible()
    elif user != "" and passwd == "":
        expect(login_page.passwd_error).to_be_visible()
    elif user == "" and passwd != "":
        expect(login_page.username_error).to_be_visible()
    elif user == "standard_user" and passwd == os.environ['PASSWORD']:
        expect(side_menu.open_menu).to_be_visible()


@pytest.mark.regression
def test_logging_in_negative_passwd(setup_browser) -> None:
    username = 'lorem_ipsum'
    passwd = ''
    page = setup_browser
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()
    expect(login_page.passwd_error).to_be_visible()


@pytest.mark.regression
def test_logging_in_negative_locked_user(setup_browser) -> None:
    username = 'locked_out_user'
    passwd = 'secret_sauce'
    page = setup_browser
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()
    expect(login_page.blocked_user_error).to_be_visible()


@pytest.mark.regression
def test_logging_in_negative_username_passwd(setup_browser) -> None:
    username = 'user'
    passwd = 'passwd'
    page = setup_browser
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()
    expect(login_page.username_and_passwd_error).to_be_visible()





