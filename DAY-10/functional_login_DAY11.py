import pytest

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"

def test_login_success():
    result = login("admin", "admin123")
    assert result == "Login Successful"

def test_login_failure():
    result = login("user", "wrongpass")
    assert result == "Login Failed"
