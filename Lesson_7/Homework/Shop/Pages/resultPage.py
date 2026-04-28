import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 4)

    def check_result(self, result):
        total = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'summary_total_label'))).text
        num_total = re.sub(r'[^0-9.$]', '', total)
        assert num_total == result
