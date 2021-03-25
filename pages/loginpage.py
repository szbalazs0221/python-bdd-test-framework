from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    email_field = (By.CSS_SELECTOR, "#user_email")
    password_field = (By.CSS_SELECTOR, "#user_password")
    sign_in_button = (By.CSS_SELECTOR, "input[value=\"Sign in\"]")
    error_message_element = (By.CSS_SELECTOR, ".ht-alert__content p")

    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(self.webdriver, 10)

    def send_keys_to_email(self, email):
        email_field = self.webdriver.find_element(*self.email_field)
        email_field.send_keys(email)

    def send_keys_to_password(self, password):
        password_field = self.webdriver.find_element(*self.password_field)
        password_field.send_keys(password)

    def sign_in(self):
        sign_in_button = self.webdriver.find_element(*self.sign_in_button)
        sign_in_button.click()

    @property
    def error_message(self):
        error = self.webdriver.find_element(*self.error_message_element).text
        return error