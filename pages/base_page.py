from selenium import webdriver
from locators.base_page_locators import BasePageLocators as bpl

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def yandex_link(self):
        return self.driver.find_element(*bpl.LINK_YANDEX)
    
    def click_yandex_link(self):
        self.yandex_link().click()
    
    def main_page_link(self):
        return self.driver.find_element(*bpl.LINK_MAIN_PAGE)
    
    def click_main_page_link(self):
        self.main_page_link().click()

    def order_button(self):
        return self.driver.find_element(*bpl.BUTTON_ORDER)
    
    def click_order_button(self):
        self.order_button().click()

    def order_state_button(self):
        return self.driver.find_element(*bpl.BUTTON_ORDER_STATE)
    
    def click_order_state_button(self):
        self.order_state_button().click()
