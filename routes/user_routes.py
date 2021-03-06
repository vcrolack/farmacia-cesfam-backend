# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

# Project imports
from schemas.user_schema import UserLogin, User, UserLoginFront, GetUser
from config.db import get_db
from services.user_service import create_user, login_user, get_all_users, get_an_user, update_user, delete_user



user_routes = APIRouter()

@user_routes.get(
    path="/users",
    tags=["users"],

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
    users = get_all_users()
    return users

@user_routes.get(
    path="/users/{rut}",
    tags=["users"],
    response_model = GetUser,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Get an user"
)
def get_user(rut: str):
    return get_an_user(rut)

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

@user_routes.put(
    path="/users/{rut}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=User,
    dependencies=[Depends(get_db)],
    summary="Update an user"
)
def update_an_user(rut: str, user: User):
    return update_user(rut, user)

@user_routes.delete(
    path="/users/{rut}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete an user"
)
def delete_an_user(rut: str):
    return delete_user(rut)
