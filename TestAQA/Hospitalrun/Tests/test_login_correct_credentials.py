from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage
from Hospitalrun.Locators.locators import Locators


login = LoginPage(webdriver)

login.setup()
login.enter_username(Locators.test_username_true)
login.enter_password(Locators.test_password_true)
login.click_login()

login.login_check()
login.teardown()

print("Correct Login Test Completed")
