from aiogram import F
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data import db
from loader import dp


@dp.message(Command('test'))
async def test_message(msg: Message):
    await msg.answer('test is working')