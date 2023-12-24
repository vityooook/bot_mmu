from sqlalchemy.sql.expression import func
from sqlalchemy import select

from database.engine import session
from database.models import Quality, Teacher, Rating


async def verify_teacher(name: str):
    async with session() as s:
        stmt = select(Teacher.teacher_id).where(Teacher.name == name)
        result = await s.execute(stmt)
        return result.scalar()


async def verify_feedback(user_id: int, teacher_id: int):
    async with session() as s:
        stmt = select(Rating.teacher_id) \
            .where((Rating.user_id == user_id) & (Rating.teacher_id == teacher_id)).limit(1)
        result = await s.execute(stmt)
        return result.scalar()


async def get_teacher_name(teacher_id: int):
    async with session() as s:
        stmt = select(Teacher.name).where(Teacher.teacher_id == teacher_id)
        result = await s.execute(stmt)
        return result.scalar()


async def get_teacher_subject(teacher_id: int):
    async with session() as s:
        stmt = select(Teacher.subject).where(Teacher.teacher_id == teacher_id)
        result = await s.execute(stmt)
        return result.scalar()


async def get_rating(teacher_id: int):
    """
    SELECT quality.quality AS quality_quality, round(avg(rating.mark), 1) AS round_1
    FROM rating JOIN quality ON quality.quality_id = rating.quality_id
    WHERE rating.teacher_id = <teacher_id> GROUP BY rating.quality_id
    """
    async with session() as s:
        stmt = select(Quality.quality, func.round(func.avg(Rating.mark), 1)).\
            select_from(Rating).join(Quality, Quality.quality_id == Rating.quality_id).\
            group_by(Rating.quality_id).where(Rating.teacher_id == teacher_id)
        result = await s.execute(stmt)
        return result.all()


async def get_avg_rating(teacher_id: int):
    """
    SELECT round(avg(rating.mark), 1) AS round_1
    FROM rating
    WHERE rating.teacher_id = ?
    """
    async with session() as s:
        stmt = select(func.round(func.avg(Rating.mark), 1)).\
            where(Rating.teacher_id == teacher_id)
        result = await s.execute(stmt)
        return result.scalar()


async def add_rating(teacher_id: int, user_id: int, marks: list):
    async with session() as s:
        for mark in marks:
            stmt = Rating(
                teacher_id=teacher_id, user_id=user_id,
                quality_id=mark["question"], mark=mark["mark"]
            )
            s.add(stmt)
        await s.commit()
