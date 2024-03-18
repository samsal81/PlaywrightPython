class login_page:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("xpath=//input[@name='user-name']")
        self.password = page.locator("xpath=//input[@name='password']")
        self.login_button = page.locator("xpath=//input[@value='LOGIN']")

    def login(self, page, username, password):
        page.goto("https://www.saucedemo.com/v1/index.html")
        self.username.click()
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.login_button.click()
