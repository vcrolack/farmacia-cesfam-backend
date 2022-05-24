# Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime, Date

# Project imports
from config.db import Base

class Prescription(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
    medic_name = Column(String(30))
    medicament_name = Column(String(30))
    patology = Column(String(30))
    created_at = Column(DateTime(), default=datetime.now())
    date_prescription = Column(Date())
    medicament_id = Column(Integer, ForeignKey("medicament.id"))
    type_medicament = Column(Integer)

    def __repr__(self) -> str:
        return super().__repr__()