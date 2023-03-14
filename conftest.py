import random
import string

import pytest
from selenium import webdriver

from . import consts as c
from .pages.base_page import BasePage


@pytest.fixture(autouse=True, scope="function")
def driver():
    '''Get Firefox webdriver'''
    driver = webdriver.Firefox()
    driver.get(c.BASE_URL)
    driver.maximize_window()
    BasePage(driver).click_accept_cookies_button()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def correct_order_data():
    '''Get correct order data'''
    correct_order_data = {
        'name': '',
        'lastname': '',
        'address': '',
        'station': '',
        'phone_number': '',
        'lease_term': '',
        'comment': ''
    }
    stations = ['Медведково', 'Сокольники', 'Ленинский проспект', 'Марьино']
    lease_terms = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    symbols = cyrillic_lower_letters + cyrillic_lower_letters.upper()

    name = ''.join(random.choice(symbols) for i in range(c.VALID_NAME_LENGTH))
    lastname = ''.join(random.choice(symbols) for i in range(c.VALID_LASTNAME_LENGTH))
    address = ''.join(random.choice(symbols) for i in range(c.VALID_ADDRESS_LENGTH))
    comment = ''.join(random.choice(symbols) for i in range(c.VALID_COMMENT_LENGTH))
    station = stations[random.randint(0, len(stations) - 1)]
    lease_term = lease_terms[random.randint(0, len(lease_terms) - 1)]
    symbols = string.digits
    phone_number = ''.join(random.choice(symbols) for i in range(c.VALID_PHONE_NUMBER_LENGTH))
    
    correct_order_data['name'] = name
    correct_order_data['lastname'] = lastname
    correct_order_data['address'] = address
    correct_order_data['station'] = station
    correct_order_data['phone_number'] = phone_number
    correct_order_data['lease_term'] = lease_term
    correct_order_data['comment'] = comment

    return correct_order_data
