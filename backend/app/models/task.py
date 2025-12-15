"""
Task domain model for Phase II.

Spec Reference: Domain Model -> Task Entity
Plan Reference: Core Components -> Task Model
"""
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class TaskBase(SQLModel):
    """Base task model with shared fields."""
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)


class Task(TaskBase, table=True):
    """Persistent task entity."""
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    owner: "User" = Relationship(back_populates="tasks")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    pass


class TaskUpdate(SQLModel):
    """Schema for updating a task (all fields optional)."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None


class TaskPublic(TaskBase):
    """Schema for task API responses."""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
