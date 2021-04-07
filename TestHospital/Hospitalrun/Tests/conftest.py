from Hospitalrun.Pages.BasePage import test_site
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(test_site)
    print("Setup is Done")
    yield
    driver.close()
    driver.quit()
    print("Teardown is done")



