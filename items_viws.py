from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])

@router.get("")
def list_items():
    return [
        'item1',
        'item2',
        'item3',
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@router.get("/{items_id}/")
def get_item_by_id(items_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {
       "item": {
            "id": items_id,
              
         },
    }