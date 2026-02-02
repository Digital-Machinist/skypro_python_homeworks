from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.maximize_window()

# Переходим на сайт
driver.get("https://aviasales.ru")

# Откуда
where_from_input = driver.find_element(
    By.CSS_SELECTOR, "#avia_form_origin-input")
where_from_input.send_keys("Нижний Новгород", Keys.TAB)
sleep(2)

# Куда
where_to_input = driver.find_element(
    By.CSS_SELECTOR, "#avia_form_destination-input")
where_to_input.send_keys("Санкт-Петербург", Keys.RETURN)
sleep(5)

# Когда
when_input = driver.find_element(
    By.CSS_SELECTOR, '[data-test-id="start-date-value"]')
when_input.click()
sleep(2)
when_data_input = driver.find_element(
    By.CSS_SELECTOR, '[aria-label="пятница, 20 февраля 2026 г."]')
when_data_input.click()

# Обратно
till_input = driver.find_element(
    By.CSS_SELECTOR, '[data-test-id="end-date-value"]')
till_input.click()
till_data_input = driver.find_element(
    By.CSS_SELECTOR, '[aria-label="четверг, 26 февраля 2026 г."]')
till_data_input.click()
sleep(2)

# Поиск
find_button = driver.find_element(
    By.CSS_SELECTOR, '[data-test-id="form-submit"]')
find_button.click()

sleep(50)


# Локатор поля Откуда
# #avia_form_origin-input

# Локатор поля Куда
# #avia_form_destination-input


# Локатор поля Когда
# [data-test-id="start-date-field"]

# Локатор поля Обратно
# [data-test-id="end-date-value"]

# Локатор кнопки Найти билеты
# .s__sAFIqDfZ9s87sdX1

# Локатор самого дешевого билета
# [data-test-id="ticket-preview-badge-cheapest"]
