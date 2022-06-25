# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.role import Role
from config.db import get_db
from services.role_service import get_roles

role_routes = APIRouter()

@role_routes.get(
  path="/roles",
  tags=["roles"],
  response_model=List[Role],
  status_code=status.HTTP_200_OK,
  dependencies=[Depends(get_db)],
  summary="Get all roles"
)
def get_all_roles():
  return get_roles()