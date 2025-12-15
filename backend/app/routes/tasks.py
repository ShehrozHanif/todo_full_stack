"""
Task management routes with authentication.

Spec Reference: REST API Endpoint Specification
  - POST /api/tasks
  - GET /api/tasks
  - PUT /api/tasks/{id}
  - PATCH /api/tasks/{id}/complete
  - DELETE /api/tasks/{id}
"""
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.auth.auth import get_current_user
from app.db.db import get_session
from app.models.task import Task, TaskCreate, TaskUpdate, TaskPublic
from app.models.user import User

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.post("/", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
def create_task(
    task_data: TaskCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new task for the authenticated user.

    Spec Reference: FR-3: Create Task (Authenticated)
    """
    db_task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        owner_id=current_user.id,
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.get("/", response_model=List[TaskPublic])
def list_tasks(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    List all tasks for the authenticated user.

    Spec Reference: FR-4: List User Tasks
    """
    statement = select(Task).where(Task.owner_id == current_user.id).order_by(Task.created_at.desc())
    tasks = session.exec(statement).all()
    return tasks


@router.get("/{task_id}", response_model=TaskPublic)
def get_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Get a specific task by ID."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task",
        )
    return task


@router.put("/{task_id}", response_model=TaskPublic)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Update an existing task.

    Spec Reference: FR-5: Update Task
    """
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this task",
        )

    # Update only provided fields
    update_data = task_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.patch("/{task_id}/complete", response_model=TaskPublic)
def complete_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Mark a task as completed.

    Spec Reference: FR-6: Complete Task
    """
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this task",
        )

    task.completed = True
    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Delete a task.

    Spec Reference: FR-7: Delete Task
    """
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task",
        )

    session.delete(task)
    session.commit()
    return None
