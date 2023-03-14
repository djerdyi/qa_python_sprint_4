from selenium.webdriver.common.by import By

# BUTTON_ORDER = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
BUTTON_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    def get_question_locator(number: int):
    return [By.XPATH, f'.//div[text()="{FAQ[number]["question"]}"]']

def get_answer_locator(number: int):
    return [By.XPATH, f'.//p[text()="{FAQ[number]["answer"]}"]']

def get_question_text(number: int):
    return FAQ[number]["question"]

def get_answer_text(number: int):
    return FAQ[number]["answer"]
