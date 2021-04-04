from selenium import webdriver
from Hospitalrun.Locators.locators import Locators


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.setting_css_selector = Locators.setting_css_selector
        self.logout_link_text = Locators.logout_link_text

        self.medication_button_id = Locators.medication_button_id

        self.medication_request_button_link_text = Locators.medication_request_button_link_text
        self.medication_completed_button_link_text = Locators.medication_completed_button_link_text
        self.medication_new_request_button_link_text = Locators.medication_new_request_button_link_text
        self.medication_return_button_link_text = Locators.medication_return_button_link_text
        self.patient_field_css = Locators.patient_field_css

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=Locators.Chrome_executable_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(Locators.test_site)
        print("Setup is Done")

    def teardown(self):
        self.driver.close()
        self.driver.quit()
        print("Teardown is done")

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        print("The username field is filled")

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        print("The password field is filled")

    def click_login(self):
        self.driver.find_element_by_css_selector(Locators.login_button_css_selector).click()

    def login_check(self):
        text = self.driver.find_element_by_css_selector(Locators.alert_message_correct_login).text
        print("The user is seen the text: " + text)
        assert text == "Patient Listing", "Error"

    def invalid_message_check(self):
        element = self.driver.find_element_by_css_selector(Locators.alert_message_css_selector).text
        print("The message in the Page: " + element)
        assert element == "Username or password is incorrect.", "The test case is down"

    def logout_check(self):
        text = self.driver.find_element_by_css_selector(Locators.logout_check_text).text
        print("The user is seen the sign in form and text: " + text)
        assert text == "PLEASE SIGN IN", "Error"




