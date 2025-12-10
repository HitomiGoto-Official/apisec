# apisec
📚 FastAPI Book API
This is a simple FastAPI CRUD API for managing a list of books.
 It includes endpoints for:
Getting all books


Getting a book by ID


Adding a new book


Deleting a book


Perfect for beginners learning FastAPI.

🚀 Features
GET /books – Get all books (optional limit parameter)


GET /books/{id} – Get one specific book


POST /books – Add a new book


DELETE /books/{id} – Delete a book by ID



📁 Project Structure
project/
│── main.py        # FastAPI application
│── README.md      # Documentation


🛠️ Requirements
Python 3.10+


FastAPI


Uvicorn (server)


Pydantic (included with FastAPI)


Install required packages:
pip install fastapi uvicorn


▶️ How to Run the FastAPI Server
Make sure you're inside the same folder as main.py.


Start the FastAPI development server:


Developer mode: fastapi dev main.py
Production mode: fastapi run main.py
Meaning of the command:
fastapi  → instance name
dev  → mode
main.py → your Python file (main.py)
Option:
- - port  → port number
- - host  → host domain 



After the server starts, open the browser:


👉 API Base URL
http://127.0.0.1:8000

🔗 API Endpoints
✔️ GET /books
Get all books.
GET http://127.0.0.1:8000/books
Optional limit:
GET /books?limit=2

✔️ GET /books/{book_id}
Example:
GET /books/1

Response:
{
  "id": 1,
  "title": "Mehdi",
  "author": "Mehdi Orang",
  "pages": 123
}


✔️ POST /books
Add a new book.
Request body:
{
  "title": "New Book",
  "author": "Hitomi",
  "pages": 200
}


✔️ DELETE /books/{book_id}
Delete a book by ID:
DELETE /books/3


⚠️ Known Issues (Fix Needed)
Your delete function has two bugs:
❌ if delb[id] == book_id: → wrong
 ✔️ Should be:
if delb["id"] == book_id:

❌ pop(delb) is incorrect
 ✔️ Needs to pop by index.
If you want, I can rewrite the function correctly.

📌 Final Notes
This project is great for learning:
FastAPI basics


Query parameters & path parameters


Pydantic request validation


Simple CRUD operations


If you'd like, I can help you:
fix the delete function


add Swagger examples


add a database (SQLite + SQLAlchemy)


organize the project into folders


Just let me know!

