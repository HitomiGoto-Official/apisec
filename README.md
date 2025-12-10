# 📚 FastAPI Book API

This is a simple **FastAPI CRUD API** for managing a list of books. It includes endpoints for:

- Getting all books
- Getting a book by ID
- Adding a new book
- Deleting a book

Perfect for beginners learning FastAPI.

---

## 🚀 Features

- **GET /books** – Get all books (optional `limit` parameter)
- **GET /books/{id}** – Get one specific book
- **POST /books** – Add a new book
- **DELETE /books/{id}** – Delete a book by ID

---

## 📁 Project Structure

```
project/
│── main.py        # FastAPI application
│── README.md      # Documentation
```

---

## 🛠️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn (server)
- Pydantic (included with FastAPI)

Install required packages:

```bash
pip install fastapi uvicorn
```

---

# ▶️ How to Run the FastAPI Server

1. Make sure you're inside the same folder as `main.py`.

2. Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Meaning of the command:

- **main** → your Python file (`main.py`)
- **app** → your FastAPI instance (`app = FastAPI()`)
- **--reload** → auto-restart when code changes

3. After the server starts, open the browser:

### 👉 API Base URL
**http://127.0.0.1:8000**

### 👉 Swagger UI Docs
**http://127.0.0.1:8000/docs**

### 👉 ReDoc UI
**http://127.0.0.1:8000/redoc**

---

## 🔗 API Endpoints

### ✔️ GET /books
Get all books:
```
GET http://127.0.0.1:8000/books
```
Optional limit:
```
GET /books?limit=2
```

---

### ✔️ GET /books/{book_id}
Example:
```
GET /books/1
```
Response:
```json
{
  "id": 1,
  "title": "Mehdi",
  "author": "Mehdi Orang",
  "pages": 123
}
```

---

### ✔️ POST /books
Add a new book.

Request body:
```json
{
  "title": "New Book",
  "author": "Hitomi",
  "pages": 200
}
```

---

### ✔️ DELETE /books/{book_id}
Delete a book by ID:
```
DELETE /books/3
```

---

## ⚠️ Known Issues (Fix Needed)
Your delete function currently has two bugs:

❌ `if delb[id] == book_id:` → invalid
✔️ Should be:
```python
if delb["id"] == book_id:
```

❌ `pop(delb)` is incorrect
✔️ Should pop by list index.

If you'd like, I can rewrite this function for you.

---

## 📌 Final Notes
This project is great for learning:

- FastAPI basics
- Query & path parameters
- Pydantic validation
- Simple CRUD operations

I can also help you:
- Fix the delete function
- Add Postman collection
- Add Swagger examples
- Add a database (SQLite + SQLAlchemy)
- Improve project folder structure

Just let me know!