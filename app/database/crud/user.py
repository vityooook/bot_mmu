from sqlalchemy import select
from loguru import logger

# * import session for connection with database
from database.engine import session
# * import tables
from database.models import User


@logger.catch()
async def verify_id(user_id: int):
    """check if a student exists

    :param user_id: student id in Telegram
    :return: student id in Telegram
    """
    logger.debug("verify a student")
    async with session() as s:
        stmt = select(User.user_id).where(User.user_id == user_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch()
async def add_user_info(
        user_id: int,
        group_id: int,
        first_name: str | None,
        last_name: str | None,
        username: str
):
    """ add information about new student

    :param user_id: student id in Telegram
    :param group_id: student group id
    :param first_name: student first_name in Telegram
    :param last_name: student last_name in Telegram
    :param username: student username in Telegram
    """
    logger.debug("add student's information")
    async with session() as s:
        stmt = User(
            user_id=user_id,
            group_id=group_id,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        logger.debug(stmt)
        s.add(stmt)
        await s.commit()


@logger.catch()
async def get_user_group_id(user_id: int) -> int:
    """get student group id

    :param user_id: student id in Telegram
    :return: student group id
    """
    logger.debug("get student group id")
    async with session() as s:
        stmt = select(User.group_id).where(User.user_id == user_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch()
async def select_all_users_id() -> list:
    """get all students id for newsletter"""
    logger.debug("get all students id")
    async with session() as s:
        stmt = select(User.user_id)
        result = await s.execute(stmt)
        return result.all()

