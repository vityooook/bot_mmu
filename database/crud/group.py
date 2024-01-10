from sqlalchemy import select, update
from database.engine import session
from database.models import User, Group


async def verify_group(title: str):
    async with session() as s:
        stmt = select(Group.group_id).where(Group.title == title)
        result = await s.execute(stmt)
        return result.scalar()


async def update_group(user_id: int, group_id: int):
    """UPDATE users SET group_id=:group_id WHERE users.user_id = :user_id_1"""
    async with session() as s:
        stmt = update(User).values(group_id=group_id).where(User.user_id == user_id)
        await s.execute(stmt)
