# Python
from datetime import datetime, date

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class Prescription(BaseModel):
    user_id: int = Field(...)
    patient_id: int = Field(...)
    medic_name: str = Field(
        ...,
        min_length=1,
        max_length=120
    )
    medicament_name: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    patology: str = Field(
        ...,
        min_length=1,
        max_length=30
    )
    created_at: datetime = Field(default=datetime.now())
    date_prescription: date = Field(...)
    medicament_id: int = Field(...)
    type_medicament_id = Field(...)
    
    class Config:
        orm_mode = True
