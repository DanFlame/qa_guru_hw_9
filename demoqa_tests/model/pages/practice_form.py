from selene import have, be, command
from selene.support.shared import browser
from demoqa_tests.model.controls import checkbox, datepicker, radiobutton, dropdown
from demoqa_tests.utils import image_path
from demoqa_tests.model.data.user import User
from demoqa_tests.utils.scroll import scroll_to


class PracticeForm:
    def __init__(self):
        pass

    def page_open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_data(self, user: User):
        scroll_to('#firstName')
        browser.element('#firstName').should(be.blank).type(user.first_name)
        scroll_to('#lastName')
        browser.element('#lastName').should(be.blank).type(user.last_name)

        scroll_to('#userEmail')
        browser.element('#userEmail').should(be.blank).type(user.email)
        scroll_to('[name="gender"]')
        radiobutton.select_by_value(browser.all('[name="gender"]'), user.gender)
        scroll_to('#userNumber')
        browser.element('#userNumber').should(be.blank).type(user.phone_number)
        scroll_to('#dateOfBirthInput')
        datepicker.set_birth_date(user.birth_day, user.birth_month, user.birth_year)

        scroll_to('#subjectsInput')
        browser.element('#subjectsInput').type(user.subject).press_enter()
        scroll_to('[for^=hobbies-checkbox]')
        checkbox.checkbox_click(browser.all('[for^=hobbies-checkbox]'), user.hobby)
        scroll_to('#uploadPicture')
        image_path.upload_file('#uploadPicture', user.picture)

        scroll_to('#currentAddress')
        browser.element('#currentAddress').type(user.address)
        scroll_to('#state')
        dropdown.select('#state', '[id^=react-select][id*=option]', user.state)
        scroll_to('#city')
        dropdown.select('#city', '[id^=react-select][id*=option]', user.city)
        return self

    def submit(self):
        scroll_to('#submit')
        browser.element('#submit').press_enter()
        return self

    def assert_fields(self, user: User):
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.birth_day} {user.birth_month},{user.birth_year}',
            user.subject,
            user.hobby,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        ))
        return self
