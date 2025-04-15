import pytest

from fastapi.testclient import TestClient

from books.models import Book  # Ton modèle Django

book_data_generic = {
    "title": "1984",
    "author": "George Orwell",
    "published_date": "1949-06-08",
    "isbn_number": "9780451524935",
    "pages": 328,
    "language": "EN",
    "isborrowed": False
}

@pytest.fixture(scope="function")
def existing_book():
    return Book.objects.create(**book_data_generic)

@pytest.mark.django_db()
def test_create_book(client: TestClient, transactional_db):
    new_book = {
        "title": "1984",
        "author": "George Orwell",
        "published_date": "1949-06-08",
        "isbn_number": "9780451524935",
        "pages": 328,
        "language": "EN",
        "isborrowed": False
    }
    response = client.post("/api/book/", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == "1984"

@pytest.mark.django_db()
def test_get_books(client: TestClient, transactional_db):
    response = client.get("/api/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.django_db()
def test_get_specific_book(client: TestClient, existing_book: Book, transactional_db):
    response = client.get(f"/api/book/{existing_book.id}")
    assert response.status_code == 200

@pytest.mark.django_db()
def test_patch_book(client: TestClient, existing_book: Book, transactional_db):
    update_data = {"title": "1984 (Updated)"}
    response = client.patch(f"/api/book/{existing_book.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "1984 (Updated)"

@pytest.mark.django_db()
def test_delete_book(client: TestClient, existing_book: Book, transactional_db):
    response = client.delete(f"/api/book/{existing_book.id}")
    assert response.status_code == 204