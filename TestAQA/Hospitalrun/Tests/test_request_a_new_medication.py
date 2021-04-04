from selenium import webdriver
import time
from Hospitalrun.Pages.MedicationPage import MedicationPage
from Hospitalrun.Locators.locators import Locators

medication = MedicationPage(webdriver.Chrome)

medication.setup()
medication.enter_username(Locators.test_username_true)
medication.enter_password(Locators.test_password_true)
medication.click_login()

time.sleep(2)


medication.click_medications()
medication.request_check()
medication.completed_check()
medication.new_request_check()
medication.return_check()
medication.new_request_click()
time.sleep(2)

medication.create_new_medication()

time.sleep(2)

medication.teardown()

print("Correct 4th Test Completed")


