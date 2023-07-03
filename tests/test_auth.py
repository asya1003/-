import pytest
import time
from locators import AuthLocators
from settings import AuthData
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\Chromedriver\chromedriver_win32\chromedriver.exe')
   # Переходим на страницу авторизации

   pytest.driver.get('https://b2c.passport.rt.ru')
   WebDriverWait(pytest.driver, 40).until(EC.presence_of_element_located((By.ID, "kc-login")))

   yield

   pytest.driver.quit()


def test_EXP_001():

   # Вводим email
   pytest.driver.find_element(*AuthLocators.AUTH_EMAIL).send_keys(*AuthData.valid_email)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   assert "redirect_uri" in pytest.driver.current_url

def test_EXP_002():
   # Вводим телефон
   pytest.driver.find_element(*AuthLocators.AUTH_PHONE).send_keys(*AuthData.valid_phone)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   assert "redirect_uri" in pytest.driver.current_url

def test_EXP_003():
   # Вводим логин
   pytest.driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(*AuthData.valid_login)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   assert "redirect_uri" in pytest.driver.current_url
   print("Text 'redirect_uri' not found in url!")

def test_EXP_004():
   # Вводим лицевой счет
   pytest.driver.find_element(*AuthLocators.AUTH_ACCOUNT).send_keys(*AuthData.valid_account)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   assert "redirect_uri" in pytest.driver.current_url

def test_EXP_005():
   # Вводим некорректный телефон
   pytest.driver.find_element(*AuthLocators.AUTH_PHONE).send_keys(*AuthData.invalid_phone)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(By.ID, 'form-error-message').text
   print(text_error)
   assert text_error == 'Неверный логин или пароль'

def test_EXP_006():
   # Вводим некорректный email
   pytest.driver.find_element(*AuthLocators.AUTH_EMAIL).send_keys(*AuthData.invalid_email)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.AUTH_ERROR_MESSAGE).text
   print(text_error)
   assert text_error == 'Неверный логин или пароль'

def test_EXP_007():
   # Вводим неверный логин
   pytest.driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(*AuthData.invalid_login)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.AUTH_ERROR_MESSAGE).text
   print(text_error)
   assert text_error == 'Неверный логин или пароль'

def test_EXP_008():
   # Вводим неверный лицевой счет
   pytest.driver.find_element(*AuthLocators.AUTH_ACCOUNT).send_keys(*AuthData.invalid_account)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(*AuthData.valid_password)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.AUTH_ERROR_MESSAGE).text
   print(text_error)
   assert text_error == 'Неверный логин или пароль'

def test_EXP_009():
   # Вводим email
   pytest.driver.find_element(*AuthLocators.AUTH_EMAIL)
   # Вводим пароль
   pytest.driver.find_element(*AuthLocators.AUTH_PASS)
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(*AuthLocators.AUTH_BTN).click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text

   assert 'Введите' in text_error

def test_EXP_010():
   # Нажимаем на кнопку зарегистрироваться
   pytest.driver.find_element(*AuthLocators.REGISTER).click()
   time.sleep(2)
   # В форме регистрации нажимаем на кнопку зарегистрироваться
   pytest.driver.find_element(*AuthLocators.REG_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text

   assert 'Введите' in text_error or 'Необходимо' in text_error

def test_EXP_011():
   # Нажимаем на кнопку забыли пароль
   pytest.driver.find_element(*AuthLocators.PASS_RECOVERY).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   text_error = pytest.driver.find_element(*AuthLocators.RECOVERY_TITLE).text

   assert 'Восстановление пароля' in text_error

def test_EXP_012():
   pytest.driver.find_element(*AuthLocators.REGISTER).click()
   time.sleep(2)
   window_before = pytest.driver.window_handles[0]
   # Нажимаем на кнопку забыли пароль
   pytest.driver.find_element(*AuthLocators.AGREEMENT).click()
   time.sleep(2)
   window_after = pytest.driver.window_handles[1]
   pytest.driver.switch_to.window(window_after)
   # Проверяем, что мы оказались на главной странице пользователя
   text_agreement = pytest.driver.find_element(*AuthLocators.AGREEMENT_TITLE).text
   assert 'Пользовательского соглашения' in text_agreement and 'agreement' in pytest.driver.current_url

def test_EXP_013():
   # Нажимаем на кнопку зарегистрироваться
   pytest.driver.find_element(*AuthLocators.REGISTER).click()
   time.sleep(2)

   # В форме регистрации нажимаем на поле имя и вводим данные 1 символ
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.invalid_name_1)
   time.sleep(1)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   time.sleep(2)
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные латинские буквы
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.invalid_name_2)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные цифры
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.invalid_name_3)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные спец символы
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.invalid_name_4)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные 2 символа
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.valid_name_1)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   time.sleep(1)
   # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные несколько символов через тире
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.valid_name_2)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   time.sleep(1)
   # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные 30 символов
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.valid_name_3)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   time.sleep(1)
    # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле имя и вводим данные 31 символ
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.invalid_name_4)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).click()
   time.sleep(1)
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите'  in text_error or 'Необходимо'  in text_error

