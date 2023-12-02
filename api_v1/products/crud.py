from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from schemas import ProductCreate


async def get_products(session: AsyncSession)->[Product]:
    stat = select(Product).order_by(Product.id)
    result: Result = await session.execute(stat)
    products = result.scalars().all()
    
    
    return list(products)



async def get_product(session: AsyncSession, product_id: int) ->Product | None:
    return await session.get(Product, product_id)



async def create_product(session: AsyncSession, product_in: ProductCreate) ->Product:
    product = Product(**product_in.model.dump())
    session.add(product)
    await session.commit
    #await session.refresh(product)
    return product