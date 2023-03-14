import allure

from .. import consts as c
from ..pages.base_page import BasePage

class TestBasePage:

    @allure.title('Редирект на страницу Яндекса.')
    @allure.description(
        'Кликаем на кнопку в шапке и ' +
        'провеяем ссылку новой вкладки.'
    )
    def test_yandex_link(self, driver):
        base_page = BasePage(driver)
        base_page.click_yandex_link()

        assert base_page.check_yandex_url(), (
            f'Текущая ссылка "{driver.current_url}" ' +
            f'не совпадает с ожидаемой "{c.YANDEX_REDIRECT_URL}".'
        )
    
    @allure.title('Возврат на главную страницу.')
    @allure.description(
        'Переходим на страницу оформления заказа, кликаем ' +
        'на кнопку в шапке, проверяем, что вернулись на главную.'
    )
    def test_home_link(self, driver):
        base_page = BasePage(driver)
        base_page.click_order_button()
        base_page.click_main_page_link()

        assert base_page.check_main_page_url(), (
            f'Текущая ссылка "{driver.current_url}" ' +
            f'не совпадает с ожидаемой "{c.BASE_URL}".'
        )
    
    @allure.title('Переход на страницу оформления заказа.')
    @allure.description(
        'По кнопке в шапке переходим на страницу оформления заказа, ' +
        'проверяем изменившуюся ссылку.'
    )
    def test_order_button(self, driver):
        base_page = BasePage(driver)
        base_page.click_order_button()

        assert base_page.check_order_url(), (
            f'Текущая ссылка "{driver.current_url}" ' +
            f'не совпадает с ожидаемой "{c.ORDER_BASE_URL}".'
        )
    
    @allure.title('Проверка кнопки статуса заказа.')
    @allure.description(
        'Кликаем на кнопку "Статус заказа", проверяем, ' +
        'что появилось поле для ввода номера заказа.'
    )
    def test_order_state_button(self, driver):
        base_page = BasePage(driver)
        base_page.click_order_state_button()

        assert base_page.check_number_input(), (
            'Не найдено поля для ввода номера заказа.'
        )
