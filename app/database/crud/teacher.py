from sqlalchemy.sql.expression import func
from sqlalchemy import select
from loguru import logger

# * import session for connection with database
from database.engine import session
# * import tables
from database.models import Teacher


@logger.catch()
async def get_teachers_name():
    """Get the names of all teachers


        :return: teachers name
        """
    logger.debug("verify name of teacher")
    async with session() as s:
        stmt = select(Teacher.name).order_by(Teacher.name)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.all()
