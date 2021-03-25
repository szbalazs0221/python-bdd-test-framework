from pytest_bdd import scenarios, given, when, then, parsers
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('../features/login_error_handling.feature')


@given("Cucumber.io login page")
def display_login_page(browser):
    page = HomePage(browser)
    page.load()
    page.accept_cookies()
    page.login()


@when(
    parsers.parse(
        'The user is trying to log in with invalid credentials: '
        '(email: "{email_address}", password: "{password}")'
    )
)
def login(browser, email_address, password):
    login_page = LoginPage(browser)
    login_page.send_keys_to_email(email_address)
    login_page.send_keys_to_password(password)
    login_page.sign_in()


@then('An error message shows up')
def validate_error_message(browser):
    error_message_element = (By.CSS_SELECTOR, ".ht-alert__content p")
    error_text = browser.find_element(*error_message_element).text
    assert error_text == "Invalid email or password."
