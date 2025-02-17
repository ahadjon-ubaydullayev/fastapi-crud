from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

items_db = [
{
  "id": 1,
  "name": "item1",
  "description": "some text",
  "price": 10
},
{
  "id": 2,
  "name": "item2",
  "description": "some text",
  "price": 20
}
]

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# Simple function to test server
@app.get("/")
async def root():
    return {"message":"Hello FastAPI!"}

# Funtion to create new item
@app.post("/items/", response_model=Item)
def create_item(item:Item):
    items_db.append(item)
    return item


# Funtion to get all the items
@app.get("/items/", response_model=List[Item])
def get_items():
    print(items_db)
    return items_db


# funtion to get item details
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error":"Item not found."}



# function to update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id:int, updated_item: Item):
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db[i] = updated_item
            print(updated_item)
            return updated_item
    return {"error":"Item not found"}
            

# function to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    global items_db
    items_db = [item for item in items_db if item["id"] != item_id]
    return {"message":"Item deleted!"}