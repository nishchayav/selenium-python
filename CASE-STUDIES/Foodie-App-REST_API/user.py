from flask import Blueprint, request, jsonify
import uuid

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/v1")

users = {}
ratings = {}

# 13. User Registration
@user_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.json

    if any(u["email"] == data["email"] for u in users.values()):
        return jsonify({"error": "User already exists"}), 409

    user_id = str(uuid.uuid4())
    data["id"] = user_id
    users[user_id] = data

    return jsonify(data), 201


# 16. Give Rating
@user_bp.route("/ratings", methods=["POST"])
def give_rating():
    data = request.json

    required_fields = ["order_id", "rating", "comment"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    rating_id = str(uuid.uuid4())
    data["id"] = rating_id
    ratings[rating_id] = data

    return jsonify(data), 201
