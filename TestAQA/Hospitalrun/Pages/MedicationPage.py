from Hospitalrun.Locators.locators import Locators
from Hospitalrun.Pages.LoginPage import LoginPage
from selenium.webdriver.support.select import Select


class MedicationPage(LoginPage):

    def click_medications(self):
        self.driver.find_element_by_id(Locators.medication_button_id).click()

    def request_check(self):
        request_check = self.driver.find_element_by_link_text(self.medication_request_button_link_text).text
        print("The user is seen the " + request_check + " button")
        assert request_check == "Requests", "The request button is missed"

    def completed_check(self):
        completed_check = self.driver.find_element_by_link_text(self.medication_completed_button_link_text).text
        print("The user is seen the " + completed_check + " button")
        assert completed_check == "Completed", "The completed button is missed"

    def new_request_check(self):
        new_request_check = self.driver.find_element_by_link_text(self.medication_new_request_button_link_text).text
        print("The user is seen the " + new_request_check + " button")
        assert new_request_check == "New Request", "The new request button is missed"

    def return_check(self):
        return_check = self.driver.find_element_by_link_text(self.medication_return_button_link_text).text
        print("The user is seen the " + return_check + " button")
        assert return_check == "Return Medication", "The return button is missed"

    def new_request_click(self):
        self.driver.find_element_by_link_text(self.medication_new_request_button_link_text).click()

    def create_new_medication(self):
        start = self.driver.find_element_by_css_selector(self.patient_field_css)
        start.click()
        start.send_keys(Locators.patient_test_name)
        # Select(self.driver.find_element_by_css_selector(self.patient_field_css)).select_by_visible_text("P00201")

        # patient_dropdown = self.driver.find_element_by_css_selector(self.patient_field_css)
        # patient_dropdown.click()
        # patient_dropdown.send_key(Locators.patient_test_name)
        # dropdown = Select(patient_dropdown)
        # dropdown.select_by_visible_text('P00201')



