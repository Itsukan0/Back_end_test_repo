import pytest
from django.conf import settings
import os

@pytest.fixture(scope="session", autouse=True)
def django_db_setup():
    """Configure Django pour utiliser SQLite en mémoire pendant les tests."""

    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Utilise SQLite en mémoire
        # "TIME_ZONE": None,
        # "CONN_HEALTH_CHECKS": False,
        # "CONN_MAX_AGE": 0,
        # 'OPTIONS': {},
        # "AUTOCOMMIT": True,
    }