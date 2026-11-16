
# Task Manager Backend API

## Project Description

The Task Manager Backend is a REST API application developed using Python and FastAPI.

It allows users to create, view, update, delete, and manage tasks. The application uses SQLite as its database and SQLAlchemy for database operations.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Structure

task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
│
├── requirements.txt
├── README.md
└── .gitignore

## Features

1. Create new tasks.
2. View all tasks.
3. View a task by ID.
4. Update existing tasks.
5. Mark tasks as completed or pending.
6. Delete tasks.
7. Filter tasks by completion status.
8. Validate task titles and descriptions.
9. Handle errors for tasks that do not exist.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks/ | Create a task |
| GET | /tasks/ | Get all tasks |
| GET | /tasks/{task_id} | Get task by ID |
| PUT | /tasks/{task_id} | Update a task |
| PATCH | /tasks/{task_id}/complete | Toggle task status |
| DELETE | /tasks/{task_id} | Delete a task |

## Installation

Install the required packages:

    python -m pip install -r requirements.txt

## Run the Application

Start the FastAPI server:

    python -m uvicorn app.main:app --reload

## API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

Use the Swagger interface to test the API endpoints.

## Database

The application uses SQLite.

The database file is created automatically when the application starts.

## Project Purpose

This project was developed to practice Python backend development, REST API creation, database connectivity, CRUD operations, and input validation.