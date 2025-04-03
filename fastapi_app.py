import os
import django
from fastapi import FastAPI, APIRouter, HTTPException
from typing import List

# Initialiser Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'name.settings')

django.setup()

from books.models import Book as DjangoBook  # Importer ton modèle Django
from books.schemas import BookCreate, BookOut

# Créer l'instance FastAPI
app = FastAPI()

# Créer un routeur
api_router = APIRouter()

# Définir des routes sur ce routeur
@api_router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de la bibliothèque"}

# Route GET pour récupérer tous les livres
@api_router.get("/books/", response_model=List[BookOut])
def get_books():
    books = DjangoBook.objects.all()
    return books

# Route GET pour récupérer un livre par son ID
@api_router.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    try:
        book = DjangoBook.objects.get(id=book_id)
        return book
    except DjangoBook.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")

# Route POST pour créer un livre
@api_router.post("/books/", response_model=BookOut)
def create_book(book: BookCreate):
    new_book = DjangoBook.objects.create(
        title=book.title,
        author=book.author,
        published_date=book.published_date,
        isbn_number=book.isbn_number,
        pages=book.pages,
        language=book.language,
        isborrowed=book.isborrowed
    )
    return new_book

# Route PUT pour mettre à jour un livre
@api_router.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookCreate):
    try:
        existing_book = DjangoBook.objects.get(id=book_id)
        existing_book.title = book.title
        existing_book.author = book.author
        existing_book.published_date = book.published_date
        existing_book.isbn_number = book.isbn_number
        existing_book.pages = book.pages
        existing_book.language = book.language
        existing_book.isborrowed = book.isborrowed
        existing_book.save()  # Enregistrer les changements
        return existing_book
    except DjangoBook.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")

# Route DELETE pour supprimer un livre
@api_router.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        book = DjangoBook.objects.get(id=book_id)
        book.delete()
        return {"detail": "Book deleted successfully"}
    except DjangoBook.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")


# Ajouter le routeur au serveur FastAPI avec un préfixe "/api"
app.include_router(api_router, prefix="/api")