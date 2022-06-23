# Python
from datetime import datetime
from typing import List

# FastAPI
from fastapi import HTTPException, status

# Project imports
from models.medicament import Medicament
from schemas.medicament import Medicament as medicament_schema
from schemas.medicament import GetMedicament
from config.db import session

def get_medicaments() -> List[GetMedicament]:
    return session.query(Medicament).all()

def create_medicament(medicament: Medicament):
    get_medicament = session.query(Medicament).filter_by(name=medicament.name, grammage=medicament.name, type_medicament_id=medicament.type_medicament_id).first()

    if get_medicament:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Medicament already registerd"
        )
    
    db_medicament = Medicament(
        name=medicament.name,
        grammage=medicament.grammage,
        stock=medicament.stock,
        format_medicament=medicament.format_medicament,
        type_medicament_id=medicament.type_medicament_id,
        laboratory_name=medicament.laboratory_name,
        principal_agent=medicament.principal_agent,
        secondary_agent=medicament.secondary_agent,
        caducity_date=medicament.caducity_date
    )

    session.add(db_medicament)
    session.commit()

    return medicament_schema(
        id=db_medicament.id,
        name=db_medicament.name,
        grammage=db_medicament.grammage,
        stock=db_medicament.stock,
        format_medicament=db_medicament.format_medicament,
        type_medicament_id=db_medicament.type_medicament_id,
        laboratory_name=db_medicament.laboratory_name,
        principal_agent=db_medicament.principal_agent,
        secondary_agent=db_medicament.secondary_agent,
        caducity_date=db_medicament.caducity_date
    )

def get_medicament(medicament_id: int):
    medicament = session.query(Medicament).get(medicament_id)
    if not medicament:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Medicament doesn't exist"
        )
    
    return medicament

def update_medicament(medicament_id: int, medicament: Medicament):
    db_medicament = session.query(Medicament).get(medicament_id)
    if not db_medicament:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Medicament doesnt't exist"
        )
    
    db_medicament.name = medicament.name
    db_medicament.grammage = medicament.grammage
    db_medicament.stock = medicament.stock
    db_medicament.format_medicament = medicament.format_medicament
    db_medicament.type_medicament_id = medicament.type_medicament_id
    db_medicament.laboratory_name = medicament.laboratory_name
    db_medicament.principal_agent = medicament.principal_agent
    db_medicament.secondary_agent = medicament.secondary_agent
    db_medicament.caducity_date = medicament.caducity_date

    session.commit()

    return db_medicament

def delete_medicament(medicament_id: int):
    medicament = session.query(Medicament).get(medicament_id)

    if not medicament:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Medicament doesn't exist"
        )
    
    session.delete(medicament)
    session.commit()

    return {"detail": "Medicament deleted"}
