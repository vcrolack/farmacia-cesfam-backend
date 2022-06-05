# Python
from datetime import datetime
from typing import List

# FastAPI
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

# SQLAlchemy


# Project imports
from models.user_model import User
from schemas import user_schema
from config.db import session



def get_all_users() -> List[User]:
    return session.query(User).all()

def create_user(user: user_schema.UserLogin):

    #get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.rut == user.rut)).first()
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

def get_an_user(user_id):
    user = session.query(User).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )
    print(user_id)
    return user

def update_user(user_id: int, user: User):
    db_user = session.query(User).get(user_id)
    if not user:
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

def delete_user(user_id: int):
    user = session.query(User).get(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )
    
    session.delete(user)
    session.commit()

    return {"detail": "User deleted"}