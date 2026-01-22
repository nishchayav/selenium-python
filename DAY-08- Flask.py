from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Nish"},
    {"id": 2, "name": "Vish"}
]


@app.route('/', methods=['GET'])
def home():
    return "Welcome"


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET user by id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404


# POST new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user), 201


# PUT → full update
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404


# PATCH → partial update
@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404


# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "user deleted"}), 200
    return jsonify({"message": "user not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
