# Python
from typing import Optional, Union

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserBase(BaseModel):
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
    specialty_id: Union[int, None] = Form(default=None)
    
class UserLogin(User):
    password: str = Form(
        ...,
        min_length=6,
        max_length=25,
    )

class PaginatedUsersInfo(BaseModel):
    limit: int
    offset: int
    data: Optional[User]

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

class GetUser(User):
    id: int