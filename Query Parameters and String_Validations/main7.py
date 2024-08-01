from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(q: Optional[str] = Query(None,
                                              title="Query string",
                                              description="Query string is for the items to search in the database that have a good match",
                                              min_length=3)
):
    
    results = {"items": [{"item_id": "lys"},
                         {"item_id": "lsy"}]}
    
    if q:
        results.update({"q": q})

    return results