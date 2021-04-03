from Hospitalrun.Locators.locators import Locators


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

        self.setting_css_selector = Locators.setting_css_selector
        self.logout_link_text = Locators.logout_link_text

    def click_setting(self):
        self.driver.find_element_by_css_selector(self.setting_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()
