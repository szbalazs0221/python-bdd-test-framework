import pytest
from selenium import webdriver

@pytest.fixture()
def browser(request):
    driver = request.config.getoption("--webdriver")

    if driver == 'chrome':
        browser = webdriver.Chrome()
    elif driver == 'firefox':
        browser = webdriver.Firefox()

    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--webdriver",
        action='store',
        choices=['chrome', 'firefox'],
        required=True)


def pytest_bdd_step_error(step_func_args):
    path = f'reports/screenshots/screenshot.png'
    step_func_args['login_page'].webdriver.save_screenshot(path)