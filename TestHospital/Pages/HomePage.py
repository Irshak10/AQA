from Pages.BasePage import BasePage


# Locators, Home page objects
setting_css_selector = "span.octicon-gear"
logout_link_text = "Logout"
logout_check_text = "h2.form-signin-heading"


class HomePage(BasePage):

    def click_setting(self):
        print(type(self.driver), self.driver)
        self.driver.find_element_by_css_selector(setting_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(logout_link_text).click()

    def logout_check(self):
        text = self.driver.find_element_by_css_selector(logout_check_text).text
        print("The user is seen the sign in form and text: " + text)
        assert text == "PLEASE SIGN IN", "Error"