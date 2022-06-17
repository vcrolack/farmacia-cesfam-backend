# Python 
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.specialty import Specialty
from config.db import get_db
from services.specialty_service import get_specialties

specialty_routes = APIRouter()

@specialty_routes.get(
  path="/specialties",
  tags=["specialties"],
  response_model=List[Specialty],
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Get all specialties"
)
def get_all_specialties():
  specialties = get_specialties()
  return specialties