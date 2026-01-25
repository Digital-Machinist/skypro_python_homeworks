from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Автоматическая установка и запуск Geckodriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()
sleep (3)
findField = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
findField.click()
findField.send_keys('Sky')
sleep (1)
findField.clear()
sleep (1)
findField.send_keys('Pro')
sleep (3)
# Закрытие браузера
driver.quit()