# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.patient import Patient
from config.db import get_db
from services.patient_service import get_patients, create_patient, update_patient, get_patient, delete_patient


patient_routes = APIRouter()

@patient_routes.get(
    path="/patients",
    tags=["patients"],
    response_model=List[Patient],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all patients"
)
def get_all_patients():
    patients = get_patients()
    return patients

@patient_routes.post(
    path="/patients",
    tags=["patients"],
    response_model=Patient,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_db)],
    summary="Create a new patient"
)
def create_a_patient(patient: Patient):
    return create_patient(patient)

@patient_routes.put(
    path="/patients/{patient_id}",
    tags=["patients"],
    response_model=Patient,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Update an patient"
)
def update_a_patient(patient_id: int, patient: Patient):
    return update_patient(patient_id, patient)

@patient_routes.get(
    path="/patients/{patient_id}",
    tags=["patients"],
    response_model=Patient,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get a patient"
)
def get_a_patient(patient_id: int):
    return get_patient(patient_id)

@patient_routes.delete(
    path="/patients/{patient_id}",
    tags=["patients"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete a patient"
)
def delete_a_patient(patient_id: int):
    return delete_patient(patient_id)