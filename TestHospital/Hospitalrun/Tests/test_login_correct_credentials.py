from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage


login = LoginPage(webdriver)

login.enter_username_true()
login.enter_password_true()
login.click_login()

login.login_check()

print("Correct Login Test Completed")
