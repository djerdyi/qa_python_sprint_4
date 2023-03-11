import locators.main_page_locators as mpl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def order_button(self):
        return self.driver.find_element(*mpl.BUTTON_ORDER)
    
    def click_order_button(self):
        self.order_button().click()
    
    def check_order_url(self):
        return "order" in self.driver.current_url

    def open_question(self, number: int):
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*mpl.get_question_locator(number)).click()
    
    def check_answer(self, number: int):
        return self.driver.find_element(*mpl.get_answer_locator(number)).is_displayed()
    
    def get_question_text(self, number: int):
        return mpl.get_question_text(number)

    def get_answer_text(self, number: int):
        return mpl.get_answer_text(number)
