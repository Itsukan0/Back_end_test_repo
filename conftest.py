import pytest

from django.core.exceptions import ImproperlyConfigured
from django.db import connections
from django.core.management import call_command

from fastapi_app import app
from fastapi.testclient import TestClient

@pytest.fixture(autouse=True, scope="function")
def setup_db():
    connection = connections['default']
    try:
        connection.connect()  # Connexion à la base de données
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)  # Applique les migrations sans demander d'entrée
    except ImproperlyConfigured:
        # Si la configuration est incorrecte (par exemple, problème de base de données)
        raise Exception("Django settings are not properly configured")
    yield
    # Si tu as besoin de faire un nettoyage après chaque test, tu peux le faire ici

@pytest.fixture()
def client():
    """Fixture pour le client de test FastAPI."""
    return TestClient(app)