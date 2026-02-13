def test_add_movie(client):
    response = client.post('/api/movies', json={
        "id": 101,
        "movie_name": "Jhon Banega Don",
        "language": "Hindi",
        "duration": "2h 49m",
        "price": 250
    })
    assert response.status_code == 201


def test_get_movies(client):
    response = client.get('/api/movies')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_movie_by_id(client):
    response = client.get('/api/movies/101')
    assert response.status_code == 200
    assert response.json['movie_name'] == "Jhon Banega Don"


def test_update_movie(client):
    response = client.put('/api/movies/101', json={"price": 300})
    assert response.status_code == 200


def test_delete_movie(client):
    response = client.delete('/api/movies/105')
    assert response.status_code == 200
