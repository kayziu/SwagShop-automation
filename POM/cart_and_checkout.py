class CartAndCheckout:

    def __init__(self, page):
        self.remove_backpack = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.remove_bike = page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")
        self.remove_t_shirt = page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
        self.remove_jacket = page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]")
        self.remove_onesie = page.locator("[data-test=\"remove-sauce-labs-onesie\"]")
        self.remove_t_shirt_red = page.locator("[data-test=\"remove-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.continue_shopping = page.locator("[data-test=\"continue-shopping\"]")
        self.go_to_checkout = page.locator("[data-test=\"checkout\"]")  # go to checkout button
        self.cancel_and_back_to_cart = page.locator("[data-test=\"cancel\"]")  # cancel the checkout and back
        # to cart
        self.first_name_input = page.locator("[data-test=\"firstName\"]")  # first name input
        self.last_name_input = page.locator("[data-test=\"lastName\"]")  # last name input
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")  # postal code input
        self.general_error_form = page.locator("[data-test=\"error\"]")  # general error on the checkout form
        self.first_name_error = page.locator("[data-test=\"checkout-info-container\"] div").\
            filter(has_text="Error: First Name is required").nth(2)  # error first name is required on the checkout
        self.last_name_error = page.locator("[data-test=\"checkout-info-container\"] div").filter\
            (has_text="Error: Last Name is required").nth(2)  # error last name is required on the checkout
        self.postal_code_error = page.locator("[data-test=\"checkout-info-container\"] div").\
            filter(has_text="Error: Postal Code is required").nth(2)  # error postal code is required
        self.continue_to_checkout_overview = page.locator("[data-test=\"continue\"]")  # continue to
        # checkout overview button
        self.price_total = page.locator("[data-test=\"subtotal-label\"]")  # price total
        self.finish_checkout = page.locator("[data-test=\"finish\"]")  # finish the checkout
        self.checkout_completed = page.locator("[data-test=\"complete-header\"]")  # complete checkout confirmation
        self.back_to_products = page.locator("[data-test=\"back-to-products\"]")  # back to products button
        self.first_remove_button = page.get_by_text("remove").nth(0)







