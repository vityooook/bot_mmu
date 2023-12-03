from sqlalchemy import select

from database.engine import session
from database.models import User


def verify_id(user_id: int):
    with session as s:
        stmt = s.query(User).where(User.user_id == user_id)
        return stmt.scalar()


def add_user_info(user_id: int, group_id: int, first_name: str | None,
                  last_name: str | None, username: str):
    with session as s:
        stmt = User(user_id=user_id, group_id=group_id, first_name=first_name,
                    last_name=last_name, username=username)
        s.add(stmt)
        s.commit()


def get_user_group_id(user_id: int) -> int:
    with session as s:
        stmt = s.query(User.group_id).where(User.user_id == user_id)
        return stmt.scalar()