def test_EXP_014():
   # Нажимаем на кнопку зарегистрироваться
   pytest.driver.find_element(*AuthLocators.REGISTER).click()
   time.sleep(2)

   # В форме регистрации нажимаем на поле фамилия и вводим данные 1 символ кириллица
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.invalid_surname_1)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные латиницу
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.invalid_surname_2)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные цифры
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.invalid_surname_3)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные спец символы
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.invalid_surname_4)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите' in text_error or 'Необходимо' in text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные кирилица 2 символа
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.valid_surname_1)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   time.sleep(1)
   # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные символы кирилицы через тире
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.valid_surname_2)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   time.sleep(1)
   # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные 30 символов кириллицы
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.valid_surname_3)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   time.sleep(1)
    # Проверяем, что не выходит ошибка заполнения поля
   try:
      text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   except NoSuchElementException as exception:
      text_error = 'None'
      assert 'None' == text_error

   pytest.driver.refresh()

   # В форме регистрации нажимаем на поле фамилия и вводим данные 31 символ (кириллица плюс пробел)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.invalid_surname_4)
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).click()
   time.sleep(1)
   # Проверяем, что выходит ошибка заполнения поля
   text_error = pytest.driver.find_element(*AuthLocators.REG_ERROR_MESSAGE).text
   assert 'Введите'  in text_error or 'Необходимо'  in text_error

def test_EXP_015():
   time.sleep(2)
   window_before = pytest.driver.window_handles[0]
   # Нажимаем на кнопку забыли пароль
   pytest.driver.find_element(*AuthLocators.AGREEMENT).click()
   time.sleep(2)
   window_after = pytest.driver.window_handles[1]
   pytest.driver.switch_to.window(window_after)
   # Проверяем, что мы оказались на главной странице пользователя
   text_agreement = pytest.driver.find_element(*AuthLocators.AGREEMENT_TITLE).text
   assert 'Пользовательского соглашения' in text_agreement and 'agreement' in pytest.driver.current_url

def test_EXP_016():
   time.sleep(2)
   # Нажимаем на кнопку войти по временному коду
   pytest.driver.find_element(*AuthLocators.TEMPORARY_CODE_BTN).click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   title_text = pytest.driver.find_element(*AuthLocators.TEMPORARY_CODE_TITLE).text
   assert 'Авторизация по коду' in title_text

def test_EXP_017():
   # Нажимаем на кнопку зарегистрироваться
   pytest.driver.find_element(*AuthLocators.REGISTER).click()
   time.sleep(2)

   # В форме регистрации нажимаем на поле имя и вводим данные
   pytest.driver.find_element(*AuthLocators.INPUT_FIRSTNAME).send_keys(*AuthData.name)
   pytest.driver.find_element(*AuthLocators.INPUT_LASTNAME).send_keys(*AuthData.surname)
   pytest.driver.find_element(*AuthLocators.INPUT_ADDRESS).send_keys(*AuthData.address)
   pytest.driver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(*AuthData.password)
   pytest.driver.find_element(*AuthLocators.INPUT_CONFIRM_PASS).send_keys(*AuthData.password_confirm)
   time.sleep(2)
   pytest.driver.find_element(*AuthLocators.REG_BTN).click()
   time.sleep(4)
   # Проверяем, что выходит сообщение, что аккаунт с такими данными уже есть
   text_error = pytest.driver.find_element(*AuthLocators.REG_TEXT_ERROR).text
   assert 'Учётная запись уже существует' == text_error

