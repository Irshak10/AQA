from selenium import webdriver
import time
from Hospitalrun.Pages.LoginPage import LoginPage
from Hospitalrun.Locators.locators import Locators


driver = webdriver.Chrome(executable_path=Locators.Chrome_executable_path)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(Locators.test_site)
login = LoginPage(driver)
login.enter_username(Locators.test_username_true)
login.enter_password(Locators.test_password_true)
login.click_login()
time.sleep(2)

driver.close()
driver.quit()
print("Correct Login Test Completed")

