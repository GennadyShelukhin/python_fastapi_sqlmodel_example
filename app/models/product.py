from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from shop import Shop


class ProductBase(SQLModel):
    name: Optional[str] = None
    shop_id: int = Field(default=None, foreign_key="shop.id")


class Product(ProductBase, table=True):

    __tablename__ = "product"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    shop: Optional["Shop"] = Relationship(back_populates="products")


class ProductRead(ProductBase):
    id: int


class ProductCreate(ProductBase):
    pass
