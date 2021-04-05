from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Locators:
# URI
test_site = "http://demo.hospitalrun.io/"


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
