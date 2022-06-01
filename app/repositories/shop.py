from typing import Optional

from sqlalchemy.future import select
from app.models.shop import Shop, ShopCreate, ShopGet
from app.repositories.base import BaseRepository


class ShopRepository(BaseRepository):

    async def create(self, shop: ShopCreate) -> Optional[Shop]:
        db_shop = Shop.from_orm(shop)
        self.session.add(db_shop)
        await self.session.commit()
        await self.session.refresh(db_shop)
        return db_shop

    async def get_by_name(self, name: str) -> Optional[Shop]:
        query = select(Shop).where(Shop.name == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_id(self, shop_id: int) -> Optional[ShopGet]:
        result = await self.session.get(Shop, int(shop_id))
        return result
