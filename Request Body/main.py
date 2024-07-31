from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    # None을 명시하지 않는 key에 대해서는 value를 필수로 받아야 함
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



app = FastAPI()



@app.post("/items/")
async def create_item(item: Item):
    return item