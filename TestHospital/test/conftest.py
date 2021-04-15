import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import test
from Pages.BasePage import test_site


@pytest.fixture
def setup():
    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(test_site)
    print("Setup is Done")
    yield
    driver.close()
    driver.quit()


# @pytest.fixture
# def teardown(request):
#     driver.close()
#     driver.quit()
#     request.cls.driver = driver
#     print("Teardown is done")


# @pytest.fixture
# def setup(request):
#     driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get(test_site)
#     request.cls.driver = driver
#     yield
#     driver.close()
#     driver.quit()
