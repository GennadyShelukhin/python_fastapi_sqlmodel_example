from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    debug: bool
    project_name: str
    version: str
    description: str

    # App starting params
    host: str
    port: int

    # Str connect to db: f"{driver}://{name}:{password}@{host}:{port}/{db}"
    # Example: "postgresql+asyncpg://root:root@localhost:32700/qa_oss"
    # Need to use "+asyncpg". This means that sqlalchemy will use the asynchronous engine to connect to the db
    db_async_connection_str: str
