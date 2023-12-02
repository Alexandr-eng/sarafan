
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn

from items_viws import router as item_router
from users.views import router as users_router

app = FastAPI()
app.include_router(item_router,)
app.include_router(users_router,)



@app.get("/")
def hello_index():
    return {
        "massage": "hello index"

    }

@app.get("/hello/")
def hello(name:str = "World"):
    name = name.strip().title()
    return {"massage": f"Hello {name}"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)


