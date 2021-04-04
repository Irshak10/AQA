from Hospitalrun.Locators.locators import Locators
from Hospitalrun.Pages.LoginPage import LoginPage


class HomePage(LoginPage):

    def click_setting(self):
        self.driver.find_element_by_css_selector(Locators.setting_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()