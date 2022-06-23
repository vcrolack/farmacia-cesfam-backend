# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.medicament import Medicament, GetMedicament
from config.db import get_db
from services.medicament_service import get_medicaments, get_medicament, create_medicament, update_medicament, delete_medicament

medicament_routes = APIRouter()

@medicament_routes.get(
    path="/medicaments",
    tags=["medicaments"],
    response_model=List[GetMedicament],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all medicaments"
)
def get_all_medicaments():
    medicaments = get_medicaments()
    return medicaments

@medicament_routes.get(
    path="/medicaments/{medicament_id}",
    tags=["medicaments"],
    response_model=GetMedicament,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get a medicament"
)
def get_a_medicament(medicament_id: int):
    return get_medicament(medicament_id)

@medicament_routes.post(
    path="/medicaments",
    tags=["medicaments"],
    response_model=Medicament,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Create a medicament"
)
def create_a_medicament(medicament: Medicament):
    return create_medicament(medicament)

@medicament_routes.put(
    path="/medicaments/{medicament_id}",
    tags=["medicaments"],
    response_model=Medicament,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Update a medicament"
)
def update_a_medicament(medicament_id: int, medicament: Medicament):
    return update_medicament(medicament_id, medicament)

@medicament_routes.delete(
    path="/medicaments/{medicament_id}",
    tags=["medicaments"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete a patient"
)
def delete_a_patient(patient_id: int):
    return delete_medicament(patient_id)