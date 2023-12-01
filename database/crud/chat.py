from database.engine import session
from database.models import ChatGroup, Group


def verify_chat(chat_id: int):
    with session as s:
        stmt = s.query(ChatGroup.name).where(ChatGroup.chat_id == chat_id)
        return stmt.scalar()


def add_chat_info(chat_id: int, time_schedule: str, name: str):
    with session as s:
        stmt = ChatGroup(chat_id=chat_id, name=name, time_schedule=time_schedule)
        s.add(stmt)
        s.commit()

def get_group_id(chat_id: int) -> int:
    with session as s:
        stmt = s.query(Group.id).join(ChatGroup, Group.name == ChatGroup.name).where(ChatGroup.chat_id == chat_id)
        return stmt.scalar()