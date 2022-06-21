# Python 
from typing import List

# FastAPI
from fastapi import HTTPException, status

# Project imports 
from models.specialty import Specialty
from schemas.specialty import Specialty as specialty_schema
from config.db import session

def get_specialties() -> List[Specialty]:
  return session.query(Specialty).all()

def get_specialty(specialty_id: int):
  specialty = session.query(Specialty).get(specialty_id)
  if not specialty:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Specialty doesn't exist"
    )
  return specialty
