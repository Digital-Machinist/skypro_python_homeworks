import pytest
from selenium import webdriver
from pages.mainPage import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_result(driver):
    calc_page = MainPage(driver)
    calc_page.set_delay('45')
    calc_page.press_buttons('7', '+', '8')
    calc_page.check_calc_sum_result('15')