from typing import Optional
from fastapi import FastAPI

query_param_app = FastAPI()

@query_param_app.get("/members/{member_name}")
async def readmembool(member_name: str, query: Optional[str] = None, islys: bool = False):
    name = {"member_name": member_name}
    
    if query:
        name.update({"query": query})
    if not islys:
        name.update(
            {"description": "islys is false. Where is lys?"}
        )
    return name