import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .. import consts as c
from ..locators.base_page_locators import BasePageLocators as bpl


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies_button(self):
        return self.driver.find_element(*bpl.BUTTON_ACCEPT_COOKIES)
    
    def click_accept_cookies_button(self):
        self.accept_cookies_button().click()

    def yandex_link(self):
        return self.driver.find_element(*bpl.LINK_YANDEX)
    
    @allure.step(
         'Клик на кнопку "Яндекс" > ' +
         'переключение на новую вкладку'
    )
    def click_yandex_link(self):
        self.yandex_link().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step('Проверяем ссылку в адресной строке')
    def check_yandex_url(self):
        return WebDriverWait(self.driver, c.WAIT_TIME).until(
            ec.url_changes(c.YANDEX_REDIRECT_URL)
        )

    def main_page_link(self):
        return self.driver.find_element(*bpl.LINK_MAIN_PAGE)
    
    @allure.step('Клик на ссылку "Самокат"')
    def click_main_page_link(self):
        self.main_page_link().click()

    @allure.step('Проверяем ссылку в адресной строке')
    def check_main_page_url(self):
        return c.BASE_URL == self.driver.current_url

    def order_button(self):
        return self.driver.find_element(*bpl.BUTTON_ORDER)
    
    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.order_button().click()

    @allure.step('Проверяем ссылку в адресной строке')
    def check_order_url(self):
        return c.ORDER_BASE_URL == self.driver.current_url

    def order_state_button(self):
        return self.driver.find_element(*bpl.BUTTON_ORDER_STATE)
    
    @allure.step('Клик на кнопку "Статус заказа"')
    def click_order_state_button(self):
        self.order_state_button().click()
    
    def order_number_input(self):
        return self.driver.find_element(*bpl.INPUT_ORDER_NUMBER)
    
    @allure.step('Проверка отображения поля для ввода номера заказа')
    def check_number_input(self):
        element = self.order_number_input()
        WebDriverWait(self.driver, c.WAIT_TIME).until(ec.visibility_of(element))

        return element.is_displayed()
