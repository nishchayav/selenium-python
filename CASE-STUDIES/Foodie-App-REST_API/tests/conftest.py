import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def create_restaurant(base_url):
    response = requests.post(
        f"{base_url}/restaurants",
        json={
            "name": "Test Restaurant",
            "category": "Veg",
            "location": "Bhopal",
            "images": ["img1.jpg"],
            "contact": "9876543210"
        }
    )
    assert response.status_code == 201
    return response.json()["id"]


@pytest.fixture(scope="session")
def create_user(base_url):
    response = requests.post(
        f"{base_url}/users/register",
        json={
            "name": "Test User",
            "email": "testuser@mail.com",
            "password": "123456"
        }
    )
    assert response.status_code == 201
    return response.json()["id"]
