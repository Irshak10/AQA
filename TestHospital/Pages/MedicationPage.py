from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random
import time


# Locators, Medication Page object

medication_button_id = "ember767"
medication_request_button_link_text = "Requests"
medication_completed_button_link_text = "Completed"
medication_new_request_button_link_text = "New Request"
medication_return_button_link_text = "Return Medication"

# New Medication Request
patient_field_id = "patientTypeAhead-ember1269"
patient_test_name = "Test Patient"
patient_choose_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/div/div/div[4]"

visit_id = "visit-ember1314"
medication_text_field = "inventoryItemTypeAhead-ember1336"
medication_choose_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/form/div[2]/div/span/div/div/div[2]/strong"
medication_test_text = "Pramoxine"
prescription_field_id = "prescription-ember1368"
prescription_test_text = "Testing prescription"
data = "display_prescriptionDate-ember1391"
quantity_field_id = "quantity-ember1410"
refills_field_id = "refills-ember1417"
add_button_xpath = "/html/body/div[1]/div/div[2]/div/div/div[2]/button[2]"
ok_button = "/html/body/div[1]/div[2]/div/div/div/div[3]/button"
page_check_xpath = "/html/body/div[1]/div/div[1]/div[1]/h1"


class MedicationPage(BasePage):

    def click_medications(self):
        self.driver.find_element_by_id(medication_button_id).click()

    def request_check(self):
        request_check = self.driver.find_element_by_link_text(medication_request_button_link_text).text
        print("The user is seen on the Medication menu the " + request_check + " button")
        assert request_check == "Requests", "The request button is missed"

    def completed_check(self):
        completed_check = self.driver.find_element_by_link_text(medication_completed_button_link_text).text
        print("The user is seen on the Medication menu the " + completed_check + " button")
        assert completed_check == "Completed", "The completed button is missed"

    def new_request_check(self):
        new_request_check = self.driver.find_element_by_link_text(medication_new_request_button_link_text).text
        print("The user is seen on the Medication menu the " + new_request_check + " button")
        assert new_request_check == "New Request", "The new request button is missed"

    def return_check(self):
        return_check = self.driver.find_element_by_link_text(medication_return_button_link_text).text
        print("The user is seen on the Medication menu the " + return_check + " button")
        assert return_check == "Return Medication", "The return button is missed"

    def new_request_click(self):
        self.driver.find_element_by_link_text(medication_new_request_button_link_text).click()

    def create_new_medication(self):
        # Patient field
        self.driver.find_element(By.ID, patient_field_id).send_keys(patient_test_name)
        time.sleep(5)
        self.driver.find_element(By.ID, patient_field_id).send_keys(Keys.BACKSPACE)
        time.sleep(3)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, patient_choose_xpath)))
        self.driver.find_element(By.XPATH, patient_choose_xpath).click()

        # Visit field
        visit = self.driver.find_element(By.ID, visit_id)
        visit.click()
        time.sleep(2)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_selected(By.ID, visit_id))
        Select(visit).select_by_index(2)

        # Medication field
        medication = self.driver.find_element(By.ID, medication_text_field)
        medication.click()
        medication.send_keys(medication_test_text)
        self.driver.find_element(By.XPATH, medication_choose_xpath).click()

        # Prescription field
        self.driver.find_element(By.ID, prescription_field_id).click()
        self.driver.find_element(By.ID, prescription_field_id).send_keys(prescription_test_text)

        # Prescription Date field
        self.driver.find_element(By.ID, data).click()
        self.driver.find_element(By.ID, data).send_keys(Keys.LEFT)

        # Quantity Requested field
        self.driver.find_element(By.ID, quantity_field_id).send_keys(random.randint(1, 5))

        # Refills field
        self.driver.find_element(By.ID, refills_field_id).send_keys(random.randint(5, 10))

        # Add button
        self.driver.find_element(By.XPATH, add_button_xpath).click()

        # Ok button
        self.driver.find_element(By.XPATH, ok_button).click()
        print("The new medication request successfully created")

    def page_check(self):
        page_check = self.driver.find_element(By.XPATH, page_check_xpath).text
        print(page_check)
        print("Medication Request Saved popup isn`t displayed and User stayed on New Medication Request Page")
        assert page_check == "New Medication Request", "User not stayed on New Medication Request Page"


