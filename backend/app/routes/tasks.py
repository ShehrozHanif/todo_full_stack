from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.db import engine
from app.models.task import Task, TaskCreate, TaskPublic
from app.models.user import User
from app.auth.auth import create_access_token, get_password_hash, verify_password

router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/tasks/", response_model=TaskPublic)
def create_task(
    *,
    session: Session = Depends(get_session),
    task: TaskCreate,
    # current_user: User = Depends(get_current_active_user),
):
    # db_task = Task.from_orm(task, update={"owner_id": current_user.id})
    db_task = Task.from_orm(task, update={"owner_id": 1})  # Dummy owner_id
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.get("/tasks/", response_model=List[TaskPublic])
def read_tasks(
    *,
    session: Session = Depends(get_session),
    # current_user: User = Depends(get_current_active_user),
):
    # tasks = session.exec(select(Task).where(Task.owner_id == current_user.id)).all()
    tasks = session.exec(select(Task)).all()  # No user filtering for now
    return tasks


@router.put("/tasks/{task_id}", response_model=TaskPublic)
def update_task(
    *,
    session: Session = Depends(get_session),
    task_id: int,
    task: TaskUpdate,
    # current_user: User = Depends(get_current_active_user),
):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    # if db_task.owner_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not enough permissions")
    task_data = task.dict(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.patch("/tasks/{task_id}/complete", response_model=TaskPublic)
def complete_task(
    *,
    session: Session = Depends(get_session),
    task_id: int,
    # current_user: User = Depends(get_current_active_user),
):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    # if db_task.owner_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not enough permissions")
    db_task.completed = True
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete("/tasks/{task_id}")
def delete_task(
    *,
    session: Session = Depends(get_session),
    task_id: int,
    # current_user: User = Depends(get_current_active_user),
):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    # if db_task.owner_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(db_task)
    session.commit()
    return {"ok": True}
