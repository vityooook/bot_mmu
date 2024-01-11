from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from loguru import logger


from keyboard.inline.menu.inline_menu import InlineMenu


router = Router()


@logger.catch()
@router.message(F.text == 'ℹ️ Показать меню')
async def menu(msg: Message, state: FSMContext):
    logger.info("Main menu is called")
    await state.clear()
    await msg.answer(
        "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
        reply_markup=await InlineMenu().menu()
    )

