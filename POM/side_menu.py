class SideMenu:

    def __init__(self, page):
        self.open_menu = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.locator("[data-test=\"logout-sidebar-link\"]")