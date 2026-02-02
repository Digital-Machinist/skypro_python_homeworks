from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get('https://vk.com')
browser.maximize_window()
sleep(2)
browser.minimize_window()
sleep(2)
browser.fullscreen_window()
sleep(2)
browser.set_window_size(1000, 600)
sleep(3)
browser.quit()