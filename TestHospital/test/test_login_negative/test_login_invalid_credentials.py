from selenium import webdriver
from Pages.LoginPage import LoginPage


def test_invalid_login():

    login = LoginPage(webdriver)

    # login.setup()
    login.enter_username_false()
    login.enter_password_true()
    login.click_login()
    login.invalid_message_check()
    # login.teardown()

    print("Correct Login Test Completed")
