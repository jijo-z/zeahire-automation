from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{BASE_URL}/login"

        # ===== Locators =====
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"

    # ================= ACTIONS ================= #

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def login(self, email, password):
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.login_button)