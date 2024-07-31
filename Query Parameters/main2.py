from typing import Optional
from fastapi import FastAPI

query_param_app = FastAPI()

@query_param_app.get("/members/{member_name}")
async def read_onemem(member_name: str, member_age: Optional[int] = None):
    if (member_age):
        return {"name": member_name, "age": member_age}
    return {"name": member_name}