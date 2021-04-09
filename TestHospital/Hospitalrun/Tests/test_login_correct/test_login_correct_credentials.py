from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage
from Hospitalrun.Tests.BaseTest import setup, teardown


login = LoginPage(webdriver)

setup()
login.enter_username_true()
login.enter_password_true()
login.click_login()

login.login_check()
teardown()


print("Correct Login Test Completed")
