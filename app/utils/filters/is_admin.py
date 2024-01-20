from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin: bool):
        self.admin = admin

    async def __call__(self, message: Message) -> bool:
        return self.admin == (message.from_user.id in [user.user.id for user in await message.chat.get_administrators()])