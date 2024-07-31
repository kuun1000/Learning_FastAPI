from fastapi import FastAPI

lysapp = FastAPI()

# 상황1: 구체적인 경로 파라미터를 먼저 선언
@lysapp.get("/computers/lyscom")
async def read_comlys():
    return {"lys computer"}

@lysapp.get("/computers/{computer_name}")
async def read_com(computer_name: str):
    return {"computer_name": computer_name}