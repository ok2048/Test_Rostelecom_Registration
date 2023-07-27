import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session', autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://b2c.passport.rt.ru')

   yield driver

   driver.quit()

@pytest.fixture(scope='session', autouse=True)
def go_to_regpage(driver):
   """Переход на страницу регистрации"""
   # Кликаем на ссылку "Зарегистрироваться"
   time.sleep(5)
   driver.find_element(By.ID, 'kc-register').click()



