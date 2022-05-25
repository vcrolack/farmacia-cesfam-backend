#Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, index=True)
    first_name = Column(String(30), nullable=False)
    second_name = Column(String(30))
    last_name = Column(String(30))
    second_last_name = Column(String(30))
    rut = Column(String(12), unique=True)
    email = Column(String(60), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    role = relationship("role")
    specialty_id = Column(String(30), nullable=True)
    specialty = relationship("specialty")
    prescription = relationship("prescription")

    def __repr__(self):
        return f"User:\nname:{self.id}\nsecond name:{self.first_name}\nlast name:{self.last_name}\nsecond last name:{self.second_last_name}\nrut:{self.rut}\nemail:{self.email}\ncreated at:{self.created_at}\nrole id:{self.role_id}\nspecialty:{self.specialty_id}"