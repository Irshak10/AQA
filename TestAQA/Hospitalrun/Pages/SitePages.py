from Hospitalrun.Locators.locators import Locators


class SitePages(object):

    def __init__(self, driver):
        self.driver = driver

        self.setting_css_selector = Locators.setting_css_selector
        self.logout_link_text = Locators.logout_link_text
        self.medication_button_id = Locators.medication_button_id

        self.medication_request_button_id = Locators.medication_request_button_id
        self.medication_completed_button_id = Locators.medication_completed_button_id
        self.medication_new_request_button_id = Locators.medication_new_request_button_id
        self.medication_dispense_button_id = Locators.medication_dispense_button_id
        self.medication_return_button_id = Locators.medication_return_button_id





    def click_setting(self):
        self.driver.find_element_by_css_selector(self.setting_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()

    def click_medications(self):
        self.driver.find_element_by_id(self.medication_button_id).click()

    def check_all_medication_buttons(self):
        medication_buttons = self.driver.find_element_by_id(self.medication_request_button_id).text
        self.assertTrue("Requests" in medication_buttons)
