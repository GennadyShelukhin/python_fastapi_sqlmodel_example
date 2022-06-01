from fastapi import APIRouter, Depends, Query
from app.repositories.shop import ShopRepository
from app.models.shop import Shop, ShopCreate, ShopGet
from app.endpoints.depends import get_shop_repository


router = APIRouter()


@router.get("/get_by_name", response_model=ShopGet)
async def get_by_name(
        name: str = Query(description="Shop name"),
        shop: ShopRepository = Depends(get_shop_repository)):
    return await shop.get_by_name(name=name)


@router.get("/get_by_id", response_model=ShopGet)
async def get_by_id(
        shop_id: int = Query(description="Shop ID"),
        shop: ShopRepository = Depends(get_shop_repository)):
    return await shop.get_by_id(shop_id=shop_id)


@router.post("/create", response_model=Shop)
async def create(
        name: str = Query(description="Shop name"),
        shop: ShopRepository = Depends(get_shop_repository)):
    return await shop.create(shop=ShopCreate(name=name))
