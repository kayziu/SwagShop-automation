class ShopInventory:
    def __init__(self, page):
        self.item_1 = page.locator("[data-test=\"item-4-title-link\"]")
        self.item_2 = page.locator("[data-test=\"item-1-title-link\"]")
        self.item_3 = page.locator("[data-test=\"item-2-title-link\"]")
        self.item_4 = page.locator("[data-test=\"item-0-title-link\"]")
        self.item_5 = page.locator("[data-test=\"item-5-title-link\"]")
        self.item_6 = page.locator("[data-test=\"item-3-title-link\"]")
        self.add_to_cart_details = page.locator("[data-test=\"add-to-cart\"]")
        self.back_to_inventory = page.locator("[data-test=\"back-to-products\"]")
        self.shopping_cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self.add_to_cart_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.add_to_cart_light = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.add_to_cart_b_t_shirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.add_to_cart_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.add_to_cart_onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.add_to_cart_r_t_shirt = page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-"
                                                  "\\(red\\)\"]")
