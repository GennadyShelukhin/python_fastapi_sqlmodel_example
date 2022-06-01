import uvicorn
from fastapi import FastAPI

from app import settings
from app.endpoints import shop, product

app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
    debug=settings.debug
)


app.include_router(shop.router, prefix="/shop", tags=["example"])
app.include_router(product.router, prefix="/product", tags=["example"])


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)
