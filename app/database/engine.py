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

# * testing requests to database
if __name__ == "__main__":
    import asyncio
    from database.crud.group import verify_group

    async def smth():
        await verify_group('sds')

    asyncio.run(smth())
