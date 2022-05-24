# Python

# SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Date, String, Integer

# Project imports
from config.db import Base


# Create type_medicament table
class Medicament(Base):
    __tablename__ = "medicament"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    stock = Column(Integer)
    format_medicament = Column(String(30))
    type_medicament_id = Column(Integer, ForeignKey("medicament_type.id"))
    laboratory_name = Column(String(30))
    principal_agent = Column(String(30))
    secondary_agent = Column(String(30))
    caducity_date = Column(Date())

    def __repr__(self) -> str:
        return super().__repr__()