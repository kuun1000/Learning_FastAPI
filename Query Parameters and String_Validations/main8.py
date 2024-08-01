from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "lys"},
                         {"item_id": "lsy"}]}
    
    if q:
        results.update({"q": q})

    return results