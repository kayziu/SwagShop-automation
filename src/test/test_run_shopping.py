import pytest
from playwright.sync_api import expect
from src.pages.shop_overview import ShopInventory
from src.pages.cart_and_checkout import CartAndCheckout


def wait_and_add_to_cart(inventory):
    cart_details_issue = True
    while cart_details_issue:
        if not inventory.add_to_cart_details.is_visible:
            inventory.add_to_cart_details.click()  # add item 1 to cart
        else:
            cart_details_issue = False

@pytest.mark.smoke
# Logging in and adding to cart one item
def test_buy_in_item_details (logging_in) -> None:
    page = logging_in
    inventory = ShopInventory(page)
    inventory.item_1.click()
    inventory.add_to_cart_details.click()
    inventory.back_to_inventory.click()
    inventory.shopping_cart.click()
    expect(inventory.item_1).to_be_visible()



@pytest.mark.regression
# Logging in and adding to cart two items, deleting one, proceed to checkout and finish
def test_buy_2_in_item_details_and_checkout (logging_in) -> None:
    page = logging_in
    inventory = ShopInventory(page)
    cart = CartAndCheckout(page)
    inventory.item_1.click()    # open item 1 details
    wait_and_add_to_cart(inventory)
    inventory.back_to_inventory.click()     # back to inventory overview
    inventory.item_2.click()    # open item 2 details
    wait_and_add_to_cart(inventory)
    inventory.add_to_cart_details.click()   # add item 2 to cart
    inventory.shopping_cart.click()     # go to cart
    expect(inventory.item_1).to_be_visible()    # check if item 1 is in the cart
    expect(inventory.item_2).to_be_visible()    # check if item 2 is in the cart
    # remove_buttons = (cart.remove_backpack, cart.remove_bike, cart.remove_jacket, cart.remove_onesie,
    #                         cart.remove_t_shirt, cart.remove_t_shirt_red)
    cart.first_remove_button.click()    # remove the item at the top of the cart
    cart.go_to_checkout.click()     # go to checkout
    first_name = 'Bob'
    last_name = 'Walsky'
    postal_code = '550'
    cart.first_name_input.fill(first_name)
    cart.last_name_input.fill(last_name)
    cart.postal_code_input.fill(postal_code)
    cart.continue_to_checkout_overview.click()
    cart.finish_checkout.click()
    expect(cart.checkout_completed).to_be_visible()


@pytest.mark.xfail(reason='Known issue - checkout button is enabled with empty cart')
def test_buy_item_and_remove_and_try_to_continue (logging_in) -> None:
    page = logging_in
    shop_inventory = ShopInventory(page)
    cart_and_checkout = CartAndCheckout(page)
    shop_inventory.add_to_cart_b_t_shirt.click()
    shop_inventory.add_to_cart_r_t_shirt.click()
    shop_inventory.shopping_cart.click()
    cart_and_checkout.remove_t_shirt.click()
    cart_and_checkout.remove_t_shirt_red.click()
    expect(cart_and_checkout.go_to_checkout).not_to_be_enabled()
