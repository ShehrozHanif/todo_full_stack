from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .user import User


class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="tasks")


class TaskCreate(TaskBase):
    pass


class TaskPublic(TaskBase):
    id: int
    owner_id: int
