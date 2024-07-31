from fastapi import FastAPI

app = FastAPI() # FastAPI 인스턴스 생성

@app.get("/")   # 경로
def read_root():    # 경로 동작 함수 정의
    return {"Im": "lys first_step!!"}   # 콘텐츠 반환