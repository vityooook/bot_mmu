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
    from database.crud.teacher import get_teachers_name

    async def smth():
        list_of_teachers = await get_teachers_name()
        text = ""
        number = 1
        for name in list_of_teachers:
            text += f"{number}. {name[0]}\n"
            number += 1
        text += "<i>\n\nИспользуй функцию поиска в чате для быстрого нахождения имени</i>"
        print(text)
    asyncio.run(smth())
