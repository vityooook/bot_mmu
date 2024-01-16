from sqlalchemy.sql.expression import func
from sqlalchemy import select
from loguru import logger

# * import session for connection with database
from database.engine import session
# * import tables
from database.models import Quality, Teacher, Rating


@logger.catch(level="INFO", message="verify name of teacher")
async def verify_teacher(name: str):
    """check if a teacher exist

        :param name: name of teacher

        :return: teacher's id
        """
    async with session() as s:
        stmt = select(Teacher.teacher_id).where(Teacher.name == name)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch(level="INFO", message="check student's review")
async def verify_feedback(user_id: int, teacher_id: int):
    """checking whether the student left a review about this teacher

    :param user_id: student id in Telegram
    :param teacher_id: teacher's id

    :return: teacher's id from Rating table
    """
    async with session() as s:
        stmt = select(Rating.teacher_id) \
            .where((Rating.user_id == user_id) & (Rating.teacher_id == teacher_id)).limit(1)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch(level="INFO", message="get name of teacher")
async def get_teacher_name(teacher_id: int):
    """get the teacher's name using id

    :param teacher_id: teacher's id
    :return: teacher's name
    """
    async with session() as s:
        stmt = select(Teacher.name).where(Teacher.teacher_id == teacher_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch(level="INFO", message="get qualification of teacher")
async def get_teacher_subject(teacher_id: int):
    """get the teacher's qualification using id

        :param teacher_id: teacher's id
        :return: teacher's qualification
        """
    async with session() as s:
        stmt = select(Teacher.subject).where(Teacher.teacher_id == teacher_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch(level="INFO", message="get the teacher's rating")
async def get_rating(teacher_id: int):
    """calculation the teacher's rating

    :param teacher_id: teacher's id
    :return: five average ratings about the teacher
    """
    async with session() as s:
        stmt = select(Quality.quality, func.round(func.avg(Rating.mark), 1)).\
            select_from(Rating).join(Quality, Quality.quality_id == Rating.quality_id).\
            group_by(Quality.quality).where(Rating.teacher_id == teacher_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.all()


@logger.catch(level="INFO", message="get the teacher's average rating")
async def get_avg_rating(teacher_id: int):
    """calculation the teacher's average rating

        :param teacher_id: teacher's id
        :return: one main average rating about the teacher
        """
    async with session() as s:
        stmt = select(func.round(func.avg(Rating.mark), 1)).\
            where(Rating.teacher_id == teacher_id)
        logger.debug(stmt)
        result = await s.execute(stmt)
        return result.scalar()


@logger.catch(level="INFO", message="add reviews to the database")
async def add_rating(teacher_id: int, user_id: int, marks: list):
    """add reviews to the database

    :param teacher_id: teacher's id
    :param user_id: student id in Telegram
    :param marks: marls from one to five
    """
    async with session() as s:
        for mark in marks:
            stmt = Rating(
                teacher_id=teacher_id, user_id=user_id,
                quality_id=mark["question"], mark=mark["mark"]
            )
            logger.debug(stmt)
            s.add(stmt)
        await s.commit()
