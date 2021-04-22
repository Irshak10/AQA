# import pickle
from selenium.webdriver.common.by import By


# Locators:
# URI
test_site = "http://demo.hospitalrun.io/"

test_username_true = "hr.doctor@hospitalrun.io"
test_password_true = "HRt3st12"
username_textbox_id = "identification"
password_textbox_id = "password"
login_button_css_selector = "button.btn-block"


class BasePage(object):

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def enter_username_true(self):
        self.driver.find_element(By.ID, username_textbox_id).clear()
        self.driver.find_element(By.ID, username_textbox_id).send_keys(test_username_true)
        print("The username field is filled")

    def enter_password_true(self):
        self.driver.find_element(By.ID, password_textbox_id).clear()
        self.driver.find_element(By.ID, password_textbox_id).send_keys(test_password_true)
        print("The password field is filled")

    def click_login(self):
        self.driver.find_element_by_css_selector(login_button_css_selector).click()

    # def save_cookies(self):
    #     pickle.dump(self.driver.get_cookies(), open("correct_cookies", "wb"))
    #     print('The cookies are saved')
    #
    # def load_cookies(self):
    #     for cookie in pickle.load(open("correct_cookies", "rb")):
    #         self.driver.add_cookie(cookie)
    #     self.driver.refresh()
    #     print("The cookies are loaded")


