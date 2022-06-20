# Python
from typing import List

# FastAPI
from fastapi import status, HTTPException

# Project imports
from models.patient import Patient
from schemas.patient import Patient as patient_schema
from config.db import session

def get_patients() -> List[Patient]:
    return session.query(Patient).all()

def create_patient(patient: Patient):
    get_patient = session.query(Patient).filter_by(email=patient.email, rut=patient.rut).first()

    if get_patient:
        message = "Email already registered"
        if get_patient.rut == patient.rut:
            message = "Rut already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
    
    db_patient = Patient(
        first_name=patient.first_name,
        second_name=patient.second_name,
        last_name=patient.last_name,
        second_last_name=patient.second_last_name,
        rut=patient.rut,
        birth_date=patient.birth_date,
        phone=patient.phone,
        email=patient.email,
        address=patient.address
    )

    session.add(db_patient)
    session.commit()

    return patient_schema(
        id=db_patient.id,
        first_name=db_patient.first_name,
        second_name=db_patient.second_name,
        last_name=db_patient.last_name,
        second_last_name=db_patient.second_last_name,
        rut=db_patient.rut,
        birth_date=db_patient.birth_date,
        phone=db_patient.phone,
        email=db_patient.email,
        address=db_patient.address
    )

def get_patient(rut: str):
    patient = session.query(Patient).filter_by(rut=rut).one()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient doesn't exist"
        )
    return patient

def update_patient(rut: str, patient: Patient):
    db_patient = session.query(Patient).filter_by(rut=rut).one()
    if not db_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient doesn't exist"
        )
    
    db_patient.first_name = patient.first_name
    db_patient.second_name = patient.second_name
    db_patient.last_name = patient.last_name
    db_patient.second_last_name = patient.second_last_name
    db_patient.rut = patient.rut
    db_patient.birth_date = patient.birth_date
    db_patient.phone = patient.phone
    db_patient.email = patient.email
    db_patient.address = patient.address

    session.commit()

    return db_patient

def delete_patient(rut: str):
    patient = session.query(Patient).filter_by(rut=rut).one()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient doesn't exist"
        )
    
    session.delete(patient)
    session.commit()

    return {"detail": "Patient deleted"}

    