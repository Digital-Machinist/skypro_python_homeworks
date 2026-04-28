from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 4)

    def submit(self):
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'checkout'))).click()

    def check_cart(self):
        elements = self._driver.find_elements(
            By.CLASS_NAME, 'inventory_item_name')
        as_is = [el.text for el in elements]
        print(as_is)
        to_be = [
            'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie'
        ]

        assert as_is == to_be
