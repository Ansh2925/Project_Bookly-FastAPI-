import uuid
from uuid import uuid4
from datetime import datetime, date

from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, DateTime


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        default_factory=lambda: str(uuid4()),
        sa_column=Column(String(36), primary_key=True)
    )

    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(DateTime)
    )

    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(DateTime)
    )

    def __repr__(self):
        return f'<Book {self.title}>'