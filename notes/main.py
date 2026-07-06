from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [ { "id": 1, "title": "The Guide", "author": "R K Narayan", "genre": "Fiction","language": "English" }, { "id": 2, "title": "Wings of Fire", "author": "A P J Abdul Kalam", "genre": "Biography", "language": "English" } ]


@app.get('/')
def home():
    return {"message": "Library API is running"}

@app.get('/books')
def get_books():
    return books

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str

@app.post('/books', status_code = 201)
def create_book(book1: BookCreate):
    max_id = max(book['id'] for book in books) if books else 0
    new_id = max_id + 1
    new_book = {
        "id": new_id,
        "title": book1.title,
        "author": book1.author,
        "genre": book1.genre,
        "language": book1.language
    }
    books.append(new_book)
    return {
        "message": "Book created successfully",
        "book": new_book
    }


