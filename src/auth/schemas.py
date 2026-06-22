import uuid
from datetime import datetime
from pydantic import BaseModel, Field

class UserCreateModel(BaseModel):
    username : str = Field(max_length=20)
    email : str = Field(min_length=8)
    password : str
    first_name : str = Field(max_length=25)
    last_name : str = Field(max_length=25)

class UserModel(BaseModel):
    uid: uuid.UUID
    username : str
    email : str
    password_hash : str = Field(exclude=True)
    first_name : str
    last_name : str
    is_verified : bool
    created_at: datetime
    updated_at: datetime
