#Python

#SQLAlchemy
from typing import final
from sqlalchemy.orm import Session

# FastAPI
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

# Project imports
from routes.user import user
from config.db import SessionLocal, engine, Base
from models import patient, medicament, prescription, role, specialty, type_medicament, user

type_medicament.Base.metadata.create_all(bind=engine)
patient.Base.metadata.create_all(bind=engine)
medicament.Base.metadata.create_all(bind=engine)
prescription.Base.metadata.create_all(bind=engine)
role.Base.metadata.create_all(bind=engine)
specialty.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


#app.include_router(user)