import uuid
from fastapi import APIRouter, HTTPException, Header
from passlib.context import CryptContext

# from schemas import userCreate
# from database import get_connection

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

sessions = {}

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.varify(
        password,
        hashed
    )

def create_token():
    return str(uuid.uuid4())

def get_current_user(
        authorization: str = Header(None)
):
    
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="token missing"
        )
    token = authorization.replace(
        "bearer",
        ""
    )

    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )
    return sessions[token]