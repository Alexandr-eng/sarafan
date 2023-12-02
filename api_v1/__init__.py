from fastapi import APIRouter

from .products.viws import router as products_router

router = APIRouter()
router.include_router(router=products_router, prefix="/products")