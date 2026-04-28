from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class text_to_be_exactly:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = driver.find_element(*self.locator).text
        return actual_text == self.text

class MainPage:
    def __init__(self, driver):
        
        self._driver = driver
        self.wait = WebDriverWait(driver, 50)
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def set_delay(self, delay):
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'delay'))).clear()
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'delay'))).send_keys(delay)
    
    def press_buttons(self, a, x, b):
        buttons = {
            '1': '//span[text()="1"]','2': '//span[text()="2"]','3': '//span[text()="3"]',
            '4': '//span[text()="4"]','5': '//span[text()="5"]','6': '//span[text()="6"]',
            '7': '//span[text()="7"]','8': '//span[text()="8"]','9': '//span[text()="9"]',
            '0': '//span[text()="0"]','+': '//span[text()="+"]','-': '//span[text()="-"]',
            '*': '//span[text()="x"]','/': '//span[text()="÷"]','=': '//span[text()="="]',
            '.': '//span[text()="."]','C': '//span[text()="C"]'
        }
        
        but1 = buttons[a]
        oper = buttons[x]
        but2 = buttons[b]
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH, but1))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, oper))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, but2))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, buttons['=']))).click()
        
        
    def check_calc_sum_result(self, res):
        self.wait.until(text_to_be_exactly(
            (By.CLASS_NAME, 'screen'), res))
        final_text = self._driver.find_element(By.CLASS_NAME, 'screen').text
        assert final_text == res