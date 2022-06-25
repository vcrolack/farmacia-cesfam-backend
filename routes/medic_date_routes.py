# Python
from importlib.resources import path
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.medic_date import MedicDate, GetMedicDate
from config.db import get_db
from services.medic_date_service import get_medics_dates, get_medic_date, create_medic_date, update_medic_date, delete_medic_date

medic_date_routes = APIRouter()

@medic_date_routes.get(
  path="/medics-dates",
  tags=["medics-dates"],
  
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Get all medics dates"
)
def get_all_medic_dates():
  return get_medics_dates()

@medic_date_routes.get(
  path="/medics-dates/{medic_date_id}",
  tags=["medics-dates"],
  response_model=GetMedicDate,
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Get a medic date"
)
def get_a_medic_date(medic_date_id: int):
  return get_medic_date(medic_date_id)

@medic_date_routes.post(
  path="/medics-dates",
  tags=["medics-dates"],
  response_model=MedicDate,
  status_code=status.HTTP_201_CREATED,
  dependencies=[Depends(get_db)],
  summary="Create a new medic date"
)
def create_a_medic_date(medic_date: MedicDate):
  return create_medic_date(medic_date)

@medic_date_routes.put(
  path="/medics-dates/{medic_date_id}",
  tags=["medics-dates"],
  response_model=MedicDate,
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Edit a medic date"
)
async def updated_a_medic_date(medic_date_id: int, medic_date: MedicDate):
  return update_medic_date(medic_date_id, medic_date)

@medic_date_routes.delete(
  path="/medics-dates/{medic_date_id}",
  tags=["medics-dates"],
  response_model=MedicDate,
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Delete a medic date"
)
def delete_a_medic_date(medic_date_id: int):
  return delete_medic_date(medic_date_id)