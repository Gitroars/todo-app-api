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

users = {

}
@app.get("/")
def index():
    return {"Data": "Hello world!"}


# path parameter to get items

@app.get("/get-item/{id}")
def get_item(id: int = Path(description="The ID of item that you want to see")):
    return items[id]
#path parameter to get users
@app.get("/get-user/{id}")
def get_user(id: int = Path(description="The ID of user that you want to see")):
    return users[id]

#Class to initialize users
class User(BaseModel):
    email: str
    password: str

#Class to update users
class UpdateUser(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

#Class to initialize items
class Item(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool

#Class to update items
class UpdateItem(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# POST method for Items
@app.post("/create-item/{item_id}")
def add_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "item id  exist"}
    items[item_id] = item
    return items[item_id]
# POST method for Users
@app.post("/create-user/{user_id}")
def add_user(user_id: int, user: User):
    if user_id in users:
        return {"error": "item id  exist"}
    users[user_id] = user
    return users[user_id]
# PUT method for Items
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
# PUT method for Users
@app.put("/update-user/{user-id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        return {"error": "user id doesn't exist"}
    if user.email!=None:
        users[user_id].email = user.email
    if user.password!=None:
        users[user_id].password = user.password

    return users[user_id]


# DELETE method for Items
@app.delete("/delete-item/{item-id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "item id doesn't exist"}
    del items[item_id]
    return {"data": "item deleted successfully"}
# DELETE method for Users
@app.delete("/delete-user/{user-id}")
def delete_user(user_id: int):
    if user_id not in items:
        return {"error": "user id doesn't exist"}
    del users[user_id]
    return {"data": "user deleted successfully"}