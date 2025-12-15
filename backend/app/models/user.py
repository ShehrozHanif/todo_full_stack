"""
User domain model for Phase II.

Spec Reference: Domain Model -> User Entity
Plan Reference: Core Components -> User Model
"""
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .task import Task


class UserBase(SQLModel):
    """Base user model with shared fields."""
    email: str = Field(unique=True, index=True, max_length=255)
    username: str = Field(unique=True, index=True, min_length=3, max_length=50)


class User(UserBase, table=True):
    """Persistent user entity."""
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(min_length=1)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    tasks: List["Task"] = Relationship(back_populates="owner")


class UserCreate(SQLModel):
    """Schema for user registration."""
    email: str = Field(max_length=255)
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=100)


class UserPublic(UserBase):
    """Schema for user API responses (no password)."""
    id: int
    is_active: bool
    created_at: datetime


class UserLogin(SQLModel):
    """Schema for user login."""
    username: str
    password: str


class Token(SQLModel):
    """Schema for JWT token response."""
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """Schema for decoded JWT token data."""
    user_id: Optional[int] = None
