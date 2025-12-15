from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    is_active: bool = True


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(...)
    tasks: List["Task"] = Relationship(back_populates="owner")


class UserCreate(UserBase):
    password: str


class UserPublic(UserBase):
    id: int
