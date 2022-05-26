from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import relationship
from config.db import Base, engine

class Father(Base):
    __tablename__="father"
    id = Column(Integer, primary_key=True, index=True)
    children=relationship("Child")
Base.metadata.create_all(engine)