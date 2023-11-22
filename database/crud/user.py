from sqlalchemy import select

from database.engine import session
from database.models import User


def verify_id(user_id: int):
    with session as s:
        stmt = s.query(User).where(User.id == user_id)
        return stmt.scalar()


def add_user_info(id: int, group: str, first_name: str | None,
                  last_name: str | None, username: str):
    with session as s:
        stmt = User(id=id, group=group, first_name=first_name,
                    last_name=last_name, username=username)
        s.add(stmt)
        s.commit()



