from Hospitalrun.Pages.BasePage import BasePage


# Locators, Home page objects
setting_css_selector = "span.octicon-gear"
logout_link_text = "Logout"


class HomePage(BasePage):

    def click_setting(self):
        self.driver.find_element_by_css_selector(setting_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(logout_link_text).click()