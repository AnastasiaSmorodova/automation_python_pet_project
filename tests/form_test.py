import allure

from pages.form_page import FormPage
from conftest import driver


@allure.suite("Form")
class TestForm:
    @allure.feature('Form')
    class TestFormPage:
        @allure.title('Check Form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]], 'The form has not been filled'
