from Pages.HomePage import HomePage


def test_logout(setup):

    home = HomePage(setup)

    home.enter_username_true()
    home.enter_password_true()
    home.click_login()
    home.click_setting()
    home.click_logout()
    home.logout_check()
