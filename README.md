# Task Manager Backend API

## Project Overview

The Task Manager Backend is a simple REST API application developed using Python, FastAPI, SQLite, and SQLAlchemy.

This application allows users to create, view, update, complete, filter, and delete tasks. It also includes input validation and error handling to ensure proper data management.

## Technologies Used

- **Python** – Backend programming language
- **FastAPI** – Framework for building REST APIs
- **SQLite** – Database for storing tasks
- **SQLAlchemy** – ORM for database operations
- **Pydantic** – Data validation and request handling
- **Uvicorn** – ASGI server for running the application

## Project Structure

```text
task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Features

1. Create a new task.
2. Retrieve all tasks.
3. Retrieve a task using its ID.
4. Update task details.
5. Mark a task as completed or pending.
6. Filter tasks by status:
   - All tasks
   - Completed tasks
   - Pending tasks
7. Delete a task.
8. Validate task titles and descriptions.
9. Handle errors such as invalid task IDs and invalid filters.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check application status |
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| PATCH | `/tasks/{task_id}/complete` | Toggle completion status |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Task Filtering

The GET `/tasks/` endpoint supports a query parameter called `status_filter`.

Examples:

- `/tasks/?status_filter=all`
- `/tasks/?status_filter=completed`
- `/tasks/?status_filter=pending`

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd task_manager
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

## API Documentation

After starting the application, open the following URL in your browser:

**Swagger UI:**
http://127.0.0.1:8000/docs

**ReDoc:**
http://127.0.0.1:8000/redoc

You can use these interfaces to test all API endpoints.

## Database

The application uses SQLite as its database.

The database file is automatically created when the application runs. SQLAlchemy manages database operations through the Task model.

## Error Handling and Validation

The application handles the following HTTP status codes:

- `200 OK` – Request completed successfully.
- `201 Created` – Task created successfully.
- `204 No Content` – Task deleted successfully.
- `400 Bad Request` – Invalid task status filter.
- `404 Not Found` – Requested task does not exist.
- `422 Unprocessable Entity` – Invalid input data.

