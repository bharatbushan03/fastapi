from fastapi import APIRouter, HTTPException, status
from data.book_data import books
from typing import Optional
from models.book_models import (
    BookResponse,
    BookCreate,
    BookActionResponse,
    BookPatch,
    BookPut
)

router = APIRouter(prefix='/books', tags=['Books'])

@router.get('', response_model=list[BookResponse], status_code = status.HTTP_200_OK)
def get_books(genre: Optional[str] = None, language: Optional[str] = None):
    filtered_books = books.copy()
    if genre:
        filtered_books = [book for book in filtered_books if book['genre'].lower() == genre.lower()]
    if language:
        filtered_books = [book for book in filtered_books if book['language'].lower() == language.lower()]
    
    return filtered_books
@router.get('/{book_id}', response_model = BookResponse, status_code = status.HTTP_200_OK)
def get_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Book not found')

@router.post('', response_model = BookActionResponse, status_code = status.HTTP_201_CREATED)
def create_book(Book: BookCreate):
    new_id = max((book['id'] for book in books), default = 0) + 1
    new_book = {
        "id": new_id,
        'title': Book.title,
        'author': Book.author,
        'genre': Book.genre,
        'language': Book.language
    }
    books.append(new_book)
    return {
        "message": "book added successfully",
        "book": new_book
    }

@router.put('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_201_CREATED)
def update_book(book_id: int, Book: BookPut):
    for book in books:
        if book['id'] == book_id:
            book['title'] = Book.title
            book['author'] = Book.author
            book['genre'] = Book.genre
            book['language'] = Book.language

            return {
                "message": "Book updated successfully",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')

@router.patch('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_201_CREATED)
def patch_book(book_id: int, Book: BookPatch):
    for book in books:
        if book['id'] == book_id:
            if Book.title:
                book['title'] = Book.title
            if Book.author:
                book['author'] = Book.author
            if Book.genre:
                book['genre'] = Book.genre
            if Book.language:
                book['language'] = Book.language

            return {
                "message": "Book updated successfully",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')

@router.delete('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {
                "message": "successfully deleted book",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')
