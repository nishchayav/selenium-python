from flask import Blueprint, jsonify

admin_bp = Blueprint("admin_bp", __name__, url_prefix="/api/v1/admin")

from restaurant import restaurants
from order import orders
from user import ratings


# 9. Approve Restaurant
@admin_bp.route("/restaurants/<restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    restaurant_id = int(restaurant_id)
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[restaurant_id]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


# 10. Disable Restaurant (Admin)
@admin_bp.route("/restaurants/<restaurant_id>/disable", methods=["PUT"])
def admin_disable_restaurant(restaurant_id):
    restaurant_id = int(restaurant_id)
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[restaurant_id]["disabled"] = True
    return jsonify({"message": "Restaurant disabled by admin"}), 200


# 11. View Customer Feedback
@admin_bp.route("/feedback", methods=["GET"])
def view_feedback():
    return jsonify(ratings), 200


# 12. View Order Status
@admin_bp.route("/orders", methods=["GET"])
def view_orders():
    return jsonify(list(orders.values())), 200
