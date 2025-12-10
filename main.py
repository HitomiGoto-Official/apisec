from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

book = [
    {"id":1, "title":"Mehdi", "author":"Mehdi Orang", "pages":123},
    {"id":2, "title":"Nene", "author":"Hitomi Goto", "pages":321},
    {"id":3, "title":"Hoho", "author":"Hitomi Goto", "pages":321},
    {"id":4, "title":"Merry Chrismas", "author":"Hitomi Goto", "pages":321}
]

class Book(BaseModel):
    title:str
    author:str
    pages:int


@app.get("/books")
def get_books(limit: int | None = None):
    """Get all books, optionally limited by count."""
    if limit:
        return{"books":book[:limit]}
    return{"books":book}

@app.get("/books/{book_id}")
def get_book(book_id:int):
    """Get a specific book by ID."""
    for b in book:
        if b["id"] == book_id:
            return b  
    return{"message":"Book Not found"}

@app.post("/books")
def add_book(newBook: Book):
    """Create a new book entry."""
    new_book = {
        "id":len(book) + 1,
        "title":newBook.title,
        "author":newBook.author,
        "pages":newBook.pages
    }
    book.append(new_book)

@app.delete("/books/{book_id}")
def del_book(book_id: int):
    """Delete a specific book by ID."""
    for delb in book:
        if delb["id"] == book_id:
            book.pop(delb)
            return{"books":book}
    return{"message":"Book Not Found"}