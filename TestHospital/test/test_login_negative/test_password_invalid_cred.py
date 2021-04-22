from Pages.LoginPage import LoginPage


def test_pass_invalid(setup):

    login = LoginPage(setup)

    login.enter_username_true()
    login.enter_password_false()
    login.click_login()
    login.invalid_message_check()

    print("Correct Login Test Completed")
