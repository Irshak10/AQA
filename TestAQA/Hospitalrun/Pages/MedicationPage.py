from Hospitalrun.Locators.locators import Locators
from Hospitalrun.Pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import random


class MedicationPage(LoginPage):

    def click_medications(self):
        self.driver.find_element_by_id(Locators.medication_button_id).click()

    def request_check(self):
        request_check = self.driver.find_element_by_link_text(self.medication_request_button_link_text).text
        print("The user is seen on the Medication menu the " + request_check + " button")
        assert request_check == "Requests", "The request button is missed"

    def completed_check(self):
        completed_check = self.driver.find_element_by_link_text(self.medication_completed_button_link_text).text
        print("The user is seen on the Medication menu the " + completed_check + " button")
        assert completed_check == "Completed", "The completed button is missed"

    def new_request_check(self):
        new_request_check = self.driver.find_element_by_link_text(self.medication_new_request_button_link_text).text
        print("The user is seen on the Medication menu the " + new_request_check + " button")
        assert new_request_check == "New Request", "The new request button is missed"

    def return_check(self):
        return_check = self.driver.find_element_by_link_text(self.medication_return_button_link_text).text
        print("The user is seen on the Medication menu the " + return_check + " button")
        assert return_check == "Return Medication", "The return button is missed"

    def new_request_click(self):
        self.driver.find_element_by_link_text(self.medication_new_request_button_link_text).click()

    def create_new_medication(self):
        # Patient field
        self.driver.find_element(By.ID, Locators.patient_field_id).click()
        self.driver.find_element(By.ID, Locators.patient_field_id).send_keys(Locators.patient_test_name)
        self.driver.find_element(By.ID, Locators.patient_field_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, Locators.patient_field_id).send_keys(Keys.BACKSPACE)
        time.sleep(4)
        self.driver.find_element(By.XPATH, Locators.patient_choose_xpath).click()

        # Visit field
        visit = self.driver.find_element(By.ID, Locators.visit_id)
        visit.click()
        time.sleep(2)
        Select(visit).select_by_index(2)

        # Medication field
        medication = self.driver.find_element(By.ID, Locators.medication_text_field)
        medication.click()
        medication.send_keys(Locators.medication_test_text)
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators.medication_choose_xpath).click()

        # Prescription field
        self.driver.find_element(By.ID, Locators.prescription_field_id).click()
        self.driver.find_element(By.ID, Locators.prescription_field_id).send_keys(Locators.prescription_test_text)

        # Prescription Date field
        self.driver.find_element(By.ID, Locators.data).click()
        self.driver.find_element(By.ID, Locators.data).send_keys(Keys.LEFT)

        # Quantity Requested field
        self.driver.find_element(By.ID, Locators.quantity_field_id).send_keys(random.randint(1, 5))

        # Refills field
        self.driver.find_element(By.ID, Locators.refills_field_id).send_keys(random.randint(5, 10))
        time.sleep(4)

        # Add button
        self.driver.find_element(By.XPATH, Locators.add_button_xpath).click()

        # Ok button
        self.driver.find_element(By.XPATH, Locators.ok_button).click()
        print("The new medication request successfully created")

    def page_check(self):
        page_check = self.driver.find_element(By.XPATH, Locators.page_check_xpath).text
        print(page_check)
        print("Medication Request Saved popup isn`t displayed and User stayed on New Medication Request Page")
        assert page_check == "New Medication Request", "User not stayed on New Medication Request Page"


