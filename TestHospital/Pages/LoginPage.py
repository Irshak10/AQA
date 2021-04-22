from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


# Locators, Login Page object

test_username_false = "test"
test_password_false = "123"

username_textbox_id = "identification"
password_textbox_id = "password"
login_button_css_selector = "button.btn-block"
alert_message_css_selector = "div.form-signin-alert"
alert_message_correct_login = "h1.view-current-title"


class LoginPage(BasePage):

    def enter_username_false(self):
        self.driver.find_element(By.ID, username_textbox_id).clear()
        self.driver.find_element(By.ID, username_textbox_id).send_keys(test_username_false)
        print("The username field is filled")

    def enter_password_false(self):
        self.driver.find_element(By.ID, password_textbox_id).clear()
        self.driver.find_element(By.ID, password_textbox_id).send_keys(test_password_false)
        print("The password field is filled")

    def click_login(self):
        self.driver.find_element_by_css_selector(login_button_css_selector).click()

    def login_check(self):
        text = self.driver.find_element_by_css_selector(alert_message_correct_login).text
        print("The user is seen the text: " + text)
        assert text == "Patient Listing", "Error"

    def invalid_message_check(self):
        element = self.driver.find_element_by_css_selector(alert_message_css_selector).text
        print("The message in the Page: " + element)
        assert element == "Username or password is incorrect.", "The test case is down"






