from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

browser = webdriver.Chrome(options=options, service=ChromeService(
    ChromeDriverManager().install()))
browser.maximize_window()
browser.get('http://uitestingplayground.com/textinput')

browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys('SkyPro')
browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()
print(browser.find_element(By.CSS_SELECTOR, "#updatingButton").text)
browser.quit()
