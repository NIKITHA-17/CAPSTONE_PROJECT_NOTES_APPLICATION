from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.environment import UI_BASE_URL


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='login-submit']")

    def open_login_page(self):
        self.open_url(UI_BASE_URL)

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)