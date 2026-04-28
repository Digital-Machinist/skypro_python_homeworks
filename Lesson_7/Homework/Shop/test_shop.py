import pytest
from selenium import webdriver
from config import Config
from Pages.authPage import AuthPage
from Pages.mainShopPage import MainPage
from Pages.cartPage import CartPage
from Pages.fillFormPage import FillFormPage
from Pages.resultPage import ResultPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_result(driver):
    authPage = AuthPage(driver)
    authPage.auth(Config.USERNAME, Config.PASSWORD)

    mainPage = MainPage(driver)
    mainPage.add_products()
    mainPage.goto_cart()

    cartPage = CartPage(driver)
    cartPage.check_cart()
    cartPage.submit()

    fillFormPage = FillFormPage(driver)
    fillFormPage.fill_form()
    fillFormPage.submit()

    resultPage = ResultPage(driver)
    resultPage.check_result(Config.TOTAL_PRICE)
