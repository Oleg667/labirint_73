from pages.labirint_locators import MainPage
from selenium.webdriver import ActionChains

# Для запуска тестов этойго файла ввести в терминал:
# pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_home_page.py

"""Тестируем ссылки в шапке главной страницы. 28 теста."""

"""Логотип"""


def test_logo(web_browser):
    page = MainPage(web_browser)
    page.logo.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


"""Что читать? Рекомендации"""


def test_now_sale(web_browser):
    page = MainPage(web_browser)
    page.now_sale.click()

    assert page.get_current_url() == 'https://www.labirint.ru/now/'


"""Сообщения"""


def test_mesages(web_browser):
    page = MainPage(web_browser)
    page.mesages.click()

    assert page.log_in


"""Мой лабиринт"""


def test_my_labirint(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()

    assert page.log_in


"""Отложено"""


def test_deferred(web_browser):
    page = MainPage(web_browser)
    page.deferred.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


"""Корзина"""


def test_cart(web_browser):
    page = MainPage(web_browser)
    page.cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


"""18+"""


def test_18_plus(web_browser):
    page = MainPage(web_browser)
    page.plus_18.click()

    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'


"""Меню черное - Книги"""


def test_header_books(web_browser):
    page = MainPage(web_browser)
    page.header_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'


"""Меню черное - Главное 2022"""


def test_header_main_2022(web_browser):
    page = MainPage(web_browser)
    page.header_main_2022.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


"""Меню черное - Школа"""


def test_header_school(web_browser):
    page = MainPage(web_browser)
    page.header_school.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


"""Меню черное - Игрушки"""


def test_header_toys(web_browser):
    page = MainPage(web_browser)
    page.header_toys.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'


"""Меню черное - Канцтовары"""


def test_header_office(web_browser):
    page = MainPage(web_browser)
    page.header_office.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'


"""Меню черное - Клуб"""


def test_header_club(web_browser):
    page = MainPage(web_browser)
    page.header_club.click()

    assert page.get_current_url() == 'https://www.labirint.ru/club/'


"""Серый фон - Доставка и оплата"""


def test_delivery_and_payment(web_browser):
    page = MainPage(web_browser)
    page.delivery_and_payment.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


"""Серый фон - Сертификаты"""


def test_certificates(web_browser):
    page = MainPage(web_browser)
    page.certificates.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


"""Серый фон - Рейтинги"""


def test_rating(web_browser):
    page = MainPage(web_browser)
    page.rating.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


"""Серый фон - Новинки"""


def test_new_books(web_browser):
    page = MainPage(web_browser)
    page.new_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


"""Серый фон - Скидки"""


def test_discount(web_browser):
    page = MainPage(web_browser)
    page.discount.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&' \
                                     'paperbooks=1&ebooks=1&otherbooks=1'


"""Серый фон - Контакты"""


def test_contacts(web_browser):
    page = MainPage(web_browser)
    page.contacts.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


"""Серый фон - Поддержка"""


def test_support(web_browser):
    page = MainPage(web_browser)
    page.support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


"""Серый фон - Пункты самовывоза"""


def test_maps(web_browser):
    page = MainPage(web_browser)
    page.maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


"""Серый фон - В соцсетях - Вконтакте"""


def test_in_socials_vkontakte(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vkontakte = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(vkontakte)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


"""Серый фон - В соцсетях - Однокласники"""


def test_in_socials_odnoklasniki(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    odnoklasniki = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-ok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(odnoklasniki)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://ok.ru/labirintru'


"""Серый фон - В соцсетях - Яндекс.Дзен"""


def test_in_socials_dzen(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    dzen = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-zen"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(dzen)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


"""Серый фон - В соцсетях - Телеграм"""


def test_in_socials_telegram(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    telegram = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tg"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(telegram)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://t.me/labirintru'


"""Серый фон - В соцсетях - Ютуб"""


def test_in_socials_youtube(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    youtube = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-yt"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(youtube)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


"""Серый фон - В соцсетях - ТикТок"""


def test_in_socials_tik_tok(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    tik_tok = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tiktok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(tik_tok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru?'


"""Серый фон - В соцсетях - Вконтакте.Дети"""


def test_in_socials_vkontakte_kids(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vkontakte_kids = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk-children"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(vkontakte_kids)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirintdeti'
