from pydantic import BaseModel
class userCreate(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
    status: str


    #this define what data the user will send