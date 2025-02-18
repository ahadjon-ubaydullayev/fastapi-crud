# FastAPI CRUD Application

This is a **FastAPI CRUD** application that performs basic Create, Read, Update, and Delete (CRUD) operations using PostgreSQL as the database and SQLAlchemy for ORM.

## Features
- FastAPI as the web framework
- PostgreSQL as the database
- SQLAlchemy for database interactions
- Pydantic for data validation
- Automatic API documentation with Swagger and Redoc

## Requirements
Make sure you have the following installed:

- Python 3.8+
- PostgreSQL
- Git

## Installation

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-directory>
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and add the following:
```env
DATABASE_URL=postgresql://postgres:<your-password>@localhost:5434/fastapicrud
```

Update `<your-password>` with your actual PostgreSQL password.

### 5. Apply Database Migrations
```sh
alembic upgrade head
```

## Running the Application

Start the FastAPI application with:
```sh
uvicorn main:app --reload
```

The application will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

| Method  | Endpoint         | Description          |
|---------|-----------------|----------------------|
| **POST** | `/items/`       | Create a new item   |
| **GET**  | `/items/`       | Get all items       |
| **GET**  | `/items/{id}`   | Get a single item   |
| **PUT**  | `/items/{id}`   | Update an item      |
| **DELETE** | `/items/{id}` | Delete an item      |

## Automatic API Documentation
Once the application is running, you can access interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



