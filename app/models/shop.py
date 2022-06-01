from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from app.models.product import Product, ProductRead


class ShopBase(SQLModel):
    name: Optional[str] = None


class Shop(ShopBase, table=True):

    __tablename__ = "shop"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    products: List["Product"] = Relationship(back_populates="shop")


class ShopRead(ShopBase):
    id: int


class ShopGet(ShopRead):
    products = []
    is_main: bool = True


class ShopCreate(ShopBase):
    pass
