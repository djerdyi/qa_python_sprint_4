from selenium import webdriver
from locators.order_page_locators import OrderPageLocators as opl

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
