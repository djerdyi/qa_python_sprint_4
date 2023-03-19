import allure
import re

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .. import consts as c
from ..locators.order_page_locators import OrderPageLocators as opl
from ..pages.base_page import BasePage


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def name_input(self):
        return self.driver.find_element(*opl.INPUT_FIRSTNAME)
    
    @allure.step('Заполняем имя: {name}')
    def set_name_input(self, name):
        self.name_input().send_keys(name)

    def lastname_input(self):
        return self.driver.find_element(*opl.INPUT_LASTNAME)
    
    @allure.step('Заполняем фамилию: {lastname}')
    def set_lastname_input(self, lastname):
        self.lastname_input().send_keys(lastname)

    def address_input(self):
        return self.driver.find_element(*opl.INPUT_ADDRESS)

    @allure.step('Заполняем адрес: {address}')
    def set_address_input(self, address):
        self.address_input().send_keys(address)

    def station_input(self):
        return self.driver.find_element(*opl.INPUT_STATION)
    
    @allure.step('Заполняем станцию метро: {station}')
    def set_station_input(self, station):
        self.station_input().click()
        self.driver.find_element(*opl.get_locator_by_text(station)).click()

    def phone_number_input(self):
        return self.driver.find_element(*opl.INPUT_PHONE_NUMBER)
    
    @allure.step('Заполняем номер телефона: {phone_number}')
    def set_phone_number_input(self, phone_number):
        self.phone_number_input().send_keys(phone_number)
    
    def next_button(self):
        return self.driver.find_element(*opl.BUTTON_NEXT)
    
    @allure.step('Заполнили первую часть, клик на кнопку "Далее"')
    def click_next_button(self):
        self.next_button().click()
        WebDriverWait(self.driver, c.WAIT_TIME).until(
            ec.element_to_be_clickable(self.make_order_button())
        )
    
    def date_input(self):
        return self.driver.find_element(*opl.INPUT_DATE)
    
    def date_next_month_button(self):
        return self.driver.find_element(*opl.BUTTON_DATE_NEXT_MONTH)

    def date_first_day_button(self):
        return self.driver.find_element(*opl.BUTTON_FIRST_DAY)

    @allure.step(
            'Заполняем дату доставки: ' +
            'клик на поле с датой -> ' +
            'клик на следующий месяц -> ' +
            'выбираем первый день следующего месяца'
    )
    def set_date_input(self):
        self.date_input().click()
        self.date_next_month_button().click()
        self.date_first_day_button().click()

    def lease_term_ddl(self):
        return self.driver.find_element(*opl.DROPDOWN_LEASE_TERM)

    @allure.step('Заполняем срок аренды: {lease_term}')
    def set_lease_term(self, lease_term):
        self.lease_term_ddl().click()
        self.driver.find_element(*opl.get_locator_by_text(lease_term)).click()
    
    def color_checkbox(self):
        return self.driver.find_element(*opl.CHECKBOX_COLOR_BLACK)
    
    @allure.step('Выбираем цвет')
    def set_color_checkbox(self):
        self.color_checkbox().click()
    
    def comment_input(self):
        return self.driver.find_element(*opl.INPUT_COMMENT)
    
    @allure.step('Заполняем комментарий: {comment}')
    def set_comment_input(self, comment):
        self.comment_input().send_keys(comment)
    
    def back_button(self):
        return self.driver.find_element(*opl.BUTTON_BACK)
    
    def click_back_button(self):
        self.back_button().click()
    
    def make_order_button(self):
        return self.driver.find_element(*opl.BUTTON_MAKE_ORDER)
    
    @allure.step('Оформляем заказ кликом на кнопку "Заказать"')
    def click_make_order_button(self):
        self.make_order_button().click()
    
    def confirm_order_popup(self):
        return self.driver.find_element(*opl.MODAL_CONFIRM_ORDER)
    
    def confirm_order_button(self):
        return self.driver.find_element(*opl.BUTTON_CONFIRM_ORDER)
    
    @allure.step('Подтверждаем заказ кликом на кнопку "Да" на всплывающем окне')
    def click_confirm_order_button(self):
        self.confirm_order_button().click()
    
    def order_result_info_text(self):
        return self.driver.find_element(*opl.DIV_APPROVE_ORDER_TEXT)
    
    def get_order_number(self):
        return re.findall(
            c.PATTERN_FIND_ORDER_NUMBER, self.order_result_info_text().text
        )

    # Так и не смог победить задержку ответа с номером заказа.
    # В 1 из 5 тестов AssetionError из-за того, что номер ещё не появился.
    # Никакие ожидания не помогли, поэтому переделал на проверку текста.
    # Как можно решить эту проблему?
    @allure.step('Проверяем, что номер заказа есть в итоговом тексте')
    def check_order_number(self):
        return len(self.get_order_number()) > 0

    @allure.step('Проверяем, что в итоговом тексте содержится "Номер заказа:"')
    def check_successed_order_text(self):
        return c.TEXT_SUCCESSED_ORDER_CHECK in self.order_result_info_text().text

    def make_order_positive(self, order_data: dict):
        base_page = BasePage(self.driver)
        base_page.click_order_button()
        self.set_name_input(order_data['name'])
        self.set_lastname_input(order_data['lastname'])
        self.set_address_input(order_data['address'])
        self.set_station_input(order_data['station'])
        self.set_phone_number_input(order_data['phone_number'])
        self.click_next_button()
        self.set_date_input()
        self.set_lease_term(order_data['lease_term'])
        self.set_color_checkbox()
        self.set_comment_input(order_data['comment'])
        self.click_make_order_button()
        WebDriverWait(self.driver, c.WAIT_TIME).until(
            ec.element_to_be_clickable(self.confirm_order_button())
        )
        self.click_confirm_order_button()
        WebDriverWait(self.driver, c.WAIT_TIME).until(
            ec.element_to_be_clickable(self.order_result_info_text())
        )
