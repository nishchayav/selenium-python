from pytest_framework.pages.logout_page import LogoutPage
from pytest_framework.pages.login_page import LoginPage

def test_logout_and_session_validation(driver, registered_user):
    login = LoginPage(driver)

    login.login_user(
        registered_user["email"],
        registered_user["password"]
    )

    logout = LogoutPage(driver)
    logout.logout()

    assert logout.is_logout_successful()
