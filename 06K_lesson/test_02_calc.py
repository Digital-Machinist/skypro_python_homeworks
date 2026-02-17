import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-first-run-ui")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    browser = webdriver.Chrome(options=options, service=ChromeService(
        ChromeDriverManager().install()))
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture(scope='module')
def fill_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 50)
    wait.until(EC.presence_of_element_located(
        (By.ID, 'delay'))).clear()
    wait.until(EC.presence_of_element_located(
        (By.ID, 'delay'))).send_keys('45')

    buttons = [
        '//span[text()="7"]', '//span[text()="+"]', '//span[text()="8"]',
        '//span[text()="="]'
    ]

    for button in buttons:
        wait.until(EC.element_to_be_clickable((By.XPATH, button))).click()
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15'))
    return driver


def test_calculator_sum_result(fill_form):
    final_text = fill_form.find_element(By.CLASS_NAME, 'screen').text
    assert final_text == '15'
