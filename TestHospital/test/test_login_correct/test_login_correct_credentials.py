from selenium import webdriver
from Pages.LoginPage import LoginPage


def test_login(setup):

    login = LoginPage(webdriver)

    # login.setup()
    login.enter_username_true()
    login.enter_password_true()
    login.click_login()

    login.login_check()
    # login.teardown()

    print("Correct Login Test Completed")
