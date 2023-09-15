from aiogram import types
from aiogram.filters.command import CommandStart
from loader import dp


@dp.message(CommandStart())
async def cmd_start_handler(msg: types.Message):
    await msg.answer('Приветик, это бот от университета МЯУ, который может скинуть расписание\!')
    # запросить данные о пользователе
    # записать из в БД
