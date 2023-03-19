from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ACCEPT_COOKIES = [By.XPATH, './/*[@id="rcc-confirm-button"]']
    LINK_YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    LINK_MAIN_PAGE = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    BUTTON_ORDER = [By.CLASS_NAME, 'Button_Button__ra12g']
    BUTTON_ORDER_STATE = [By.XPATH, './/button[@class="Header_Link__1TAG7"]']
    INPUT_ORDER_NUMBER = [By.XPATH, './/input[@class="Input_Input__1iN_Z Header_Input__xIoUq"]']
    BUTTON_TRACK = [By.XPATH, './/button[@class="Button_Button__ra12g Header_Button__28dPO"]']
