from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://uitestingplayground.com/classattr")
findButton = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
findButton.click()
sleep (3)
alert = driver.switch_to.alert
alert.accept()
sleep (3)