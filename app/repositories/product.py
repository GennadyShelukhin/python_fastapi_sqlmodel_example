from typing import Optional

from sqlalchemy.future import select
from app.models.product import Product, ProductCreate
from app.repositories.base import BaseRepository


class ProductRepository(BaseRepository):

    async def create(self, product: ProductCreate) -> Optional[Product]:
        db_product = Product.from_orm(product)
        self.session.add(db_product)
        await self.session.commit()
        await self.session.refresh(db_product)
        return db_product

    async def get_by_name(self, name: str) -> Optional[Product]:
        query = select(Product).where(Product.name == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        result = await self.session.get(Product, int(product_id))
        return result
