#Python

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Project imports
from routes.user_routes import user_routes
from routes.patient_routes import patient_routes
from routes.medicament_routes import medicament_routes
from routes.specialty_routes import specialty_routes
from routes.type_medicament_routes import type_medicament_routes
from routes.prescription_routes import prescription_routes
from routes.medic_date_routes import medic_date_routes
from config.db import engine
from models import patient, medicament, prescription, role, specialty, type_medicament, user_model, medic_date
from models.test import child, father

type_medicament.Base.metadata.create_all(bind=engine)
patient.Base.metadata.create_all(bind=engine)
medicament.Base.metadata.create_all(bind=engine)
prescription.Base.metadata.create_all(bind=engine)
role.Base.metadata.create_all(bind=engine)
specialty.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
medic_date.Base.metadata.create_all(bind=engine)

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
app.include_router(patient_routes)
app.include_router(medicament_routes)
app.include_router(specialty_routes)
app.include_router(type_medicament_routes)
app.include_router(prescription_routes)
app.include_router(medic_date_routes)