#Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine
from models.role import Role

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, index=True)
    first_name = Column(String(30), nullable=False)
    second_name = Column(String(30))
    last_name = Column(String(30), nullable=False)
    second_last_name = Column(String(30), nullable=False)
    rut = Column(String(12), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    role = relationship("Role")
    specialty_id = Column(String(30), nullable=True)
    specialty = relationship("specialty")
    prescription = relationship("prescription")

    def __repr__(self):
        return f"User:\nname:{self.id}\nsecond name:{self.first_name}\nlast name:{self.last_name}\nsecond last name:{self.second_last_name}\nrut:{self.rut}\nemail:{self.email}\ncreated at:{self.created_at}\nrole id:{self.role_id}\nspecialty:{self.specialty_id}"

Base.metadata.create_all(engine)