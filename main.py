from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# address domain/path - endpont
# GET
# POST
# UPDATE
# DELETE
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


#default page
@app.get("/")
def index():
    return {"Data": "Hello world!"}

#query parameter to get items
@app.get("/get-item-query")
def get_item(id: int = Query(..., description="The ID of item that you want to see")):
    return items[id]
#query paramter to get users
@app.get("/get-user-query")
def get_user(id: int = Query(..., description="The ID of user that you want to see")):
    return users[id]


# path parameter to get items

@app.get("/get-item/{id}")
def get_item(id: int = Path(description="The ID of item that you want to see")):
    return items[id]
#path parameter to get users
@app.get("/get-user/{id}")
def get_user(id: int = Path(description="The ID of user that you want to see")):
    return users[id]




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

items = {
    1:Item(title="Buy groceries",description="Milk, bread, eggs, and cheese",completed=False),
    2:Item(title="Clean the house",description="Vacuum the carpets, mop the floors, and dust the furniture",completed=False),
    3:Item(title="Finish homework",description="Read chapter 5, complete exercises 1-10, and submit by Friday",completed=True)
}


users = {
    1:User(email="alvena35@yahoo.com",password="6P3veEWX0fB44bJ"),
    2:User(email="furman_will@yahoo.com",password="rUBeUYSOgwWyWDO"),
    3:User(email="peter.hills@gmail.com",password="misjZwVzLVyuyVy")
}