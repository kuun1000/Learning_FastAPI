from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel



class User(BaseModel):
    age: int
    name: str
    lys: Optional[bool] = None



app = FastAPI()

@app.get("/")
def read_root():
    return {"I am": "LYS!!!"}

@app.get("/user/{user_id}")
def read_item(user_id: int, name: Optional[str] = None):
    return {"user_id": user_id, "name": name}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_name": user.name, "user_id": user_id}