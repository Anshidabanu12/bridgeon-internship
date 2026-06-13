from fastapi import APIRouter, HTTPException

from models import User, Login
from database import users_db, tasks_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(user: User):

    if user.username in users_db:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    users_db[user.username] = {
        "email": user.email,
        "password": user.password
    }

    tasks_db[user.username] = []

    return {
        "message": "Registration Successful"
    }


@router.post("/login")
def login(data: Login):

    if data.username not in users_db:
        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if users_db[data.username]["password"] != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    return {
        "message": "Login Successful",
        "username": data.username
    }