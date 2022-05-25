# Python

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy import String, Integer, Date

# Project imports
from config.db import Base

class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30))
    second_name = Column(String(30))
    last_name = Column(String(30))
    second_last_name = Column(String(30))
    rut = Column(String(12))
    birth_date = Column(Date())
    phone = Column(String(9))
    email = Column(String(60))
    prescription = relationship("Prescription")
    address = Column(String(60))

    def __repr__(self):
        return f"Patient:\nid:{self.id}\nfirst_name:{self.first_name}\nsecond_name:{self.second_name}\nlast_name:{self.last_name}\nsecond_last:{self.second_last_name}\nrut:{self.rut}\nbirth_date:{self.birth_date}\nphone:{self.phone}\nemail:{self.email}\nAddress:{self.address}"

