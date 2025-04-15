from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# # Modèle Pydantic pour la création d'un livre
class BookCreate(BaseModel):
    title: str
    author: str
    published_date: date
    isbn_number: str
    pages: int
    language: str
    isborrowed: bool = False

# # Modèle Pydantic pour la réponse de l'API (inclut l'ID du livre)
class BookOut(BaseModel):
    id: int
    title: str
    author: str
    published_date: date
    isbn_number: str
    pages: int
    language: str
    isborrowed: bool
    model_config = ConfigDict(from_attributes=True)

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_date: Optional[date] = None
    isbn_number: Optional[str] = None
    pages: Optional[int] = None
    language: Optional[str] = None
    isborrowed: Optional[bool] = None