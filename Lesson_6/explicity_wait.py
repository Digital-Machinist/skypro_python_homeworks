from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
browser = webdriver.Chrome(options=options, service=ChromeService(
    ChromeDriverManager().install()))
waiter = WebDriverWait(browser, 40, 0.01)

browser.get('https://uitestingplayground.com/progressbar')

browser.find_element(By.CSS_SELECTOR, '#startButton').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

browser.find_element(By.CSS_SELECTOR, '#stopButton').click()

print(browser.find_element(By.CSS_SELECTOR, '#result').text)
browser.quit()
