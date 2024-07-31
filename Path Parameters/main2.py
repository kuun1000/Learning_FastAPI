from fastapi import FastAPI

lysapp = FastAPI()

@lysapp.get("/computers/{computer_id}")
async def read_com(computer_id: int):   # 타입이 있는 매개변수
    return {"computer_id": computer_id}