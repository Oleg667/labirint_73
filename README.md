# labirint_tests
Проект по курсу Тестировщик-автоматизатор на Python (QAP) с использованием PyTest и Selenium интернет-магазина Labirint.ru.

Для запуска тестов необходимо предварительно установить следующие библиотеки (pip install):

pytest
pytest-selenium
selenium
termcolor
allure-python-commons

Актуальный на 21.03.2022 драйвер для браузера Chrome лежит в папке tests.

Для запуска всех тестов в данном репрезитории необходимо ввести команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe

pytest -v --driver Chrome --driver-path chromedriver.exe

Тестируемые сценарии:

tests_test_auth_page.py - Тестируем возможность входа в личный кабинет. 4 теста. 
Для запуска теста вводим команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_auth_page.py

test_book_page.py - Тестируем книги с главной страницы. 4 теста. 
Для запуска теста вводим команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_book_page.py

test_home_page.py - Тестируем ссылки в шапке главной страницы. 28 теста. 
Для запуска теста вводим команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_home_page.py

test_search_page.py - Тестируем поиск по тексту с главной страницы. 7 тестов. 
Для запуска теста вводим команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_search_page.py

test_cart_page.py - Тестируем корзину с книгами. 3 теста. 
Для запуска теста вводим команду: pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_cart_page.py
