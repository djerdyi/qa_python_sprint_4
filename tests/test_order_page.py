import allure

from ..pages.order_page import OrderPage
from .. import consts as c


class TestOrderPage:

    @allure.title('Позитивный сценарий оформления заказа.')
    @allure.description(
        'Заполняем все необходимые поля и подтверждаем заказ, ' +
        'в итоговой информации по заказу ищем его номер.'
    )
    def test_positive_make_order(self, driver, correct_order_data):
        order_page = OrderPage(driver)
        order_page.make_order_positive(correct_order_data)

        assert order_page.check_successed_order_text(), (
            f'Ключавая фраза "{c.TEXT_SUCCESSED_ORDER_CHECK}" не найдена в ' +
            f'тексте "{order_page.order_result_info_text().text}".'
        )
