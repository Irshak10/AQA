from Hospitalrun.Pages.HomePage import HomePage
from Hospitalrun.Pages.LoginPage import LoginPage
from selenium import webdriver


login = LoginPage(webdriver)
home = HomePage(webdriver)

login.setup()
login.enter_username_true()
login.enter_password_true()
login.click_login()


home.click_setting()
home.click_logout()

login.logout_check()

login.teardown()
print("LogOut Test Completed")