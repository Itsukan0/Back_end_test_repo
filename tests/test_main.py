import pytest

from fastapi.testclient import TestClient

@pytest.mark.django_db
def test_read_main(client: TestClient, transactional_db):
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de la bibliothèque"}
