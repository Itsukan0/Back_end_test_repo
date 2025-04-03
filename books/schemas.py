from pydantic import BaseModel
from datetime import date

# Modèle Pydantic pour la création d'un livre
class BookCreate(BaseModel):
    title: str
    author: str
    published_date: date
    isbn_number: str
    pages: int
    language: str
    isborrowed: bool = False

# Modèle Pydantic pour la réponse de l'API (inclut l'ID du livre)
class BookOut(BaseModel):
    id: int
    title: str
    author: str
    published_date: date
    isbn_number: str
    pages: int
    language: str
    isborrowed: bool

    class Config:
        orm_mode = True  # Permet à Pydantic de gérer directement les objets Django ORM
