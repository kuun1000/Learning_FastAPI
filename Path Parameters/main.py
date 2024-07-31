from fastapi import FastAPI

lysapp = FastAPI()

@lysapp.get("/computers/{computer_id}")
async def read_com(computer_id):
    return {"computer_id": computer_id}