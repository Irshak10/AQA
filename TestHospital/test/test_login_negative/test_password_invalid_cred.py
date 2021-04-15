from selenium import webdriver
from Pages.LoginPage import LoginPage


def test_pass_invalid():

    login = LoginPage(webdriver)

    # login.setup()
    login.enter_username_true()
    login.enter_password_false()
    login.click_login()
    login.invalid_message_check()
    # login.teardown()

    print("Correct Login Test Completed")
