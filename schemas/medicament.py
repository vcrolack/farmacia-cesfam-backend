# Python
from datetime import date

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class Medicament(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    grammage: int = Field(...)
    stock: int = Field(...)
    format_medicament: int = Field(
        ...,
        min_length=1,
        max_length=25
    )
    type_medicament_id: int = Field(...)
    laboratory_name: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    principal_agent: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    secondary_agent: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    caducity_date: date = Field(...)