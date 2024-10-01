from playwright.sync_api import expect
from src.pages.shop_overview import ShopInventory
from src.pages.login_page import LoginPage
import os

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    from src import utils

    PASSWORD = utils.credentials.PASSWORD


# def test_visual_shop_overview(logging_in, assert_snapshot) -> None:
#     page = logging_in
#     inventory = ShopInventory(page)
#     expect(inventory.shopping_cart).to_be_visible()
#     assert_snapshot(page.screenshot())


def test_visual_shop_overview(page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    username = 'standard_user'
    passwd = PASSWORD
    login_page = LoginPage(page)
    login_page.username_box.fill(username)
    login_page.password_box.fill(passwd)
    login_page.login_button.click()
    inventory = ShopInventory(page)
    # inventory.item_1.click()    # added for failure test
    expect(inventory.shopping_cart).to_be_visible()
    # assert_snapshot(page.screenshot(full_page=True))