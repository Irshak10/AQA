from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage
import time


login = LoginPage(webdriver)

login.setup()
login.enter_username_true()
login.enter_password_true()
login.click_login()
login.login_check()

time.sleep(10)
login.save_cookies()
login.teardown()


print("Correct Login Test Completed")
