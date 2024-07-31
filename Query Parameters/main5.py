from typing import Optional
from fastapi import FastAPI

query_param_app = FastAPI()

@query_param_app.get("/members/{member_name}")
async def readmemmulti(member_name: str, islys: bool):
    member = {"name": member_name, "islys": islys}
    
    return member