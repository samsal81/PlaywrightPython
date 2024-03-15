class login_page:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("xpath=//input[@name='username']")
        self.password = page.locator("xpath=//input[@name='password']")
        self.login_button = page.locator("xpath=//input[@value='Log In']")

    def login(self, username, password):
        self.username.click()
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.login_button.click()
