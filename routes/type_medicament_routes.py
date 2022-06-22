# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.type_medicament import TypeMedicament
from config.db import get_db
from services.type_medicament_service import get_types_medicaments

type_medicament_routes = APIRouter()

@type_medicament_routes.get(
  path="/types-medicaments",
  tags=["medicaments"],
  response_model=List[TypeMedicament],
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Get all types of medicaments"
)
def get_all_types_medicaments():
  types_medicaments = get_types_medicaments()
  return types_medicaments