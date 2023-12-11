from sqlalchemy import update

from database.engine import session
from database.models import Group, User


def verify_group(title: str):
    with session as s:
        stmt = s.query(Group.group_id).where(Group.title == title)
        return stmt.scalar()


def get_group_id(user_id: int) -> int:
    with session as s:
        stmt = s.query(Group.group_id).join(User, Group.name == User.group).where(User.id == user_id)
        return stmt.scalar()


def update_group(user_id: int, group_id: int):
    """UPDATE users SET group_id=:group_id WHERE users.user_id = :user_id_1"""
    with session as s:
        stmt = update(User).values(group_id=group_id).where(User.user_id == user_id)
        s.execute(stmt)
        s.commit()
