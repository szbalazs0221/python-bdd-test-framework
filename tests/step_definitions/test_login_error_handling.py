from pytest_bdd import scenario, given, when, then
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

@scenario(
    feature_name='../features/login_error_handling.feature', 
    scenario_name='Log in with an invalid email address'
)
def test_log_in_with_invalid_email():
    pass

@scenario(
    feature_name='../features/login_error_handling.feature', 
    scenario_name='Log in with an invalid password'
)
def test_log_in_with_invalid_password():
    pass

@scenario(
    feature_name='../features/login_error_handling.feature', 
    scenario_name='Log in with an invalid password and email address'
)
def test_log_in_with_invalid_password_and_email():
    pass


@given("Cucumber.io login page", target_fixture="webdriver")
def display_login_page():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    page = HomePage(browser)
    page.load()
    page.accept_cookies()
    page.login()
    return browser


@when('The user is trying to log in with invalid credentials: '
      '(email: "test_user_invalid@testde.com", password: "myvalidpassword")')
def login(webdriver):
    login_page = LoginPage(webdriver)
    login_page.send_keys_to_email("test_user_invalid@testde.com")
    login_page.send_keys_to_password("myvalidpassword")
    login_page.sign_in()


@when('The user is trying to log in with invalid credentials: '
      '(email: "test_user_valid@testde.com", password: "myinvalidpassword")')
def login(webdriver):
    login_page = LoginPage(webdriver)
    login_page.send_keys_to_email("test_user_valid@testde.com")
    login_page.send_keys_to_password("myinvalidpassword")
    login_page.sign_in()


@when('The user is trying to log in with invalid credentials: '
      '(email: "test_user_invalid@testde.com", password: "myinvalidpassword")')
def login(webdriver):
    login_page = LoginPage(webdriver)
    login_page.send_keys_to_email("test_user_invalid@testde.com")
    login_page.send_keys_to_password("myinvalidpassword")
    login_page.sign_in()


@then('An error message shows up')
def validate_error_message(webdriver):
    error_message_element = (By.CSS_SELECTOR, ".ht-alert__content p")
    error_text = webdriver.find_element(*error_message_element).text
    assert error_text == "Invalid email or password."
    webdriver.quit()





