from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pickle


# Locators:
# URI
test_site = "http://demo.hospitalrun.io/"


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(test_site)
        print("Setup is Done")

    def teardown(self):
        self.driver.close()
        self.driver.quit()
        print("Teardown is done")

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open("correct_cookies", "wb"))
        print('The cookies are saved')

    def load_cookies(self):
        for cookie in pickle.load(open("correct_cookies", "rb")):
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        print("The cookies are loaded")


