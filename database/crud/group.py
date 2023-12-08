from sqlalchemy import select, exists

from database.engine import session
from database.models import Group, User


def verify_group(name: str):
    with session as s:
        stmt = s.query(Group.id).where(Group.name == name)
        return stmt.scalar()


def get_group_id(user_id: int) -> int:
    with session as s:
        stmt = s.query(Group.id).join(User, Group.name == User.group).where(User.id == user_id)
        return stmt.scalar()

