from selenium import webdriver
from Hospitalrun.Pages.MedicationPage import MedicationPage
from Hospitalrun.Pages.LoginPage import LoginPage
from Hospitalrun.Tests.BaseTest import setup, teardown


login = LoginPage(webdriver)

medication = MedicationPage()


setup(setup)
login.enter_username_true()
login.enter_password_true()
login.click_login()
login.login_check()

medication.click_medications()

medication.request_check()
medication.completed_check()
medication.new_request_check()
medication.return_check()

medication.new_request_click()
medication.create_new_medication()
medication.page_check()
teardown(teardown)

print("Correct 4th Test Completed")


