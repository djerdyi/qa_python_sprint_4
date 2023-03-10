from selenium import webdriver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as mpl
from time import sleep

class TestMainPage:

    driver = None

    def test_main_page(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.open_question_1()
        check = False
        check = self.driver.find_element(*mpl.PARAGRAPH_ANSWER_1).is_displayed()
        # sleep(5)
        self.driver.quit()

        assert check
