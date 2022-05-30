# Python
from typing import List, Dict
import json

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body, Path, Query, Form

# Project imports
from schemas.user_schema import UserBase, UserLogin, User, UserLoginFront
from config.db import get_db
from services.user_service import create_user, login_user



user_routes = APIRouter()

@user_routes.get(
    path="/users",
    tags=["users"],
    #response_model = List[User],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get all users"
)
def get_users():
    """
    This path parameter shows all users in the app

    Args:
    -

    Returns a json with all users in the app with the following keys.
        - id: int
        - email: EmailStr
        - rut: str
        - first_name: str
        - second_name: str
        - last_name: str
        - second_last_name: str
        - created_at: datetime
        - role_id: int
        - specialty_id: int
    """
    return {"Helo": "world"}

@user_routes.post(
    path="/users",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model= User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
async def post_user(user: UserLogin):
    """Create a new user in the app.

    Args:
        The app can recive next fields into a JSON
        - email: str
        - rut: str
        - first_name: str
        - second_name: Optiona[str]
        - last_name: str
        - second_last_name: str
        - password: str

    ###Returns:
        -user: User info
    """
    print(type(user))
    return create_user(user)

@user_routes.post(
    path="/login",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Sign in in the app"
)
async def login(user: UserLoginFront):
    return login_user(user)

@user_routes.get("/users")
def helloWorld():
    return "Hello World"

@user_routes.get("/users")
def helloWorld():
    return "Hello World"