from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

browser = webdriver.Chrome(options=options, service=ChromeService(
    ChromeDriverManager().install()))

browser.get('https://uitestingplayground.com/ajax')

browser.implicitly_wait(16)

browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = browser.find_element(By.CSS_SELECTOR, '#content')

print(content.find_element(By.CSS_SELECTOR, 'p.bg-success').text)
browser.quit()
