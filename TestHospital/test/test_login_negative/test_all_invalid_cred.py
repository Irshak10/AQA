from Pages.LoginPage import LoginPage


def test_all_invalid_cred(setup):

    login = LoginPage(setup)
    login.enter_username_false()
    login.enter_password_false()
    login.click_login()
    login.invalid_message_check()

    print("Correct Login Test Completed")
