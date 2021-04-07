from Hospitalrun.Pages.LoginPage import LoginPage
from selenium import webdriver

login = LoginPage(webdriver)

def test_1():
    login.enter_username_true()
    login.enter_password_true()
    login.click_login()
    login.login_check()


def test_2():
    login.enter_username_false()
    login.enter_password_false()
    login.click_login()
    login.invalid_message_check()