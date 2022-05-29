#Python
from datetime import datetime
from typing import TYPE_CHECKING

# SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine
from models.role import Role
#from models.specialty import Specialty
#from models.prescription import Prescription


from .specialty import Specialty

if TYPE_CHECKING:
    from models.prescription import Prescription

class User(Base):
    __tablename__ = "user"

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
    # role = relationship("Role")
    specialty_id = Column(Integer, ForeignKey(Specialty.id), nullable=True)
    # medic_specialty = relationship("Specialty", back_populates="specialties")
    # prescriptions = relationship("prescription", back_populates="user")

    def __repr__(self):
        return f"User:\nname:{self.id}\nsecond name:{self.first_name}\nlast name:{self.last_name}\nsecond last name:{self.second_last_name}\nrut:{self.rut}\nemail:{self.email}\ncreated at:{self.created_at}\nrole id:{self.role_id}\nspecialty:{self.specialty_id}"

Base.metadata.create_all(engine)