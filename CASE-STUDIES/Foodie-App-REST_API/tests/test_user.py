import requests

def test_user_registration(base_url):
    response = requests.post(
        f"{base_url}/users/register",
        json={
            "name": "New User",
            "email": "newuser@mail.com",
            "password": "123456"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_duplicate_user_registration(base_url):
    data = {
        "name": "Duplicate User",
        "email": "duplicate@mail.com",
        "password": "123456"
    }

    requests.post(f"{base_url}/users/register", json=data)
    response = requests.post(f"{base_url}/users/register", json=data)

    assert response.status_code == 409
