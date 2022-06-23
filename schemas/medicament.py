# Python
from datetime import date

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class Medicament(BaseModel):
    name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    grammage: int = Form(...)
    stock: int = Form(...)
    format_medicament: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    type_medicament_id: int = Form(...)
    laboratory_name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    principal_agent: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    secondary_agent: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    caducity_date: date = Form(...)

    class Config:
        orm_mode = True

class GetMedicament(Medicament):
    id: int