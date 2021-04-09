from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Hospitalrun.Pages.BasePage import test_site


def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(test_site)
    print("Setup is Done")


def teardown():
    webdriver.Chrome.quit(ChromeDriverManager)
    print("Teardown is done")