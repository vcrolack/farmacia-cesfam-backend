# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.patient import Patient
from config.db import get_db
#from services.user_service import


patient_routes = APIRouter()

@patient_routes.get(
    path="/patients",
    tags=["patients"],
    response_model=List[Patient],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all patients"
)
def get_patients():
    pass