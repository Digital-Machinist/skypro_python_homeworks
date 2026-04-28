from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 4)
        self._driver.get("https://www.saucedemo.com/")

    def auth(self, login, password):
        data = {
        '#user-name': login, '#password': password
        }

        for locator, value in data.items():
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, locator))).send_keys(value)
        self.wait.until(EC.presence_of_element_located((By.ID, 'login-button'))).click()

