# Python
from typing import List

# FastAPI
from fastapi import status, HTTPException

# Project imports
from models.medic_date import MedicDate
from schemas.medic_date import MedicDate as medic_date_schema
from config.db import session

def get_medics_dates() -> List[MedicDate]:
  return session.query(MedicDate).all()

def get_medic_date(medic_date: id):
  medic_date = session.query(MedicDate).get(medic_date)
  if not medic_date:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Medic date doesn't exist"
    )
  return medic_date

def create_medic_date(medic_date: MedicDate):

  db_medic_date = MedicDate(
    user_id = medic_date.user_id,
    patient_id = medic_date.patient_id,
    medic_date = medic_date.medic_date,
    observations = medic_date.observations
  )

  session.add(db_medic_date)
  session.commit()

  return medic_date_schema(
    id=db_medic_date.id,
    user_id=db_medic_date.user_id,
    patient_id=db_medic_date.patient_id,
    medic_date=db_medic_date.medic_date,
    observations=db_medic_date.observations
  )

def update_medic_date(medic_date_id: int, medic_date: MedicDate):
  db_medic_date = session.query(MedicDate).get(medic_date_id)
  if not db_medic_date:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Medic date doesn't exist"
    )
  
  db_medic_date.user_id = medic_date.user_id
  db_medic_date.patient_id = medic_date.patient_id
  db_medic_date.medic_date = medic_date.medic_date
  db_medic_date.observations = medic_date.observations

  session.commit()

  return db_medic_date

def delete_medic_date(medic_date_id: int):
  db_medic_date = session.query(MedicDate).get(medic_date_id)
  if not db_medic_date:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Medic date doesn't exist"
    )
  
  session.delete(db_medic_date)
  session.commit()

  return {"detail": "Prescription deleted"}
