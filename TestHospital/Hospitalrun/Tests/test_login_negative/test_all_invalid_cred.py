from selenium import webdriver
from Hospitalrun.Pages.LoginPage import LoginPage


login = LoginPage(webdriver)

login.setup()
login.enter_username_false()
login.enter_password_false()
login.click_login()
login.invalid_message_check()
login.teardown()

print("Invalid Login Test Completed")
