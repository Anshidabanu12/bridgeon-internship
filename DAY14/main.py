from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class loginRequest(BaseModel):
    email: str 
    password: str

@app.post("/auth/login")
def login(data: loginRequest):

    if(
        data.email == "anshida@gmail.com"
        and data.password == "12345"
    ):
        return{
            "token": "abc123"
        }
    raise HTTPException(
        status_code=401,
        detail="invalid email or password"
    )