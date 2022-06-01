# python_fastapi_sqlmodel_example

## Test project. REST API, using Python 3.10.2, Fastapi, SQLModel, SQLAlchemy.

## This is my first test project on these technologies. Correctness and performance is not guaranteed.

### Resources Used:

* https://medium.com/@estretyakov/the-ultimate-async-setup-fastapi-sqlmodel-alembic-pytest-ae5cdcfed3d4
* https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/
* https://www.cosmicpython.com/book/chapter_02_repository.html

### Before using:

* Create virtual env
* Install requirements: ```poetry install```
* Create .env file (check example.env) or change ```app/__init__.py``` file

### Run Postgres DB:

```
docker-compose -f docker-compose.dev.yaml up
```

### Make auto migrations:

```
alembic revision --autogenerate -m “add_shop_and_product”
```
```
alembic upgrade head
```

### Run server:
For debugging start the server from ```app/main.py```

### You can open swagger (use port from .env):
```
http://localhost:8081/docs
```