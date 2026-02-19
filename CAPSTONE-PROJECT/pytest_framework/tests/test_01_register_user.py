from pytest_framework.pages.login_page import LoginPage
from pytest_framework.utils import Utils

def test_user_registration(driver, registered_user):
    login_page = LoginPage(driver)

    login_page.register_user(registered_user)

    assert "Your Account Has Been Created!" in driver.page_source

    Utils.save_user_to_csv(registered_user)
