from fastapi import FastAPI

app = FastAPI()

vitrina = [
    {"одежда", "обувь", "головные уборы", "термобелье"}
]

@app.get("/")
def hello():
    return "hello"


