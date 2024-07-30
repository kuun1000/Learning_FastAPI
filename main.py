from fastapi import FastAPI

app = FastAPI() # FastAPI 인스턴스 생성

@app.get("/")   # app에 Get 요청을 받았을 때 아래 함수 실행
async def root():   # 비동기 함수
    return {"message": "Hello World"}   # JSON 형태의 응답 반환