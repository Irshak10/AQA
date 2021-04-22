# import pickle


# Locators:
# URI
test_site = "http://demo.hospitalrun.io/"


class BasePage(object):

    driver = None

    def __init__(self, driver):
        self.driver = driver

    # def save_cookies(self):
    #     pickle.dump(self.driver.get_cookies(), open("correct_cookies", "wb"))
    #     print('The cookies are saved')
    #
    # def load_cookies(self):
    #     for cookie in pickle.load(open("correct_cookies", "rb")):
    #         self.driver.add_cookie(cookie)
    #     self.driver.refresh()
    #     print("The cookies are loaded")


