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
    name = Column(String(30), nullable=False)
    grammage = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    format_medicament = Column(String(30), nullable=False)
    type_medicament_id = Column(Integer, ForeignKey(TypeMedicament.id), nullable=False)
    laboratory_name = Column(String(30), nullable=False)
    principal_agent = Column(String(30), nullable=False)
    secondary_agent = Column(String(30), nullable=False)
    caducity_date = Column(Date(), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()

Base.metadata.create_all(engine)