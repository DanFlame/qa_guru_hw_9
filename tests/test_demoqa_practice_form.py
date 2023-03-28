from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PracticeForm
import allure
from allure_commons.types import Severity


@allure.tag('WEB')
@allure.label('owner', 'danflame')
@allure.severity(Severity.CRITICAL)
@allure.feature('Practice form')
@allure.description('We should check that all fields completed correctly')
@allure.story('Practice form completion with valid data')
def test_positive_fill_practice_form():
    user = User(first_name='Daniel',
                last_name='Fazylov',
                email='daniel@test.ru',
                gender='Male',
                phone_number='8999123456',
                birth_year='1998',
                birth_month='November',
                birth_day=25,
                subject='Computer Science',
                hobby='Music',
                picture='picture.PNG',
                address='Indo st. 10',
                state='Uttar Pradesh',
                city='Agra'
                )

    with allure.step('Open practice form'):
        practice_form.page_open()
    with allure.step('Ads removing'):
        practice_form.remove_ads()

    with allure.step('Data entering'):
        practice_form.fill_data(user)
    with allure.step('Submit data entering'):
        practice_form.submit()

    with allure.step('Assert fields'):
        practice_form.assert_fields(user)


practice_form = PracticeForm()
