from selene.support.shared import browser
import os


def upload_file(selector, file_path):

    browser.element(selector).set_value(
        os.path.abspath(
            os.path.join(
                os.path.join(
                    os.path.join(
                        os.path.dirname(
                            os.path.dirname(
                                os.path.dirname(__file__))
                        ), 'tests'
                    ), 'resources'
                ), file_path
            )
        )
    )
