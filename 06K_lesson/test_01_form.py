import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    options = Options()
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-first-run-ui")
    browser = webdriver.Edge(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture(scope='module')
def fill_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 4)
    names = {
        'first-name': 'Иван', 'last-name': 'Петров', 'address': 'Ленина 5',
        'e-mail': 'test@mail.ru', 'phone': '+7999', 'city': 'Москва',
        'country': 'РФ', 'job-position': 'QA', 'company': 'SkyPro'
    }

    for name, value in names.items():
        wait.until(EC.visibility_of_element_located(
            (By.NAME, name))).send_keys(value)

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[type="submit"]'))).click()
    return driver


def test_zipcode_is_red(fill_form):
    zip_class = fill_form.find_element(
        By.ID, "zip-code").get_attribute('class')
    assert "alert-danger" in zip_class, "Поле Zipcode не подсвечено красным!"


@pytest.mark.parametrize('field_id', [
    'first-name', 'last-name', 'address', 'e-mail',
    'phone', 'city', 'country', 'job-position', 'company'
])
def test_fields_are_green(fill_form, field_id):
    field_class = fill_form.find_element(
        By.ID, field_id).get_attribute('class')
    assert 'alert-success' in field_class, f"Поле {field_id} не зелёное!"
