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
