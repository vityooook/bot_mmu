from sqlalchemy.sql.expression import func

from database.engine import session
from database.models import Quality, Teacher, Rating


def verify_teacher(name: str):
    with session as s:
        stmt = s.query(Teacher.teacher_id).where(Teacher.name == name)
        return stmt.scalar()


def verify_feedback(user_id: int, teacher_id: int):
    with session as s:
        stmt = s.query(Rating.teacher_id).where((Rating.user_id == user_id) &
                                                (Rating.teacher_id == teacher_id)).limit(1)
        return stmt.scalar()


def get_teacher_name(teacher_id: int):
    with session as s:
        stmt = s.query(Teacher.name).where(Teacher.teacher_id == teacher_id)
        return stmt.scalar()


def get_teacher_subject(teacher_id: int):
    with session as s:
        stmt = s.query(Teacher.subject).where(Teacher.teacher_id == teacher_id)
        return stmt.scalar()

def get_rating(teacher_id: int):
    """
    SELECT quality.quality AS quality_quality, round(avg(rating.mark), 1) AS round_1
    FROM rating JOIN quality ON quality.quality_id = rating.quality_id
    WHERE rating.teacher_id = <teacher_id> GROUP BY rating.quality_id
    """
    with session as s:
        stmt = s.query(Quality.quality, func.round(func.avg(Rating.mark), 1)).\
            select_from(Rating).join(Quality, Quality.quality_id == Rating.quality_id).\
            group_by(Rating.quality_id).where(Rating.teacher_id == teacher_id)
        return stmt.all()


def get_avg_rating(teacher_id: int):
    """
    SELECT round(avg(rating.mark), 1) AS round_1
    FROM rating
    WHERE rating.teacher_id = ?
    """
    with session as s:
        stmt = s.query(func.round(func.avg(Rating.mark), 1)).\
            where(Rating.teacher_id == teacher_id)
        return stmt.scalar()


def add_rating(teacher_id: int, user_id: int, marks: list):
    with session as s:
        for mark in marks:
            stmt = Rating(
                teacher_id=teacher_id, user_id=user_id,
                quality_id=mark["question"], mark=mark["mark"]
            )
            s.add(stmt)
        s.commit()
