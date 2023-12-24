from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import DB_LINK


engine = create_async_engine(DB_LINK, echo=True, pool_pre_ping=True, future=True)
session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()


# async def proceed_schemas() -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

