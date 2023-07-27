import time

import pytest
# from conftest import *
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_all_elements_are_enabled(driver, go_to_regpage):
    '''Проверка наличия полей для ввода информации о новом пользователе: "Имя", "Фамилия",
    "Регион", "Email", "Пароль", "Подтверждение пароля", а также кнопки "Зарегистрироваться"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)
    # Проверяем, что мы оказались на странице "Регистрация"
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"

    # Инициализируем поля ввода данных
    name_field = driver.find_element(By.NAME, 'firstName')
    lastname_field = driver.find_element(By.NAME, 'lastName')
    region_field = driver.find_element(By.TAG_NAME, 'path')
    email_field = driver.find_element(By.ID, 'address')
    pass_field = driver.find_element(By.ID, 'password')
    confpass_field = driver.find_element(By.ID, 'password-confirm')
    reg_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    # Проверяем, что все поля активны
    assert name_field.is_enabled()
    assert lastname_field.is_enabled()
    assert region_field.is_enabled()
    assert email_field.is_enabled()
    assert pass_field.is_enabled()
    assert pass_field.is_enabled()
    assert confpass_field.is_enabled()
    assert reg_btn.is_enabled()


def test_basic_positive_scenario_email(driver, go_to_regpage):
    '''Проверка выполнения базового позитивного сценария регистрации по email'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    # Инициализируем поля ввода данных
    name_field = driver.find_element(By.NAME, 'firstName')
    lastname_field = driver.find_element(By.NAME, 'lastName')
    region_field = driver.find_element(By.TAG_NAME, 'path')
    email_field = driver.find_element(By.ID, 'address')
    pass_field = driver.find_element(By.ID, 'password')
    confpass_field = driver.find_element(By.ID, 'password-confirm')
    reg_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # Заполняем поля
    name_field.send_keys('Василий')
    name_field.send_keys(Keys.TAB)
    lastname_field.send_keys('Петров')
    lastname_field.send_keys(Keys.TAB)
    region_field.click()
    region_field.send_keys(Keys.TAB)
    email_field.send_keys('ok1024@mail.com')
    email_field.send_keys(Keys.TAB)
    pass_field.send_keys('Asd678lkj')
    pass_field.send_keys(Keys.TAB)
    confpass_field.send_keys('Asd678lkj')
    reg_btn.click()
    time.sleep(3)
    # Проверяем, что оказались на странице ввода кода
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Подтверждение email'


def test_basic_positive_scenario_phone(driver, go_to_regpage):
    '''Проверка выполнения базового позитивного сценария регистрации по телефону'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    # Инициализируем поля ввода данных
    name_field = driver.find_element(By.NAME, 'firstName')
    lastname_field = driver.find_element(By.NAME, 'lastName')
    region_field = driver.find_element(By.TAG_NAME, 'path')
    email_field = driver.find_element(By.ID, 'address')
    pass_field = driver.find_element(By.ID, 'password')
    confpass_field = driver.find_element(By.ID, 'password-confirm')
    reg_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # Заполняем поля
    name_field.send_keys('Василий')
    name_field.send_keys(Keys.TAB)
    lastname_field.send_keys('Петров')
    lastname_field.send_keys(Keys.TAB)
    region_field.click()
    region_field.send_keys(Keys.TAB)
    email_field.send_keys('+79443332211')
    email_field.send_keys(Keys.TAB)
    pass_field.send_keys('Asd678lkj')
    pass_field.send_keys(Keys.TAB)
    confpass_field.send_keys('Asd678lkj')
    reg_btn.click()
    time.sleep(3)
    # Проверяем, что оказались на странице ввода кода
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Подтверждение телефона'


def test_existing_email(driver, go_to_regpage):
    '''Проверка попытки регистрации по существующему email'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    # Инициализируем поля ввода данных
    name_field = driver.find_element(By.NAME, 'firstName')
    lastname_field = driver.find_element(By.NAME, 'lastName')
    region_field = driver.find_element(By.TAG_NAME, 'path')
    email_field = driver.find_element(By.ID, 'address')
    pass_field = driver.find_element(By.ID, 'password')
    confpass_field = driver.find_element(By.ID, 'password-confirm')
    reg_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # Заполняем поля
    name_field.send_keys('Василий')
    name_field.send_keys(Keys.TAB)
    lastname_field.send_keys('Петров')
    lastname_field.send_keys(Keys.TAB)
    region_field.click()
    region_field.send_keys(Keys.TAB)
    email_field.send_keys('ok1024@gmail.com')
    email_field.send_keys(Keys.TAB)
    pass_field.send_keys('Asd678lkj')
    pass_field.send_keys(Keys.TAB)
    confpass_field.send_keys('Asd678lkj')
    reg_btn.click()
    time.sleep(3)
    # Проверяем, что оказались на странице ввода кода
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Учетная запись уже существует'


