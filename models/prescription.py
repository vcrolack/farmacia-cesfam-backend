# Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime, Date

# Project imports
from config.db import Base
from config.db import engine
from models.user import User
from models.type_medicament import TypeMedicament

class Prescription(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    patient_id = Column(Integer, ForeignKey("patient.id"), nullable=False)
    medic_name = Column(String(120), nullable=False)
    medicament_name = Column(String(30), nullable=False)
    patology = Column(String(30), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    date_prescription = Column(Date(), nullable=False)
    medicament_id = Column(Integer, ForeignKey("medicament.id"), nullable=False)
    type_medicament_id = Column(Integer, ForeignKey(TypeMedicament.id), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()

Base.metadata.create_all(engine)