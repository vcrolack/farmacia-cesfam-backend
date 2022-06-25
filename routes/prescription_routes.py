# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.prescription import Prescription, GetPrescription
from config.db import get_db
from services.prescription_service import get_prescriptions, get_prescription, update_prescription, create_prescription, delete_prescription, get_prescriptions_patient

prescription_routes = APIRouter()

@prescription_routes.get(
    path="/prescriptions",
    tags=["prescriptions"],
    response_model=List[GetPrescription],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all prescriptions"
)
def get_all_prescriptions():
    prescriptions = get_prescriptions()
    return prescriptions

@prescription_routes.get(
    path="/prescriptions/patient/{patient_id}",
    tags=["prescriptions", "patients"],
    response_model=List[GetPrescription],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all prescriptions by patient id"
)
def get_all_prescriptions_by_patient(patient_id: int):
    return get_prescriptions_patient(patient_id)

@prescription_routes.post(
    path="/prescriptions",
    tags=["prescriptions"],
    response_model=Prescription,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_db)],
    summary="Create a new prescription"
)
def create_a_prescription(prescription: Prescription):
    return create_prescription(prescription)

@prescription_routes.put(
    path="/prescriptions/{prescription_id}",
    tags=["prescriptions"],
    response_model=Prescription,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Update a prescription"
)
def update_a_prescription(prescription_id: int, prescription: Prescription):
    return update_prescription(prescription_id, prescription)

@prescription_routes.get(
    path="/prescriptions/{prescription_id}",
    tags=["prescriptions"],
    response_model=Prescription,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get a prescription"
)
def get_a_prescription(prescription_id: int):
    return get_prescription(prescription_id)

@prescription_routes.delete(
    path="/prescriptions/{prescription_id}",
    tags=[Depends(get_db)],
    response_model=Prescription,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete a prescription"
)
def delete_a_prescription(prescription_id: int):
    return delete_prescription(prescription_id)