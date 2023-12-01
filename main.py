from imp import reload
from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get("/")
def hello_index():
    return {
        "massage": "hello index"

    }

@app.get("/items")
def list_items():
    return [
        'item1',
        'item2',
        'item3',
    ]

@app.get


@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@app.get("/items/{items_id}/")
def get_item_by_id(items_id:int):
    return {
       "item": {
            "id": items_id,
              
         },
    }
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)

