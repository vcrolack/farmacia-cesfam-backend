# Python
from typing import TYPE_CHECKING

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine

if TYPE_CHECKING:
    from .user_model import User

class Specialty(Base):
    __tablename__ = "specialty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(35), nullable=False)
    #specialties = relationship("User", back_populates="medic_specialty")

    def __repr__(self):
        return f"Specialty:\nid:{self.id}\nname:{self.name} "

Base.metadata.create_all(engine)