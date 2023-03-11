import pytest
import random
import string
from copy import copy

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
VALID_NAME_LENGTH = 2
VALID_LASTNAME_LENGTH = 2
VALID_ADDRESS_LENGTH = 5
VALID_PHONE_NUMBER_LENGTH = 11

@pytest.fixture(autouse=True, scope="function")
def driver():
    '''Get Firefox webdriver'''
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    new_cookie = {"name": "Cartoshka", "value": "true"}
    driver.add_cookie(new_cookie)
    new_cookie = {"name": "Cartoshka-legacy", "value": "true"}
    driver.add_cookie(new_cookie)
    driver.refresh()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def get_correct_order_data():
    '''Get correct order data'''
    order_data = {
        'name': '',
        'lastname': '',
        'address': '',
        'station': '',
        'phone_number': ''
    }
    stations = ['Сокольники', 'Медведково', 'Ленинский проспект', 'Марьино']
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    symbols = cyrillic_lower_letters + cyrillic_lower_letters.upper()
    name = ''.join(random.choice(symbols) for i in range(VALID_NAME_LENGTH))
    lastname = ''.join(random.choice(symbols) for i in range(VALID_LASTNAME_LENGTH))
    address = ''.join(random.choice(symbols) for i in range(VALID_ADDRESS_LENGTH))
    station = stations[random.randint(0, len(stations) - 1)]
    symbols = string.digits
    phone_number = ''.join(random.choice(symbols) for i in range(VALID_PHONE_NUMBER_LENGTH))
    
    order_data['name'] = name
    order_data['lastname'] = lastname
    order_data['address'] = address
    order_data['station'] = station
    order_data['phone_number'] = phone_number

    return order_data
