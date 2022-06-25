# Python
from typing import List

# FastAPI
from fastapi import status, HTTPException

# Project imports
from models.role import Role
from schemas.role import Role as role_schema
from config.db import session

def get_roles():
  return session.query(Role).all()