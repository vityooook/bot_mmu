from aiogram import Router, F
from aiogram.types import Message

from keyboard.inline.inline_menu import InlineMenu
router = Router()


@router.message(F.text == 'ℹ️ Показать меню')
async def menu(msg: Message):
    await msg.answer("МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
                     reply_markup=await InlineMenu().menu())

