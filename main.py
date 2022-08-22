from typing import Union
import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


url = 'https://62f7acbd73b79d01535c4dc7.mockapi.io/naim/items'

@app.get("/")
def read_root():
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    response = requests.get(url=url + '/' + str(item_id))
    #return {"item_id": item_id, "q": q}
    return {"items": response.json() }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    response = requests.put(url=url , data=item.json())
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
def save_item(item: Item):
    print(item.json())
    response = requests.post(url, item.json(), timeout=5)

@app.delete("/items/")
def delete_item():
    print("Va a borrar: ")
    response = requests.delete(url)
    return {"items": response.json()}