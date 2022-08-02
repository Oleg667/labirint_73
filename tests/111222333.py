import selenium
import pytest
import pytest_selenium
import os


from pages.labirint_locators import MainPage

def test_valid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("1208-41C9-80DB")
    page.enter.click()
    page.automatic_closing.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'