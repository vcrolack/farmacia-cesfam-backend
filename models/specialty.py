# Python

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String

# Project imports
from config.db import Base
from config.db import engine

class Specialty(Base):
    __tablename__ = "specialty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(35))

    def __repr__(self):
        return f"Specialty:\nid:{self.id}\nname:{self.name} "

Base.metadata.create_all(engine)