from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import relationship
from config.db import Base, engine
from models.test.father import Father

class Child(Base):
    __tablename__="child"
    id = Column(Integer, primary_key=True, index=True)
    father_id = Column(Integer, ForeignKey(Father.id))
Base.metadata.create_all(engine)
