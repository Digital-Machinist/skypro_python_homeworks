from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):

        self.browser = driver
        self.wait = WebDriverWait(driver, 4)
        self.browser.get(
            'https://www.bonigarcia.dev/'
            'selenium-webdriver-java/data-types.html')

    def fill_form(self):
        names = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина 5',
            'e-mail': 'test@mail.ru',
            'phone': '+7999',
            'city': 'Москва',
            'country': 'РФ',
            'job-position': 'QA',
            'company': 'SkyPro'
        }

        for name, value in names.items():
            self.wait.until(EC.visibility_of_element_located(
                (By.NAME, name))).send_keys(value)

    def submit_form(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id):
        element = self.wait.until(EC.presence_of_element_located(
            (By.ID, field_id))).get_attribute('class')
        return element

    def check_zip_code_error(self):
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self):
        fields = [
            'first-name',
            'last-name',
            'address',
            'e-mail',
            'phone',
            'city',
            'country',
            'job-position',
            'company'
        ]
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    def check_form_submission(self):
        assert self.check_zip_code_error()
        assert self.check_fields_success()
