from selenium import webdriver
from Hospitalrun.Pages.HomePage import HomePage
from Hospitalrun.Locators.locators import Locators


home = HomePage(webdriver)

home.setup()
home.enter_username(Locators.test_username_true)
home.enter_password(Locators.test_password_true)
home.click_login()

home.click_setting()
home.click_logout()

home.logout_check()

home.teardown()
print("LogOut Test Completed")