locators.py - содержит локаторы на все элементы веб-страницы, используемых в тестах
settings.py - содержит данные, необходимые для тестирования (логины, пароли, имена и пр.)
test_auth.py - содержит несколько автотестов страницы Ростелекома - https://b2c.passport.rt.ru

Перед прохождением тестов необходимо установить ( для PyCharm - делала все там):
- pytest
- pytest-selenium
- requests
- скачать Selenium WebDriver с https://chromedriver.chromium.org/downloads (выбрать версию совместимую с вашим браузером)
- в файле test_auth.py в строке 16 указать путь, где сохранили вебрайвер с расширением .exe
- запустить тесты через зеленый треугольник в PyCharm или команду python3 -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver test_auth.py
