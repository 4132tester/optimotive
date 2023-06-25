import pytest
import selenium.webdriver


@pytest.fixture(scope='session')
def browser():
    browser = selenium.webdriver.Firefox()
    browser.maximize_window()

    yield browser

    browser.quit()
