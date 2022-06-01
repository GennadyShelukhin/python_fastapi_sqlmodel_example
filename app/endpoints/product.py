from fastapi import APIRouter, Depends, Query
from app.repositories.product import ProductRepository
from app.models.product import Product, ProductCreate
from app.endpoints.depends import get_product_repository


router = APIRouter()


@router.get("/get_by_name", response_model=Product)
async def get_by_name(
        name: str = Query(description="Product name"),
        shop: ProductRepository = Depends(get_product_repository)):
    return await shop.get_by_name(name=name)


@router.get("/get_by_id", response_model=Product)
async def get_by_id(
        product_id: int = Query(description="Product ID"),
        shop: ProductRepository = Depends(get_product_repository)):
    return await shop.get_by_id(product_id=product_id)


@router.post("/create", response_model=Product)
async def create(
        name: str = Query(description="Product name"),
        shop_id: int = Query(description="Shop ID"),
        product: ProductRepository = Depends(get_product_repository)):
    return await product.create(product=ProductCreate(name=name, shop_id=shop_id))
