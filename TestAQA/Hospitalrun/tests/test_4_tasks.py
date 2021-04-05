from Hospitalrun.Pages.LoginPage import *
from Hospitalrun.Pages.HomePage import *
from Hospitalrun.Pages.MedicationPage import *
from Hospitalrun.Pages.BasePage import *
from selenium import webdriver


def test_1(setup):
    login = LoginPage(webdriver)

    login.enter_username_true()
    login.enter_password_true()
    login.click_login()
    login.login_check()

    print("Correct Login Test Completed")


def test_2(setup):
    login = LoginPage(webdriver)

    login.enter_username_false()
    login.enter_password_false()
    login.click_login()
    login.invalid_message_check()
    print("Correct Login Test Completed")
