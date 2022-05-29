# Python
from datetime import datetime

# FastAPI
from fastapi import HTTPException, status

# Project imports
from models.user_model import User
from schemas import user_schema
from config.db import session

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