import pytest
from fastapi.testclient import TestClient
from fastapi_app import app

client = TestClient(app)

@pytest.mark.django_db
def test_create_book():
    new_book = {
        "title": "1984",
        "author": "George Orwell",
        "published_date": "1949-06-08",
        "isbn_number": "9780451524935",
        "pages": 328,
        "language": "EN",
        "isborrowed": False
    }
    response = client.post("/api/books/", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == "1984"

@pytest.mark.django_db
def test_get_books():
    response = client.get("/api/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.django_db
def test_update_book():
    update_data = {"title": "1984 (Updated)"}
    response = client.patch("/api/books/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "1984 (Updated)"

@pytest.mark.django_db
def test_delete_book():
    response = client.delete("/api/books/1")
    assert response.status_code == 204
