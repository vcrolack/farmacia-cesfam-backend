# Python
from datetime import datetime
from typing import TYPE_CHECKING

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine
from models.user_model import User
from models.patient import Patient
from models.medicament import Medicament
from models.type_medicament import TypeMedicament

if TYPE_CHECKING:
    from models.user_model import User


class Prescription(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    # user = relationship("user", back_populates="prescriptions")
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
    medic_name = Column(String(120), nullable=False)
    medicament_name = Column(String(30), nullable=False)
    patology = Column(String(30), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    date_prescription = Column(Date(), nullable=False)
    medicament_id = Column(Integer, ForeignKey(Medicament.id), nullable=False)
    type_medicament_id = Column(Integer, ForeignKey(TypeMedicament.id), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()

Base.metadata.create_all(engine)