# Python

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship

# Project imports
from config.db import Base
from config.db import engine
 
class TypeMedicament(Base):
    #Like ansiolitic, analgesic...
    __tablename__ = "type_medicament"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(30), nullable=False)
    medicament = relationship("medicament")
    prescription = relationship("type_medicament")

    def __repr__(self) -> str:
        return super().__repr__()
    
Base.metadata.create_all(engine)