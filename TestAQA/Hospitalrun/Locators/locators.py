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

    # New Medication Request
    patient_field_id = "patientTypeAhead-ember2300" # True
    patient_test_name = "Test Patient" # True
    patient_choose_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/div/div/div[6]/strong"
    visit_id = "visit-ember2345"
    medication_text_field = "inventoryItemTypeAhead-ember2367"
    medication_choose_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/form/div[2]/div/span/div/div/div[2]/strong"
    medication_test_text = "Pramoxine"
    prescription_field_id = "prescription-ember2399"
    prescription_test_text = "Testing prescription"
    data = "display_prescriptionDate-ember2422"
    quantity_field_id = "quantity-ember2441"
    refills_field_id = "refills-ember2448"
    add_button_xpath = "/html/body/div[1]/div/div[2]/div/div/div[2]/button[2]"
    ok_button = "/html/body/div[1]/div[2]/div/div/div/div[3]/button"
    page_check_xpath = "/html/body/div[1]/div/div[1]/div[1]/h1"