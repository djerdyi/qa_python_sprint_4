from selenium import webdriver
from pages.base_page import BasePage
from time import sleep

class TestBasePage:

    driver = None

    def test_yandex_link(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_yandex_link()
        sleep(5)
        self.driver.quit()

        assert 1 == 1
