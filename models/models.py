#Python
from datetime import datetime, date

# SQLAlchemy
from sqlalchemy import Column, DateTime, Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine



# PATIENT MODEL
class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30), nullable=False)
    second_name = Column(String(30))
    last_name = Column(String(30), nullable=False)
    second_last_name = Column(String(30), nullable=False)
    rut = Column(String(12), nullable=False, unique=True)
    birth_date = Column(Date(), nullable=False)
    phone = Column(String(9), nullable=False)
    email = Column(String(60), nullable=False)
    prescription = relationship("Prescription")
    address = Column(String(60), nullable=False )

    def __repr__(self):
        return f"Patient:\nid:{self.id}\nfirst_name:{self.first_name}\nsecond_name:{self.second_name}\nlast_name:{self.last_name}\nsecond_last:{self.second_last_name}\nrut:{self.rut}\nbirth_date:{self.birth_date}\nphone:{self.phone}\nemail:{self.email}\nAddress:{self.address}"

# PRESCRIPTION MODEL
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

# ROLE MODEL
class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(35), nullable=False)
    
    def __repr__(self):
        return f"Role:\nid:{self.id}\nname:{self.name} "

# SPECIALTY MODEL
class Specialty(Base):
    __tablename__ = "specialty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(35), nullable=False)

    def __repr__(self):
        return f"Specialty:\nid:{self.id}\nname:{self.name} "

# TYPE_MEDICAMENT MODEL
class TypeMedicament(Base):
    #Like ansiolitic, analgesic...
    __tablename__ = "type_medicament"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(30), nullable=False)
    medicament = relationship("medicament")
    prescription = relationship("type_medicament")

    def __repr__(self) -> str:
        return super().__repr__()

# USER MODEL
class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key = True, index=True)
    first_name = Column(String(30), nullable=False)
    second_name = Column(String(30))
    last_name = Column(String(30), nullable=False)
    second_last_name = Column(String(30), nullable=False)
    rut = Column(String(12), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    role = relationship("Role")
    specialty_id = Column(String(30), ForeignKey(Specialty.__table__.c.id), nullable=True)
    specialty = relationship(Specialty)
    prescription = relationship("Prescription")

    def __repr__(self):
        return f"User:\nname:{self.id}\nsecond name:{self.first_name}\nlast name:{self.last_name}\nsecond last name:{self.second_last_name}\nrut:{self.rut}\nemail:{self.email}\ncreated at:{self.created_at}\nrole id:{self.role_id}\nspecialty:{self.specialty_id}"
