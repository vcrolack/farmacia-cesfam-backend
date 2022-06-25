# Python

#SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import relationship

#Project imports
from config.db import Base
from config.db import engine
from models.user_model import User
from models.patient import Patient

class MedicDate(Base):
  __tablename__ = "medicdate"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey(User.id), nullable=False)
  patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
  medic_date = Column(Date(), nullable=False)
  observations = Column(String(300), nullable=True)

  def __repr__(self) -> str:
    return super().__repr__()

Base.metadata.create_all(engine)