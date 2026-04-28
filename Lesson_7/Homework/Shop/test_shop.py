import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.authPage import AuthPage
from Pages.mainPage import MainPage
from Pages.fillFormPage import FillFormPage
from Pages.resultPage import ResultPage


@pytest.fixture
def driver():
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_result(driver):
    authPage = AuthPage(driver)
    authPage.auth('standard_user', 'secret_sauce')

    mainPage = MainPage(driver)
    mainPage.add_products()
    mainPage.checkout()

    fillFormPage = FillFormPage(driver)
    fillFormPage.fill_form()
    fillFormPage.submit()

    resultPage = ResultPage(driver)
    resultPage.check_result('$58.29')
