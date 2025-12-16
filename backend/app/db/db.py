"""
Database configuration and session management.

Spec Reference: Data & Persistence Rules
Plan Reference: Core Components -> Database Layer
"""
import os
from typing import Generator

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Use SQLite for local development if no DATABASE_URL provided
if not DATABASE_URL or DATABASE_URL == "your_neon_database_url":
    DATABASE_URL = "sqlite:///./todo.db"
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

# Create engine with appropriate settings
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args=connect_args,
)


def create_db_and_tables() -> None:
    """Create all database tables from SQLModel metadata."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Dependency for getting database sessions."""
    with Session(engine) as session:
        yield session
