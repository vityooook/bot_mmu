from sqlalchemy import select, update
from loguru import logger

# * import session for connection with database
from database.engine import session
# * import tables
from database.models import User, Group


@logger.catch()
async def verify_group(title: str):
    """check if the group exists

    :param title: name of student group
    :return: student's group id
    """
    logger.debug("verify name of student group")
    async with session() as s:
        stmt = select(Group.group_id).where(Group.title == title)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch()
async def update_group(user_id: int, group_id: int):
    """if a student changes his/her group, he/she can change it

    :param user_id: student id in Telegram
    :param group_id: student's group id
    """
    logger.debug("update student's group")
    async with session() as s:
        stmt = update(User).values(group_id=group_id).where(User.user_id == user_id)
        logger.debug(stmt)
        await s.execute(stmt)
        await s.commit()
