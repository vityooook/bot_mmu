from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()

@router.message(F.text == 'главное меню')
async def delete(msg: Message):
    await msg.delete()