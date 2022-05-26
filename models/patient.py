# Python

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy import String, Integer, Date

# Project imports
from config.db import Base
from config.db import engine

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

Base.metadata.create_all(engine)