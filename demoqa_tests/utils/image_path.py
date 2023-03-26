from selene.support.shared import browser
import os


def upload_file(selector, file_path):
    print(os.path.abspath(__file__))
    print(os.path.join(os.path.dirname(__file__), file_path))
    browser.element(selector).set_value(
        os.path.abspath(
            os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'tests'), file_path)
        )
    )
