# Python

# FastAPI

# Pydantic
from pydantic import BaseModel
from pydantic import Field

class Specialty(BaseModel):
  id: int
  name: str = Field(...)

  class Config:
    orm_mode = True