from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# address domain/path - endpont
# GET
# POST
# UPDATE
# DELETE

items = {
    1: {
        "title": "Welcome to TodoApp!",
        "description": "To get started, complete this task",
        "completed": False

    }
}


@app.get("/")
def index():
    return {"Data": "Hello world!"}


# path parameter
# domain/get-student/1
@app.get("/get-item/{id}")
def get_item(id: int = Path(description="The ID of item that you want to see")):
    return items[id]


class User(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    email: str
    password: str


class Item(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool


class UpdateItem(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# POST method
@app.post("/create-item/{item_id}")
def add_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "item id  exist"}
    items[item_id] = item
    return items[item_id]


# PUT method
@app.put("/update-item/{item-id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {"error": "item id doesn't exist"}
    if item.title!= None:
        items[item_id].title = item.title
    if item.description != None:
        items[item_id].description = item.description
    if item.completed != None:
        items[item_id].completed = item.completed

    return items[item_id]


# DELETE method
@app.delete("/delete-item/{item-id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "item id doesn't exist"}
    del items[item_id]
    return {"data": "item deleted successfully"}
