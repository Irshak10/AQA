from selenium import webdriver
from Hospitalrun.Pages.MedicationPage import MedicationPage


medication = MedicationPage(webdriver)

medication.enter_username_true()
medication.enter_password_true()
medication.click_login()
medication.login_check()

medication.click_medications()

medication.request_check()
medication.completed_check()
medication.new_request_check()
medication.return_check()

medication.new_request_click()
medication.create_new_medication()
medication.page_check()

print("Correct 4th Test Completed")


