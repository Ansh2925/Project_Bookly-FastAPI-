import uuid
from uuid import uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, DateTime

class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        default_factory=lambda: str(uuid4()),
        sa_column=Column(String(36), primary_key=True)
    )

    username : str
    password : str
    email : str
    first_name : str
    last_name : str
    is_verified : bool = False

    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(DateTime)
    )

    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(DateTime)
    )

    def __repr__(self):
        return f"<User {self.username}"