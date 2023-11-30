from aiogram import Router, F
from aiogram.types import CallbackQuery

from utils.callback_data import MenuCallback
from .inline_menu_teacher import InlineMenuTeacher


router = Router()


@router.callback_query(MenuCallback.filter(F.act == "teacher_rating"))
async def teacher_rating(query: CallbackQuery):
    await query.message.edit_text(
        text="меню рейтинга преподователей:",
        reply_markup= await InlineMenuTeacher().menu()
    )

