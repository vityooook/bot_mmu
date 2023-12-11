from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboard.inline.menu.inline_menu import InlineMenu


router = Router()


@router.message(F.text == 'ℹ️ Показать меню')
async def menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(
        "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
        reply_markup=await InlineMenu().menu()
    )

