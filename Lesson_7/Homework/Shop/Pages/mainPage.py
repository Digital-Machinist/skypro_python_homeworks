from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 4)

    def add_products(self):
        selectors = [
            '#add-to-cart-sauce-labs-backpack',
            '#add-to-cart-sauce-labs-bolt-t-shirt',
            '#add-to-cart-sauce-labs-onesie',
        ]
        for selector in selectors:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, selector))).click()

    def checkout(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'shopping_cart_link'))).click()
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'checkout'))).click()
