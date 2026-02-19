from pytest_framework.pages.login_page import LoginPage
import random

def test_login(driver, registered_user):
    login_page = LoginPage(driver)

    login_page.login_user(
        registered_user["email"],
        registered_user["password"]
    )

    assert "My Account" in driver.page_source
