from fastapi import FastAPI

query_param_app = FastAPI()

dia_member_db = [{"name": "lys"},
                 {"name": "gg"},
                 {"name": "abc"},
                 {"name": "def"}]

@query_param_app.get("/members/")
async def read_mem(skip: int = 0, limit: int = 10):
    return dia_member_db[skip: skip + limit]