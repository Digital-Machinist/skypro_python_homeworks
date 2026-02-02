from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get('https://ya.ru')

txt = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]').text
print(txt)

tag = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]').tag_name
print(tag)

id = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]').id
print(id)

href = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]'
    ).get_attribute('href')
print(href)

ff = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]'
    ).value_of_css_property('font-family')
print(ff)

color = browser.find_element(
    By.CSS_SELECTOR,
    'a[data-statlog="2informers.stocks.item.300000000101470118"]'
    ).value_of_css_property('color')
print(color)

browser.get('http://uitestingplayground.com/visibility')

isDisplayed = browser.find_element(
    By.CSS_SELECTOR, '#transparentButton').is_displayed()
print(isDisplayed)

browser.find_element(By.CSS_SELECTOR, '#hideButton').click()

isDisplayed = browser.find_element(
    By.CSS_SELECTOR, '#transparentButton').is_displayed()
print(isDisplayed)

browser.get('https://demoqa.com/radio-button')

isEnabled = browser.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(isEnabled)

isEnabled = browser.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(isEnabled)

browser.get('https://the-internet.herokuapp.com/checkboxes')

cb = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
isSelected = cb.is_selected()
print(isSelected)
sleep(2)
cb.click()

isSelected = cb.is_selected()
print(isSelected)
sleep(2)
cb2 = browser.find_element(By.CSS_SELECTOR, 'input:nth-of-type(2)')

isSelected = cb2.is_selected()
print(isSelected)
sleep(2)
cb2.click()

isSelected = cb2.is_selected()
print(isSelected)

sleep(2)
browser.quit()
