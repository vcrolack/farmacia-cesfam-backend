# Python
from datetime import datetime, date

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class Prescription(BaseModel):
    user_id: int = Form(...)
    patient_id: int = Form(...)
    medic_name: str = Form(
        ...,
        min_length=1,
        max_length=120
    )
    medicament_name: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    patology: str = Form(
        ...,
        min_length=1,
        max_length=30
    )
    #created_at: datetime = Field(default=datetime.now())
    date_prescription: date = Form(...)
    medicament_id: int = Form(...)
    type_medicament_id: int = Form(...)
    
    class Config:
        orm_mode = True

class GetPrescription(Prescription):
    id: int
