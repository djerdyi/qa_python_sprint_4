from selenium.webdriver.common.by import By

class OrderPageLocators:
    INPUT_FIRSTNAME = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Имя"]']
    INPUT_LASTNAME = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Фамилия"]']
    INPUT_ADDRESS = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Адрес: куда привезти заказ"]']
    INPUT_STATION = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Станция метро"]']
    INPUT_PHONE = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Телефон: на него позвонит курьер"]']
    BUTTON_NEXT = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    INPUT_DATE = [By.CLASS_NAME, 'Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside']
    DROPDOWN_LEASE_TERM = [By.CLASS_NAME, 'Dropdown-root Order_FilledDate__1pb8n']
    DROPDOWN_MENU_OPTION_LEASE_TERM = [By.XPATH, './/*[@class="Dropdown-option" and text()="двое суток"]']
    CHECKBOX_BLACK = [By.ID, 'black']
    INPUT_COMMENT = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="Комментарий для курьера"]']
    BUTTON_BACK = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']
    BUTTON_MAKE_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]']
    BUTTON_CONFIRM_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]']
    DIV_APPROVE_ORDER_TEXT = [By.XPATH, './/*[@class="Order_Text__2broi"]']
    BUTTON_CHECK_STATE = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]']
