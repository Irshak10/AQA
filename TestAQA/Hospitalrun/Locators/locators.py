class Locators(object):

    # Drivers
    Chrome_executable_path = "E:/AQA/AQA/TestAQA/drivers/chromedriver.exe"
    Firefox_executable_path = "E:/AQA/AQA/TestAQA/drivers/genkodriver.exe"

    # URI

    test_site = "http://demo.hospitalrun.io/"

    # Credintials

    test_username_true = "hr.doctor@hospitalrun.io"
    test_password_true = "HRt3st12"
    test_username_false = "test"
    test_password_false = "123"

    # Login page objects

    username_textbox_id = "identification"
    password_textbox_id = "password"
    login_button_css_selector = "button.btn-block"

    # Home page objects

    setting_css_selector = "span.octicon-gear"
    logout_link_text = "Logout"