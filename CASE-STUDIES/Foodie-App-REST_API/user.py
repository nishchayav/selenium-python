from flask import Blueprint, request, jsonify

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/v1")
user_id = 1
rating_id = 1

users = {}
ratings = {}

# 13. User Registration
@user_bp.route("/users/register", methods=["POST"])
def register_user():
    global user_id
    data = request.json

    if any(u["email"] == data["email"] for u in users.values()):
        return jsonify({"error": "User already exists"}), 409


    data["id"] = user_id
    users[user_id] = data
    user_id += 1

    return jsonify(data), 201


# 16. Give Rating
@user_bp.route("/ratings", methods=["POST"])
def give_rating():
    global rating_id
    data = request.json

    required_fields = ["order_id", "rating", "comment"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    data["id"] = rating_id
    ratings[rating_id] = data
    rating_id += 1

    return jsonify(data), 201
