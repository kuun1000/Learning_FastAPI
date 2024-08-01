from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}

    return query_items

# # 기본값 지정
# @app.get("/items/")
# async def read_items(q: Optional[List[str]] = Query(default=["test", "lys"])):
#     query_items = {"q": q}

#     return query_items