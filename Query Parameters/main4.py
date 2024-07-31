from typing import Optional
from fastapi import FastAPI

query_param_app = FastAPI()

@query_param_app.get("/members/{member_name}/items/{item_id}")
async def readmemmulti(member_name: str, item_id: str, query: Optional[str] = None, islys: bool = False):
    name = {"member_name": member_name, "have item_id": item_id}

    if query:
        name.update({"query": query})
    
    if not islys:
        name.update(
            {"description": "islys is false. Where is lys?"}
        )
    
    return name