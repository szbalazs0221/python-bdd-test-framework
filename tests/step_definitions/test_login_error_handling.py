from pytest_bdd import scenarios, given, when, then, parsers
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('../features/login_error_handling.feature')


@given("Cucumber.io login page", target_fixture="login_page")
def display_login_page(browser):
    page = HomePage(browser)
    page.load()
    page.accept_cookies()
    page.login()
    return LoginPage(browser)


@when(
    parsers.parse(
        'The user is trying to log in with invalid credentials: '
        '(email: "{email}", password: "{password}")'
    )
)
@when('The user is trying to log in with invalid credentials: '
      '(email: "<email>", password: "<password>")')
def login(login_page, email, password):
    login_page.send_keys_to_email(email)
    login_page.send_keys_to_password(password)
    login_page.sign_in()


@then('An error message shows up')
def validate_error_message(login_page):
    assert login_page.error_message == "Invalid email or password."
