from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Автоматическая установка и запуск Geckodriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep (3)
nameField = driver.find_element(By.CSS_SELECTOR, '#username')
nameField.click()
nameField.send_keys('tomsmith')
sleep (1)
passwordField = driver.find_element(By.CSS_SELECTOR, '#password')
passwordField.click()
passwordField.send_keys('SuperSecretPassword!')
sleep (1)
loginButton = driver.find_element(By.CSS_SELECTOR, '.fa-sign-in')
loginButton.click()
sleep(2)
success = driver.find_element(By.CSS_SELECTOR, '#flash').text
print (success)
driver.quit()