from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage


login = LoginPage(webdriver)

login.setup()
login.enter_username_true()
login.enter_password_true()
login.click_login()

login.login_check()
login.setup()

print("Correct Login Test Completed")
