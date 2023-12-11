from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from utils.filters import ChatTypeFilter
from database import crud


router = Router()


@router.message(Command(commands=['schedule']),
                ChatTypeFilter(chat_type=["group", "supergroup"]))
async def scheulde_chat(message: Message):
    print(crud.chat.get_group_id(-4071362367))
