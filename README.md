จากที่โทชจทย์ให้มา ผมได้ใช้ python Fast  APL
python  3.10
pip install fastapi
pip install "uvicorn[standard]"

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


uvicorn laundromat:app --reload (คำสั่งรัน)

////////////////////////////////////////////////////////////////
@app.get("/api/v1/test/{number}")
async def read_root(number: int):
จากโค้ดผมระบุRoute /api/v1/test/{number} เป็นการเข้าลิ้งค์ ตรงnumber เป็นการระบุตัวเล

 elif number < 1 or number > 100:
        return 'json error'
    เป็นการบอกว่าถ้า numberน้อยกว่า หรือมากกว่า 100 แสดง json error


