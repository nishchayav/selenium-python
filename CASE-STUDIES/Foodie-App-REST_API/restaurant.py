from flask import Blueprint, request, jsonify
import uuid

restaurant_bp = Blueprint("restaurant_bp", __name__, url_prefix="/api/v1")

restaurants = {}

# 1. Register Restaurant
@restaurant_bp.route("/restaurants", methods=["POST"])
def register_restaurant():
    data = request.json

    required_fields = ["name", "category", "location", "images", "contact"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Check duplicate name
    for r in restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant already exists"}), 409

    restaurant_id = str(uuid.uuid4())
    data["id"] = restaurant_id
    data["approved"] = False
    data["disabled"] = False

    restaurants[restaurant_id] = data
    return jsonify(data), 201


# 2. Update Restaurant Details
@restaurant_bp.route("/restaurants/<restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[restaurant_id].update(request.json)
    return jsonify(restaurants[restaurant_id]), 200


# 3. Disable Restaurant
@restaurant_bp.route("/restaurants/<restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[restaurant_id]["disabled"] = True
    return jsonify({"message": "Restaurant disabled"}), 200


# 4. View Restaurant Profile
@restaurant_bp.route("/restaurants/<restaurant_id>", methods=["GET"])
def view_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404

    return jsonify(restaurants[restaurant_id]), 200


# 14. Search Restaurants
@restaurant_bp.route("/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name")
    location = request.args.get("location")

    results = []

    for r in restaurants.values():
        if name and name.lower() not in r["name"].lower():
            continue
        if location and location.lower() not in r["location"].lower():
            continue
        results.append(r)

    return jsonify(results), 200
