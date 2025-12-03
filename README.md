# FASTApi_CRUD_Authentication

A simple backend API built with **FastAPI** that implements:

- User registration & authentication (e.g. JWT or session-based)
- CRUD operations on a protected resource
- Basic security best practices (password hashing, dependency-based auth)

This project is meant as a compact example of how to structure a FastAPI application with both **authentication** and **database-backed CRUD**.

---

## Features

- ⚙️ **FastAPI** application with automatic interactive docs (`/docs`, `/redoc`)
- 👤 **User management**
  - Sign up / register
  - Login with username + password
  - Password hashing (no plain-text passwords in the database)
- 🔑 **Authentication**
  - Issue access tokens on successful login
  - Protect endpoints using a dependency that validates the token
- 📦 **CRUD API**
  - Create / Read / Update / Delete items (e.g. posts, products, todos, etc.)
  - Separation between public and authenticated endpoints
- 🗄️ **Database integration**
  - SQLAlchemy models and schemas (Pydantic) for request/response validation

> If you are reading this repo from my CV: this project is meant to show my understanding of **backend APIs, database modeling and authentication flows** using Python.

---

## Tech stack

- **Python** (3.x)
- **FastAPI**
- **Uvicorn** (ASGI server)
- **SQLAlchemy** or equivalent ORM
- **Pydantic** for data validation
- **Passlib / bcrypt** (or similar) for password hashing
- **JWT** (e.g. `python-jose`) or similar token library for auth

---

```markdown
## Project structure

```text
FastAPI-CRUD/
├─ README.md
├─ requirement.txt
└─ user/
    ├─ __init__.py
    ├─ database.py
    ├─ hashing.py
    ├─ main.py
    ├─ models.py
    ├─ oauth2.py
    ├─ repository/
    │   ├─ products.py
    │   └─ users.py
    ├─ routers/
    │   ├─ __init__.py
    │   ├─ authentication.py
    │   ├─ products.py
    │   └─ users.py
    ├─ schemas.py
    └─ token.py


⸻

Getting started

1. Clone the repository

git clone https://github.com/Hamedius/FASTApi_CRUD_Authentication.git
cd FASTApi_CRUD_Authentication

2. Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

If you don’t have a requirements.txt yet, you can generate one after installing the needed packages:

pip freeze > requirements.txt


⸻

Configuration

Most FastAPI projects use environment variables for secrets (JWT secret key, DB URL).
Typical configuration variables might be:
	•	DATABASE_URL
	•	SECRET_KEY
	•	ALGORITHM (e.g. HS256 for JWT)
	•	ACCESS_TOKEN_EXPIRE_MINUTES

You can set them via your shell, .env file (with python-dotenv), or any other preferred method.

export DATABASE_URL="sqlite:///./test.db"
export SECRET_KEY="change-this-secret-key"
export ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES=30

(Adjust based on how you configured your project.)

⸻

Running the application

Run the FastAPI app with uvicorn:

uvicorn app.main:app --reload

Then open:
	•	Swagger UI: http://127.0.0.1:8000/docs
	•	ReDoc: http://127.0.0.1:8000/redoc

⸻

Authentication flow

A typical workflow for this project:
	1.	Register a user
	•	POST /users/ or POST /auth/register
	•	Send username, email, and password
	•	Password is hashed and stored in the database
	2.	Login
	•	POST /auth/login
	•	Send username & password
	•	On success, receive an access token (e.g. JWT)
	3.	Use protected endpoints
	•	For endpoints that require authentication, send the token in the Authorization header:

Authorization: Bearer <access_token>


	•	The FastAPI dependency validates the token and injects the current user into the route handler.

	4.	CRUD operations
	•	POST /items/ – create new item
	•	GET /items/ – list all items for the current user
	•	GET /items/{id} – get item by id
	•	PUT /items/{id} – update item
	•	DELETE /items/{id} – delete item

(Rename items to posts, products, etc., depending on your project.)

⸻

Example requests (using curl)

Register

curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
      }'

Login

curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpassword"

Response will contain an access_token.

Access a protected route

curl -X GET "http://127.0.0.1:8000/items/" \
  -H "Authorization: Bearer <access_token>"


⸻

Possible improvements
	•	Add refresh tokens and token revocation
	•	Add role-based access control (admin, normal user, etc.)
	•	Add tests using pytest and httpx / TestClient
	•	Dockerize the application for easier deployment
	•	Integrate with a real database in production (PostgreSQL, MySQL, etc.)

⸻

Author

Hamed Nahvi
GitHub: @Hamedius
