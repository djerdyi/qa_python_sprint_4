from selenium import webdriver
from locators.base_page_locators import BasePageLocators as bpl

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_yandex_link(self):
        self.driver.find_element(*bpl.LINK_YANDEX).click()
