from selenium.webdriver.common.by import By

from .. import consts as c


class MainPageLocators:
    BUTTON_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    def get_question_locator(number: int):
        return [By.XPATH, f'.//div[text()="{c.FAQ[number]["question"]}"]']

    def get_answer_locator(number: int):
        return [By.XPATH, f'.//p[text()="{c.FAQ[number]["answer"]}"]']
