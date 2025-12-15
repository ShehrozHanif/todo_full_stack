from sqlmodel import SQLModel, create_engine

from app.models.task import Task
from app.models.user import User

DATABASE_URL = "postgresql://user:password@host:port/database"

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)