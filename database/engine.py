from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import DB_LINK


engine = create_async_engine(DB_LINK, echo=False, pool_pre_ping=False, future=True)
session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()


# async def proceed_schemas() -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# if __name__ == "__main__":
#     from database.crud.rating import get_rating
#
#     async def smth():
#         stmt = await get_rating(teacher_id=66)
#         print(stmt)
#
#     asyncio.run(smth())
