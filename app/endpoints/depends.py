from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session
from app.repositories.shop import ShopRepository
from app.repositories.product import ProductRepository


async def get_shop_repository(session: AsyncSession = Depends(get_async_session)) -> ShopRepository:
    return ShopRepository(session=session)


async def get_product_repository(session: AsyncSession = Depends(get_async_session)) -> ProductRepository:
    return ProductRepository(session=session)
