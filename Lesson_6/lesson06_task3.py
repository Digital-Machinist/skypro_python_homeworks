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
waiter = WebDriverWait(browser, 10)

browser.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

award = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#award'))
)
print(award.get_attribute('src'))
browser.quit()
