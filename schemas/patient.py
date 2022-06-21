# Python
from datetime import datetime, date
from typing import Optional

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr

class Patient(BaseModel):
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
        max_length=30,
        null=False
    )
    rut: str = Form(
        ...,
        min_length=8,
        max_length=9
    )
    birth_date: date = Form(...)
    phone: str = Form(
        ...,
        min_length=9,
        max_length=9
    )
    email: EmailStr = Form(...)
    address: str = Form(
        ...,
        min_length=1,
        max_length=60
    )

    class Config:
        orm_mode = True

class GetPatient(Patient):
    id: int
