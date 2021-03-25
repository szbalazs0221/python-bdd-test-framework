import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def pytest_bdd_step_error(step_func_args):
    path = f'reports/screenshots/screenshot.png'
    step_func_args['login_page'].webdriver.save_screenshot(path)