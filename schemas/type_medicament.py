# Python

# FastAPI

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class TypeMedicament(BaseModel):
  id: int = (...)
  type: str = Field(
    min_length=1,
    max_length=20
  )
  class Config:
    orm_mode = True