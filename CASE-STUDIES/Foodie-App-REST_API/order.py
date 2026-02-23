from flask import Blueprint, request, jsonify


order_bp = Blueprint("order_bp", __name__, url_prefix="/api/v1")
order_id = 1
orders = {}

# 15. Place Order
@order_bp.route("/orders", methods=["POST"])
def place_order():
    global order_id
    data = request.json

    required_fields = ["user_id", "restaurant_id", "dish"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    data["id"] = order_id
    data["status"] = "Placed"

    orders[order_id] = data
    order_id += 1
    return jsonify(data), 201


# 17. View Orders by Restaurant
@order_bp.route("/restaurants/<restaurant_id>/orders", methods=["GET"])
def view_orders_by_restaurant(restaurant_id):
    result = [o for o in orders.values() if o["restaurant_id"] == restaurant_id]
    return jsonify(result), 200


# 18. View Orders by User
@order_bp.route("/users/<user_id>/orders", methods=["GET"])
def view_orders_by_user(user_id):
    result = [o for o in orders.values() if o["user_id"] == user_id]
    return jsonify(result), 200