def test_existing_phone(driver, go_to_regpage):
    '''Проверка попытки регистрации по существующему телефону'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    # Инициализируем поля ввода данных
    name_field = driver.find_element(By.NAME, 'firstName')
    lastname_field = driver.find_element(By.NAME, 'lastName')
    region_field = driver.find_element(By.TAG_NAME, 'path')
    email_field = driver.find_element(By.ID, 'address')
    pass_field = driver.find_element(By.ID, 'password')
    confpass_field = driver.find_element(By.ID, 'password-confirm')
    reg_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # Заполняем поля
    name_field.send_keys('Василий')
    name_field.send_keys(Keys.TAB)
    lastname_field.send_keys('Петров')
    lastname_field.send_keys(Keys.TAB)
    region_field.click()
    region_field.send_keys(Keys.TAB)
    email_field.send_keys('+79897291008')
    email_field.send_keys(Keys.TAB)
    pass_field.send_keys('Asd678lkj')
    pass_field.send_keys(Keys.TAB)
    confpass_field.send_keys('Asd678lkj')
    reg_btn.click()
    time.sleep(3)
    # Проверяем, что оказались на странице ввода кода
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Учетная запись уже существует'



@pytest.mark.parametrize('name',
                         ['ВАСИЛИЙ',
                          'василий',
                          'Аа',
                          'а'*30],
                         ids=['name_uppercase',
                              'name_lowercase',
                              'name_min_length',
                              'name_max_length'])
def test_positive_name(driver, go_to_regpage, name):
    '''Позитивные сценарии для поля "Имя"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    name_field = driver.find_element(By.NAME, 'firstName')
    # Заполняем поля
    name_field.clear()
    name_field.send_keys(name)
    name_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is None


@pytest.mark.parametrize('name',
                         ['Vасилий',
                          'А',
                          'а'*31,
                          '123',
                          'Эрих Мария',
                          '~`!@#$%^&*()_+<>?:/”{}[];’'],
                         ids=['name_contains_latin',
                              'name_too_short',
                              'name_too_long',
                              'name_digits',
                              'name_contains_space',
                              'name_specific_symbols'])
def test_negative_name(driver, go_to_regpage, name):
    '''Негативные сценарии для поля "Имя"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    name_field = driver.find_element(By.NAME, 'firstName')
    # Заполняем поля
    name_field.clear()
    name_field.send_keys(name)
    name_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is not None


@pytest.mark.parametrize('lastname',
                         ['ПЕТРОВ',
                          'петров',
                          'Аа',
                          'а'*30,
                          'Мамин-Сибиряк',
                          'Ли Си Цин'],
                         ids=['lastname_uppercase',
                              'lastname_lowercase',
                              'lastname_min_length',
                              'lastname_max_length',
                              'lastname_contains_minus',
                              'lastname_contains_space'])
def test_positive_lastname(driver, go_to_regpage, lastname):
    '''Позитивные сценарии для поля "Фамилия"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    lastname_field = driver.find_element(By.NAME, 'lastName')
    # Заполняем поля
    lastname_field.clear()
    lastname_field.send_keys(lastname)
    lastname_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is None


@pytest.mark.parametrize('lastname',
                         ['ПетроV',
                          'А',
                          'а'*31,
                          '123',
                          '~`!@#$%^&*()_+<>?:/”{}[];’'],
                         ids=['lastname_contains_latin',
                              'lastname_too_short',
                              'lastname_too_long',
                              'lastname_digits',
                              'lastname_specific_symbols'])
def test_negative_lastname(driver, go_to_regpage, lastname):
    '''Негативные сценарии для поля "Фамилия"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    lastname_field = driver.find_element(By.NAME, 'lastName')
    # Заполняем поля
    lastname_field.clear()
    lastname_field.send_keys(lastname)
    lastname_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is not None


@pytest.mark.parametrize('email',
                         ['Vasya@mail.com',
                          'vasya123@mail.com',
                          'vasya-petrov@mail.com',
                          'vasya@super-mail.com',
                          'vasya_petrov@mail.com',
                          'vasya@super_mail.com'],
                         ids=['email_uppercase',
                              'email_digits',
                              'email_name_contains_minus',
                              'email_domain_contains_minus',
                              'email_name_contains_underline',
                              'email_domain_contains_underline'])
def test_positive_email(driver, go_to_regpage, email):
    '''Позитивные сценарии для поля "Email"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    email_field = driver.find_element(By.ID, 'address')
    # Заполняем поля
    email_field.clear()
    email_field.send_keys(email)
    email_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is None


@pytest.mark.parametrize('email',
                         ['vasyamail.com',
                          '@mail.com',
                          'vasya@mail',
                          'vasya@.com',
                          'vasya@mail..com',
                          '.vasya@mail.com',
                          'vasya@.mail.com'],
                         ids=['email_missed_at',
                              'email_missed_name',
                              'email_missed_zone',
                              'email_missed_domain',
                              'email_double_dot',
                              'email_name_begins_with_dot',
                              'email_domain_begins_with_dot'])
def test_negative_email(driver, go_to_regpage, email):
    '''Негативные сценарии для поля "Email"'''
    # Задаем таймаут для неявного ожидания
    driver.implicitly_wait(5)

    email_field = driver.find_element(By.ID, 'address')
    # Заполняем поля
    email_field.clear()
    email_field.send_keys(email)
    email_field.send_keys(Keys.TAB)
    assert driver.find_element(By.CSS_SELECTOR,'.rt-input-container__meta--error') is not None

