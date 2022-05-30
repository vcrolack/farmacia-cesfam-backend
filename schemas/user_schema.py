# Python
from datetime import datetime
from typing import Optional

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserBase(BaseModel):
    #user_id: int = Field(...)
    email: EmailStr = Form(...)
    rut: str = Form(
        ...,
        min_length= 8,
        max_length=9
    )
    class Config:
        orm_mode = True

class User(UserBase):
    first_name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    second_name: Optional[str] = Form(
        default=None,
        min_length=1,
        max_length=30
    )
    last_name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    second_last_name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    #created_at: datetime = Field(default=datetime.now())
    role_id: int = Form(...)
    specialty_id: Optional[int] = Form(...)
    
class UserLogin(User):
    password: str = Form(
        ...,
        min_length=6,
        max_length=25,
    )

class UserLoginFront(BaseModel):
    rut: str = Form(
        ...,
        min_length=8,
        max_length=9
    )
    password: str = Form(
        ...,
        min_length=6,
        max_length=25
    )
