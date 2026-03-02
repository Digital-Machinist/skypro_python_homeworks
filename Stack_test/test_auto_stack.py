import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-first-run-ui")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument("--disable-features=PasswordManagerOnboarding")
    options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='module')
def app(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://demo.app.stack-it.ru/fl/")
    # Логин
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="login"]'))).send_keys('DEMOWEB')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="password"]'))).send_keys('awdrgy')
    browser.find_element(By.CSS_SELECTOR, '[data-cy="submit-btn"]').click()
    try: wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="btn-yes"]'))).click()
    except: pass
    # Навигация до формы
    nav_buttons = [
        '//div[text()="Адресный фонд"]', '//span[text()=" Адреса проживающих "]', 
        '//button[@title="Добавить запись"]', '//div[text()=" Район "]'
    ]
    for btn in nav_buttons:
        wait.until(EC.element_to_be_clickable((By.XPATH, btn))).click()
    return browser

# 5 ТЕСТОВ 

def test_0_required_field_validation(app):
    # Проверка, что нельзя сохранить район без названия
    wait = WebDriverWait(app, 10)
    
    field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="stack-input"]')))
    field.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
    
    # Пробуем нажать сохранить
    save_btn = app.find_element(By.CSS_SELECTOR, '[data-cy="btn-save"]')
    
    if not save_btn.is_enabled():
        assert not save_btn.is_enabled(), "Кнопка 'Сохранить' должна быть заблокирована для пустого поля"
    
    else:
        save_btn.click()
        error_message = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(text(), "не может быть пустым")]')
        ))
        assert error_message.is_displayed(), "Должно появиться сообщение о пустом поле"

def test_1_dialog_window(app):
    wait = WebDriverWait(app, 10)
    window = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Район (создание)")]')))
    assert "Район (создание)" in window.text

def test_2_added_district(app):
    wait = WebDriverWait(app, 10)
    app.find_element(By.CSS_SELECTOR, '[data-cy="stack-input"]').send_keys('district13')
    app.find_element(By.CSS_SELECTOR, '[data-cy="btn-save"]').click()
    district_in_list = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "district13")]')))
    assert district_in_list.is_displayed()

def test_3_edit_district(app):
    wait = WebDriverWait(app, 10)
    row = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "district13")]/ancestor::tr')))
    row.find_element(By.CSS_SELECTOR, '[data-cy="btn-edit"]').click()
    field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="Название района"]')))
    field.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
    field.send_keys('Район №1')
    field.send_keys(Keys.TAB)
    app.find_element(By.CSS_SELECTOR, '[data-cy="btn-save"]').click()
    updated = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Район №1")]')))
    assert updated.is_displayed()

def test_4_delete_district(app):
    wait = WebDriverWait(app, 10)
    row = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Район №1")]/ancestor::tr')))
    
    checkbox_ripple = row.find_element(By.CSS_SELECTOR, '.v-input--selection-controls__ripple')
    app.execute_script("arguments[0].click();", checkbox_ripple) # Кликаем напрямую по элементу
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="btn-delete"]'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="btn-yes"]'))).click()
    
    # Проверка удаления
    assert wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Район №1")]')))
