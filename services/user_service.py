# Python
from datetime import datetime
from typing import List

# FastAPI
from fastapi import HTTPException, status

# Project imports
from models.user_model import User
from schemas import user_schema
from config.db import session
from models.role import Role
from models.specialty import Specialty



def get_all_users():
    return session.query(User, Role, Specialty).filter_by(role_id=Role.id, specialty_id=Specialty.id).all()

def create_user(user: user_schema.UserLogin):
    get_user = session.query(User).filter_by(email=user.email, rut=user.rut ).first()
    print(get_user)
    if get_user:
        message =  "Email already registered"
        if get_user.rut == user.rut:
            message = "Rut already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= message
        )

    db_user = User(
        email = user.email,
        rut = user.rut,
        first_name = user.first_name,
        second_name = user.second_name,
        last_name = user.last_name,
        second_last_name = user.second_last_name,
        created_at = datetime.now(),
        password = user.password,
        role_id = user.role_id,
        specialty_id = user.specialty_id
    )

    session.add(db_user)
    session.commit()
    
    return user_schema.User(
        id = db_user.id,
        email = db_user.email,
        rut = db_user.rut,
        first_name = db_user.first_name,
        second_name = db_user.second_name,
        last_name = db_user.last_name,
        second_last_name= db_user.second_last_name,
        created_at = db_user.created_at,
        role_id = db_user.role_id,
        specialty_id = db_user.specialty_id
    )

def login_user(user: user_schema.UserLoginFront):
    user = session.query(User).filter_by(rut=user.rut, password=user.password).first()
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or password incorrect"
        )

    return user

def get_an_user(rut: str):
    user = session.query(User).filter_by(rut=rut).one()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )
    return user

def update_user(rut: str, user: User):
    db_user = session.query(User).filter_by(rut=rut).one()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )

    db_user.first_name = user.first_name
    db_user.second_name = user.second_name
    db_user.last_name = user.last_name
    db_user.second_last_name = user.second_last_name
    db_user.rut = user.rut
    db_user.email = user.email
    db_user.role_id = user.role_id
    db_user.specialty_id = user.specialty_id

    session.commit()
    
    return db_user

def delete_user(rut: str):
    user = session.query(User).filter_by(rut=rut).one()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )
    
    session.delete(user)
    session.commit()

    return {"detail": "User deleted"}