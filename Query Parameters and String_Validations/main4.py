from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query("MyprojectIsDia", min_length=3)):
    results = {"items": [{"item_id": "lys"},
                         {"item_id": "lsy"}]}
    
    if q:
        results.update({"q": q})

    return results