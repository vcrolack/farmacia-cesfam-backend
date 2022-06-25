# Python
from datetime import date

#FastAPI
from fastapi import Form

# Pydantic 
from pydantic import BaseModel

class MedicDate(BaseModel):
  user_id: int = Form(...)
  patient_id: int = Form(...)
  medic_date: date = Form(...)
  observations: str = Form(
    default=None,
    min_length=1,
    max_length=300
    )
    
  class Config:
    orm_mode = True

class GetMedicDate(MedicDate):
  id: int