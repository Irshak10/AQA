from Pages.LoginPage import LoginPage


def test_invalid_login(setup):

    login = LoginPage(setup)

    login.enter_username_false()
    login.enter_password_true()
    login.click_login()
    login.invalid_message_check()

    print("Correct Login Test Completed")
