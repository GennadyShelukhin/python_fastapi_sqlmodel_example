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
    # products: List["ProductRead"] = []
    """
    ------------------------------------------------------------------------------------------------------
    Problem №1:
    Exception `TypeError: issubclass() arg 1 must be a class` occurs when open swagger if make annotation:
    products: List["ProductRead"] = []
    Error occurs when using TYPE_CHECKING in import
    
    ------------------------------------------------------------------------------------------------------
    Problem №2:
    Endpoint shop/get_by_id always return empty product list
    Expected that endpoint return products if it in db.
    I use Relationship(), docs: https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/
    
    Preconditions:
    * shop with id=1
    * 2 products with shop_id=1
    
    Steps:
    * Call http://0.0.0.0:8081/shop/get_by_id?shop_id=1
    
    Actual result:
    {
      "name": "Adidas",
      "id": 1,
      "is_main": true,
      "products": []
    }
    
    Expected result:
    {
      "name": "Adidas",
      "id": 1,
      "is_main": true,
      "products": [
        {
          "id": 1,
          "name": "sneakers",
          "shop_id": 1
        },
        {
          "id": 2,
          "name": "T-shirt",
          "shop_id": 1
        }
      ]
    }
    ------------------------------------------------------------------------------------------------------
    """
    is_main: bool = True


class ShopCreate(ShopBase):
    pass
