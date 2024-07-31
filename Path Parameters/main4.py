from enum import Enum
from fastapi import FastAPI

lysapp = FastAPI()

class Animal(str, Enum):
    cat = "cat"
    dog = "dog"
    lion = "lion"
    tiger = "tiger"

@lysapp.get("/animals/{animal_name}")
async def getanimal(animal: Animal):
    # 열거형 멤버 비교
    if animal == Animal.cat:
        return {"animal_name": animal, "type": "goyang-i"}
    # 열거형 값 가져오기
    if animal.value == "dog":
        return {"animal_name": animal, "type": "gae"}
    # 열거형 멤버 반환
    return {"animal_name": animal, "type": "tiger | lion"}