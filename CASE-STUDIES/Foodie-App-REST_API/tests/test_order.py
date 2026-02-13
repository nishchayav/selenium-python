import requests

def test_place_order(base_url, create_user, create_restaurant):
    response = requests.post(
        f"{base_url}/orders",
        json={
            "user_id": create_user,
            "restaurant_id": create_restaurant,
            "dishes": ["dish1"]
        }
    )
    assert response.status_code == 201
    assert response.json()["status"] == "Placed"


def test_view_orders_by_user(base_url, create_user):
    response = requests.get(
        f"{base_url}/users/{create_user}/orders"
    )
    assert response.status_code == 200
