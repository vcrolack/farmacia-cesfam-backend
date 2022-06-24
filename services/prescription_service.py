# Python
from datetime import datetime
from typing import List

# FastAPI
from fastapi import status, HTTPException

# Project imports
from models.prescription import Prescription
from schemas.prescription import Prescription as prescription_schema
from config.db import session

def get_prescriptions() -> List[Prescription]:
    return session.query(Prescription).all()

def create_prescription(prescription: Prescription):
    
    db_prescription = Prescription(
        user_id=prescription.user_id,
        patient_id=prescription.patient_id,
        medic_name=prescription.medic_name,
        medicament_name=prescription.medicament_id,
        created_at=datetime.now(),
        date_prescription=prescription.date_prescription,
        patology=prescription.patology,
        medicament_id=prescription.medicament_id,
        type_medicament_id=prescription.type_medicament_id
    )

    session.add(db_prescription)
    session.commit()

    return prescription_schema(
        id=db_prescription.id,
        user_id=db_prescription.user_id,
        patient_id=db_prescription.patient_id,
        medic_name=db_prescription.medic_name,
        medicament_name=db_prescription.medicament_name,
        patology=db_prescription.patology,
        date_prescription=db_prescription.date_prescription,
        created_at=db_prescription.created_at,
        medicament_id=db_prescription.medicament_id,
        type_medicament_id=db_prescription.type_medicament_id
    )

def get_prescription(prescription_id: int):
    prescription = session.query(Prescription).get(prescription_id)
    if not prescription:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Prescription doesn't exist"
        )
    return prescription

def update_prescription(prescription_id: int, prescription: Prescription):
    db_prescription = session.query(Prescription).get(prescription_id)
    if not db_prescription:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Prescription doesn't exist"
        )
    
    db_prescription.user_id = prescription.user_id
    db_prescription.patient_id = prescription.patient_id
    db_prescription.medic_name = prescription.medicament_name
    db_prescription.medicament_name = prescription.medicament_name
    db_prescription.patology = prescription.patology
    db_prescription.medicament_id = prescription.medicament_id
    db_prescription.type_medicament_id = prescription.type_medicament_id

    session.commit()

    return db_prescription

def delete_prescription(prescription_id: int):
    prescription = session.query(Prescription).get(prescription_id)

    if not prescription:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Prescription doesn't exist"
        )
    
    session.delete(prescription)
    session.commit()

    return {"detail": "Prescription deleted"}

