from database.engine import Database
from database.models import User


def id_check(user_id: int):
    stmt = Database().session.query(User).where(id=user_id).one()
    print(stmt)
