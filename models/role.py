#Python

#SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(35), nullable=False)
    
    def __repr__(self):
        return f"Role:\nid:{self.id}\nname:{self.name} "

Base.metadata.create_all(engine)