
def test_create_book(client):
    response = client.post('/books/', {'title': 'Test Book', 'author': 'Author', 'published_date': '2024-01-01', 'stock': 10})
    assert response.status_code == 201
