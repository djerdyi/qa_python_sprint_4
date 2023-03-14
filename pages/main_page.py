import allure

from .. import consts as c
from ..locators.main_page_locators import MainPageLocators as mpl


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def order_button(self):
        return self.driver.find_element(*mpl.BUTTON_ORDER)
    
    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.order_button().click()
    
    @allure.step('Проверяем ссылку')
    def check_order_url(self):
        return c.ORDER_BASE_URL == self.driver.current_url

    @allure.step('Открываем статью {number}')
    def open_question(self, number: int):
        self.driver.find_element(*mpl.get_question_locator(number)).click()
    
    @allure.step('Проверяем ответ {number}')
    def check_answer(self, number: int):
        return self.driver.find_element(*mpl.get_answer_locator(number)).is_displayed()
    
    def get_question_text(self, number: int):
        return c.FAQ[number]["question"]

    def get_answer_text(self, number: int):
        return c.FAQ[number]["answer"]
