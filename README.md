# FastAPI-CRUD

A clean and minimal **FastAPI backend** that demonstrates:

- CRUD API development
- Proper project structure with routers, schemas, models, and repository pattern
- Database layer with SQLAlchemy
- Password hashing and authentication (via `oauth2.py`)
- A realistic backend codebase suitable for learning and CV demonstration

This project is useful as a template for building scalable REST APIs with Python and FastAPI.

---

##  Features

- **FastAPI + Pydantic** for fast development and type safety
- **SQLAlchemy ORM** for database modeling
- **Repository pattern** for clean separation of logic
- **Authentication**:
  - Password hashing (`hashing.py`)
  - Token generation (`oauth2.py`)
- **CRUD Endpoints**:
  - Users (create, read, list)
  - Products (create, read, list)
- **Modular architecture** using:
  - `routers/` for route grouping  
  - `repository/` for business logic  
  - `schemas.py` for request/response models  
  - `models.py` for SQLAlchemy models

---

##  Project structure

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
```

This structure follows best practices for a medium-size FastAPI app.

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/Hamedius/FastAPI-CRUD.git
cd FastAPI-CRUD
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirement.txt
```

---

##  Database setup

The project uses **SQLite by default**—no configuration needed.  
To switch to PostgreSQL/MySQL, edit:

`user/database.py`

and update the connection string.

---

##  Running the application

Start the FastAPI app with Uvicorn:

```bash
uvicorn user.main:app --reload
```

Open API documentation:

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

##  Example API workflow

### Create a user  
**POST** `/users/`
```json
{
  "name": "hamed",
  "email": "hamed@example.com",
  "password": "1234"
}
```

### Login  
**POST** `/login`
Returns:
```json
{
  "access_token": "XXXXXXXX",
  "token_type": "bearer"
}
```

### Create product  
**POST** `/product/`

Headers:
```
Authorization: Bearer <token>
```

Body:
```json
{
  "title": "Laptop",
  "description": "Fast machine"
}
```

### Get product list  
**GET** `/product/`

---

##  Code architecture (high-level)

- `main.py` — FastAPI entry point  
- `routers/` — routes for users, products, and auth  
- `repository/` — database operation logic  
- `schemas.py` — Pydantic request/response models  
- `models.py` — SQLAlchemy ORM models  
- `database.py` — DB engine + session  
- `hashing.py` — password hashing utilities  
- `oauth2.py` — authentication & token helpers  



---

##  Author

**Hamed Nahvi**
