from selene import have


def select_by_value(element, text):
    element.element_by(have.value(text)).element('..').click()
