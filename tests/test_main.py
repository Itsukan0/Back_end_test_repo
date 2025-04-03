from fastapi.testclient import TestClient
from fastapi_app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de la bibliothèque"}
