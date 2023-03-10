from selenium import webdriver
from locators.track_page_locators import TrackPageLocators as tpl

class TrackPage:

    def __init__(self, driver):
        self.driver = driver
