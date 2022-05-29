#Python

#SQLAlchemy
from typing import final
from sqlalchemy.orm import Session

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Project imports
from routes.user_routes import user_routes
from config.db import engine
from models import patient, medicament, prescription, role, specialty, type_medicament, user_model
from models.test import child, father
#from models import models

type_medicament.Base.metadata.create_all(bind=engine)
patient.Base.metadata.create_all(bind=engine)
medicament.Base.metadata.create_all(bind=engine)
prescription.Base.metadata.create_all(bind=engine)
role.Base.metadata.create_all(bind=engine)
specialty.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
#models.Base.metadata.create_all(bind=engine)

#Test class
child.Base.metadata.create_all(bind=engine)
father.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:4200/admin/add-user",
    "http://localhost:4200",
    "http://localhost:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_routes)