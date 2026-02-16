import requests

def test_register_restaurant(base_url):
    response = requests.post(
        f"{base_url}/restaurants",
        json={
            "name": "Food Hub",
            "category": "Veg",
            "location": "Indore",
            "images": ["img.jpg"],
            "contact": "9999999999"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_register_duplicate_restaurant(base_url):
    data = {
        "name": "Duplicate Restaurant",
        "category": "Veg",
        "location": "Bhopal",
        "images": ["img.jpg"],
        "contact": "8888888888"
    }

    requests.post(f"{base_url}/restaurants", json=data)
    response = requests.post(f"{base_url}/restaurants", json=data)

    assert response.status_code == 409


def test_view_restaurant(base_url, create_restaurant):
    response = requests.get(f"{base_url}/restaurants/{create_restaurant}")
    assert response.status_code == 200


def test_update_restaurant(base_url, create_restaurant):
    response = requests.put(
        f"{base_url}/restaurants/{create_restaurant}",
        json={"location": "Updated City"}
    )
    assert response.status_code == 200
    assert response.json()["location"] == "Updated City"


def test_disable_restaurant(base_url, create_restaurant):
    response = requests.put(
        f"{base_url}/restaurants/{create_restaurant}/disable"
    )
    assert response.status_code == 200
