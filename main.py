from typing import Annotated
from imp import reload
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "massage": "hello index"

    }

@app.get("/hello/")
def hello(name:str = "World"):
    name = name.strip().title()
    return {"massage": f"Hello {name}"}


@app.post("/users")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.get("/items")
def list_items():
    return [
        'item1',
        'item2',
        'item3',
    ]


@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@app.get("/items/{items_id}/")
def get_item_by_id(items_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {
       "item": {
            "id": items_id,
              
         },
    }
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)


