from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int

# start the server :- uvicorn app:app --reload
app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": "50"
    },
    2: {
        "name": "Pepsi",
        "price": "20"
    }
}

@app.get("/")
def home():
    return {"data": "test"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"data": "not found"}

@app.post("/create-item")
def create_item(item: Item):
    inventory[len(inventory)+1] = item
    return {"data": "done"}

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404)
    del inventory[item_id]
    return {"data": "done"}

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    inventory[item_id] = item
    return {"data": "done"}
