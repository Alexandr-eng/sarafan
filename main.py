
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


     
from core.models import Base, db_helper
from core.config import settings

from items_viws import router as item_router
from users.views import router as users_router
from api_v1 import router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
       await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lefespan=lifespan)
app.include_router(product=router_v1, prefix=settings.api_v1_prefix)
app.include_router(item_router)
app.include_router(users_router)



@app.get("/")
def hello_index():
    return {
        "massage": "hello index"

    }

@app.get("/hello/")
def hello(name:str = "World"):
    name = name.strip().title()
    return {"massage": f"Hello {name}"}




