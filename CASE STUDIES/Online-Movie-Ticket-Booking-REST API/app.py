from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
movies = []
bookings = []

# ------------------ MOVIES APIs ------------------

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200


@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    for movie in movies:
        if movie['id'] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()

    if not data or 'id' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    for movie in movies:
        if movie['id'] == data['id']:
            return jsonify({"error": "Duplicate movie ID"}), 400

    movies.append(data)
    return jsonify({"message": "Movie added successfully"}), 201


@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()

    for movie in movies:
        if movie['id'] == movie_id:
            movie.update(data)
            return jsonify({"message": "Movie updated successfully"}), 200

    return jsonify({"error": "Movie not found"}), 404


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    for movie in movies:
        if movie['id'] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted successfully"}), 200

    return jsonify({"error": "Movie not found"}), 404


# ------------------ BOOKINGS API ------------------

@app.route('/api/bookings', methods=['POST'])
def book_ticket():
    data = request.get_json()

    if not data or 'movie_id' not in data or 'seats' not in data:
        return jsonify({"error": "Invalid booking request"}), 400

    for movie in movies:
        if movie['id'] == data['movie_id']:
            booking = {
                "movie_id": data['movie_id'],
                "seats": data['seats'],
                "total_price": movie['price'] * data['seats']
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Movie not found for booking"}), 404


if __name__ == '__main__':
    app.run(debug=True)
