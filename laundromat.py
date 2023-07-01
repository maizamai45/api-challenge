from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/test/{number}")
async def read_root(number: int):

    if number  == 1:
        return {"mamber-count":number,
            "sequence":[0], 
            "total":0
    }
    elif number < 1 or number > 100:
        return 'json error'
    
    else:
        fibo = [0]
        fa,fb = 0,1
        for i in range(1, number):
            fa , fb  = fb, fa+fb 
            fibo.append(fa)
        return {"mamber-count":number,
            "sequence":fibo,
            "total":sum(fibo)
        }
   
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}