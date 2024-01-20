from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.utils.filters import ChatTypeFilter, IsAdmin
from database import crud


router = Router()

class Chatinfo(StatesGroup):
    user_group = State()
    schedule = State()


@router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), 
                CommandStart(), IsAdmin(admin=True))
async def start_group(message: Message, state: FSMContext):
    if not crud.chat.verify_chat(message.chat.id):
        await message.answer("Напишите вашу группу")
        await state.set_state(Chatinfo.user_group)
    else:
        await message.answer('Чат уже настроен!')


@router.message(Chatinfo.user_group, 
                ChatTypeFilter(chat_type=["group", "supergroup"]), 
                IsAdmin(admin=True))
async def set_group(message: Message, state: FSMContext):
    if await str.database.crud.group.verify_group(message.text.upper()):
        
        crud.chat.add_chat_info(message.chat.id, message.from_user.id, message.text.upper())
        await message.answer("спасибо, все супер\nтеперь ты можешь получить расписание")
        await state.clear()
    
    else:
        await message.answer('такой группы нету')
