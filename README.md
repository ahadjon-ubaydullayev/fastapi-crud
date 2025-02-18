# FastAPI CRUD Application

## Overview
This project is a FastAPI-based CRUD application that manages doctors and patients. It provides RESTful endpoints for creating, retrieving, updating, and deleting records for both entities.

## Features
- Create, Read, Update, and Delete (CRUD) operations for doctors and patients.
- Search functionality for both doctors and patients.
- Uses PostgreSQL as the database.
- Implements SQLAlchemy for database interactions.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- PostgreSQL
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   Update the `DATABASE_URL` in your `.env` file:
   ```env
   DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
   ```

5. **Apply migrations**
   ```bash
   alembic upgrade head
   ```

6. **Run the FastAPI application**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Doctors
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/doctors/` | Create a new doctor |
| GET    | `/doctors/` | Get all doctors |
| GET    | `/doctors/{doctor_id}` | Get a doctor by ID |
| PUT    | `/doctors/{doctor_id}` | Update a doctor by ID |
| DELETE | `/doctors/{doctor_id}` | Delete a doctor by ID |

### Patients
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/patients/` | Create a new patient |
| GET    | `/patients/` | Get all patients |
| GET    | `/patients/{patient_id}` | Get a patient by ID |
| PUT    | `/patients/{patient_id}` | Update a patient by ID |
| DELETE | `/patients/{patient_id}` | Delete a patient by ID |

### Search
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/search-doctors/search` | Search for doctors |
| GET    | `/search-patients/search` | Search for patients |


## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

