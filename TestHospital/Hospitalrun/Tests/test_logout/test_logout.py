from Hospitalrun.Pages.HomePage import HomePage
from selenium import webdriver


home = HomePage(webdriver)

home.setup()
home.load_cookies()

home.click_setting()

home.click_logout()

home.logout_check()

home.teardown()
print("LogOut Test Completed")