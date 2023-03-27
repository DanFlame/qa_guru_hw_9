from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PracticeForm


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

    practice_form.page_open()
    practice_form.remove_ads()

    practice_form.fill_data(user)
    practice_form.submit()

    practice_form.assert_fields(user)


practice_form = PracticeForm()
