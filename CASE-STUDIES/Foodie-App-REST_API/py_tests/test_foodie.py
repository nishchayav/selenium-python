import requests

BASE = "http://127.0.0.1:5000"


# -------------------------------
# Restaurant Module Tests
# -------------------------------

def test_01_register_restaurant():
    res = requests.post(f"{BASE}/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Veg",
        "location": "Hyderabad",
        "contact": "9999999999"
    })
    assert res.status_code == 201


def test_02_update_restaurant():
    res = requests.put(f"{BASE}/api/v1/restaurants/1", json={
        "location": "Bangalore"
    })
    assert res.status_code == 200


def test_03_disable_restaurant():
    res = requests.put(f"{BASE}/api/v1/restaurants/1/disable")
    assert res.status_code == 200


def test_04_view_restaurant_profile():
    res = requests.get(f"{BASE}/api/v1/restaurants/1")
    assert res.status_code == 200


# -------------------------------
# Dish Module Tests
# -------------------------------

def test_05_add_dish():
    res = requests.post(f"{BASE}/api/v1/restaurants/1/dishes", json={
        "name": "Paneer Biryani",
        "price": 250,
        "available_time": "Lunch"
    })
    assert res.status_code == 201


def test_06_update_dish():
    res = requests.put(f"{BASE}/api/v1/dishes/1", json={
        "price": 300
    })
    assert res.status_code == 200


def test_07_enable_disable_dish():
    res = requests.put(f"{BASE}/api/v1/dishes/1/status", json={
        "enabled": False
    })
    assert res.status_code == 200


def test_08_delete_dish():
    res = requests.delete(f"{BASE}/api/v1/dishes/1")
    assert res.status_code == 200


# -------------------------------
# Admin Module Tests
# -------------------------------

def test_09_approve_restaurant():
    res = requests.put(f"{BASE}/api/v1/admin/restaurants/1/approve")
    assert res.status_code == 200


def test_10_admin_disable_restaurant():
    res = requests.put(f"{BASE}/api/v1/admin/restaurants/1/disable")
    assert res.status_code == 200


def test_11_view_feedback():
    res = requests.get(f"{BASE}/api/v1/admin/feedback")
    assert res.status_code == 200


def test_12_view_orders_status():
    res = requests.get(f"{BASE}/api/v1/admin/orders")
    assert res.status_code == 200


# -------------------------------
# User/Customer Module Tests
# -------------------------------

def test_13_user_registration():
    res = requests.post(f"{BASE}/api/v1/users/register", json={
        "name": "Abhi",
        "email": "abhi@gmail.com",
        "password": "1234"
    })
    assert res.status_code == 201


def test_14_search_restaurants():
    res = requests.get(f"{BASE}/api/v1/restaurants/search?name=Food")
    assert res.status_code == 200


def test_15_place_order():
    res = requests.post(f"{BASE}/api/v1/orders", json={
        "user_id": 1,
        "restaurant_id": 1,
        "dish": "Paneer Biryani"
    })
    assert res.status_code == 201


def test_16_give_rating():
    res = requests.post(f"{BASE}/api/v1/ratings", json={
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent Taste!"
    })
    assert res.status_code == 201


# -------------------------------
# Order Module Tests
# -------------------------------

def test_17_view_orders_by_restaurant():
    res = requests.get(f"{BASE}/api/v1/restaurants/1/orders")
    assert res.status_code == 200


def test_18_view_orders_by_user():
    res = requests.get(f"{BASE}/api/v1/users/1/orders")
    assert res.status_code == 200