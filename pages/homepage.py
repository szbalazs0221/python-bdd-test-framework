from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    url = "https://www.cucumber.io"
    accept_cookies_button = (By.CSS_SELECTOR, "body > div.cc-pop.active > div > div > div.cc-th.ok.text-white > a")
    login_button = (By.CSS_SELECTOR, "a[title=Login]")

    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(self.webdriver, 10)

    def load(self):
        self.webdriver.get(self.url)
        self.webdriver.maximize_window()

    def accept_cookies(self):
        accept_cookies_button = self.wait.until(EC.presence_of_element_located(self.accept_cookies_button))
        accept_cookies_button.click()

    def login(self):
        login_button = self.webdriver.find_element(*self.login_button)
        login_button.click()
