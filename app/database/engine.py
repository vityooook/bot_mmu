from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
# * import key for postgresql
from config import DB_LINK

# * connecting to postgresql
engine = create_async_engine(DB_LINK, echo=False, pool_pre_ping=False, future=True)
# * open session
session = async_sessionmaker(engine, expire_on_commit=False)
# * declare tables
Base = declarative_base()


# async def proceed_schemas() -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# if __name__ == "__main__":
#     import asyncio
#     from database.crud.user import select_all_users_id
#
#     async def smth():
#         stmt = await select_all_users_id()
#         print(stmt)
#
#     asyncio.run(smth())
