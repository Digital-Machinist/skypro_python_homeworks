import pytest
import re
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def ff():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-first-run-ui")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    ff = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    ff.maximize_window()

    yield ff

    ff.quit()


@pytest.fixture(scope='module')
def get_result(ff):
    ff.maximize_window()
    ff.get('https://www.saucedemo.com/')
    wait = WebDriverWait(ff, 4)
    data = {
        '#user-name': 'standard_user', '#password': 'secret_sauce'
    }

    for locator, value in data.items():
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, locator))).send_keys(value)

    selectors = [
        '#login-button', '#add-to-cart-sauce-labs-backpack',
        '#add-to-cart-sauce-labs-bolt-t-shirt',
        '#add-to-cart-sauce-labs-onesie',
        '.shopping_cart_link',
        '#checkout'
    ]
    for selector in selectors:
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector))).click()

    data_2 = {
        '#first-name': 'Sergey', '#last-name': 'Tsareg',
        '#postal-code': '600006'
    }

    for data1, data2 in data_2.items():
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, data1))).send_keys(data2)

    ff.find_element(By.ID, 'continue').click()
    return ff


def test_total_price(get_result):
    total = get_result.find_element(By.CLASS_NAME, 'summary_total_label').text
    num_total = re.sub(r'[^0-9.$]', '', total)
    assert num_total == '$58.29'
