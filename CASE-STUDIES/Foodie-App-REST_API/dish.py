from flask import Blueprint, request, jsonify
import uuid

dish_bp = Blueprint("dish_bp", __name__, url_prefix="/api/v1")
dish_id= 1
dishes = {}

# 5. Add Dish
@dish_bp.route("/restaurants/<restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    global dish_id
    data = request.json

    required_fields = ["name", "price", "available_time"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    data["id"] = dish_id
    data["restaurant_id"] = restaurant_id
    data["enabled"] = True

    dishes[dish_id] = data
    dish_id += 1
    return jsonify(data), 201


# 6. Update Dish
@dish_bp.route("/dishes/<dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish_id = int(dish_id)
    if dish_id not in dishes:
        return jsonify({"error": "Not found"}), 404

    dishes[dish_id].update(request.json)
    return jsonify(dishes[dish_id]), 200


# 7. Enable / Disable Dish
@dish_bp.route("/dishes/<dish_id>/status", methods=["PUT"])
def update_dish_status(dish_id):
    dish_id = int(dish_id)
    if dish_id not in dishes:
        return jsonify({"error": "Not found"}), 404

    enabled = request.json.get("enabled")
    dishes[dish_id]["enabled"] = enabled

    return jsonify({"message": "Dish status updated"}), 200


# 8. Delete Dish
@dish_bp.route("/dishes/<dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    dish_id = int(dish_id)
    if dish_id not in dishes:
        return jsonify({"error": "Not found"}), 404

    del dishes[dish_id]
    return jsonify({"message": "Dish deleted"}), 200
