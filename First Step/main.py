from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"I am": "LYS!!!"}

@app.get("/user/{user_id}")
def read_item(user_id: int, name: Optional[str] = None):
    return {"user_id": user_id, "name": name}