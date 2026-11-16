
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


# Create the tasks router
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# Create a new task
@router.post("/", response_model=schemas.TaskResponse,
             status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db)):

    # Convert the request data into a database model
    db_task = models.Task(**task.model_dump())

    # Save the task
    db.add(db_task)
    db.commit()

    # Get the newly generated task ID
    db.refresh(db_task)

    return db_task


# Get tasks with status filtering
@router.get("/", response_model=list[schemas.TaskResponse])
def get_tasks(
    status_filter: str = "all",
    db: Session = Depends(get_db)
):
    query = db.query(models.Task)

    if status_filter == "completed":
        query = query.filter(models.Task.completed.is_(True))

    elif status_filter == "pending":
        query = query.filter(models.Task.completed.is_(False))

    elif status_filter != "all":
        raise HTTPException(
            status_code=400,
            detail="Invalid status. Use all, completed, or pending."
        )

    return query.all()


# Get a single task by ID
@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

# Update an existing task
@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    db_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)

    return db_task

# Toggle task completion status
@router.patch("/{task_id}/complete",
              response_model=schemas.TaskResponse)
def toggle_task_completion(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # Change the completion status
    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task

# Delete a task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return None
