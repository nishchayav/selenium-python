def test_booking_failure(client):
    response = client.post('/api/bookings', json={
        "movie_id": 999,
        "seats": 2
    })
    assert response.status_code == 404
