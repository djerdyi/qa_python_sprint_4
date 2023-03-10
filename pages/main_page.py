from selenium import webdriver
from locators.main_page_locators import MainPageLocators as mpl

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_question_1(self):
        element = self.driver.find_element(*mpl.DIV_QUESTION_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
