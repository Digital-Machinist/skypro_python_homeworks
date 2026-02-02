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

browser.get("http://the-internet.herokuapp.com/")

waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'a[href="/abtest"]'), "A/B Testing")
)
browser.find_element(By.CSS_SELECTOR, 'a[href="/abtest"]').is_enabled
print('элемент A/B Testing прогрузился и виден')
