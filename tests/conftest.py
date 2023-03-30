import pytest
from demoqa_tests.utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser


@pytest.fixture(scope='function')
def setup_chrome():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
