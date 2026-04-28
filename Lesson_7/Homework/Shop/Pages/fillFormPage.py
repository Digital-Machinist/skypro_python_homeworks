from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FillFormPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 4)

    def fill_form(self):
        data_2 = {
            '#first-name': 'Sergey', '#last-name': 'Tsareg',
            '#postal-code': '600006'
        }

        for field, value in data_2.items():
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, field))).send_keys(value)

        

    def submit(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'continue'))).click()