from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [ {"id": 1, "title": "The Guide", "author": "R K Narayan", "genre": "Fiction", "language": "English", "available": True}, {"id": 2, "title": "Wings of Fire", "author": "A P J Abdul Kalam", "genre": "Biography", "language": "English", "avail able": True}, {"id": 3, "title": "Python Basics", "author": "Code Team", "genre": "Technology", "language": "English", "availabl e": False}, {"id": 4, "title": "Telugu Stories", "author": "Local Author", "genre": "Fiction", "language": "Telugu", "available": True}, {"id": 5, "title": "Indian History", "author": "History Team", "genre": "History", "language": "English", "available": False}, {"id": 6, "title": "Science Facts", "author": "Science Te am", "genre": "Science", "language": "Hindi", "available": True} ]


@app.get("/")
def home():
    return {"message": "Library API is running"}

@app.get("/books")
def get_book_by_genre(genre: str | None = None):
    if genre:
        genre_books = []
        for book in books:
            if book["genre"].lower() == genre.lower():
                genre_books.append(book)
        return genre_books
    return books

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail = "Book not found")

@app.get('/books-by-language')
def get_book_by_language(language: str | None = None):
    if language:
        language_books = []
        for book in books:
            if book["language"].lower() == language.lower():
                language_books.append(book)
        return language_books
    return books