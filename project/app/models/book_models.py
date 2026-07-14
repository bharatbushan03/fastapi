from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str
    internal_note: Optional[str] = None
    created_by: Optional[str] = None

class BookPut(BaseModel):
    title: str
    author: str
    genre: str
    language: str
    internal_note: Optional[str] = None
    created_by: Optional[str] = None

class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    language: Optional[str] = None
    internal_note: Optional[str] = None
    created_by: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    language: str

class BookActionResponse(BaseModel):
    message: str
    book: BookResponse