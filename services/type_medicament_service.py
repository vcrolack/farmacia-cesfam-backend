# Python
from typing import List

# FastAPI
from fastapi import HTTPException, status

# Project imports
from models.type_medicament import TypeMedicament
from schemas.type_medicament import TypeMedicament as type_medicament_schema
from config.db import session

def get_types_medicaments() -> List[TypeMedicament]:
  return session.query(TypeMedicament).all()