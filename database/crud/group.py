from sqlalchemy import select, exists

from database.engine import session
from database.models import Group, User


def verify_group(name: str):
    with session as s:
        stmt = s.query(Group.group_id).where(Group.name == name)
        return stmt.scalar()


# def get_group_id(user_id: int) -> int:
#     with session as s:
#         stmt = s.query(Group.group_id).join(User, Group.group_id == User.group_id).where(User.user_id == user_id)
#         return stmt.scalar()

