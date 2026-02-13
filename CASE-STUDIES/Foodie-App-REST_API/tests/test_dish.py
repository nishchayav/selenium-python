import requests

def test_add_dish(base_url, create_restaurant):
    response = requests.post(
        f"{base_url}/restaurants/{create_restaurant}/dishes",
        json={
            "name": "Paneer Butter Masala",
            "type": "Veg",
            "price": 250,
            "available_time": "10AM-10PM",
            "image": "paneer.jpg"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()
