from sqlalchemy import select
from database.engine import session
from database.models import User


async def verify_id(user_id: int):
    async with session() as s:
        stmt = select(User.user_id).where(User.user_id == user_id)
        result = await s.scalar(stmt)
        return result


async def add_user_info(
        user_id: int,
        group_id: int,
        first_name: str | None,
        last_name: str | None,
        username: str
):
    async with session() as s:
        stmt = User(
            user_id=user_id,
            group_id=group_id,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        s.add(stmt)
        await s.commit()


async def get_user_group_id(user_id: int) -> int:
    async with session() as s:
        stmt = select(User.group_id).where(User.user_id == user_id)
        result = await s.scalar(stmt)
        return result
