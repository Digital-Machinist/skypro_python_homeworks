import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://labirint.ru")

# найти книги по слову "Питон"
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)
sleep(2)
# найти все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books))

# вывести в консоль информацию : название, автор, цена
cheapestPrice = 9999
cheapestTitle = ''
cheapestAuthor = ''
for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(
        By.CSS_SELECTOR, 'div.product-card__price-current').text
    # 'div.product-card__price-current'
    # 'a.product-card__name'
    author = ''
    try:
        author = book.find_element(
            By.CSS_SELECTOR, 'div.product-card__author').text
    except Exception:
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)
    cleanPrice = re.sub(r'\D', '', price)
    numPrice = int(cleanPrice) if cleanPrice else 0
    print(numPrice)
    if cheapestPrice > numPrice:
        cheapestPrice = numPrice
        cheapestTitle = title
        cheapestAuthor = author
print('Самая дешевая книга - ', cheapestTitle, 'Автора ',
      cheapestAuthor, 'По цене: ', cheapestPrice, '₽')
