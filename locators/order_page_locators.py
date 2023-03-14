from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIRSTNAME = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Имя"]']
    INPUT_LASTNAME = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Фамилия"]']
    INPUT_ADDRESS = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Адрес: куда привезти заказ"]']
    INPUT_STATION = [By.XPATH, './/*[@class="select-search__input" and @placeholder="* Станция метро"]']
    INPUT_PHONE_NUMBER = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Телефон: на него позвонит курьер"]']
    BUTTON_NEXT = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    INPUT_DATE = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Когда привезти самокат"]']
    BUTTON_DATE_NEXT_MONTH = [By.XPATH, './/*[@class="react-datepicker__navigation react-datepicker__navigation--next"]']
    BUTTON_FIRST_DAY = [By.XPATH, '(.//*[@role="button" and text()=1])[1]']
    DROPDOWN_LEASE_TERM = [By.XPATH, './/*[@class="Dropdown-arrow"]']
    CHECKBOX_COLOR_BLACK = [By.ID, 'black']
    INPUT_COMMENT = [By.XPATH, './/*[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="Комментарий для курьера"]']
    BUTTON_BACK = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]']
    BUTTON_MAKE_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]']
    MODAL_CONFIRM_ORDER = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]']
    BUTTON_CONFIRM_ORDER = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]']
    DIV_APPROVE_ORDER_TEXT = [By.XPATH, './/*[@class="Order_Text__2broi"]']
    BUTTON_CHECK_STATE = [By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]']

    def get_locator_by_text(text):
        return [By.XPATH, f'.//*[text()="{text}"]']
