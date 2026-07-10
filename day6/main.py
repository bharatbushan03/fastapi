from fastapi import FastAPI , HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English",
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }
]

@app.get('/')
def home():
    return {"message": "Welcome to Book API"}

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    language: str

@app.get('/books', response_model = list[BookResponse])
def get_books():
    return books

@app.get('/books/{book_id}', response_model = BookResponse)
def get_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'book not found')

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str

class BookActionResponse(BaseModel):
    message: str
    book: BookResponse

@app.post('/books', response_model = BookActionResponse, status_code = status.HTTP_201_CREATED)
def create_book(book: BookCreate):

    for existing_book in books:
        if existing_book['title'].lower() == book.title.lower():
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = 'book already exists')

    new_id = max((curr_book['id'] for curr_book in books), default = 0) + 1
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "language": book.language,
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }

    books.append(new_book)

    return {
        "message": "book created successfully",
        "book": new_book
    }

@app.delete('/books/{book_id}', response_model = BookActionResponse)
def delete_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {
                "message": "book deleted successfully",
                "book": book
            }
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'book not found')

class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    language: str

@app.put('/books/{book_id}', response_model = BookActionResponse, status_code = status.HTTP_201_CREATED)
def put_book(book_id: int, book: BookUpdate):
    for existing_book in books:
        if existing_book['id'] == book_id:
            existing_book.update(book.model_dump())
            return {
                "message": "book updated successfully",
                "book": existing_book
            }

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'book not found')

class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    language: Optional[str] = None

@app.patch('/books/{book_id}', response_model = BookActionResponse, status_code = status.HTTP_201_CREATED)
def patch_book(book_id: int, book: BookPatch):
    for existing_book in books:
        if existing_book['id'] == book_id:
            if book.title:
                existing_book['title'] = book.title
            if book.author:
                existing_book['author'] = book.author
            if book.genre:
                existing_book['genre'] = book.genre
            if book.language:
                existing_book['language'] = book.language

            return {
                "message": "book patch updated successfully",
                "book": existing_book
            }

    raise HTTPException(status_code = status.HTTP_201_CREATED, detail = "book not found")