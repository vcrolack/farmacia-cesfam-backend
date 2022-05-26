# Python
from datetime import datetime, date
from re import M
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class Patient(BaseModel):
    patient_id: int = Field(...)
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
    second_last_name: str = Field(
        ...,
        min_length=1,
        max_length=30,
        null=False
    )
    rut: str = Field(
        ...,
        min_length=8,
        max_length=9
    )
    birth_date: date = Field(default=None)
    phone: str = Field(
        ...,
        min_length=9,
        max_length=9
    )
    email: EmailStr = Field(
        ...,
        max_length=60
    )
    address: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
