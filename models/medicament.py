# Python

# SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Date, String, Integer

# Project imports
from config.db import Base
from config.db import engine
from models.type_medicament import TypeMedicament


# Create type_medicament table
class Medicament(Base):
    __tablename__ = "medicament"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    stock = Column(Integer)
    format_medicament = Column(String(30))
    type_medicament_id = Column(Integer, ForeignKey(TypeMedicament.id))
    laboratory_name = Column(String(30))
    principal_agent = Column(String(30))
    secondary_agent = Column(String(30))
    caducity_date = Column(Date())

    def __repr__(self) -> str:
        return super().__repr__()

Base.metadata.create_all(engine)