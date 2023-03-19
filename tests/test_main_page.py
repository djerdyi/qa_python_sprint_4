import allure
import pytest

from .. import consts as c
from ..pages.main_page import MainPage


class TestMainPage:

    @allure.title('Кнопка "Заказать" на главной странице.')
    @allure.description(
        'Кликаем на кнопку заказа, проверяем, что ссылка ' +
        'изменилась на "https://qa-scooter.praktikum-services.ru/order".'
    )
    def test_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()

        assert main_page.check_order_url(), (
            f'Текущая ссылка "{driver.current_url}" ' +
            f'не совпадает с ожидаемой "{c.ORDER_BASE_URL}".'
        )

    @allure.title('Консистентность FAQ на галвной странице.')
    @allure.description(
        'Раскрываем все статьи в FAQ и сверяем ответы со справочником.'
    )
    @pytest.mark.parametrize('article_number', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_faq(self, driver, article_number):
        main_page = MainPage(driver)
        main_page.open_question(article_number)

        assert main_page.check_answer(article_number), (
            f'Для вопроса "{main_page.get_question_text(article_number)}" ' +
            f'ожидался ответ "{main_page.get_answer_text(article_number)}".'
        )
