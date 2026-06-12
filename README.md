# College-management-system

# College Management System

A backend-based College Management System developed using **Python**, **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Pydantic**. The system is designed to manage students, faculty, courses, attendance, examinations, grades, and other academic operations efficiently.

## Features

* Student Management
* Faculty Management
* Course Management
* Attendance Management
* Examination Management
* Grades Management
* Authentication & Authorization
* RESTful API Architecture
* Database Relationship Management
* CRUD Operations

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Git & GitHub

## Database Relationships

* One-to-One Relationship
* One-to-Many Relationship
* Many-to-Many Relationship
* Foreign Keys
* SQLAlchemy `relationship()`
* `back_populates`

## Project Structure

```text
app/
├── models/
├── schemas/
├── routers/
├── services/
├── database/
└── main.py
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd College-management-system
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Configure PostgreSQL database settings.

7. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, access:

* Swagger UI: `/docs`
* ReDoc: `/redoc`

## Learning Outcomes

This project helped in understanding:

* FastAPI Application Development
* REST API Design
* PostgreSQL Database Management
* SQLAlchemy ORM
* Pydantic Data Validation
* Database Relationships
* Authentication & Authorization
* Backend System Design

## Future Enhancements

* Role-Based Access Control (RBAC)
* Notifications and Alerts
* Timetable Management
* Student Performance Analytics
* Microservices Architecture
* Docker Deployment

## Author

Developed as a learning and portfolio project to explore modern backend development using Python and FastAPI.
