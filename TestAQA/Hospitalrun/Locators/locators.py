class Locators(object):

    # Drivers
    Chrome_executable_path = "E:/AQA/AQA/TestAQA/drivers/chromedriver.exe"
    Firefox_executable_path = "E:/AQA/AQA/TestAQA/drivers/genkodriver.exe"

    # URI

    test_site = "http://demo.hospitalrun.io/"

    # Credentials

    test_username_true = "hr.doctor@hospitalrun.io"
    test_password_true = "HRt3st12"

    test_username_false = "test"
    test_password_false = "123"

    # Login page objects

    username_textbox_id = "identification"
    password_textbox_id = "password"
    login_button_css_selector = "button.btn-block"
    alert_message_css_selector = "div.form-signin-alert"
    alert_message_correct_login = "h1.view-current-title"
    logout_check_text = "h2.form-signin-heading"

    # Site pages objects

    setting_css_selector = "span.octicon-gear"
    logout_link_text = "Logout"
    medication_button_id = "ember767"

    medication_request_button_link_text = "Requests"
    medication_completed_button_link_text = "Completed"
    medication_new_request_button_link_text = "New Request"
    medication_return_button_link_text = "Return Medication"

    patient_field_css = "id.patientTypeAhead-ember1016"
    patient_test_name = "Test Parient"