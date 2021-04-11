from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage
import pickle

login = LoginPage(webdriver)

login.setup()
login.enter_username_true()
login.enter_password_true()
login.click_login()
login.save_cookies()

login.login_check()
login.teardown()


print("Correct Login Test Completed")
