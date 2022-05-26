# Python
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserBase(BaseModel):
    user_id: int = Field(...)
    email: EmailStr = Field(...)
    rut: str = Field(
        ...,
        min_length= 8,
        max_length=9
    )

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=25,
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    second_name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=30
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    second_last_name = Field(
        ...,
        min_length=1,
        max_length=30
    )
    created_at: datetime = Field(default=datetime.now())
    role_id: int = Field(...)
    specialty_id: Optional[int] = Field(...)
    