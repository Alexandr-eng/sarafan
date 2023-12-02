from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=["Producs"])

@router.post(path="/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_product(session=session)


router.post(path="/", response_model=Product)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_dependency),

                         
):
    return await crud.create_product(session=session, product_in=product_in,)



@router.post(path="/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
    
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail= f"Product {product_id} nat found"
    )