import re      # Regular Expression Syntax. A regular expression (or RE) specifies a set of strings that matches it
class LoginPage:

    def __init__(self, page):
        self.username_box = page.locator("[data-test=\"username\"]")
        self.password_box = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_box = page.locator("[data-test=\"error\"]")
        self.username_error = page.locator("div").filter(has_text=re.compile(r"^Epic sadface: Username is required$"))
        self.passwd_error = page.locator("div").filter(has_text=re.compile(r"^Epic sadface: Password is required$"))
        self.blocked_user_error = page.locator("div").filter(has_text=re.compile(r"^Epic sadface: Sorry, this user "
                                                                                 r"has been locked out\.$"))
        self.username_and_passwd_error = page.locator("div").filter(has_text=re.compile(r"^Epic sadface: Username and "
                                                                                        r"password do not match any "
                                                                                        r"user in this service$"))
