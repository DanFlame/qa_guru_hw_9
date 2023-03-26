from selene import have
from selene.support.shared import browser


def select(locator, locator_option, value):
    browser.element(locator).click()
    browser.all(locator_option).element_by(have.exact_text(value)).click()
