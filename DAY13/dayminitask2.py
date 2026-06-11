from fastapi import FastAPI,  httpexception, header, depants
from pydantic import BaseModel
from  passlib.context import cryptcontext
import sqlite3
import uuid
app = FastAPI()

pwd_context = cryptcontext(schema = ["bcrpt"])

sessions = {}

conn = sqlite3.connect("app.db")
cursor = conn.coursor()
cursor.execute(""""CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT UIQUE,
               hashed_password TEXT
               )
               """)
conn.commit()

class  user(BaseModel):
    email: str
    password: str

#registraction 
@app.post("auth/register")
def register(user:user):

  cursor.execute("SELECT * FROM users WHERE email=?",
               (user.email,)
)

if cursor.fetchone():
   raise HTTP
