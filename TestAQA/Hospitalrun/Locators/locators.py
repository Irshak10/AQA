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

    # Site pages objects

    setting_css_selector = "span.octicon-gear"
    logout_link_text = "Logout"
    medication_button_id = "ember767"

    medication_request_button_id = "ember3216"
    medication_completed_button_id = "ember3218"
    medication_new_request_button_id = "ember3220"
    medication_dispense_button_id = "ember3222"
    medication_return_button_id = "ember3224"